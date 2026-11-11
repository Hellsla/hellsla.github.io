"""Which pages a pull request's browser checks must test (teacher 2026-11-01: "testaa vain muuttuneet sivut").

  python scripts/ci_scope.py [<base-ref>]      prints "full", or the page ids to test (space separated; empty: none)

The three slow CI steps (test_sims.py, the per-lesson inquiry tests and check_layout.py at eight widths; together
about 1 h 30 min of a full run) open pages in a browser. On a pull request they test only the pages the change can
alter; every other check, and the whole run on main, on the weekly schedule and on a manual run, stays full.
A page id is a page's file name without .html (fy4-3, fy10-heiluri, tvt-kuvaaja, FY2-sovella) and covers that page in
every language (site/<id>.html, site/en/<id>.html, site/fi-easy/<id>.html).

A changed file maps to pages, or to nothing, or is shared. Since 2026-11-11 (teacher: one axis name must not start 33
jobs over the whole site) a shared change (a script, a template, the style sheet, shared site files, configuration,
other interface texts, the workflow) tests SMOKE, a fixed sample of pages of every kind and course, together with the
pages the change names by their own sources; the site/ HTML that a shared change re-renders on every page is then not
counted page by page. The whole site is tested by the weekly run and by a manual run (Actions -> fysiikkalabra-ci ->
Run workflow), and by a push to main whose comparison commit is not known. A push to main is scoped like a pull
request, against the commit main had before the push (github.event.before), so every commit of the push counts.
The review system's own files (scripts/reviews.py, review_packet.py, their tests, docs/presentation-only.tsv,
docs/teacher-figures.tsv) change no page: their unit tests and `reviews.py verify` run in every run.
"full" remains for: a file that decides what publishes (docs/visual-baseline.tsv), and an asset no lesson uses.
  content/<lang>/<COURSE>/<id>/**, lessons/<COURSE>/<id>/**   that page (sovella -> <COURSE>-sovella), any language
  tests/sims/<id>.json                                         that page
  assets/sims/..., assets/pics/..., assets/shared/{sims,pics}/  the lessons that use it (courses.deps());
                                                               used by none, or by an investigation or guide -> full
  lang/<lang>.json                                             only its "sims" block changed: the lessons of those
                                                               sims; any other text -> full
  site/<id>.html, site/<lang>/<id>.html, site/<id>-sim.js      that page (a lesson that publishes or unpublishes, a
                                                               neighbour whose Edellinen / Seuraava luku changed)
  site/sims/**, site/pics/**                                   nothing of its own (copies of assets/, mapped above)
  site/index.html, site/<COURSE>.html                          nothing (the course pages are not in the browser
                                                               steps; test_home.py checks them on every run)
  content/<lang>/lukuvinkit.json, site/<lang>/lukuvinkit.html  nothing (the reading list; test_home.py checks it)
  booklets/**, site/vihkot/**, site/<lang>/vihkot.html          nothing (Vihkot, the printable books; test_home.py checks it)
  content/<lang>/tietoa.md, site/<lang>/tietoa.html          nothing (Sivustosta, the about page; test_home.py checks it)
  content/<lang>/tietosuoja.md, site/<lang>/tietosuoja.html  nothing (Tietosuoja, the privacy page; test_home.py checks it)
  site/<lang>/nain-opiskelet.html                              nothing (the study guide; test_home.py checks it)
  site/<lang>/yo-sekoitin.html                                 nothing (the task mixer, scripts/mixer.py; test_home.py checks it)
  kortit/**, site/kortit/**, site/<lang>/kasitteet.html        nothing of its own: the concept cards (concept_cards.py) are
                                                               rendered into the chapters, module and Sovella pages, and
                                                               their site/ diff names them; test_home.py checks the cards
  content/<lang>/courses.json                                  nothing of its own: a module or lesson title is
                                                               rendered into the pages, and their site/ diff names them
  docs/*.md and docs/<dir>/**, *.md outside content/, tests/models/**, news/ newsletter/ tips/   nothing
  docs/visual-baseline.tsv                                     full (decides what publishes)
  scripts/, templates/, other site/ files (site.css, lesson.js, vendor/ ...), curriculum.json, competencies.json,
  glossary.json, local-courses.json, the workflow file                                             full
The site/ rows are sound because CI fails unless the committed site/ is exactly a fresh render of the sources:
every page whose HTML a change alters is in the pull request's diff.
"""
import json, re, subprocess, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses
from courses import ROOT

LANG = r"[a-z]{2,3}(?:-[a-z]+)?"
REVIEW_SYSTEM = re.compile(r"scripts/(?:reviews|review_packet|test_reviews|ci_scope|ci_parallel|test_ci_parallel)\.py")   # tested by their own unit tests and reviews.py verify in every run; they render no page
SMOKE = ("fy1-1", "fy2-1", "fy3-5", "fy3-10", "fy4-14", "fy5-8", "fy5-14", "fy6-2", "fy7-3", "fy8-15", "FY3-sovella", "lumatutor-tyopaja-ilmastodata")   # one or two pages of every course and kind, the ones that have failed before first; at most 12, so one job per check
NOTHING = re.compile(rf"(?:docs/(?!visual-baseline\.tsv$).+|(?!content/)[^/]+\.md|(?!content/).+/README\.md|tests/models/.+|(?:news|newsletter|tips)/.+"
                     rf"|site/(?:sims|pics|kortit|vihkot)/.+|kortit/.+|booklets/.+|content/{LANG}/(?:courses|lukuvinkit)\.json|content/{LANG}/(?:tietoa|tietosuoja)\.md|site/(?:{LANG}/)?(?:index|FY\d+|lukuvinkit|vihkot|nain-opiskelet|tietoa|tietosuoja|kasitteet|yo-sekoitin)\.html)")


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def page_of(course, lid):
    return f"{course}-{lid}" if lid in ("sovella", "koe") else lid


def scope(base):
    """("full", reason) or ("pages", {page id: [why, ...]})."""
    names = git("diff", "--name-only", "--relative", f"{base}...HEAD").split()
    # the workflow first: it lies outside fysiikkalabra/, so a pull request that changes nothing else has no name above,
    # and returning "no page" for it skipped every browser check of a change to how they are run (2026-11-11)
    wf = git("diff", "--name-only", f"{base}...HEAD", "--", f"{git('rev-parse', '--show-toplevel').strip()}/.github/").split()
    shared = [f"workflow changed: {wf[0]}"] if wf else []
    if not names and not shared: return "pages", {}
    deps, pages, rendered = courses.deps(), {}, {}
    add = lambda p, n: pages.setdefault(p, []).append(n)
    for n in names:
        if NOTHING.fullmatch(n) or REVIEW_SYSTEM.fullmatch(n): continue
        if n == "docs/visual-baseline.tsv": return "full", f"{n}: decides what publishes"
        m = re.fullmatch(rf"content/{LANG}/([^/]+)/([^/]+)/.+", n) or re.fullmatch(r"lessons/([^/]+)/([^/]+)/.+", n)
        if m: add(page_of(*m.groups()), n); continue
        m = re.fullmatch(r"tests/sims/([^/]+)\.json", n)
        if m: add(m.group(1), n); continue
        m = re.fullmatch(rf"site/(?:{LANG}/)?([^/]+)\.html", n) or re.fullmatch(r"site/([^/]+)-sim\.js", n)
        if m: rendered.setdefault(m.group(1), []).append(n); continue   # counted below, unless a shared change re-rendered every page
        m = re.fullmatch(r"assets/((?:sims/[^/]+|shared/sims)/[^/]+)/.+", n) or re.fullmatch(r"assets/((?:pics/[^/]+|shared/pics)/[^/]+)", n)
        if m:
            users = deps.get(m.group(1), [])
            if not users: return "full", f"{n}: no lesson uses it (an investigation, a guide or a new asset)"
            for u in users: add(u, n)
            continue
        if re.fullmatch(rf"lang/{LANG}\.json", n):
            old = json.loads(subprocess.run(["git", "show", f"{base}:./{n}"], cwd=ROOT, capture_output=True, text=True).stdout or "{}")
            new = json.loads((ROOT / n).read_text()) if (ROOT / n).exists() else {}
            if {k: v for k, v in old.items() if k != "sims"} != {k: v for k, v in new.items() if k != "sims"}:
                shared.append(f"{n}: interface texts changed")
            o, w = old.get("sims", {}), new.get("sims", {})
            for key in sorted(k for k in set(o) | set(w) if o.get(k) != w.get(k)):
                users = [key] if any(f.name == key for f in courses.lessons()) else deps.get(next((d for d in deps if d.endswith(f"/{key}")), ""), [])
                if not users: return "full", f"{n} sims.{key}: no lesson uses it"
                for u in users: add(u, f"{n} sims.{key}")
            continue
        shared.append(f"{n}: shared by every page (scripts, templates, site files, configuration)")
    if shared:                                          # the sample, and the pages the change names by their own sources
        for q in SMOKE: add(q, f"smoke sample ({shared[0]})")
    else:
        for q, why in rendered.items(): pages.setdefault(q, []).extend(why)
    return "pages", pages


if __name__ == "__main__":
    kind, what = scope(sys.argv[1] if len(sys.argv) > 1 else "origin/main")
    if kind == "full":
        print("full"); print(f"full run: {what}", file=sys.stderr)
    else:
        print(" ".join(sorted(what)))
        for p, why in sorted(what.items()): print(f"{p}: {', '.join(why[:3])}{' …' if len(why) > 3 else ''}", file=sys.stderr)
        if not what: print("no page changed: the browser steps have nothing to test", file=sys.stderr)
