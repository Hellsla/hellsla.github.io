/* Embeds a lesson simulation. Loaded after p5 and before <id>-sim.js, it wraps window.p5 so that a sketch
   written for a fixed 600×400 canvas:
   - is resized to the width of its container and drawn with p.scale(), so text stays crisp on a phone
     (the sketch keeps drawing in 600×400 coordinates and never handles resizing itself),
   - pauses when it is scrolled out of view and resumes when it comes back (battery, and 80 bouncing
     particles need not run under the exercises),
   - runs at a low frame rate when the reader prefers reduced motion,
   - uses the page's own font inside the canvas,
   - folds a long explanation under the canvas (p.note, from a sim written before 2026-10-26) behind a closed
     "Mallin oletukset ja selitys" box, so the picture, the controls and the values come first; one legend line of
     at most 15 words stays visible. New sims put no explanation in the page: the lesson's inquiry.json carries
     Käyttöohje, Mallin oletukset and Laskennan selitys (NOTES.md §4).
   - draws every p.text() string that contains $…$ with KaTeX in a layer over the canvas, at the same place, size,
     alignment and fill colour as p.text would (teacher's rule 2026-10-26: every symbol and label is LaTeX, the
     simulation too); words outside the dollars stay text in the page font. A p5 element's .html() with $…$ (the
     readout, a legend) renders its maths the same way, and is re-rendered only when its string changes.
   Tests run at 1280 px, where the container is wider than 600 px, so the canvas keeps its native size there.
   - draws a static simulation only when something changes (2026-11-05, performance): a sim named in STATIC below has
     no motion of its own; its picture follows its controls, the pointer and its own events. It is drawn after setup,
     after any input, change, click, key or pointer event on it, a resize, a font load, a return into view and an
     adapter call, for a few frames until the picture and simState stop changing (an eased value settles), never in a
     60 fps loop. If it keeps changing for STATIC_MAX frames it is not static after all and loops as before.
     ?simloop=1 (or window.flSimLoop = true before the page loads) keeps the old continuous loop, for comparison tests.
   - "Suurenna" (teacher 2026-11-03, "simulaatiot saa klikattua isoksi") shows the whole simulation card full screen
     (the Fullscreen API, or a fixed layer where it is missing, as on an iPhone); the canvas then fills the window
     (teacher 2026-11-03: no empty margins; the Käyttöohje and model boxes are hidden there), the controls stay beside it on a wide screen, and Esc or "Pienennä" brings it back.
   It also defines window.defineSimAdapter (docs/inquiry.md, "Simulation interface"): a sim that calls it once
   from setup exposes a small adapter that guided investigations (inquiry.js) use to read the state, set
   parameters, lock controls, reset and pause. The physics stays in the sim; window.simState is untouched.
   Texts: the page's #fl-strings block (build.py, from lang/<lang>.json) carries the simulation's own block of
   "sims"; __('key') and __(`key`, {name: value}) give the sim its buttons, labels and readouts (scripts/i18n.py), and
   __v(value) shows an identifier the sim also uses as a value (a material, a body) from that block's "values". An
   option of a select whose label is such a value shows it the same way and keeps its value. */
(() => {
  let S = {};
  try { S = JSON.parse(document.getElementById('fl-strings').textContent) || {}; } catch (e) { S = {}; }
  const sim = S.sim || {}, values = sim.values || {}, own = (o, k) => Object.prototype.hasOwnProperty.call(o, k);
  const fill = (s, v) => s.replace(/\{\{(\w+)\}\}/g, (m, n) => (v && own(v, n) ? String(v[n]) : m));
  window.__ = (key, v) => (typeof sim[key] === 'string' ? fill(sim[key], v) : key);
  window.__v = (x) => (own(values, x) ? values[x] : x);
  window.flMsg = (key) => { const s = (S.js || {})[key]; return typeof s === 'string' ? s : key; };
})();
(() => {
  const Base = window.p5;
  if (!Base || Base.__fysiikkalabra) return;
  const W = 600; let H = 400;
  const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const font = (getComputedStyle(document.body).fontFamily.split(',')[0] || '').replace(/["']/g, '').trim();
  const foldNotes = (root) => {
    let box = null;
    [...root.children].forEach((el) => {
      if (!(el.tagName === 'P' && el.classList.contains('note') && el.textContent.trim().split(/\s+/).length > 15)) { box = null; return; }
      if (!box) { box = document.createElement('details'); box.className = 'note'; box.innerHTML = '<summary>' + window.flMsg('sim_note') + '</summary>'; el.before(box); }
      box.appendChild(el);
    });
  };

  const MATH = { delimiters: [{ left: '$', right: '$', display: false }], throwOnError: false };
  let fontGen = 0;                             // bumped when a web font (KaTeX's) finishes loading: label sizes measured before it are stale
  const onFont = new Set(), simWakers = new Set();   // the on-demand sims to draw again with new metrics, or after an adapter call
  window.flSimWake = () => simWakers.forEach((f) => f());
  const fontLoaded = () => { fontGen++; onFont.forEach((f) => f()); };
  try { document.fonts.addEventListener('loadingdone', fontLoaded); document.fonts.ready.then(fontLoaded); } catch (e) { /* no FontFaceSet */ }
  // the sims without motion of their own (2026-11-05): checked by scripts/test_sims.py, which fails a listed sim that
  // changes while nothing happens or whose drawn result differs from the continuous loop's. Names: sims/<course>/<name>
  // as "fy6/fy6-9"; FY3's <id>-sim.js as "fy3-4".
  const STATIC = new Set([/*STATIC*/
    'fy1/fy1-4', 'fy2/fy2-2', 'fy5/fy5-2', 'fy5/fy5-5', 'fy5/fy5-8', 'fy6/fy6-2', 'fy6/fy6-5', 'fy6/fy6-9', 'fy6/fy6-10', 'fy6/fy6-11', 'fy6/fy6-13', 'fy6/fy6-14',
    'fy7/fy7-4', 'fy7/fy7-8', 'fy7/fy7-9', 'fy7/fy7-10', 'fy7/fy7-11', 'fy7/fy7-12', 'fy7/fy7-13', 'fy7/fy7-14', 'fy7/fy7-15', 'fy7/fy7-16', 'fy8/fy8-5', 'fy8/fy8-6', 'fy8/fy8-10',
  /*END*/]);
  const STATIC_MAX = 240;                      // frames of change after one event before a listed sim counts as animated
  const loopAlways = (() => { try { return window.flSimLoop === true || /[?&]simloop=1\b/.test(location.search); } catch (e) { return false; } })();
  const simName = (src) => {
    const m = /sims\/([^/]+\/[^/]+)\/sim\.js(?:[?#]|$)/.exec(src || '') || /(?:^|\/)([^/]+)-sim\.js(?:[?#]|$)/.exec(src || '');
    return m ? m[1] : '';
  };
  // the size of a $…$ label does not depend on which digits its formulas hold: KaTeX's upright fonts give every digit
  // the same advance (checked in Chromium over 1000 labels at five sizes, 2026-11-12). A label with a live value
  // ("$\theta = 296^\circ$") is therefore measured once per shape ("$\theta = 000^\circ$"), not at every frame:
  // each measurement made the browser lay the lesson page out again (fy7-7 and fy3-10 ran at 3–5 fps on a phone).
  // Bold, italic, sans, typewriter and the other font changes have digits of their own widths, and a dimension, a
  // colour or a character code is a number that is not drawn: such a formula is kept as it is.
  const OWN_DIGITS = /\\(?:bf|it|sf|tt|rm|sl|bm|pmb|boldsymbol|bold|emph|math[a-z]*|text(?!(?:rm)?\{)[a-z]+|color|colorbox|fcolorbox|[hvm]?space|[hvm]?skip|m?kern|rule|raisebox|char|html[A-Za-z]*|href|url|tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge|size\d|includegraphics)(?![A-Za-z])/;
  const shape = (str) => str.replace(/\$[^$]+\$/g, (m) => (/\d/.test(m) && !OWN_DIGITS.test(m.replace(/\\(?:mathrm|operatorname)\{/g, '{')) ? m.replace(/\d/g, '0') : m));
  // a sketch reads the width of its box at every frame (document.getElementById('sim-root').clientWidth, 98 sims, to
  // keep its text legible on a phone) right after writing its readout, and p.text below reads the canvas's size for
  // every $…$ label after placing the one before: each read made the browser lay the lesson page out again before the
  // frame was drawn (2026-11-12). These sizes are kept here and read again only after the element has changed size
  // (a ResizeObserver, made before the one that redraws the canvas, so a redraw sees the new size) or the canvas has
  // been resized (fit below). keep(el, 'clientWidth') for a box whose height follows its readout at every frame.
  const CLIENT = { clientWidth: 'width', clientHeight: 'height' };
  const keep = (el, ...props) => {
    if (!el || el.__flKept || !('ResizeObserver' in window)) return () => {};
    const got = {}, seen = {};
    for (const k of props) {
      const d = Object.getOwnPropertyDescriptor(Element.prototype, k);
      if (!d || !d.get) return () => {};
      got[k] = null;
      Object.defineProperty(el, k, { configurable: true, get() { if (got[k] === null) got[k] = d.get.call(el); return got[k]; } });
    }
    const reset = () => { for (const k of props) got[k] = null; };
    el.__flKept = true;
    new ResizeObserver((es) => {
      const r = es[es.length - 1].contentRect;
      for (const k of props) if (r[CLIENT[k]] !== seen[k]) { seen[k] = r[CLIENT[k]]; got[k] = null; }
    }).observe(el);
    return reset;
  };
  const mixed = (el, str) => {                 // "Massa $m = 10$ kg": text nodes and KaTeX spans
    el.textContent = '';
    str.split(/(\$[^$]+\$)/).forEach((part) => {
      if (!part) return;
      if (part.length > 2 && part[0] === '$' && part[part.length - 1] === '$') {
        const span = document.createElement('span');
        try { window.katex.render(part.slice(1, -1), span, { throwOnError: false }); } catch (e) { span.textContent = part; }
        el.appendChild(span);
      } else el.appendChild(document.createTextNode(part));
    });
  };
  // the page is written once per frame, after the sketch has drawn it (2026-11-12, performance): p5 sets the canvas
  // font at every textSize() and textAlign(), and the browser works out the styles of the whole lesson page before it
  // takes a canvas font whenever the page has changed since, so a readout or a label written in the middle of draw()
  // cost a restyle of the page at each following text call (fy3-10: about 70 ms a frame on a phone). While draw() runs,
  // a p5 element's .html(…) and the KaTeX labels below wait in `pend`; they are written in order when draw() returns.
  // Reading .html() flushes them first.
  let drawing = 0, pend = [];
  const later = (fn) => { if (drawing) pend.push(fn); else fn(); };
  const flush = () => { while (pend.length) { const q = pend; pend = []; q.forEach((fn) => fn()); } };
  if (Base.Element && !Base.Element.prototype.__tex) {
    const html = Base.Element.prototype.html;
    const write = (el, a) => {
      if (a[1] || typeof a[0] !== 'string' || !a[0].includes('$')) { el.__texLast = null; return html.apply(el, a); }
      if (el.__texLast === a[0]) return el;    // the readout is set every frame; KaTeX runs only on a change
      el.__texLast = a[0];
      const r = html.apply(el, a);
      if (window.renderMathInElement) window.renderMathInElement(el.elt, MATH);
      return r;
    };
    Base.Element.prototype.html = function (...a) {
      if (!a.length) { flush(); return html.apply(this, a); }
      if (drawing) { pend.push(() => write(this, a)); return this; }
      return write(this, a);
    };
    Base.Element.prototype.__tex = true;
  }

  class Embedded extends Base {
    constructor(sketch, node) {
      const script = document.currentScript;     // the sim's own <script> runs `new p5(...)`
      const name = simName(script && script.src);
      const onDemand = !loopAlways && !!name && STATIC.has(name);
      super((p) => {
        const createSelect = p.createSelect;     // an option labelled with one of the sim's values: shown translated, value kept
        p.createSelect = function (...a) {
          const sel = createSelect.apply(this, a), option = sel && sel.option;
          if (option) sel.option = function (name, value) {
            const shown = typeof name === 'string' ? window.__v(name) : name;
            return shown === name ? option.apply(this, arguments) : option.call(this, shown, value === undefined ? name : value);
          };
          return sel;
        };
        sketch(p);
        const setup = p.setup, draw = p.draw;
        let s = 1, internal = false, canvasSize = () => {};
        let layer = null, labels = [], used = 0;
        const text = p.text;
        // the canvas and its KaTeX layer share a box (.sim-canvas); fit() sizes the canvas to that box, so the page can
        // narrow it (site.css: on a short screen the simulation beside the experiments keeps its controls in view)
        const wrapCanvas = () => {
          if (layer || !p.canvas) return;
          const wrap = document.createElement('div'); wrap.className = 'sim-canvas';
          p.canvas.before(wrap); wrap.appendChild(p.canvas);
          layer = document.createElement('div'); layer.className = 'sim-tex-layer'; layer.setAttribute('aria-hidden', 'true');
          wrap.appendChild(layer);
        };
        p.text = function (str, x, y, ...rest) {
          if (typeof str !== 'string' || !str.includes('$') || !window.katex || !p.canvas) return text.call(p, str, x, y, ...rest);
          if (!layer) wrapCanvas();
          const ctx = p.drawingContext, m = ctx.getTransform(), pd = p.pixelDensity();
          const k = (p.canvas.clientWidth || p.width) / p.width;        // CSS size of the canvas against its own size
          const al = p.textAlign();
          let el = labels[used];
          if (!el) { el = document.createElement('div'); el.className = 'sim-tex'; labels.push(el); }
          used++;
          const st = el.style;
          const lx = (m.a * x + m.c * y + m.e) / pd * k, ly = (m.b * x + m.d * y + m.f) / pd * k;
          const shown = Number.isFinite(lx) && Number.isFinite(ly) ? '' : 'none';   // a label at NaN (an empty average) is not drawn, as on the canvas
          const sz = p.textSize() * Math.hypot(m.a, m.b) / pd;   // in canvas pixels
          const fs = Math.max(sz * (k < 1 ? Math.sqrt(k) : k), Math.min(sz, 10)).toFixed(2) + 'px';   // a phone-sized canvas shrinks its labels less than its picture, never below 10 px
          const color = ctx.fillStyle;
          const put = () => {                    // the label's text, size and colour (written after draw(), above)
            if (!el.parentNode) layer.appendChild(el);
            if (el.__s !== str) { mixed(el, str); el.__s = str; }
            st.display = shown; st.fontSize = fs; st.color = color;
          };
          const sh = shape(str);
          const measure = el.__fs !== fs || el.__ms !== sh || el.__fg !== fontGen || !el.__w;   // only when the label's shape (above) or its size changes
          if (measure) { put(); const r = el.getBoundingClientRect(); el.__w = r.width; el.__h = r.height; el.__fs = fs; el.__ms = sh; el.__fg = fontGen; }
          const fx = { left: 0, center: -0.5, right: -1 }[al.horizontal] || 0;
          const fy = { top: 0, center: -0.5, bottom: -1 }[al.vertical] ?? -0.78;   // alphabetic: baseline near 78 % of the line
          const cw = p.canvas.clientWidth || p.width * k, ch = p.canvas.clientHeight || p.height * k;
          // the larger phone labels are kept inside the canvas
          const left = Math.max(0, Math.min(lx + fx * el.__w, cw - el.__w)).toFixed(1) + 'px';
          const top = Math.max(0, Math.min(ly + fy * el.__h, ch - el.__h)).toFixed(1) + 'px';
          later(() => { if (!measure) put(); st.left = left; st.top = top; });
          return p;
        };
        // the widths of $…$ labels, measured once per text size and font state. A sim whose label carries a live value
        // ("$t = 1{,}23\,\text{s}$") asks for a new string every frame, so the cache is bounded (least recently used out)
        // and emptied when a font finishes loading, since every width measured before it is stale (2026-11-05).
        const textWidth = p.textWidth, widths = new Map(), WIDTHS_MAX = 400;
        let meter = null, widthsGen = fontGen;
        p.textWidth = function (str) {           // the width of a $…$ label as KaTeX draws it, in sketch units
          if (typeof str !== 'string' || !str.includes('$') || !window.katex) return textWidth.call(p, str);
          if (widthsGen !== fontGen) { widths.clear(); widthsGen = fontGen; }
          // measured at the size the label is drawn at (p.text above: the canvas scale, the phone rule and the 10 px floor)
          // and turned back into sketch units. A browser's glyph widths are not proportional to the font size: one that
          // rounds glyph advances to whole pixels (Chromium 158 on the CI machine) draws a label at 11,76 px about 5 %
          // wider than its width at 24 px scaled down, so a row laid out from the scaled width overlapped (fy1-1 at
          // 360 px: laid out 199,9 px, drawn 210 px; measured by .github/diag/sim_labels.py, 2026-11-11).
          let fsz = p.textSize(), per = 1;
          if (p.canvas && p.drawingContext && p.drawingContext.getTransform) {
            const m = p.drawingContext.getTransform(), u = Math.hypot(m.a, m.b) / p.pixelDensity(), k = (p.canvas.clientWidth || p.width) / p.width;
            if (u > 0 && k > 0) { const sz = p.textSize() * u; fsz = +Math.max(sz * (k < 1 ? Math.sqrt(k) : k), Math.min(sz, 10)).toFixed(2); per = u * k; }
          }
          const key = fsz + '|' + shape(str);   // one width per shape (above), so a live value needs no new measurement
          let w = widths.get(key);
          if (w === undefined) {
            if (!meter) { meter = document.createElement('div'); meter.className = 'sim-tex'; meter.style.cssText = 'position:absolute;visibility:hidden;left:-9999px;top:0'; document.body.appendChild(meter); }
            meter.style.fontSize = fsz + 'px'; mixed(meter, str);
            w = meter.getBoundingClientRect().width;
            if (widths.size >= WIDTHS_MAX) widths.delete(widths.keys().next().value);
          } else widths.delete(key);             // re-inserted below: the most recently used last
          widths.set(key, w);
          return w / per;
        };
        // p5 measures a font's ascent and descent by putting elements on the page and reading their position, which lays
        // the whole lesson out again at every call; a sim that records its label boxes (lab(): textAscent and textDescent
        // per label) then spends seconds on a frame of a long page. Both depend only on the font, its style and its
        // size, so each is measured once per such state and emptied when a font finishes loading (2026-11-11).
        const metrics = new Map(); let metricsGen = fontGen;
        for (const fn of ['textAscent', 'textDescent']) {
          const measure = p[fn];
          p[fn] = function () {
            if (metricsGen !== fontGen) { metrics.clear(); metricsGen = fontGen; }
            const r = p._renderer, f = r && r._textFont, key = fn + '|' + p.textSize() + '|' + (r && r._textStyle) + '|' + (f && typeof f === 'object' ? 'obj' : f);
            if (f && typeof f === 'object') return measure.call(p);      // a loaded font file: p5 reads its own table, no layout
            let v = metrics.get(key);
            if (v === undefined) { if (metrics.size >= 200) metrics.clear(); v = measure.call(p); metrics.set(key, v); }
            return v;
          };
        }
        // read by scripts/test_sims.py: how the sim is drawn, and the label-width cache
        window.flSimInfo = () => ({ name, onDemand: onDemand && !animated, animated, draws: p.__flDraws, looping: p.isLooping(),
                                    widths: widths.size, widthsMax: WIDTHS_MAX });
        window.flSimRedraw = () => p.redraw();
        window.flSimTextWidth = (str, size) => { p.push(); if (size) p.textSize(size); const w = p.textWidth(str); p.pop(); return w; };
        const root = () => (p.canvas && p.canvas.parentElement) || document.getElementById('sim-root');
        const fit = () => {
          const el = root();
          if (!el || !p.canvas) return;
          const big = el.closest && el.closest('#sim.sim-expanded');   // enlarged (part below): as large as the window allows (site.css keeps it on screen)
          const w = Math.min(big ? 5 * W : W, el.clientWidth || W);
          if (big) el.style.setProperty('--sim-ar-x', (W / H).toFixed(4));
          const ns = Math.max(0.3, w / W);
          if (Math.abs(ns - s) < 0.002 && p.height === Math.round(H * s)) return;
          s = ns;
          internal = true; p.resizeCanvas(Math.round(W * s), Math.round(H * s), true); internal = false; canvasSize();
          p.redraw();
        };
        const rc = p.resizeCanvas;           // a sketch that stacks its panels on a phone asks for p.resizeCanvas(600, taller): the box keeps its 600 width
        p.resizeCanvas = function (w, h, ...r) {
          if (internal) return rc.call(p, w, h, ...r);
          if (w === W && h !== H) { H = h; s = 0; fit(); }
        };
        p.setup = () => {
          keep(document.getElementById('sim-root'), 'clientWidth');
          if (setup) setup();
          if (!p.canvas) return;
          const simRoot = document.getElementById('sim-root');
          if (simRoot) foldNotes(simRoot);
          if (simRoot && window.renderMathInElement) window.renderMathInElement(simRoot, MATH);   // labels and legends set once
          wrapCanvas();
          keep(p.canvas.parentElement, 'clientWidth');
          canvasSize = keep(p.canvas, 'clientWidth', 'clientHeight');
          fit();
          const resized = () => { fit(); wake(); };
          if ('ResizeObserver' in window) new ResizeObserver(resized).observe(root());
          else window.addEventListener('resize', resized);
          if ('IntersectionObserver' in window) {
            new IntersectionObserver((entries) => {
              entries.forEach((en) => { if (onDemand && !animated) { if (en.isIntersecting) wake(); } else if (en.isIntersecting) loop.call(p); else p.noLoop(); });
            }, { rootMargin: '120px 0px' }).observe(p.canvas);
          }
          if (reduced) p.frameRate(12);
          if (font && document.fonts && document.fonts.load) {
            document.fonts.load('16px "' + font + '"').then(() => { p.textFont(font); wake(); }).catch(() => {});
          }
          if (onDemand) startOnDemand();
        };
        // on-demand drawing of a STATIC sim (header): p.redraw() in bursts that end when the picture and the state stop changing
        let burst = 0, frame = 0, still = 0, lastSig = null, thumb = null, animated = false;
        p.__flDraws = 0;                         // frames drawn, for scripts/test_sims.py
        const loop = p.loop;
        const signature = () => {
          let st = '';
          try { st = JSON.stringify(window.simState); } catch (e) { st = String(Math.random()); }
          try {
            if (!thumb) { thumb = document.createElement('canvas'); thumb.width = 48; thumb.height = 32; }
            const t = thumb.getContext('2d', { willReadFrequently: true });
            t.clearRect(0, 0, 48, 32); t.drawImage(p.canvas, 0, 0, 48, 32);
            const d = t.getImageData(0, 0, 48, 32).data; let h = 0;
            for (let i = 0; i < d.length; i++) h = (h * 31 + d[i]) | 0;
            st += '|' + h + '|' + p.width + 'x' + p.height;
          } catch (e) { /* a tainted or missing canvas: the state alone */ }
          return st;
        };
        const tick = () => {
          frame = 0;
          if (animated) return;
          p.redraw();
          const sig = signature();
          still = sig === lastSig ? still + 1 : 0; lastSig = sig;
          burst++;
          if (burst >= STATIC_MAX) { animated = true; onFont.delete(wake); simWakers.delete(wake); p.loop = loop; loop.call(p); return; }   // moving on its own: as before
          if (burst < 3 || still < 2) frame = requestAnimationFrame(tick);
          else burst = 0;
        };
        function wake() {
          if (!onDemand || animated || !p.canvas) return;
          still = 0; burst = Math.min(burst, 1);
          if (!frame) frame = requestAnimationFrame(tick);
        }
        const startOnDemand = () => {
          p.noLoop();
          p.loop = () => wake();                 // the adapter's resume() and a sketch's own loop(): one more burst
          onFont.add(wake); simWakers.add(wake);
          const box = document.getElementById('sim') || root();
          ['input', 'change', 'click', 'keydown', 'keyup'].forEach((t) => box.addEventListener(t, wake, true));
          let over = false, held = false;
          const near = (e) => {                  // p5 reads the pointer on the whole window: wake on it over the canvas, while a
            const pt = e.changedTouches && e.changedTouches[0] ? e.changedTouches[0] : e;   // press that began there lasts, and once on leaving
            const r = p.canvas.getBoundingClientRect();
            const now = pt.clientX >= r.left && pt.clientX <= r.right && pt.clientY >= r.top && pt.clientY <= r.bottom;
            if (/down|start/.test(e.type) && now) held = true;
            if (now || over || held) wake();
            if (/up|end|cancel/.test(e.type)) held = false;
            over = now;
          };
          ['pointermove', 'pointerdown', 'pointerup', 'pointercancel', 'touchstart', 'touchmove', 'touchend', 'touchcancel'].forEach((t) => window.addEventListener(t, near, { passive: true }));
          p.canvas.addEventListener('wheel', wake, { passive: true });
          window.addEventListener('keydown', wake); window.addEventListener('keyup', wake);
          wake();
        };
        if (draw) p.draw = () => {
          used = 0; p.__flDraws++;
          drawing++;
          try { p.push(); p.scale(s); draw(); p.pop(); } finally { drawing--; if (!drawing) flush(); }   // the page's writes of this frame, at once
          for (let i = used; i < labels.length; i++) labels[i].style.display = 'none';   // a label not drawn this frame
        };
      }, node);
    }
  }
  Embedded.__fysiikkalabra = true;
  window.addEventListener('DOMContentLoaded', () => expandable(document.getElementById('sim')));
  const expandable = (box) => {
    if (!box || box.querySelector(':scope > .sim-expand')) return;
    const b = document.createElement('button'); b.type = 'button'; b.className = 'sim-expand';
    const ICON = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="%" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    const OUT = 'M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5', IN = 'M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5';
    const label = (on) => {
      b.innerHTML = ICON.replace('%', on ? IN : OUT);   // the icon alone (teacher 2026-11-03); its name is the label and the tooltip
      b.setAttribute('aria-label', window.flMsg(on ? 'sim_shrink_aria' : 'sim_expand_aria')); b.title = window.flMsg(on ? 'sim_shrink_aria' : 'sim_expand_aria');
    };
    let back = 0;
    const fs = () => document.fullscreenElement || document.webkitFullscreenElement;
    const set = (on) => {
      if (box.classList.contains('sim-expanded') === on) return;
      if (on) back = window.scrollY;
      box.classList.toggle('sim-expanded', on);
      document.documentElement.classList.toggle('sim-open', on);
      label(on);
      if (!on) { window.scrollTo(0, back); b.focus({ preventScroll: true }); }
    };
    const toggle = (on) => {
      set(on);
      const req = box.requestFullscreen || box.webkitRequestFullscreen, exit = document.exitFullscreen || document.webkitExitFullscreen;
      if (on && req) { try { const r = req.call(box); if (r && r.catch) r.catch(() => {}); } catch (e) { /* a fixed layer is enough */ } }
      if (!on && fs() && exit) { try { const r = exit.call(document); if (r && r.catch) r.catch(() => {}); } catch (e) { /* already left */ } }
    };
    b.addEventListener('click', () => toggle(!box.classList.contains('sim-expanded')));
    const left = () => { if (!fs() && box.classList.contains('sim-expanded')) set(false); };   // Esc ends full screen: the card returns too
    document.addEventListener('fullscreenchange', left); document.addEventListener('webkitfullscreenchange', left);
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && box.classList.contains('sim-expanded')) toggle(false); });
    label(false);
    box.prepend(b);
  };
  window.p5 = Embedded;
})();

/* window.simText(el): the text of a sim element with each KaTeX formula as its TeX source between dollars
   ("Massa $m = 10\,\text{kg}$ (sama kaikkialla)"), for tests that read the readout. */
window.simText = (el) => {
  if (typeof el === 'string') el = document.querySelector(el);
  if (!el) return '';
  const c = el.cloneNode(true);
  c.querySelectorAll('.katex').forEach((k) => { const a = k.querySelector('annotation'); k.replaceWith('$' + (a ? a.textContent : k.textContent) + '$'); });
  return c.textContent;
};

/* window.defineSimAdapter({ params, reset, pause, resume, get })
   params: { name: { input: <input or select element>, unit: 'N' } } — every parameter an investigation may set
   or lock. set() writes the value and fires input + change, so a sketch that reads its controls each frame
   (p5 slider.value()) or on events sees the change at once; lock() disables the control and marks its label.
   reset(): the sim's own function that returns every control to its default and stops any motion.
   step(): draws one frame (p.redraw()), so that get() after set() returns fresh values even while the sketch is
   paused off-screen. get(): defaults to window.simState. pause()/resume(): optional, the sketch's own noLoop()/loop(). */
window.defineSimAdapter = (spec) => {
  const params = spec.params || {};
  const wake = () => { if (window.flSimWake) window.flSimWake(); };   // a static sim drawn on demand (sim-embed.js above) settles after the call
  const fire = (el) => { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); };
  const el = (k) => { const p = params[k]; return p && (typeof p.input === 'string' ? document.querySelector(p.input) : p.input); };
  const adapter = {
    params,
    capabilities: { set: Object.keys(params), lock: true, reset: typeof spec.reset === 'function', pause: typeof spec.pause === 'function' },
    get() { if (spec.step) spec.step(); return (spec.get || (() => window.simState))(); },
    set(values) { Object.entries(values).forEach(([k, v]) => { const e = el(k); if (!e) return; if (e.tagName === 'SELECT') e.value = String(v); else e.value = v; fire(e); }); if (spec.step) spec.step(); wake(); },
    lock(k, on) { const e = el(k); if (!e) return; e.disabled = !!on; e.setAttribute('aria-disabled', on ? 'true' : 'false'); e.closest('label')?.classList.toggle('locked', !!on); },
    reset() { Object.keys(params).forEach((k) => adapter.lock(k, false)); if (spec.reset) spec.reset(); if (spec.step) spec.step(); wake(); },
    pause() { if (spec.pause) spec.pause(); }, resume() { if (spec.resume) spec.resume(); wake(); },
  };
  window.simAdapter = adapter;
  return adapter;
};
