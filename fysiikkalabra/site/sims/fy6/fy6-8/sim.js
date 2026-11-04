// fy6-8 Lähdejännite ja sisäinen resistanssi: a battery drawn as its model (an ideal source E in series with the internal
// resistance R_s inside a dashed outline), a switch, an ammeter and an adjustable load R in the loop, a voltmeter across
// the battery's terminals. The battery is new (E = 1,60 V, R_s = 0,20 Ω) or used (E = 1,45 V, R_s = 1,2 Ω); one cell,
// two in series (2E, 2R_s) or two in parallel (E, R_s/2). The meters show U and I only; E and R_s are not displayed, so
// the student finds them from the (I, U) graph. Model (lessons/FY6/fy6-8/lesson-answers.py): I = E / (R + R_s) with the
// switch closed, 0 open; U = E − R_s I. Ideal meters and wires. The right (or lower) panel is the (I, U) graph: the points
// the student marks for the present battery and connection, the line fitted to them (least squares, dashed, extended to
// the axes) and the present reading. The internal resistors glow with the power R_s I² of each cell. Moving dots show the
// conventional current (+ to −) in the external circuit; their speed grows with I and the speed select changes only their
// pace. Every canvas text goes through lab(), which pushes its box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const BAT = { uusi: { E: 1.60, Rs: 0.20 }, kaytetty: { E: 1.45, Rs: 1.2 } };
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], CUR = [112, 72, 232], POT = [25, 113, 194];
  const HEATC = [232, 89, 12], HEATL = [255, 192, 120], GLASSC = [238, 245, 249];
  // the circuit is drawn in its own 300 × 400 units, scaled by s and moved by (ox, oy); the graph has its own box
  const WIDE = { H: 400, s: 1, ox: 0, oy: 0, gx0: 352, gy0: 330, gx1: 548, gy1: 84, sep: 'v' };
  const NARROW = { H: 1040, s: 1.75, ox: 37, oy: -20, gx0: 110, gy0: 964, gx1: 520, gy1: 716, sep: 'h' };
  let G = WIDE, narrow = false, sk = 1, fs = 13, labels = [];
  let btnMark, btnClear, selBat, selCells, selSwitch, slR, selSpeed, lR, readout;
  let marks = [], phase = 0;

  const params = () => ({ bat: selBat.value(), cells: selCells.value(), sw: selSwitch.value(), R: Number(slR.value()) });
  // the source voltage and internal resistance of the battery group
  function group(bat, cells) {
    const b = BAT[bat];
    return cells === 'sarja' ? { E: 2 * b.E, Rs: 2 * b.Rs } : cells === 'rinnan' ? { E: b.E, Rs: b.Rs / 2 } : { E: b.E, Rs: b.Rs };
  }
  function solve(P) {
    const g = group(P.bat, P.cells);
    const I = P.sw === 'kiinni' ? g.E / (P.R + g.Rs) : 0;
    return { E: g.E, Rs: g.Rs, I, U: g.E - g.Rs * I };
  }
  // least-squares line U = a + b I through the marked points of this battery and connection (null if under two currents)
  function fit(pts) {
    if (pts.length < 2) return null;
    const n = pts.length, sx = pts.reduce((s, m) => s + m.I, 0), sy = pts.reduce((s, m) => s + m.U, 0);
    const sxx = pts.reduce((s, m) => s + m.I * m.I, 0), sxy = pts.reduce((s, m) => s + m.I * m.U, 0), d = n * sxx - sx * sx;
    if (Math.abs(d) < 1e-9) return null;
    const b = (n * sxy - sx * sy) / d;
    return { a: (sy - b * sx) / n, b };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnMark = p.createButton(__('merkitse')).parent(controls);
    btnMark.elt.addEventListener('click', () => { const P = params(), S = solve(P); marks.push({ key: P.bat + '|' + P.cells, I: S.I, U: S.U }); });
    btnClear = p.createButton(__('tyhjenna')).parent(controls);
    btnClear.elt.addEventListener('click', () => { marks = []; });
    const lb = p.createElement('label').parent(controls); p.createSpan(__('paristo')).parent(lb); selBat = p.createSelect().parent(lb);
    selBat.option(__('uusi'), 'uusi'); selBat.option(__('kaytetty'), 'kaytetty'); selBat.selected('uusi');
    const lc = p.createElement('label').parent(controls); p.createSpan(__('kennot')).parent(lc); selCells = p.createSelect().parent(lc);
    selCells.option(__('yksi'), 'yksi'); selCells.option(__('sarja'), 'sarja'); selCells.option(__('rinnan'), 'rinnan'); selCells.selected('yksi');
    const lk = p.createElement('label').parent(controls); p.createSpan(__('kytkin')).parent(lk); selSwitch = p.createSelect().parent(lk);
    selSwitch.option(__('auki'), 'auki'); selSwitch.option(__('kiinni'), 'kiinni'); selSwitch.selected('kiinni');
    const l1 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l1); slR = p.createSlider(0.5, 10, 2, 0.5).parent(l1);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.4'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { paristo: { input: selBat.elt }, kennot: { input: selCells.elt }, kytkin: { input: selSwitch.elt }, R: { input: slR.elt, unit: 'Ω' } },
      reset: () => { selBat.selected('uusi'); selCells.selected('yksi'); selSwitch.selected('kiinni'); slR.value(2); marks = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = params(), S = solve(P), key = P.bat + '|' + P.cells;
    phase += Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()) * 140 * S.I / (S.I + 0.5);   // dot speed grows with I
    lR.html(__('kuorma', { r: tx(P.R, 1) }));
    readout.html(__('lukemat', { u: tx(S.U, 3), i: tx(S.I, 3) }));
    const mine = marks.filter((m) => m.key === key), F = fit(mine);
    const nCells = P.cells === 'yksi' ? 1 : 2, Icell = P.cells === 'rinnan' ? S.I / 2 : S.I, RsCell = BAT[P.bat].Rs;
    window.simState = { paristo: P.bat, kennot: P.cells, kytkin: P.sw, R: P.R, E: S.E, Rs: S.Rs, I: S.I, U: S.U, Ik: S.E / S.Rs,
      Pin: S.Rs * S.I * S.I, P: S.U * S.I, Pcell: RsCell * Icell * Icell, cells: nCells, marks: marks.length, shown: mine.length,
      fitE: F ? F.a : null, fitRs: F ? -F.b : null, speed: Number(selSpeed.value()), narrow, labels: null };
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
    circuit(P, S, Icell, RsCell);
    graph(P, S, mine, F);
    window.simState.labels = labels;
  };

  // ---- the circuit ----
  const X = (x) => G.ox + x * G.s, Y = (y) => G.oy + y * G.s;
  const LX = 80, RX = 262, T = 62, B = 356, BT = 96, BB = 326, VX = 176, VY = 211, AX = 215, LOADY = 252, SWY = 128;
  function wire(pts, w) {
    p.noFill(); p.stroke(...INKC); p.strokeWeight((w || 2.5) * sk); p.beginShape();
    for (const [x, y] of pts) p.vertex(X(x), Y(y));
    p.endShape();
  }
  function plates(x, y) {                                   // long thin plate (+) above, short thick (−) below
    p.noStroke(); p.fill(...INKC);
    p.rect(X(x - 16), Y(y - 6), 32 * G.s, 3 * G.s); p.rect(X(x - 8), Y(y + 3), 16 * G.s, 6 * G.s);
  }
  function rs(x, y, h, glow) {                              // an internal resistance, glowing with its power
    if (glow > 0.01) {
      p.noStroke();
      for (let r = 3; r >= 1; r--) { p.fill(...HEATL, 60 * glow); p.rect(X(x - 9 - 4 * r), Y(y - h / 2 - 4 * r), (18 + 8 * r) * G.s, (h + 8 * r) * G.s, 6); }
    }
    p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    p.fill(255 - 23 * glow, 255 - 63 * glow, 255 - 135 * glow);
    p.rect(X(x - 9), Y(y - h / 2), 18 * G.s, h * G.s);
  }
  function circuit(P, S, Icell, RsCell) {
    const glow = Math.min(1, RsCell * Icell * Icell / 1.5);
    // the battery outline
    p.fill(...GLASSC); p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk);
    p.drawingContext.setLineDash([6 * sk, 5 * sk]); p.rect(X(24), Y(BT), 112 * G.s, (BB - BT) * G.s, 8); p.drawingContext.setLineDash([]);
    if (P.cells === 'rinnan') {
      const xl = 52, xr = 108;
      wire([[LX, BT], [LX, 112]]); wire([[xl, 150], [xl, 112], [xr, 112], [xr, 150]]);
      wire([[xl, 162], [xl, 218]]); wire([[xr, 162], [xr, 218]]);
      wire([[xl, 262], [xl, 300], [xr, 300], [xr, 262]]); wire([[LX, 300], [LX, BB]]);
      plates(xl, 156); plates(xr, 156); rs(xl, 240, 44, glow); rs(xr, 240, 44, glow);
      p.noStroke(); p.fill(...INKC); p.circle(X(LX), Y(112), 7 * sk); p.circle(X(LX), Y(300), 7 * sk);
      lab('$E$', X(20), Y(156) + fs * 0.35, 'r'); lab('$R_\\text{s}$', X(20), Y(240) + fs * 0.35, 'r');
    } else if (P.cells === 'sarja') {
      wire([[LX, BT], [LX, 122]]); wire([[LX, 134], [LX, 150]]); wire([[LX, 186], [LX, 224]]); wire([[LX, 236], [LX, 252]]); wire([[LX, 288], [LX, BB]]);
      plates(LX, 128); rs(LX, 168, 36, glow); plates(LX, 230); rs(LX, 270, 36, glow);
      for (const y of [128, 230]) lab('$E$', X(LX + 24), Y(y) + fs * 0.35, 'l');
      for (const y of [168, 270]) lab('$R_\\text{s}$', X(LX + 16), Y(y) + fs * 0.35, 'l');
    } else {
      wire([[LX, BT], [LX, 150]]); wire([[LX, 162], [LX, 208]]); wire([[LX, 252], [LX, BB]]);
      plates(LX, 156); rs(LX, 230, 44, glow);
      lab('$E$', X(LX + 24), Y(156) + fs * 0.35, 'l');
      lab('$R_\\text{s}$', X(LX + 16), Y(230) + fs * 0.35, 'l');
    }
    lab(__('c_paristo'), X(LX + 12), Y(BB + 15) + fs * 0.35, 'l', MUTEDC);
    // the external loop with the switch on the right side
    const closed = P.sw === 'kiinni';
    wire([[LX, BT], [LX, T], [RX, T], [RX, SWY - 20]]);
    wire([[RX, SWY + 20], [RX, B], [LX, B], [LX, BB]]);
    p.noStroke(); p.fill(...INKC); p.circle(X(RX), Y(SWY - 20), 7 * sk); p.circle(X(RX), Y(SWY + 20), 7 * sk);
    p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    if (closed) p.line(X(RX), Y(SWY + 20), X(RX), Y(SWY - 20)); else p.line(X(RX), Y(SWY + 20), X(RX - 24), Y(SWY - 12));
    // terminals
    for (const y of [BT, BB]) { p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(X(LX), Y(y), 10 * sk); }
    lab('$+$', X(LX - 10), Y(BT - 12) + fs * 0.35, 'r');
    lab('$-$', X(LX - 10), Y(BB + 14) + fs * 0.35, 'r');
    // moving charges in the external circuit, + round to −
    if (S.I > 1e-6) {
      const path = [[LX, BT], [LX, T], [RX, T], [RX, B], [LX, B], [LX, BB]];
      const segs = []; let tot = 0;
      for (let i = 1; i < path.length; i++) { const d = Math.hypot(path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1]); segs.push(d); tot += d; }
      p.noStroke(); p.fill(...CUR);
      for (let q = (phase % 26 + 26) % 26; q < tot; q += 26) {
        let r = q, i = 0; while (i < segs.length - 1 && r > segs[i]) { r -= segs[i]; i++; }
        const f = r / segs[i], x = path[i][0] + (path[i + 1][0] - path[i][0]) * f, y = path[i][1] + (path[i + 1][1] - path[i][1]) * f;
        if (y < T + 2 && Math.abs(x - AX) < 22) continue;                    // inside the ammeter
        if (x > RX - 2 && Math.abs(y - LOADY) < 34) continue;                // inside the load
        p.circle(X(x), Y(y), 7 * sk);
      }
      p.fill(...CUR); p.triangle(X(RX), Y(196), X(RX - 8), Y(178), X(RX + 8), Y(178));
    }
    // the load: an adjustable resistor (a rectangle crossed by an arrow)
    p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(X(RX - 11), Y(LOADY - 30), 22 * G.s, 60 * G.s);
    p.strokeWeight(2 * sk); p.line(X(RX - 22), Y(LOADY + 30), X(RX + 16), Y(LOADY - 28));
    p.noStroke(); p.fill(...INKC); p.triangle(X(RX + 21), Y(LOADY - 36), X(RX + 9), Y(LOADY - 30), X(RX + 17), Y(LOADY - 22));
    lab(__('lbl_r', { r: tx(P.R, 1) }), X(RX - 16), Y(LOADY + 52) + fs * 0.35, 'r');
    // the ammeter on the top wire and the voltmeter across the terminals
    meter(AX, T, '$\\text{A}$');
    lab(__('lbl_i', { i: tx(S.I, 3) }), X(AX), Y(T - 34) + fs * 0.35, 'c', INKC, true);
    p.noStroke(); p.fill(...INKC); p.circle(X(VX), Y(T), 8 * sk); p.circle(X(VX), Y(B), 8 * sk);
    wire([[VX, T], [VX, VY - 18]], 2); wire([[VX, VY + 18], [VX, B]], 2);
    meter(VX, VY, '$\\text{V}$');
    lab(__('lbl_u', { u: tx(S.U, 3) }), X(VX), Y(VY - 38) + fs * 0.35, 'c', POT, true);
    p.stroke(220); p.strokeWeight(1);
    if (G.sep === 'v') p.line(300, 8, 300, 392); else p.line(8, G.gy1 - 60, 592, G.gy1 - 60);
  }
  function meter(cx, cy, letter) {
    p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(X(cx), Y(cy), 36 * G.s);
    lab(letter, X(cx), Y(cy) + fs * 0.35, 'c');
  }

  // ---- the (I, U) graph ----
  function graph(P, S, mine, F) {
    const Imax = 4, Umax = P.cells === 'sarja' ? 4 : 2, ustep = Umax / 8;
    const { gx0, gy0, gx1, gy1 } = G;
    const GX = (i) => gx0 + i / Imax * (gx1 - gx0), GY = (u) => gy0 - u / Umax * (gy0 - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let j = 1; j <= 8; j++) p.line(GX(j * 0.5), gy0, GX(j * 0.5), gy1);
    for (let j = 1; j <= 8; j++) p.line(gx0, GY(j * ustep), gx1, GY(j * ustep));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(gx0, gy0, gx1 + 16 * sk, gy0); p.line(gx0, gy0, gx0, gy1 - 16 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, gy0, gx1 + 14 * sk, gy0 - 6 * sk, gx1 + 14 * sk, gy0 + 6 * sk);
    p.triangle(gx0, gy1 - 28 * sk, gx0 - 6 * sk, gy1 - 14 * sk, gx0 + 6 * sk, gy1 - 14 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let j = 1; j <= 8; j++) p.line(GX(j * 0.5), gy0, GX(j * 0.5), gy0 + 6 * sk);
    for (let j = 1; j <= 8; j++) p.line(gx0 - 6 * sk, GY(j * ustep), gx0, GY(j * ustep));
    for (let j = 2; j <= 8; j += 2) lab('$' + tx(j * ustep, Umax === 2 ? 1 : 0) + '$', gx0 - 10 * sk, GY(j * ustep) + fs * 0.35, 'r');
    for (let v = 1; v <= 4; v++) lab('$' + v + '$', GX(v), gy0 + 8 * sk + fs, 'c');
    lab('$0$', gx0 - 8 * sk, gy0 + 8 * sk + fs, 'r');
    lab('$I\\ (\\text{A})$', gx1 + 28 * sk, gy0 - 10 * sk, 'r');
    lab('$U\\ (\\text{V})$', gx0 + 12 * sk, gy1 - 22 * sk + fs * 0.35, 'l');
    // the fitted line, dashed, from the U axis to the I axis or the edge of the plot
    if (F) {
      const iEnd = F.b < 0 ? Math.min(Imax, -F.a / F.b) : Imax;
      const u0 = Math.min(Umax, F.a), i0 = F.a > Umax && F.b < 0 ? (Umax - F.a) / F.b : 0;
      p.stroke(...POT, 200); p.strokeWeight(2.5 * sk); p.drawingContext.setLineDash([8 * sk, 6 * sk]);
      p.line(GX(i0), GY(u0), GX(iEnd), GY(Math.max(0, Math.min(Umax, F.a + F.b * iEnd))));
      p.drawingContext.setLineDash([]);
    }
    for (const m of mine) if (m.I <= Imax && m.U <= Umax) { p.fill(...INKC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(m.I), GY(m.U), 12 * sk); }
    if (S.I <= Imax && S.U <= Umax) { p.fill(...CUR); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(S.I), GY(S.U), 15 * sk); }
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
