"""Rewrite one FY9 unit's rows of docs/fy9/kaavanimet.tsv (or one lesson's rows of docs/<module>/kaavanimet.tsv) from its texts as they are now: one row per display formula
(fi and en, in text order), each keeping the name, English name, source, MAFY page and note its formula had before.
Used when formulas are taken out of a unit (teacher 2026-11-12: a result the exam asks to derive is a "Johda itse"
task, ```johda, not a formula of its own); `kaavat.py write --check` must pass afterwards.

  python scripts/kaavanimet_sync.py <unit-or-lesson-id>...
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import kaavat, units

P = kaavat.NAMES


def sync(uid):
    unit = uid.startswith("fy9-")
    P = kaavat.NAMES if unit else kaavat.ROOT / "docs" / uid.split("-")[0] / "kaavanimet.tsv"
    key = "yksikkö" if unit else "tunti"
    text_of = (lambda lang: (units.folder(uid, lang) / "unit.md").read_text(encoding="utf-8")) if unit else \
              (lambda lang: kaavat.text_file("tunti", uid, lang).read_text(encoding="utf-8"))
    lines = P.read_text(encoding="utf-8").split("\n")
    head_i = next(i for i, l in enumerate(lines) if l.startswith(key + "\t"))
    head = lines[head_i].split("\t")
    rows = [dict(zip(head, l.split("\t"))) for l in lines[head_i + 1:] if l]
    old = {}
    for r in rows:
        if r[key] == uid: old.setdefault(r["kaava"], []).append(r)   # the k-th row of a formula keeps the k-th row's name
    fi, en = text_of("fi"), text_of("en")
    bf, be = kaavat._blocks(fi), kaavat._blocks(en)
    pf = [(fi[:m.start()].count("\n") + 1, p) for m, ps in bf for p in ps]
    pe = [p for _, ps in be for p in ps]
    if len(pf) != len(pe): sys.exit(f"{uid}: fi has {len(pf)} display formulas, en {len(pe)}")
    new, seen = [], {}
    for (line, a), b in zip(pf, pe):
        k = seen.get(a, 0); seen[a] = k + 1
        was = old.get(a, [])
        r = dict(was[k] if k < len(was) else {c: "" for c in head})
        r.update({key: uid, "rivi": str(line), "kaava": a, "kaava_en": b})
        new.append(r)
    first = next(i for i, r in enumerate(rows) if r[key] == uid)
    rows = rows[:first] + new + [r for r in rows[first:] if r[key] != uid]
    gone = sorted(set(old) - {r["kaava"] for r in new})
    P.write_text("\n".join(lines[:head_i + 1] + ["\t".join(r.get(k, "") for k in head) for r in rows]) + "\n", encoding="utf-8")
    print(f"{uid}: {len(new)} rows" + (f"; taken out: {gone}" if gone else ""))


if __name__ == "__main__":
    for uid in sys.argv[1:]: sync(uid)
