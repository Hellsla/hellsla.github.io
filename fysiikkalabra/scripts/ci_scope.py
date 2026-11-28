"""Which pages a pull request's browser checks must test (teacher 2026-11-01: "testaa vain muuttuneet sivut").

  python scripts/ci_scope.py <base-ref> --built <base site dir> <head site dir>
                                               prints "full", or the page ids to test (space separated; empty: none)
  python scripts/ci_scope.py --changed <base site dir> <head site dir>
                                               the pages two renders differ in: added, removed and changed (a PR's step summary)

Since work queue 0g PR 2 (2026-11-22) the site/ rows come from two renders of the site (the base commit's and this one's,
built in CI's plan job), never from a committed site/ diff: a `site/` path in the git diff is ignored.

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
docs/teacher-figures.tsv, docs/teacher-text.tsv) change no page: their unit tests and `reviews.py verify` run in every run.
"full" remains for: a file that decides what publishes (docs/visual-baseline.tsv), and an asset no lesson uses.
  content/<lang>/<COURSE>/<id>/**, lessons/<COURSE>/<id>/**   that page (sovella -> <COURSE>-sovella), any language
  lessons/<COURSE>/ASETTELU.tsv                                the pages of the figures it lists and the pages that show one
                                                               (the picture layout, scripts/figimage.py; work queue 24)
  tests/sims/<id>.json                                         that page
  assets/sims/..., assets/pics/..., assets/shared/{sims,pics}/  the lessons that use it (courses.deps());
                                                               used by none, or by an investigation or guide -> full
  lang/<lang>.json                                             only its "sims" block changed: the lessons of those
                                                               sims; any other text -> full
  site/<id>.html, site/<lang>/<id>.html, site/<id>-sim.js      (rows of the two renders' difference) that page (a lesson that
                                                               publishes or unpublishes, a neighbour whose Edellinen / Seuraava
                                                               luku changed); a page whose only change is ?v= cache tokens: nothing
  site/sims/**, site/pics/**                                   nothing of its own (copies of assets/, mapped above)
  site/index.html, site/<COURSE>.html                          nothing (the course pages are not in the browser
                                                               steps; test_home.py checks them on every run)
  content/<lang>/lukuvinkit.json, site/<lang>/lukuvinkit.html  nothing (the reading list; test_home.py checks it)
  booklets/**, site/vihkot/**, site/<lang>/vihkot.html          nothing (Vihkot, the printable books; test_home.py checks it)
  content/<lang>/tietoa.md, site/<lang>/tietoa.html          nothing (Sivustosta, the about page; test_home.py checks it)
  content/<lang>/tietosuoja.md, site/<lang>/tietosuoja.html  nothing (Tietosuoja, the privacy page; test_home.py checks it)
  site/<lang>/nain-opiskelet.html                              nothing (the study guide; test_home.py checks it)
  site/<lang>/kaavat.html                                      nothing (the formula index, scripts/kaavahakemisto.py, 17f PR 1; test_home.py and test_kaavat.py check it)
  site/<lang>/simulaatiot.html                                  nothing (the simulation gallery, scripts/simulaatiogalleria.py, 17f PR 2; test_home.py and test_kaavat.py check it)
  site/<lang>/yo-sekoitin.html                                 nothing (the task mixer, scripts/mixer.py; test_home.py checks it)
  site/<lang>/FY9-valmentaja.html                              nothing (the FY9 coach page, 11b PR 4; test_valmentaja_coach.py checks it in every run)
  site/<lang>/fy9-minikoe-*.html                               nothing of its own (the FY9 minikoe pages, 11b PR 6: cut out of the unit pages, which are in the plan; test_koetila.py and a layout step check them in every run)
  kertaus/**, site/<lang>/valmentaja/*.json, scripts/valmentaja.py, test_valmentaja.py   nothing (the FY9 task index, 11b PR 2: data, no page; test_valmentaja.py runs every run)
  kortit/**, site/kortit/**, site/<lang>/kasitteet.html        nothing of its own: the concept cards (concept_cards.py) are
                                                               rendered into the chapters, module and Sovella pages, and
                                                               their site/ diff names them; test_home.py checks the cards
  content/<lang>/courses.json                                  nothing of its own: a module or lesson title is
                                                               rendered into the pages, and their site/ diff names them
  docs/*.md and docs/<dir>/**, *.md outside content/, tests/models/**, news/ newsletter/ tips/   nothing
  docs/visual-baseline.tsv                                     full (decides what publishes)
  templates/sw.js, templates/offline.js, site/sw.js, site/offline.js                shared (every page registers the worker): smoke; scripts/test_offline.py runs in every run
  scripts/, templates/, other site/ files (site.css, lesson.js, vendor/ ...), curriculum.json, competencies.json,
  glossary.json, local-courses.json, the workflow file                                             full
The site/ rows are sound because they come from rendering both commits: every page whose HTML a change alters differs
between the two renders (checks-3 fails if the build is not deterministic).
"""
import json, re, subprocess, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses
from courses import ROOT

LANG = r"[a-z]{2,3}(?:-[a-z]+)?"
REVIEW_SYSTEM = re.compile(r"scripts/(?:reviews|review_packet|test_reviews|ci_scope|ci_parallel|test_ci_parallel|valmentaja|test_valmentaja)\.py")   # tested by their own unit tests and reviews.py verify in every run; they render no page
SMOKE = ("fy1-1", "fy2-1", "fy3-5", "fy3-10", "fy4-14", "fy5-8", "fy5-14", "fy6-2", "fy7-3", "fy8-15", "FY3-sovella", "lumatutor-tyopaja-ilmastodata")   # one or two pages of every course and kind, the ones that have failed before first; at most 12, so one job per check
NOTHING = re.compile(rf"(?:docs/(?!visual-baseline\.tsv$).+|(?!content/)[^/]+\.md|(?!content/).+/README\.md|tests/models/.+|(?:news|newsletter|tips)/.+"
                     rf"|site/(?:sims|pics|kortit|vihkot)/.+|kortit/.+|kertaus/.+|site/(?:{LANG}/)?valmentaja/.+|booklets/.+|content/{LANG}/(?:courses|lukuvinkit)\.json|content/{LANG}/(?:tietoa|tietosuoja)\.md|site/(?:{LANG}/)?(?:index|FY\d+(?:-valmentaja)?|lukuvinkit|vihkot|nain-opiskelet|tietoa|tietosuoja|kasitteet|kaavat|simulaatiot|yo-sekoitin)\.html|site/(?:{LANG}/)?fy9-minikoe-[a-z0-9-]+\.html)")


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def page_of(course, lid):
    return f"{course}-{lid}" if lid in ("sovella", "koe") else lid


def set_deps():
    """{picture: [page ids]} of the course Sovella and exam pages (FY4-sovella, FY4-koe): courses.deps() walks the lessons only, so a
    picture of a task set had no user and the change was a full run (work queue 24). The pictures are the same files in every
    language, so the Finnish texts decide."""
    out = {}
    for d in sorted((courses.ROOT / "content" / courses.SOURCE_LANG).glob("*/*")):
        if d.name not in ("sovella", "koe") or d.parent.name not in courses.codes(): continue
        texts = [(d / n).read_text() for n in ("tasks.json", "solutions.md") if (d / n).is_file()]
        for r in courses.pic_refs_in(texts): out.setdefault(r, []).append(page_of(d.parent.name, d.name))
    for d in sorted((courses.ROOT / "content").glob("*/units/*")) + sorted((courses.ROOT / "content").glob("*/tutkimukset/*")):   # a unit's or an investigation's figures drawn on pictures (scripts/figimage.py): the unit page
        for r in courses.pic_refs_in([f.read_text() for f in d.glob("*") if f.suffix in (".md", ".json")]):
            if d.name not in out.setdefault(r, []): out[r].append(d.name)
    return out


def scope(base, built):
    """("full", reason) or ("pages", {page id: [why, ...]}).
    built = (base_site_dir, head_site_dir): the two renders give the site/ rows; a committed site/ diff is not read (work queue 0g)."""
    names = [n for n in git("diff", "--name-only", "--relative", f"{base}...HEAD").split() if not n.startswith("site/")] + built_names(*built)
    # the workflow first: it lies outside fysiikkalabra/, so a pull request that changes nothing else has no name above,
    # and returning "no page" for it skipped every browser check of a change to how they are run (2026-11-11)
    wf = git("diff", "--name-only", f"{base}...HEAD", "--", f"{git('rev-parse', '--show-toplevel').strip()}/.github/").split()
    shared = [f"workflow changed: {wf[0]}"] if wf else []
    if not names and not shared: return "pages", {}
    deps, pages, rendered = courses.deps(), {}, {}
    for r, us in set_deps().items(): deps.setdefault(r, []).extend(us)   # the task-set pages use pictures too
    add = lambda p, n: pages.setdefault(p, []).append(n)
    for n in names:
        if NOTHING.fullmatch(n) or REVIEW_SYSTEM.fullmatch(n): continue
        if n == "docs/visual-baseline.tsv": return "full", f"{n}: decides what publishes"
        m = re.fullmatch(rf"content/{LANG}/([^/]+)/([^/]+)/.+", n) or re.fullmatch(r"lessons/([^/]+)/([^/]+)/.+", n)
        if m: add(page_of(*m.groups()), n); continue
        m = re.fullmatch(r"lessons/([^/]+)/ASETTELU\.tsv", n)      # the picture layout of a module (scripts/figimage.py): the pages of the figures it lists, and every page that shows one
        if m:
            import figimage
            for fid in figimage.layout(m.group(1)):
                add(re.sub(r"^([a-z]+\d+)-(koe|sovella)$", lambda m: page_of(m.group(1).upper(), m.group(2)), fid.split("/")[0]), n)   # fy4-koe/x is the page FY4-koe
                for u in deps.get(figimage.pic(fid), []): add(u, n)
            continue
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


VER = re.compile(r"\?v=[0-9a-f]*")


def changed_pages(base_dir, head_dir):
    """(added, removed, changed) HTML pages (paths under site/) between two renders; ?v= tokens alone are no change."""
    names = built_names(base_dir, head_dir)
    base_dir, head_dir = pathlib.Path(base_dir), pathlib.Path(head_dir)
    add, gone, ch = [], [], []
    for n in names:
        if not n.endswith(".html"): continue
        rel = n[len("site/"):]
        (ch if (base_dir / rel).is_file() and (head_dir / rel).is_file() else add if (head_dir / rel).is_file() else gone).append(rel)
    return add, gone, ch


def built_names(base_dir, head_dir):
    """The site/ paths (as `site/<path>`) that differ between two renders of the site, as the committed site/ diff names
    them (work queue 0g): added, removed or changed files; a page that differs only in its ?v= cache tokens is equal."""
    base_dir, head_dir = pathlib.Path(base_dir), pathlib.Path(head_dir)
    files = lambda d: {p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file()}
    a, b, out = files(base_dir), files(head_dir), []
    for rel in sorted(a | b):
        if rel in a and rel in b:
            x, y = (base_dir / rel).read_bytes(), (head_dir / rel).read_bytes()
            if x == y: continue
            if rel.endswith(".html") and VER.sub("", x.decode("utf-8", "replace")) == VER.sub("", y.decode("utf-8", "replace")): continue
        out.append(f"site/{rel}")
    return out


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv[:1] == ["--changed"]:                      # --changed <base site dir> <head site dir>: the pages the two renders differ in
        add, gone, changed = changed_pages(argv[1], argv[2])
        print(f"added {len(add)}, removed {len(gone)}, changed {len(changed)} pages")
        for label, ps in (("added", add), ("removed", gone), ("changed", changed)):
            for p in ps: print(f"  {label}: {p}")
        sys.exit(0)
    if "--built" not in argv or len(argv) < 4:
        sys.exit("usage: ci_scope.py <base-ref> --built <base site dir> <head site dir>")   # the plan job falls back to a full run
    i = argv.index("--built"); built = (argv[i + 1], argv[i + 2]); del argv[i:i + 3]
    kind, what = scope(argv[0] if argv else "origin/main", built)
    if kind == "full":
        print("full"); print(f"full run: {what}", file=sys.stderr)
    else:
        print(" ".join(sorted(what)))
        for p, why in sorted(what.items()): print(f"{p}: {', '.join(why[:3])}{' …' if len(why) > 3 else ''}", file=sys.stderr)
        if not what: print("no page changed: the browser steps have nothing to test", file=sys.stderr)
