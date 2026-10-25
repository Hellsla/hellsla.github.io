/* Embeds a lesson simulation. Loaded after p5 and before <id>-sim.js, it wraps window.p5 so that a sketch
   written for a fixed 600×400 canvas:
   - is resized to the width of its container and drawn with p.scale(), so text stays crisp on a phone
     (the sketch keeps drawing in 600×400 coordinates and never handles resizing itself),
   - pauses when it is scrolled out of view and resumes when it comes back (battery, and 80 bouncing
     particles need not run under the exercises),
   - runs at a low frame rate when the reader prefers reduced motion,
   - uses the page's own font inside the canvas.
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

  class Embedded extends Base {
    constructor(sketch, node) {
      super((p) => {
        sketch(p);
        const setup = p.setup, draw = p.draw;
        let s = 1;
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
        if (draw) p.draw = () => { p.push(); p.scale(s); draw(); p.pop(); };
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
