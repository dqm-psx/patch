# Releasing a patch

Build both editions, review their README and the website preview, then publish
after the project owner's go-ahead. GitHub Releases here hold the ZIPs;
GitHub Latest selects the homepage download.

## Prepare and review

In the development checkout, prepare the release with the original Japanese BIN,
a notes JSON file, the authored README, and the website checkout. The release
tool's `prepare --help` lists the local paths and options.

Enhanced uses the builder's default features. Translation only includes the
same English translation, required technical support, and original-game fixes.
Each ZIP contains a BPS, CUE, README.txt, and BUILD.json. Game images are excluded.

Review the README text that will be packaged and the rendered local webpage.
Revise the draft README and notes or edit FAQ wording in the website checkout,
then refresh the preview. README changes repackage the existing game patches;
FAQ-only changes leave the ZIPs untouched. Gameplay changes require new builds.

The generated README appendix identifies the edition, filenames, original and
patched image checksums, and patch checksum. SHA256SUMS.txt records the final
ZIP and release.json hashes. A ZIP cannot contain its own final checksum.

## Publish

After approval, publish the reviewed bundle as a stable GitHub Release and ship
the reviewed FAQ updates to the website. Routine releases do not require a
specific PR or a separate approval in every repository. Code changes can still
use PRs normally.

Publication validates the reviewed files and hashes, uploads through an internal
GitHub draft, marks the release Latest, and verifies its assets. It never
replaces an existing published ZIP. Matching interrupted uploads can be retried.
After release, FAQ corrections are ordinary website edits and do not require
a new patch package.

## Automatic updates

The Update release information workflow runs on stable release publication,
release edits, or a manual run. It follows GitHub Latest and updates this
repository's README with verified downloads and release notes.

The homepage independently verifies the packages and renders its reviewed FAQ.
Missing explanations or invalid packages stop the website update and appear as
errors in Actions. Edition selection changes downloads, not the shared FAQ.

The homepage checks for new releases every six hours. Its build workflow can
also be run immediately from Actions. If WEBSITE_DISPATCH_TOKEN is configured
here with access to the website dispatch endpoint, the release workflow sends
an immediate patch-release notification. No additional secret is required for
the scheduled check.

## Files and archive

Each new release contains two edition ZIPs, release.json (schema version 2), and
SHA256SUMS.txt. Package names use DQM1-2-English-vVERSION-EDITION.zip, with
edition IDs enhanced and translation-only.

The catalog records notes, credits, package hashes, build records, feature IDs,
and initial feature explanations. The website maintains reviewed FAQ wording
independently. The builder chooses features; the website displays the recorded
choices.

Historical releases retain their original files and hashes. release-manifest.json
documents the older archive, with original packages and notes also retained in
Archive/ and README.txt.
