# Board Game Collection & Quick-Start Guides

A structured catalog of my board game shelf paired with concise, tabletop-ready **Quick-Start Guides** and **SVG Setup / Turn-Flow Schematics** for fast game-night refreshers.

## Collection Progress
* **Total Cataloged Games:** 62
* **Completed Guides:** 2 / 62
* **In Progress:** 0
* **Needs Box Verification:** 6

---

## Repository Structure

```text
├── README.md                     # Master collection index (auto-updated via sync script)
├── mkdocs.yml                    # Optional MkDocs Material config for GitHub Pages
├── data/
│   └── collection.csv            # Local mirror of the Google Sheet catalog
├── guides/
│   ├── 7-wonders-duel.md         # Completed guide + schematic
│   ├── power-grid.md             # Completed guide + schematic
│   └── ...                       # Stub guides for all 62 shelf items
├── assets/
│   ├── 7-wonders-duel-schematic.svg
│   └── power-grid-schematic.svg
├── templates/
│   └── quick-start-template.md   # Standardized guide template
└── scripts/
    └── sync_collection.py        # Syncs Google Sheet CSV -> README & guide stubs
```

---

## Game Catalog

| Shelf | Pos | Game Title | Box / Localized Title | Type | Players | Play Time | Guide | Status |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 1 | 1 | **KeyForge: Call of the Archons (2 Player Starter Set)** | KeyForge: Call of the Archons | Base Game | 2 | 45 min | [Quick Start](guides/keyforge-call-of-the-archons.md) | ⬜ Not Started |
| 1 | 2 | **Power Grid** | 電力会社 (Power Grid) | Base Game | 2-6 | 120 min | [Quick Start](guides/power-grid.md) | ✅ Completed |
| 1 | 3 | **Unidentified Card Deck (Ziplock Bag)** | Unlabeled plastic bag | Unknown | TBD | TBD | [Quick Start](guides/shelf-1-pos-3-unverified.md) | 🔍 Needs Verification |
| 1 | 4 | **My Dungeon Does Not Lie** | 職場地下城 - 真心・不騙 | Base Game | 3-6 | 30 min | [Quick Start](guides/my-dungeon-does-not-lie.md) | ⬜ Not Started |
| 1 | 5 | **Cat & Chocolate** | キャット＆チョコレート | Base Game | 3-6 | 20 min | [Quick Start](guides/cat-and-chocolate.md) | ⬜ Not Started |
| 1 | 6 | **Imagine** | イマジン (Imagine) | Base Game | 3-8 | 30 min | [Quick Start](guides/imagine.md) | ⬜ Not Started |
| 1 | 7 | **CV (What Will Your Life Look Like?)** | CV | Base Game | 2-4 | 60 min | [Quick Start](guides/cv.md) | ⬜ Not Started |
| 1 | 8 | **Small Card Game (Shelf 1, Pos 8)** | Partially obscured Japanese/Chinese box | Base Game | TBD | TBD | [Quick Start](guides/shelf-1-pos-8-unverified.md) | 🔍 Needs Verification |
| 1 | 9 | **Oink Games Small Box (Blue)** | Oink Games (Deep Sea Adventure / Start-Ups) | Base Game | 2-6 | 30 min | [Quick Start](guides/oink-games-blue-box.md) | 🔍 Needs Verification |
| 1 | 10 | **Oh My Goods!** | オー・マイ・グーッズ！ | Base Game | 2-4 | 30 min | [Quick Start](guides/oh-my-goods.md) | ⬜ Not Started |
| 1 | 11 | **Oh My Goods!: Longsdale in Revolt** | オー・マイ・グーッズ！ロングズデールの反乱 | Expansion | 1-4 | 45 min | [Quick Start](guides/oh-my-goods-longsdale-in-revolt.md) | ⬜ Not Started |
| 1 | 12 | **Aquarius** | Aquarius | Base Game | 2-5 | 30 min | [Quick Start](guides/aquarius.md) | ⬜ Not Started |
| 1 | 13 | **Citadels** | 富饒之城 (Citadels) | Base Game | 2-8 | 30-60 min | [Quick Start](guides/citadels.md) | ⬜ Not Started |
| 1 | 14 | **Chrononauts** | Chrononauts | Base Game | 1-6 | 30 min | [Quick Start](guides/chrononauts.md) | ⬜ Not Started |
| 1 | 15 | **Pocket Madness** | Pocket Madness | Base Game | 2-4 | 20 min | [Quick Start](guides/pocket-madness.md) | ⬜ Not Started |
| 1 | 16 | **Slim White Card Box (Shelf 1, Pos 16)** | PHANTASM... (partially obscured) | Base Game | TBD | TBD | [Quick Start](guides/shelf-1-pos-16-unverified.md) | 🔍 Needs Verification |
| 2 | 1 | **Slim Dark Box (Shelf 2, Pos 1)** | Unidentified dark slim box | Unknown | TBD | TBD | [Quick Start](guides/shelf-2-pos-1-unverified.md) | 🔍 Needs Verification |
| 2 | 2 | **Unearth** | Unearth | Base Game | 2-4 | 60 min | [Quick Start](guides/unearth.md) | ⬜ Not Started |
| 2 | 3 | **Coal Baron** | 炭鉱王 / 煤炭大亨 | Base Game | 2-4 | 60 min | [Quick Start](guides/coal-baron.md) | ⬜ Not Started |
| 2 | 4 | **Majesty: For the Realm** | マジェスティ | Base Game | 2-4 | 30 min | [Quick Start](guides/majesty-for-the-realm.md) | ⬜ Not Started |
| 2 | 5 | **Evolution: Plantarum** | 演化論：綠意盎然 | Expansion | 2-6 | 60 min | [Quick Start](guides/evolution-plantarum.md) | ⬜ Not Started |
| 2 | 6 | **Evolution (Base Game - Chinese Ed.)** | 演化論：物種起源 | Base Game | 2-6 | 60 min | [Quick Start](guides/evolution-chinese-ed.md) | ⬜ Not Started |
| 2 | 7 | **Evolution: Expansion** | 演化論・擴充 | Expansion | 2-6 | 60 min | [Quick Start](guides/evolution-expansion.md) | ⬜ Not Started |
| 2 | 8 | **Exploding Minions** | ミニオンばくはつ | Base Game | 2-5 | 15 min | [Quick Start](guides/exploding-minions.md) | ⬜ Not Started |
| 2 | 9 | **Cat in the Box (Deluxe Edition)** | Cat in the Box | Base Game | 2-5 | 30-45 min | [Quick Start](guides/cat-in-the-box.md) | ⬜ Not Started |
| 3 | 1 | **7 Wonders Duel** | 7 Wonders Duel | Base Game | 2 | 30 min | [Quick Start](guides/7-wonders-duel.md) | ✅ Completed |
| 3 | 2 | **8Bit Box** | 8Bit Box | Base Game | 3-6 | 40 min | [Quick Start](guides/8bit-box.md) | ⬜ Not Started |
| 3 | 3 | **Hit Z Road** | Hit Z Road | Base Game | 1-4 | 60 min | [Quick Start](guides/hit-z-road.md) | ⬜ Not Started |
| 3 | 4 | **Orbis** | Orbis | Base Game | 2-4 | 45 min | [Quick Start](guides/orbis.md) | ⬜ Not Started |
| 3 | 5 | **Kanagawa** | Kana Gawa | Base Game | 2-4 | 45 min | [Quick Start](guides/kanagawa.md) | ⬜ Not Started |
| 3 | 6 | **Carcassonne** | Carcassonne | Base Game | 2-5 | 35 min | [Quick Start](guides/carcassonne.md) | ⬜ Not Started |
| 3 | 7 | **Valeria: Card Kingdoms** | Valeria: Card Kingdoms | Base Game | 1-5 | 45 min | [Quick Start](guides/valeria-card-kingdoms.md) | ⬜ Not Started |
| 3 | 8 | **Inception** | 盜夢都市 | Base Game | 3-7 | 30-45 min | [Quick Start](guides/inception.md) | ⬜ Not Started |
| 3 | 9 | **Pickomino** | 蟲蟲燒烤派對 | Base Game | 2-7 | 20-30 min | [Quick Start](guides/pickomino.md) | ⬜ Not Started |
| 4 | 1 | **Viracocha** | ウィラコチャ / 天空都市 | Base Game | 2-4 | 45 min | [Quick Start](guides/viracocha.md) | ⬜ Not Started |
| 4 | 2 | **King of Tokyo** | King of Tokyo | Base Game | 2-6 | 30 min | [Quick Start](guides/king-of-tokyo.md) | ⬜ Not Started |
| 4 | 3 | **Hobby Japan Box (老師請給分)** | 老師請給分 (Hobby Japan) | Base Game | TBD | TBD | [Quick Start](guides/hobby-japan-box-shelf-4.md) | 🔍 Needs Verification |
| 4 | 4 | **Marvel Champions: The Card Game** | Marvel Champions | Base Game | 1-4 | 45-90 min | [Quick Start](guides/marvel-champions.md) | ⬜ Not Started |
| 4 | 5 | **Azul** | Azul | Base Game | 2-4 | 30-45 min | [Quick Start](guides/azul.md) | ⬜ Not Started |
| 4 | 6 | **Terra** | Terra | Base Game | 2-6 | 45-60 min | [Quick Start](guides/terra.md) | ⬜ Not Started |
| 4 | 7 | **Machi Koro** | 街コロ (Machi Koro) | Base Game | 2-4 | 30 min | [Quick Start](guides/machi-koro.md) | ⬜ Not Started |
| 4 | 8 | **Arcane Academy** | Arcane Academy | Base Game | 2-4 | 45 min | [Quick Start](guides/arcane-academy.md) | ⬜ Not Started |
| 4 | 9 | **10 Days in the USA** | 10 Days in the USA | Base Game | 2-4 | 30 min | [Quick Start](guides/10-days-in-the-usa.md) | ⬜ Not Started |
| 5 | 1 | **Funkoverse Strategy Game: Harry Potter 100** | Funkoverse: Harry Potter | Base Game | 2-4 | 20-60 min | [Quick Start](guides/funkoverse-harry-potter-100.md) | ⬜ Not Started |
| 5 | 2 | **Funkoverse Strategy Game: DC Comics 100** | Funkoverse: Batman | Base Game | 2-4 | 20-60 min | [Quick Start](guides/funkoverse-dc-comics-100.md) | ⬜ Not Started |
| 5 | 3 | **Marvel United** | Marvel United | Base Game | 1-4 | 40 min | [Quick Start](guides/marvel-united.md) | ⬜ Not Started |
| 5 | 4 | **Marvel United: Tales of Asgard** | Marvel United: Tales of Asgard | Expansion | 1-4 | 40 min | [Quick Start](guides/marvel-united-tales-of-asgard.md) | ⬜ Not Started |
| 5 | 5 | **Marvel United: Enter the Spider-Verse** | Marvel United: Enter the Spider-Verse | Expansion | 1-4 | 40 min | [Quick Start](guides/marvel-united-enter-the-spider-verse.md) | ⬜ Not Started |
| 5 | 6 | **God of War: The Card Game** | God of War: The Card Game | Base Game | 1-4 | 60-90 min | [Quick Start](guides/god-of-war-the-card-game.md) | ⬜ Not Started |
| 5 | 7 | **Eclipse** | ECLIPSE | Base Game | 2-6 | 60-180 min | [Quick Start](guides/eclipse.md) | ⬜ Not Started |
| 5 | 8 | **How to Become President** | 大統領になる方法 | Base Game | 3-6 | 45 min | [Quick Start](guides/how-to-become-president.md) | ⬜ Not Started |
| 5 | 9 | **504** | 504 | Base Game | 2-4 | 60-120 min | [Quick Start](guides/504.md) | ⬜ Not Started |
| 5 | 10 | **Fearsome Floors** | Fearsome Floors | Base Game | 2-7 | 60 min | [Quick Start](guides/fearsome-floors.md) | ⬜ Not Started |
| 6 | 1 | **Alien Frontiers** | Alien Frontiers | Base Game | 2-4 | 90 min | [Quick Start](guides/alien-frontiers.md) | ⬜ Not Started |
| 6 | 2 | **Kingsburg** | Kingsburg | Base Game | 2-5 | 90 min | [Quick Start](guides/kingsburg.md) | ⬜ Not Started |
| 6 | 3 | **Gangsi** | GANGSI | Base Game | 2-4 | 30 min | [Quick Start](guides/gangsi.md) | ⬜ Not Started |
| 6 | 4 | **Small World Underground** | Small World Underground | Base Game | 2-5 | 40-80 min | [Quick Start](guides/small-world-underground.md) | ⬜ Not Started |
| 6 | 5 | **Small World** | Small World | Base Game | 2-5 | 40-80 min | [Quick Start](guides/small-world.md) | ⬜ Not Started |
| 6 | 6 | **Via Nebula** | Via Nebula | Base Game | 2-4 | 45-60 min | [Quick Start](guides/via-nebula.md) | ⬜ Not Started |
| 6 | 7 | **Evolution (North Star Games)** | Evolution | Base Game | 2-6 | 60 min | [Quick Start](guides/evolution-north-star.md) | ⬜ Not Started |
| 6 | 8 | **Machi Koro Legacy** | Machi Koro Legacy | Base Game | 2-4 | 30-45 min | [Quick Start](guides/machi-koro-legacy.md) | ⬜ Not Started |
| 6 | 9 | **Battle Cry (150th Civil War Anniversary Edition)** | Battle Cry | Base Game | 2 | 60 min | [Quick Start](guides/battle-cry.md) | ⬜ Not Started |

---

## Syncing Updates from Google Sheets

1. Open your **Board Game Collection** Google Sheet and go to **File → Share → Publish to web**.
2. Select the **Board Game Catalog** sheet and **Comma-separated values (.csv)**, then copy the published link.
3. Run:
   ```bash
   python scripts/sync_collection.py --url "<YOUR_PUBLISHED_CSV_URL>"
   ```
   Or rebuild the README locally after editing `data/collection.csv`:
   ```bash
   python scripts/sync_collection.py --local
   ```
