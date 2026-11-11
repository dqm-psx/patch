import copy
import hashlib
import json
import unittest

import update_release_readme as readme


class ReleaseSummaryTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {
            'schemaVersion': 2, 'version': '1.0.74', 'defaultEdition': 'enhanced',
            'sourceImage': readme.SOURCE_IMAGE,
            'notes': ['Example release.'], 'contributors': [],
            'features': [
                {'id': 'movement', 'name': 'Running', 'category': 'quality-of-life', 'requires': []},
                {'id': 'truth-gate-fix', 'name': 'Truth fix', 'category': 'bug-fix', 'requires': []},
            ],
            'faq': [
                {'id': 'movement-settings', 'section': 'quality-of-life', 'question': 'How do I run?',
                 'answerHtml': '<p>Hold R1.</p>', 'features': ['movement']},
                {'id': 'truth-gate-fix', 'section': 'bug-fixes', 'question': 'What is fixed?',
                 'answerHtml': '<p>The unfinished encounter state.</p>', 'features': ['truth-gate-fix']},
            ],
            'editions': [],
        }
        for identifier, name, features in (
                ('enhanced', 'Enhanced', ['movement', 'truth-gate-fix']),
                ('translation-only', 'Translation only', ['truth-gate-fix'])):
            stem = 'DQM1-2-English-v1.0.74-' + identifier
            self.catalog['editions'].append({
                'id': identifier, 'name': name, 'description': 'Example edition.',
                'file': stem + '.zip', 'bytes': 100, 'sha256': 'a' * 64,
                'features': features,
                'contents': [stem + '.bps', stem + '.cue', 'README.txt', 'BUILD.json'],
                'build': {'schemaVersion': 1, 'version': '1.0.74', 'edition': identifier,
                          'sourceImage': readme.SOURCE_IMAGE, 'features': features},
            })
        self.archive = {'releases': [{
            'version': '1.0.73', 'tag': 'v1.0.73',
            'file': 'DQM1-2-English-v1.0.73-public.zip',
            'bytes': 75, 'sha256': 'b' * 64,
        }]}

    def release(self, catalog=None):
        data = self.catalog if catalog is None else catalog
        raw = json.dumps(data).encode()
        tag = 'v' + data['version']
        assets = [{
            'name': 'release.json', 'id': 101, 'state': 'uploaded',
            'size': len(raw), 'digest': 'sha256:' + hashlib.sha256(raw).hexdigest(),
            'browser_download_url': f'{readme.PUBLIC}/releases/download/{tag}/release.json',
        }]
        for edition in data['editions']:
            assets.append({
                'name': edition['file'], 'state': 'uploaded',
                'size': edition['bytes'], 'digest': 'sha256:' + edition['sha256'],
                'browser_download_url': f'{readme.PUBLIC}/releases/download/{tag}/{edition["file"]}',
            })
        return {'tag_name': tag, 'draft': False, 'prerelease': False,
                'published_at': '2026-11-11T00:00:00Z', 'assets': assets}, raw

    def test_editions_render_with_pinned_downloads_and_preserve_other_readme_content(self):
        release, raw = self.release()
        data = readme.selected_release(release, self.archive, lambda identifier: raw)
        before = 'Intro\n' + readme.START + '\nOld\n' + readme.END + '\nInstall'
        result = readme.updated_readme(before, data)
        self.assertTrue(result.startswith('Intro\n'))
        self.assertTrue(result.endswith('\nInstall'))
        for edition in self.catalog['editions']:
            self.assertIn('/releases/download/v1.0.74/' + edition['file'], result)
            self.assertIn(edition['name'], result)
        self.assertNotIn('\nOld\n', result)

    def test_missing_feature_explanation_or_edition_holds_the_update(self):
        missing_faq = copy.deepcopy(self.catalog)
        missing_faq['faq'].pop()
        missing_edition = copy.deepcopy(self.catalog)
        missing_edition['editions'].pop()
        for catalog in (missing_faq, missing_edition):
            with self.subTest(catalog=catalog):
                release, raw = self.release(catalog)
                with self.assertRaises(ValueError):
                    readme.selected_release(release, self.archive, lambda identifier: raw)

    def test_mismatching_metadata_or_package_asset_is_rejected(self):
        release, raw = self.release()
        with self.assertRaisesRegex(ValueError, 'Downloaded release.json'):
            readme.selected_release(release, self.archive, lambda identifier: raw + b' ')
        release['assets'][1]['digest'] = 'sha256:' + 'c' * 64
        with self.assertRaisesRegex(ValueError, 'Release asset differs'):
            readme.selected_release(release, self.archive, lambda identifier: raw)

    def test_edition_dependencies_and_published_feature_coverage_are_required(self):
        missing_dependency = copy.deepcopy(self.catalog)
        missing_dependency['features'][0]['requires'] = ['truth-gate-fix']
        missing_dependency['editions'][0]['features'] = ['movement']
        missing_dependency['editions'][0]['build']['features'] = ['movement']
        unshipped_feature = copy.deepcopy(self.catalog)
        unshipped_feature['editions'][0]['features'] = ['truth-gate-fix']
        unshipped_feature['editions'][0]['build']['features'] = ['truth-gate-fix']
        for catalog, error in (
                (missing_dependency, 'missing required features'),
                (unshipped_feature, 'absent from both editions')):
            with self.subTest(error=error):
                release, raw = self.release(catalog)
                with self.assertRaisesRegex(ValueError, error):
                    readme.selected_release(release, self.archive, lambda identifier: raw)

    def test_draft_and_prerelease_are_rejected(self):
        for flag in ('draft', 'prerelease'):
            release, raw = self.release()
            release[flag] = True
            with self.assertRaisesRegex(ValueError, 'published stable'):
                readme.selected_release(release, self.archive, lambda identifier: raw)

    def test_unknown_release_without_metadata_is_rejected(self):
        release, _ = self.release()
        release['assets'] = []
        with self.assertRaisesRegex(ValueError, 'new release needs release.json'):
            readme.selected_release(release, self.archive, lambda identifier: self.fail('Unexpected fetch'))

    def test_known_legacy_latest_supports_rollback_without_a_catalog(self):
        old = self.archive['releases'][0]
        release = {
            'tag_name': old['tag'], 'draft': False, 'prerelease': False,
            'published_at': '2026-01-01T00:00:00Z',
            'assets': [{
                'name': old['file'], 'state': 'uploaded', 'size': old['bytes'],
                'digest': 'sha256:' + old['sha256'],
                'browser_download_url': f'{readme.PUBLIC}/releases/download/{old["tag"]}/{old["file"]}',
            }],
        }
        data = readme.selected_release(release, self.archive, lambda identifier: self.fail('Unexpected fetch'))
        result = readme.updated_readme(readme.START + 'new version' + readme.END, data)
        self.assertIn('v1.0.73', result)
        self.assertIn(old['file'], result)
        self.assertNotIn('Translation only', result)

    def test_authored_text_does_not_inject_markdown_links_or_html(self):
        data = copy.deepcopy(self.catalog)
        data['notes'] = ['<script>alert(1)</script> [link](javascript:bad)']
        result = readme.summary(data)
        self.assertNotIn('<script>', result)
        self.assertNotIn('[link]', result)
        self.assertIn('&lt;script&gt;', result)


if __name__ == '__main__':
    unittest.main()
