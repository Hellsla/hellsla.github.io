#!/usr/bin/env python3
"""Export committed metadata only. Never reads Claude sessions or modifies lesson files."""
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import tempfile
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def export():
    raw = subprocess.run(
        ["git", "log", "--first-parent", "--diff-merges=first-parent", "-200", "--date=iso-strict",
         "--format=%x1e%H%x00%cI%x00%s", "--name-only"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout
    events = []
    for record in raw.split("\x1e"):
        if not record.strip():
            continue
        header, *paths = record.strip().splitlines()
        sha, timestamp, title = header.split("\x00", 2)
        files = [p.strip() for p in paths if p.strip()]
        roles = []
        if any(p.startswith("fysiikkalabra/content/") and "/review/" not in p for p in files):
            roles.append("developer")
        if any(p.endswith("/review/science.md") for p in files):
            roles.append("science")
        if any(p.endswith("/review/pedagogy.md") for p in files):
            roles.append("pedagogy")
        local = dt.datetime.fromisoformat(timestamp).astimezone(ZoneInfo("Europe/Helsinki"))
        events.append({"id": sha, "timestamp": local.isoformat(), "day": local.date().isoformat(),
                       "minute": local.hour * 60 + local.minute + local.second / 60,
                       "title": title, "roles": roles or ["repository"], "files": len(files),
                       "merge": title.startswith("Merge ")})
    events.sort(key=lambda e: (e["timestamp"], e["id"]))
    payload = {"repository": "Hellsla/hellsla.github.io", "timezone": "Europe/Helsinki",
               "exportedAt": dt.datetime.now(dt.timezone.utc).isoformat(), "events": events}
    content = "window.OFFICE_HISTORY = " + json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c") + ";\n"
    # The only write is an atomic replacement inside this feature's directory.
    handle, temporary = tempfile.mkstemp(prefix=".history-", dir=HERE)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as output:
            output.write(content)
        os.replace(temporary, HERE / "history.js")
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print(f"Exported {len(events)} commits across {len({e['day'] for e in events})} days to agent-office/history.js")


if __name__ == "__main__":
    export()
