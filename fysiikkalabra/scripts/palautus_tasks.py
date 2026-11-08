"""Task statements for the teacher's grading view (submission trial, teacher 2026-11-05; palautus/README.md).

Usage: python scripts/palautus_tasks.py [site] [--check]

Reads the built Finnish chapter pages that carry the button (build.py SUBMISSION_CHAPTER: every FY1-FY8 chapter) in a
browser, course by course, after their own KaTeX has run, and writes palautus/apps-script/Tehtavat.gs: the course's chapters in the
teaching order ("FY3 · Luku 4" on the page), each with its exercises in page order with their
running number ("1-4"), level, statement (text, data table and choices, formulas as MathML, figures as PNG pictures
so the Apps Script view needs no fonts, styles or scripts from outside) and the short model answer. The answer
checks, hints, solutions, feedback and which choice is correct are left out. Since file version 3 (teacher 2026-11-06
evening) the lesson's own tasks with an answer follow too (lesson: true, named "Itsearvio: 4. Laskutehtävä"): the grading
page shows their answers but gives them no points. --check fails when the file is not
up to date (the build changed an exercise and the generator was not run).
One local grading page for the running period, palautus/arviointi-<year>-p<period>.html, with the courses that
palautukset.json has forms for (teacher 2026-11-06: one file, a new one each period); Tehtavat.gs (the Apps Script
version, blocked in eduespoo) stays FY3."""
import base64, functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch

args = sys.argv[1:]
check = "--check" in args
args = [a for a in args if a != "--check"]
SITE = ROOT / (args[0] if args else "site")
OUT = ROOT / "palautus/apps-script/Tehtavat.gs"
GAS_COURSE = "FY3"   # Tehtavat.gs


# The self-assessment items of a chapter (teacher 2026-11-06): the id, the page's plain label, and for a task what it asks
# (its own title without the number and kind, and the start of the question) so that the fingerprint tells its content.
# Teacher 2026-11-06 evening: the file carries only the goals' summary, so only the goals (tavoite-<n>) are listed.
SELF_ITEMS = r"""(() => [...document.querySelectorAll('fieldset.sa-rate')].filter((f) => /^tavoite-\d+$/.test(f.dataset.sa || '')).map((f) => {
  const out = { id: f.dataset.sa, label: f.dataset.label };
  if (f.closest('details.opt')) out.optional = true;   // a Valinnainen task: not in the summary's average (teacher 2026-11-06)
  const act = f.closest('.activity');
  if (!act || /^tavoite-/.test(out.id)) return out;
  // the question itself: a numeric or explain task's .task, a choice's legend, the reflection's first item (not its answer)
  const src = act.querySelector('.task, fieldset.choice > legend, ol > li') || act;
  const c = src.cloneNode(true);
  const tex = (x) => x.replace(/\\(?:text|mathrm|mathit|mathbf)\{([^{}]*)\}/g, '$1').replace(/\{,\}/g, ',').replace(/\\[,;:!]|~/g, ' ').replace(/\\cdot/g, '·')
         .replace(/\\t?frac\{([^{}]*)\}\{([^{}]*)\}/g, '$1/$2').replace(/\\Delta\s*/g, 'Δ').replace(/\\(?:left|right)/g, '').replace(/\\([a-zA-Z]+)/g, '$1').replace(/[{}]/g, '').replace(/\s+/g, ' ').trim();
  // a formula as short plain text (3,0 cm, F = ma); a closed box is not typeset yet, so its $…$ too
  c.querySelectorAll('.katex').forEach((k) => { const a = k.querySelector('annotation'); k.replaceWith(tex(a ? a.textContent : k.textContent)); });
  c.querySelectorAll('details, .feedback, .choices, button, output, .practice-hint, input, textarea, select, form, .hints, .model, script, style, [hidden]').forEach((e) => e.remove());
  const q = c.textContent.replace(/\$([^$]*)\$/g, (m, x) => tex(x)).replace(/\s+/g, ' ').trim();
  const t = /^\s*\d+\.\s*[^:]+(?::\s*(.+))?$/.exec(out.label || '');
  const own = t && t[1] ? t[1].trim() : '';
  out.full = [own, q].filter(Boolean).join(': ') || out.label;
  out.label = out.full;   // one row each: the page cuts it to the column with … and shows the rest on hover
  out.kind = (f.dataset.label || '').replace(/:.*$/, '');
  return out;
}))()"""

def pages(course):
    """The Finnish pages of the course with the button (build.py submission_script), as chapter ids."""
    out = []
    for f in SITE.glob(f"{course.lower()}-*.html"):
        m = re.search(r'<script src="palautus\.js(?:\?v=\w+)?" data-chapter="([a-z0-9-]+)"', f.read_text())
        if m and m.group(1) == f.stem: out.append(m.group(1))
    return sorted(out, key=lambda c: int(c.split("-")[1]) if c.split("-")[1].isdigit() else 0)   # FY9 units: by "Luku 1.2" below


def courses_with_button():
    found = {re.match(r"(fy\d+)-", f.name).group(1).upper() for f in SITE.glob("fy*-*.html") if re.fullmatch(r"fy\d+-[a-z0-9-]+\.html", f.name)}   # a FY9 review lesson too (fy9-energia)
    return sorted((c for c in found if pages(c)), key=lambda c: int(c[2:]))

EXTRACT = r"""(id) => {
  const page = document;
  const strip = (root) => {
    root.querySelectorAll('.ex-num,.ex-core,.task-skills,.pts,form,details,.pad-open,.pad,.feedback,button,script,style,.ex-head,.zoom-btn,legend').forEach((e) => e.remove());
    root.querySelectorAll('input').forEach((e) => e.remove());
    // lesson.js flFitMath moves the punctuation after a formula wider than the column into the formula (.kx-punct), and
    // which formulas are too wide depends on the machine's fonts: put the mark back after the formula, so the grading
    // view gets the same text everywhere (CI 2026-11-06: fy8-10 lost a comma there on the CI machine only).
    root.querySelectorAll('.katex .kx-punct').forEach((m) => { const k = m.closest('.katex'), h = k.parentNode && k.parentNode.nodeName === 'SPAN' && !k.parentNode.className && k.parentNode.childNodes.length === 1 ? k.parentNode : k, n = h.nextSibling;
      if (n && n.nodeType === 3) n.data = m.dataset.text + n.data; else h.after(m.dataset.text || ''); m.remove(); k.classList.remove('kx-wide'); });
    // KaTeX: keep only its MathML (Chrome draws MathML Core); display formulas as blocks
    root.querySelectorAll('.katex-display').forEach((d) => { const m = d.querySelector('math'); if (m) { m.setAttribute('display', 'block'); d.replaceWith(m); } });
    root.querySelectorAll('.katex').forEach((k) => { const m = k.querySelector('math'); if (m) k.replaceWith(m); });
    root.querySelectorAll('annotation').forEach((a) => a.remove());
    root.querySelectorAll('*').forEach((e) => [...e.attributes].forEach((a) => {
      const keep = ['display', 'mathvariant', 'stretchy', 'fence', 'separator', 'lspace', 'rspace', 'width', 'scope', 'colspan', 'rowspan', 'class', 'src', 'alt'];
      if (!keep.includes(a.name)) e.removeAttribute(a.name);
    }));
  };
  // the tasks templates/palautus.js puts in the file, from the page's own list (window.flSubmissionTasks, version 3):
  // the exercises and FY9 review tasks, and the lesson's own tasks with an answer (teacher 2026-11-06 evening)
  const lis = window.flSubmissionTasks();
  // a review task's short answer: the answer step of each part of its model solution, under the part's heading
  const reviewAnswer = (li) => {
    const steps = [...li.querySelectorAll(':scope > details.reveal .steps')];
    if (!steps.length) return null;
    const box = document.createElement('div');
    steps.forEach((st) => {
      const h = st.previousElementSibling && st.previousElementSibling.matches('h4.sol-part') ? st.previousElementSibling : null;
      const a = st.querySelector('.sol-step[data-step="vastaus"], .sol-step[data-step="mallivastaus"]');
      if (!a) return;
      if (h) { const p = document.createElement('p'); p.innerHTML = '<strong></strong>'; p.firstChild.textContent = h.textContent.trim(); box.append(p); }
      [...a.children].filter((c) => !c.matches('.sol-label')).forEach((c) => box.append(c.cloneNode(true)));
    });
    return box.childNodes.length ? box : null;
  };
  // a lesson task's name in the list: its stage and its own title ("Itsearvio: 4. Laskutehtävä"), the title of the
  // closed box it sits in when it has no heading of its own
  const stageOf = (t) => { const h = t.closest('section.stage') && t.closest('section.stage').querySelector(':scope > h2');
    return h ? [...h.childNodes].filter((n) => !(n.classList && n.classList.contains('stage-no'))).map((n) => n.textContent).join('').trim() : ''; };
  const nameOf = (t) => { const h = t.querySelector(':scope > h3'); if (h) return h.textContent.trim();
    const d = t.parentElement.closest('details.opt'), sum = d && d.querySelector(':scope > summary');
    return sum ? [...sum.childNodes].filter((n) => !(n.classList && n.classList.contains('opt-tag'))).map((n) => n.textContent).join('').trim() : t.id; };
  return lis.map((li) => {
    if (!li.closest('#exercises')) {
      li.querySelectorAll('.fig, figure').forEach((f) => f.removeAttribute('data-rl-fig'));
      [...li.querySelectorAll('.fig, figure')].filter((f) => !f.parentElement.closest('.fig, figure')).forEach((f, i) => f.setAttribute('data-rl-fig', String(i)));
      const c = li.cloneNode(true);
      c.querySelectorAll('[data-rl-fig]').forEach((f) => { const i = f.getAttribute('data-rl-fig'); const img = document.createElement('img'); const lab = f.querySelector('[aria-label]'); img.setAttribute('alt', lab ? lab.getAttribute('aria-label') : ''); img.setAttribute('src', 'FIG:' + i); img.className = 'fig'; f.replaceWith(img); });
      c.querySelectorAll('h3, .sa-rate, .exp-table, .exp-status, .exp-controls, .exp-buttons, .practice-hint, .hints, .model, .crit-result, ul.criteria, .lock-note, .act-core, .pending, .revise, .my-predictions, textarea, select, .tf-opts, .ord-right, .copy-notes, .explain-status, .drew').forEach((e) => e.remove());
      c.querySelectorAll('legend').forEach((l) => { const q = document.createElement('p'); q.innerHTML = l.innerHTML; l.replaceWith(q); });   // a lesson choice's question is its legend
      strip(c);
      return { id: window.flSubmissionTaskId(li), dom: li.id, number: [stageOf(li), nameOf(li)].filter(Boolean).join(': '), level: 0, lesson: true, html: c.innerHTML.replace(/\s+/g, ' ').trim(), answer: '' };
    }
    const answer = li.matches('li') ? li.querySelector(':scope > details.answer > :not(summary)') : null;
    const ans = answer ? answer.cloneNode(true) : (li.matches('li') ? null : reviewAnswer(li));
    // figures become pictures (filled in by the caller from element screenshots)
    // every figure of the task (also inside a choice), outermost only, numbered on the page so the caller shoots the same one
    li.querySelectorAll('.fig, figure').forEach((f) => f.removeAttribute('data-rl-fig'));
    [...li.querySelectorAll('.fig, figure')].filter((f) => !f.parentElement.closest('.fig, figure') && !f.closest('details.reveal')).forEach((f, i) => f.setAttribute('data-rl-fig', String(i)));
    const c = li.cloneNode(true);
    c.querySelectorAll('[data-rl-fig]').forEach((f) => { const i = f.getAttribute('data-rl-fig'); const img = document.createElement('img'); const lab = f.querySelector('[aria-label]'); img.setAttribute('alt', lab ? lab.getAttribute('aria-label') : ''); img.setAttribute('src', 'FIG:' + i); img.className = 'fig'; f.replaceWith(img); });
    strip(c); if (ans) strip(ans);
    return { id: li.id, number: li.dataset.num || '', level: Number((li.closest('details.level') ? [...document.querySelectorAll('#exercises details.level')].indexOf(li.closest('details.level')) : -1) + 1),
             html: c.innerHTML.replace(/\s+/g, ' ').trim(), answer: ans ? ans.innerHTML.replace(/\s+/g, ' ').trim() : '' };
  });
}"""


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


def collect(course):
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    chapters = []
    with sync_playwright() as p:
        b = launch(p)
        pg = b.new_page(viewport={"width": 900, "height": 1000}, device_scale_factor=2)
        for pid in pages(course):
            pg.goto(f"http://127.0.0.1:{srv.server_port}/{pid}.html")
            pg.wait_for_function("typeof window.renderMathInElement === 'function' && typeof window.flMath === 'function'")
            # Every box open and typeset before reading (lesson.html flMath typesets a closed box only on its toggle event,
            # which fires later; on a slow CI machine the old fixed waits read some boxes as raw LaTeX, 2026-11-06).
            pg.evaluate("""() => document.querySelectorAll('#exercises details').forEach((d) => {
              if (d.closest('.level, .answer') || d.matches('.level, .answer') || d.matches('.practice-task > details.reveal')) { d.open = true; if (d.flMathOpen) d.flMathOpen(); } })""")
            # the lesson's own tasks in a closed box (Valinnainen, the Ennusta box): opened and typeset too (version 3)
            pg.evaluate("""() => document.querySelectorAll('details.opt, details.fold').forEach((d) => { if (!d.closest('#exercises')) { d.open = true; if (d.flMathOpen) d.flMathOpen(); } })""")
            pg.wait_for_function("""() => ![...document.querySelectorAll('#exercises details.level, #exercises details.answer, #exercises .practice-task > details.reveal, details.opt, details.fold')].some((d) => !d.open || d.dataset.flMath === 'wait' || d.classList.contains('fl-math-later'))""")
            pg.evaluate("document.fonts ? document.fonts.ready.then(() => true) : true")
            pg.wait_for_timeout(200)
            pg.wait_for_function("typeof window.flSubmissionTasks === 'function'")
            tasks = pg.evaluate(EXTRACT)
            tasks = [t for t in tasks if not t.get("lesson")] + [t for t in tasks if t.get("lesson")]   # the exercises first in the grading list, then the lesson's tasks
            for t in tasks:
                dom = t.pop("dom", t["id"])   # a lesson task's page id (its id in the file has the chapter in front)
                figs = pg.locator(f'[id="{dom}"] [data-rl-fig]')
                for i in range(figs.count()):   # each figure of the task, choices too (before 2026-11-06 only the task's own)
                    png = base64.b64encode(pg.locator(f'[id="{dom}"] [data-rl-fig="{i}"]').screenshot(type="png", animations="disabled")).decode()
                    t["html"] = t["html"].replace(f'src="FIG:{i}"', f'src="data:image/png;base64,{png}"')
                if "FIG:" in t["html"]: sys.exit(f"{pid} {t['id']}: a figure was not drawn for the grading view")
            title = pg.evaluate("(() => { const h = document.querySelector('main h1').cloneNode(true); h.querySelectorAll('.katex').forEach((k) => { const a = k.querySelector('annotation'); k.replaceWith(a ? a.textContent : k.textContent); }); return h.textContent; })()").strip()
            eyebrow = pg.evaluate("(() => { const e = document.querySelector('.ch-no'); return e ? e.textContent : ''; })()")
            m = re.search(r"Luku\s+(\d+(?:\.\d+)?)", eyebrow)   # "Luku 4", a FY9 review lesson "Luku 2.1"
            # guided self-assessment of Tarkista osaamisesi (teacher 2026-11-06): its items in page order, id and plain label
            # teacher 2026-11-06: "Käsitetehtävä 1" tells too little, so a task's item carries its own title and question
            self_items = pg.evaluate(SELF_ITEMS)
            ch = {"id": pid, "number": (int(m.group(1)) if m.group(1).isdigit() else m.group(1)) if m else int(pid.split("-")[1]), "title": re.sub(r"\s+", " ", title).replace("\\Delta ", "Δ").replace("\\Delta", "Δ"), "tasks": tasks}
            if self_items:
                # the goals' English wording from the English page (teacher 2026-11-08: the group's fingerprint in fi and en)
                enp = SITE / "en" / f"{pid}.html"
                if enp.is_file():
                    import html as _h
                    en_lab = {m.group(1): _h.unescape(m.group(2)) for m in re.finditer(r'<fieldset class="sa-rate[^"]*"[^>]*data-sa="(tavoite-\d+)" data-label="([^"]*)"', enp.read_text())}
                    for it in self_items:
                        if it["id"] in en_lab: it["label_en"] = en_lab[it["id"]]
                ch["self"] = self_items
            en = EN_TITLES.get(course, {}).get(pid)   # the chapter's English name for the grading page's EN view (teacher 2026-11-08)
            if en: ch["title_en"] = re.sub(r"\s+", " ", re.sub(r"\$([^$]*)\$", r"\1", en)).replace("\\Delta ", "Δ").replace("\\Delta", "Δ").strip()
            chapters.append(ch)
        b.close()
    srv.shutdown()
    return chapters


def render(code, chapters):
    chapters = sorted(chapters, key=lambda c: tuple(int(x) for x in str(c["number"]).split(".")))
    course = {"id": code, "chapters": chapters, "themes": themes(code)}
    return ("/* GENERATED by scripts/palautus_tasks.py from the built pages; do not edit by hand.\n"
            "   The course's chapters in teaching order, each with its exercises for the grading view: id, running number,\n"
            "   level, statement (MathML, figures as PNG) and the short model answer. Trusted content written by Ruukkilabra,\n"
            "   not by students. */\n"
            "var RL_COURSE = " + json.dumps(course, ensure_ascii=False, indent=1) + ";\n")


FORMS = ROOT / "palautukset.json"
EN_FILE = ROOT / "content/en/courses.json"


def themes(code):
    """The course's themes (curriculum.json "themes": [{title, first}]) with their English names (content/en/courses.json
    "themes", in the same order), for the group's fingerprint on the grading page (teacher 2026-11-08)."""
    cur = json.loads((ROOT / "curriculum.json").read_text()).get(code) or {}
    en = (json.loads(EN_FILE.read_text()).get(code) or {}).get("themes", []) if EN_FILE.is_file() else []
    out = []
    for i, t in enumerate(cur.get("themes") or []):
        th = {"title": t["title"], "first": t["first"]}
        if i < len(en) and isinstance(en[i], str): th["title_en"] = en[i]
        out.append(th)
    return out
EN_TITLES = {c: v.get("lessons", {}) for c, v in json.loads(EN_FILE.read_text()).items() if isinstance(v, dict)} if EN_FILE.is_file() else {}


def period():
    """The period of palautukset.json (teacher 2026-11-06: one grading file for the running period, a new one when the
    next period starts): its courses (from the groups, "FY3.2" -> FY3), its name and the grading page's path."""
    d = json.loads(FORMS.read_text()) if FORMS.is_file() else {}
    codes = sorted({re.match(r"FY\d+", f["group"]).group(0) for f in d.get("forms", []) if re.match(r"FY\d+", f["group"])}, key=lambda c: int(c[2:]))
    if not codes: return None
    return {"courses": codes, "name": f"{d['period']}. periodi · lv {d['year']}",
            "path": ROOT / f"palautus/arviointi-{d['year']}-p{d['period']}.html"}


CSP = ("<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'; img-src data: blob:; "
       "style-src 'unsafe-inline'; script-src 'unsafe-inline'\">")


def local_page(courses, name):
    """The local grading page (teacher 2026-11-05: Apps Script is blocked in eduespoo): Review.html with the services
    of palautus/paikallinen/local-backend.js, Tehtavat.gs and Code.gs inlined, opened from the teacher's own computer.
    Nothing is loaded from the network (CSP)."""
    gas = ROOT / "palautus"
    js = lambda t: "<script>" + t.replace("</script", "<\\/script") + "</script>"
    tasks = ("/* GENERATED by scripts/palautus_tasks.py: the period's courses, each with its chapters and exercises. */\n"
             "var RL_COURSES = " + json.dumps(courses, ensure_ascii=False, indent=1) + ";\n"
             "var RL_COURSE = RL_COURSES[" + json.dumps(next(iter(courses))) + "];\n")
    head = (CSP + f"<title>RuukkiLabra · arviointi · {name}</title><script>window.RL_LOCAL = true;</script>"
            + js(tasks) + js((gas / "apps-script/Code.gs").read_text()) + js((gas / "paikallinen/local-backend.js").read_text())
            + js((gas / "paikallinen/kieli-en.js").read_text()))   # EN button: the page in English (teacher 2026-11-08)
    page = (gas / "apps-script/Review.html").read_text().replace('<base target="_top">\n', "")
    return ("<!-- GENERATED by scripts/palautus_tasks.py from palautus/apps-script and palautus/paikallinen; do not edit by hand. -->\n"
            + page.replace("<head>", "<head>" + head, 1))


def explain(old, new, path):
    """Where a stale file differs (CI shows it in the log, so a difference is never a guess)."""
    i = next((k for k, (x, y) in enumerate(zip(old, new)) if x != y), min(len(old), len(new)))
    print(f"DIFF {path.relative_to(ROOT)} at character {i} (lengths {len(old)}, {len(new)}):\n  committed: {old[max(0, i - 200):i + 200]!r}\n  built:     {new[max(0, i - 200):i + 200]!r}")


if __name__ == "__main__":
    strip = lambda s: re.sub(r"data:image/png;base64,[A-Za-z0-9+/=]+", "PNG", s)   # screenshots differ by a pixel between machines
    bad = []
    per = period()
    have = courses_with_button()
    wanted = [c for c in have if c == GAS_COURSE or (per and c in per["courses"])]
    courses = {}
    for code in wanted:
        chapters = collect(code)
        text = render(code, chapters)
        if per and code in per["courses"]: courses[code] = {"id": code, "chapters": sorted(chapters, key=lambda c: tuple(int(x) for x in str(c["number"]).split("."))), "themes": themes(code)}
        if code == GAS_COURSE:
            if check:
                if strip(OUT.read_text() if OUT.is_file() else "") != strip(text):
                    bad.append(OUT); explain(strip(OUT.read_text() if OUT.is_file() else ""), strip(text), OUT)
                else: print(f"ok   {OUT.relative_to(ROOT)} is up to date")
            else:
                OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(text)
                print("wrote", OUT.relative_to(ROOT), f"({len(text) // 1024} kB)")
    if per:
        missing = [c for c in per["courses"] if c not in courses]
        if missing: sys.exit(f"palautukset.json names {', '.join(missing)}, which has no chapter with the button")
        local, page = per["path"], local_page(courses, per["name"])
        if check:
            if not local.is_file() or strip(local.read_text()) != strip(page):
                bad.append(local); explain(strip(local.read_text()) if local.is_file() else "", strip(page), local)
            else: print(f"ok   {local.relative_to(ROOT)} is up to date")
        else:
            local.write_text(page)
            print("wrote", local.relative_to(ROOT), f"({len(page) // 1024} kB)")
    # one grading file at a time: the running period's (teacher 2026-11-06)
    stale = [f for f in (ROOT / "palautus").glob("arviointi-*.html") if not per or f != per["path"]]
    if stale:
        if check: bad += stale; print("stale grading pages (run python scripts/palautus_tasks.py):", ", ".join(f.name for f in stale))
        else:
            for f in stale: f.unlink(); print("removed", f.relative_to(ROOT))
    if bad: sys.exit("out of date (run python scripts/palautus_tasks.py): " + ", ".join(str(p.relative_to(ROOT)) for p in bad))
