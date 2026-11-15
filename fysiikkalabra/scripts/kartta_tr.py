"""Helper for the FY9 recognition charts (docs: tyojono 9c): put a unit's chart texts into its figures.json files.
Usage: python scripts/kartta_tr.py <unit> <spec.json>
spec.json: {"en": {"aria": "...", "words": {fi: en, ...}}, "fi-easy": {"aria": "...", "words": {fi: fi-easy, ...}}}
The old aria key (the one starting with Tunnistuskaavio or Käsitekartta) is replaced by the Finnish ARIA_KARTTA of
lessons/units/<unit>/figures.py; each word is added or updated; words no longer used by figures.py are left alone."""
import json, re, sys, pathlib
unit, spec = sys.argv[1], json.load(open(sys.argv[2]))
src = pathlib.Path(f"lessons/units/{unit}/figures.py").read_text()
m = re.search(r"ARIA_KARTTA = \((.*?)\)\n\n", src, re.S)
fi_key = "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1)))
for lang, sp in spec.items():
    fp = pathlib.Path(f"content/{lang}/units/{unit}/figures.json")
    raw = fp.read_text(); d = json.loads(raw)
    indent = 1 if raw.startswith('{\n "') else 2
    old = [k for k in d if k.startswith(("Käsitekartta", "Tunnistuskaavio"))]
    nd = {}
    for k, v in d.items():
        if k in old: nd[fi_key] = sp["aria"]
        else: nd[k] = v
    if fi_key not in nd: nd[fi_key] = sp["aria"]
    nd.update(sp.get("words", {}))
    fp.write_text(json.dumps(nd, ensure_ascii=False, indent=indent) + ("\n" if raw.endswith("\n") else ""))
print("ok", unit)
