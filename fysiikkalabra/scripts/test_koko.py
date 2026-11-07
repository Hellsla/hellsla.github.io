"""The size of the module's work file (teacher 2026-11-07, "palautustiedostojen koon optimointi"): realistic FY3 work
on the built site, before and after the pasted pictures are optimised (templates/lesson.js pasteImage), saved, opened
again in another browser and read by the offline grading page (palautus/arviointi-*.html).

  python scripts/test_koko.py           the cases, a size table, and the checks (exit 1 on a failure)

Cases: 75 text solutions; 75 with text and formulas; and those with 10 and 30 pictures (photographed handwritten
solutions, large screenshots and graphs). The pictures are drawn in the browser (canvas): a phone photo 4032x3024 JPEG,
a screenshot 2560x1440 PNG, a graph 1800x1200 PNG, a small screenshot 600x400 PNG."""
import functools, http.server, json, pathlib, sys, threading, time, zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _browser import launch   # noqa: E402
from playwright.sync_api import sync_playwright   # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
TMP = ROOT / "preview" / "koko-test"; TMP.mkdir(parents=True, exist_ok=True)
fails = []


def expect(what, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + what + ("" if ok else f"  -> {str(detail)[:400]}"))
    if not ok: fails.append(what)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
_a = json.loads((ROOT / "annetut.json").read_text()); assigned = _a.get("FY3") or _a["_FY3"]   # FY3 list kept (off since 2026-11-07) as a realistic set of 72 tasks
IDS = [(lid, i) for lid, ids in assigned.items() for i in ids][:75]
while len(IDS) < 75: IDS.append(IDS[len(IDS) % 72])

# In the page: pictures as files (as the clipboard gives them), formulas as the editor stores them (MathJax SVG + LaTeX)
JS_MAKE = r"""async ([kind]) => {
  const W = { photo: [4032, 3024], shot: [2560, 1440], graph: [1800, 1200], small: [600, 400] }[kind];
  const c = document.createElement('canvas'); c.width = W[0]; c.height = W[1]; const g = c.getContext('2d');
  let seed = 7; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
  if (kind === 'photo') {   // paper under a lamp: a gradient, grain, slightly tilted handwriting in blue ink
    const gr = g.createLinearGradient(0, 0, W[0], W[1]); gr.addColorStop(0, '#d9d4c7'); gr.addColorStop(1, '#a8a294'); g.fillStyle = gr; g.fillRect(0, 0, W[0], W[1]);
    const im = g.getImageData(0, 0, W[0], W[1]), d = im.data; for (let i = 0; i < d.length; i += 4) { const n = (rnd() - 0.5) * 28; d[i] += n; d[i + 1] += n; d[i + 2] += n; } g.putImageData(im, 0, 0);
    g.strokeStyle = 'rgba(80,110,160,.35)'; g.lineWidth = 3; for (let y = 300; y < W[1]; y += 110) { g.beginPath(); g.moveTo(0, y); g.lineTo(W[0], y + 20); g.stroke(); }
    g.save(); g.translate(400, 380); g.rotate(0.015); g.fillStyle = '#1d2f6b'; g.font = 'italic 78px serif';
    const L = ['v = s / t = 120 m / 9,6 s', 'v ≈ 12,5 m/s', 'a = Δv / Δt = (12,5 m/s − 0) / 4,0 s', 'a ≈ 3,1 m/s²', 'F = ma = 72 kg · 3,1 m/s² ≈ 220 N', 'E_k = ½mv² = ½ · 72 kg · (12,5 m/s)²', 'E_k ≈ 5,6 kJ', 'Vastaus: noin 220 N'];
    L.forEach((t, k) => g.fillText(t, (rnd() - 0.5) * 30, k * 220)); g.restore();
  } else {   // a screen: white, interface bars, text lines and a graph with axes, ticks and subscripts
    g.fillStyle = '#fff'; g.fillRect(0, 0, W[0], W[1]); g.fillStyle = '#e8ecf2'; g.fillRect(0, 0, W[0], W[1] * 0.06);
    const s = W[0] / 2560; g.fillStyle = '#222'; g.font = `${Math.round(28 * s)}px sans-serif`;
    for (let k = 0; k < 14; k++) g.fillText(`Mittaus ${k + 1}: t = ${(k * 0.4).toFixed(1).replace('.', ',')} s, x₁ = ${(k * k * 0.12).toFixed(2).replace('.', ',')} m, v_x = ${(k * 0.24).toFixed(2).replace('.', ',')} m/s`, 60 * s, (140 + k * 46) * s);
    const x0 = W[0] * 0.5, y0 = W[1] * 0.9, w = W[0] * 0.45, h = W[1] * 0.75;
    g.strokeStyle = '#000'; g.lineWidth = 2 * s; g.beginPath(); g.moveTo(x0, y0 - h); g.lineTo(x0, y0); g.lineTo(x0 + w, y0); g.stroke();
    g.strokeStyle = '#d0d4da'; g.lineWidth = 1; for (let k = 1; k <= 10; k++) { g.beginPath(); g.moveTo(x0 + k * w / 10, y0); g.lineTo(x0 + k * w / 10, y0 - h); g.stroke(); g.beginPath(); g.moveTo(x0, y0 - k * h / 10); g.lineTo(x0 + w, y0 - k * h / 10); g.stroke(); }
    g.strokeStyle = '#1f6feb'; g.lineWidth = 3 * s; g.beginPath(); for (let k = 0; k <= 200; k++) { const u = k / 200; g.lineTo(x0 + u * w, y0 - u * u * h); } g.stroke();
    g.fillStyle = '#c0392b'; for (let k = 0; k <= 10; k++) { const u = k / 10; g.beginPath(); g.arc(x0 + u * w, y0 - u * u * h + (rnd() - 0.5) * 8 * s, 5 * s, 0, 7); g.fill(); }
    g.fillStyle = '#000'; g.font = `${Math.round(24 * s)}px sans-serif`; for (let k = 0; k <= 10; k += 2) g.fillText(String(k / 2).replace('.', ','), x0 + k * w / 10 - 6 * s, y0 + 30 * s);
    g.fillText('t (s)', x0 + w - 40 * s, y0 + 60 * s); g.fillText('x (m)', x0 - 80 * s, y0 - h - 10 * s);
  }
  const type = kind === 'photo' ? 'image/jpeg' : 'image/png';
  const blob = await new Promise((ok) => c.toBlob(ok, type, 0.92));
  const raw = await new Promise((ok) => { const r = new FileReader(); r.onload = () => ok(r.result); r.readAsDataURL(blob); });
  const opt = await window.flPads.image(new File([blob], 'kuva', { type }));
  const size = (u) => new Promise((ok) => { const i = new Image(); i.onload = () => ok([i.naturalWidth, i.naturalHeight]); i.src = u; });
  return { raw, opt, rawSize: await size(raw), optSize: await size(opt) };
}"""
JS_FORMULA = r"""(latex) => { const svg = window.MathJax.tex2svg(latex, { display: false }).querySelector('svg'); svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
  return `<img src="data:image/svg+xml;base64,${btoa(unescape(encodeURIComponent(svg.outerHTML)))}" alt="${latex.replace(/"/g, '&quot;')}">`; }"""
TEXT = ("Lähtötiedot: massa on 72 kg ja nopeus muuttuu tasaisesti. Valitaan positiivinen suunta liikkeen suuntaan. "
        "Kappaleeseen vaikuttavat paino ja tukivoima, jotka kumoavat toisensa, sekä vetävä voima. "
        "Newtonin II lain mukaan kokonaisvoima on massan ja kiihtyvyyden tulo. Sijoitetaan arvot ja lasketaan. "
        "Tulos on järkevän suuruinen, koska ihmisen kiihtyvyys juoksun alussa on muutamia metrejä sekunnin neliössä. ")
FORMULAS = [r"a=\frac{\Delta v}{\Delta t}", r"a=\frac{12{,}5\,\mathrm{\frac{m}{s}}-0}{4{,}0\,\mathrm{s}}\approx 3{,}1\,\mathrm{\frac{m}{s^2}}",
            r"F_\mathrm{kok}=ma", r"F_\mathrm{kok}=72\,\mathrm{kg}\cdot 3{,}1\,\mathrm{\frac{m}{s^2}}\approx 220\,\mathrm{N}", r"E_\mathrm{k}=\tfrac12 mv^2"]
MIX30 = ["photo"] * 12 + ["shot"] * 8 + ["graph"] * 6 + ["small"] * 4
MIX10 = ["photo"] * 4 + ["shot"] * 3 + ["graph"] * 2 + ["small"]

PW = sync_playwright().start()
b = launch(PW)
ctx = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
pg = ctx.new_page(); errs = []
pg.on("pageerror", lambda e: errs.append(str(e)))
pg.goto(BASE + "fy3-1.html")
pg.evaluate("document.querySelectorAll('#exercises details.level').forEach((d) => { d.open = true; })")
first = pg.evaluate("document.querySelector('#exercises li[id] .pad-open').closest('li').id")
pg.click(f'[id="{first}"] .pad-open'); pg.wait_for_selector(f'[id="{first}"] .rich-text-editor')   # loads the editor and MathJax
pics = {k: pg.evaluate(JS_MAKE, [k]) for k in ("photo", "shot", "graph", "small")}
f_html = [pg.evaluate(JS_FORMULA, f) for f in FORMULAS]

print("\nKuvat (yksi kustakin): alkuperäinen -> tallennettu")
for k, p in pics.items():
    print(f"  {k:6} {p['rawSize'][0]}x{p['rawSize'][1]} {len(p['raw']) * 3 // 4 / 1e3:8.0f} kt  ->  {p['optSize'][0]}x{p['optSize'][1]} {len(p['opt']) * 3 // 4 / 1e3:6.0f} kt  {p['opt'][5:15]}")
ar = lambda s: s[0] / s[1]
expect("pictures keep their aspect ratio", all(abs(ar(p["rawSize"]) - ar(p["optSize"])) < 0.01 for p in pics.values()), {k: (p["rawSize"], p["optSize"]) for k, p in pics.items()})
expect("a small picture is kept exactly as pasted (not blurred, not compressed again)", pics["small"]["opt"] == pics["small"]["raw"])
expect("a screenshot and a graph stay PNG (sharp text), at most 2000 px", all(pics[k]["opt"].startswith("data:image/png") and max(pics[k]["optSize"]) <= 2000 for k in ("shot", "graph")), {k: pics[k]["opt"][:22] for k in ("shot", "graph")})
expect("a phone photo becomes JPEG of at most 1600 px", pics["photo"]["opt"].startswith("data:image/jpeg") and max(pics["photo"]["optSize"]) == 1600, pics["photo"]["optSize"])
again = pg.evaluate("async (u) => { const b = await (await fetch(u)).blob(); return window.flPads.image(new File([b], 'k', { type: b.type })); }", pics["photo"]["opt"])
expect("an optimised picture pasted again is not compressed again", again == pics["photo"]["opt"])
for k in ("photo", "shot"):   # for looking at by eye: a 100 % crop of the stored picture
    pg.set_content(f'<body style="margin:0"><img src="{pics[k]["opt"]}" style="display:block"></body>')
    pg.screenshot(path=str(TMP / f"{k}-tallennettu.png"), clip={"x": 0, "y": 0, "width": 1200, "height": 700})
pg.goto(BASE + "fy3-1.html"); pg.wait_for_timeout(300)


def solutions(case, which):
    pick = {"teksti": [], "kaavat": [], "kaavat+10kuvaa": MIX10, "teksti+30kuvaa": MIX30, "kaavat+30kuvaa": MIX30}[case]
    out = []
    for n, (lid, tid) in enumerate(IDS):
        html = f"<div>Ratkaisu {n + 1}. {TEXT}</div><div>{TEXT}</div>"
        if case.startswith("kaavat"): html += "".join(f"<div>{f} </div>" for f in f_html) + f"<div>{TEXT[:200]}</div>"
        if n < len(pick): html += f'<div><img src="{pics[pick[n]][which]}"></div>'
        out.append((tid, html, lid + ".html"))
    return out


PUT = """async (rs) => { await window.flPadStore.clear(); for (const [id, html, page] of rs) await window.flPadStore.put(id, html, page); }"""
pg.evaluate("() => new Promise((ok) => { if (window.flPadStore) return ok(); const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); })")
rows, files = [], {}
for case in ("teksti", "kaavat", "kaavat+10kuvaa", "teksti+30kuvaa", "kaavat+30kuvaa"):
    sizes = {}
    for which in ("raw", "opt"):
        if which == "raw" and case in ("teksti", "kaavat"): continue
        pg.evaluate(PUT, solutions(case, which))
        t0 = time.time()
        r = pg.evaluate("window.flWork.make().then((r) => ({ ok: true, n: new TextEncoder().encode(r.text).length, text: r.text }), (e) => ({ ok: false, m: e.message }))")
        if r["ok"]:
            sizes[which] = (r["n"], time.time() - t0)
            if which == "opt": files[case] = r["text"]; (TMP / f"{case}.json").write_text(r["text"])
        else:   # too large or a picture over its limit: the size it would have had
            est = pg.evaluate("async () => { const a = await window.flPadStore.all(); return new TextEncoder().encode(JSON.stringify(a.solutions)).length; }")
            sizes[which] = (None, r["m"], est)
    rows.append((case, sizes))

print("\nTyötiedosto (FY3, 75 ratkaisua):")
for case, s in rows:
    before = s.get("raw"); after = s["opt"]
    bt = "-" if not before else (f"{before[0] / 1e6:.2f} Mt" if before[0] else f"ei tallennu (~{before[2] / 1e6:.1f} Mt): {before[1][:70]}")
    at = f"{after[0] / 1e6:.2f} Mt ({after[1]:.1f} s)" if after[0] else f"ei tallennu (~{after[2] / 1e6:.1f} Mt): {after[1][:70]}"
    print(f"  {case:15} ennen: {bt:40}  jälkeen: {at}")
limit = 9_000_000
R = dict(rows)
expect("after optimisation every case but the heaviest saves under the 9 MB limit", all(R[c]["opt"][0] and R[c]["opt"][0] <= limit for c in R if c != "kaavat+30kuvaa"), [(c, s["opt"][0]) for c, s in rows])
expect("over the limit: a clear message with the size, nothing left out silently", R["kaavat+30kuvaa"]["opt"][0] or "Tiedostosta tulisi liian suuri" in R["kaavat+30kuvaa"]["opt"][1], R["kaavat+30kuvaa"]["opt"])
expect("before optimisation a phone photo is refused (over 2 MB)", all(not R[c]["raw"][0] and "liian suuri" in R[c]["raw"][1] for c in R if "kuvaa" in c))

# the largest file: opened again in another browser (all solutions and pictures back) and read by the offline grading page
big = files["teksti+30kuvaa"]; (TMP / "kuvat30.json").write_text(big)
ctx2 = b.new_context(accept_downloads=True); p2 = ctx2.new_page(); p2.on("pageerror", lambda e: errs.append(str(e)))
p2.goto(BASE + "FY3.html"); p2.wait_for_selector("#oma-tyo:not([hidden])")
p2.on("dialog", lambda d: d.accept())
t0 = time.time()
with p2.expect_navigation(): p2.set_input_files('#oma-tyo input[type="file"]', str(TMP / "kuvat30.json"))
p2.wait_for_timeout(500)
back = p2.evaluate("() => new Promise((ok) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = () => window.flPadStore.all().then((a) => ok([a.solutions.length, a.solutions.reduce((n, r) => n + (r.html.match(/<img src=\"data:image\\/(png|jpeg)/g) || []).length, 0)])); document.head.append(s); })")
expect(f"the 30-picture file opens in another browser ({time.time() - t0:.1f} s): every solution and picture back", back == [len({t for _, t in IDS}), 30], back)

page = sorted((ROOT / "palautus").glob("arviointi-*.html"))[0]
zp = TMP / "ryhma.zip"
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for k, (case, text) in enumerate(files.items()):
        zi = zipfile.ZipInfo(f"FY3.1 lv 2026-27 Palauta ratkaisut (File responses)/Palauta vastaukset (File responses)/{json.loads(text)['course']}_{case} - Opiskelija {k + 1}.json", date_time=(2026, 11, 7, 10, k, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED; z.writestr(zi, text)
lctx = b.new_context(viewport={"width": 1400, "height": 900}, bypass_csp=True)
lp = lctx.new_page(); lp.on("pageerror", lambda e: errs.append(str(e))); lp.on("dialog", lambda d: d.accept())
lp.goto(page.as_uri()); lp.wait_for_selector("#import")
t0 = time.time()
lp.set_input_files("#pick", str(zp))
lp.wait_for_function("document.getElementById('localMsg').textContent.indexOf('luettu') >= 0", timeout=120000)
lp.wait_for_function("document.getElementById('homeState').textContent !== 'Ladataan…'")
t_import = time.time() - t0
msg = lp.inner_text("#localMsg")
expect(f"offline grading page: the four work files are read ({t_import:.1f} s, {zp.stat().st_size / 1e6:.1f} MB zip)", "luettu 4 tiedostoa" in msg and "hyväksyttyjä" in msg and "virheellisiä 0" in msg, msg)
tid = IDS[0][1]
lp.locator(f'tr.task-row[data-task="{tid}"]').first.click(); lp.wait_for_function("document.querySelector('#gAnswer .t')")
shots = []
for k in range(4):
    lp.wait_for_function("!document.getElementById('gAnswer').textContent.includes('Ladataan')")
    shots.append((lp.locator("#gAnswer img.shot").count(), lp.locator("#gAnswer img.math").count()))
    if k < 3: lp.evaluate("document.activeElement.blur()"); lp.keyboard.press("ArrowDown"); lp.wait_for_timeout(300)
expect("offline grading page: the task's solution with its picture and formulas for each student", sorted(shots) == sorted([(0, 0), (0, 5), (1, 5), (1, 0)]), shots)
expect("offline grading page: no completion times or progress graph", "2026-11" not in lp.inner_text("body").replace("2026-11-07", "") and lp.locator("svg.pm-chart, .my-progress").count() == 0)
expect("no script errors", not errs, errs[:3])
b.close(); PW.stop(); srv.shutdown()
print(f"\n{len(fails)} failure(s)" if fails else "\nall ok")
sys.exit(1 if fails else 0)
