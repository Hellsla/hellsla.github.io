#!/usr/bin/env python3
"""Pick one unfinished curriculum lesson without calling any AI service."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def select(skip=(), course=None):
    curriculum = json.loads((ROOT / "curriculum.json").read_text())
    statuses = {}
    for path in (ROOT / "content").glob("*/*/meta.json"):
        if path.parent.parent.name == "_gold":
            continue
        meta = json.loads(path.read_text())
        statuses[meta["id"]] = meta.get("status", "draft")
    options = []
    for order, (code, module) in enumerate(curriculum.items()):
        if code.startswith("_") or (course and code != course):
            continue
        for index, lesson in enumerate(module.get("lessons", [])):
            lid = lesson["id"]
            if lid in skip or statuses.get(lid) == "reviewed":
                continue
            folder = ROOT / "content" / code / lid
            existing = (folder / "meta.json").exists()
            missing = [p for p in lesson.get("prerequisites", []) if statuses.get(p) != "reviewed"]
            priority = (bool(missing), not existing, order, index)
            options.append((priority, {
                "id": lid, "course": code, "title": lesson["title"],
                "mode": "continue_draft" if existing else "create_draft",
                "pending_prerequisites": missing,
                "simulation": bool(lesson.get("sim", False))
            }))
    return min(options, key=lambda x: x[0])[1] if options else None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip", action="append", default=[])
    parser.add_argument("--course")
    args = parser.parse_args()
    print(json.dumps({"next_lesson": select(args.skip, args.course)}, ensure_ascii=False, indent=2))
