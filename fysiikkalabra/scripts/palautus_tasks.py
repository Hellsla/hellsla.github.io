"""Task statements for the teacher's grading view (submission trial, teacher 2026-11-05; palautus/README.md).

Usage: python scripts/palautus_tasks.py [site] [--check]

Reads the built Finnish chapter pages named in build.py SUBMISSION_PAGES (site/<id>.html) in a browser, after their
own KaTeX has run, and writes palautus/apps-script/Tehtavat.gs: the chapter's exercises in page order with their
running number ("1-4"), level, statement (text, data table and choices, formulas as MathML, figures as PNG pictures
so the Apps Script view needs no fonts, styles or scripts from outside) and the short model answer. The answer
checks, hints, solutions, feedback and which choice is correct are left out. --check fails when the file is not
up to date (the build changed an exercise and the generator was not run)."""
import base64, functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch

args = sys.argv[1:]
check = "--check" in args
args = [a for a in args if a != "--check"]
SITE = ROOT / (args[0] if args else "site")
OUT = ROOT / "palautus/apps-script/Tehtavat.gs"
PAGES = ["fy3-1"]   # build.py SUBMISSION_PAGES (Finnish)

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


def collect():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    chapters = []
    with sync_playwright() as p:
        b = launch(p)
        pg = b.new_page(viewport={"width": 900, "height": 1000}, device_scale_factor=2)
        for pid in PAGES:
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
            course = pid.split("-")[0].upper()
            chapters.append({"id": pid, "course": course, "title": re.sub(r"\s+", " ", title), "tasks": tasks})
        b.close()
    srv.shutdown()
    return chapters


def render(chapters):
    ch = chapters[0]   # one chapter in this trial
    return ("/* GENERATED by scripts/palautus_tasks.py from the built page; do not edit by hand.\n"
            "   The chapter's exercises for the grading view: id, running number, level, statement (MathML, figures as PNG)\n"
            "   and the short model answer. Trusted content written by Ruukkilabra, not by students. */\n"
            "var RL_CHAPTER = " + json.dumps(ch, ensure_ascii=False, indent=1) + ";\n")


if __name__ == "__main__":
    text = render(collect())
    if check:
        old = OUT.read_text() if OUT.is_file() else ""
        strip = lambda s: re.sub(r"data:image/png;base64,[A-Za-z0-9+/=]+", "PNG", s)   # screenshots differ by a pixel between machines
        if strip(old) != strip(text): sys.exit(f"{OUT.relative_to(ROOT)} is out of date: run python scripts/palautus_tasks.py")
        print("ok   palautus/apps-script/Tehtavat.gs is up to date")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)
        print("wrote", OUT.relative_to(ROOT), f"({len(text) // 1024} kB)")
