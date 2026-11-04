// fy8-9 Hajoamislaki ja puoliintumisaika: N0 radioactive nuclei (20, 100, 400 or 1600) of one model isotope with
// half-life T½ (10–40 s). Every nucleus decays at a random moment: its lifetime is tau = -T½ / ln 2 · ln u with u drawn
// from a seeded generator (mulberry32, seed 1000 · series + 42; series 1–5), so every nucleus has at every moment the same
// probability per second, ln 2 / T½, of decaying, whatever its age, and a series is repeatable. N(t) counts the nuclei
// with tau > t. The picture: the nuclei on a grid (undecayed a filled orange disc, decayed a grey ring, a just-decayed
// one flashes and sends out a short ray); beside it (below on a phone) the graph of the series' N(t) up to the current
// time with the decay law N0 (1/2)^(t/T½) faint and dashed behind it and guides at T½ and N0/2. The time runs with
// Käynnistä at the chosen speed (simulated seconds per second) or is set with the time slider; the physics depends
// only on t, so the speed changes nothing but the pace. Every canvas text goes through lab(), which pushes its ink box
// to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const LN2 = Math.log(2), TMAX = 120, NMAXP = 1600, FLASH = 2.5;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], PAPER = [246, 241, 230];
  // wide 600 x 400: nuclei left, graph right; narrow (sim-root < 500 px): 600 x 820, stacked, larger labels
  const WIDE = { H: 400, gx: 20, gy: 46, gs: 268, ox: 368, oy: 330, x1: 566, y1: 62, cap: 340, title: 24, xlab: 352, xstep: 20 };
  const NARROW = { H: 820, gx: 110, gy: 60, gs: 380, ox: 112, oy: 736, x1: 548, y1: 588, cap: 452, title: 30, xlab: 768, xstep: 20 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let btnRun, selN, slT, slt, selS, selSpeed, lT, lt, readout;
  let t = 0, running = false, poolKey = '', pool = null;

  function rng(s) {
    let a = s >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let x = a; x = Math.imul(x ^ (x >>> 15), x | 1); x ^= x + Math.imul(x ^ (x >>> 7), x | 61); return (((x ^ (x >>> 14)) >>> 0) + 0.5) / 4294967297; };
  }
  // the uniform numbers of one series; a nucleus' lifetime is -T½ / ln 2 · ln u, so changing T½ rescales the same series
  function uniforms(series) {
    const key = String(series);
    if (key !== poolKey) { const R = rng(1000 * series + 42); pool = []; for (let i = 0; i < NMAXP; i++) pool.push(R()); poolKey = key; }
    return pool;
  }

  const params = () => ({ N0: Number(selN.value()), T: Number(slT.value()), series: Number(selS.value()) });

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnRun = p.createButton(__('kaynnista')).parent(controls);
    btnRun.elt.addEventListener('click', () => { if (running) running = false; else { if (t >= TMAX - 1e-9) t = 0; running = true; } });
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('ytimia')).parent(l1); selN = p.createSelect().parent(l1);
    for (const k of ['20', '100', '400', '1600']) selN.option(k, k);
    selN.selected('400');
    const l2 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l2); slT = p.createSlider(10, 40, 20, 5).parent(l2);
    const l3 = p.createElement('label').parent(controls); lt = p.createSpan('').parent(l3); slt = p.createSlider(0, TMAX, 0, 1).parent(l3);
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('arvonta')).parent(l4); selS = p.createSelect().parent(l4);
    for (let s = 1; s <= 5; s++) selS.option(__('sarja', { n: String(s) }), String(s));
    selS.selected('1');
    const l5 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l5); selSpeed = p.createSelect().parent(l5);
    selSpeed.option(__('hidas'), '1'); selSpeed.option(__('normaali'), '4'); selSpeed.option(__('nopea'), '12'); selSpeed.selected('4');
    for (const ev of ['input', 'change']) slt.elt.addEventListener(ev, () => { t = Number(slt.value()); running = false; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { N0: { input: selN.elt, unit: '' }, T: { input: slT.elt, unit: 's' }, t: { input: slt.elt, unit: 's' }, sarja: { input: selS.elt, unit: '' } },
      reset: () => { selN.selected('400'); slT.value(20); selS.selected('1'); t = 0; slt.value(0); running = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params();
    if (running) {
      t = Math.min(TMAX, t + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
      if (t >= TMAX) running = false;
      slt.value(Math.round(t));
    }
    const U = uniforms(S.series), k = S.T / LN2;
    const tau = new Array(S.N0);
    let N = 0;
    for (let i = 0; i < S.N0; i++) { tau[i] = -k * Math.log(U[i]); if (tau[i] > t) N++; }
    btnRun.html(running ? __('pysayta') : __('kaynnista'));
    lT.html(__('puoliintumisaika', { T: String(S.T) }));
    lt.html(__('aika', { t: tx(t, 0) }));
    const frac = N / S.N0;
    readout.html(__('lukemat', { t: tx(t, 0), r: tx(t / S.T, 2), N: String(N), D: String(S.N0 - N), f: tx(frac, 3) }));
    window.simState = { N0: S.N0, T: S.T, t, sarja: S.series, N, decayed: S.N0 - N, frac, halves: t / S.T,
                        model: S.N0 * Math.pow(0.5, t / S.T), running: running ? 1 : 0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    nuclei(S, tau, N);
    graph(S, tau);
    window.simState.labels = labels;
  };

  // --- the sample: one disc per nucleus on a square grid ---
  function nuclei(S, tau, N) {
    const { gx, gy, gs } = G, cols = S.N0 === 20 ? 5 : Math.round(Math.sqrt(S.N0)), rows = Math.ceil(S.N0 / cols);
    const cell = gs / Math.max(cols, rows), ox = gx + (gs - cols * cell) / 2, oy = gy + (gs - rows * cell) / 2;
    p.noStroke(); p.fill(...PAPER); p.rect(gx - 6, gy - 6, gs + 12, gs + 12, 6);
    p.noFill(); p.stroke(...RULEC); p.strokeWeight(1.5); p.rect(gx - 6, gy - 6, gs + 12, gs + 12, 6);
    const r = cell * 0.36;
    for (let i = 0; i < S.N0; i++) {
      const cx = ox + (i % cols + 0.5) * cell, cy = oy + (Math.floor(i / cols) + 0.5) * cell;
      if (tau[i] > t) {                                   // undecayed: a filled disc
        p.noStroke(); p.fill(...HEATC); p.circle(cx, cy, 2 * r);
        if (r > 6) { p.fill(...HEATL); p.circle(cx - r * 0.3, cy - r * 0.3, r * 0.7); }
      } else {                                            // decayed: a grey ring; a fresh decay flashes and sends a ray
        const age = t - tau[i];
        if (age < FLASH && r > 1.5) {
          const u = age / FLASH, a = (i * 2.399963) % (2 * Math.PI);
          p.noFill(); p.stroke(HEATL[0], HEATL[1], HEATL[2], 255 * (1 - u)); p.strokeWeight(Math.max(1.5, r * 0.4));
          p.circle(cx, cy, 2 * r * (1 + 1.6 * u));
          p.stroke(HEATC[0], HEATC[1], HEATC[2], 255 * (1 - u)); p.strokeWeight(Math.max(1.2, r * 0.25));
          const d0 = r * (1 + 2 * u), d1 = r * (2 + 4 * u);
          p.line(cx + d0 * Math.cos(a), cy + d0 * Math.sin(a), cx + d1 * Math.cos(a), cy + d1 * Math.sin(a));
        }
        p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(Math.max(1, r * 0.28)); p.circle(cx, cy, 1.5 * r);
      }
    }
    lab(__('otsikko', { N0: String(S.N0) }), gx, G.title, 'l', INKC);
    lab(__('jaljella', { N: String(N) }), gx + gs / 2, G.cap + (G === NARROW ? 18 * sk : 22), 'c', HEATC);
  }

  // --- N(t) of this series (steps) with the decay law dashed behind it ---
  function graph(S, tau) {
    const { ox, oy, x1, y1 } = G;
    const GX = (v) => ox + v / TMAX * (x1 - ox), GY = (n) => oy - n / S.N0 * (oy - y1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let v = G.xstep; v <= TMAX + 1e-9; v += G.xstep) p.line(GX(v), oy, GX(v), y1);
    for (let j = 1; j <= 4; j++) p.line(ox, GY(j * S.N0 / 4), x1, GY(j * S.N0 / 4));
    // guides: the first half-life and half of N0
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([6 * sk, 5 * sk]);
    p.line(GX(S.T), oy, GX(S.T), GY(S.N0 / 2)); p.line(ox, GY(S.N0 / 2), GX(S.T), GY(S.N0 / 2));
    p.drawingContext.setLineDash([]);
    // the decay law, faint and dashed
    p.noFill(); p.stroke(HEATL[0], HEATL[1], HEATL[2]); p.strokeWeight(3 * sk); p.drawingContext.setLineDash([9 * sk, 6 * sk]);
    p.beginShape();
    for (let i = 0; i <= 240; i++) { const v = TMAX * i / 240; p.vertex(GX(v), GY(S.N0 * Math.pow(0.5, v / S.T))); }
    p.endShape(); p.drawingContext.setLineDash([]);
    // the series: N steps down by one at each decay, drawn up to the current time
    const ts = tau.filter((x) => x <= t).sort((a, b) => a - b);
    p.stroke(...HEATC); p.strokeWeight(3 * sk); p.strokeJoin(p.ROUND);
    p.beginShape();
    let n = S.N0, x = 0;
    p.vertex(GX(0), GY(n));
    for (const d of ts) { p.vertex(GX(d), GY(n)); n -= 1; p.vertex(GX(d), GY(n)); x = d; }
    p.vertex(GX(t), GY(n));
    p.endShape();
    // the current point
    p.stroke(255); p.strokeWeight(2 * sk); p.fill(...HEATC); p.circle(GX(t), GY(n), 13 * sk);
    // axes with filled arrowheads
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, x1 + 12 * sk, oy); p.line(ox, oy, ox, y1 - 12 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(x1 + 24 * sk, oy, x1 + 10 * sk, oy - 6 * sk, x1 + 10 * sk, oy + 6 * sk);
    p.triangle(ox, y1 - 24 * sk, ox - 6 * sk, y1 - 10 * sk, ox + 6 * sk, y1 - 10 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let v = G.xstep; v <= TMAX + 1e-9; v += G.xstep) {
      p.line(GX(v), oy, GX(v), oy + 6 * sk);
      if (v % 40 === 0) lab('$' + String(v) + '$', GX(v), G.xlab, 'c', INKC);
    }
    lab('$0$', ox - 8 * sk, G.xlab, 'r', INKC);
    for (let j = 1; j <= 4; j++) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(j * S.N0 / 4), ox, GY(j * S.N0 / 4));
      if (j % 2 === 0 || sk < 1.5) lab('$' + String(j * S.N0 / 4) + '$', ox - 10 * sk, GY(j * S.N0 / 4) + 0.36 * fh, 'r', INKC);
    }
    lab('$N$', ox + 12 * sk, y1 - 18 * sk, 'l', INKC);
    lab('$t\\ (\\text{s})$', (ox + x1) / 2, G.xlab + 1.5 * fh, 'c', INKC);
    lab('$T_{1/2}$', GX(S.T) + 6 * sk, oy - 0.9 * fh, 'l', MUTEDC);
  }

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
  const tx = (v, d) => v.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
