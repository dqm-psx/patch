# Release handoff

The development builder defines the feature presets, builds both editions, and
prepares their player-facing explanations. This repository distributes the
approved packages. The homepage uses their published metadata for its download
links, edition selector, release notes, and shared feature FAQ.

## Prepare a release

Run the development builder's preparation command with the approved version,
release notes, and the homepage checkout used for the preview.

    python prepare_release.py "<original Japanese BIN>" --version X.Y.Z --notes release-notes.json --website "<homepage checkout>" --draft

The notes file contains a nonempty notes array and a contributors array.
Preparation builds Enhanced and Translation only together. Enhanced uses the
builder's default feature set. Translation only includes English translation
support and original-game bug fixes. The source registry determines those
selections.

The preparation command produces two ZIPs, release.json, and SHA256SUMS.txt, then
creates a draft release in dqm-psx/patch. Each ZIP contains its BPS, matching CUE,
README.txt, and BUILD.json. The build record identifies the version, edition,
selected features, text and font choices, and source/output image checksums.

Review the rendered homepage preview and both packages before publishing the
draft. The first two-edition release begins with the next approved version.
Archived releases retain their original packages.

To retry uploading an already prepared bundle, use:

    python prepare_release.py --release-dir "<bundle>" --website "<homepage checkout>" --draft

Preparation keeps a feature's recorded introduction version when it reads a
previous published catalog. For offline preparation after the first catalog
release, supply that catalog using --previous-release. Draft preparation can
retrieve the published catalog automatically.

## Public release metadata

release.json is schema version 2. Its version matches the vMAJOR.MINOR.PATCH
release tag. The two edition IDs are enhanced and translation-only, displayed
as Enhanced and Translation only. Each package is named
DQM1-2-English-vVERSION-EDITION.zip.

The catalog records the original image identity, release notes, contributor
names, both package sizes and SHA-256 checksums, and both build records. Its
feature definitions provide stable IDs, names, categories, dependencies, and
known introduction versions. Its FAQ entries provide stable answer IDs,
questions, explanations, and feature references.

The main FAQ describes all released features. Selecting a download edition
changes its download information. New explanations and revisions are prepared
with the release so the website can publish them together with the packages.

The release assets are the authoritative download packages. The root
release-manifest.json documents the historical archive. README.txt and Archive/
retain the original archived release material.

## After publication

The Update release information workflow runs when a stable release is published
or edited, and can also be run manually from Actions. It queries GitHub's Latest
release so an older maintenance release cannot take over the homepage merely
because it triggered the workflow. An intentional Latest rollback is supported.

The workflow verifies the uploaded release.json against GitHub's byte count and
SHA-256, checks the two package identities against the uploaded assets, and
requires a FAQ explanation for every feature before updating the README.
The homepage performs its own full package and content validation. Incomplete
release information fails the update and reports the missing or invalid data
in Actions.

The current single-edition archive remains supported through its recorded
filenames and checksums. New releases need the complete schema version 2
catalog.

The workflow can notify dqm-psx/dqm-psx.github.io with the patch-release
repository_dispatch event. For immediate notification, configure the
WEBSITE_DISPATCH_TOKEN Actions secret in this repository using a credential
authorized for the website repository's dispatch endpoint. A fine-grained
token needs Contents write access to that website repository. The token is used
only by the notification step.

When that secret is absent, the Actions summary explains that the website's
scheduled check runs every six hours. The website can also be refreshed using
its manual workflow. Website deployment follows its existing Pages
configuration and the owner's launch approval.

The homepage importer checks downloads without release-asset credentials, as a
visitor would. Automatic import therefore needs public release downloads.
While this repository is private, review new packages using the preparation
command's local homepage preview. Changing visibility remains a launch decision.
