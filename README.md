# Board Game Collection & Quick-Start Guides

A structured catalog of my board game shelf paired with concise, tabletop-ready **Quick-Start Guides** and **SVG Setup / Turn-Flow Schematics** for fast game-night refreshers.

## Collection Progress
* **Total Cataloged Games:** 62
* **Completed Guides:** 10 / 62
* **In Progress:** 5
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
| Shelf 1 | 1 | **KeyForge: Call of the Archons (2 Player Starter Set)** | KeyForge: Call of the Archons (Starter Set) | Base Game | 2 players | ~45 min | [Quick Start](guides/keyforge-call-of-the-archons.md) | ✅ Completed |
| Shelf 1 | 2 | **Power Grid** | 電力会社 (Funkenschlag) | Base Game | 2-6 players | ~120 min | [Quick Start](guides/power-grid.md) | 🚧 In Progress |
| Shelf 1 | 3 | **Unlabeled plastic bag (deck/cards)** | Unlabeled card deck | Unknown | Unclear | Unclear | [Quick Start](guides/shelf1-unlabeled-bag.md) | 🔍 Needs Verification |
| Shelf 1 | 4 | **My Dungeon Does Not Lie** | 職場地下城 - 真心・不騙 | Base Game | 3-6 players | ~30 min | [Quick Start](guides/my-dungeon-does-not-lie.md) | ⬜ Not Started |
| Shelf 1 | 5 | **Cat & Chocolate** | キャット＆チョコレート | Base Game | 3-6 players | ~20 min | [Quick Start](guides/cat-and-chocolate.md) | ⬜ Not Started |
| Shelf 1 | 6 | **Imagine** | イマジン (Imagine) | Base Game | 3-8 players | ~30 min | [Quick Start](guides/imagine.md) | ⬜ Not Started |
| Shelf 1 | 7 | **CV** | CV (What Will Your Life Look Like?) | Base Game | 2-4 players | ~60 min | [Quick Start](guides/cv.md) | ⬜ Not Started |
| Shelf 1 | 8 | **Small brown/green Japanese/Chinese box** | Title partially obscured | Base Game | Unclear | Unclear | [Quick Start](guides/shelf1-obscured-box-8.md) | 🔍 Needs Verification |
| Shelf 1 | 9 | **Oink Games box (blue)** | Oink Games (Blue Box) | Base Game | 2-6 players | ~30 min | [Quick Start](guides/oink-games-blue-box.md) | 🔍 Needs Verification |
| Shelf 1 | 10 | **Oh My Goods!** | オー・マイ・グーッズ！ | Base Game | 2-4 players | ~30 min | [Quick Start](guides/oh-my-goods.md) | ⬜ Not Started |
| Shelf 1 | 11 | **Oh My Goods!: Longsdale in Revolt** | オー・マイ・グーッズ！ロングズデールの反乱 | Expansion | 1-4 players | ~45 min | [Quick Start](guides/oh-my-goods-longsdale.md) | ⬜ Not Started |
| Shelf 1 | 12 | **Aquarius** | Aquarius | Base Game | 2-5 players | ~30 min | [Quick Start](guides/aquarius.md) | ⬜ Not Started |
| Shelf 1 | 13 | **Citadels** | 富饒之城 (Citadels) | Base Game | 2-8 players | ~30-60 min | [Quick Start](guides/citadels.md) | ✅ Completed |
| Shelf 1 | 14 | **Chrononauts** | Chrononauts | Base Game | 1-6 players | ~30 min | [Quick Start](guides/chrononauts.md) | ⬜ Not Started |
| Shelf 1 | 15 | **Pocket Madness** | Pocket Madness | Base Game | 2-4 players | ~20 min | [Quick Start](guides/pocket-madness.md) | ⬜ Not Started |
| Shelf 1 | 16 | **White slim box on far right** | PHANTASM... (partially obscured) | Base Game | Unclear | Unclear | [Quick Start](guides/shelf1-white-box-16.md) | 🔍 Needs Verification |
| Shelf 2 | 1 | **Unidentified dark slim box** | Dark slim box / deckbox | Unknown | Unclear | Unclear | [Quick Start](guides/shelf2-dark-box-1.md) | 🔍 Needs Verification |
| Shelf 2 | 2 | **Unearth** | Unearth | Base Game | 2-4 players | ~60 min | [Quick Start](guides/unearth.md) | ⬜ Not Started |
| Shelf 2 | 3 | **Coal Baron** | 炭鉱王 / 煤炭大亨 (Glück Auf) | Base Game | 2-4 players | ~60 min | [Quick Start](guides/coal-baron.md) | ⬜ Not Started |
| Shelf 2 | 4 | **Majesty: For the Realm** | マジェスティ (Majesty) | Base Game | 2-4 players | ~30 min | [Quick Start](guides/majesty-for-the-realm.md) | ⬜ Not Started |
| Shelf 2 | 5 | **Evolution: Plantarum** | 演化論：綠意盎然 | Expansion | 2-6 players | ~60 min | [Quick Start](guides/evolution-plantarum.md) | ⬜ Not Started |
| Shelf 2 | 6 | **Evolution** | 演化論：物種起源 | Base Game | 2-6 players | ~60 min | [Quick Start](guides/evolution-origin-of-species.md) | 🚧 In Progress |
| Shelf 2 | 7 | **Evolution: Flight / Expansion** | 演化論・擴充 | Expansion | 2-6 players | ~60 min | [Quick Start](guides/evolution-flight.md) | ⬜ Not Started |
| Shelf 2 | 8 | **Exploding Minions** | Exploding Minions | Base Game | 2-5 players | ~15 min | [Quick Start](guides/exploding-minions.md) | ⬜ Not Started |
| Shelf 2 | 9 | **Cat in the Box (Deluxe Edition)** | Cat in the Box: Deluxe Edition | Base Game | 2-5 players | ~30-45 min | [Quick Start](guides/cat-in-the-box.md) | ✅ Completed |
| Shelf 3 | 1 | **7 Wonders Duel** | 7 Wonders Duel | Base Game | 2 players | ~30 min | [Quick Start](guides/7-wonders-duel.md) | ✅ Completed |
| Shelf 3 | 2 | **8Bit Box** | 8Bit Box | Base Game | 3-6 players | ~40 min | [Quick Start](guides/8bit-box.md) | ⬜ Not Started |
| Shelf 3 | 3 | **Hit Z Road** | Hit Z Road | Base Game | 1-4 players | ~60 min | [Quick Start](guides/hit-z-road.md) | ⬜ Not Started |
| Shelf 3 | 4 | **Orbis** | Orbis | Base Game | 2-4 players | ~45 min | [Quick Start](guides/orbis.md) | ⬜ Not Started |
| Shelf 3 | 5 | **Kanagawa** | Kanagawa (神奈川) | Base Game | 2-4 players | ~45 min | [Quick Start](guides/kanagawa.md) | ⬜ Not Started |
| Shelf 3 | 6 | **Carcassonne** | Carcassonne | Base Game | 2-5 players | ~35 min | [Quick Start](guides/carcassonne.md) | ✅ Completed |
| Shelf 3 | 7 | **Valeria: Card Kingdoms** | Valeria: Card Kingdoms | Base Game | 1-5 players | ~45 min | [Quick Start](guides/valeria-card-kingdoms.md) | ⬜ Not Started |
| Shelf 3 | 8 | **Inception** | 盜夢都市 (Inception) | Base Game | 3-7 players | ~30-45 min | [Quick Start](guides/inception-boardgame.md) | ⬜ Not Started |
| Shelf 3 | 9 | **Pickomino** | 蟲蟲燒烤派對 (Heckmeck) | Base Game | 2-7 players | ~20-30 min | [Quick Start](guides/pickomino.md) | ⬜ Not Started |
| Shelf 4 | 1 | **Viracocha** | ウィラコチャ / 天空都市 | Base Game | 2-4 players | ~45 min | [Quick Start](guides/viracocha.md) | ⬜ Not Started |
| Shelf 4 | 2 | **King of Tokyo** | King of Tokyo (東京之王) | Base Game | 2-6 players | ~30 min | [Quick Start](guides/king-of-tokyo.md) | ✅ Completed |
| Shelf 4 | 3 | **Welcome to the Dungeon / Dungeon Petz?** | 老師請給分 / Hobby Japan box | Base Game | Unclear | Unclear | [Quick Start](guides/shelf4-hobby-japan-box.md) | 🔍 Needs Verification |
| Shelf 4 | 4 | **Marvel Champions: The Card Game** | Marvel Champions: The Card Game | Base Game | 1-4 players | ~45-90 min | [Quick Start](guides/marvel-champions.md) | 🚧 In Progress |
| Shelf 4 | 5 | **Azul: Stained Glass of Sintra** | Azul: Stained Glass of Sintra | Base Game | 2-4 players | ~30-45 min | [Quick Start](guides/azul-stained-glass-of-sintra.md) | ✅ Completed |
| Shelf 4 | 6 | **Terra** | Terra | Base Game | 2-6 players | ~45-60 min | [Quick Start](guides/terra.md) | ⬜ Not Started |
| Shelf 4 | 7 | **Machi Koro** | 街コロ (Machi Koro) | Base Game | 2-4 players | ~30 min | [Quick Start](guides/machi-koro.md) | ✅ Completed |
| Shelf 4 | 8 | **Arcane Academy** | Arcane Academy | Base Game | 2-4 players | ~45 min | [Quick Start](guides/arcane-academy.md) | ⬜ Not Started |
| Shelf 4 | 9 | **10 Days in the USA** | 10 Days in the USA | Base Game | 2-4 players | ~30 min | [Quick Start](guides/10-days-in-the-usa.md) | ⬜ Not Started |
| Shelf 5 | 1 | **Funkoverse Strategy Game: Harry Potter 100** | Funkoverse: Harry Potter 100 | Base Game | 2-4 players | ~20-60 min | [Quick Start](guides/funkoverse-harry-potter.md) | ⬜ Not Started |
| Shelf 5 | 2 | **Funkoverse Strategy Game: DC Comics 100** | Funkoverse: DC Comics 100 (Batman) | Base Game | 2-4 players | ~20-60 min | [Quick Start](guides/funkoverse-dc-batman.md) | ⬜ Not Started |
| Shelf 5 | 3 | **Marvel United** | Marvel United | Base Game | 1-4 players | ~40 min | [Quick Start](guides/marvel-united.md) | ✅ Completed |
| Shelf 5 | 4 | **Marvel United: Tales of Asgard** | Marvel United: Tales of Asgard | Expansion | 1-4 players | ~40 min | [Quick Start](guides/marvel-united-tales-of-asgard.md) | 🚧 In Progress |
| Shelf 5 | 5 | **Marvel United: Enter the Spider-Verse** | Marvel United: Enter the Spider-Verse | Expansion | 1-4 players | ~40 min | [Quick Start](guides/marvel-united-spider-verse.md) | ⬜ Not Started |
| Shelf 5 | 6 | **God of War: The Card Game** | God of War: The Card Game | Base Game | 1-4 players | ~60-90 min | [Quick Start](guides/god-of-war-card-game.md) | ⬜ Not Started |
| Shelf 5 | 7 | **Eclipse** | Eclipse: Second Dawn for the Galaxy | Base Game | 2-6 players | ~60-180 min | [Quick Start](guides/eclipse.md) | 🚧 In Progress |
| Shelf 5 | 8 | **How to Become President** | 大統領になる方法 (Friese) | Base Game | 3-6 players | ~45 min | [Quick Start](guides/how-to-become-president.md) | ⬜ Not Started |
| Shelf 5 | 9 | **504** | 504 | Base Game | 2-4 players | ~60-120 min | [Quick Start](guides/504-friese.md) | ⬜ Not Started |
| Shelf 5 | 10 | **Fearsome Floors** | Fearsome Floors (Finstere Flure) | Base Game | 2-7 players | ~60 min | [Quick Start](guides/fearsome-floors.md) | ⬜ Not Started |
| Shelf 6 | 1 | **Alien Frontiers** | Alien Frontiers | Base Game | 2-4 players | ~90 min | [Quick Start](guides/alien-frontiers.md) | ⬜ Not Started |
| Shelf 6 | 2 | **Kingsburg** | Kingsburg | Base Game | 2-5 players | ~90 min | [Quick Start](guides/kingsburg.md) | ⬜ Not Started |
| Shelf 6 | 3 | **Gangsi** | Gangsi (殭屍 / 僵尸) | Base Game | 2-4 players | ~30 min | [Quick Start](guides/gangsi.md) | ⬜ Not Started |
| Shelf 6 | 4 | **Small World Underground** | Small World Underground | Base Game | 2-5 players | ~40-80 min | [Quick Start](guides/small-world-underground.md) | ⬜ Not Started |
| Shelf 6 | 5 | **Small World** | Small World | Base Game | 2-5 players | ~40-80 min | [Quick Start](guides/small-world.md) | ✅ Completed |
| Shelf 6 | 6 | **Via Nebula** | Via Nebula | Base Game | 2-4 players | ~45-60 min | [Quick Start](guides/via-nebula.md) | ⬜ Not Started |
| Shelf 6 | 7 | **Evolution (North Star Games)** | Evolution (North Star Games Edition) | Base Game | 2-6 players | ~60 min | [Quick Start](guides/evolution-north-star.md) | ⬜ Not Started |
| Shelf 6 | 8 | **Machi Koro Legacy** | Machi Koro Legacy | Base Game | 2-4 players | ~30-45 min | [Quick Start](guides/machi-koro-legacy.md) | ⬜ Not Started |
| Shelf 6 | 9 | **Battle Cry** | Battle Cry (150th Civil War Edition) | Base Game | 2 players | ~60 min | [Quick Start](guides/battle-cry.md) | ⬜ Not Started |

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
