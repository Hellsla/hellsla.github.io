"""Oikotiet (work queue 33.3): the row of shortcuts at the start of a FY9 unit's page, straight to the part a student came for. A regular review unit
(its chapter, "Liike kuvaajina" first): "Testaa lähtötasosi" (the unit's Lähtötaso predictions, stage Ennusta), "Kertaa teoria" (Teoria) and "Ratkaise yo-tyylinen tehtävä"
(the unit's first long task, its core task, whose situation is in view at once). The practice exam (fy9-harjoituskoe) uses its own names, taken from its own
headings: "Kokeen ohjeet", "Osa I", "Osa II", "Osa III" (nothing is written for them). Presentation only: no id, text or answer of a unit changes."""
import json, re

COURSE = "FY9"
EXAM = "fy9-harjoituskoe"


def is_fy9(folder):
    f = folder / "unit.json"
    try: return folder.parent.name == "units" and json.loads(f.read_text(encoding="utf-8")).get("course") == COURSE
    except (OSError, ValueError): return False


def _tasks(folder):
    f = folder / "sovella" / "tasks.json"
    try: return json.loads(f.read_text(encoding="utf-8")).get("tasks", [])
    except (OSError, ValueError): return []


def _first(tasks, part):
    return next((t for t in tasks if re.match(rf"{re.escape(part)}\b", t.get("title") or "")), None)


def _heading(folder, key):
    """The unit.md heading of a section key ("## Kokeen ohjeet {Ohjeet}" -> "Kokeen ohjeet"); the key itself when there is none."""
    try: text = (folder / "unit.md").read_text(encoding="utf-8")
    except OSError: return key
    m = re.search(rf"^##\s+(.+?)\s*\{{{re.escape(key)}\}}\s*$", text, re.M)
    return m.group(1) if m else key


def items(T, folder, acts, by_stage):
    """[(label, href)] for the unit; [] where the unit is not one of FY9's."""
    if not is_fy9(folder): return []
    tasks = _tasks(folder)
    if folder.name == EXAM:
        out = []
        ohjeet = next((a for a in acts if a["id"] == "ohjeet" and a.get("sections")), None)
        if ohjeet: out.append((_heading(folder, ohjeet["sections"][0]), "#ohjeet"))
        osa1 = next((a for a in acts if a["id"] == "osa-1" and a.get("title")), None)
        if osa1: out.append((osa1["title"].split(":")[0].strip(), "#osa-1"))
        for part in sorted({(t.get("title") or "").split(":")[0].strip() for t in tasks if ":" in (t.get("title") or "")}):
            t = _first(tasks, part)
            if t: out.append((part, "#" + t["id"]))
        return out
    out = []
    if by_stage.get("ennusta"): out.append((T("inquiry.sc_level"), "#ennusta"))
    if by_stage.get("selita"): out.append((T("inquiry.sc_theory"), "#selita"))
    if tasks: out.append((T("inquiry.sc_task"), "#" + tasks[0]["id"]))
    return out


def html(esc, rows):
    if not rows: return ""
    return '<p class="unit-short">' + "".join(f'<a href="{esc(h)}">{esc(l)}</a>' for l, h in rows) + "</p>"
