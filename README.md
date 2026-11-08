# Dragon Quest Monsters 1 & 2 — English patch

Unofficial English fan translation for the Japanese PlayStation collection, covering Terry’s, Cobi’s, and Tara’s adventures.

**[Download the latest patch](https://github.com/dqm-psx/patch/releases/latest)** · [All releases](https://github.com/dqm-psx/patch/releases) · [Report a bug](https://github.com/dqm-psx/patch/issues/new?template=bug-report.yml)

The ZIP contains the BPS patch, matching CUE, and original README. No game image or BIOS is included.

## What’s new in v1.0.73

- **Running and movement settings:** Open **Tactics → Movement** in any adventure. Set walking and R1 speeds independently to 1×, 2×, or 4×, with Hold or Toggle controls. Defaults are Walk 1× and Hold R1 for 2×. Save normally to retain settings for that adventure; loading returns to Walk speed.
- **Encounter options:** Time keeps encounters at roughly the usual frequency while running. Distance retains the normal encounter rate per step, bringing encounters closer together in time at faster speeds.
- **Two-player Colosseum monster wagers:** Enable prizes in Local Rules to offer an awake farm monster outside your saved party. Players need distinct identities and room on their farms. The winner receives the loser’s offered monster and keeps their own; draws transfer nothing. Local Rules also provides skill, level, family, turn, timer, combo, and accessory options.
- **Translation and stability:** Updated dialogue font, monster names and default nicknames, reduced memory use, and fixes for battle loading, scene and NPC graphics, and walking sprites. Existing saved nicknames stay unchanged.

**Monster transfers save both Adventure Logs.** Back up your saves first. Keep the game running and both memory cards inserted until both saves finish; use Retry after a card error without resetting. An interruption between saves can lose the prize monster. Prizes are off by default.

The patch also includes restored monster table conversations and special dungeon floors in Terry’s adventure, expanded HP/MP displays, grouped item lists, bulk selling, and earlier translation and gameplay fixes. See the included README for the full history and controls.

## Install or update

1. Supply an unmodified Japanese **SLPM-87050 BIN**:
   - Size: **260,975,568 bytes**
   - SHA-256: `a1217657786430ac1c3ad71f16cdadb65d47b0df9a7e30278900651c1f1eec29`
2. Download and extract the ZIP from the release you want to play.
3. Apply its BPS patch to the original Japanese BIN with a BPS patcher such as [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/). Keep checksum validation enabled.
4. Give the patched image the BIN filename specified in that release’s README, place it beside the included CUE, and open the CUE in your PlayStation emulator.
5. When updating, back up your memory-card saves, patch a clean Japanese image, boot fresh, and load an in-game memory-card save. Do not patch an already translated image or resume a save state from another patch version.

The v1.0.73 ZIP is **7,558,537 bytes** and has this SHA-256. Each release includes its own checksum attachment.

```text
652ae16c06cc2291495b592bde5a2737e68e483879b4dc684ed4d58a56e1493a
```

## Reports and contributions

For [bug reports](https://github.com/dqm-psx/patch/issues), include the patch version, campaign, emulator/version or hardware, device/OS, location, reproduction steps, expected and actual behavior, and whether it repeats after a fresh boot from a memory-card save. Include cheats or non-default settings, screenshots, and a save from before the issue when available. A save state from the affected patch version can help debugging.

Use the [translation comparison](https://dqm-psx.github.io/translations/) for wording suggestions, the [breeding guide](https://dqm-psx.github.io/guide/) for gameplay reference, and [Discord](https://discord.gg/6V9p6Y2pBt) for discussion and setup help.

## Release archive

This repository hosts 28 existing packages copied from [`phakic/DQM-1-2-PSX-translation`](https://github.com/phakic/DQM-1-2-PSX-translation), including its `Archive` folder. Every ZIP is unchanged and was verified against its source Git blob and SHA-256. Original package READMEs and credits are preserved. Original release notes are retained where present; other versions are identified as historical packages. Beta packages remain marked as beta in their names.

[`release-manifest.json`](release-manifest.json) records the source snapshot, filenames, sizes, SHA-256 values, and destination links. Each release includes a checksum file; historical checksum files were added during copying. The v1.0.73 checksum attachment is an unchanged copy of the source attachment.

Dragon Quest and its characters belong to their respective owners. This is an independent fan project.
