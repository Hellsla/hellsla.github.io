// fy8-4 Valo ja elektroni aaltoina ja hiukkasina: a double-slit experiment with single quanta (photons or electrons).
// The source sends one quantum at a time. Its probability wave (faint rings) spreads from the source, through the open
// slits, to the screen, where the quantum is detected at one random point. The point is drawn from the model's
// probability distribution on the screen: x = -12 ... 12 mm in 480 bins of 0,05 mm with weight
//   both slits open, path not measured:    cos²(π x / 2,0 mm) · sinc²(π x / 10 mm)   (fringes 2,0 mm apart)
//   one slit, or the path measured:        sinc²(π x / 10 mm)                        (no fringes)
// Photons and electrons share the same scale on purpose, so the patterns can be compared. Every hit draws four
// Park–Miller numbers (bin, place in the bin, height in the strip, slit); every reset (a change of particles, slits or
// path measurement, or Tyhjennä) clears the screen and reseeds with 12345, so a run is reproducible
// (lessons/FY8/fy8-4/lesson-answers.py replays it). The counting interval x0 ± 0,2 mm counts n of the N hits.
// The canvas shows the apparatus seen from above (the beam goes down), the screen seen from the front (the hits) and a
// histogram of the hits in 0,5 mm bins with the model's expected counts as a dashed curve. Every canvas text goes
// through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const XMIN = -12, XMAX = 12, BW = 0.05, NB = 480, FRINGE = 2.0, ENV = 10, M = 2147483647, SEED = 12345, NMAX = 20000;
  const HALF = 0.2, TF = 1.2;                                            // counting half-width (mm); flight time of one quantum (s, simulated)
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203];
  const HOTC = [201, 42, 42], HOTL = [242, 166, 156], COLDC = [25, 113, 194], COLDL = [208, 230, 251];
  const GOODC = [43, 138, 62], GOODL = [178, 242, 187], LAMP = [255, 192, 120], STEEL = [196, 204, 212], STEEL2 = [138, 150, 163];
  const WIDE = { H: 400, gx0: 64, gx1: 560, ySrc: 30, yPlate: 98, yScreen: 168, s0: 182, s1: 258, h0: 280, h1: 346, tickY: 368, titleY: 390, slitDx: 34 };
  const NARROW = { H: 600, gx0: 92, gx1: 560, ySrc: 50, yPlate: 132, yScreen: 228, s0: 248, s1: 344, h0: 392, h1: 494, tickY: 530, titleY: 572, slitDx: 40 };
  let G = WIDE, narrow = false, sk = 1, fh = 13, labels = [];
  let btn, btnAdd, btnClear, selP, selS, selR, selSpeed, slX, lX, readout, pg = null, pgKey = '';
  let seed = SEED, fine = new Array(NB).fill(0), hits = [], q = null, running = false, flash = null, dirty = true;
  let C = [], W = 1, wts = [];

  const centre = (i) => XMIN + BW * (i + 0.5);
  const rnd = () => { seed = (seed * 16807) % M; return seed / M; };
  const both = () => selS.value() === 'molemmat' && selR.value() === 'ei';
  function inten(x, b) {
    const u = Math.PI * x / ENV, env = x === 0 ? 1 : Math.pow(Math.sin(u) / u, 2);
    return b ? Math.pow(Math.cos(Math.PI * x / FRINGE), 2) * env : env;
  }
  function weights() {                                                   // cumulative weights of the 480 bins, in order
    const b = both(); C = []; wts = []; let s = 0;
    for (let i = 0; i < NB; i++) { const w = inten(centre(i), b); wts.push(w); s += w; C.push(s); }
    W = s;
  }
  function draw1() {                                                     // one quantum: where it lands, and through which slit the lamp clicks
    const r1 = rnd(), r2 = rnd(), r3 = rnd(), r4 = rnd(), t = r1 * W;
    let i = 0; while (C[i] <= t && i < NB - 1) i++;
    const s = selS.value(), slit = s === 'vasen' ? -1 : s === 'oikea' ? 1 : (r4 < 0.5 ? -1 : 1);
    return { i, dx: (r2 - 0.5) * BW, yy: r3, slit };
  }
  function register(h) { if (hits.length >= NMAX) return; hits.push(h); fine[h.i]++; dirty = true; }
  function resetScreen() {
    seed = SEED; fine = new Array(NB).fill(0); hits = []; q = null; running = false; flash = null; dirty = true; weights();
  }
  function addMany(k) {
    if (q) { register(q.h); q = null; }
    for (let j = 0; j < k && hits.length < NMAX; j++) register(draw1());
  }
  const inWin = (i, x0) => Math.abs(centre(i) - x0) < HALF;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; });
    btnAdd = p.createButton(__('lisaa')).parent(controls);
    btnAdd.elt.addEventListener('click', () => addMany(1000));
    btnClear = p.createButton(__('tyhjenna')).parent(controls);
    btnClear.elt.addEventListener('click', resetScreen);
    const mk = (key, opts, def) => {
      const l = p.createElement('label').parent(controls); p.createSpan(__(key)).parent(l); const s = p.createSelect().parent(l);
      for (const [k, v] of opts) s.option(__(k), v);
      s.selected(def); s.elt.addEventListener('change', resetScreen); return s;
    };
    selP = mk('hiukkaset', [['fotonit', 'fotoni'], ['elektronit', 'elektroni']], 'fotoni');
    selS = mk('raot', [['vasen', 'vasen'], ['molemmat', 'molemmat'], ['oikea', 'oikea']], 'molemmat');
    selR = mk('reitti', [['ei', 'ei'], ['kylla', 'kylla']], 'ei');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '4'); selSpeed.selected('1');
    const lx = p.createElement('label').parent(controls); lX = p.createSpan('').parent(lx); slX = p.createSlider(-10, 10, 1, 0.5).parent(lx);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    resetScreen();
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { hiukkanen: { input: selP.elt, unit: '' }, raot: { input: selS.elt, unit: '' }, reitti: { input: selR.elt, unit: '' }, x0: { input: slX.elt, unit: 'mm' } },
      reset: () => { selP.selected('fotoni'); selS.selected('molemmat'); selR.selected('ei'); slX.value(1); resetScreen(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    if (running && hits.length < NMAX) {
      if (!q) q = { h: draw1(), ph: 0 };
      q.ph += dt / TF;
      if (q.ph >= 1) { register(q.h); flash = { x: centre(q.h.i) + q.h.dx, a: 1 }; q = null; }
    } else if (hits.length >= NMAX) running = false;
    if (flash) { flash.a -= dt * 1.5; if (flash.a <= 0) flash = null; }
    const x0 = Number(slX.value()), N = hits.length;
    let n = 0, pw = 0;
    for (let i = 0; i < NB; i++) if (inWin(i, x0)) { n += fine[i]; pw += wts[i]; }
    pw = pw / W * 100;
    const osuus = N ? n / N * 100 : 0;
    lX.html(__('vali', { x: tx(x0, 1) }));
    const bt = running ? __('pysayta') : __('kaynnista');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    btnAdd.elt.disabled = N >= NMAX;
    readout.html(__('lukemat', { N: String(N), n: String(n), o: tx(osuus, 1), x: tx(x0, 1) }));
    window.simState = { hiukkanen: selP.value(), raot: selS.value(), reitti: selR.value(), x0, N, n, osuus, pw, running,
      phase: q ? q.ph : 0, slit: q ? q.h.slit : 0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state
    labels = [];
    p.background(255);
    apparatus();
    screenFace(x0);
    histogram(x0, N);
    window.simState.labels = labels;
  };

  const X = (x) => G.gx0 + (x - XMIN) / (XMAX - XMIN) * (G.gx1 - G.gx0);
  const col = () => (selP.value() === 'fotoni' ? HOTC : COLDC);
  const colL = () => (selP.value() === 'fotoni' ? HOTL : COLDL);

  // --- the apparatus from above: source, slit plate with its path lamps, the screen edge-on, the probability wave ---
  function apparatus() {
    const { ySrc, yPlate, yScreen, slitDx } = G, xc = X(0), c = col();
    grect(0, 0, 600, yScreen + 8 * sk, [[246, 241, 230], [255, 255, 255]]);
    // the wave of the quantum in flight
    if (q) {
      const ctx = p.drawingContext; p.noFill();
      const rings = (cx, cy, r, y0, y1) => {
        ctx.save(); ctx.beginPath(); ctx.rect(0, y0, 600, y1 - y0); ctx.clip();
        for (let j = 0; j < 4; j++) {
          const rr = r - j * 11 * sk; if (rr <= 2) continue;
          p.stroke(c[0], c[1], c[2], 150 - j * 32); p.strokeWeight(2 * sk); p.circle(cx, cy, 2 * rr);
        }
        ctx.restore();
      };
      const sp = 0.42;
      if (q.ph < sp) rings(xc, ySrc, q.ph / sp * (yPlate - ySrc + 10 * sk), ySrc, yPlate);
      else {
        const r = (q.ph - sp) / (1 - sp) * (yScreen - yPlate) * 1.25;
        const open = both() ? [-1, 1] : [q.h.slit];
        for (const s of open) rings(xc + s * slitDx, yPlate, r, yPlate, yScreen);
      }
    }
    // the source
    if (selP.value() === 'fotoni') {
      p.fill(...STEEL); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(xc - 34 * sk, ySrc - 22 * sk, 68 * sk, 26 * sk, 4 * sk);
      p.noStroke(); p.fill(...HOTC); p.rect(xc - 6 * sk, ySrc + 2 * sk, 12 * sk, 5 * sk, 2);
    } else {
      p.fill(...STEEL2); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(xc - 22 * sk, ySrc - 24 * sk, 44 * sk, 24 * sk, 3 * sk);
      p.fill(...STEEL); p.triangle(xc - 14 * sk, ySrc, xc + 14 * sk, ySrc, xc, ySrc + 9 * sk);
    }
    if (q && q.ph < 0.08) { p.noStroke(); p.fill(c[0], c[1], c[2], 200 * (1 - q.ph / 0.08)); p.circle(xc, ySrc + 8 * sk, 14 * sk); }
    lab(__(selP.value() === 'fotoni' ? 'lbl_lahde_f' : 'lbl_lahde_e'), xc + 44 * sk, ySrc - 2 * sk, 'l', INKC);
    // the slit plate: two gaps; a closed slit is covered by a shutter
    const pl = xc - 150, pr = xc + 150, gw = 9 * sk, th = 8 * sk;
    p.noStroke(); p.fill(...STEEL2);
    p.rect(pl, yPlate - th / 2, xc - slitDx - gw / 2 - pl, th);
    p.rect(xc - slitDx + gw / 2, yPlate - th / 2, 2 * slitDx - gw, th);
    p.rect(xc + slitDx + gw / 2, yPlate - th / 2, pr - xc - slitDx - gw / 2, th);
    p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.noFill();
    p.rect(pl, yPlate - th / 2, pr - pl, th);
    for (const s of [-1, 1]) {
      const closed = (selS.value() === 'vasen' && s === 1) || (selS.value() === 'oikea' && s === -1);
      const gx = xc + s * slitDx;
      if (closed) { p.fill(...INKC); p.noStroke(); p.rect(gx - gw / 2 - 2, yPlate - th / 2 - 3 * sk, gw + 4, th + 6 * sk, 2); }
      else { p.fill(255); p.noStroke(); p.rect(gx - gw / 2, yPlate - th / 2, gw, th); }
      if (selR.value() === 'kylla') {                                    // the path lamps beside the slits
        const lit = q && q.ph >= 0.42 && q.h.slit === s;
        p.fill(...(lit ? LAMP : [255, 255, 255])); p.stroke(...INKC); p.strokeWeight(1.5 * sk);
        p.circle(gx + s * 16 * sk, yPlate - 14 * sk, 11 * sk);
      }
    }
    lab(__('lbl_raot'), pr + 8 * sk, yPlate + fh * 0.36, 'l', INKC);
    // the screen edge-on
    p.stroke(...INKC); p.strokeWeight(4 * sk); p.line(G.gx0, yScreen, G.gx1, yScreen);
    lab(__('lbl_varjostin'), G.gx1, yScreen - 8 * sk, 'r', INKC);
    if (flash) { p.noStroke(); p.fill(c[0], c[1], c[2], 255 * flash.a); p.circle(X(flash.x), yScreen, 16 * sk); }
  }

  // --- the screen from the front: every hit as a dot, kept in an off-screen buffer ---
  function screenFace(x0) {
    const { s0, s1 } = G, key = G.H + ':' + selP.value();
    if (!pg || pgKey !== key) { if (pg) pg.remove(); pg = p.createGraphics(600, G.H); pg.pixelDensity(2); pgKey = key; dirty = true; pg.__n = 0; }
    if (dirty) {
      if (hits.length < pg.__n || pg.__n === 0) { pg.clear(); pg.__n = 0; }
      const ctx = pg.drawingContext, c = col(), r = narrow ? 2 : 1.2;
      ctx.fillStyle = `rgb(${c.join(',')})`;
      for (let j = pg.__n; j < hits.length; j++) {
        const h = hits[j];
        ctx.fillRect(X(centre(h.i) + h.dx) - r, s0 + 4 + h.yy * (s1 - s0 - 8) - r, 2 * r, 2 * r);
      }
      pg.__n = hits.length; dirty = false;
    }
    p.fill(255); p.stroke(...RULEC); p.strokeWeight(1.5); p.rect(G.gx0, s0, G.gx1 - G.gx0, s1 - s0);
    band(x0, s0, s1);
    p.image(pg, 0, 0, 600, G.H);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(G.gx0, s0, G.gx1 - G.gx0, s1 - s0);
  }
  function band(x0, y0, y1) {                                            // the counting interval x0 ± 0,2 mm
    p.noStroke(); p.fill(GOODL[0], GOODL[1], GOODL[2], 150); p.rect(X(x0 - HALF), y0, X(x0 + HALF) - X(x0 - HALF), y1 - y0);
    p.stroke(...GOODC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([4 * sk, 3 * sk]);
    p.line(X(x0 - HALF), y0, X(x0 - HALF), y1); p.line(X(x0 + HALF), y0, X(x0 + HALF), y1); p.drawingContext.setLineDash([]);
  }

  // --- the histogram of the hits (0,5 mm bins) and the model's expected counts ---
  function histogram(x0, N) {
    const { h0, h1, gx0, gx1, tickY, titleY } = G;
    const bins = new Array(48).fill(0), exp = new Array(48).fill(0);
    for (let i = 0; i < NB; i++) { bins[Math.floor(i / 10)] += fine[i]; exp[Math.floor(i / 10)] += N * wts[i] / W; }
    const top = Math.max(1, ...bins, ...exp), step = nice(top), ymax = Math.ceil(top / step) * step;
    const Y = (v) => h1 - v / ymax * (h1 - h0);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let v = step; v <= ymax + 1e-9; v += step) p.line(gx0, Y(v), gx1, Y(v));
    band(x0, h0, h1);
    const bw = (gx1 - gx0) / 48;
    p.fill(...colL()); p.stroke(...col()); p.strokeWeight(1);
    for (let b = 0; b < 48; b++) if (bins[b] > 0) p.rect(gx0 + b * bw + 1, Y(bins[b]), bw - 2, h1 - Y(bins[b]));
    if (N > 0) {                                                          // the model's expectation, dashed
      p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(2 * sk); p.drawingContext.setLineDash([6 * sk, 4 * sk]); p.beginShape();
      for (let b = 0; b < 48; b++) { p.vertex(gx0 + b * bw, Y(exp[b])); p.vertex(gx0 + (b + 1) * bw, Y(exp[b])); }
      p.endShape(); p.drawingContext.setLineDash([]);
    }
    // axes
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(gx0, h1, gx1 + 12 * sk, h1); p.line(gx0, h1, gx0, h0 - 8 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 24 * sk, h1, gx1 + 10 * sk, h1 - 6 * sk, gx1 + 10 * sk, h1 + 6 * sk);
    p.triangle(gx0, h0 - 20 * sk, gx0 - 6 * sk, h0 - 6 * sk, gx0 + 6 * sk, h0 - 6 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (const v of [-10, -5, 0, 5, 10]) { p.line(X(v), h1, X(v), h1 + 6 * sk); lab('$' + (v < 0 ? '-' : '') + Math.abs(v) + '$', X(v), tickY, 'c', INKC); }
    if (N > 0) for (let v = step; v <= ymax + 1e-9; v += step) { p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(gx0 - 6 * sk, Y(v), gx0, Y(v)); lab('$' + Math.round(v) + '$', gx0 - 9 * sk, Y(v) + fh * 0.36, 'r', INKC); }
    lab(__('lbl_osumia'), 2, h0 - (narrow ? 26 : 16) * sk, 'l', INKC);
    lab('$x\\,(\\text{mm})$', 594, titleY, 'r', INKC);
  }
  function nice(v) { const e = Math.pow(10, Math.floor(Math.log10(v))), m = v / e; return (m <= 2 ? 1 : m <= 5 ? 2 : 5) * e; }   // a gridline step: 1, 2 or 5 times a power of ten

  function lab(s, x, y, align, colr) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(colr || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  function grect(x, y, w, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, w, h); c.restore();
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
