/* Embeds a lesson simulation. Loaded after p5 and before <id>-sim.js, it wraps window.p5 so that a sketch
   written for a fixed 600×400 canvas:
   - is resized to the width of its container and drawn with p.scale(), so text stays crisp on a phone
     (the sketch keeps drawing in 600×400 coordinates and never handles resizing itself),
   - pauses when it is scrolled out of view and resumes when it comes back (battery, and 80 bouncing
     particles need not run under the exercises),
   - runs at a low frame rate when the reader prefers reduced motion,
   - uses the page's own font inside the canvas.
   Tests run at 1280 px, where the container is wider than 600 px, so the canvas keeps its native size there. */
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
