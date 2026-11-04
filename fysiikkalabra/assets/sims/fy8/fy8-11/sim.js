// fy8-11 Fissio, fuusio ja ydinvoima: a chain reaction generation by generation. Generation 0 has N0 = 1000 neutrons.
// Each neutron causes a fission with probability P_f = (1,2 - 0,008 s) : 2,5, where s (0-100 %) is how far the control
// rods are in; otherwise it is lost (absorbed in a control rod with probability 0,0032 s, otherwise absorbed elsewhere
// or escaped). A fission gives 2 or 3 new neutrons (equally likely, mean 2,5), so the multiplication factor is
// k = 2,5 P_f = 1,2 - 0,008 s. The draws come from a seeded generator (mulberry32, seed 1000 * (series + 2) + 7;
// series 1-3), so a series is repeatable and the numbers agree with lessons/FY8/fy8-11/lesson-answers.py.
// The picture: the reactor core (water, fuel rods, control rods lowered to s) with the current generation's neutrons
// (grey dots, at most 160 drawn) that move, then cause a fission (orange flash), vanish into a rod or leave the core;
// beside it (below on a phone) the graph of N per generation with the model N0 k^g dashed. Käynnistä runs the
// generations at the chosen speed (generations per second); the physics depends only on g. Every canvas text goes
// through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const GMAX = 30, N0 = 1000, CAP = 3000000, SHOW = 160;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], WATERL = [169, 209, 240], WATERC = [47, 116, 181], ALU = [196, 204, 212], IRONC = [108, 117, 125],
        METAL = [138, 150, 163], PAPER = [246, 241, 230];
  const WIDE = { H: 400, cx: 22, cy: 58, cw: 270, ch: 262, ox: 380, oy: 330, x1: 560, y1: 62, title: 26, cap: 352, xlab: 354 };
  const NARROW = { H: 860, cx: 70, cy: 104, cw: 460, ch: 320, ox: 150, oy: 772, x1: 540, y1: 560, title: 36, cap: 470, xlab: 806 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let btnRun, slS, slG, selS, selSpeed, lS, lG, readout;
  let gt = 0, running = false, key = '', run = null;

  function rng(s) {
    let a = s >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let x = a; x = Math.imul(x ^ (x >>> 15), x | 1); x ^= x + Math.imul(x ^ (x >>> 7), x | 61); return (((x ^ (x >>> 14)) >>> 0) + 0.5) / 4294967297; };
  }
  // the whole chain of one setting: N[g], F[g] and the fates of the first SHOW neutrons of each generation
  function chain(s, series) {
    const k2 = s + ':' + series;
    if (k2 === key) return run;
    const R = rng(1000 * (series + 2) + 7), pf = (1.2 - 0.008 * s) / 2.5, prod = 0.0032 * s;
    const N = [N0], F = [], fate = [];
    for (let g = 0; g < GMAX; g++) {
      const n = N[g]; let nxt = 0, f = 0; const fg = [];
      if (n > CAP) { N.push(n); F.push(0); fate.push(fg); continue; }
      for (let i = 0; i < n; i++) {
        const u = R();
        if (u < pf) { f++; nxt += R() < 0.5 ? 2 : 3; if (i < SHOW) fg.push(1); }
        else if (i < SHOW) fg.push(u < pf + prod ? 2 : 3);       // 2: into a control rod, 3: lost elsewhere
      }
      N.push(nxt); F.push(f); fate.push(fg);
    }
    F.push(0); fate.push([]);
    key = k2; run = { N, F, fate, k: 1.2 - 0.008 * s };
    return run;
  }
  const params = () => ({ s: Number(slS.value()), series: Number(selS.value()) });

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnRun = p.createButton(__('kaynnista')).parent(controls);
    btnRun.elt.addEventListener('click', () => { if (running) running = false; else { if (gt >= GMAX - 1e-9) gt = 0; running = true; } });
    const l1 = p.createElement('label').parent(controls); lS = p.createSpan('').parent(l1); slS = p.createSlider(0, 100, 30, 5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lG = p.createSpan('').parent(l2); slG = p.createSlider(0, GMAX, 0, 1).parent(l2);
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('arvonta')).parent(l3); selS = p.createSelect().parent(l3);
    for (let s = 1; s <= 3; s++) selS.option(__('sarja', { n: String(s) }), String(s));
    selS.selected('1');
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l4); selSpeed = p.createSelect().parent(l4);
    selSpeed.option(__('hidas'), '0.4'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2.5'); selSpeed.selected('1');
    for (const ev of ['input', 'change']) slG.elt.addEventListener(ev, () => { gt = Number(slG.value()); running = false; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { s: { input: slS.elt, unit: '%' }, g: { input: slG.elt, unit: '' }, sarja: { input: selS.elt, unit: '' } },
      reset: () => { slS.value(30); selS.selected('1'); gt = 0; slG.value(0); running = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params(), C = chain(S.s, S.series);
    if (running) {
      gt = Math.min(GMAX, gt + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
      if (gt >= GMAX) running = false;
      slG.value(Math.floor(gt));
    }
    const g = Math.min(GMAX, Math.floor(gt + 1e-9)), phase = running ? gt - g : 0;
    const N = C.N[g], F = g < GMAX ? C.F[g] : 0, ratio = g > 0 && C.N[g - 1] > 0 ? N / C.N[g - 1] : null;
    btnRun.html(running ? __('pysayta') : __('kaynnista'));
    lS.html(__('sauvat', { s: String(S.s) }));
    lG.html(__('sukupolvi', { g: String(g) }));
    readout.html(__('lukemat', { k: tx(C.k, 2), g: String(g), N: big(N), F: g < GMAX ? big(F) : '\\text{–}',
                                 r: ratio === null ? '\\text{–}' : tx(ratio, 3), m: big(Math.round(N0 * Math.pow(C.k, g))) }));
    window.simState = { s: S.s, k: C.k, g, N, F, ratio: ratio === null ? -1 : ratio, model: N0 * Math.pow(C.k, g), sarja: S.series,
                        running: running ? 1 : 0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    core(S, C, g, phase);
    graph(C, g);
    window.simState.labels = labels;
  };

  // --- the reactor core: water, fuel rods, control rods lowered to s, the current generation's neutrons ---
  function core(S, C, g, phase) {
    const { cx, cy, cw, ch } = G;
    // pressure vessel and water
    p.noStroke();
    for (let i = 0; i <= 20; i++) { const u = i / 20; p.fill(p.lerpColor(p.color(...WATERL), p.color(...WATERC), u * 0.55)); p.rect(cx, cy + u * ch * 0.95, cw, ch / 20 + 1); }
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3 * sk); p.rect(cx, cy, cw, ch, 10 * sk);
    // fuel rods (6) and control rods (5) between them
    const nf = 6, gap = cw / nf, top = cy + 16 * sk, bot = cy + ch - 16 * sk, rodW = 12 * sk;
    for (let i = 0; i < nf; i++) {
      const x = cx + gap * (i + 0.5);
      p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.fill(...ALU); p.rect(x - rodW / 2, top, rodW, bot - top, 4 * sk);
      p.noStroke(); p.fill(...HEATL); p.rect(x - rodW / 2 + 3 * sk, top + 4 * sk, rodW - 6 * sk, bot - top - 8 * sk, 2 * sk);
    }
    const depth = (bot - top) * S.s / 100;
    for (let i = 1; i < nf; i++) {
      const x = cx + gap * i;
      p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.fill(...IRONC);
      p.rect(x - 4 * sk, cy - 22 * sk, 8 * sk, 22 * sk + depth + 6 * sk, 2 * sk);
    }
    // neutrons of this generation: the first SHOW of them (or all, if fewer)
    const n = Math.min(C.N[g], SHOW), fates = C.fate[g] || [];
    for (let i = 0; i < n; i++) {
      const h1 = hash(g * 977 + i * 13 + 1), h2 = hash(g * 977 + i * 13 + 2), h3 = hash(g * 977 + i * 13 + 3);
      const x0 = cx + 18 * sk + h1 * (cw - 36 * sk), y0 = cy + 18 * sk + h2 * (ch - 36 * sk), ang = h3 * 2 * Math.PI;
      const fate = g < GMAX ? fates[i] : 0, mv = Math.min(phase / 0.7, 1);
      let x = x0 + Math.cos(ang) * 40 * sk * mv, y = y0 + Math.sin(ang) * 40 * sk * mv;
      if (fate === 3 && phase > 0.7) { const e = (phase - 0.7) / 0.3; x += Math.cos(ang) * 120 * sk * e; y += Math.sin(ang) * 120 * sk * e; }
      x = Math.min(Math.max(x, cx + 6 * sk), cx + cw - 6 * sk); y = Math.min(Math.max(y, cy + 6 * sk), cy + ch - 6 * sk);
      if (phase > 0.7 && fate === 1) {                    // a fission: an orange flash
        const e = (phase - 0.7) / 0.3;
        p.noStroke(); p.fill(HEATC[0], HEATC[1], HEATC[2], 255 * (1 - 0.6 * e)); p.circle(x, y, (8 + 14 * e) * sk);
        p.fill(HEATL[0], HEATL[1], HEATL[2], 255 * (1 - e)); p.circle(x, y, (4 + 6 * e) * sk);
        continue;
      }
      if (phase > 0.7 && fate === 2) continue;           // absorbed in a control rod: gone
      const alpha = fate === 3 && phase > 0.7 ? 255 * (1 - (phase - 0.7) / 0.3) : 255;
      p.stroke(INKC[0], INKC[1], INKC[2], alpha); p.strokeWeight(1.2 * sk); p.fill(ALU[0], ALU[1], ALU[2], alpha); p.circle(x, y, 6.5 * sk);
    }
    lab(__('sydan_otsikko'), cx, G.title, 'l', INKC);
    lab(__('neutroneja', { N: big(C.N[g]) }), cx + cw / 2, G.cap, 'c', INKC);
  }
  function hash(i) { let x = Math.imul(i ^ 0x9E3779B9, 0x85EBCA6B); x ^= x >>> 13; x = Math.imul(x, 0xC2B2AE35); x ^= x >>> 16; return (x >>> 0) / 4294967296; }

  // --- neutrons per generation with the model N0 k^g dashed ---
  function graph(C, g) {
    const { ox, oy, x1, y1 } = G;
    let top = N0;
    for (const v of C.N) top = Math.max(top, v);
    top = Math.max(top, N0 * Math.pow(C.k, GMAX));
    const steps = [2000, 4000, 8000, 20000, 40000, 100000, 200000, 400000, 800000, 2000000, 4000000];
    let ymax = steps[steps.length - 1];
    for (const v of steps) if (v >= top) { ymax = v; break; }
    const GX = (v) => ox + v / GMAX * (x1 - ox), GY = (v) => oy - Math.min(v, ymax) / ymax * (oy - y1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let v = 5; v <= GMAX; v += 5) p.line(GX(v), oy, GX(v), y1);
    for (let j = 1; j <= 4; j++) p.line(ox, GY(j * ymax / 4), x1, GY(j * ymax / 4));
    // the model, faint and dashed
    p.noFill(); p.stroke(...HEATL); p.strokeWeight(3 * sk); p.drawingContext.setLineDash([9 * sk, 6 * sk]);
    p.beginShape();
    for (let i = 0; i <= 120; i++) { const v = GMAX * i / 120; p.vertex(GX(v), GY(N0 * Math.pow(C.k, v))); }
    p.endShape(); p.drawingContext.setLineDash([]);
    // the series' generations up to the current one
    for (let j = 0; j <= g; j++) {
      p.stroke(255); p.strokeWeight(1.5 * sk); p.fill(...HEATC);
      p.circle(GX(j), GY(C.N[j]), (j === g ? 13 : 8) * sk);
    }
    // axes with filled arrowheads
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, x1 + 12 * sk, oy); p.line(ox, oy, ox, y1 - 12 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(x1 + 24 * sk, oy, x1 + 10 * sk, oy - 6 * sk, x1 + 10 * sk, oy + 6 * sk);
    p.triangle(ox, y1 - 24 * sk, ox - 6 * sk, y1 - 10 * sk, ox + 6 * sk, y1 - 10 * sk);
    for (let v = 5; v <= GMAX; v += 5) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(v), oy, GX(v), oy + 6 * sk);
      if (v % 10 === 0) lab('$' + String(v) + '$', GX(v), G.xlab, 'c', INKC);
    }
    lab('$0$', ox - 8 * sk, G.xlab, 'r', INKC);
    for (let j = 1; j <= 4; j++) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(j * ymax / 4), ox, GY(j * ymax / 4));
      if (j % 2 === 0 || sk < 1.5) lab('$' + big(j * ymax / 4) + '$', ox - 10 * sk, GY(j * ymax / 4) + 0.36 * fh, 'r', INKC);
    }
    lab('$N$', ox + 12 * sk, y1 - 18 * sk, 'l', INKC);
    lab(__('sukupolvi_akseli'), (ox + x1) / 2, G.xlab + 1.5 * fh, 'c', INKC);
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
  // a whole number with thin spaces between the thousands (LaTeX)
  const big = (v) => String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g, '\\,');
});
