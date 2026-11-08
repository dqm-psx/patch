DRAGON QUEST MONSTERS 1 & 2 - ENGLISH TRANSLATION
v1.0.73 - public release
Latest package: DQM1-2-English-v1.0.73-public.zip
Previous package: DQM1-2-English-v1.0.72-public.zip

Unofficial fan English translation of
ドラゴンクエストモンスターズ1・2 星降りの勇者と牧場の仲間たち
(Dragon Quest Monsters 1 & 2: The Starry Night Hero and Friends at the Ranch).

English text and title artwork for Terry's, Cobi's and Tara's adventures.

PUBLIC RELEASE HIGHLIGHTS
v73:
- Adds run and speed options in menu. Tactics > Movement in all three adventures: walking and R1 speeds, R1 Hold/Toggle, and encounter-rate options. Settings save with each adventure. See Movement Settings below. 
- Restores cut/unfinished content; monster betting/wager now available in Colosseum battles, along with additional rule options. 
- Updated Dialogue font. 
- Makes about 24 KB more RAM available during gameplay by storing menu text more efficiently.
- Improves battle-loading safety for Milly's Starry Night final.
- Fixes memory leaks in scene and NPC graphics, plus a walking-sprite loading bug (these leaks/bugs were present in original japanese game, now fixed)
- Reduces memory used by Fire Breath and Freeze Solid without changing their appearance.
- Changes the starter Slime's default nickname from Sura to Slib.
- Renames Drakeling to MiniDrak in the current translation, including matching dialogue and an updated arena joke.
- Updates some monster names throughout dialogue and menus:
  King Azrail -> Azurile; Healer Slime -> Healer
  Dark Dragon Knight -> Serpentia; Minon -> Saccer
  Super Tentuck -> Super Ten; Danbiramucho -> Dumbira
  Paom -> Trumpeter; Moza -> Growlbear
  Gappurin -> Gulpple; Onion Knight -> Oniono
  Madron -> Mudron; Manemane -> Copycat
- Renames Hell Spark to Hellblast.
- Updates default monster nicknames: Ikar -> Squiz, Jin -> Face, and Pashi -> Percy. Existing saved nicknames stay unchanged.
- Includes all earlier translation and gameplay fixes.
Thanks to everyone who contributed reports, suggestions, and testing!

v72:
- Updates monster names throughout dialogue and menus:
  Clockwork Bird / Windup Bird -> CoilBird
  Baby Dragon -> Drakeling
  Cyborg Slime -> Slimeborg
  Slappy -> Slabbit
  Dork / Lord Dork -> Darck / Lord Darck
- Uses DeadTree consistently for the kingdom previously called Kareki,
  and renames Taiboku to BigTrunk.
- Replaces the arena's Baby Dragon joke with a Drakeling scales joke.
- Clarifies two NPC refusals to breed low-level monsters.
- Corrects the Sky Shield legend and examination text to describe
  a shield instead of an umbrella.
- Includes all earlier translation and gameplay fixes.
Thanks to everyone who contributed translation suggestions and feedback!

v71:
- Fixes the NightLich battle-start freeze.
- Reduces memory use for Blizzard and other battle effects.
- Fixes cleanup after failed battle sound loads.
- Fixes accessory labels and renames BounceOnce/Bounce1 to Bound.
- Corrects the Port Ritz dialogue to say "giant clam".
- Includes all earlier translation and gameplay fixes.
- Thanks to Nelin and Sparrow for the reports and help!

v70:
- Fixes becoming invisible and unable to leave Terry's traveling
  colosseum after choosing "No" to another challenge (issue #70).
- Lets the native arrival sequence finish before starting the challenge,
  including arrivals from a Wizard teleport.
- Includes all earlier translation and gameplay fixes.
Thanks to Suppi for reporting the arena-floor problem!
Built from merged PR #71, commit f1e6ac4138f640f9aa1932da6d22bd53efb07f85.
Validated with 329 automated tests (326 passed; 3 optional checks skipped)
and a separate focused run of 8 passing tests, including disc checks.
A fresh current-edition build and independent BPS round trip passed.
Compared with v69, only the colosseum resource and its size entry change.
Directed emulator testing received a Flame Staff prize (inventory count
28 -> 29), chose "No", and exited the room with the hero visible.
The repeat/final-round state was seeded for this directed check; it was
not a full natural-progression playthrough or the reporter's original save.

v69:
- Fixes Japanese artwork in the appraisal scenes' embedded certificate
  images (issue #68). Both affected certificates now use the English
  heading Appraisal and the labels Species:, Sex:, Skills: and Growth:.
- Includes all earlier translation and gameplay fixes.
Thanks to PkmnTrainerAbram for reporting the appraisal-certificate problem!
Built from merged PR #69, commit 8796859bc2fb71bd7c4d4c634be47be03de15ad4.
Validated with 321 automated tests (321 passed; no checks skipped),
translation checks for all four editions, a fresh current-edition disc
build, and independent verification of the packaged BPS round trip.
Directed PCSX-ReARMed checks exercised both native appraisal image loaders.
The tester also reported that the fix works in DuckStation.

v68:
- Machiko's Rank A statue gift now receives the English nickname Pete
  and original-owner label Machi. Existing saved monsters keep their names.
- Changes the breeding offspring confirmation from "Use [monster]?"
  to "Make [monster]?" (issue #64).
- Includes v67's breeding crash fix and all earlier fixes.
Built from merged PRs #63, #65 and #66, commit 368c5c50aab911239323c3297132fba101093e65.
Validated with 316 automated tests (314 passed; 2 opt-in checks skipped),
translation checks for all four editions, a fresh current-edition disc
build, and independent verification of the packaged BPS round trip.
No emulator testing was performed for v68.

v67:
- Fixes the reproduced black-screen crash during Master Teto's IceMan
  breeding offer in Terry's adventure (issue #60).
- Improves the shared memory allocator so small allocations reuse only
  the space they need, leaving freed memory available for later loads.
- Preserves v66's transformed-name correction and all earlier fixes.
Source merged in PR #61, commit 4fe360e358732dd21e3a0a5396e9f1b891e6d1b9.
Validated with 313 automated tests (311 passed; two opt-in checks skipped),
fresh builds of all four translation editions, and BPS round-trip checks.
A directed Windows DuckStation check completed the IceMan breeding event
and returned to responsive field movement and menus. It used a copied
Arena save and a debugger-started native offer to bypass progression,
not the reporter's save. The alternate editions received build and
automated-test coverage.

v66:
- Fixes garbled text after a transformed enemy's copied name in
  the battle target selector (issue #58). Names now use the existing
  English "-ish" suffix, for example "Atlas-ish".
- Preserves v65's skill-learning/forgetting fixes and all earlier
  translation and gameplay fixes.
Thanks to BalK for reporting the transformed-name problem!
Built from main after PR #59, commit 55868daf77cd01e825d4a39c381c519de8e11c3d.
Validated with automated native-instruction regressions, checks
across all four translation editions, and a fresh disc build with
BPS round-trip verification. No emulator testing for this release.

v65:
- Improves the full-skill warning and shows the complete two-line
  skill-forgetting prompt without menu overlap (issue #56).
- Verified selection, paging, canceling and replacement in an emulator.
Built from main after PR #57, commit 4fb170a3fea33210a9e7f914c93e2f69d67f4fcf.

v64:
- Fixes the wrapped and overlapping description box when choosing a skill
  to forget while learning a new skill (issue #54).
- Restores deferred description-window initialization so the skill list
  is ready before the description is drawn.
- Includes the current English translation and prior fixes. Built from
  main after PR #55, commit 2439a7b3b29be30be8bebbf3c2884c302d5b7dbb.
Thanks to nextlvlroy for reporting the skill-description problem!

The reported layout and initialization regressions were absent in v60
and already present in the corrected v62 package. A static audit found
no additional confirmed regression introduced specifically by v63.
The fix passed automated checks and a fresh build with BPS round-trip
verification; no emulator testing was performed for this release.

v63:
- Fixed an audio-buffer leak behind the reproduced breeding/shrine-exit crash.
- Reduced memory usage and added an audio-capacity safeguard.
Thanks to nextlvlroy for reporting and helping reproduce the crash!

v62 (corrected audio ownership build):
- Includes the breeding/shrine fixes and an audio memory leak fix for the
  reported ClockBird crash when returning to GreatLog.
- Includes the earlier gate and battle transition fixes.
Thanks to nextlvlroy and BalK for the bug reports and save files!
Thanks also to nextlvlroy for helping reproduce and test the ClockBird crash.

This v62 package uses the corrected audio ownership build, which differs
from the earlier v62 build.

v61:
- Alternative translation options, including Game Boy and Game Boy
  delocalization wording, are available in Discord. Translation work
  remains in progress.

v60:

- Fixed bug with NPC monster breeding offer. Thanks gollum_007 for the bug report!

v59:

- Fixes the reported crash when Baramos learns HellSpark with a full
  skill list. Thanks to Lori for reporting and confirming the fix!
- Corrects description-window initialization and placement in the
  skill-forgetting menu.
- Based on public v57 with the tested skill-learning correction.

v57:

- Ice world map fix; thanks Wingforth for the bug report!

v56:

- Not released, still working on font improvements

v55:

- Improved translations for battle messages

v54:

- Corrected malformed battle messages

v53:

- Translates the appraisal certificate heading and four printed labels.
- Corrects the certificate's character spacing and centered temperament
  line so English appraisal text fits within its border.
- Retains v52's dialogue formatter and all prior translation content
  and gameplay fixes.

v52:

- Fixes rapid dialogue scrolling after the nut pie scene and in Cobi's
  ship conversation. The shared formatter now preserves the spacing
  of already wrapped dialogue. Thanks to _Zev for the report!
- Retains all v51 translation content, fonts and prior fixes.
- The project owner playtested v52 and reported that it seems to work.

v51:

- Fixes the reproduced King dialogue freeze after the Starry Night final.
  The valley scene now advances with its graphics intact.
- Fixes a verified battle-memory overwrite during attack loading.
- Includes v49's combat skill panel correction and all earlier fixes.
  Thanks to Schnaki and _Zev for the crash reports!

v49:

- Combat skill descriptions now fit in a full-width panel below the skill
  choices. MP cost remains on its own row. All three combat menu entry
  paths are corrected; v48 translation, fonts and gameplay fixes remain.

v48:

- Selling part of an item stack now keeps the remaining stack in its
  original inventory position.
- Beavern's default nickname is now Biino. Thanks to Wingforth for the
  suggestion! Names already stored in your save, including names you
  chose, are unchanged.
- Includes restored monster table conversations and special dungeon
  floors in Terry's adventure. See below for details and instructions.

v46: The hidden movement mode works with the hero name Sanic (capital S).
Press and hold Square, keeping it held while changing areas to
activate the mode. Existing saves using the original みんさん
trigger still work.

v45: Clearer item-description headers. Using or discarding one copy keeps
the remaining stack in place, and rejected battle items return the
cursor to the correct row. Retains v43's fonts and dialogue spacing.

v38: Fixed the Master Teto breeding crash and NPC breeding names
overwriting monster data. Thanks to Schnaki for reporting the bug!

v36: Fixed DQM2 gate room text glitches and improved key names.

v34: Fixed the original Japanese game's Truth gate / Digster progression
bug, along with intermittent portal-entry crashes in the
translation patch.

v30: Improved inventory, status bars and dialogue; fixed the
Arena/School transition bug.

v23: English text and title artwork, menu fixes and expanded HP/MP displays.

MOVEMENT SETTINGS

Open Tactics > Movement, just below Text Speed.

Defaults: Walk 1x, R1 2x, Hold, Time.
Hold R1 to run at twice the normal speed. Choose Toggle to press R1 once
for the R1 speed and again for the walking speed. Both speeds can be
set to 1x, 2x or 4x.

Time keeps encounters at roughly the same frequency while running.
Distance uses the usual encounter rate per step.

Use Up/Down to select a setting and Left/Right to change it.
Circle or Triangle applies changes. Cross cancels; Square cancels and
closes the field menu. Save normally to keep each adventure's settings.
Loading a save starts you at the walking speed.

COLOSSEUM BATTLES

Choose Free Battle, Enix Rules or Local Rules in Colosseum.
Local Rules lets you set skill, level and family limits, turns, timer,
combos and accessories. Set Turns to 0 for no turn limit.

To wager monsters, enable prizes in Local Rules (off by default).
Offer an awake farm monster outside your saved adventure party.
Leave space on the receiving farm. The winner receives the loser's
offer and keeps their own; draws transfer nothing.

A transfer saves both Adventure Logs. Keep the game running until both
saves finish. If a memory-card error occurs, use Retry without resetting.
Resetting or losing power between saves can lose the prize.

RESTORED CONTENT IN TERRY'S ADVENTURE

Monster table conversations

The Game Boy original includes a small Easter egg that lets you chat
with your monsters at a table in the Arena. The Japanese PlayStation
release retained 112 conversations, but the table interaction was
unavailable. This patch makes those conversations accessible, with
reconstructed seating and personality matching.

At the arena dining room's right table, walk onto the east stool with
one to three living, visible party monsters.

- Up, Left and Down select the north, west and south monster.
- Confirm/Talk starts a conversation.
- Cancel or Right stands up.

Leave the stool before sitting again, and revive fallen party members
before taking a seat.

Special dungeon floors

The Game Boy original's special dungeon floors return: treasure/Mimic
rooms, Lost Forest, the traveling colosseum, mazes and sliding floors.

These restorations combine unused PS1 maps and other retained assets
with behavior adapted from the Game Boy original. Some mechanics and
encounter rates are reconstruction choices.

Travel Bookmark cannot be used inside the traveling colosseum.
Leave through its north door.

REQUIRED GAME

Unmodified Japanese PlayStation BIN, serial SLPM-87050.
Size: 260,975,568 bytes

Source SHA-256:
a1217657786430ac1c3ad71f16cdadb65d47b0df9a7e30278900651c1f1eec29

INSTALL

1. Extract the latest package. Apply DQM1-2-English-v1.0.73.bps to the
   original Japanese BIN using a BPS patcher, such as:
   https://www.marcrobledo.com/RomPatcher.js/
   Do not patch an already translated image. Keep checksum validation on.

2. Name the output DQM1-2-English-v1.0.73.bin and place it beside the
   included DQM1-2-English-v1.0.73.cue.

3. Open that CUE in your PlayStation emulator. Boot fresh, then load your
   existing in-game memory-card save to continue playing after updating.

4. Avoid emulator save states from other patch versions, which can
   restore old game code.

Patched BIN SHA-256 (v73):
c7fd48e4decd7747a3e8b72ff052960b4ae0943ad61b6a95c57c946791cba812

BPS SHA-256 (v73):
8a44ee27921f6644c7adb174a0a8936b92b782d6a9e698b03479464195f3a1a1

Public ZIP SHA-256 (DQM1-2-English-v1.0.73-public.zip):
652ae16c06cc2291495b592bde5a2737e68e483879b4dc684ed4d58a56e1493a

PLAYTESTING

Back up your saves.

Full campaign playthroughs and original-hardware compatibility remain
unverified. Some names are shortened, and some area transitions may load
more slowly than in the Japanese game.

For bugs, report the patch version, campaign, location and steps to
reproduce the issue. If possible, include a screenshot and a save from
before the issue occurred.

Game and BIOS files are not included. Earlier public packages are retained.

https://discord.gg/Y5vrQ5ww9
https://www.romhacking.net/translations/7734/
