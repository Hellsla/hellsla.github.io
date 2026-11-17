// fy6-3 Resistanssi ja Ohmin laki: an adjustable source U (0–3,0 V), an ammeter in series and a voltmeter across one
// component: a 10 Ω resistor, a 3,0 V lamp or a constantan wire (ρ = 5,0·10⁻⁷ Ω·m, length l, cross-section A).
// The meters show U and I only; the student works out U : I. Models (lessons/FY6/fy6-3/lesson-answers.py):
// resistor R = 10 Ω; lamp R(U) = R_k + (R_n − R_k)(U/U_n)^0,6 (R_k = 1,0 Ω cold, R_n = 12,0 Ω at U_n = 3,0 V: the
// filament heats as U grows); wire R = ρ l / A at constant temperature (constantan hardly changes with temperature).
// The right (or lower) panel is the (I, U) graph: the component's characteristic faint, the points the student marks,
// the present reading. Moving dots show the conventional current (+ to −); their speed grows with I and the speed
// select changes only their pace. Every canvas text goes through lab(), which pushes its box to simState.labels.
// p5.js 1.9 instance mode.
new p5((p) => {
  const R_RES = 10, RK = 1.0, RN = 12.0, UN = 3.0, RHO = 5.0e-7;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], CUR = [112, 72, 232], LAMPC = [232, 89, 12];
  const HEATL = [255, 192, 120], WIREC = [184, 98, 45], METAL = [138, 150, 163];
  // the circuit is drawn in its own 300 × 400 units, scaled by s and moved by (ox, oy); the graph has its own box
  const WIDE = { H: 400, s: 1, ox: 0, oy: 0, gx0: 352, gy0: 330, gx1: 548, gy1: 84, sep: 'v' };
  const NARROW = { H: 960, s: 1.5, ox: 75, oy: -30, gx0: 110, gy0: 884, gx1: 520, gy1: 636, sep: 'h' };
  let G = WIDE, narrow = false, sk = 1, fs = 13, labels = [];
  let btnMark, btnClear, selComp, slU, slL, slA, selSpeed, lU, lL, lA, readout;
  let marks = [], phase = 0;

  const lampR = (U) => RK + (RN - RK) * Math.pow(Math.max(U, 0) / UN, 0.6);
  const wireR = (l, A) => RHO * l / (A * 1e-6);
  const Rof = (c, U, l, A) => (c === 'vastus' ? R_RES : c === 'lamppu' ? lampR(U) : wireR(l, A));
  const params = () => ({ comp: selComp.value(), U: Number(slU.value()), l: Number(slL.value()), A: Number(slA.value()) });

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnMark = p.createButton(__('merkitse')).parent(controls);
    btnMark.elt.addEventListener('click', () => { const P = params(), R = Rof(P.comp, P.U, P.l, P.A); marks.push({ comp: P.comp, I: P.U / R, U: P.U }); });
    btnClear = p.createButton(__('tyhjenna')).parent(controls);
    btnClear.elt.addEventListener('click', () => { marks = []; });
    const lc = p.createElement('label').parent(controls); p.createSpan(__('komponentti')).parent(lc); selComp = p.createSelect().parent(lc);
    selComp.option(__('vastus'), 'vastus'); selComp.option(__('lamppu'), 'lamppu'); selComp.option(__('lanka'), 'lanka'); selComp.selected('vastus');
    const l1 = p.createElement('label').parent(controls); lU = p.createSpan('').parent(l1); slU = p.createSlider(0, 3, 1.5, 0.1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l2); slL = p.createSlider(0.5, 2, 1, 0.25).parent(l2);
    const l3 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l3); slA = p.createSlider(0.1, 0.4, 0.2, 0.05).parent(l3);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.4'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { comp: { input: selComp.elt }, U: { input: slU.elt, unit: 'V' }, L: { input: slL.elt, unit: 'm' }, A: { input: slA.elt, unit: 'mm²' } },
      reset: () => { selComp.selected('vastus'); slU.value(1.5); slL.value(1); slA.value(0.2); marks = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = params(), R = Rof(P.comp, P.U, P.l, P.A), I = P.U / R;
    phase += Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()) * 140 * I / (I + 0.4);   // dot speed grows with I
    lU.html(__('jannite', { u: tx(P.U, 1) }));
    lL.html(__('pituus', { l: tx(P.l, 2) }));
    lA.html(__('ala', { a: tx(P.A, 2) }));
    readout.html(__('lukemat', { u: tx(P.U, 2), i: tx(I, 3) }));
    const shown = marks.filter((m) => m.comp === P.comp).length;
    window.simState = { comp: P.comp, U: P.U, I, R, L: P.l, A: P.A, P: P.U * I, marks: marks.length, shown, speed: Number(selSpeed.value()), narrow, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fs = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    window.simState.narrow = narrow;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    circuit(P, R, I);
    graph(P, I);
    window.simState.labels = labels;
  };

  // ---- the circuit: source, ammeter, component, voltmeter, moving charges ----
  const X = (x) => G.ox + x * G.s, Y = (y) => G.oy + y * G.s;
  function wire(pts, w) {
    p.noFill(); p.stroke(...INKC); p.strokeWeight((w || 2.5) * sk); p.beginShape();
    for (const [x, y] of pts) p.vertex(X(x), Y(y));
    p.endShape();
  }
  function circuit(P, R, I) {
    const Lx = 44, Rx = 262, T = 96, B = 300, cx = 153;
    const half = P.comp === 'vastus' ? 30 : P.comp === 'lamppu' ? 20 : 40 * P.l;   // the wire drawn to scale, 80 units per metre
    const xa = cx - half, xb = cx + half;
    // wires of the main loop (the battery plates break the left side)
    wire([[Lx, 190], [Lx, T], [Rx, T], [Rx, B], [xb, B]]);
    wire([[xa, B], [Lx, B], [Lx, 206]]);
    // moving charges along the loop, + (top of the battery) round to −
    const path = [[Lx, 190], [Lx, T], [Rx, T], [Rx, B], [Lx, B], [Lx, 206]];
    const segs = []; let tot = 0;
    for (let i = 1; i < path.length; i++) { const d = Math.hypot(path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1]); segs.push(d); tot += d; }
    if (I > 1e-6) {
      p.noStroke(); p.fill(...CUR);
      for (let q = (phase % 26 + 26) % 26; q < tot; q += 26) {
        let r = q, i = 0; while (i < segs.length - 1 && r > segs[i]) { r -= segs[i]; i++; }
        const f = r / segs[i], x = path[i][0] + (path[i + 1][0] - path[i][0]) * f, y = path[i][1] + (path[i + 1][1] - path[i][1]) * f;
        if (y >= B - 1 && x > xa - 4 && x < xb + 4) continue;          // the component draws its own inside
        p.circle(X(x), Y(y), 7 * sk);
      }
    }
    // the adjustable source: long plate (+) above, short plate (−) below, an arrow across
    p.noStroke(); p.fill(...INKC);
    p.rect(X(Lx - 20), Y(188), 40 * G.s, 4 * G.s); p.rect(X(Lx - 10), Y(203), 20 * G.s, 6 * G.s);
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(X(Lx - 22), Y(222), X(Lx + 18), Y(176));
    p.noStroke(); p.triangle(X(Lx + 24), Y(169), X(Lx + 11), Y(176), X(Lx + 19), Y(183));
    lab('$+$', X(Lx - 26), Y(190) + fs * 0.35, 'r');
    lab('$-$', X(Lx - 26), Y(212) + fs * 0.35, 'r');
    // current arrow on the right side
    p.noStroke(); p.fill(...CUR);
    p.triangle(X(Rx), Y(214), X(Rx - 8), Y(196), X(Rx + 8), Y(196));
    lab('$I$', X(Rx + 12), Y(205) + fs * 0.35, 'l', CUR);
    // ammeter on the top wire, its display above
    meter(cx, T, '$\\text{A}$');
    lab(__('lbl_i', { i: tx(I, 3) }), X(cx), Y(T - 34) + fs * 0.35, 'c', INKC, true);
    // the component
    if (P.comp === 'vastus') {
      p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(X(xa), Y(B - 11), 60 * G.s, 22 * G.s);
    } else if (P.comp === 'lamppu') {
      const b = Math.min(1, P.U * I / 0.75);                            // brightness by power, full at 3,0 V
      p.noStroke();
      for (let r = 4; r >= 1; r--) { p.fill(...HEATL, 70 * b); p.circle(X(cx), Y(B), (20 + 5 * r * b) * 2 * G.s); }
      p.fill(255 - 20 * b, 255 - 70 * b, 255 - 150 * b); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(X(cx), Y(B), 40 * G.s);
      p.stroke(...(b > 0.05 ? LAMPC : INKC)); p.strokeWeight(2.5 * sk);
      const d = 14.1;
      p.line(X(cx - d), Y(B - d), X(cx + d), Y(B + d)); p.line(X(cx - d), Y(B + d), X(cx + d), Y(B - d));
    } else {
      const th = (3 + 12 * P.A) * G.s;                                  // thickness grows with the cross-section
      p.noStroke(); p.fill(...METAL);
      p.rect(X(xa) - 5 * G.s, Y(B) - 8 * G.s, 10 * G.s, 16 * G.s, 2); p.rect(X(xb) - 5 * G.s, Y(B) - 8 * G.s, 10 * G.s, 16 * G.s, 2);
      p.stroke(...WIREC); p.strokeWeight(th); p.strokeCap(p.SQUARE); p.line(X(xa), Y(B), X(xb), Y(B)); p.strokeCap(p.ROUND);
      if (I > 1e-6) {                                                   // the charges inside the wire too
        p.noStroke(); p.fill(...CUR);
        for (let q = (phase % 26 + 26) % 26; q < xb - xa; q += 26) p.circle(X(xb - q), Y(B), 6 * sk);
      }
    }
    // voltmeter across the component, with its leads
    const VY = 212, VL = 96, VR = 210;
    p.noStroke(); p.fill(...INKC); p.circle(X(xa), Y(B), 8 * sk); p.circle(X(xb), Y(B), 8 * sk);
    wire([[xa, B], [xa, 262], [VL, 262], [VL, VY], [cx - 18, VY]], 2);
    wire([[xb, B], [xb, 262], [VR, 262], [VR, VY], [cx + 18, VY]], 2);
    meter(cx, VY, '$\\text{V}$');
    lab(__('lbl_u', { u: tx(P.U, 2) }), X(cx), Y(VY - 34) + fs * 0.35, 'c', INKC, true);
    lab(__('c_' + P.comp), X(cx), Y(B + 38) + fs * 0.35, 'c');
    if (P.comp === 'lanka') lab(__('lbl_mitat', { l: tx(P.l, 2), a: tx(P.A, 2) }), X(cx), Y(B + 38) + fs * 1.75, 'c');
    p.stroke(220); p.strokeWeight(1);
    if (G.sep === 'v') p.line(300, 8, 300, 392); else p.line(8, G.gy1 - 60, 592, G.gy1 - 60);
  }
  function meter(cx, cy, letter) {
    p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(X(cx), Y(cy), 36 * G.s);
    lab(letter, X(cx), Y(cy) + fs * 0.35, 'c');
  }

  // ---- the (I, U) graph ----
  function graph(P, I) {
    const wireMode = P.comp === 'lanka';
    const Imax = wireMode ? 5 : 0.35, Umax = 3.5;
    const { gx0, gy0, gx1, gy1 } = G;
    const GX = (i) => gx0 + i / Imax * (gx1 - gx0), GY = (u) => gy0 - u / Umax * (gy0 - gy1);
    const xstep = wireMode ? 0.5 : 0.05, nx = Math.round(Imax / xstep);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let j = 1; j <= nx; j++) p.line(GX(j * xstep), gy0, GX(j * xstep), gy1);
    for (let j = 1; j <= 7; j++) p.line(gx0, GY(j * 0.5), gx1, GY(j * 0.5));
    // axes with arrowheads
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(gx0, gy0, gx1 + 16 * sk, gy0); p.line(gx0, gy0, gx0, gy1 - 16 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, gy0, gx1 + 14 * sk, gy0 - 6 * sk, gx1 + 14 * sk, gy0 + 6 * sk);
    p.triangle(gx0, gy1 - 28 * sk, gx0 - 6 * sk, gy1 - 14 * sk, gx0 + 6 * sk, gy1 - 14 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let j = 1; j <= nx; j++) p.line(GX(j * xstep), gy0, GX(j * xstep), gy0 + 6 * sk);
    for (let j = 1; j <= 7; j++) p.line(gx0 - 6 * sk, GY(j * 0.5), gx0, GY(j * 0.5));
    for (let u = 1; u <= 3; u++) lab('$' + u + '$', gx0 - 10 * sk, GY(u) + fs * 0.35, 'r');
    const xl = wireMode ? [1, 2, 3, 4, 5] : [0.1, 0.2, 0.3];
    for (const v of xl) lab('$' + tx(v, wireMode ? 0 : 1) + '$', GX(v), gy0 + 8 * sk + fs, 'c');
    lab('$0$', gx0 - 8 * sk, gy0 + 8 * sk + fs, 'r');
    lab('$I\\ (\\text{A})$', gx1 + 28 * sk, gy0 - 10 * sk, 'r');
    lab('$U\\ (\\text{V})$', gx0 + 12 * sk, gy1 - 22 * sk + fs * 0.35, 'l');
    // the component's characteristic, faint
    p.noFill(); p.stroke(...(P.comp === 'lamppu' ? LAMPC : INKC), 70); p.strokeWeight(3 * sk); p.beginShape();
    for (let j = 0; j <= 60; j++) { const u = 3 * j / 60; const i = u / Rof(P.comp, u, P.l, P.A); p.vertex(GX(Math.min(i, Imax)), GY(u)); }
    p.endShape();
    // the marked points of this component and the present reading
    for (const m of marks) if (m.comp === P.comp && m.I <= Imax) { p.fill(...INKC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(m.I), GY(m.U), 12 * sk); }
    if (I <= Imax) { p.fill(...CUR); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(I), GY(P.U), 15 * sk); }
  }

  // every canvas text: its box pushed to simState.labels (canvas coordinates); bg puts a white box under it
  function lab(s, x, y, align, col, bg) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fs);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fs), G.H - 0.3 * fs);
    if (bg) { p.noStroke(); p.fill(255, 255, 255, 230); p.rect(x0 - 3, y - 0.85 * fs, w + 6, 1.15 * fs, 3); }
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fs, x1: x0 + w, y1: y + 0.25 * fs });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
