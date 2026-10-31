r"""Layout check of built lesson pages. Usage: python scripts/check_layout.py [lesson-id] [--width 360] [--site]

Opens each page in preview/ (or site/) at a viewport (360 by default; CI runs 360, 390, 768, 1024, 1280, 1440 and
1920, and 640 for a 1280 px window at 200 % zoom) and checks it in three states, because a page that is fine closed
can break when the student opens things (teacher 2026-10-27, "avautuvat kortit"):

  closed   as the page loads
  hints    the first hint and the solution of every task open, the first box of every group open
  open     every <details> open (hints, solutions, optional tasks, Ennusta, exercise levels, exit ticket answers) and
           every hidden feedback, model answer and worked-example stage shown, as after a student has answered all

In each state it reports:
  overflow   a formula KaTeX cannot parse, or an element wider than its box: display formulas (.katex-display), inline formulas that cannot wrap (a
             long \dfrac), inline SVG figures, the page itself (tables scroll by design: a warning only), a calculation row whose left
             side runs into its right side or wraps although the chain has room (2026-10-31)
  svg-text   a figure label that overlaps another label or leaves the figure (NOTES 3)
  column     a column whose content spills into its neighbour
  text       text wider than a reading column (44rem, about 80 characters)
  overlap    two blocks of the same group drawn over each other (task cards, figure units, solution steps, options)
  order      a task card shown above the one before it in the reading order
  gap        a two-column row where one column is far taller than the other, leaving a large empty area beside the
             shorter one (a card that grows beside a short one; a figure beside a much longer text). The simulation
             and the worked example's problem are sticky beside their column and are not counted.
  small      reading text under 17 px (a phone never gets smaller text) or a control under 40 px tall
  heading    a stage heading hidden under the sticky navigation after following its link (closed state only)
Exit status 1 on anything but a wide table."""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
import i18n
args = [a for a in sys.argv[1:] if not a.startswith("--")]
width = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 360
args = [a for a in args if a != str(width)]
only = args[0] if args else None
OUT = ROOT / "site" if "--site" in sys.argv else ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"   # --site: the published pages (CI)

JS = """() => {
  const out = [], V = (e) => e.checkVisibility();
  const el = document.scrollingElement, vw = document.documentElement.clientWidth;
  if (el.scrollWidth > el.clientWidth + 1) out.push({what: 'page', over: el.scrollWidth - el.clientWidth, text: ''});
  for (const d of document.querySelectorAll('.katex-display')) {
    if (!d.checkVisibility()) continue;
    if (d.scrollWidth > d.clientWidth + 3) {   // KaTeX's struts (vlist-t2, margin -2px) may stick out 2 px without anything showing
      const ann = d.querySelector('annotation');
      out.push({what: 'formula', over: d.scrollWidth - d.clientWidth, text: ann ? ann.textContent.slice(0, 90) : ''});
    }
  }
  for (const e of document.querySelectorAll('main .katex-error'))   // a formula KaTeX could not parse (as split into rows, too)
    out.push({what: 'formula', over: 0, text: 'KaTeX error: ' + (e.getAttribute('title') || e.textContent).slice(0, 90)});
  for (const k of document.querySelectorAll('main .katex')) {
    if (!k.checkVisibility() || k.closest('.katex-display, table, svg, #sim-root')) continue;
    const box = k.closest('p, li, .steps, .stage') || k.parentElement;
    const over = Math.round(k.getBoundingClientRect().right - Math.min(box.getBoundingClientRect().right, vw));
    if (over > 1) { const ann = k.querySelector('annotation'); out.push({what: 'formula', over, text: 'inline, cannot wrap: ' + (ann ? ann.textContent.slice(0, 70) : '')}); }
  }
  for (const c of document.querySelectorAll('main .eq-chain')) {   // a calculation set as rows (mathlayout.py): its left side must neither spill into the right one
    if (!V(c)) continue;                                          // nor wrap while the chain has room (teacher 2026-10-31, the visual reviewer's fy1-4 and fy3-7 findings)
    const room = c.parentElement.getBoundingClientRect().width - c.getBoundingClientRect().width;
    for (const l of c.querySelectorAll('.eq-l')) {
      const k = l.querySelector('.katex'); if (!k) continue;
      const ann = k.querySelector('annotation'), txt = ann ? ann.textContent.slice(0, 70) : '';
      const kr = k.getBoundingClientRect(), lr = l.getBoundingClientRect();
      if (kr.right > lr.right + 2) out.push({what: 'formula', over: Math.round(kr.right - lr.right), text: 'calculation row: left side runs into the right side: ' + txt});
      const lines = new Set([...k.querySelectorAll('.base')].map((b) => Math.round(b.getBoundingClientRect().top))).size;
      if (lines > 1 && room > 40) out.push({what: 'formula', over: Math.round(room), text: 'calculation row: left side wraps though the chain has room: ' + txt});
    }
  }
  for (const t of document.querySelectorAll('table')) {
    if (t.closest('#sim-root') || !t.checkVisibility()) continue;
    const box = t.parentElement;
    if (t.scrollWidth > box.clientWidth + 1) out.push({what: 'table', over: t.scrollWidth - box.clientWidth, text: t.innerText.slice(0, 60)});
  }
  for (const s of document.querySelectorAll('main svg')) {
    const r = s.getBoundingClientRect();
    if (!r.width) continue;
    if (r.right > vw + 1) out.push({what: 'svg', over: Math.round(r.right - vw), text: s.getAttribute('aria-label') || ''});
    const T = [...s.querySelectorAll('text'), ...s.querySelectorAll('foreignObject')].map((t) => ({t: t.textContent.trim().slice(0, 40), b: (t.querySelector('.katex, div') || t).getBoundingClientRect()})).filter((x) => x.t);
    for (const x of T) if (x.b.left < r.left - 1 || x.b.right > r.right + 1 || x.b.top < r.top - 1 || x.b.bottom > r.bottom + 1)
      out.push({what: 'svg-text', over: Math.round(Math.max(r.left - x.b.left, x.b.right - r.right, r.top - x.b.top, x.b.bottom - r.bottom)), text: `"${x.t}" leaves the figure`});
    for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = T[i].b, b = T[j].b;
      const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left), oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (ox > 1 && oy > 1) out.push({what: 'svg-text', over: Math.round(Math.min(ox, oy)), text: `"${T[i].t}" overlaps "${T[j].t}"`}); }
  }
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
  for (const c of document.querySelectorAll('.lab > *, .fig-row > *, .intro-row > *, .example > *'))
    if (V(c) && c.scrollWidth > c.clientWidth + 3) out.push({what: 'column', over: c.scrollWidth - c.clientWidth, text: c.className});
  for (const t of document.querySelectorAll('main p, main li')) {
    if (!V(t) || t.closest('#sim-root, .katex-display, table')) continue;
    const w = t.getBoundingClientRect().width;
    if (w > 44 * rem + 1) { out.push({what: 'text', over: Math.round(w - 44 * rem), text: `line length: "${t.textContent.trim().slice(0, 50)}"`}); break; }
  }
  const R = (e) => e.getBoundingClientRect();
  const name = (e) => (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\\s+/).join('.') : e.tagName.toLowerCase());
  // overlap: blocks of the same group (siblings) never drawn over each other
  const groups = ['.activity', 'details.opt', 'details.level', '.fig-row', '.fig-row > *', '.intro-row > *', '.sol-step', 'ul.choices > li', '.stage', '#exit > ol > li', 'details.level > ol > li'];
  const seen = new Set();
  for (const g of groups) for (const a of document.querySelectorAll(g)) {
    if (!V(a) || a.closest('.lab-side, .example-task')) continue;
    for (const b of a.parentElement.children) {
      if (b === a || !b.matches(g) || !V(b) || seen.has(b)) continue;
      const p = R(a), q = R(b), ox = Math.min(p.right, q.right) - Math.max(p.left, q.left), oy = Math.min(p.bottom, q.bottom) - Math.max(p.top, q.top);
      if (ox > 2 && oy > 2) out.push({what: 'overlap', over: Math.round(Math.min(ox, oy)), text: `${name(a)} and ${name(b)}`});
    }
    seen.add(a);
  }
  // order: the task cards read from top to bottom in the order they are written
  const cards = [...document.querySelectorAll('main .activity, main details.opt')].filter((e) => V(e) && !e.closest('.lab-side, details.opt .activity') && !e.parentElement.closest('.activity'));
  for (let i = 1; i < cards.length; i++) if (R(cards[i]).top < R(cards[i - 1]).top - 1)
    out.push({what: 'order', over: Math.round(R(cards[i - 1]).top - R(cards[i]).top), text: `${name(cards[i])} shows above ${name(cards[i - 1])}`});
  // gap: a row of two columns where one is far taller than the other (the empty area beside a grown card)
  for (const g of document.querySelectorAll('main *')) {
    const cs = getComputedStyle(g);
    if (cs.display !== 'grid' || !V(g) || g.matches('.lab, .example, ul.choices, .prior ul')) continue;
    if (cs.gridTemplateColumns.trim().split(/\\s+/).length < 2) continue;
    const rows = {};
    for (const c of g.children) { if (!V(c) || getComputedStyle(c).position === 'sticky') continue; const k = Math.round(R(c).top); (rows[k] = rows[k] || []).push(R(c).height); }
    for (const hs of Object.values(rows)) if (hs.length > 1) {
      const hi = Math.max(...hs), lo = Math.min(...hs);
      if (hi - lo > 240 && lo < 0.55 * hi) out.push({what: 'gap', over: Math.round(hi - lo), text: `${name(g)}: ${Math.round(hi - lo)} px empty beside the shorter column`});
    }
  }
  // small: reading text keeps its size on a phone, and every control is big enough to hit
  for (const t of document.querySelectorAll('.act-theory > p, .act-theory .fig-text > p, .act-theory li, p.task, fieldset.choice legend, ul.choices label, .hook p, .learn li, details.solution .steps p:not(.sol-label)')) {
    if (!V(t) || t.closest('#sim-root')) continue;
    const fs = parseFloat(getComputedStyle(t).fontSize);
    if (fs < 16.5) { out.push({what: 'small', over: Math.round(17 - fs), text: `${fs} px text: "${t.textContent.trim().slice(0, 40)}"`}); break; }
  }
  for (const c of document.querySelectorAll('main button, main summary, ul.choices label, nav.toc a, form.check input')) {
    if (!V(c) || c.closest('#sim-root')) continue;
    if (R(c).height < 39.5) { out.push({what: 'small', over: Math.round(40 - R(c).height), text: `control ${Math.round(R(c).height)} px tall: "${c.textContent.trim().slice(0, 40)}"`}); break; }
  }
  return out;
}"""

OPEN = {
  "closed": "() => true",
  "hints": """() => { for (const g of document.querySelectorAll('.hints, .numeric, .activity, details.level > ol > li')) {
      const h = g.querySelector('details.hint'); if (h) h.open = true; const s = g.querySelector(':scope details.solution, :scope > details.solution'); if (s) s.open = true; }
    document.querySelectorAll('details.fold, details.level').forEach((d) => { d.open = true; }); return true; }""",
  "open": """() => { document.querySelectorAll('details').forEach((d) => { d.open = true; });
    document.querySelectorAll('main [hidden]').forEach((e) => { if (!e.closest('#sim-root')) e.hidden = false; }); return true; }""",
}

# a stage heading after its link is followed: below the sticky navigation and near the top of the window
HEADINGS = """async () => { const V = (e) => e.checkVisibility(), out = [], nav = document.querySelector('nav.toc');
  for (const a of document.querySelectorAll('nav.toc a[href^="#"]')) {
    const t = document.querySelector(a.getAttribute('href')); if (!t || !V(t)) continue;
    t.scrollIntoView(); await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
    const h = (t.matches('h2, h3') ? t : t.querySelector('h2, h3')) || t, r = h.getBoundingClientRect(), n = nav.getBoundingClientRect();
    const covered = getComputedStyle(nav).position === 'sticky' && n.left < r.right && n.right > r.left && n.bottom > r.top + 2 && n.top < r.bottom;
    if (covered || r.top < -1 || r.top > innerHeight / 2) out.push({what: 'heading', over: Math.round(covered ? n.bottom - r.top : r.top), text: `${a.textContent.trim()}: heading ${covered ? 'under the navigation' : 'not brought into view'}`});
  }
  window.scrollTo(0, 0); return out; }"""

bad = 0
with sync_playwright() as pw:
    b = launch(pw)
    for page_file in sorted(OUT.glob("*.html")) + [f for lang in i18n.languages()[1:] for f in sorted((OUT / lang).glob("*.html"))]:   # site/<lang>/ too
        lid = page_file.stem
        if only and lid != only: continue
        if lid == "index" or "-" not in lid: continue
        page = b.new_page(viewport={"width": width, "height": 800})
        page.goto(page_file.as_uri())
        page.evaluate("document.fonts.ready.then(() => true)")   # measure with the page's own fonts, not a fallback
        page.wait_for_timeout(400)
        found = [dict(f, state="closed") for f in page.evaluate(HEADINGS)]
        for state, js in OPEN.items():
            page.evaluate(js); page.wait_for_timeout(150 if state != "closed" else 0)
            if state != "closed": page.evaluate("document.querySelectorAll('.katex-display').length")   # (opened maths is already rendered by auto-render)
            found += [dict(f, state=state) for f in page.evaluate(JS)]
        page.close()
        uniq = []
        for f in found:                               # the same problem in several states is reported once, with its first state
            if not any(u["what"] == f["what"] and u["text"] == f["text"] for u in uniq): uniq.append(f)
        hard = [f for f in uniq if f['what'] != 'table']   # tables scroll sideways by design (NOTES 1)
        tag = f"{OUT.name}/{page_file.relative_to(OUT).with_suffix('').as_posix()} at {width} px"
        if hard:
            bad += 1
            print(f"FAIL {tag}")
            for f in uniq:
                print(f"  {f['what']:8} {f['over']:4} px  [{f['state']}]  {f['text']}" + ("  (warning: scrolls)" if f['what'] == 'table' else ""))
        else:
            print(f"OK   {tag}" + (f"  ({len(uniq)} wide table, scrolls)" if uniq else ""))
    b.close()
sys.exit(1 if bad else 0)
