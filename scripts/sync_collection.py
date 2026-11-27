#!/usr/bin/env python3
"""
Syncs the Board Game Collection Google Sheet (published as CSV) with:
  1. data/collection.csv
  2. README.md (auto-regenerates the collection index table & progress stats)
  3. guides/*.md (creates missing stub files from templates/quick-start-template.md)

Usage:
  1. In Google Sheets: File -> Share -> Publish to web -> Select "Board Game Catalog" tab & "Comma-separated values (.csv)" -> Copy URL.
  2. Set SHEET_CSV_URL environment variable or pass --url:
       python scripts/sync_collection.py --url "https://docs.google.com/spreadsheets/d/e/.../pub?output=csv"
     Or run offline from local data/collection.csv:
       python scripts/sync_collection.py --local
"""

import argparse
import csv
import io
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "collection.csv"
README_PATH = ROOT / "README.md"


def fetch_rows(csv_url: str | None) -> list[dict[str, str]]:
    if csv_url:
        with urllib.request.urlopen(csv_url) as resp:
            raw = resp.read().decode("utf-8")
        lines = raw.splitlines()
        # Skip KPI header rows if exported directly from the styled Google Sheet tab
        header_idx = 0
        for idx, line in enumerate(lines):
            if "Shelf" in line and "Game Title" in line:
                header_idx = idx
                break
        cleaned = "\n".join(lines[header_idx:])
        reader = csv.DictReader(io.StringIO(cleaned))
        rows = []
        for r in reader:
            title = (r.get("Game Title") or "").strip()
            if not title:
                continue
            rows.append(
                {
                    "Shelf": (r.get("Shelf") or "").strip(),
                    "Position": (r.get("Pos") or r.get("Position") or "").strip(),
                    "Game Title": title,
                    "Box Title / Localized": (r.get("Box Title / Localized") or "").strip(),
                    "Type": (r.get("Type") or "Base Game").strip(),
                    "Players": (r.get("Players") or "").strip(),
                    "Play Time": (r.get("Play Time") or "").strip(),
                    "Guide Status": (r.get("Guide Status") or "Not Started").strip(),
                    "GitHub Doc Slug": (r.get("GitHub Doc Slug") or "").strip(),
                    "Notes": (r.get("Notes") or "").strip(),
                }
            )
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "Shelf",
                    "Position",
                    "Game Title",
                    "Box Title / Localized",
                    "Type",
                    "Players",
                    "Play Time",
                    "Guide Status",
                    "GitHub Doc Slug",
                    "Notes",
                ],
            )
            writer.writeheader()
            writer.writerows(rows)
        return rows

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ensure_guide_stubs(rows: list[dict[str, str]]) -> int:
    created = 0
    for r in rows:
        slug = r["GitHub Doc Slug"]
        if not slug:
            continue
        target = ROOT / slug
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            content = f"""---
title: "{r['Game Title']}"
box_title: "{r['Box Title / Localized']}"
type: "{r['Type']}"
players: "{r['Players']}"
play_time: "{r['Play Time']}"
shelf: {r['Shelf'] or 0}
position: {r['Position'] or 0}
status: "{r['Guide Status']}"
---

# {r['Game Title']} — Quick Start Guide

**Box Title:** {r['Box Title / Localized']} | **Type:** {r['Type']} | **Players:** {r['Players']} | **Play Time:** {r['Play Time']}

---

## 1. Objective
*TODO*

## 2. Setup
*TODO*

## 3. Turn Structure
*TODO*

## 4. Key Rules & Reminders
*TODO*

## 5. End-Game & Scoring
*TODO*
"""
            target.write_text(content, encoding="utf-8")
            created += 1
    return created


def update_readme(rows: list[dict[str, str]]) -> None:
    total = len(rows)
    completed = sum(1 for r in rows if r["Guide Status"] == "Completed")
    in_progress = sum(1 for r in rows if r["Guide Status"] == "In Progress")
    verify = sum(1 for r in rows if r["Guide Status"] == "Needs Verification")

    badge = {
        "Completed": "✅ Completed",
        "In Progress": "🚧 In Progress",
        "Needs Verification": "🔍 Needs Verification",
        "Not Started": "⬜ Not Started",
    }

    table_lines = [
        "| Shelf | Pos | Game Title | Box / Localized Title | Type | Players | Play Time | Guide | Status |",
        "| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- | :--- |",
    ]
    for r in rows:
        slug = r["GitHub Doc Slug"]
        guide_link = f"[Quick Start]({slug})" if slug else "—"
        st = badge.get(r["Guide Status"], r["Guide Status"])
        table_lines.append(
            f"| {r['Shelf']} | {r['Position']} | **{r['Game Title']}** | {r['Box Title / Localized']} | "
            f"{r['Type']} | {r['Players']} | {r['Play Time']} | {guide_link} | {st} |"
        )

    readme = f"""# Board Game Collection & Quick-Start Guides

A structured catalog of my board game shelf paired with concise, tabletop-ready **Quick-Start Guides** and **SVG Setup / Turn-Flow Schematics** for fast game-night refreshers.

## Collection Progress
* **Total Cataloged Games:** {total}
* **Completed Guides:** {completed} / {total}
* **In Progress:** {in_progress}
* **Needs Box Verification:** {verify}

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

{chr(10).join(table_lines)}

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
"""
    README_PATH.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync Board Game Collection README and guide stubs.")
    parser.add_argument("--url", default=os.environ.get("SHEET_CSV_URL"), help="Published Google Sheet CSV URL")
    parser.add_argument("--local", action="store_true", help="Read from local data/collection.csv")
    args = parser.parse_args()

    url = None if args.local else args.url
    records = fetch_rows(url)
    added = ensure_guide_stubs(records)
    update_readme(records)
    print(f"Synced {len(records)} games. Created {added} new guide stub(s). Updated README.md.")
