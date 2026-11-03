// fy8-5 Aaltomekaaninen atomimalli ja orbitaalit: the position of hydrogen's electron is "measured" N times in the
// state 1s, 2s or 2p_z. Each measurement is one random point drawn from the state's probability density (lengths in
// units of the Bohr radius a0 = 0,0529 nm, normalisation left out): 1s e^(-2r), 2s (2 - r)^2 e^(-r),
// 2p r^2 cos^2(theta) e^(-r). The points of one series come from a seeded generator, so the series is repeatable and
// a larger N only adds points to it; "Uusi mittaussarja" changes the seed.
// The orbital's boundary at threshold p is the surface of constant density that encloses the probability p (the region
// where the density is largest); the threshold density is found once from a grid in r and cos(theta). A hit is inside
// when its density exceeds the threshold. The picture is a see-through view along y: every hit is drawn at (x, z),
// inside hits blue, outside hits grey, and the boundary as the region's outline. Beside it: the histogram of the hits'
// distances r from the nucleus (0,02 nm bins) with the expected counts faint behind it.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode, static
// picture (nothing moves, so no speed control).
new p5((p) => {
  const A0 = 0.0529, NMAX = 5000, BIN = 0.02, RHIST = 0.8, NB = Math.round(RHIST / BIN);
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], COLDC = [25, 113, 194], COLDL = [208, 230, 251],
        HOTC = [201, 42, 42], WATERL = [169, 209, 240], WATERC = [47, 116, 181], PAPER = [246, 241, 230];
  // geometry: wide 600 x 400 (cloud left, histogram right); narrow (sim-root < 500 px) 600 x 780, stacked, larger labels
  const WIDE = { H: 400, cx: 168, cy: 212, half: 160, sc: 265, ox: 400, oy: 330, gx1: 566, gy1: 86, title: 30, scaleY: 382, xlab: 352, xstep: 0.2 };
  const NARROW = { H: 800, cx: 300, cy: 236, half: 200, sc: 350, ox: 110, oy: 712, gx1: 550, gy1: 548, title: 26, scaleY: 456, xlab: 750, xstep: 0.2 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let selOrb, selN, slP, lP, btnNew, readout, seed = 1, poolKey = '', pool = null;
  const thresholds = {};   // orbital -> {p: threshold density}

  const DENS = {
    '1s': (r, mu) => Math.exp(-2 * r),
    '2s': (r, mu) => (2 - r) * (2 - r) * Math.exp(-r),
    '2p': (r, mu) => r * r * mu * mu * Math.exp(-r),
  };

  // --- the threshold density that encloses probability p: cells of a (r, mu) grid sorted by density ---
  function makeThresholds(orb) {
    const nr = 1500, nmu = orb === '2p' ? 160 : 1, rmax = 40, dr = rmax / nr, f = DENS[orb];
    const d = new Float64Array(nr * nmu), w = new Float64Array(nr * nmu);
    let tot = 0;
    for (let i = 0; i < nr; i++) {
      const r = (i + 0.5) * dr;
      for (let j = 0; j < nmu; j++) {
        const mu = nmu === 1 ? 1 : -1 + (j + 0.5) * 2 / nmu, k = i * nmu + j;
        d[k] = f(r, mu); w[k] = d[k] * r * r * dr; tot += w[k];
      }
    }
    const idx = Array.from(d.keys()).sort((x, y) => d[y] - d[x]);
    const out = {};
    let acc = 0, q = 50;
    for (const k of idx) {
      acc += w[k] / tot;
      while (q <= 95 && acc >= q / 100) { out[q] = d[k]; q += 5; }
      if (q > 95) break;
    }
    return out;
  }

  // --- seeded random numbers (mulberry32) and the sampling of one measurement ---
  function rng(s) {
    let a = s >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return (((t ^ (t >>> 14)) >>> 0) + 0.5) / 4294967297; };
  }
  let cdf2s = null;   // inverse-CDF table of the 2s radial distribution r^2 (2 - r)^2 e^(-r)
  function radius2s(u) {
    if (!cdf2s) {
      const n = 6000, rmax = 40, t = new Float64Array(n + 1); let acc = 0;
      for (let i = 1; i <= n; i++) { const r = (i - 0.5) * rmax / n; acc += r * r * (2 - r) * (2 - r) * Math.exp(-r); t[i] = acc; }
      for (let i = 0; i <= n; i++) t[i] /= acc;
      cdf2s = { t, n, rmax };
    }
    const { t, n, rmax } = cdf2s; let lo = 0, hi = n;
    while (hi - lo > 1) { const m = (lo + hi) >> 1; if (t[m] < u) lo = m; else hi = m; }
    return (lo + (u - t[lo]) / Math.max(t[hi] - t[lo], 1e-12)) * rmax / n;
  }
  function makePool(orb, s) {
    const R = rng(1000 * s + (orb === '1s' ? 1 : orb === '2s' ? 2 : 3)), pts = [];
    for (let i = 0; i < NMAX; i++) {
      let r, mu;
      if (orb === '1s') { r = -0.5 * Math.log(R() * R() * R()); mu = 2 * R() - 1; }
      else if (orb === '2s') { r = radius2s(R()); mu = 2 * R() - 1; }
      else { r = -Math.log(R() * R() * R() * R() * R()); mu = Math.cbrt(2 * R() - 1); }
      const ph = 2 * Math.PI * R(), s_ = Math.sqrt(Math.max(0, 1 - mu * mu));
      pts.push({ r, mu, x: r * s_ * Math.cos(ph), z: r * mu, d: DENS[orb](r, mu) });
    }
    return pts;
  }

  // --- outer extent of the region along the direction where it reaches farthest (z axis for 2p), nm ---
  function extent(orb, t) {
    const f = (r) => DENS[orb](r, 1) - t;
    let lo = orb === '1s' ? 0 : orb === '2s' ? 4 : 2, hi = 40;
    for (let i = 0; i < 80; i++) { const m = (lo + hi) / 2; if (f(m) > 0) lo = m; else hi = m; }
    return (lo + hi) / 2 * A0;
  }

  const params = () => ({ orb: selOrb.value().slice(1), N: Number(selN.value()), p: Number(slP.value()) });

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnNew = p.createButton(__('uusi')).parent(controls);
    btnNew.elt.addEventListener('click', () => { seed += 1; });
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('orbitaali')).parent(l1); selOrb = p.createSelect().parent(l1);
    selOrb.option(__('o1s'), 'o1s'); selOrb.option(__('o2s'), 'o2s'); selOrb.option(__('o2p'), 'o2p');
    selOrb.selected('o1s');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('mittauksia')).parent(l2); selN = p.createSelect().parent(l2);
    for (const k of ['1', '10', '100', '1000', '5000']) selN.option(k, k);
    selN.selected('1000');
    const l3 = p.createElement('label').parent(controls); lP = p.createSpan('').parent(l3); slP = p.createSlider(50, 95, 90, 5).parent(l3);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    for (const o of ['1s', '2s', '2p']) thresholds[o] = makeThresholds(o);
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { orb: { input: selOrb.elt, unit: '' }, N: { input: selN.elt, unit: '' }, p: { input: slP.elt, unit: '%' } },
      reset: () => { selOrb.selected('o1s'); selN.selected('1000'); slP.value(90); seed = 1; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params();
    const key = S.orb + '|' + seed;
    if (key !== poolKey) { pool = makePool(S.orb, seed); poolKey = key; }
    const t = thresholds[S.orb][S.p];
    const pts = pool.slice(0, S.N);
    let k = 0;
    const hist = new Array(NB).fill(0);
    for (const q of pts) {
      if (q.d > t) k++;
      const b = Math.floor(q.r * A0 / BIN);
      if (b < NB) hist[b]++;
    }
    let peak = 0;
    for (let b = 1; b < NB; b++) if (hist[b] > hist[peak]) peak = b;
    const rpeak = (peak + 0.5) * BIN, R = extent(S.orb, t), frac = 100 * k / S.N;
    lP.html(__('kynnys', { p: String(S.p) }));
    const sN = String(S.N), sK = String(k), sOut = String(S.N - k), sF = tx(frac, 1), sRp = tx(rpeak, 2), sR = tx(R, 3);
    readout.html(__('lukemat', { N: sN, k: sK, out: sOut, f: sF, rp: sRp, R: sR }));
    window.simState = { orb: 'o' + S.orb, N: S.N, p: S.p, seed, k, out: S.N - k, frac, rpeak, R, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1;
    fh = narrow ? Math.round(14 * kk) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    cloud(S, pts, t, R);
    histogram(S, hist, peak);
    window.simState.labels = labels;
  };

  // --- the see-through picture of the hits and the boundary ---
  function cloud(S, pts, t, R) {
    const { cx, cy, sc, half } = G;
    const ctx = p.drawingContext;
    ctx.save();
    ctx.fillStyle = `rgb(${PAPER.join(',')})`;
    ctx.beginPath(); ctx.rect(cx - half, cy - half + 8, 2 * half, 2 * half - 16); ctx.fill(); ctx.clip();
    // boundary region, tinted, under the hits
    const X = (u) => cx + u * A0 * sc, Z = (v) => cy - v * A0 * sc;
    ctx.fillStyle = `rgba(${COLDL.join(',')},0.9)`; ctx.strokeStyle = `rgb(${COLDC.join(',')})`; ctx.lineWidth = 2.5 * sk;
    const outline = boundary(S.orb, t);
    for (const poly of outline) {
      ctx.beginPath();
      poly.forEach(([u, v], i) => (i ? ctx.lineTo(X(u), Z(v)) : ctx.moveTo(X(u), Z(v))));
      ctx.closePath(); ctx.fill();
    }
    // the hits: outside grey first, then inside blue on top
    const rad = (S.N <= 100 ? 3.2 : S.N <= 1000 ? 2 : 1.4) * sk;
    for (const inside of [false, true]) {
      ctx.fillStyle = inside ? `rgba(${COLDC.join(',')},0.85)` : `rgba(${MUTEDC.join(',')},0.7)`;
      ctx.beginPath();
      for (const q of pts) if ((q.d > t) === inside) { ctx.moveTo(X(q.x) + rad, Z(q.z)); ctx.arc(X(q.x), Z(q.z), rad, 0, 2 * Math.PI); }
      ctx.fill();
    }
    for (const poly of outline) {
      ctx.beginPath();
      poly.forEach(([u, v], i) => (i ? ctx.lineTo(X(u), Z(v)) : ctx.moveTo(X(u), Z(v))));
      ctx.closePath(); ctx.stroke();
    }
    ctx.restore();
    // the nucleus
    p.stroke(255); p.strokeWeight(1.5 * sk); p.fill(...HOTC); p.circle(cx, cy, 9 * sk);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.rect(cx - half, cy - half + 8, 2 * half, 2 * half - 16, 4);
    lab('$\\text{' + S.orb + '-orbitaali}$', cx - half + 8 * sk, G.title + 10, 'l', INKC);
    // scale bar 0,1 nm
    const x0 = cx - half + 14 * sk, y = G.scaleY - 4 * sk, L = 0.1 * sc;
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(x0, y, x0 + L, y);
    p.strokeWeight(2 * sk); p.line(x0, y - 6 * sk, x0, y + 6 * sk); p.line(x0 + L, y - 6 * sk, x0 + L, y + 6 * sk);
    lab('$0{,}1\\,\\text{nm}$', x0 + L + 8 * sk, y + 0.36 * fh, 'l', INKC);
  }

  // outline polygons of the region where the density exceeds t, in the plane y = 0 (a0 units)
  function boundary(orb, t) {
    const f = DENS[orb];
    if (orb !== '2p') {
      const R = extent(orb, t) / A0, poly = [];
      for (let i = 0; i < 120; i++) { const a = i * 2 * Math.PI / 120; poly.push([R * Math.cos(a), R * Math.sin(a)]); }
      return [poly];
    }
    // 2p: for each polar angle theta, the region along the ray is r_in < r < r_out around the maximum r = 2
    const g = (r) => r * r * Math.exp(-r), gmax = g(2), lobes = [];
    for (const sgn of [1, -1]) {
      const outer = [], inner = [];
      const cmin = Math.sqrt(t / gmax);
      const thMax = Math.acos(Math.min(1, cmin));
      for (let i = 0; i <= 60; i++) {
        const th = -thMax + 2 * thMax * i / 60, cs = Math.max(Math.cos(th), cmin) , need = t / (cs * cs);
        let lo = 2, hi = 40; for (let j = 0; j < 50; j++) { const m = (lo + hi) / 2; if (g(m) > need) lo = m; else hi = m; }
        const ro = lo;
        lo = 0; hi = 2; for (let j = 0; j < 50; j++) { const m = (lo + hi) / 2; if (g(m) > need) hi = m; else lo = m; }
        const ri = hi;
        outer.push([ro * Math.sin(th), sgn * ro * Math.cos(th)]);
        inner.push([ri * Math.sin(th), sgn * ri * Math.cos(th)]);
      }
      lobes.push(outer.concat(inner.reverse()));
    }
    return lobes;
  }

  // --- histogram of the distances, expected counts faint behind ---
  function histogram(S, hist, peak) {
    const { ox, oy, gx1, gy1 } = G;
    const top = niceMax(Math.max(...hist, expectedMax(S)));
    const GX = (r) => ox + r / RHIST * (gx1 - ox), GY = (c) => oy - c / top * (oy - gy1);
    const ystep = top / 4;
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let r = G.xstep; r <= RHIST + 1e-9; r += G.xstep) p.line(GX(r), oy, GX(r), gy1);
    for (let j = 1; j <= 4; j++) p.line(ox, GY(j * ystep), gx1, GY(j * ystep));
    // bars
    p.noStroke();
    for (let b = 0; b < NB; b++) {
      if (!hist[b]) continue;
      p.fill(...(b === peak ? WATERC : WATERL));
      p.rect(GX(b * BIN) + 0.5, GY(hist[b]), GX(BIN) - ox - 1, oy - GY(hist[b]));
    }
    // expected counts N P(bin), dashed
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 4 * sk]);
    p.beginShape();
    for (let b = 0; b < NB; b++) p.vertex(GX((b + 0.5) * BIN), GY(S.N * binProb(S.orb, b)));
    p.endShape(); p.drawingContext.setLineDash([]);
    // axes with arrowheads
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 12 * sk, oy); p.line(ox, oy, ox, gy1 - 12 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 24 * sk, oy, gx1 + 10 * sk, oy - 6 * sk, gx1 + 10 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 24 * sk, ox - 6 * sk, gy1 - 10 * sk, ox + 6 * sk, gy1 - 10 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let r = G.xstep; r <= RHIST + 1e-9; r += G.xstep) {
      p.line(GX(r), oy, GX(r), oy + 6 * sk);
      if (Math.round(r * 10) % 4 === 0 || sk < 1.5) lab('$' + tx(r, 1) + '$', GX(r), G.xlab, 'c', INKC);
    }
    lab('$0$', ox - 8 * sk, G.xlab, 'r', INKC);
    for (let j = 1; j <= 4; j++) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(j * ystep), ox, GY(j * ystep));
      if (sk < 1.5 || j % 2 === 0) lab('$' + fmtCount(j * ystep) + '$', ox - 10 * sk, GY(j * ystep) + 0.36 * fh, 'r', INKC);
    }
    lab('$\\text{osumia}$', ox + 10 * sk, gy1 - 18 * sk, 'l', INKC);
    lab('$r\\ (\\text{nm})$', (ox + gx1) / 2, G.xlab + 1.5 * fh, 'c', INKC);
  }
  // probability that a hit falls in bin b (radial distribution integrated with the midpoint rule)
  const binCache = {};
  function binProb(orb, b) {
    if (!binCache[orb]) {
      const rad = orb === '1s' ? (r) => r * r * Math.exp(-2 * r) : orb === '2s' ? (r) => r * r * (2 - r) * (2 - r) * Math.exp(-r) : (r) => Math.pow(r, 4) * Math.exp(-r);
      const norm = orb === '1s' ? 0.25 : orb === '2s' ? 8 : 24, out = [];
      for (let i = 0; i < NB; i++) {
        let s = 0; const a = i * BIN / A0, w = BIN / A0 / 20;
        for (let j = 0; j < 20; j++) s += rad(a + (j + 0.5) * w) * w;
        out.push(s / norm);
      }
      binCache[orb] = out;
    }
    return binCache[orb][b];
  }
  function expectedMax(S) { let m = 0; for (let b = 0; b < NB; b++) m = Math.max(m, S.N * binProb(S.orb, b)); return m; }
  function niceMax(v) {
    const steps = [4, 8, 12, 20, 40, 80, 120, 200, 400, 800, 1200, 2000];
    for (const s of steps) if (v <= s) return s;
    return Math.ceil(v / 400) * 400;
  }
  const fmtCount = (v) => (Number.isInteger(v) ? String(v) : tx(v, 1));

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
