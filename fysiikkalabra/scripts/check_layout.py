r"""Layout check of built lesson pages. Usage: python scripts/check_layout.py [page-id ...] [--width 360] [--site] [--dir <folder of built pages>]

Opens each page in preview/ (or site/) at a viewport (360 by default; CI runs 360, 390, 768, 1024, 1280, 1440 and
1920, and 640 for a 1280 px window at 200 % zoom) and checks it in three states, because a page that is fine closed
can break when the student opens things (teacher 2026-10-27, "avautuvat kortit"):

  closed   as the page loads
  hints    the first hint and the solution of every task open, the first box of every group open
  open     every <details> open (hints, solutions, optional tasks, Ennusta, exercise levels, exit ticket answers) and
           every hidden feedback, model answer and worked-example stage shown, as after a student has answered all

In each state it reports:
  overflow   a formula that is clipped: its last glyph beyond the box that shows it (a calculation row or a long inline formula
             that must be scrolled to, "m/s" cut to "m/"; teacher 2026-11-15), in every open state, solutions included;
             a formula KaTeX cannot parse, or an element wider than its box: display formulas (.katex-display), inline formulas that cannot wrap (a
             long \dfrac), inline SVG figures, the page itself, a table wider than its box (no table scrolls sideways, teacher
             2026-11-08: long words break at soft hyphens, scripts/tablefit.py), a calculation row whose left
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
Each finding names where it is (work queue 5, 2026-11-16): the nearest block with an id (the task "#fy8-1-L2-08", the
stage "#teoria"), the open box, the solution step and the element ("at #fy8-1-L2-08 > details.solution > step
"Substitution" > div.eq-chain"); a page wider than the window names the deepest element past its edge. For CI's
verdict run it in CI's browser image: python scripts/ci_env.py run python scripts/check_layout.py <id> --width 360.
Exit status 1 on any finding."""
import os, re, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
import i18n
args = [a for a in sys.argv[1:] if not a.startswith("--")]
width = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 360
args = [a for a in args if a != str(width) and (a != sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else True)]
only = set(args)   # none: every page; CI on a pull request passes the pages scripts/ci_scope.py names
OUT = pathlib.Path(sys.argv[sys.argv.index("--dir") + 1]) if "--dir" in sys.argv else ROOT / "site" if "--site" in sys.argv else ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"   # --site: the published pages (CI)

CLIPPED = "clipped or scrolling, not fully shown: "
# page <TAB> formula: what the pages already had when the check was added (2026-11-15); never added to by hand. One file per
# course, docs/clipped-formulas/<group>.tsv (work queue 5, 2026-11-16: two courses' pull requests never touch the same
# file); CLIPPED_KNOWN names another folder or a single file (a test).
KNOWN = pathlib.Path(os.environ.get("CLIPPED_KNOWN") or ROOT / "docs" / "clipped-formulas")
KNOWN_HEAD = ("# Formulas that were clipped on a phone (360 or 390 px, solutions open) when check_layout.py learned to see them (teacher 2026-11-15, work queue 5b).\n"
              "# page<TAB>formula. A page may keep them until its text changes; any other clipped formula fails the check. Rows are only ever removed\n"
              "# (fix the formula and delete its row; the file with its last row); written by `check_layout.py --write-known`, never by hand.\n")


def group(key):
    """The file a page's rows live in: its course (fy4-3, en/fy4-3, FY4-sovella, FY4-koe -> FY4), else the first part of
    its id (tvt-kulmakerroin -> tvt)."""
    page = key.split("/")[-1]
    m = re.match(r"(?i)fy(\d+)\b", page)
    return f"FY{m.group(1)}" if m else page.split("-")[0]


def read_known(path):
    files = [path] if path.is_file() else sorted(path.glob("*.tsv")) if path.is_dir() else []
    out = set()
    for f in files:
        for l in f.read_text().splitlines():
            if not l or l.startswith("#"): continue
            row = tuple(l.split("\t", 1))
            if path.is_dir() and group(row[0]) != f.stem: sys.exit(f"{f}: the row of {row[0]} belongs in {group(row[0])}.tsv")
            out.add(row)
    return out


known = read_known(KNOWN)
write_known = "--write-known" in sys.argv   # add what this run finds to docs/clipped-formulas/ (once, from a full run at 360 and 390 px)
found_known = set()

JS = """() => {
  if (window.flFitMath) window.flFitMath();   // lesson.js: a too-wide inline formula gets its own scrolling line (kx-wide)
  if (window.flFitTables) window.flFitTables();   // lesson.js: a table still too wide for its box is stacked
  const out = [], V = (e) => e.checkVisibility();
  // where a finding is (work queue 5, QUALITY.md): the nearest block with an id (a task "#fy8-1-L2-08", a stage "#teoria"), the
  // solution step it is in, and the element itself, so a failure names what to fix without a screenshot
  const tag = (e) => e.tagName.toLowerCase() + (e.classList.length ? '.' + [...e.classList].slice(0, 2).join('.') : '');
  const W = (e) => {
    if (!e || !e.closest) return '';
    const parts = [], id = e.parentElement && e.parentElement.closest('[id]:not(main, body, html, #sim-root)');
    if (id) parts.push('#' + id.id);
    const d = e.closest('details'); if (d && d !== id && (!id || id.contains(d))) parts.push(tag(d));
    const st = e.closest('.sol-step'), lab = st && st.querySelector('.sol-label');
    if (lab) parts.push('step "' + lab.textContent.trim().slice(0, 30) + '"');
    const own = e.closest('.eq-chain, .kx-wide, .katex-display, table, svg, figure') || e;
    parts.push(tag(own));
    return parts.join(' > ');
  };
  // the page itself is wider than the window: name the deepest element that reaches past the window's right edge
  const widest = () => {
    let hit = null; const vw0 = document.documentElement.clientWidth;
    for (const e of document.querySelectorAll('body *')) {
      if (!e.checkVisibility() || e.closest('svg') && e.tagName.toLowerCase() !== 'svg') continue;
      const r = e.getBoundingClientRect(); if (r.width && r.right > vw0 + 1) hit = e;   // document order: the last one is the deepest
    }
    return hit ? W(hit) : '';
  };
  const el = document.scrollingElement, vw = document.documentElement.clientWidth;
  // From 1600 px the whole page is drawn larger (site.css, 2026-11-11: the root size grows to 117.65 % at 1920 px, every
  // size of the site is in rem). K is that enlargement, 1 under 1600 px. The limits below that are a length of the
  // drawing itself (a figure label 1 px over the figure's edge or over another label, 240 px empty beside a column) are
  // counted in the page's own scale, so the
  // same layout passes or fails alike at 1280 px and enlarged at 1920 px; every other limit stays in real pixels.
  const K = Math.max(1, parseFloat(getComputedStyle(document.documentElement).fontSize) / 16);
  if (el.scrollWidth > el.clientWidth + 1) out.push({what: 'page', over: el.scrollWidth - el.clientWidth, text: '', at: widest()});
  for (const d of document.querySelectorAll('.katex-display')) {
    if (!d.checkVisibility()) continue;
    if (d.scrollWidth > d.clientWidth + 3) {   // KaTeX's struts (vlist-t2, margin -2px) may stick out 2 px without anything showing
      const ann = d.querySelector('annotation');
      out.push({at: W(d), what: 'formula', over: d.scrollWidth - d.clientWidth, text: ann ? ann.textContent.slice(0, 90) : ''});
    }
  }
  for (const e of document.querySelectorAll('main .katex-error'))   // a formula KaTeX could not parse (as split into rows, too)
    out.push({at: W(e), what: 'formula', over: 0, text: 'KaTeX error: ' + (e.getAttribute('title') || e.textContent).slice(0, 90)});
  for (const k of document.querySelectorAll('main .katex')) {
    if (!k.checkVisibility() || k.closest('.katex-display, .eq-chain, table, svg, #sim-root')) continue;   // a calculation in rows (.eq-chain) scrolls sideways as a whole
    const box = k.closest('p, li, .steps, .stage') || k.parentElement;
    const over = Math.round(k.getBoundingClientRect().right - (k.closest('.kc-card') ? box.getBoundingClientRect().right : Math.min(box.getBoundingClientRect().right, vw)));   // a concept card's own box is the limit
    if (over > 1) { const ann = k.querySelector('annotation'); out.push({at: W(k), what: 'formula', over, text: 'inline, cannot wrap: ' + (ann ? ann.textContent.slice(0, 70) : '')}); }
  }
  // clipped: a formula whose ink runs past the edge of what shows it (teacher 2026-11-15; fy8-1, fy8-2: "m/s" cut to "m/" in a
  // solution's calculation row, which scrolls sideways on its own, and a long inline formula, which scrolls on its own line).
  // A reviewer sees a screenshot, so what has to be scrolled to is cut off. The limit is the nearest box that clips (overflow
  // other than visible: a calculation chain, a scrolling formula line, a concept card) or the window, measured to the last
  // glyph; a formula cannot rely on scrolling. (display formulas have their own check above)
  const ink = (k) => [...k.querySelectorAll('.katex-html *')].filter((e) => !e.children.length && e.textContent.trim()).reduce((m, e) => Math.max(m, e.getBoundingClientRect().right), 0);
  for (const k of document.querySelectorAll('main .katex')) {
    if (vw > 480 || !V(k) || k.parentElement.closest('.katex') || k.closest('.katex-display, svg, #sim-root, thead, .sim-tex-layer, .fig-tex')) continue;   // a phone's width: what a student scrolls to on a laptop is not the finding
    let lim = vw;
    for (let a = k.parentElement; a && a !== document.body; a = a.parentElement) {
      if (getComputedStyle(a).overflowX === 'visible' || !a.clientWidth) continue;
      lim = Math.min(lim, a.getBoundingClientRect().left + a.clientLeft + a.clientWidth);
    }
    const hidden = Math.max(Math.round(ink(k) - lim), getComputedStyle(k).overflowX === 'visible' ? 0 : k.scrollWidth - k.clientWidth);
    if (hidden > 3) { const ann = k.querySelector('annotation'); out.push({at: W(k), what: 'formula', over: hidden, text: 'clipped or scrolling, not fully shown: ' + (ann ? ann.textContent.slice(0, 70) : '')}); }
  }
  for (const c of document.querySelectorAll('main .eq-chain')) {   // a calculation set as rows (mathlayout.py): its left side must neither spill into the right one
    if (!V(c)) continue;                                          // nor wrap while the chain has room (teacher 2026-10-31, the visual reviewer's fy1-4 and fy3-7 findings)
    const room = c.parentElement.getBoundingClientRect().width - c.getBoundingClientRect().width;
    for (const l of c.querySelectorAll('.eq-l')) {
      const k = l.querySelector('.katex'); if (!k) continue;
      const ann = k.querySelector('annotation'), txt = ann ? ann.textContent.slice(0, 70) : '';
      const kr = k.getBoundingClientRect(), lr = l.getBoundingClientRect();
      if (kr.right > lr.right + 2) out.push({at: W(k), what: 'formula', over: Math.round(kr.right - lr.right), text: 'calculation row: left side runs into the right side: ' + txt});
      const bs = [...k.querySelectorAll('.base')].map((b) => b.getBoundingClientRect());   // KaTeX splits a formula into bases at its operators; a tall base (a fraction) starts higher on the same line,
      const wrapped = bs.some((b) => b.top > bs[0].bottom - 2);                           // so a row has wrapped only when a base starts below the first one's bottom
      if (wrapped && room > 40) out.push({at: W(k), what: 'formula', over: Math.round(room), text: 'calculation row: left side wraps though the chain has room: ' + txt});
    }
  }
  for (const t of document.querySelectorAll('table')) {
    if (t.closest('#sim-root') || !t.checkVisibility()) continue;
    const box = t.parentElement, cs = getComputedStyle(box), room = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    const over = Math.max(t.scrollWidth - t.clientWidth, Math.round(t.getBoundingClientRect().width - room));   // it would scroll, or it is wider than its box (no table scrolls, 2026-11-08)
    if (over > 1) out.push({at: W(t), what: 'table', over, text: t.innerText.replace(/\\s+/g, ' ').slice(0, 60)});
    if (!t.classList.contains('tbl-stack')) for (const k of t.querySelectorAll('th .katex, td .katex')) {   // a cell's formula that scrolls in its column: "E_distri" in a
      if (k.scrollWidth > k.clientWidth + 3) { out.push({at: W(k), what: 'table', over: k.scrollWidth - k.clientWidth, text: 'formula in a cell scrolls, not fully shown: ' + ((k.querySelector('annotation') || {}).textContent || '').slice(0, 50)}); break; }   // heading (en/fy3-15, 2026-11-16)
    }
    if (t.classList.contains('tbl-stack')) for (const c of t.querySelectorAll('td, tbody th')) {   // a stacked table (lesson.js): its label must not run into its value
      const l = c.querySelector(':scope > .tbl-lab'), v = c.querySelector(':scope > .tbl-val');   // ("E_district heating (GWh)" over 1190 at 390 px, en/fy3-15, 2026-11-16)
      if (!l || !v || !v.textContent.trim()) continue;
      const vr = v.getBoundingClientRect(), vl = vr.left, lr = Math.max(ink(l), l.getBoundingClientRect().left + l.scrollWidth);
      if (lr > vl + 1 && l.getBoundingClientRect().bottom > vr.top + 2) { out.push({at: W(l), what: 'table', over: Math.round(lr - vl), text: 'stacked table: label runs into its value: ' + l.textContent.trim().slice(0, 50)}); break; }
    }
  }
  for (const c of document.querySelectorAll('main .eq-chain')) {   // regression 2026-11-04: rows of a calculation collapsed to 0 px (kx-wide inside the grid)
    if (!c.checkVisibility()) continue;
    for (const k of c.querySelectorAll('.katex')) if (k.getBoundingClientRect().width < 4) { out.push({at: W(k), what: 'formula', over: 0, text: 'calculation row collapsed: ' + ((k.querySelector('annotation') || {}).textContent || '').slice(0, 60)}); break; }
  }
  for (const s of document.querySelectorAll('main svg')) {
    const r = s.getBoundingClientRect();
    if (!r.width || !V(s) || s.closest('.kx-wide, .eq-chain')) continue;   // a root sign inside a wide formula's own scrolling line (lesson.js kx-wide) scrolls with it; a picture in a closed <details> has a box but is not drawn (content-visibility), and the 'open' state measures it once it shows (2026-11-11: the root sign of a display formula in fy1-4's closed sim box, laid out at the closed box's width)
    const card = s.closest('.kc-card'), lim = card ? card.getBoundingClientRect().right : vw;   // a concept card's own box is the limit
    if (r.right > lim + 1) out.push({at: W(s), what: 'svg', over: Math.round(r.right - lim), text: s.getAttribute('aria-label') || ''});
    const T = [...s.querySelectorAll('text'), ...s.querySelectorAll('foreignObject')].map((t) => ({t: t.textContent.trim().slice(0, 40), b: (t.querySelector('.katex, div') || t).getBoundingClientRect()})).filter((x) => x.t);
    // the 1 px allowance in the page's own scale (K), like the overlap below; an enlarged drawing is also placed on whole
    // pixels again, which moved a label 0.09 px past K (FY4-sovella, 0.92 px at 1280 px, 1.27 px at 1920 px), so the
    // enlarged page gets a quarter pixel for that. Under 1600 px the allowance is 1 px as before.
    const E = K > 1 ? K + 0.25 : 1;
    for (const x of T) if (x.b.left < r.left - E || x.b.right > r.right + E || x.b.top < r.top - E || x.b.bottom > r.bottom + E)
      out.push({at: W(s), what: 'svg-text', over: Math.round(Math.max(r.left - x.b.left, x.b.right - r.right, r.top - x.b.top, x.b.bottom - r.bottom)), text: `"${x.t}" leaves the figure`});
    for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = T[i].b, b = T[j].b;
      const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left), oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (ox > K && oy > K) out.push({at: W(s), what: 'svg-text', over: Math.round(Math.min(ox, oy)), text: `"${T[i].t}" overlaps "${T[j].t}"`}); }
  }
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
  for (const c of document.querySelectorAll('.lab > *, .fig-row > *, .intro-row > *, .example > *'))
    if (V(c) && c.scrollWidth > c.clientWidth + 3) out.push({at: W(c), what: 'column', over: c.scrollWidth - c.clientWidth, text: c.className});
  for (const t of document.querySelectorAll('main p, main li')) {
    if (!V(t) || t.closest('#sim-root, .katex-display, table')) continue;
    const w = t.getBoundingClientRect().width;
    if (w > 44 * rem + 1) { out.push({at: W(t), what: 'text', over: Math.round(w - 44 * rem), text: `line length: "${t.textContent.trim().slice(0, 50)}"`}); break; }
  }
  const R = (e) => e.getBoundingClientRect();
  const name = (e) => (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\\s+/).join('.') : e.tagName.toLowerCase());
  // overlap: blocks of the same group (siblings) never drawn over each other
  const groups = ['.activity', 'details.opt', 'details.level', '.core-card', '.fig-row', '.fig-row > *', '.intro-row > *', '.sol-step', 'ul.choices > li', '.stage', '#exit > ol > li', 'details.level > ol > li', '.core-card > ol > li'];
  const seen = new Set();
  for (const g of groups) for (const a of document.querySelectorAll(g)) {
    if (!V(a) || a.closest('.lab-side, .example-task')) continue;
    for (const b of a.parentElement.children) {
      if (b === a || !b.matches(g) || !V(b) || seen.has(b)) continue;
      const p = R(a), q = R(b), ox = Math.min(p.right, q.right) - Math.max(p.left, q.left), oy = Math.min(p.bottom, q.bottom) - Math.max(p.top, q.top);
      if (ox > 2 && oy > 2) out.push({at: W(a), what: 'overlap', over: Math.round(Math.min(ox, oy)), text: `${name(a)} and ${name(b)}`});
    }
    seen.add(a);
  }
  // order: the task cards read from top to bottom in the order they are written
  const cards = [...document.querySelectorAll('main .activity, main details.opt')].filter((e) => V(e) && !e.closest('.lab-side, details.opt .activity') && !e.parentElement.closest('.activity'));
  for (let i = 1; i < cards.length; i++) if (R(cards[i]).top < R(cards[i - 1]).top - 1)
    out.push({at: W(cards[i]), what: 'order', over: Math.round(R(cards[i - 1]).top - R(cards[i]).top), text: `${name(cards[i])} shows above ${name(cards[i - 1])}`});
  // gap: a row of two columns where one is far taller than the other (the empty area beside a grown card)
  for (const g of document.querySelectorAll('main *')) {
    const cs = getComputedStyle(g);
    if (cs.display !== 'grid' || !V(g) || g.matches('.lab, .example, ul.choices, .prior ul')) continue;
    if (cs.gridTemplateColumns.trim().split(/\\s+/).length < 2) continue;
    const rows = {};
    for (const c of g.children) { if (!V(c) || getComputedStyle(c).position === 'sticky') continue; const k = Math.round(R(c).top); (rows[k] = rows[k] || []).push(R(c).height); }
    for (const hs of Object.values(rows)) if (hs.length > 1) {
      const hi = Math.max(...hs), lo = Math.min(...hs);
      if (hi - lo > 240 * K && lo < 0.55 * hi) out.push({at: W(g), what: 'gap', over: Math.round(hi - lo), text: `${name(g)}: ${Math.round(hi - lo)} px empty beside the shorter column`});
    }
  }
  // small: reading text keeps its size on a phone, and every control is big enough to hit
  for (const t of document.querySelectorAll('.act-theory > p, .act-theory .fig-text > p, .act-theory li, p.task, fieldset.choice legend, ul.choices label, .hook p, .learn li, details.solution .steps p:not(.sol-label)')) {
    if (!V(t) || t.closest('#sim-root')) continue;
    const fs = parseFloat(getComputedStyle(t).fontSize);
    if (fs < 16.5) { out.push({at: W(t), what: 'small', over: Math.round(17 - fs), text: `${fs} px text: "${t.textContent.trim().slice(0, 40)}"`}); break; }
  }
  for (const c of document.querySelectorAll('main button, main summary, ul.choices label, nav.toc a, form.check input')) {
    if (!V(c) || c.closest('#sim-root') || c.matches('.kc-term-btn')) continue;   // a concept term inside a sentence is an inline target (WCAG 2.5.8 exception)
    if (R(c).height < 39.5) { out.push({at: W(c), what: 'small', over: Math.round(40 - R(c).height), text: `control ${Math.round(R(c).height)} px tall: "${c.textContent.trim().slice(0, 40)}"`}); break; }
  }
  return out;
}"""

OPEN = {
  "closed": "() => true",
  "hints": """() => { for (const g of document.querySelectorAll('.hints, .numeric, .activity, details.level > ol > li, .core-card > ol > li')) {
      const h = g.querySelector('details.hint'); if (h) h.open = true; const s = g.querySelector(':scope details.solution, :scope > details.solution'); if (s) s.open = true; }
    document.querySelectorAll('details.fold, details.level').forEach((d) => { d.open = true; }); if (window.flFitMath) window.flFitMath(); return true; }""",
  "open": """() => { document.querySelectorAll('details').forEach((d) => { d.open = true; });
    document.querySelectorAll('main [hidden]').forEach((e) => { if (!e.closest('#sim-root')) e.hidden = false; }); if (window.flFitMath) window.flFitMath(); return true; }""",
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
        if only and lid not in only: continue
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
        key = page_file.relative_to(OUT).with_suffix("").as_posix()
        for f in found:                               # the same problem in several states is reported once, with its first state
            if not any(u["what"] == f["what"] and u["text"] == f["text"] for u in uniq): uniq.append(f)
        was = [f for f in uniq if f["text"].startswith(CLIPPED) and (key, f["text"][len(CLIPPED):]) in known]   # a clipped formula the page already had
        for f in uniq:
            if f["text"].startswith(CLIPPED) and write_known: found_known.add((key, f["text"][len(CLIPPED):]))
        if write_known: was = [f for f in uniq if f["text"].startswith(CLIPPED)]
        if os.environ.get("CHECK_LAYOUT_NO_CLIPPED"): was = [f for f in uniq if f["text"].startswith(CLIPPED)]   # a test of something else (test_courses.py) with a copied lesson
        uniq = [f for f in uniq if f not in was]
        hard = uniq   # a table too wide for its box fails too: no table scrolls sideways (teacher 2026-11-08)
        tag = f"{OUT.name}/{page_file.relative_to(OUT).with_suffix('').as_posix()} at {width} px"
        if hard:
            bad += 1
            print(f"FAIL {tag}")
            for f in uniq:
                print(f"  {f['what']:8} {f['over']:4} px  [{f['state']}]  {f['text']}" + (f"\n{'':26}at {f['at']}" if f.get('at') else ""))
        else:
            print(f"OK   {tag}" + (f" ({len(was)} known clipped formulas, docs/clipped-formulas/{group(key)}.tsv)" if was else ""))
    b.close()
if write_known:
    by = {}
    for p, t in known | found_known: by.setdefault(group(p), []).append((p, t))
    KNOWN.mkdir(parents=True, exist_ok=True)
    for g, rows in by.items(): (KNOWN / f"{g}.tsv").write_text(KNOWN_HEAD + "".join(f"{p}\t{t}\n" for p, t in sorted(rows)))
sys.exit(1 if bad and not write_known else 0)
