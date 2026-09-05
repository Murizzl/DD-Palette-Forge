#!/usr/bin/env python3
from pathlib import Path
import json, re, datetime

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / "library"
OUT = LIB / "index.json"

ALLOWED = {".png", ".skel", ".atlas"}

def pretty(name):
    return name.replace("_"," ").replace("-"," ").strip().title()

def roster_for(files):
    for f in files:
        if f.name.lower().endswith("_portrait_roster.png"):
            return f.as_posix()
    for f in files:
        if f.suffix.lower()==".png":
            return f.as_posix()
    return None

packs = []

for category in ("vanilla","mods"):
    base = LIB / category
    if not base.exists():
        continue

    for hero_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        # Each direct child is normally one skin. If there are files directly
        # in the hero directory, treat that directory as one pack too.
        candidates = [p for p in hero_dir.iterdir() if p.is_dir()]
        if any(p.is_file() and p.suffix.lower() in ALLOWED for p in hero_dir.iterdir()):
            candidates.insert(0, hero_dir)

        for skin_dir in candidates:
            files = sorted(
                p for p in skin_dir.rglob("*")
                if p.is_file() and p.suffix.lower() in ALLOWED
            )
            if not files:
                continue

            rel_files = [p.relative_to(ROOT).as_posix() for p in files]
            roster = roster_for(files)
            roster_rel = roster_for(files)
            if roster_rel:
                roster_rel = Path(roster_rel).relative_to(ROOT).as_posix()

            skin_name = pretty(skin_dir.name if skin_dir != hero_dir else "Default")
            slot_match = re.search(r"_([A-Za-z0-9]+)$", skin_dir.name)
            slot = slot_match.group(1).upper() if slot_match else ""

            packs.append({
                "id": f"{category}_{hero_dir.name}_{skin_dir.name}".lower(),
                "hero": hero_dir.name.lower(),
                "name": skin_name,
                "type": "default" if category=="vanilla" else "community",
                "heroType": "vanilla" if category=="vanilla" else "mod",
                "author": "Base Game" if category=="vanilla" else "Community",
                "slot": slot,
                "thumbnail": roster_rel,
                "files": [{"path": rel, "url": rel} for rel in rel_files]
            })

data = {
    "version": 1,
    "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "packs": packs
}
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {OUT} with {len(packs)} packs.")
