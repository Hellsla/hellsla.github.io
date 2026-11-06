"""Task statements for the teacher's grading view (submission trial, teacher 2026-11-05; palautus/README.md).

Usage: python scripts/palautus_tasks.py [site] [--check]

Reads the built Finnish chapter pages that carry the button (build.py SUBMISSION_CHAPTER: every FY1-FY8 chapter) in a
browser, course by course, after their own KaTeX has run, and writes palautus/apps-script/Tehtavat.gs: the course's chapters in the
teaching order ("FY3 · Luku 4" on the page), each with its exercises in page order with their
running number ("1-4"), level, statement (text, data table and choices, formulas as MathML, figures as PNG pictures
so the Apps Script view needs no fonts, styles or scripts from outside) and the short model answer. The answer
checks, hints, solutions, feedback and which choice is correct are left out. --check fails when the file is not
up to date (the build changed an exercise and the generator was not run).
One local grading page per course, palautus/arviointi-<course>.html (teacher 2026-11-06: every course); Tehtavat.gs
(the Apps Script version, blocked in eduespoo) stays FY3."""
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


def pages(course):
    """The Finnish pages of the course with the button (build.py submission_script), as chapter ids."""
    out = []
    for f in SITE.glob(f"{course.lower()}-*.html"):
        m = re.search(r'<script src="palautus\.js(?:\?v=\w+)?" data-chapter="([a-z0-9-]+)"', f.read_text())
        if m and m.group(1) == f.stem: out.append(m.group(1))
    return sorted(out, key=lambda c: int(c.split("-")[1]))


def courses_with_button():
    found = {re.match(r"(fy\d+)-", f.name).group(1).upper() for f in SITE.glob("fy*-*.html") if re.fullmatch(r"fy\d+-\d+\.html", f.name)}
    return sorted((c for c in found if pages(c)), key=lambda c: int(c[2:]))

EXTRACT = r"""(id) => {
  const page = document;
  const strip = (root) => {
    root.querySelectorAll('.ex-num,.ex-core,form,details,label.solved,.pad-open,.pad,.feedback,button,script,style,.ex-head,.zoom-btn,legend').forEach((e) => e.remove());
    root.querySelectorAll('input').forEach((e) => e.remove());
    // KaTeX: keep only its MathML (Chrome draws MathML Core); display formulas as blocks
    root.querySelectorAll('.katex-display').forEach((d) => { const m = d.querySelector('math'); if (m) { m.setAttribute('display', 'block'); d.replaceWith(m); } });
    root.querySelectorAll('.katex').forEach((k) => { const m = k.querySelector('math'); if (m) k.replaceWith(m); });
    root.querySelectorAll('annotation').forEach((a) => a.remove());
    root.querySelectorAll('*').forEach((e) => [...e.attributes].forEach((a) => {
      const keep = ['display', 'mathvariant', 'stretchy', 'fence', 'separator', 'lspace', 'rspace', 'width', 'scope', 'colspan', 'rowspan', 'class', 'src', 'alt'];
      if (!keep.includes(a.name)) e.removeAttribute(a.name);
    }));
  };
  const lis = [...page.querySelectorAll('#exercises li[id]')].filter((li) => li.querySelector(':scope > .task'));
  return lis.map((li) => {
    const c = li.cloneNode(true);
    const answer = li.querySelector(':scope > details.answer > :not(summary)');
    const ans = answer ? answer.cloneNode(true) : null;
    // figures become pictures (filled in by the caller from element screenshots)
    c.querySelectorAll('.fig, figure').forEach((f, i) => { const img = document.createElement('img'); const lab = f.querySelector('[aria-label]'); img.setAttribute('alt', lab ? lab.getAttribute('aria-label') : ''); img.setAttribute('src', 'FIG:' + i); img.className = 'fig'; f.replaceWith(img); });
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
            pg.evaluate("document.querySelectorAll('#exercises details.level, #exercises details.answer').forEach((d) => { d.open = true; })")
            pg.wait_for_function("document.querySelectorAll('#exercises .katex').length > 0")
            pg.wait_for_timeout(400)
            pg.evaluate("window.flMath && window.flMath(document.getElementById('exercises'))")
            pg.wait_for_timeout(300)
            tasks = pg.evaluate(EXTRACT)
            for t in tasks:
                figs = pg.locator(f'[id="{t["id"]}"] > .fig, [id="{t["id"]}"] > figure')
                for i in range(figs.count()):
                    png = base64.b64encode(figs.nth(i).screenshot(type="png")).decode()
                    t["html"] = t["html"].replace(f'src="FIG:{i}"', f'src="data:image/png;base64,{png}"')
            title = pg.evaluate("(() => { const h = document.querySelector('main h1').cloneNode(true); h.querySelectorAll('.katex').forEach((k) => { const a = k.querySelector('annotation'); k.replaceWith(a ? a.textContent : k.textContent); }); return h.textContent; })()").strip()
            eyebrow = pg.evaluate("(() => { const e = document.querySelector('.ch-no'); return e ? e.textContent : ''; })()")
            m = re.search(r"Luku\s+(\d+)", eyebrow)
            chapters.append({"id": pid, "number": int(m.group(1)) if m else int(pid.split("-")[1]), "title": re.sub(r"\s+", " ", title).replace("\\Delta ", "Δ").replace("\\Delta", "Δ"), "tasks": tasks})
        b.close()
    srv.shutdown()
    return chapters


def render(code, chapters):
    chapters = sorted(chapters, key=lambda c: c["number"])
    course = {"id": code, "chapters": chapters}
    return ("/* GENERATED by scripts/palautus_tasks.py from the built pages; do not edit by hand.\n"
            "   The course's chapters in teaching order, each with its exercises for the grading view: id, running number,\n"
            "   level, statement (MathML, figures as PNG) and the short model answer. Trusted content written by Ruukkilabra,\n"
            "   not by students. */\n"
            "var RL_COURSE = " + json.dumps(course, ensure_ascii=False, indent=1) + ";\n")


LOCAL = lambda code: ROOT / f"palautus/arviointi-{code.lower()}.html"
CSP = ("<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'; img-src data: blob:; "
       "style-src 'unsafe-inline'; script-src 'unsafe-inline'\">")


def local_page(tasks_gs, course):
    """The local grading page (teacher 2026-11-05: Apps Script is blocked in eduespoo): Review.html with the services
    of palautus/paikallinen/local-backend.js, Tehtavat.gs and Code.gs inlined, opened from the teacher's own computer.
    Nothing is loaded from the network (CSP)."""
    gas = ROOT / "palautus"
    js = lambda t: "<script>" + t.replace("</script", "<\\/script") + "</script>"
    head = (CSP + f"<title>RuukkiLabra · arviointi {course} (paikallinen)</title><script>window.RL_LOCAL = true;</script>"
            + js(tasks_gs) + js((gas / "apps-script/Code.gs").read_text()) + js((gas / "paikallinen/local-backend.js").read_text()))
    page = (gas / "apps-script/Review.html").read_text().replace('<base target="_top">\n', "")
    return ("<!-- GENERATED by scripts/palautus_tasks.py from palautus/apps-script and palautus/paikallinen; do not edit by hand. -->\n"
            + page.replace("<head>", "<head>" + head, 1))


if __name__ == "__main__":
    strip = lambda s: re.sub(r"data:image/png;base64,[A-Za-z0-9+/=]+", "PNG", s)   # screenshots differ by a pixel between machines
    bad = []
    for code in courses_with_button():
        text = render(code, collect(code))
        local = LOCAL(code)
        if code == GAS_COURSE:
            if check:
                if strip(OUT.read_text() if OUT.is_file() else "") != strip(text): bad.append(OUT)
                else: print(f"ok   {OUT.relative_to(ROOT)} is up to date")
            else:
                OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(text)
                print("wrote", OUT.relative_to(ROOT), f"({len(text) // 1024} kB)")
        if check:
            if not local.is_file() or strip(local.read_text()) != strip(local_page(text, code)): bad.append(local)
            else: print(f"ok   {local.relative_to(ROOT)} is up to date")
        else:
            local.write_text(local_page(text, code))
            print("wrote", local.relative_to(ROOT), f"({len(local.read_text()) // 1024} kB)")
    if bad: sys.exit("out of date (run python scripts/palautus_tasks.py): " + ", ".join(str(p.relative_to(ROOT)) for p in bad))
