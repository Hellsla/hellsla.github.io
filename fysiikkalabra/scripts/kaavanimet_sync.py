"""Rewrite one FY9 unit's rows of docs/fy9/kaavanimet.tsv from its texts as they are now: one row per display formula
(fi and en, in text order), each keeping the name, English name, source, MAFY page and note its formula had before.
Used when formulas are taken out of a unit (teacher 2026-11-12: a result the exam asks to derive is a "Johda itse"
task, ```johda, not a formula of its own); `kaavat.py write --check` must pass afterwards.

  python scripts/kaavanimet_sync.py <unit-id>...
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import kaavat, units

P = kaavat.NAMES


def sync(uid):
    lines = P.read_text(encoding="utf-8").split("\n")
    head_i = next(i for i, l in enumerate(lines) if l.startswith("yksikkö\t"))
    head = lines[head_i].split("\t")
    rows = [dict(zip(head, l.split("\t"))) for l in lines[head_i + 1:] if l]
    old = {r["kaava"]: r for r in rows if r["yksikkö"] == uid}
    fi = (units.folder(uid, "fi") / "unit.md").read_text(encoding="utf-8")
    en = (units.folder(uid, "en") / "unit.md").read_text(encoding="utf-8")
    bf, be = kaavat._blocks(fi), kaavat._blocks(en)
    pf = [(fi[:m.start()].count("\n") + 1, p) for m, ps in bf for p in ps]
    pe = [p for _, ps in be for p in ps]
    if len(pf) != len(pe): sys.exit(f"{uid}: fi has {len(pf)} display formulas, en {len(pe)}")
    new = []
    for (line, a), b in zip(pf, pe):
        r = dict(old.get(a, {k: "" for k in head}))
        r.update({"yksikkö": uid, "rivi": str(line), "kaava": a, "kaava_en": b})
        new.append(r)
    first = next(i for i, r in enumerate(rows) if r["yksikkö"] == uid)
    rows = rows[:first] + new + [r for r in rows[first:] if r["yksikkö"] != uid]
    gone = sorted(set(old) - {r["kaava"] for r in new})
    P.write_text("\n".join(lines[:head_i + 1] + ["\t".join(r.get(k, "") for k in head) for r in rows]) + "\n", encoding="utf-8")
    print(f"{uid}: {len(new)} rows" + (f"; taken out: {gone}" if gone else ""))


if __name__ == "__main__":
    for uid in sys.argv[1:]: sync(uid)
