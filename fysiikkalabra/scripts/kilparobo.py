"""Kilparobotiikka (teacher's brief 2026-11-09): Kiviruukin lukio's VEX V5 competition team as a student-led learning and
working environment, in the school's colours like its course page (local-courses.json KILPAROBO, "theme": "kiviruukki").

jaksot/kilparobo/jakso.json is the source (Finnish); jaksot/kilparobo/<lang>/jakso.json has the same shape in another
language, and a language without one shows the Finnish (fi-easy). Since 2026-11-12 the unit is written as pages of
blocks and drawn by scripts/jaksot.py alone (its block library began as this file's page functions): a text, a card, a
stage, a phase or a link is changed in jakso.json, never here. Five pages in every language that has the course:
  KILPAROBO.html                 the start page: what the team is and how to join (five quick answers first), how the
                                 team works, the team's tools, what it is doing now, competitions and experiences (the
                                 course's photos and quotes from local-courses.json, never duplicated), Ahjo 1 and 2
  kilparobo-polku.html           the beginner's path: five stages, each with a goal, a practice, a mentor's tip and a way
                                 to show the skill; the official VEX technical guides and the Ruukkilabra chapters behind them
  kilparobo-kausi.html           the competition season in eight phases (no dates, no game: the game changes every season)
                                 and the team's development diary with a template to copy or download (nothing is stored)
  kilparobo-mentorointi.html     mentoring (students teach students) and a light model for making skills visible
  kilparobo-turvallisuus.html    safety: the mentor's and the teacher's parts kept apart; a draft until the school approves

What stays here is what only this unit has, the rules of the brief, checked by validate(): no dates, credits or season
rules invented (the "nyt" block's text and updated are the teacher's to fill; an empty one says so); every external
link is https on VEX's or RECF's own sites (OFFICIAL_HOSTS); a Ruukkilabra chapter (refs) is linked only where it is
published; VEX only here, Ahjo's robotics is Arduino; eight season phases and five path stages.

  python scripts/kilparobo.py   validate (also run by build.py)
"""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, jaksot

JAKSO = "kilparobo"                    # jaksot/kilparobo/ (scripts/jaksot.py)
SOURCE = jaksot.source(JAKSO)
CODE = "KILPAROBO"
PAGE, PATH, SEASON, MENTOR, SAFETY = "KILPAROBO.html", "kilparobo-polku.html", "kilparobo-kausi.html", "kilparobo-mentorointi.html", "kilparobo-turvallisuus.html"
SUBPAGES = (PATH, SEASON, MENTOR, SAFETY)
OFFICIAL_HOSTS = ("kb.vex.com", "www.vexrobotics.com", "api.vex.com", "www.robotevents.com", "www.roboticseducation.org", "kb.roboticseducation.org")


def data_file(lang=i18n.SOURCE): return jaksot.data_file(JAKSO, lang)
def load(lang=i18n.SOURCE): return jaksot.load(JAKSO, lang)
def block(d, kind): return jaksot.block(d, kind)          # the unit's block of a type: "nyt", "polku", "kausi", "turva-aiheet", "varoitukset" …
def page(d, file): return next(p for p in d["pages"] if p["file"] == file)


def validate(lesson_ids):
    """Errors against the brief in jakso.json and its translations (the structure itself is jaksot.validate's)."""
    if not SOURCE.is_file(): return []
    errs, d = [], load()
    if [p["file"] for p in d["pages"]] != [PAGE, *SUBPAGES]: errs.append(f"jaksot/{JAKSO}: the pages are {[PAGE, *SUBPAGES]} in this order")
    for lang in [i18n.SOURCE] + [l for l in i18n.languages() if data_file(l) != SOURCE]:
        x = load(lang); name = jaksot._rel(data_file(lang))
        for u in jaksot.urls(x):
            m = re.match(r"https://([^/]+)/", u)
            if not m or m.group(1) not in OFFICIAL_HOSTS: errs.append(f"{name}: {u} is not https on an official VEX/RECF site (OFFICIAL_HOSTS)")
        now, season, path = block(x, "nyt"), block(x, "kausi"), block(x, "polku")
        if not (now and season and path and block(x, "turva-aiheet") and block(x, "varoitukset")): errs.append(f"{name}: the unit has its nyt, kausi, polku, varoitukset and turva-aiheet blocks"); continue
        if not (isinstance(now["phase"], int) and 0 <= now["phase"] <= len(season["phases"])): errs.append(f"{name}: nyt.phase must be 0 (none) or a phase's number")
        if now["text"] and not re.fullmatch(r"\d{1,2}\.\d{1,2}\.\d{4}", now["updated"]): errs.append(f"{name}: nyt.text needs nyt.updated as d.m.yyyy")
        if len(season["phases"]) != 8 or len(path["stages"]) != 5: errs.append(f"{name}: 8 season phases and 5 path stages (the brief)")
    path = block(d, "polku")
    for s in path["stages"] if path else []:
        bad = [r for r in s["refs"] if r not in lesson_ids]
        if bad: errs.append(f"jaksot/{JAKSO}: stage {s['id']} refs unknown chapters {bad}")
    if re.search(r"\bArduino\b", json.dumps(page(d, PATH), ensure_ascii=False)): errs.append(f"jaksot/{JAKSO}: the VEX path names Arduino (Ahjo's robotics is Arduino, VEX only here)")
    return errs


# --- the pages: jakso.json's blocks, drawn by jaksot.py ------------------------------------------------------------------
def hub_body(d, head, photos, quotes):
    """The start page. head: the course page's title block (local_courses.head); photos, quotes: its photo grid and the
    students' quotes (local_courses.photos_html, quotes_html), shown under Kilpailut ja kokemukset."""
    return jaksot.page_body(JAKSO, d, PAGE, ctx={"head": head, "photos": photos, "quotes": quotes})


def path_body(d, ref):
    """ref(lesson id) -> (title, href) of a published Ruukkilabra chapter, None where it is not published."""
    return jaksot.page_body(JAKSO, d, PATH, ctx={"ref": ref})


def season_body(d, diary_href=None):
    """diary_href: Ahjo's project diary guide where it is built, for the longer guide and criteria."""
    return jaksot.page_body(JAKSO, d, SEASON, ctx={"has": lambda href: href == diary_href})


def mentor_body(d): return jaksot.page_body(JAKSO, d, MENTOR)


def safety_body(d, ahjo_href=None):
    return jaksot.page_body(JAKSO, d, SAFETY, ctx={"has": lambda href: href == ahjo_href})


def template_text(d): return jaksot.template_text(block(d, "paivakirja"))


if __name__ == "__main__":
    cur = json.loads((ROOT / "curriculum.json").read_text())
    ids = {l["id"] for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", [])}
    e = jaksot.validate_pages(JAKSO) + validate(ids)
    print("\n".join(e) or "kilparobo.json OK")
    sys.exit(1 if e else 0)
