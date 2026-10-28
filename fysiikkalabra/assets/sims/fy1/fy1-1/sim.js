// fy1-1 Maailmankaikkeuden mittasuhteet: a zoom from the Planck length to the observable universe, in the manner of "Scale of the Universe".
// Model: the canvas shows a view W = 10^L metres wide (560 canvas px across; L is continuous). An object of size d is drawn
// d / W · 560 px wide, so every picture is to scale for the current L. Every object between about 1/2000 and about 3 times the view
// is on screen at once, side by side on the ground line in size order: a larger one is cropped by the canvas (its limb is a big arc),
// one under 4 px is a dot with a leader line to its label. Objects fade in and out smoothly as the view slides past their size.
// All sizes are rounded orders of magnitude (see OBJ). Controls: ±1 power of ten buttons (animated), a log slider, drag / wheel / keys
// on the canvas, the map at the bottom, an auto-zoom with the speed select (hidas · normaali · nopea = 0,5 · 1 · 2 powers of ten per second).
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const LMIN = -34, LMAX = 27.5, VIEW = 560, GAP = 20, CAP = 340;
  const CATS = { q: [112, 72, 232], b: [43, 138, 62], h: [232, 118, 28], p: [38, 110, 214], c: [214, 160, 0] };
  // size m (m), LaTeX value, extent ext (m, defaults to m: orbits are drawn as diameters), layout width bw · S, dimension bracket dim
  const OBJ = [
    { id: 'planck', m: 1.6e-35, lat: '1{,}6\\cdot10^{-35}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'quark', m: 1.0e-18, lat: '{<}10^{-18}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'proton', m: 1.7e-15, lat: '1{,}7\\cdot10^{-15}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'henuc', m: 3.4e-15, lat: '3{,}4\\cdot10^{-15}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'pbnuc', m: 1.4e-14, lat: '1{,}4\\cdot10^{-14}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'gamma', m: 1.0e-12, lat: '1{,}0\\cdot10^{-12}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'heatom', m: 6.2e-11, lat: '6{,}2\\cdot10^{-11}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'atom', m: 1.1e-10, lat: '1{,}1\\cdot10^{-10}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'water', m: 2.8e-10, lat: '2{,}8\\cdot10^{-10}\\,\\text{m}', bw: 1, dim: 'w', cat: 'q' },
    { id: 'dna', m: 2.0e-9, lat: '2{,}0\\cdot10^{-9}\\,\\text{m}', bw: 1, dim: 'w', cat: 'b' },
    { id: 'virus', m: 1.0e-7, lat: '1{,}0\\cdot10^{-7}\\,\\text{m}', bw: 1, dim: 'w', cat: 'b' },
    { id: 'rbc', m: 7.5e-6, lat: '7{,}5\\cdot10^{-6}\\,\\text{m}', bw: 1, dim: 'w', cat: 'b' },
    { id: 'hair', m: 7.0e-5, lat: '7{,}0\\cdot10^{-5}\\,\\text{m}', bw: 6, dim: 'h', cat: 'b' },
    { id: 'ant', m: 5.0e-3, lat: '5{,}0\\cdot10^{-3}\\,\\text{m}', bw: 1, dim: 'w', cat: 'h' },
    { id: 'coin', m: 2.3e-2, lat: '2{,}3\\cdot10^{-2}\\,\\text{m}', bw: 1, dim: 'w', cat: 'h' },
    { id: 'ball', m: 2.2e-1, lat: '2{,}2\\cdot10^{-1}\\,\\text{m}', bw: 1, dim: 'w', cat: 'h' },
    { id: 'human', m: 1.7, lat: '1{,}7\\,\\text{m}', bw: 0.42, dim: 'h', cat: 'h' },
    { id: 'whale', m: 3.0e1, lat: '3{,}0\\cdot10^{1}\\,\\text{m}', bw: 1, dim: 'w', cat: 'h' },
    { id: 'building', m: 8.3e2, lat: '8{,}3\\cdot10^{2}\\,\\text{m}', bw: 0.2, dim: 'h', cat: 'h' },
    { id: 'everest', m: 8.8e3, lat: '8{,}8\\cdot10^{3}\\,\\text{m}', bw: 1.8, dim: 'h', cat: 'h' },
    { id: 'nstar', m: 2.4e4, lat: '2{,}4\\cdot10^{4}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'space', m: 1.0e5, lat: '1{,}0\\cdot10^{5}\\,\\text{m}', bw: 0.3, dim: 'h', cat: 'h' },
    { id: 'moon', m: 3.5e6, lat: '3{,}5\\cdot10^{6}\\,\\text{m}', bw: 1, dim: 'w', cat: 'p' },
    { id: 'earth', m: 1.27e7, lat: '1{,}27\\cdot10^{7}\\,\\text{m}', bw: 1, dim: 'w', cat: 'p' },
    { id: 'jupiter', m: 1.4e8, lat: '1{,}4\\cdot10^{8}\\,\\text{m}', bw: 1, dim: 'w', cat: 'p' },
    { id: 'sun', m: 1.39e9, lat: '1{,}39\\cdot10^{9}\\,\\text{m}', bw: 1, dim: 'w', cat: 'p' },
    { id: 'bh', m: 2.5e10, lat: '2{,}5\\cdot10^{10}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'au', m: 1.50e11, ext: 3.0e11, lat: '1{,}5\\cdot10^{11}\\,\\text{m}', bw: 1, dim: 'r', cat: 'p' },
    { id: 'saturn', m: 1.43e12, ext: 2.86e12, lat: '1{,}43\\cdot10^{12}\\,\\text{m}', bw: 1, dim: 'r', cat: 'p' },
    { id: 'neptune', m: 4.5e12, ext: 9.0e12, lat: '4{,}5\\cdot10^{12}\\,\\text{m}', bw: 1, dim: 'r', cat: 'p' },
    { id: 'helio', m: 1.8e13, ext: 3.6e13, lat: '1{,}8\\cdot10^{13}\\,\\text{m}', bw: 1, dim: 'r', cat: 'p' },
    { id: 'ly', m: 9.46e15, lat: '9{,}46\\cdot10^{15}\\,\\text{m}', bw: 1, dim: 'none', cat: 'c' },
    { id: 'oort', m: 1.5e16, ext: 3.0e16, lat: '1{,}5\\cdot10^{16}\\,\\text{m}', bw: 1, dim: 'r', cat: 'c' },
    { id: 'proxima', m: 4.0e16, lat: '4{,}0\\cdot10^{16}\\,\\text{m}', bw: 1, dim: 'none', cat: 'c', lane: 46 },
    { id: 'orion', m: 2.3e17, lat: '2{,}3\\cdot10^{17}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'arm', m: 3.3e19, lat: '3{,}3\\cdot10^{19}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'lmc', m: 1.3e20, lat: '1{,}3\\cdot10^{20}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'milky', m: 9.5e20, lat: '9{,}5\\cdot10^{20}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'andromeda', m: 2.1e21, lat: '2{,}1\\cdot10^{21}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'group', m: 9.5e22, lat: '9{,}5\\cdot10^{22}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'virgo', m: 1.0e24, lat: '1{,}0\\cdot10^{24}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'laniakea', m: 4.7e24, lat: '4{,}7\\cdot10^{24}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
    { id: 'universe', m: 8.8e26, lat: '8{,}8\\cdot10^{26}\\,\\text{m}', bw: 1, dim: 'w', cat: 'c' },
  ];
  OBJ.forEach((o) => { o.ext = o.ext || o.m; o.logExt = Math.log10(o.ext); o.logM = Math.log10(o.m); });
  const MAPX0 = 24, MAPX1 = 576, MAPL0 = -36, MAPL1 = 28;
  const mapX = (l) => MAPX0 + (l - MAPL0) / (MAPL1 - MAPL0) * (MAPX1 - MAPX0);
  const mapL = (x) => MAPL0 + (x - MAPX0) / (MAPX1 - MAPX0) * (MAPL1 - MAPL0);
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
  const mix = (a, b, t) => a.map((v, i) => v + (b[i] - v) * t);
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');                       // Finnish decimal comma inside LaTeX
  // how much of an object is shown: it fades in as its picture grows past a fraction of a pixel, and out as it passes 3 views wide
  const fadeIn = (S) => smooth(0.25, 0.7, S), fadeOut = (R) => 1 - smooth(3.0, 4.0, R);

  // fixed pseudo-random pictures (galaxy stars, cosmic web, background stars): the same every frame
  let seed = 7;
  const rnd = () => { seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  const gauss = () => (rnd() + rnd() + rnd() + rnd() - 2) * 0.9;
  const GAL = [];
  for (let a = 0; a < 4; a++) for (let i = 0; i < 260; i++) {
    const t = i / 260, r = 0.1 + 0.9 * t, th = a * Math.PI / 2 + 3.0 * Math.log(r / 0.1) + gauss() * 0.16 / (0.3 + r);
    GAL.push([r * Math.cos(th) + gauss() * 0.025, r * Math.sin(th) + gauss() * 0.025, rnd() < 0.7 ? 0 : 1]);
  }
  for (let i = 0; i < 220; i++) GAL.push([gauss() * 0.11, gauss() * 0.11, 2]);
  const NODES = [];
  for (let k = 0; k < 46; k++) { const a = rnd() * 6.283, r = Math.sqrt(rnd()) * 0.9; for (let j = 0; j < 4; j++) NODES.push([r * Math.cos(a) + gauss() * 0.06, r * Math.sin(a) + gauss() * 0.06]); }
  const EDGES = [];
  NODES.forEach((a, i) => { let n = 0; NODES.forEach((b, j) => { if (j > i && n < 3 && Math.hypot(a[0] - b[0], a[1] - b[1]) < 0.2) { EDGES.push([i, j]); n++; } }); });
  const DUST = Array.from({ length: 26 }, () => [rnd() * 600, rnd() * 290, 12 + rnd() * 34, 0.05 + rnd() * 0.1]);
  const STARS = Array.from({ length: 70 }, () => [rnd() * 600, rnd() * 300, 0.5 + rnd() * 1.3, 0.3 + rnd() * 0.6]);
  const GRAN = Array.from({ length: 16 }, () => { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * 0.85; return [d * Math.cos(a), d * Math.sin(a), a]; });
  const COMET = Array.from({ length: 150 }, () => { const a = rnd() * 6.283, d = 0.18 + 0.8 * Math.sqrt(rnd()); return [d * Math.cos(a), d * Math.sin(a), 0.4 + rnd() * 0.6]; });
  const NEB = Array.from({ length: 9 }, (_, i) => [gauss() * 0.3, gauss() * 0.22, 0.28 + rnd() * 0.3, i % 3]);
  const NSTAR = Array.from({ length: 90 }, () => [gauss() * 0.55, gauss() * 0.4, 0.4 + rnd() * 0.6]);
  const ARM = Array.from({ length: 330 }, () => [gauss() * 0.85, gauss() * 0.16, rnd()]);
  const GROUP = Array.from({ length: 22 }, () => { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * 0.8; return [d * Math.cos(a), d * Math.sin(a), 0.012 + rnd() * 0.02]; });
  const CLUSTER = Array.from({ length: 24 }, () => { const a = rnd() * 6.283, d = Math.sqrt(rnd()) * 0.8; return [d * Math.cos(a), d * Math.sin(a), 0.02 + rnd() * 0.05]; });

  let btn, bIn, bOut, sl, lSl, selDir, selSp, readout, cv;
  let L = 1, tgt = null, running = false, k = 1, labels = [], geo = {};

  // --- state helpers ---
  const setL = (v) => { L = clamp(v, LMIN, LMAX); tgt = null; sl.value(L); };
  const goTo = (v) => { running = false; tgt = clamp(v, LMIN, LMAX); };                // an animated step: the picture glides there
  const mainObj = () => { let best = 0, bd = 1e9; OBJ.forEach((o, i) => { const d = Math.abs(o.logExt - L - Math.log10(150 / VIEW)); if (d < bd) { bd = d; best = i; } }); return best; };
  const Lfmt = (x) => { const r = Math.round(x * 10) / 10; return Number.isInteger(r) ? String(r) : tx(r, 1); };

  p.setup = () => {
    cv = p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => {
      tgt = null;
      if (running) { running = false; return; }
      const dir = Number(selDir.value());
      if (dir > 0 && L >= LMAX - 0.05) setL(LMIN); else if (dir < 0 && L <= LMIN + 0.05) setL(LMAX);   // replay from the other end
      running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', () => reset());
    bIn = p.createButton('').parent(controls); bIn.html(__('lahenna'));
    bIn.elt.addEventListener('click', () => goTo(Math.ceil((tgt === null ? L : tgt) - 1e-9) - 1));
    bOut = p.createButton('').parent(controls); bOut.html(__('loitonna'));
    bOut.elt.addEventListener('click', () => goTo(Math.floor((tgt === null ? L : tgt) + 1e-9) + 1));
    const lt = p.createElement('label').parent(controls); lSl = p.createSpan('').parent(lt);
    sl = p.createSlider(LMIN, LMAX, L, 0.1).parent(lt);
    const scrub = () => { running = false; tgt = null; L = clamp(Number(sl.value()), LMIN, LMAX); };
    sl.elt.addEventListener('input', scrub); sl.elt.addEventListener('change', scrub);
    const ld = p.createElement('label').parent(controls); p.createSpan(__('suunta')).parent(ld); selDir = p.createSelect().parent(ld);
    selDir.option(__('suunta_ulos'), '1'); selDir.option(__('suunta_sisaan'), '-1');
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                    // pace only: L advances by simulated time dt · speed
    p.createP(__('kartta_ohje')).parent('sim-root').class('note');
    p.textFont('Arial');
    // direct manipulation: drag the picture, drag along the map, wheel and keys once the canvas has the focus
    cv.elt.tabIndex = 0; cv.elt.style.touchAction = 'pan-y'; cv.elt.style.cursor = 'grab';
    cv.elt.setAttribute('role', 'img'); cv.elt.setAttribute('aria-label', __('kuva_alt'));
    let drag = null;
    const pt = (e) => { const r = cv.elt.getBoundingClientRect(); return [(e.clientX - r.left) / r.width * 600, (e.clientY - r.top) / r.height * 400]; };
    cv.elt.addEventListener('pointerdown', (e) => {
      const [x, y] = pt(e); cv.elt.focus({ preventScroll: true }); running = false; tgt = null;
      if (y >= geo.mapTop) { drag = { mode: 'map' }; setL(mapL(x)); } else drag = { mode: 'pan', x0: x, L0: L };
      try { cv.elt.setPointerCapture(e.pointerId); } catch (err) { /* synthetic events */ }
    });
    cv.elt.addEventListener('pointermove', (e) => { if (!drag) return; const [x] = pt(e); setL(drag.mode === 'map' ? mapL(x) : drag.L0 - (x - drag.x0) / 60); });
    const up = () => { drag = null; };
    cv.elt.addEventListener('pointerup', up); cv.elt.addEventListener('pointercancel', up);
    cv.elt.addEventListener('wheel', (e) => { if (document.activeElement !== cv.elt) return; e.preventDefault(); running = false; setL(L + Math.sign(e.deltaY) * 0.25); }, { passive: false });
    cv.elt.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowUp' || e.key === '+' || e.key === '=') { e.preventDefault(); goTo(Math.ceil((tgt === null ? L : tgt) - 1e-9) - 1); }
      else if (e.key === 'ArrowDown' || e.key === '-') { e.preventDefault(); goTo(Math.floor((tgt === null ? L : tgt) + 1e-9) + 1); }
    });
    sl.value(L);
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { L: { input: sl.elt, unit: '' } },
      reset: () => reset(),
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };
  function reset() { running = false; tgt = null; selDir.selected('1'); selSp.selected('1'); setL(1); }

  p.draw = () => {
    const speed = Number(selSp.value()), dir = Number(selDir.value()), dt = Math.min(p.deltaTime, 100) / 1000;
    if (running) {
      L += dir * speed * dt;
      if (L >= LMAX) { L = LMAX; running = false; } else if (L <= LMIN) { L = LMIN; running = false; }
      sl.value(L);
    } else if (tgt !== null) {                                              // glide one power of ten: ease out, then land exactly
      L += (tgt - L) * (1 - Math.exp(-dt * 9)) + Math.sign(tgt - L) * dt * 0.5;
      if (Math.abs(tgt - L) < 0.006 || (L - tgt) * Math.sign(tgt - L) > 0) { L = tgt; tgt = null; }
      sl.value(L);
    }
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    lSl.html(__('leveys', { L: Lfmt(L) }));
    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(13);
    const W = Math.pow(10, L), mi = mainObj(), M = OBJ[mi];
    // every object with its size on screen S (px), the fade a, and the true-size ratio R to the view
    const items = [];
    OBJ.forEach((o) => { const S = o.ext / W * VIEW, a = fadeIn(S) * fadeOut(o.ext / W); if (a > 0.01) items.push({ o, S, a, w: Math.min(S * o.bw, 4000) }); });
    const vis = items.filter((it) => it.a >= 0.5);
    const kk = Math.floor(L + 1e-9), barPx = VIEW * Math.pow(10, kk - L);
    // vertical layout from the bottom up (heights follow the label size, so a phone keeps its spacing)
    const TB = 398 - 0.32 * fh, mapY = TB - 1.09 * fh - 8, ySb = mapY - 16, ySbL = ySb - 4 - 0.32 * fh;
    const vb = ySbL - 1.09 * fh - 4 - 0.32 * fh, nb = vb - 1.43 * fh - 2, yb = nb - 0.9 * fh - 14;
    geo = { mapTop: mapY - 16, yb };
    readout.html(__('rivi_leveys', { L: Lfmt(L) }) + '<br>' + __('rivi_kohde', { nimi: __('o_' + M.id), lat: M.lat }) + '<br>' +
      (vis.length ? __('rivi_nakyvissa', { n: vis.length, nimet: vis.map((it) => `$\\text{${__('o_' + it.o.id)}}$`).join(', ') }) : __('rivi_tyhja')));
    window.simState = { L, logW: L, W, tavoite: tgt === null ? L : tgt, kohde: mi, kohdeLog: M.logM, kohdeId: M.id, kohdeExp: Math.round(M.logM), nVis: vis.length, nakyvat: vis.map((it) => it.o.id).join(','),
      palkkiK: kk, palkkiPx: barPx, running, dir, speed, labels: null };
    labels = [];
    scene(ts, fh, items, { TB, mapY, ySb, ySbL, vb, nb, yb, kk, barPx });
    window.simState.labels = labels;
  };

  // --- scene: background, objects to scale side by side on the ground, their labels, the scale bar and the map ---
  function scene(ts, fh, items, g) {
    const c = p.drawingContext, f = smooth(-5.6, -4.2, L) * (1 - smooth(4.4, 5.8, L));     // 1 = daylight, 0 = dark (atoms, space)
    const top = mix([8, 12, 30], [190, 220, 248], f), bot = mix([26, 32, 66], [236, 246, 255], f), ink = f > 0.5 ? [28, 36, 50] : [236, 241, 252];
    c.save(); c.fillStyle = lg(0, 0, 0, 400, [[0, `rgb(${top.map(Math.round)})`], [1, `rgb(${bot.map(Math.round)})`]]); c.fillRect(0, 0, 600, 400); c.restore();
    if (f < 0.9) {
      c.save();
      if (L > 5) STARS.forEach(([x, y, r, a]) => { if (y < g.yb - 4) { c.globalAlpha = a * (1 - f); c.fillStyle = '#fff'; c.beginPath(); c.arc(x, y, r, 0, 6.283); c.fill(); } });
      else DUST.forEach(([x, y, r, a]) => { disc(x, y * g.yb / 300, r, rg(x, y * g.yb / 300, 0, x, y * g.yb / 300, r, [[0, `rgba(150,190,255,${a})`], [1, 'rgba(150,190,255,0)']])); });
      c.restore();
    }
    // layout along the ground: smallest on the left; a slot is at most CAP wide, a wider object starts at its slot and runs on to the right (cropped)
    const slot = items.map((it) => Math.min(it.w, CAP));
    let adv = items.map((it, i) => slot[i] + GAP * it.a), total = adv.reduce((s, v) => s + v, 0) - (items.length ? GAP * items[items.length - 1].a : 0);
    const room = 556, sc = total > room ? room / total : 1;
    let x = Math.max(22, (600 - Math.min(total, room)) / 2);
    items.forEach((it, i) => {
      const e = x, wide = it.w > CAP;
      it.x = wide ? e + it.w / 2 : e + it.w / 2 * 1;           // centre of the picture
      it.x0 = it.x - it.w / 2; it.x1 = it.x + it.w / 2;
      if (it.o.dim === 'w' || it.o.dim === 'r' || it.o.dim === 'none') { it.x0 = it.x - it.S / 2; it.x1 = it.x + it.S / 2; }
      x += adv[i] * sc;
    });
    // draw the largest first so that smaller objects stand in front of the bigger ones
    items.slice().reverse().forEach((it) => {
      const dotA = 1 - smooth(3, 6, it.S), picA = smooth(2, 5, it.S);
      c.save(); c.globalAlpha = it.a * picA; if (picA > 0.01) DRAW[it.o.id](it.x, g.yb - (it.o.lane || 0), it.S, f); c.restore();
      if (dotA > 0.01) { c.save(); c.globalAlpha = it.a * dotA; dot(it, g.yb, f); c.restore(); }
    });
    items.forEach((it) => dimension(it, g.yb, f));
    // the ground line, drawn over the feet
    c.save(); c.strokeStyle = `rgba(${mix([150, 160, 200], [90, 100, 112], f).map(Math.round)},0.8)`; c.lineWidth = 2; c.beginPath(); c.moveTo(14, g.yb + 1); c.lineTo(586, g.yb + 1); c.stroke(); c.restore();
    // labels under the ground line: centred under the visible part of the object, pushed apart, joined to it by a leader line where needed
    p.textSize(fh);
    let cands = items.map((it) => ({ it, la: fadeIn(it.S * 1.6) * fadeOut(it.o.ext / Math.pow(10, L)) })).filter((cl) => cl.la > 0.03);
    const wid = (cl) => Math.max(p.textWidth(`$\\text{${__('o_' + cl.it.o.id)}}$`), p.textWidth(`$${cl.it.o.lat}$`)) + 10;
    // no room even at 0,8 times: the labels of objects under 1 px (the smallest first) give way
    while (cands.length > 1 && 0.8 * cands.reduce((s, cl) => s + wid(cl), 0) > 584) {
      const sm = cands.reduce((a, b) => (a.it.S < b.it.S ? a : b));
      if (sm.it.S >= 1) break;
      cands = cands.filter((cl) => cl !== sm);
    }
    const cols = cands.map((cl) => {
      const it = cl.it, nm = `$\\text{${__('o_' + it.o.id)}}$`, vl = `$${it.o.lat}$`, w = Math.max(p.textWidth(nm), p.textWidth(vl)) + 6;
      const ax = clamp((clamp(it.x0, 12, 588) + clamp(it.x1, 12, 588)) / 2, 12, 588);
      return { nm, vl, w, ax, la: cl.la, it };
    }).sort((a, b) => a.ax - b.ax);
    // crowded: the labels shrink together (down to 0,8 times) so that all fit side by side
    const need = cols.reduce((s, cl) => s + cl.w + 4, 0), fs = clamp(584 / Math.max(need, 1), 0.8, 1), lfh = fh * fs;
    cols.forEach((cl) => { cl.w *= fs; cl.cx = clamp(cl.ax, 8 + cl.w / 2, 592 - cl.w / 2); });
    for (let i = 1; i < cols.length; i++) cols[i].cx = Math.max(cols[i].cx, cols[i - 1].cx + (cols[i - 1].w + cols[i].w) / 2 + 4);
    for (let i = cols.length - 1; i >= 0; i--) { const lim = i === cols.length - 1 ? 592 - cols[i].w / 2 : cols[i + 1].cx - (cols[i + 1].w + cols[i].w) / 2 - 4; cols[i].cx = Math.min(cols[i].cx, lim); }
    cols.forEach((cl) => {
      const bracket = cl.it.S >= 14 && cl.it.o.dim !== 'none' && cl.it.o.dim !== 'r' && cl.it.o.dim !== 'h' && cl.it.x0 > 4 && cl.it.x1 < 596;
      if (Math.abs(cl.cx - cl.ax) > 3 || cl.it.S < 30) {
        c.save(); c.globalAlpha = cl.la * 0.7; c.strokeStyle = `rgb(${ink.map(Math.round)})`; c.lineWidth = 1; c.beginPath();
        c.moveTo(cl.ax, g.yb + (bracket ? 11 : 5)); c.lineTo(cl.ax, g.yb + 9 + (bracket ? 3 : 0)); c.lineTo(cl.cx, g.nb - 0.75 * fh - 3); c.stroke(); c.restore();
      }
      lab(cl.nm, cl.cx, g.nb, 'c', lfh, ink, cl.la); lab(cl.vl, cl.cx, g.vb, 'c', lfh, ink, cl.la);
    });
    // scale bar: this length is one power of ten of metres
    c.save(); c.strokeStyle = `rgb(${ink.map(Math.round)})`; c.lineWidth = 2.5; c.beginPath(); c.moveTo(20, g.ySb); c.lineTo(20 + g.barPx, g.ySb); c.stroke();
    c.lineWidth = 2; c.beginPath(); for (const bx of [20, 20 + g.barPx]) { c.moveTo(bx, g.ySb - 5); c.lineTo(bx, g.ySb + 5); } c.stroke(); c.restore();
    lab(g.kk === 0 ? '$1\\,\\text{m}$' : `$10^{${g.kk}}\\,\\text{m}$`, 20, g.ySbL, 'l', fh, ink);
    map(fh, g, f, ink);
  }

  // an object smaller than a few pixels: a glowing dot in its category colour, standing on the ground
  function dot(it, yb, f) {
    const cc = CATS[it.o.cat], r = Math.max(it.S / 2, 1.7), cy = yb - (it.o.lane || 0) - r - 1;
    disc(it.x, cy, r * 2.4, rg(it.x, cy, 0, it.x, cy, r * 2.4, [[0, `rgba(${cc},0.45)`], [1, `rgba(${cc},0)`]]));
    disc(it.x, cy, r, `rgb(${cc})`, f > 0.5 ? 'rgba(255,255,255,0.9)' : 'rgba(255,255,255,0.7)', 0.8);
  }

  // the map: log axis of every size from 10^-36 to 10^28 m, a dot per object, the band of sizes that fit the view now
  function map(fh, g, f, ink) {
    const c = p.drawingContext, y = g.mapY, col = `rgb(${ink.map(Math.round)})`;
    c.save();
    c.fillStyle = 'rgba(255,214,102,0.34)'; c.strokeStyle = 'rgba(232,118,28,0.95)'; c.lineWidth = 1.5;
    const bx0 = mapX(L - 3.2), bx1 = mapX(L + 0.45);
    c.beginPath(); c.roundRect(bx0, y - 13, bx1 - bx0, 26, 4); c.fill(); c.stroke();
    c.strokeStyle = col; c.lineWidth = 2; c.beginPath(); c.moveTo(MAPX0, y); c.lineTo(MAPX1, y); c.stroke();
    c.lineWidth = 1.2;
    for (let e = -35; e <= 25; e += 5) { c.beginPath(); c.moveTo(mapX(e), y); c.lineTo(mapX(e), y + (e % 10 === 0 ? 7 : 4)); c.stroke(); }
    const W = Math.pow(10, L);
    OBJ.forEach((o) => {
      const on = fadeIn(o.ext / W * VIEW) * fadeOut(o.ext / W) >= 0.5, cc = CATS[o.cat];
      c.beginPath(); c.arc(mapX(o.logExt), y - 6, on ? 4.2 : 2.6, 0, 6.283); c.fillStyle = `rgb(${cc})`; c.fill();
      c.lineWidth = on ? 1.8 : 1; c.strokeStyle = on ? '#fff' : 'rgba(255,255,255,0.7)'; c.stroke();
    });
    c.fillStyle = 'rgb(232,118,28)'; c.beginPath(); const lx = mapX(L); c.moveTo(lx, y + 1); c.lineTo(lx - 5, y + 11); c.lineTo(lx + 5, y + 11); c.closePath(); c.fill();
    c.restore();
    const step = k > 1.4 ? 20 : 10;
    for (let e = -30; e <= 20; e += 10) if (e % step === 0) lab(e === 0 ? '$1$' : `$10^{${e}}$`, mapX(e), g.TB, 'c', fh, ink);
  }

  // measuring bracket of an object: orange, horizontal under it (width) or vertical beside it (height / thickness)
  function dimension(it, yb, f) {
    const o = it.o; if (it.S < 14 || o.dim === 'none' || o.dim === 'r') return;
    const c = p.drawingContext; c.save(); c.globalAlpha = it.a * smooth(14, 24, it.S) * (1 - smooth(480, 640, it.S)); c.strokeStyle = 'rgb(232,118,28)'; c.fillStyle = 'rgb(232,118,28)'; c.lineWidth = 2;
    if (o.dim === 'w') {
      const x0 = it.x - it.S / 2, x1 = it.x + it.S / 2, y = yb + 6;
      if (x0 > 4 && x1 < 596) { c.beginPath(); c.moveTo(x0, y); c.lineTo(x1, y); c.moveTo(x0, y - 4); c.lineTo(x0, y + 4); c.moveTo(x1, y - 4); c.lineTo(x1, y + 4); c.stroke(); }
    } else if (o.dim === 'h') {
      const x = it.x - it.w / 2 - 8, y0 = yb - it.S, y1 = yb;
      if (x > 4 && y0 > 2) { c.beginPath(); c.moveTo(x, y0); c.lineTo(x, y1); c.moveTo(x - 4, y0); c.lineTo(x + 4, y0); c.moveTo(x - 4, y1); c.lineTo(x + 4, y1); c.stroke(); }
    }
    c.restore();
  }

  // --- gradients and shapes on the raw canvas, saved and restored so that p5's own state is untouched ---
  const ctx = () => p.drawingContext;
  const lg = (x0, y0, x1, y1, st) => { const g = ctx().createLinearGradient(x0, y0, x1, y1); st.forEach(([o, col]) => g.addColorStop(o, col)); return g; };
  const rg = (x0, y0, r0, x1, y1, r1, st) => { const g = ctx().createRadialGradient(x0, y0, r0, x1, y1, r1); st.forEach(([o, col]) => g.addColorStop(o, col)); return g; };
  const lw = (S, a = 0.012, lo = 0.8, hi = 2.2) => clamp(S * a, lo, hi);
  function disc(x, y, r, fill, stroke, w) {
    const c = ctx(); c.beginPath(); c.arc(x, y, Math.max(r, 0.01), 0, 6.283185);
    if (fill) { c.fillStyle = fill; c.fill(); } if (stroke) { c.lineWidth = w || 1; c.strokeStyle = stroke; c.stroke(); }
  }
  function ell(x, y, rx, ry, rot, fill, stroke, w) {
    const c = ctx(); c.beginPath(); c.ellipse(x, y, Math.max(rx, 0.01), Math.max(ry, 0.01), rot || 0, 0, 6.283185);
    if (fill) { c.fillStyle = fill; c.fill(); } if (stroke) { c.lineWidth = w || 1; c.strokeStyle = stroke; c.stroke(); }
  }
  function poly(pts, fill, stroke, w, close = true) {
    const c = ctx(); c.beginPath(); pts.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); if (close) c.closePath();
    if (fill) { c.fillStyle = fill; c.fill(); } if (stroke) { c.lineWidth = w || 1; c.lineJoin = 'round'; c.strokeStyle = stroke; c.stroke(); }
  }
  function rrect(x, y, w, h, r, fill, stroke, sw) {
    const c = ctx(); c.beginPath(); c.roundRect(x, y, w, h, Math.min(r, w / 2, h / 2));
    if (fill) { c.fillStyle = fill; c.fill(); } if (stroke) { c.lineWidth = sw || 1; c.strokeStyle = stroke; c.stroke(); }
  }
  function line(x0, y0, x1, y1, col, w, cap) { const c = ctx(); c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y1); c.lineWidth = w; c.strokeStyle = col; c.lineCap = cap || 'round'; c.stroke(); }
  function wave(x0, y0, x1, y1, amp, n, col, w) {
    const c = ctx(), d = Math.hypot(x1 - x0, y1 - y0) || 1, nx = -(y1 - y0) / d, ny = (x1 - x0) / d; c.beginPath();
    for (let i = 0; i <= 40; i++) { const t = i / 40, a = Math.sin(t * n * 6.283) * amp; c.lineTo(x0 + (x1 - x0) * t + nx * a, y0 + (y1 - y0) * t + ny * a); }
    c.lineWidth = w; c.strokeStyle = col; c.lineCap = 'round'; c.stroke();
  }

  // an atom: a soft electron cloud of colour `col` with `n` electrons; the nucleus is drawn larger than its true size
  function atomPic(cx, yb, S, col, n) {
    const r = S / 2, cy = yb - r, rgb = col.join(',');
    disc(cx, cy, r, rg(cx, cy, 0, cx, cy, r, [[0, `rgba(${rgb},0.95)`], [0.35, `rgba(${rgb},0.6)`], [0.75, `rgba(${rgb},0.25)`], [1, `rgba(${rgb},0)`]]));
    const c = ctx(); c.save(); c.setLineDash([5, 5]); disc(cx, cy, r * 0.97, null, 'rgba(235,245,255,0.7)', 1.3); c.restore();
    for (let i = 0; i < n; i++) { const an = 0.9 + i * 3.1416, x = cx + r * 0.5 * Math.cos(an), y = cy + r * 0.5 * Math.sin(an); disc(x, y, Math.max(1.6, S * 0.02), '#fff', `rgba(${rgb},1)`, 1); }
    disc(cx, cy, Math.max(2.4, S * 0.016), '#e03131', '#fff', 1);
  }
  // a nucleus: N nucleons (Z protons red, the rest neutrons blue-grey) packed in a disc of diameter S
  function nucleusPic(cx, yb, S, N, Z) {
    const R = S / 2, cy = yb - R, nr = R * 0.8 / Math.sqrt(N);
    disc(cx, cy, R * 1.12, rg(cx, cy, R * 0.8, cx, cy, R * 1.12, [[0, 'rgba(255,160,80,0.35)'], [1, 'rgba(255,160,80,0)']]));
    for (let i = N - 1; i >= 0; i--) {
      const rr = (R - nr) * Math.sqrt((i + 0.5) / N), an = i * 2.39996, x = cx + rr * Math.cos(an), y = cy + rr * Math.sin(an), pr = (i * 0.6180339) % 1 < Z / N;
      disc(x, y, nr, rg(x - 0.3 * nr, y - 0.35 * nr, 0.05 * nr, x, y, nr, pr ? [[0, '#ffd8d8'], [0.5, '#e03131'], [1, '#8f1d1d']] : [[0, '#e7edf5'], [0.5, '#7a8ba3'], [1, '#3d4a5e']]), 'rgba(0,0,0,0.35)', Math.max(0.3, nr * 0.06));
    }
  }
  // a galaxy of diameter S seen at a slant (flatness `fl`, tilt `rot`); the Sun marks our own galaxy
  function galaxyPic(cx, yb, S, fl, rot, sun) {
    const R = S / 2, ry = fl * S, cy = yb - ry - 2, c = ctx(), q = fl * 2;
    c.save(); c.translate(cx, cy); c.rotate(rot); c.scale(1, q);
    disc(0, 0, R, rg(0, 0, 0, 0, 0, R, [[0, 'rgba(255,230,150,0.85)'], [0.18, 'rgba(255,200,120,0.45)'], [0.55, 'rgba(120,160,255,0.2)'], [1, 'rgba(120,160,255,0)']]));
    const s = Math.max(1.2, S / 130);
    GAL.forEach(([u, v, t]) => { c.fillStyle = t === 2 ? 'rgba(255,230,160,0.9)' : t === 1 ? 'rgba(200,215,255,0.95)' : 'rgba(255,255,255,0.9)'; c.fillRect(u * R, v * R, s, s / q * 0.6); });
    c.restore();
    if (sun) { const an = 2.3, sx = cx + 0.6 * R * Math.cos(an), sy = cy + 0.6 * R * Math.sin(an) * q;
      disc(sx, sy, Math.max(2, S * 0.012), '#ffd43b', '#fff', 1.2); disc(sx, sy, Math.max(4, S * 0.03), null, 'rgba(255,255,255,0.8)', 1.2); }
  }
  // a patch of the cosmic web: filaments, bright cluster knots, a dark disc; `flow` adds streamlines converging on one point (a supercluster)
  function webPic(cx, yb, S, tint, flow) {
    const R = S / 2, cy = yb - R, c = ctx();
    disc(cx, cy, R, rg(cx, cy, 0, cx, cy, R, [[0, '#241a5c'], [0.7, '#130e36'], [1, '#080b20']]), 'rgba(150,170,255,0.7)', lw(S, 0.01, 1, 2));
    c.save(); c.beginPath(); c.arc(cx, cy, R * 0.99, 0, 6.283); c.clip();
    c.strokeStyle = tint; c.lineWidth = Math.max(0.7, S * 0.004); c.beginPath();
    EDGES.forEach(([i, j]) => { c.moveTo(cx + NODES[i][0] * R, cy + NODES[i][1] * R); c.lineTo(cx + NODES[j][0] * R, cy + NODES[j][1] * R); }); c.stroke();
    CLUSTER.forEach(([u, v, s]) => { const x = cx + u * R, y = cy + v * R, r = Math.max(1.5, s * R); disc(x, y, r * 2.2, rg(x, y, 0, x, y, r * 2.2, [[0, 'rgba(255,235,190,0.85)'], [1, 'rgba(255,235,190,0)']])); });
    if (flow) {
      const tx0 = cx + 0.25 * R, ty0 = cy - 0.1 * R; c.strokeStyle = 'rgba(255,220,160,0.8)'; c.lineWidth = Math.max(1, S * 0.004);
      for (let i = 0; i < 14; i++) { const an = i / 14 * 6.283, x0 = cx + 0.9 * R * Math.cos(an), y0 = cy + 0.9 * R * Math.sin(an); c.beginPath(); c.moveTo(x0, y0); c.quadraticCurveTo((x0 + tx0) / 2 + 0.12 * R * Math.sin(an), (y0 + ty0) / 2 - 0.12 * R * Math.cos(an), tx0 + (x0 - tx0) * 0.2, ty0 + (y0 - ty0) * 0.2); c.stroke(); }
      disc(tx0, ty0, Math.max(3, R * 0.05), rg(tx0, ty0, 0, tx0, ty0, Math.max(3, R * 0.05), [[0, '#fff'], [1, 'rgba(255,200,120,0)']]));
    }
    c.restore();
    disc(cx - 0.35 * R, cy + 0.3 * R, Math.max(1.8, S * 0.012), '#ffd43b', '#fff', 1.2);
  }

  // --- the pictures: each is drawn with its measured size S (px) standing on y = yb, centred on cx ---
  const DRAW = {
    planck(cx, yb, S, f) {                              // a symbolic cell of a "grid of space": nothing is known about the real structure
      const c = ctx(), x0 = cx - S / 2, y0 = yb - S;
      c.save(); c.strokeStyle = 'rgba(190,170,255,0.26)'; c.lineWidth = 1; c.beginPath();
      for (let x = x0 - Math.ceil(x0 / S) * S; x < 600; x += S) { c.moveTo(x, 0); c.lineTo(x, yb); }
      for (let y = y0 - Math.ceil(y0 / S) * S; y < yb; y += S) { c.moveTo(0, y); c.lineTo(600, y); }
      c.stroke(); c.restore();
      c.save(); c.shadowColor = 'rgba(177,151,252,0.9)'; c.shadowBlur = Math.min(24, S * 0.4);
      rrect(x0, y0, S, S, S * 0.12, lg(x0, y0, x0 + S, yb, [[0, '#d0bfff'], [0.5, '#9775fa'], [1, '#5f3dc4']]), '#e5dbff', lw(S, 0.02, 1, 2.5)); c.restore();
      if (S > 20) { c.save(); c.strokeStyle = 'rgba(255,255,255,0.85)'; c.lineWidth = lw(S, 0.012, 1, 2); c.beginPath(); const q = S * 0.22; c.moveTo(cx - q, yb - S / 2); c.lineTo(cx + q, yb - S / 2); c.moveTo(cx, yb - S / 2 - q); c.lineTo(cx, yb - S / 2 + q); c.stroke(); c.restore(); }
    },
    proton(cx, yb, S) {
      const r = S / 2, cy = yb - r, w = lw(S);
      disc(cx, cy, r * 1.25, rg(cx, cy, r * 0.9, cx, cy, r * 1.25, [[0, 'rgba(255,160,80,0.45)'], [1, 'rgba(255,160,80,0)']]));
      disc(cx, cy, r, rg(cx - 0.35 * r, cy - 0.4 * r, 0.05 * r, cx, cy, r, [[0, '#fff0dc'], [0.5, '#ffa94d'], [1, '#d9480f']]), '#a63a0b', w);
      const Q = [[-90, '#e03131'], [30, '#2f9e44'], [150, '#1c7ed6']].map(([a, col]) => [cx + 0.5 * r * Math.cos(a * Math.PI / 180), cy + 0.5 * r * Math.sin(a * Math.PI / 180), col]);
      [[0, 1], [1, 2], [2, 0]].forEach(([i, j]) => wave(Q[i][0], Q[i][1], Q[j][0], Q[j][1], r * 0.06, 4, 'rgba(255,255,255,0.8)', Math.max(0.8, r * 0.035)));
      Q.forEach(([x, y, col]) => disc(x, y, r * 0.19, rg(x - 0.05 * r, y - 0.06 * r, 0.01 * r, x, y, 0.19 * r, [[0, '#fff'], [0.35, col], [1, col]]), 'rgba(0,0,0,0.35)', 1));
    },
    atom(cx, yb, S) { atomPic(cx, yb, S, [51, 154, 240], 1); },       // electron cloud (probability), nucleus drawn larger than true size
    heatom(cx, yb, S) { atomPic(cx, yb, S, [64, 192, 87], 2); },
    water(cx, yb, S) {                                   // a water molecule: one oxygen atom and two hydrogen atoms at 104,5°; the atoms drawn as balls
      const rO = S * 0.3, rH = S * 0.2, cy = yb - S * 0.44, d = S * 0.3, a = 52.25 * Math.PI / 180;
      for (const sg of [-1, 1]) { const x = cx + sg * d * Math.sin(a) * 1.25, y = cy + d * Math.cos(a) * 1.25;
        disc(x, y, rH, rg(x - 0.3 * rH, y - 0.35 * rH, 0.05 * rH, x, y, rH, [[0, '#ffffff'], [0.6, '#dee2e6'], [1, '#868e96']]), '#495057', lw(S, 0.008, 0.6, 1.6)); }
      disc(cx, cy, rO, rg(cx - 0.3 * rO, cy - 0.35 * rO, 0.05 * rO, cx, cy, rO, [[0, '#ffc9c9'], [0.55, '#e03131'], [1, '#8f1d1d']]), '#7a1717', lw(S, 0.008, 0.6, 1.6));
    },
    dna(cx, yb, S) {                                     // double helix, width S; the pitch is 1,7 times the width
      const c = ctx(), H = S * 3.2, N = 120, pitch = S * 1.7, R = S * 0.42, wd = Math.max(1.6, S * 0.11);
      const pt = (t, ph) => [cx + R * Math.cos(t * H / pitch * 6.283 + ph), yb - t * H, Math.sin(t * H / pitch * 6.283 + ph)];
      const strand = (ph, col, front) => { c.lineWidth = wd; c.lineCap = 'round'; c.strokeStyle = col; for (let i = 0; i < N; i++) { const a = pt(i / N, ph), b = pt((i + 1) / N, ph); if ((a[2] > 0) === front) { c.beginPath(); c.moveTo(a[0], a[1]); c.lineTo(b[0], b[1]); c.stroke(); } } };
      c.save(); strand(0, '#1864ab', false); strand(Math.PI, '#a61e4d', false);
      for (let i = 1; i < 26; i++) { const t = i / 26, a = pt(t, 0), b = pt(t, Math.PI); const g = lg(a[0], a[1], b[0], b[1], [[0, '#74c0fc'], [0.5, '#fff'], [1, '#ffa8c4']]); line(a[0], a[1], b[0], b[1], g, Math.max(1, S * 0.06), 'butt'); }
      strand(0, '#339af0', true); strand(Math.PI, '#e64980', true); c.restore();
    },
    virus(cx, yb, S) {                                   // crown-shaped virus: body, RNA and spike proteins
      const r = S / 2, cy = yb - r, body = r * 0.68;
      for (let i = 0; i < 26; i++) { const a = i / 26 * 6.283, x0 = cx + body * 0.96 * Math.cos(a), y0 = cy + body * 0.96 * Math.sin(a), x1 = cx + r * 0.84 * Math.cos(a), y1 = cy + r * 0.84 * Math.sin(a);
        line(x0, y0, x1, y1, '#c92a2a', Math.max(1, r * 0.05)); disc(cx + r * 0.9 * Math.cos(a), cy + r * 0.9 * Math.sin(a), r * 0.1, rg(cx + r * 0.9 * Math.cos(a) - r * 0.02, cy + r * 0.9 * Math.sin(a) - r * 0.02, 0, cx + r * 0.9 * Math.cos(a), cy + r * 0.9 * Math.sin(a), r * 0.1, [[0, '#ff8787'], [1, '#c92a2a']])); }
      disc(cx, cy, body, rg(cx - 0.3 * body, cy - 0.35 * body, 0.05 * body, cx, cy, body, [[0, '#dee2e6'], [0.6, '#868e96'], [1, '#495057']]), '#343a40', lw(S));
      const c = ctx(); c.save(); c.beginPath(); c.arc(cx, cy, body * 0.94, 0, 6.283); c.clip();
      c.strokeStyle = 'rgba(255,224,102,0.9)'; c.lineWidth = Math.max(1, r * 0.06); c.lineCap = 'round'; c.beginPath();
      for (let i = 0; i <= 60; i++) { const t = i / 60, a = t * 14, rr = body * 0.6 * (0.4 + 0.6 * Math.abs(Math.sin(t * 5))); c.lineTo(cx + rr * Math.cos(a), cy + rr * Math.sin(a)); } c.stroke(); c.restore();
    },
    rbc(cx, yb, S) {                                     // red blood cell seen from above: thicker rim, thinner middle
      const r = S / 2, cy = yb - r;
      disc(cx, cy, r, rg(cx - 0.2 * r, cy - 0.25 * r, 0.1 * r, cx, cy, r, [[0, '#ff8787'], [0.55, '#e03131'], [1, '#8f1d1d']]), '#7a1717', lw(S));
      disc(cx, cy, r * 0.58, rg(cx, cy, 0, cx, cy, r * 0.58, [[0, 'rgba(120,10,20,0.55)'], [0.7, 'rgba(160,20,30,0.25)'], [1, 'rgba(255,200,200,0)']]));
      const c = ctx(); c.save(); c.strokeStyle = 'rgba(255,255,255,0.55)'; c.lineWidth = Math.max(1, r * 0.06); c.lineCap = 'round'; c.beginPath(); c.arc(cx, cy, r * 0.82, Math.PI * 1.1, Math.PI * 1.45); c.stroke(); c.restore();
    },
    hair(cx, yb, S) {                                    // a hair lying on the shelf, thickness S
      const w = S * 6, x0 = cx - w / 2, y0 = yb - S, c = ctx();
      rrect(x0, y0, w, S, S / 2, lg(0, y0, 0, yb, [[0, '#4a2f17'], [0.28, '#b07d45'], [0.55, '#8a5a2b'], [1, '#2f1c0d']]), '#2f1c0d', lw(S, 0.01, 0.8, 1.6));
      c.save(); c.beginPath(); c.roundRect(x0, y0, w, S, S / 2); c.clip(); c.strokeStyle = 'rgba(40,22,8,0.45)'; c.lineWidth = Math.max(0.8, S * 0.025); c.beginPath();
      for (let x = x0 + S * 0.3; x < x0 + w; x += S * 0.55) { c.moveTo(x, y0 + S * 0.1); c.lineTo(x + S * 0.3, yb - S * 0.1); } c.stroke(); c.restore();
      ell(x0 + w - S * 0.5, y0 + S / 2, S * 0.2, S * 0.4, 0, 'rgba(240,214,170,0.55)');
    },
    ant(cx, yb, S) {                                     // black garden ant, side view, facing left
      const X = (u) => cx - S / 2 + u * S, Y = (v) => yb + v * S, w = Math.max(1, S * 0.012), dark = '#1c1410';
      const legs = [[0.36, -0.22, 0.30, -0.46, 0.22, -0.0], [0.42, -0.22, 0.44, -0.5, 0.46, -0.0], [0.48, -0.22, 0.60, -0.44, 0.70, -0.0]];
      legs.forEach(([ax, ay, kx, ky, fx, fy]) => { line(X(ax - 0.03), Y(ay), X(kx - 0.03), Y(ky), 'rgba(40,30,25,0.55)', w * 0.9); line(X(kx - 0.03), Y(ky), X(fx - 0.03), Y(fy), 'rgba(40,30,25,0.55)', w * 0.9); });
      legs.forEach(([ax, ay, kx, ky, fx, fy]) => { line(X(ax), Y(ay), X(kx), Y(ky), dark, w * 1.2); line(X(kx), Y(ky), X(fx), Y(fy), dark, w * 1.2); });
      line(X(0.1), Y(-0.3), X(0.0), Y(-0.45), dark, w); line(X(0.0), Y(-0.45), X(-0.04), Y(-0.38), dark, w);
      const body = (x, y, rx, ry) => ell(X(x), Y(y), rx * S, ry * S, 0, lg(0, Y(y - ry), 0, Y(y + ry), [[0, '#5a4a40'], [0.35, '#2b2018'], [1, '#0f0b08']]), '#000', Math.max(0.6, S * 0.006));
      body(0.76, -0.27, 0.2, 0.14); body(0.45, -0.28, 0.12, 0.075); body(0.585, -0.26, 0.04, 0.035); body(0.15, -0.28, 0.1, 0.085);
      disc(X(0.12), Y(-0.3), Math.max(0.8, S * 0.018), '#f1f3f5');
    },
    human(cx, yb, S) {                                   // a generic standing person, height S
      const Y = (v) => yb - v * S, X = (u) => cx + u * S, c = ctx();
      ell(cx, yb, S * 0.16, S * 0.015, 0, 'rgba(0,0,0,0.18)');
      rrect(X(-0.115), Y(0.52), S * 0.108, S * 0.48, S * 0.04, lg(0, Y(0.52), 0, yb, [[0, '#4b5563'], [1, '#1f2937']]));
      rrect(X(0.007), Y(0.52), S * 0.108, S * 0.48, S * 0.04, lg(0, Y(0.52), 0, yb, [[0, '#4b5563'], [1, '#1f2937']]));
      ell(X(-0.07), Y(0.018), S * 0.07, S * 0.02, 0, '#111827'); ell(X(0.06), Y(0.018), S * 0.07, S * 0.02, 0, '#111827');
      rrect(X(-0.185), Y(0.82), S * 0.05, S * 0.34, S * 0.025, '#e8b99a'); rrect(X(0.135), Y(0.82), S * 0.05, S * 0.34, S * 0.025, '#e8b99a');
      rrect(X(-0.19), Y(0.84), S * 0.07, S * 0.14, S * 0.03, '#2563eb'); rrect(X(0.12), Y(0.84), S * 0.07, S * 0.14, S * 0.03, '#2563eb');
      rrect(X(-0.14), Y(0.84), S * 0.28, S * 0.36, S * 0.07, lg(X(-0.14), 0, X(0.14), 0, [[0, '#60a5fa'], [0.5, '#2563eb'], [1, '#1d4ed8']]));
      rrect(X(-0.02), Y(0.87), S * 0.04, S * 0.045, S * 0.015, '#d9a283');
      disc(cx, Y(0.935), S * 0.058, rg(cx - S * 0.02, Y(0.95), 0, cx, Y(0.935), S * 0.058, [[0, '#f5cfb3'], [1, '#d9a283']]));
      c.save(); c.beginPath(); c.arc(cx, Y(0.935), S * 0.06, Math.PI * 1.02, Math.PI * 2.0); c.closePath(); c.fillStyle = '#4a3322'; c.fill(); c.restore();
    },
    building(cx, yb, S) {                                // a generic super-tall tower: tapering tiers and a spire
      const Y = (v) => yb - v * S, X = (u) => cx + u * S;
      const tier = (hw, y0, y1) => rrect(X(-hw), Y(y1), 2 * hw * S, (y1 - y0) * S, S * 0.004, lg(X(-hw), 0, X(hw), 0, [[0, '#b8c9db'], [0.45, '#6f8cab'], [1, '#33506e']]), '#243b53', lw(S, 0.004, 0.8, 1.6));
      tier(0.1, 0, 0.12); tier(0.075, 0.1, 0.45); tier(0.055, 0.43, 0.65); tier(0.037, 0.63, 0.8); tier(0.022, 0.78, 0.9);
      poly([[X(-0.012), Y(0.9)], [X(0), Y(1)], [X(0.012), Y(0.9)]], '#8d99a6', '#3e4c59', 1);
      if (S > 120) { const c = ctx(); c.save(); c.strokeStyle = 'rgba(255,255,255,0.28)'; c.lineWidth = 1; c.beginPath(); for (let v = 0.02; v < 0.9; v += 0.02) { const hw = v < 0.12 ? 0.1 : v < 0.45 ? 0.075 : v < 0.65 ? 0.055 : v < 0.8 ? 0.037 : 0.022; c.moveTo(X(-hw), Y(v)); c.lineTo(X(hw), Y(v)); } c.stroke(); c.restore(); }
      disc(X(0), Y(1) , Math.max(1.2, S * 0.004), '#fa5252');
    },
    everest(cx, yb, S) {                                 // Mount Everest: 8,8 km above sea level; a sketch of the shape
      const X = (u) => cx + u * S, Y = (v) => yb - v * S;
      const mt = [[-0.9, 0], [-0.62, 0.3], [-0.4, 0.42], [-0.2, 0.7], [0, 1], [0.14, 0.82], [0.3, 0.68], [0.5, 0.42], [0.7, 0.28], [0.9, 0]].map(([u, v]) => [X(u), Y(v)]);
      poly(mt, lg(0, Y(1), 0, yb, [[0, '#cfd6de'], [0.45, '#8995a3'], [1, '#56616d']]), '#3e4a56', lw(S, 0.006, 1, 2));
      poly([[X(0), Y(1)], [X(0.14), Y(0.82)], [X(0.3), Y(0.68)], [X(0.5), Y(0.42)], [X(0.7), Y(0.28)], [X(0.9), Y(0)], [X(0.35), Y(0)], [X(0.16), Y(0.35)]], 'rgba(30,40,60,0.28)');
      poly([[X(0), Y(1)], [X(-0.08), Y(0.84)], [X(-0.05), Y(0.78)], [X(-0.14), Y(0.7)], [X(-0.2), Y(0.7)], [X(-0.12), Y(0.82)]], '#f8fbff');
      poly([[X(0), Y(1)], [X(0.14), Y(0.82)], [X(0.1), Y(0.76)], [X(0.04), Y(0.78)], [X(0.02), Y(0.7)], [X(-0.05), Y(0.78)], [X(-0.08), Y(0.84)]], '#e7f1fb');
      poly([[X(-0.4), Y(0.42)], [X(-0.34), Y(0.38)], [X(-0.28), Y(0.45)], [X(-0.2), Y(0.7)], [X(-0.3), Y(0.6)]], '#f1f6fb');
      line(X(0), Y(1), X(0.12), Y(0.4), 'rgba(40,50,64,0.35)', Math.max(0.8, S * 0.006)); line(X(-0.2), Y(0.7), X(-0.1), Y(0.3), 'rgba(40,50,64,0.3)', Math.max(0.8, S * 0.006));
    },
    earth(cx, yb, S) {
      const r = S / 2, cy = yb - r, c = ctx();
      disc(cx, cy, r * 1.06, rg(cx, cy, r * 0.97, cx, cy, r * 1.06, [[0, 'rgba(120,190,255,0.7)'], [1, 'rgba(120,190,255,0)']]));
      disc(cx, cy, r, rg(cx - 0.35 * r, cy - 0.4 * r, 0.05 * r, cx, cy, r, [[0, '#a5d8ff'], [0.5, '#2f74b5'], [1, '#0b2e63']]));
      c.save(); c.beginPath(); c.arc(cx, cy, r, 0, 6.283); c.clip();
      const land = (pts, col) => poly(pts.map(([u, v]) => [cx + u * r, cy + v * r]), col, 'rgba(20,80,30,0.5)', Math.max(0.6, r * 0.01));
      land([[-0.55, -0.45], [-0.3, -0.62], [-0.05, -0.5], [-0.12, -0.3], [-0.3, -0.2], [-0.45, -0.1], [-0.6, -0.25]], '#74d680');
      land([[-0.1, -0.35], [0.2, -0.55], [0.55, -0.4], [0.62, -0.1], [0.4, 0.0], [0.28, 0.2], [0.08, 0.05], [-0.02, -0.15]], '#82e08c');
      land([[-0.12, 0.0], [0.1, 0.1], [0.2, 0.4], [0.05, 0.7], [-0.1, 0.5], [-0.2, 0.2]], '#e2cc84');
      land([[-0.6, 0.15], [-0.4, 0.1], [-0.3, 0.4], [-0.38, 0.65], [-0.5, 0.45]], '#6fcf7a');
      ell(cx, cy - r * 1.0, r * 0.4, r * 0.1, 0, '#f1f8ff');
      [[-0.3, -0.05, 0.3], [0.3, -0.7, 0.25], [0.35, 0.4, 0.3], [-0.5, 0.5, 0.2]].forEach(([u, v, s]) => ell(cx + u * r, cy + v * r, s * r, s * r * 0.2, -0.3, 'rgba(255,255,255,0.7)'));
      disc(cx + 0.3 * r, cy + 0.3 * r, r * 1.15, rg(cx - 0.45 * r, cy - 0.5 * r, r * 0.6, cx + 0.3 * r, cy + 0.3 * r, r * 1.15, [[0, 'rgba(0,10,40,0)'], [1, 'rgba(0,10,40,0.42)']]));
      c.restore();
    },
    sun(cx, yb, S) {
      const r = S / 2, cy = yb - r;
      disc(cx, cy, r * 1.5, rg(cx, cy, r * 0.9, cx, cy, r * 1.5, [[0, 'rgba(255,190,60,0.55)'], [1, 'rgba(255,190,60,0)']]));
      disc(cx, cy, r, rg(cx - 0.25 * r, cy - 0.3 * r, 0.05 * r, cx, cy, r, [[0, '#fff9db'], [0.5, '#ffd43b'], [1, '#f08c00']]), '#e67700', lw(S));
      [[-0.3, 0.2, 0.12], [0.35, -0.25, 0.09], [0.1, 0.45, 0.07]].forEach(([u, v, s]) => ell(cx + u * r, cy + v * r, s * r, s * r * 0.8, 0.4, 'rgba(120,53,15,0.55)'));
      GRAN.forEach(([u, v, a]) => ell(cx + u * r, cy + v * r, r * 0.07, r * 0.045, a, 'rgba(255,255,255,0.18)'));
    },
    au(cx, yb, S, f) { orbitPicture(cx, yb, S, [1], 1, f); },
    bh(cx, yb, S, f) {                                   // the black hole at the centre of the Milky Way: S is the diameter of its event horizon (a boundary, not a surface)
      const r = S / 2, cy = yb - r, c = ctx();
      disc(cx, cy, r * 1.7, rg(cx, cy, r, cx, cy, r * 1.7, [[0, 'rgba(255,146,43,0.55)'], [0.4, 'rgba(255,192,120,0.22)'], [1, 'rgba(255,192,120,0)']]));
      disc(cx, cy, r, '#000000');
      c.save(); c.setLineDash([5, 4]); disc(cx, cy, r, null, f > 0.5 ? 'rgba(60,70,90,0.8)' : 'rgba(255,214,170,0.85)', 1.3); c.restore();
    },
    saturn(cx, yb, S, f) { orbitPicture(cx, yb, S, [0.387, 0.723, 1, 1.524, 5.203, 9.537], 9.537, f); },
    neptune(cx, yb, S, f) { orbitPicture(cx, yb, S, [0.387, 0.723, 1, 1.524, 5.203, 9.537, 19.19, 30.07], 30.07, f); },
    ly(cx, yb, S) {                                      // a beam of light, one year long
      const x0 = cx - S / 2, x1 = cx + S / 2, y = yb - 14, c = ctx();
      rrect(x0, y - 4, S, 8, 4, lg(x0, 0, x1, 0, [[0, 'rgba(255,212,59,0)'], [0.7, 'rgba(255,212,59,0.85)'], [1, '#fff9db']]));
      disc(x1, y, 7, rg(x1, y, 0, x1, y, 8, [[0, '#fff'], [0.5, 'rgba(255,240,150,0.9)'], [1, 'rgba(255,212,59,0)']]));
      c.save(); c.strokeStyle = '#ffd43b'; c.lineWidth = 2.5; c.beginPath(); [x0, x1].forEach((x) => { c.moveTo(x, y - 12); c.lineTo(x, y + 12); }); c.stroke(); c.restore();
    },
    proxima(cx, yb, S) {                                 // the Sun and its nearest neighbour star; stars drawn larger than true size
      const x0 = cx - S / 2, x1 = cx + S / 2, y = yb - 14 - 0, c = ctx();
      c.save(); c.setLineDash([7, 6]); line(x0, y, x1, y, 'rgba(255,255,255,0.65)', 1.6, 'butt'); c.restore();
      [[x0, '#fff3bf', '#ffa94d', 'rgba(255,190,60,0.55)', 6], [x1, '#ffc9c9', '#e03131', 'rgba(255,100,100,0.5)', 5]].forEach(([x, c0, c1, glow, r]) => {
        disc(x, y, r * 3, rg(x, y, 0, x, y, r * 3, [[0, glow], [1, 'rgba(255,200,100,0)']]));
        disc(x, y, r, rg(x - 1, y - 1, 0, x, y, r, [[0, '#fff'], [0.4, c0], [1, c1]]));
      });
    },
    milky(cx, yb, S) { galaxyPic(cx, yb, S, 0.21, 0, true); },           // spiral galaxy seen at a slant; the Sun sits in one arm
    andromeda(cx, yb, S) { galaxyPic(cx, yb, S, 0.14, -0.28, false); },
    universe(cx, yb, S) {                                // the observable universe with the cosmic web; we are in the middle
      const R = S / 2, cy = yb - R, c = ctx();
      disc(cx, cy, R, rg(cx, cy, 0, cx, cy, R, [[0, '#2b1f6b'], [0.7, '#150f3a'], [1, '#070a1c']]), 'rgba(150,170,255,0.85)', lw(S, 0.01, 1, 2));
      c.save(); c.beginPath(); c.arc(cx, cy, R * 0.99, 0, 6.283); c.clip(); c.strokeStyle = 'rgba(150,175,255,0.26)'; c.lineWidth = Math.max(0.6, S * 0.0025); c.beginPath();
      EDGES.forEach(([i, j]) => { c.moveTo(cx + NODES[i][0] * R, cy + NODES[i][1] * R); c.lineTo(cx + NODES[j][0] * R, cy + NODES[j][1] * R); }); c.stroke();
      c.fillStyle = 'rgba(255,240,210,0.9)'; NODES.forEach(([u, v]) => { const s = Math.max(1, S * 0.006); c.fillRect(cx + u * R - s / 2, cy + v * R - s / 2, s, s); }); c.restore();
      disc(cx, cy, Math.max(2, S * 0.012), '#fff', '#ffd43b', 1.5);
    },
    space(cx, yb, S) {                                   // a column of air up to the edge of space: sky blue below, black above
      const w = S * 0.3, x0 = cx - w / 2, c = ctx();
      rrect(x0, yb - S, w, S, 3, lg(0, yb - S, 0, yb, [[0, '#050818'], [0.35, '#1a3a7a'], [0.7, '#5b9bdc'], [1, '#bfe0ff']]), 'rgba(255,255,255,0.6)', 1.2);
      c.save(); c.setLineDash([5, 4]); line(x0 - w * 0.2, yb - S, x0 + w * 1.2, yb - S, 'rgba(255,255,255,0.9)', 1.5, 'butt'); c.restore();
      for (let i = 0; i < 6; i++) disc(x0 + w * (0.12 + 0.15 * i), yb - S * (0.94 - 0.04 * (i % 3)), Math.max(0.8, S * 0.006), '#fff');
    },
    lmc(cx, yb, S) { galaxyPic(cx, yb, S, 0.33, 0.5, false); },
    quark(cx, yb, S) {                                   // point-like: drawn as a small glowing ball
      const r = Math.max(S / 2, 0.5), cy = yb - r;
      disc(cx, cy, r * 1.6, rg(cx, cy, 0, cx, cy, r * 1.6, [[0, 'rgba(255,120,120,0.5)'], [1, 'rgba(255,120,120,0)']]));
      disc(cx, cy, r, rg(cx - 0.3 * r, cy - 0.3 * r, 0.02 * r, cx, cy, r, [[0, '#fff'], [0.4, '#ff6b6b'], [1, '#c92a2a']]));
    },
    henuc(cx, yb, S) { nucleusPic(cx, yb, S, 4, 2); },
    pbnuc(cx, yb, S) { nucleusPic(cx, yb, S, 208, 82); },
    gamma(cx, yb, S) {                                   // one wavelength of a gamma ray
      const a = S * 0.2, y = yb - S * 0.3, c = ctx(), w = Math.max(1.6, S * 0.035);
      c.save(); c.shadowColor = 'rgba(190,120,255,0.9)'; c.shadowBlur = Math.min(14, S * 0.15);
      c.beginPath(); for (let i = 0; i <= 60; i++) { const t = i / 60; c.lineTo(cx - S / 2 + S * t, y - Math.sin(t * 6.283) * a); }
      c.lineWidth = w; c.strokeStyle = '#9c36e8'; c.lineCap = 'round'; c.stroke(); c.restore();
      [-S / 2, S / 2].forEach((x) => line(cx + x, yb - S * 0.02, cx + x, y - a * 1.5, 'rgba(156,54,232,0.5)', 1, 'butt'));
    },
    coin(cx, yb, S) {                                    // a one-euro coin, face on: silver centre, gold ring
      const r = S / 2, cy = yb - r;
      disc(cx, cy, r, rg(cx - 0.3 * r, cy - 0.35 * r, 0.05 * r, cx, cy, r, [[0, '#ffe9a8'], [0.55, '#e0b040'], [1, '#9c7416']]), '#7a5a10', lw(S));
      disc(cx, cy, r * 0.62, rg(cx - 0.25 * r, cy - 0.3 * r, 0.05 * r, cx, cy, r * 0.62, [[0, '#f8f9fa'], [0.6, '#bcc3ca'], [1, '#8b939b']]), '#6b737b', lw(S, 0.008));
      const c = ctx(); c.save(); c.strokeStyle = 'rgba(122,90,16,0.55)'; c.lineWidth = Math.max(0.6, S * 0.006); c.beginPath();
      for (let i = 0; i < 12; i++) { const an = i / 12 * 6.283; c.moveTo(cx + r * 0.7 * Math.cos(an), cy + r * 0.7 * Math.sin(an)); c.lineTo(cx + r * 0.93 * Math.cos(an), cy + r * 0.93 * Math.sin(an)); } c.stroke(); c.restore();
    },
    ball(cx, yb, S) {                                    // a football: black pentagon patches on white
      const r = S / 2, cy = yb - r, c = ctx();
      ell(cx, yb, r * 0.8, r * 0.07, 0, 'rgba(0,0,0,0.16)');
      disc(cx, cy, r, rg(cx - 0.35 * r, cy - 0.4 * r, 0.05 * r, cx, cy, r, [[0, '#ffffff'], [0.7, '#e6e9ee'], [1, '#aeb6c1']]), '#3b4350', lw(S, 0.01));
      c.save(); c.beginPath(); c.arc(cx, cy, r, 0, 6.283); c.clip();
      const pent = (x, y, s, rot) => poly(Array.from({ length: 5 }, (_, i) => [x + s * Math.cos(rot + i * 1.2566), y + s * Math.sin(rot + i * 1.2566)]), '#1f2933', '#1f2933', 1);
      c.strokeStyle = 'rgba(31,41,51,0.7)'; c.lineWidth = Math.max(0.8, S * 0.012);
      pent(cx, cy, r * 0.3, -1.5708);
      for (let i = 0; i < 5; i++) { const an = -1.5708 + i * 1.2566 + 0.6283; c.beginPath(); c.moveTo(cx + r * 0.24 * Math.cos(an - 0.6283), cy + r * 0.24 * Math.sin(an - 0.6283)); c.lineTo(cx + r * 0.62 * Math.cos(an - 0.6283), cy + r * 0.62 * Math.sin(an - 0.6283)); c.stroke(); pent(cx + r * 0.98 * Math.cos(an - 0.6283), cy + r * 0.98 * Math.sin(an - 0.6283), r * 0.3, an + 1.5708); }
      disc(cx + 0.3 * r, cy + 0.3 * r, r * 1.15, rg(cx - 0.45 * r, cy - 0.5 * r, r * 0.6, cx + 0.3 * r, cy + 0.3 * r, r * 1.15, [[0, 'rgba(0,10,40,0)'], [1, 'rgba(0,10,40,0.28)']]));
      c.restore();
    },
    whale(cx, yb, S) {                                   // a blue whale in the sea, side view, facing left
      const X = (u) => cx - S / 2 + u * S, Y = (v) => yb - S * 0.02 - v * S, c = ctx(), top = [[0, 0.07], [0.1, 0.12], [0.3, 0.14], [0.55, 0.115], [0.8, 0.07], [0.93, 0.065]], bot = [[0.93, 0.045], [0.8, 0.035], [0.55, 0.0], [0.3, -0.005], [0.1, 0.015], [0, 0.04]];
      c.save(); c.beginPath(); top.forEach(([u, v], i) => (i ? c.lineTo(X(u), Y(v)) : c.moveTo(X(u), Y(v)))); c.lineTo(X(1.0), Y(0.1)); c.lineTo(X(0.985), Y(0.065)); c.lineTo(X(1.0), Y(0.02)); bot.forEach(([u, v]) => c.lineTo(X(u), Y(v))); c.closePath();
      c.fillStyle = lg(0, Y(0.14), 0, Y(0), [[0, '#6f8fa8'], [1, '#4a6a83']]); c.fill(); c.lineWidth = Math.max(0.8, S * 0.002); c.strokeStyle = '#2f4a5f'; c.stroke(); c.clip();
      c.strokeStyle = 'rgba(220,235,245,0.55)'; c.lineWidth = Math.max(0.8, S * 0.0025); c.beginPath(); for (let i = 0; i < 12; i++) { c.moveTo(X(0.08 + i * 0.012), Y(0.03)); c.lineTo(X(0.08 + i * 0.012 + 0.2), Y(0.03)); } c.stroke(); c.restore();
      poly([[X(0.3), Y(0.03)], [X(0.4), Y(-0.03)], [X(0.35), Y(0.01)]], '#4a6a83', '#2f4a5f', Math.max(0.8, S * 0.002));
      disc(X(0.045), Y(0.075), Math.max(0.8, S * 0.0035), '#10202c');
      const sea = lg(0, Y(0.06), 0, yb, [[0, 'rgba(70,150,225,0.55)'], [1, 'rgba(25,90,170,0.7)']]);
      c.save(); c.beginPath(); c.moveTo(X(-0.08), Y(0.06)); for (let i = 0; i <= 40; i++) c.lineTo(X(-0.08 + 1.16 * i / 40), Y(0.06) - Math.sin(i * 1.3) * S * 0.003);
      c.quadraticCurveTo(X(1.12), Y(0.0), X(1.06), yb); c.lineTo(X(-0.02), yb); c.quadraticCurveTo(X(-0.1), Y(0.0), X(-0.08), Y(0.06)); c.closePath(); c.fillStyle = sea; c.fill(); c.restore();
    },
    moon(cx, yb, S) {
      const r = S / 2, cy = yb - r, c = ctx();
      disc(cx, cy, r, rg(cx - 0.35 * r, cy - 0.4 * r, 0.05 * r, cx, cy, r, [[0, '#f1f3f5'], [0.55, '#adb5bd'], [1, '#5c6770']]), '#495057', lw(S));
      c.save(); c.beginPath(); c.arc(cx, cy, r, 0, 6.283); c.clip();
      [[-0.35, -0.3, 0.22], [0.2, -0.45, 0.14], [0.4, 0.1, 0.2], [-0.1, 0.35, 0.16], [-0.55, 0.2, 0.1], [0.05, -0.05, 0.08]].forEach(([u, v, s]) => { ell(cx + u * r, cy + v * r, s * r, s * r, 0, 'rgba(73,80,87,0.35)', 'rgba(255,255,255,0.25)', Math.max(0.6, r * 0.01)); });
      disc(cx + 0.3 * r, cy + 0.3 * r, r * 1.2, rg(cx - 0.4 * r, cy - 0.45 * r, r * 0.6, cx + 0.3 * r, cy + 0.3 * r, r * 1.2, [[0, 'rgba(0,0,20,0)'], [1, 'rgba(0,0,20,0.45)']]));
      c.restore();
    },
    jupiter(cx, yb, S) {
      const r = S / 2, cy = yb - r, c = ctx();
      c.save(); c.beginPath(); c.arc(cx, cy, r, 0, 6.283); c.clip();
      c.fillStyle = '#e6c9a0'; c.fillRect(cx - r, cy - r, S, S);
      [[-0.85, -0.65, '#c68b5a'], [-0.6, -0.45, '#f3dfbf'], [-0.45, -0.3, '#b9774a'], [-0.2, -0.05, '#f0d6b0'], [0.05, 0.2, '#c98f5e'], [0.25, 0.4, '#f3e2c4'], [0.45, 0.62, '#b9774a'], [0.7, 0.85, '#dcc096']].forEach(([a, b, col]) => { c.fillStyle = col; c.fillRect(cx - r, cy + a * r, S, (b - a) * r); });
      ell(cx + 0.28 * r, cy + 0.3 * r, 0.2 * r, 0.1 * r, 0, '#c8553d', '#e9a58f', Math.max(0.6, r * 0.01));
      disc(cx + 0.3 * r, cy + 0.3 * r, r * 1.2, rg(cx - 0.4 * r, cy - 0.45 * r, r * 0.55, cx + 0.3 * r, cy + 0.3 * r, r * 1.2, [[0, 'rgba(30,10,0,0)'], [1, 'rgba(30,10,0,0.5)']]));
      c.restore(); disc(cx, cy, r, null, '#8a5a30', lw(S));
    },
    helio(cx, yb, S, f) {                                // the bubble the solar wind blows into the interstellar gas; Neptune's orbit inside
      const R = S / 2, cy = yb - R;
      disc(cx, cy, R, rg(cx - 0.15 * R, cy, 0.1 * R, cx, cy, R, [[0, 'rgba(255,214,102,0.32)'], [0.8, 'rgba(255,170,80,0.2)'], [1, 'rgba(255,140,60,0.4)']]));
      const c = ctx(); c.save(); c.setLineDash([6, 5]); disc(cx, cy, R, null, 'rgba(232,118,28,0.95)', 2); disc(cx, cy, R * 0.25, null, f > 0.5 ? 'rgba(60,70,90,0.6)' : 'rgba(200,215,245,0.7)', 1.2); c.restore();
      disc(cx, cy, Math.max(3, S * 0.01), rg(cx, cy, 0, cx, cy, Math.max(3, S * 0.01), [[0, '#fff9db'], [1, '#f08c00']]), '#e67700', 1);
      radiusLine(cx, cy, R, -0.5);
    },
    nstar(cx, yb, S) {                                   // a neutron star: a city-sized ball of neutrons, hot and blue-white; faint beams of a pulsar
      const r = S / 2, cy = yb - r, c = ctx();
      c.save(); c.translate(cx, cy); c.rotate(-0.35);
      for (const sg of [-1, 1]) poly([[0, 0], [-r * 0.45, sg * r * 2.6], [r * 0.45, sg * r * 2.6]], lg(0, 0, 0, sg * r * 2.6, [[0, 'rgba(165,216,255,0.55)'], [1, 'rgba(165,216,255,0)']]));
      c.restore();
      disc(cx, cy, r * 1.35, rg(cx, cy, r * 0.9, cx, cy, r * 1.35, [[0, 'rgba(165,216,255,0.6)'], [1, 'rgba(165,216,255,0)']]));
      disc(cx, cy, r, rg(cx - 0.3 * r, cy - 0.35 * r, 0.05 * r, cx, cy, r, [[0, '#ffffff'], [0.5, '#d0ebff'], [1, '#4dabf7']]), '#1971c2', lw(S));
    },
    oort(cx, yb, S, f) {                                 // a shell of icy bodies; the planets' region is a speck in the middle
      const R = S / 2, cy = yb - R, c = ctx();
      disc(cx, cy, R, rg(cx, cy, 0, cx, cy, R, [[0, 'rgba(160,200,255,0.1)'], [0.7, 'rgba(160,200,255,0.2)'], [1, 'rgba(160,200,255,0.4)']]), 'rgba(140,180,240,0.8)', 1.6);
      c.save(); c.fillStyle = f > 0.5 ? 'rgba(40,60,110,0.85)' : 'rgba(225,238,255,0.9)'; const s = Math.max(1, S * 0.006);
      COMET.forEach(([u, v, a]) => { c.globalAlpha *= 1; c.fillRect(cx + u * R - s / 2, cy + v * R - s / 2, s * a, s * a); }); c.restore();
      disc(cx, cy, Math.max(2.5, S * 0.012), '#ffd43b', '#fff', 1);
      radiusLine(cx, cy, R, -0.5);
    },
    orion(cx, yb, S) {                                   // a glowing gas cloud where stars are born
      const R = S / 2, cy = yb - R * 0.8, c = ctx(), col = ['255,120,170', '120,160,255', '190,120,255'];
      c.save(); NEB.forEach(([u, v, s, t]) => { const x = cx + u * R * 1.6, y = cy + v * R * 1.6, r = s * R * 1.1; disc(x, y, r, rg(x, y, 0, x, y, r, [[0, `rgba(${col[t]},0.7)`], [0.6, `rgba(${col[t]},0.28)`], [1, `rgba(${col[t]},0)`]])); });
      NSTAR.forEach(([u, v, a]) => { const x = cx + u * R * 1.8, y = cy + v * R * 1.8; disc(x, y, Math.max(0.9, S * 0.006 * a), `rgba(255,255,255,${0.5 + a * 0.5})`); });
      [[-0.04, 0], [0.02, 0.03], [0.05, -0.03], [-0.02, 0.05]].forEach(([u, v]) => { const x = cx + u * R, y = cy + v * R; disc(x, y, Math.max(1.4, S * 0.012), rg(x, y, 0, x, y, Math.max(1.4, S * 0.012) * 3, [[0, '#fff'], [0.3, 'rgba(210,225,255,0.9)'], [1, 'rgba(210,225,255,0)']])); });
      c.restore();
    },
    arm(cx, yb, S) {                                     // the Orion arm seen from above: a band of stars and gas with the Sun inside
      const R = S / 2, cy = yb - 0.2 * S, c = ctx();
      c.save(); c.translate(cx, cy); c.rotate(-0.12);
      disc(0, 0, R, rg(0, 0, 0, 0, 0, R, [[0, 'rgba(200,215,255,0.5)'], [1, 'rgba(120,160,255,0)']]));
      c.restore();
      c.save(); c.translate(cx, cy); c.rotate(-0.12); c.scale(1, 0.4); disc(0, 0, R, rg(0, 0, 0, 0, 0, R, [[0, 'rgba(255,224,160,0.7)'], [0.5, 'rgba(180,170,255,0.3)'], [1, 'rgba(120,160,255,0)']]));
      const s = Math.max(1.2, S / 160); ARM.forEach(([u, v, t]) => { c.fillStyle = t < 0.3 ? 'rgba(255,230,160,0.9)' : 'rgba(225,235,255,0.9)'; c.fillRect(u * R, v * R / 0.4 * 0.9, s, s); }); c.restore();
      disc(cx, cy, Math.max(2.2, S * 0.012), '#ffd43b', '#fff', 1.2); disc(cx, cy, Math.max(5, S * 0.03), null, 'rgba(255,255,255,0.8)', 1.2);
    },
    group(cx, yb, S) {                                   // the Local Group: two big spirals and many dwarf galaxies
      const R = S / 2, cy = yb - R, c = ctx();
      disc(cx, cy, R, rg(cx, cy, 0, cx, cy, R, [[0, 'rgba(110,130,230,0.2)'], [1, 'rgba(110,130,230,0.05)']]), 'rgba(150,175,255,0.45)', 1.2);
      GROUP.forEach(([u, v, s]) => { const x = cx + u * R, y = cy + v * R, r = Math.max(1.2, s * R); disc(x, y, r * 2, rg(x, y, 0, x, y, r * 2, [[0, 'rgba(255,235,190,0.8)'], [1, 'rgba(255,235,190,0)']])); });
      [[-0.14, 0.04, 0.0], [0.2, -0.06, -0.3]].forEach(([u, v, rot]) => { const x = cx + u * R, y = cy + v * R, r = Math.max(3, R * 0.11);
        c.save(); c.translate(x, y); c.rotate(rot); c.scale(1, 0.4); disc(0, 0, r, rg(0, 0, 0, 0, 0, r, [[0, 'rgba(255,240,200,1)'], [0.4, 'rgba(210,225,255,0.8)'], [1, 'rgba(160,190,255,0)']])); c.restore(); });
    },
    virgo(cx, yb, S) { webPic(cx, yb, S, 'rgba(120,140,255,0.5)', false); },
    laniakea(cx, yb, S) { webPic(cx, yb, S, 'rgba(255,170,120,0.55)', true); },
  };

  // the measured radius: a line from the centre to the edge at angle `ang`, in the measuring colour
  function radiusLine(cx, cy, R, ang) {
    const ex = cx + R * Math.cos(ang), ey = cy + R * Math.sin(ang), px = -Math.sin(ang) * 5, py = Math.cos(ang) * 5;
    line(cx, cy, ex, ey, 'rgb(232,118,28)', 2.2); line(ex - px, ey - py, ex + px, ey + py, 'rgb(232,118,28)', 2.2, 'butt');
  }

  // plan view of orbits around the Sun: `radii` in AU, outermost `rmax` AU is the picture's radius S / 2
  function orbitPicture(cx, yb, S, radii, rmax, f) {
    const R = S / 2, cy = yb - R, c = ctx(), colP = ['#adb5bd', '#e8c17a', '#339af0', '#e8590c', '#d9a066', '#e6cf9a', '#74c0fc', '#4263eb'];
    const ring = f > 0.5 ? 'rgba(60,70,90,0.55)' : 'rgba(200,215,245,0.6)';
    disc(cx, cy, R * 1.0, f > 0.5 ? 'rgba(255,255,255,0.35)' : 'rgba(255,255,255,0.05)');
    radii.forEach((a, i) => { c.save(); if (i < radii.length - 1) c.setLineDash([4, 5]); disc(cx, cy, R * a / rmax, null, ring, i === radii.length - 1 ? 1.8 : 1.1); c.restore(); });
    disc(cx, cy, Math.max(3, S * 0.012), rg(cx, cy, 0, cx, cy, Math.max(3, S * 0.012), [[0, '#fff9db'], [1, '#f08c00']]), '#e67700', 1);
    disc(cx, cy, Math.max(7, S * 0.03), rg(cx, cy, 0, cx, cy, Math.max(7, S * 0.03), [[0, 'rgba(255,200,60,0.5)'], [1, 'rgba(255,200,60,0)']]));
    // the measured radius: from the Sun to the outermost planet, in the measuring colour
    radiusLine(cx, cy, R, -0.5 - (radii.length - 1) * 0.75);
    radii.forEach((a, i) => { const an = -0.5 - i * 0.75, x = cx + R * a / rmax * Math.cos(an), y = cy + R * a / rmax * Math.sin(an); disc(x, y, 2.4 + (i > 3 ? 1.6 : 0.4) + (radii.length === 1 ? 1.6 : 0), colP[radii.length === 1 ? 2 : i], '#fff', 1); });
  }

  // every canvas text: its ink box is pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col, alpha) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35]), 255 * (alpha === undefined ? 1 : alpha)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
});
