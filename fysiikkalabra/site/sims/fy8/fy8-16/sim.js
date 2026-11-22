// fy8-16 Maailmankaikkeuden kehitys: galaxies' redshift against their distance, and the Hubble–Lemaître law fitted by hand.
// Eight galaxies (invented model values, the same table as lessons/FY8/fy8-16/lesson-answers.py GALAXIES) recede at
// v = 70 km/s/Mpc · d plus a fixed own motion of a few hundred km/s. Their light has z = v / c (small z, v ≈ cz) and every
// hydrogen absorption line is seen at λ = λ0 (1 + z) (Hα 656,3, Hβ 486,1, Hγ 434,0, Hδ 410,2 nm). The student picks a
// galaxy: the sky map rings it and a light wave runs from it to the Milky Way, its wavelength stretching on the way (the
// stretch is exaggerated eightfold so that it shows); the spectrum panel shows the laboratory and the galaxy's lines; each
// galaxy picked leaves its point (d, v) on the graph. A slider sets the slope H0 of a line v = H0 d through the origin,
// which the student fits to the points by eye; the readout gives 1 / H0 in 10⁹ a (1 Mpc = 3,086e19 km, 1 a = 3,156e7 s).
// The speed select paces the wave only and changes no value. Every canvas text goes through lab(), which pushes its box to
// simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const C_KMS = 2.998e5, MPC_KM = 3.086e19, YEAR_S = 3.156e7, H0_MODEL = 70, LINES = [656.3, 486.1, 434.0, 410.2], HA = 656.3;
  // [number, d in Mpc, own motion in km/s, direction on the sky map in degrees above the horizontal]
  const GAL = [[1, 22, 260, 72], [2, 45, -310, 18], [3, 78, 190, 52], [4, 110, -140, 12], [5, 145, 330, 40], [6, 185, -260, 8],
    [7, 230, 150, 27], [8, 275, -220, 4]];
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], WHITE = [255, 255, 255], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], RULEC = [201, 194, 178], ALU = [196, 204, 212], COLDL = [208, 230, 251];
  const WIDE = { H: 400, s: 1, map: { x: 10, y: 10, w: 285, h: 190 }, spec: { x: 10, y: 212, w: 285 },
                 gx0: 352, gy0: 340, gx1: 560, gy1: 62 };
  const NARROW = { H: 1100, s: 1.6, map: { x: 20, y: 10, w: 560, h: 330 }, spec: { x: 20, y: 360, w: 560 },
                   gx0: 120, gy0: 1010, gx1: 520, gy1: 712 };
  let G = WIDE, sk = 1, fh = 13, labels = [], phase = 0;
  let sel, slider, selSpeed, readout;
  const visited = new Set();

  const galaxy = (k) => {
    const [num, d, vp, ang] = GAL[k - 1], v = H0_MODEL * d + vp, z = v / C_KMS;
    return { num, d, v, z, ang, lam: HA * (1 + z), dlam: HA * z };
  };
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace('.', DEC);
  const thin = (x) => String(Math.round(x)).replace(/\B(?=(\d{3})+(?!\d))/g, '\\,');

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('galaksi')).parent(l0); sel = p.createSelect().parent(l0);
    for (const g of GAL) sel.option(__('galaksi_n', { n: g[0] }), String(g[0]));
    sel.selected('1');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('suora')).parent(l1);
    slider = p.createSlider(40, 100, 50, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l2); selSpeed = p.createSelect().parent(l2);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const bClear = p.createButton(__('tyhjenna')).parent(controls);
    bClear.elt.addEventListener('click', () => { visited.clear(); p.redraw(); });
    sel.changed(() => { phase = 0; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { galaksi: { input: sel.elt, unit: '' }, H0: { input: slider.elt, unit: 'km/s/Mpc' } },
      reset: () => { sel.selected('1'); slider.value(50); visited.clear(); phase = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    phase = (phase + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value())) % 1000;
    const S = galaxy(Math.max(1, Math.min(8, Number(sel.value()) || 1)));
    visited.add(S.num);
    const H0 = Number(slider.value()), age = MPC_KM / H0 / YEAR_S / 1e9;
    readout.html(__('lukemat', { n: S.num, d: S.d, lam: tx(S.lam, 1), dlam: tx(S.dlam, 1), z: tx(S.z, 4), v: thin(Math.round(S.v / 10) * 10),
      H0: H0, age: tx(age, 1) }));
    window.simState = { galaksi: S.num, d: S.d, lam: S.lam, dlam: S.dlam, z: S.z, v: S.v, H0, age, visited: visited.size, phase, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    G = narrow ? NARROW : WIDE; sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    sky(S); spectrum(S); graph(S, H0);
    window.simState.labels = labels;
  };

  // --- the sky map: the Milky Way at the lower left, the galaxies in their directions, the light wave of the picked one ---
  function sky(S) {
    const M = G.map, s = sk;
    p.noStroke(); p.fill(...INKC); p.rect(M.x, M.y, M.w, M.h, 8 * s);
    for (let i = 0; i < 46; i++) {                     // faint stars, fixed
      const a = Math.sin(i * 12.9898) * 43758.5453, b = Math.sin(i * 78.233) * 12345.678;
      p.fill(255, 255, 255, 110); p.circle(M.x + 6 * s + (a - Math.floor(a)) * (M.w - 12 * s), M.y + 6 * s + (b - Math.floor(b)) * (M.h - 12 * s), 1.6 * s);
    }
    const mw = { x: M.x + 30 * s, y: M.y + M.h - 40 * s };
    const ppm = (M.w - 70 * s) / 300;
    const pos = (g) => { const r = 18 * s + g.d * ppm, t = g.ang * Math.PI / 180; return { x: mw.x + r * Math.cos(t), y: mw.y - r * Math.sin(t) }; };
    // the light wave from the picked galaxy to us: its wavelength grows on the way (exaggerated eightfold)
    const P0 = pos(S), L = Math.hypot(mw.x - P0.x, mw.y - P0.y), ux = (mw.x - P0.x) / L, uy = (mw.y - P0.y) / L;
    const lam0 = 9 * s, aex = 8 * S.z;
    p.noFill(); p.stroke(...colour(HA * (1 + S.z))); p.strokeWeight(2 * s); p.beginShape();
    const start = 12 * s, end = L - 12 * s;
    for (let q = start; q <= end; q += 1.5 * s) {
      const u = q / L, ph = (aex > 0 ? Math.log(1 + aex * u) / aex : u) * L / lam0 * 2 * Math.PI - phase * 2 * Math.PI * 1.2;
      const amp = 3.5 * s * Math.min(1, (q - start) / (8 * s), (end - q) / (8 * s));
      p.vertex(P0.x + ux * q - uy * amp * Math.sin(ph), P0.y + uy * q + ux * amp * Math.sin(ph));
    }
    p.endShape();
    // the Milky Way and the galaxies
    disc(mw.x, mw.y, 12 * s, 5 * s, -20);
    lab('$\\text{' + __('linnunrata') + '}$', M.x + 8 * s, M.y + M.h - 10 * s, 'l', WHITE);
    for (let k = 1; k <= 8; k++) {
      const g = galaxy(k), P = pos(g), r = 10 * s * Math.max(0.45, 1 - g.d / 380);
      disc(P.x, P.y, r, r * 0.45, 25 - 9 * k);
      if (k === S.num) { p.noFill(); p.stroke(...WHITE); p.strokeWeight(2 * s); p.circle(P.x, P.y, 2 * r + 12 * s); }
      lab('$' + k + '$', P.x + r + 8 * s, P.y + 0.36 * fh, 'l', k === S.num ? WHITE : RULEC);
    }
  }

  function disc(x, y, rx, ry, deg) {
    p.push(); p.translate(x, y); p.rotate(deg * Math.PI / 180); p.noStroke();
    for (let i = 4; i >= 1; i--) { p.fill(...HEATL, 50 + 40 * (4 - i)); p.ellipse(0, 0, 2 * rx * i / 4, 2 * ry * i / 4); }
    p.fill(255); p.circle(0, 0, Math.max(2.5 * sk, ry * 0.8));
    p.pop();
  }

  // --- the spectra: hydrogen in the laboratory and the same lines in the picked galaxy ---
  function spectrum(S) {
    const B = G.spec, s = sk, lo = 400, hi = 720, X = (l) => B.x + (l - lo) / (hi - lo) * B.w;
    const L1 = B.y + fh, st1 = L1 + 6 * s, sh = 30 * s, L2 = st1 + sh + fh + 6 * s, st2 = L2 + 6 * s, ax = st2 + sh + 4 * s;
    lab('$\\text{' + __('lab_vety') + '}$', B.x, L1, 'l');
    lab('$\\text{' + __('galaksi_n', { n: S.num }) + '}$', B.x, L2, 'l');
    lab('$\\text{H}\\alpha$', X(HA), L1, 'c', MUTEDC);
    const c = p.drawingContext;
    for (const [y, z] of [[st1, 0], [st2, S.z]]) {
      c.save(); const gr = c.createLinearGradient(B.x, 0, B.x + B.w, 0);
      for (let l = lo; l <= hi; l += 10) { const [r, g, b] = colour(l); gr.addColorStop((l - lo) / (hi - lo), `rgb(${r},${g},${b})`); }
      c.fillStyle = gr; c.fillRect(B.x, y, B.w, sh); c.restore();
      p.noStroke(); p.fill(...INKC);
      for (const l0 of LINES) p.rect(X(l0 * (1 + z)) - 1.5 * s, y, 3 * s, sh);
      p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5 * s); p.rect(B.x, y, B.w, sh);
    }
    // the Hα line's shift between the strips
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * s); c.setLineDash([4 * s, 4 * s]);
    p.line(X(HA), st1 + sh + 2 * s, X(HA * (1 + S.z)), st2 - 2 * s); c.setLineDash([]);
    p.stroke(...INKC); p.strokeWeight(2 * s); p.line(B.x, ax, B.x + B.w, ax);
    for (let l = lo; l <= hi; l += 20) { p.strokeWeight((l % 100 === 0 ? 2 : 1.2) * s); p.line(X(l), ax, X(l), ax + (l % 100 === 0 ? 6 : 3) * s); }
    for (const l of [400, 500, 600, 700]) lab('$' + l + '$', X(l), ax + 7 * s + fh, 'c', MUTEDC);
    lab('$\\lambda\\ (\\text{nm})$', B.x + B.w, ax + 7 * s + 2.4 * fh, 'r');
  }

  // --- the graph: v against d for the galaxies picked, the current one ringed, the line v = H0 d of the slider ---
  const GX = (d) => G.gx0 + d / 300 * (G.gx1 - G.gx0), GY = (v) => G.gy0 - v / 21000 * (G.gy0 - G.gy1);
  function graph(S, H0) {
    const s = sk, every = sk > 1.5 ? 2 : 1;
    p.stroke(...GRID); p.strokeWeight(1 * s);
    for (let d = 50; d <= 300; d += 50) p.line(GX(d), G.gy0, GX(d), G.gy1);
    for (let v = 3000; v <= 21000; v += 3000) p.line(G.gx0, GY(v), G.gx1, GY(v));
    p.stroke(...INKC); p.strokeWeight(2 * s);
    p.line(G.gx0, G.gy0, G.gx1 + 12 * s, G.gy0); p.line(G.gx0, G.gy0, G.gx0, G.gy1 - 12 * s);
    p.noStroke(); p.fill(...INKC);
    p.triangle(G.gx1 + 20 * s, G.gy0, G.gx1 + 10 * s, G.gy0 - 5 * s, G.gx1 + 10 * s, G.gy0 + 5 * s);
    p.triangle(G.gx0, G.gy1 - 20 * s, G.gx0 - 5 * s, G.gy1 - 10 * s, G.gx0 + 5 * s, G.gy1 - 10 * s);
    p.stroke(...INKC); p.strokeWeight(1.5 * s);
    for (let i = 1; i <= 6; i++) {
      const d = 50 * i; p.line(GX(d), G.gy0, GX(d), G.gy0 + 5 * s);
      if (i % every === 0) lab('$' + d + '$', GX(d), G.gy0 + 6 * s + fh, 'c', MUTEDC);
    }
    for (let i = 1; i <= 7; i++) {
      const v = 3000 * i; p.stroke(...INKC); p.line(G.gx0 - 5 * s, GY(v), G.gx0, GY(v));
      if (i % every === 0) lab('$' + (3 * i) + '$', G.gx0 - 8 * s, GY(v) + 0.36 * fh, 'r', MUTEDC);
    }
    lab('$0$', G.gx0 - 8 * s, G.gy0 + 6 * s + fh, 'r', MUTEDC);
    lab('$d\\ (\\text{Mpc})$', G.gx1 + 20 * s, G.gy0 + 6 * s + 2.4 * fh, 'r');
    lab('$v\\ (10^3\\,\\text{km/s})$', G.gx0 + 10 * s, G.gy1 - 12 * s, 'l');
    // the fitted line through the origin, clipped to the plot
    const dEnd = Math.min(300, 21000 / H0);
    p.stroke(...INKC); p.strokeWeight(2.5 * s); p.line(G.gx0, G.gy0, GX(dEnd), GY(H0 * dEnd));
    lab('$H_0 = ' + H0 + '\\,\\text{km/s/Mpc}$', G.gx0 + 10 * s, G.gy1 + 1.3 * fh, 'l');
    for (const k of visited) {
      const g = galaxy(k);
      p.fill(...HEATC); p.stroke(255); p.strokeWeight(1.5 * s); p.circle(GX(g.d), GY(g.v), 10 * s);
    }
    const x = GX(S.d), y = GY(S.v);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2.5 * s); p.circle(x, y, 20 * s);
    lab('$' + S.num + '$', x + 12 * s, y + 1.25 * fh, 'l');
  }

  // the colour of light of wavelength lam (nm) (Bruton), as in the chapter Spektrit paljastavat atomin energiatasot
  function colour(lam) {
    let r = 0, g = 0, b = 0;
    if (lam < 440) { r = -(lam - 440) / 60; b = 1; } else if (lam < 490) { g = (lam - 440) / 50; b = 1; }
    else if (lam < 510) { g = 1; b = -(lam - 510) / 20; } else if (lam < 580) { r = (lam - 510) / 70; g = 1; }
    else if (lam < 645) { r = 1; g = -(lam - 645) / 65; } else r = 1;
    const f = lam < 420 ? 0.3 + 0.7 * (lam - 380) / 40 : lam > 700 ? 0.3 + 0.7 * (750 - lam) / 50 : 1;
    return [r, g, b].map((v) => Math.round(255 * Math.pow(Math.max(0, Math.min(1, v)) * f, 0.8)));
  }

  // every canvas text: its box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
});
