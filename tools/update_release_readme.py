"""Validate GitHub's published Latest release and summarize its downloads."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.parse
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'dqm-psx/patch'
API = 'https://api.github.com/repos/' + REPOSITORY
PUBLIC = 'https://github.com/' + REPOSITORY
VERSION = re.compile(r'(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2}')
HASH = re.compile(r'[a-f0-9]{64}')
MAX_METADATA_BYTES = 1_048_576
SOURCE_IMAGE = {
    'bytes': 260975568,
    'sha256': 'a1217657786430ac1c3ad71f16cdadb65d47b0df9a7e30278900651c1f1eec29',
}


class GitHubRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, url):
        target = urllib.parse.urlsplit(url)
        if target.scheme != 'https' or target.hostname not in (
                'api.github.com', 'release-assets.githubusercontent.com',
                'objects.githubusercontent.com'):
            raise ValueError('Unexpected GitHub release-asset redirect')
        redirected = super().redirect_request(request, response, code, message, headers, url)
        if target.hostname != 'api.github.com':
            redirected.remove_header('Authorization')
        return redirected


def fetch(path, accept='application/vnd.github+json'):
    headers = {
        'Accept': accept,
        'User-Agent': 'dqm-psx-release-summary',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    request = urllib.request.Request(API + path, headers=headers)
    with urllib.request.build_opener(GitHubRedirects).open(request, timeout=60) as response:
        result = response.read(MAX_METADATA_BYTES + 1)
    if len(result) > MAX_METADATA_BYTES:
        raise ValueError('Release metadata exceeds its size limit')
    return result


def single_line(value):
    if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
        raise ValueError('Expected nonempty, single-line release text')
    return value


def markdown(value):
    """Display authored text without interpreting it as links or HTML."""
    value = single_line(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return re.sub(r'([\\`*_{}\[\]|])', r'\\\1', value)


def asset_index(release):
    assets = {}
    for asset in release['assets']:
        if asset.get('state') != 'uploaded':
            continue
        if asset['name'] in assets:
            raise ValueError('Duplicate release asset')
        assets[asset['name']] = asset
    return assets


def verified_asset(assets, filename, size, digest, tag):
    if (type(size) is not int or size <= 0 or not isinstance(digest, str)
            or not HASH.fullmatch(digest)):
        raise ValueError('Invalid package byte count or SHA-256')
    asset = assets.get(filename, {})
    expected = f'{PUBLIC}/releases/download/{tag}/{filename}'
    if (asset.get('size') != size or asset.get('digest') != 'sha256:' + digest
            or asset.get('browser_download_url') != expected):
        raise ValueError('Release asset differs from its metadata: ' + filename)
    return expected


def release_catalog(release, assets, read_asset):
    manifest = assets.get('release.json')
    if not manifest:
        return None
    if (type(manifest.get('size')) is not int or not 0 < manifest['size'] <= MAX_METADATA_BYTES
            or type(manifest.get('id')) is not int or manifest['id'] <= 0
            or not isinstance(manifest.get('digest'), str)
            or not re.fullmatch(r'sha256:[a-f0-9]{64}', manifest['digest'])):
        raise ValueError('release.json needs its uploaded size and SHA-256')
    verified_asset(assets, 'release.json', manifest['size'],
                   manifest['digest'][7:], release['tag_name'])
    raw = read_asset(manifest['id'])
    if len(raw) != manifest['size'] or hashlib.sha256(raw).hexdigest() != manifest['digest'][7:]:
        raise ValueError('Downloaded release.json differs from its GitHub asset')
    data = json.loads(raw)
    version = data.get('version')
    if (data.get('schemaVersion') != 2 or not isinstance(version, str)
            or not VERSION.fullmatch(version) or release['tag_name'] != 'v' + version
            or data.get('defaultEdition') != 'enhanced'
            or data.get('sourceImage') != SOURCE_IMAGE):
        raise ValueError('Unsupported release catalog or source image')
    if not isinstance(data.get('notes'), list) or not data['notes']:
        raise ValueError('The release needs its notes')
    for note in data['notes']:
        single_line(note)
    features = data.get('features')
    faq = data.get('faq')
    if not isinstance(features, list) or not features or not isinstance(faq, list) or not faq:
        raise ValueError('The release needs feature definitions and FAQ explanations')
    feature_ids = {single_line(feature['id']) for feature in features}
    if len(feature_ids) != len(features):
        raise ValueError('Duplicate feature ID')
    for feature in features:
        single_line(feature['name'])
        if (feature.get('category') not in (
                'quality-of-life', 'restored-content', 'additional-content', 'bug-fix')
                or not isinstance(feature.get('requires'), list)
                or not set(feature['requires']) <= feature_ids):
            raise ValueError('Invalid feature category or dependencies')
    covered = set()
    answer_ids = set()
    for answer in faq:
        identifier = single_line(answer['id'])
        if identifier in answer_ids:
            raise ValueError('Duplicate FAQ ID')
        answer_ids.add(identifier)
        single_line(answer['question'])
        if (not isinstance(answer.get('answerHtml'), str) or not answer['answerHtml'].strip()
                or answer.get('section') not in (
                    'restored-content', 'quality-of-life', 'additional-content', 'bug-fixes')
                or not isinstance(answer.get('features'), list)
                or not answer['features']
                or not set(answer['features']) <= feature_ids):
            raise ValueError('Invalid FAQ answer or feature references')
        covered.update(answer['features'])
    if covered != feature_ids:
        raise ValueError('Every feature needs a FAQ explanation')
    editions = data.get('editions')
    names = {'enhanced': 'Enhanced', 'translation-only': 'Translation only'}
    if (not isinstance(editions, list) or len(editions) != 2
            or {edition.get('id') for edition in editions} != set(names)):
        raise ValueError('The release needs Enhanced and Translation only together')
    published_features = set()
    for edition in editions:
        identifier = edition['id']
        if (edition.get('name') != names[identifier]
                or edition.get('file') != f'DQM1-2-English-v{version}-{identifier}.zip'
                or not isinstance(edition.get('features'), list)
                or not set(edition['features']) <= feature_ids):
            raise ValueError('Invalid edition identity or feature selection')
        selected = set(edition['features'])
        for feature in features:
            if feature['id'] in selected and not set(feature['requires']) <= selected:
                raise ValueError('Edition is missing required features: ' + identifier)
        published_features.update(selected)
        single_line(edition['description'])
        stem = edition['file'][:-4]
        build = edition.get('build', {})
        if (edition.get('contents') != [stem + '.bps', stem + '.cue', 'README.txt', 'BUILD.json']
                or build.get('schemaVersion') != 1 or build.get('version') != version
                or build.get('edition') != identifier
                or build.get('sourceImage') != SOURCE_IMAGE
                or build.get('features') != edition['features']):
            raise ValueError('Edition package contents and build record disagree')
        verified_asset(assets, edition['file'], edition['bytes'],
                       edition['sha256'], release['tag_name'])
    if published_features != feature_ids:
        raise ValueError('Feature definitions include features absent from both editions')
    return data


def selected_release(release, archive, read_asset):
    if release.get('draft') is not False or release.get('prerelease') is not False:
        raise ValueError('Latest must be a published stable release')
    if not release.get('published_at'):
        raise ValueError('Latest release has not been published')
    assets = asset_index(release)
    catalog = release_catalog(release, assets, read_asset)
    if catalog:
        return catalog
    record = next((record for record in archive['releases']
                   if record['tag'] == release['tag_name']), None)
    if not record:
        raise ValueError('A new release needs release.json with both editions and FAQ content')
    verified_asset(assets, record['file'], record['bytes'], record['sha256'], record['tag'])
    return {
        'version': record['version'],
        'tag': record['tag'],
        'notes': record.get('notes', ['See the included README for this version’s changes and controls.']),
        'editions': [{
            'name': 'English patch', 'description': 'BPS patch, matching CUE, and release README.',
            'file': record['file'], 'bytes': record['bytes'], 'sha256': record['sha256'],
        }],
    }


def summary(data):
    version = data['version']
    tag = data.get('tag', 'v' + version)
    lines = [
        f'## Latest release — v{markdown(version)}', '',
        f'[Release notes and downloads]({PUBLIC}/releases/tag/{urllib.parse.quote(tag, safe="")})',
        '',
    ]
    checksums = []
    for edition in data['editions']:
        url = f'{PUBLIC}/releases/download/{urllib.parse.quote(tag, safe="")}/{edition["file"]}'
        lines.append(f'- **[{markdown(edition["name"])}]({url})** · '
                     f'{edition["bytes"] / 1_000_000:.2f} MB — {markdown(edition["description"])}')
        checksums.append(f'`{edition["file"]}`\n\n```text\n{edition["sha256"]}\n```')
    lines.extend(['', '### Changes', ''])
    lines.extend('- ' + markdown(note) for note in data['notes'])
    lines.extend(['', '<details>', '<summary>ZIP checksums</summary>', ''])
    lines.append('\n\n'.join(checksums))
    lines.extend(['', '</details>', ''])
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary-only', action='store_true',
                        help='Print the verified release details and append them to the Actions summary')
    args = parser.parse_args(argv)
    release = json.loads(fetch('/releases/latest'))
    archive = json.loads((ROOT / 'release-manifest.json').read_text(encoding='utf-8'))
    data = selected_release(release, archive,
                            lambda asset_id: fetch(f'/releases/assets/{asset_id}', 'application/octet-stream'))
    print('Verified GitHub Latest, v' + data['version'])
    if args.summary_only:
        rendered = summary(data)
        print(rendered)
        if destination := os.environ.get('GITHUB_STEP_SUMMARY'):
            with Path(destination).open('a', encoding='utf-8', newline='\n') as output:
                output.write(rendered + '\n')
    return data


if __name__ == '__main__':
    main()
