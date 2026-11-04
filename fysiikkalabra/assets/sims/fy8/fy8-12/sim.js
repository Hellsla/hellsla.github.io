// fy8-12 Ionisoiva säteily ja elimistö: a radiation source (none, alpha, beta or gamma), n sheets or plates of an absorber
// (paper 0,1 mm a sheet, aluminium or lead 1,0 mm a plate; n = 0–20) and a Geiger–Müller tube that counts pulses for
// 10 s. Model: without an absorber each source gives on average 600 pulses in 10 s at the tube, the background 4.
// Transmission T: alpha 0 behind any sheet (range in paper about 0,05 mm); beta exp(-6,6 cm²/g · x) below the maximum
// range x = 1,1 g/cm² (E_max 2,28 MeV), 0 beyond it (x = density · thickness); gamma (1/2)^(d / d½) with the narrow-beam
// half-value thicknesses of 662 keV photons, paper 100 mm, aluminium 34 mm, lead 5,5 mm. A count is 6000 time slots of
// 10/6000 s, each a source hit with probability 0,1 · T and a background hit with probability 4/6000, drawn from a seeded
// generator (mulberry32, seed 100003 · k + 1009 · (4 · source + material) + 31 · n + 24, k the count's number at this
// setting), so the first count at a setting is repeatable and a second one differs. The picture: the source in a lead
// holder, the plates (drawn to scale in their own material, paper sheets thicker than scale), the tube with its wire,
// a particle or photon for every counted hit (violet alpha, blue beta, orange wavy gamma, grey background from above),
// absorbed ones stopping in the plates, an avalanche flash at the wire for each pulse, and the counter. Time runs at the
// chosen speed (simulated seconds per second); the count depends only on simulated time. Every canvas text goes through
// lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const TM = 10, SLOTS = 6000, S0 = 600, B0 = 4;
  const SOURCES = ['tausta', 'alfa', 'beeta', 'gamma'], MATERIALS = ['paperi', 'alumiini', 'lyijy'];
  const PLATE = { paperi: 0.1, alumiini: 1.0, lyijy: 1.0 }, RHO = { paperi: 0.80, alumiini: 2.70, lyijy: 11.35 };
  const HVL = { paperi: 100, alumiini: 34, lyijy: 5.5 }, MU_B = 6.6, R_B = 1.1;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], RULEL = [227, 220, 203], PAPER = [246, 241, 230],
        GLASSC = [238, 245, 249], ALU = [196, 204, 212], IRONC = [108, 117, 125], EDGE = [138, 150, 163],
        ALPHA = [112, 72, 232], BETA = [25, 113, 194], GAMMA = [232, 89, 12], HEATL = [255, 192, 120];
  const PCOL = { paperi: [255, 255, 255], alumiini: ALU, lyijy: IRONC };
  const AXY = 190, XS = 112, XT = 362, XT1 = 560, YT0 = 166, YT1 = 214, CX0 = 236;   // beam axis, source, tube, plates' centre
  const SPEED = { alfa: 900, beeta: 1300, gamma: 1600 };                               // drawn px per simulated second
  let sk = 1, fh = 15, labels = [];
  let btn, selL, selA, slN, selSpeed, lN, readout;
  let t = 0, running = false, k = 0, hits = [], bg = [], lost = [], counted = 0, result = null;

  function rng(s) {
    let a = s >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let x = a; x = Math.imul(x ^ (x >>> 15), x | 1); x ^= x + Math.imul(x ^ (x >>> 7), x | 61); return (((x ^ (x >>> 14)) >>> 0) + 0.5) / 4294967297; };
  }
  const params = () => ({ L: selL.value(), A: selA.value(), n: Number(slN.value()) });
  const thick = (S) => S.n * PLATE[S.A];                                               // mm
  function trans(S) {
    if (S.L === 'tausta') return 0;
    if (S.n === 0) return 1;
    const d = thick(S);
    if (S.L === 'alfa') return 0;
    if (S.L === 'beeta') { const x = RHO[S.A] * d / 10; return x >= R_B ? 0 : Math.exp(-MU_B * x); }
    return Math.pow(0.5, d / HVL[S.A]);
  }
  const platePx = (S) => S.A === 'paperi' ? 3 * S.n : 4 * S.n;                        // drawn width of the stack

  // one 10 s count: the slot times of the source's hits and of the background's
  function plan(S) {
    const mi = S.n > 0 ? MATERIALS.indexOf(S.A) : 0;
    const R = rng(100003 * k + 1009 * (4 * SOURCES.indexOf(S.L) + mi) + 31 * S.n + 24);
    const q = S0 * trans(S) / SLOTS, qb = B0 / SLOTS, dt = TM / SLOTS;
    hits = []; bg = [];
    for (let i = 0; i < SLOTS; i++) {
      if (R() < q) hits.push((i + 0.5) * dt);
      if (R() < qb) bg.push({ t: (i + 0.5) * dt, x: 0 });
    }
    // drawing only: the absorbed particles and where they stop, and where the background enters the tube
    const V = rng(7 * k + 13 * SOURCES.indexOf(S.L) + 5 * S.n + 3);
    lost = [];
    if (S.L !== 'tausta' && S.n > 0) {
      const m = Math.round(S0 * (1 - trans(S))), w = platePx(S);
      for (let j = 0; j < m; j++) lost.push({ t: V() * TM, depth: S.L === 'alfa' ? 0 : V() * w, y: (V() - 0.5) * 30 });
    }
    for (const b of bg) b.x = XT + 30 + V() * (XT1 - XT - 60);
    for (let j = 0; j < hits.length; j++) hits[j] = { t: hits[j], y: (V() - 0.5) * 30, w: XT + 20 + V() * (XT1 - XT - 40) };
  }
  function abort() { running = false; t = 0; counted = 0; result = null; k = 0; hits = []; bg = []; lost = []; }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('mittaa')).parent(controls);
    btn.elt.addEventListener('click', () => { if (running) return; k += 1; plan(params()); t = 0; counted = 0; result = null; running = true; });
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('lahde')).parent(l1); selL = p.createSelect().parent(l1);
    for (const s of SOURCES) selL.option(__('lahde_' + s), s);
    selL.selected('gamma');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('este')).parent(l2); selA = p.createSelect().parent(l2);
    for (const m of MATERIALS) selA.option(__('aine_' + m), m);
    selA.selected('lyijy');
    const l3 = p.createElement('label').parent(controls); lN = p.createSpan('').parent(l3); slN = p.createSlider(0, 20, 0, 1).parent(l3);
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l4); selSpeed = p.createSelect().parent(l4);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '5'); selSpeed.selected('1');
    for (const el of [selL.elt, selA.elt, slN.elt]) for (const ev of ['input', 'change']) el.addEventListener(ev, abort);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { lahde: { input: selL.elt, unit: '' }, aine: { input: selA.elt, unit: '' }, n: { input: slN.elt, unit: '' } },
      reset: () => { selL.selected('gamma'); selA.selected('lyijy'); slN.value(0); abort(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params(), T = trans(S), d = thick(S);
    const t0 = t;
    if (running) {
      t = Math.min(TM, t + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
      for (const h of hits) if (h.t > t0 && h.t <= t) counted++;
      for (const b of bg) if (b.t > t0 && b.t <= t) counted++;
      if (t >= TM) { running = false; result = counted; }
    }
    btn.html(running ? __('mitataan') : __('mittaa'));
    const dtx = S.A === 'paperi' ? tx(d, 1) : tx(d, 0);
    lN.html(__('levyja', { n: String(S.n), d: dtx }));
    const este = S.n === 0 ? __('ei_estetta') : __('este_kuvaus', { A: __('aine_' + S.A), d: dtx });
    readout.html(__('lukemat', { L: __('lahde_' + S.L), E: este, t: tx(t, 1), N: String(counted),
                                 R: result === null ? '\\text{–}' : String(result) }));
    window.simState = { lahde: S.L, aine: S.A, n: S.n, d, T, odotus: S0 * T + B0, t, laskuri: counted, pulssit: result,
                        mittaus: k, running: running ? 1 : 0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 17;
    labels = [];
    p.background(255);
    scene(S, d);
    particles(S);
    window.simState.labels = labels;
  };

  // --- the bench: source holder, plates, the GM tube with its wire, the cable and the counter ---
  function scene(S, d) {
    p.noStroke(); p.fill(...PAPER); p.rect(14, 262, 572, 10, 3);
    // lead holder with the source disc facing the tube
    p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...IRONC); p.rect(36, 150, 76, 80, 6);
    p.fill(...(S.L === 'tausta' ? RULEL : S.L === 'alfa' ? ALPHA : S.L === 'beeta' ? BETA : GAMMA));
    p.rect(104, AXY - 13, 10, 26, 2);
    p.noStroke(); p.fill(...EDGE); p.rect(52, 230, 44, 32);
    lab(__('k_lahde_' + S.L), 74, 300, 'c', INKC);
    // the plates, centred on CX0
    const w = platePx(S), x0 = CX0 - w / 2;
    if (S.n > 0) {
      for (let i = 0; i < S.n; i++) {
        const pw = S.A === 'paperi' ? 3 : 4, x = x0 + i * pw;
        p.stroke(...(S.A === 'paperi' ? RULEC : INKC)); p.strokeWeight(S.A === 'paperi' ? 1 : 1.2); p.fill(...PCOL[S.A]);
        p.rect(x, 128, pw, 124);
      }
      p.noFill(); p.stroke(...INKC); p.strokeWeight(2); p.rect(x0, 128, w, 124);
    } else {
      p.noFill(); p.stroke(...RULEC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 6]); p.line(CX0, 132, CX0, 248); p.drawingContext.setLineDash([]);
    }
    const dtx = S.A === 'paperi' ? tx(d, 1) : tx(d, 0);
    lab(S.n === 0 ? '$\\text{' + __('ei_estetta') + '}$' : '$\\text{' + __('aine_' + S.A) + '}$', CX0, 98, 'c', INKC);
    if (S.n > 0) lab('$d = ' + dtx + '\\,\\text{mm}$', CX0, 300, 'c', INKC);
    // the GM tube: metal wall, gas, a thin window towards the source, the central wire
    p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...EDGE); p.rect(XT, YT0 - 6, XT1 - XT, YT1 - YT0 + 12, 8);
    p.noStroke(); p.fill(...GLASSC); p.rect(XT + 6, YT0, XT1 - XT - 12, YT1 - YT0, 4);
    p.stroke(...INKC); p.strokeWeight(3); p.line(XT, YT0 - 2, XT, YT1 + 2);
    p.stroke(...GAMMA); p.strokeWeight(2); p.line(XT + 14, AXY, XT1 - 2, AXY);
    lab(__('gm_putki'), (XT + XT1) / 2, 132, 'c', INKC);
    // cable and counter
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.bezier(XT1, AXY, 590, AXY, 590, 300, 560, 318);
    p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...ALU); p.rect(400, 286, 160, 100, 10);
    p.fill(255); p.strokeWeight(2); p.rect(412, 296, 136, 80, 6);
    lab('$N = ' + String(counted) + '$', 480, 320, 'c', INKC);
    lab('$t = ' + tx(t, 1) + '\\,\\text{s}$', 480, 366, 'c', MUTEDC);
  }

  // --- what flies: a mark for every counted hit, the absorbed ones stopping in the plates, avalanches at the wire ---
  function particles(S) {
    if (!running && result === null) return;
    const v = SPEED[S.L] || 1600, L = XT - XS, travel = L / v;
    const w = platePx(S), xa = CX0 - w / 2;
    for (const h of hits) {
      const f = (t - (h.t - travel)) / travel;
      if (f >= 0 && f <= 1) mark(S.L, XS + f * L, AXY + h.y * (1 - f), v);
      const age = t - h.t;
      if (age >= 0 && age < 0.15) avalanche(h.w, 1 - age / 0.15);
    }
    for (const q of lost) {
      const xs = xa + q.depth, tr = (xs - XS) / v, f = (t - q.t) / tr;
      if (f >= 0 && f <= 1) mark(S.L, XS + f * (xs - XS), AXY + q.y, v);
      else if (f > 1 && f < 1 + 0.12 / tr) { p.noStroke(); p.fill(HEATL[0], HEATL[1], HEATL[2], 200); p.circle(xs, AXY + q.y, 9); }
    }
    for (const b of bg) {
      const f = (t - (b.t - 0.12)) / 0.12;
      if (f >= 0 && f <= 1) wave(b.x, 40 + f * (YT0 - 40), 0, 1, MUTEDC);
      const age = t - b.t;
      if (age >= 0 && age < 0.15) avalanche(b.x, 1 - age / 0.15);
    }
  }
  function mark(kind, x, y) {
    if (kind === 'alfa') { p.stroke(255); p.strokeWeight(1.5); p.fill(...ALPHA); p.circle(x, y, 11); }
    else if (kind === 'beeta') { p.stroke(255); p.strokeWeight(1.2); p.fill(...BETA); p.circle(x, y, 7); }
    else wave(x, y, 1, 0, GAMMA);
  }
  function wave(x, y, ux, uy, col) {              // a short wavy photon whose head is at (x, y), moving along (ux, uy)
    p.noFill(); p.stroke(...col); p.strokeWeight(2.2); p.beginShape();
    for (let s = 0; s <= 22; s += 2) { const a = 3.5 * Math.sin(s / 22 * 2 * Math.PI * 1.5); p.vertex(x - ux * s - uy * a, y - uy * s + ux * a); }
    p.endShape();
  }
  function avalanche(x, a) {                      // electrons drifting in to the wire and a glow: one pulse
    p.noStroke(); p.fill(HEATL[0], HEATL[1], HEATL[2], 210 * a); p.ellipse(x, AXY, 44 * (1.4 - a), 22);
    p.fill(BETA[0], BETA[1], BETA[2], 255 * a);
    for (let j = 0; j < 6; j++) { const dx = (j - 2.5) * 6, dy = (j % 2 ? -1 : 1) * 14 * a; p.circle(x + dx, AXY + dy, 4); }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), 400 - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (v, d) => v.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
