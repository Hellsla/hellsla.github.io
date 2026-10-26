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
   It also defines window.defineSimAdapter (docs/inquiry.md, "Simulation interface"): a sim that calls it once
   from setup exposes a small adapter that guided investigations (inquiry.js) use to read the state, set
   parameters, lock controls, reset and pause. The physics stays in the sim; window.simState is untouched. */
(() => {
  const Base = window.p5;
  if (!Base || Base.__fysiikkalabra) return;
  const W = 600, H = 400;
  const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const font = (getComputedStyle(document.body).fontFamily.split(',')[0] || '').replace(/["']/g, '').trim();
  const foldNotes = (root) => {
    let box = null;
    [...root.children].forEach((el) => {
      if (!(el.tagName === 'P' && el.classList.contains('note') && el.textContent.trim().split(/\s+/).length > 15)) { box = null; return; }
      if (!box) { box = document.createElement('details'); box.className = 'note'; box.innerHTML = '<summary>Mallin oletukset ja selitys</summary>'; el.before(box); }
      box.appendChild(el);
    });
  };

  const MATH = { delimiters: [{ left: '$', right: '$', display: false }], throwOnError: false };
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
  if (Base.Element && !Base.Element.prototype.__tex) {
    const html = Base.Element.prototype.html;
    Base.Element.prototype.html = function (...a) {
      if (!a.length || a[1] || typeof a[0] !== 'string' || !a[0].includes('$')) { this.__texLast = null; return html.apply(this, a); }
      if (this.__texLast === a[0]) return this;   // the readout is set every frame; KaTeX runs only on a change
      this.__texLast = a[0];
      const r = html.apply(this, a);
      if (window.renderMathInElement) window.renderMathInElement(this.elt, MATH);
      return r;
    };
    Base.Element.prototype.__tex = true;
  }

  class Embedded extends Base {
    constructor(sketch, node) {
      super((p) => {
        sketch(p);
        const setup = p.setup, draw = p.draw;
        let s = 1;
        let layer = null, labels = [], used = 0;
        const text = p.text;
        p.text = function (str, x, y, ...rest) {
          if (typeof str !== 'string' || !str.includes('$') || !window.katex || !p.canvas) return text.call(p, str, x, y, ...rest);
          if (!layer) {
            const wrap = document.createElement('div'); wrap.className = 'sim-canvas';
            p.canvas.before(wrap); wrap.appendChild(p.canvas);
            layer = document.createElement('div'); layer.className = 'sim-tex-layer'; layer.setAttribute('aria-hidden', 'true');
            wrap.appendChild(layer);
          }
          const ctx = p.drawingContext, m = ctx.getTransform(), pd = p.pixelDensity();
          const k = (p.canvas.clientWidth || p.width) / p.width;        // CSS size of the canvas against its own size
          const al = p.textAlign();
          let el = labels[used];
          if (!el) { el = document.createElement('div'); el.className = 'sim-tex'; layer.appendChild(el); labels.push(el); }
          used++;
          if (el.__s !== str) { mixed(el, str); el.__s = str; }
          const st = el.style;
          st.display = '';
          st.left = ((m.a * x + m.c * y + m.e) / pd * k).toFixed(1) + 'px';
          st.top = ((m.b * x + m.d * y + m.f) / pd * k).toFixed(1) + 'px';
          st.fontSize = (p.textSize() * Math.hypot(m.a, m.b) / pd * k).toFixed(2) + 'px';
          st.color = ctx.fillStyle;
          const tx = { left: '0', center: '-50%', right: '-100%' }[al.horizontal] || '0';
          const ty = { top: '0', center: '-50%', bottom: '-100%' }[al.vertical] || '-78%';   // alphabetic: baseline near 78 % of the line
          st.transform = `translate(${tx},${ty})`;
          return p;
        };
        const textWidth = p.textWidth, widths = new Map();
        let meter = null;
        p.textWidth = function (str) {           // the width of a $…$ label as KaTeX draws it, in sketch units
          if (typeof str !== 'string' || !str.includes('$') || !window.katex) return textWidth.call(p, str);
          const key = p.textSize() + '|' + str;
          if (!widths.has(key)) {
            if (!meter) { meter = document.createElement('div'); meter.className = 'sim-tex'; meter.style.cssText = 'position:absolute;visibility:hidden;left:-9999px;top:0'; document.body.appendChild(meter); }
            meter.style.fontSize = p.textSize() + 'px'; mixed(meter, str);
            widths.set(key, meter.getBoundingClientRect().width);
          }
          return widths.get(key);
        };
        const root = () => (p.canvas && p.canvas.parentElement) || document.getElementById('sim-root');
        const fit = () => {
          const el = root();
          if (!el || !p.canvas) return;
          const w = Math.min(W, el.clientWidth || W);
          const ns = Math.max(0.3, w / W);
          if (Math.abs(ns - s) < 0.002) return;
          s = ns;
          p.resizeCanvas(Math.round(W * s), Math.round(H * s), true);
          p.redraw();
        };
        p.setup = () => {
          if (setup) setup();
          if (!p.canvas) return;
          const simRoot = document.getElementById('sim-root');
          if (simRoot) foldNotes(simRoot);
          if (simRoot && window.renderMathInElement) window.renderMathInElement(simRoot, MATH);   // labels and legends set once
          fit();
          if ('ResizeObserver' in window) new ResizeObserver(fit).observe(root());
          else window.addEventListener('resize', fit);
          if ('IntersectionObserver' in window) {
            new IntersectionObserver((entries) => {
              entries.forEach((en) => { if (en.isIntersecting) p.loop(); else p.noLoop(); });
            }, { rootMargin: '120px 0px' }).observe(p.canvas);
          }
          if (reduced) p.frameRate(12);
          if (font && document.fonts && document.fonts.load) {
            document.fonts.load('16px "' + font + '"').then(() => { p.textFont(font); }).catch(() => {});
          }
        };
        if (draw) p.draw = () => {
          used = 0;
          p.push(); p.scale(s); draw(); p.pop();
          for (let i = used; i < labels.length; i++) labels[i].style.display = 'none';   // a label not drawn this frame
        };
      }, node);
    }
  }
  Embedded.__fysiikkalabra = true;
  window.p5 = Embedded;
})();

/* window.defineSimAdapter({ params, reset, pause, resume, get })
   params: { name: { input: <input or select element>, unit: 'N' } } — every parameter an investigation may set
   or lock. set() writes the value and fires input + change, so a sketch that reads its controls each frame
   (p5 slider.value()) or on events sees the change at once; lock() disables the control and marks its label.
   reset(): the sim's own function that returns every control to its default and stops any motion.
   step(): draws one frame (p.redraw()), so that get() after set() returns fresh values even while the sketch is
   paused off-screen. get(): defaults to window.simState. pause()/resume(): optional, the sketch's own noLoop()/loop(). */
window.defineSimAdapter = (spec) => {
  const params = spec.params || {};
  const fire = (el) => { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); };
  const el = (k) => { const p = params[k]; return p && (typeof p.input === 'string' ? document.querySelector(p.input) : p.input); };
  const adapter = {
    params,
    capabilities: { set: Object.keys(params), lock: true, reset: typeof spec.reset === 'function', pause: typeof spec.pause === 'function' },
    get() { if (spec.step) spec.step(); return (spec.get || (() => window.simState))(); },
    set(values) { Object.entries(values).forEach(([k, v]) => { const e = el(k); if (!e) return; if (e.tagName === 'SELECT') e.value = String(v); else e.value = v; fire(e); }); if (spec.step) spec.step(); },
    lock(k, on) { const e = el(k); if (!e) return; e.disabled = !!on; e.setAttribute('aria-disabled', on ? 'true' : 'false'); e.closest('label')?.classList.toggle('locked', !!on); },
    reset() { Object.keys(params).forEach((k) => adapter.lock(k, false)); if (spec.reset) spec.reset(); if (spec.step) spec.step(); },
    pause() { if (spec.pause) spec.pause(); }, resume() { if (spec.resume) spec.resume(); },
  };
  window.simAdapter = adapter;
  return adapter;
};
