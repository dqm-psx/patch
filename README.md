# Dragon Quest Monsters 1 & 2 — English patch

Unofficial English fan translation for the Japanese PlayStation collection, covering Terry’s, Cobi’s, and Tara’s adventures.

<!-- latest-release:begin -->
## Latest release — v1.0.73

[Release notes and downloads](https://github.com/dqm-psx/patch/releases/tag/v1.0.73)

- **[English patch](https://github.com/dqm-psx/patch/releases/download/v1.0.73/DQM1-2-English-v1.0.73-public.zip)** · 7.56 MB — BPS patch, matching CUE, and release README.

### Changes

- Running and movement settings in all three adventures, with independent walking and R1 speeds, Hold or Toggle running, and saved preferences.
- Time and Distance encounter options let you choose how movement speed affects random battles.
- Two-player Colosseum Local Rules and optional monster wagers. Transfers save both Adventure Logs, so keep both cards inserted and the game running until both saves finish.
- Updated dialogue font, monster names and nicknames, reduced memory use, and fixes for battle loading, graphics, and walking sprites. Existing saved nicknames stay unchanged.

<details>
<summary>ZIP checksums</summary>

`DQM1-2-English-v1.0.73-public.zip`

```text
652ae16c06cc2291495b592bde5a2737e68e483879b4dc684ed4d58a56e1493a
```

</details>
<!-- latest-release:end -->

## Install or update

1. Supply an unmodified Japanese **SLPM-87050 BIN**:
   - Size: **260,975,568 bytes**
   - SHA-256: `a1217657786430ac1c3ad71f16cdadb65d47b0df9a7e30278900651c1f1eec29`
2. Download and extract your chosen patch ZIP from the latest release.
3. Apply its BPS patch to the original Japanese BIN with a BPS patcher such as [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/). Keep checksum validation enabled.
4. Give the patched BIN the exact filename in the included CUE, keep both files together, and open the CUE in your PlayStation emulator.
5. When updating, back up your memory-card saves, patch a clean Japanese image, boot fresh, and load an in-game memory-card save. Do not patch an already translated image or resume a save state from another patch version.

## Reports and contributions

For [bug reports](https://github.com/dqm-psx/patch/issues/new?template=bug-report.yml), include the patch version and edition, campaign, emulator/version or hardware, device/OS, location, reproduction steps, expected and actual behavior, and whether it repeats after a fresh boot from a memory-card save. Include BUILD.json or its build ID when your package provides one, along with cheats or non-default settings, screenshots, and a save from before the issue when available. A save state from the affected patch version can help debugging.

Use the [translation comparison](https://dqm-psx.github.io/translations/) for wording suggestions, the [Guide](https://dqm-psx.github.io/guide/) for gameplay reference, and [Discord](https://discord.gg/6V9p6Y2pBt) for discussion and setup help.

## Release archive

Download the [latest English patch](https://github.com/dqm-psx/patch/releases/latest) or browse [earlier versions](https://github.com/dqm-psx/patch/releases). Each release lists its available patch ZIPs and checksums.

The [package list](release-manifest.json) gives the filename, size, checksum, and download link for each archived version. You can also browse the [archived ZIPs](Archive/) and [original release notes](README.txt).

Release maintainers can follow the [release handoff instructions](docs/RELEASING.md).

Dragon Quest and its characters belong to their respective owners. This is an independent fan project.
