// fy6-5 Kirchhoffin lait ja potentiaali virtapiirissä: an ideal source U (no internal resistance), R1 in series with
// R2 and R3 in parallel, ideal wires (no resistance). R23 = 1/(1/R2 + 1/R3), I1 = U / (R1 + R23), U1 = R1 I1,
// U2 = U3 = U - U1 (voltage law), I2 = U2 / R2, I3 = U3 / R3 (and I1 = I2 + I3, current law). Potentials relative
// to the minus pole: A = U; B = C = U - U1; D = E = F = 0. The reference (zero) point is the minus pole F or the
// junction B, so every potential shifts by the same amount. A voltmeter's black lead sits on the reference point and
// its red lead on the chosen point: it shows that point's potential. Wires are tinted by their potential (darker blue
// = higher), the currents are violet arrows (#7048e8). Below: the potential graph of the loop F -> source -> A -> R1 -> B -> R2
// -> E -> F, the probe's level dashed. Static picture, no animation. Every canvas text goes through lab(), which
// pushes its box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], POTC = [25, 113, 194], POTL = [208, 230, 251],
        CURC = [112, 72, 232], GLASSC = [238, 245, 249], ALU = [196, 204, 212], HOTC = [201, 42, 42];
  const XW = { S: 60, A: 100, R1: 172, B: 245, J: 300, C: 450, M: 548 },
        XN = { S: 50, A: 95, R1: 172, B: 250, J: 305, C: 430, M: 305 };   // phone: the meter sits under the circuit
  const WIDE = { H: 400, top: 62, bot: 196, letTop: 50, potTop: 32, letBot: 214, potBot: 230, picH: 244,
                 ox: 70, oy: 360, gx1: 540, gy1: 274, glab: 386 };
  // phone: letters and potentials beside their points, the voltmeter and its reading under the circuit, its leads
  // drawn as right-angled wires in lanes that no label occupies (below the labels, up the right edge, over the top)
  const NARROW = { H: 966, top: 142, bot: 410, letTop: 121, potTop: 70, letBot: 453, potBot: 496, picH: 642, my: 549,
                   ox: 112, oy: 892, gx1: 500, gy1: 714, glab: 944 };   // the plot ends early: "kohta" sits past its end
  let X = XW, G = WIDE, sk = 1, fh = 13, narrow = false, labels = [], leads = [];
  let slU, slR1, slR2, slR3, selP, selG, lU, lR1, lR2, lR3, readout;
  const POINTS = ['A', 'B', 'C', 'D', 'E', 'F'];

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const mk = (min, max, v, st) => { const l = p.createElement('label').parent(controls); const s = p.createSpan('').parent(l); return [s, p.createSlider(min, max, v, st).parent(l)]; };
    [lU, slU] = mk(1, 12, 9, 0.5);
    [lR1, slR1] = mk(5, 100, 10, 5);
    [lR2, slR2] = mk(10, 120, 30, 5);
    [lR3, slR3] = mk(10, 120, 60, 5);
    const l5 = p.createElement('label').parent(controls); p.createSpan(__('mittauskohta')).parent(l5); selP = p.createSelect().parent(l5);
    for (const k of POINTS) selP.option(__('kohta' + k), k);
    selP.selected('A');
    const l6 = p.createElement('label').parent(controls); p.createSpan(__('nollakohta')).parent(l6); selG = p.createSelect().parent(l6);
    selG.option(__('nollaF'), 'F'); selG.option(__('nollaB'), 'B'); selG.selected('F');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { U: { input: slU.elt, unit: 'V' }, R1: { input: slR1.elt, unit: 'Ω' }, R2: { input: slR2.elt, unit: 'Ω' },
                R3: { input: slR3.elt, unit: 'Ω' }, probe: { input: selP.elt, unit: '' }, ground: { input: selG.elt, unit: '' } },
      reset: () => { slU.value(9); slR1.value(10); slR2.value(30); slR3.value(60); selP.selected('A'); selG.selected('F'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function solve() {
    const U = Number(slU.value()), R1 = Number(slR1.value()), R2 = Number(slR2.value()), R3 = Number(slR3.value());
    const R23 = 1 / (1 / R2 + 1 / R3), I1 = U / (R1 + R23), U1 = R1 * I1, U23 = U - U1;
    const phi = { A: U, B: U23, C: U23, D: 0, E: 0, F: 0 };                 // relative to the minus pole
    const ground = selG.value(), probe = selP.value(), g = phi[ground];
    const V = {}; for (const k of POINTS) V[k] = phi[k] - g;
    return { U, R1, R2, R3, R23, Rkok: R1 + R23, I1, U1, U23, I2: U23 / R2, I3: U23 / R3, V, ground, probe, Vp: V[probe] };
  }

  p.draw = () => {
    const S = solve();
    lU.html(__('jannite', { U: tx(S.U, 1) }));
    lR1.html(__('vastus', { n: '1', R: String(S.R1) }));
    lR2.html(__('vastus', { n: '2', R: String(S.R2) }));
    lR3.html(__('vastus', { n: '3', R: String(S.R3) }));
    const vps = '$V_' + S.probe + ' = ' + tx(S.Vp, 2) + '\\,\\text{V}$';
    readout.html(__('lukemat', { I1: tx(S.I1, 3), I2: tx(S.I2, 3), I3: tx(S.I3, 3), U1: tx(S.U1, 2), U2: tx(S.U23, 2),
                                 Vp: vps, sum: tx(S.U - S.U1 - S.U23, 2) }));
    window.simState = { U: S.U, R1: S.R1, R2: S.R2, R3: S.R3, R23: S.R23, Rkok: S.Rkok, I1: S.I1, I2: S.I2, I3: S.I3,
                        U1: S.U1, U2: S.U23, U3: S.U23, VA: S.V.A, VB: S.V.B, VC: S.V.C, VD: S.V.D, VE: S.V.E, VF: S.V.F,
                        Vp: S.Vp, probe: S.probe, ground: S.ground, sumLoop: S.U - S.U1 - S.U23, labels: null };
    const cw = (p.canvas && p.canvas.parentElement && p.canvas.parentElement.clientWidth) || document.getElementById('sim-root').clientWidth || 600;   // the canvas's box, not the padded root
    narrow = cw < 500; const k = Math.min(2.4, Math.max(1, 600 / cw));   // phone: labels about 14 px, a little less under 250 px
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13; G = narrow ? NARROW : WIDE; X = narrow ? XN : XW;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = []; leads = [];
    p.background(255);
    grect(0, 0, 600, G.picH, [[246, 241, 230], [255, 255, 255]]);
    circuit(S);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.picH, 600, G.picH);
    graph(S);
    window.simState.labels = labels; window.simState.leads = leads;
  };

  // --- the circuit -------------------------------------------------------------------------------------------
  const hi = () => 13, lo = (S) => (S.ground === 'F' ? 0 : -13);
  function tint(v, S) {                       // a wire's colour from its potential: light blue low, dark blue high
    const t = Math.max(0, Math.min(1, (v - lo(S)) / (hi() - lo(S))));
    return POTL.map((c, i) => c + (POTC[i] - c) * t);
  }
  function seg(pts, col) {
    p.noFill(); p.strokeJoin(p.ROUND);
    p.stroke(...INKC); p.strokeWeight(6 * sk); p.beginShape(); for (const [x, y] of pts) p.vertex(x, y); p.endShape();
    p.stroke(...col); p.strokeWeight(3.5 * sk); p.beginShape(); for (const [x, y] of pts) p.vertex(x, y); p.endShape();
  }
  function circuit(S) {
    const { top, bot } = G, mid = (top + bot) / 2, V = S.V;
    const cA = tint(V.A, S), cB = tint(V.B, S), cF = tint(V.F, S);
    const pos = { A: [X.A, top], B: [X.B, top], C: [X.C, top], D: [X.C, bot], E: [X.J, bot], F: [X.A, bot] };
    const mx = X.M, my = narrow ? G.my : mid, r = (narrow ? 15 : 18) * sk;
    if (narrow) {                  // the lead with the longer way takes the outer lane, so the two never cross
      const far = (k) => (pos[k][1] === bot ? Math.abs(pos[k][0] - mx) : 1000 - pos[k][0]), outer = far(S.ground) >= far(S.probe);
      wireLead(mx, my, r, S.ground, pos, false, outer); wireLead(mx, my, r, S.probe, pos, true, !outer);
    }
    else {
      lead(mx - r, my + 6 * sk, pos[S.ground], INKC);                              // the meter's leads behind the circuit
      lead(mx - r, my - 6 * sk, pos[S.probe], HOTC);
    }
    seg([[X.S, mid - 9 * sk], [X.S, top], [X.R1, top]], cA);                       // + pole to R1: potential of A
    seg([[X.R1, top], [X.C, top], [X.C, mid]], cB);                                // R1 to the branches: B and C
    seg([[X.J, top], [X.J, mid]], cB);
    seg([[X.C, mid], [X.C, bot], [X.S, bot], [X.S, mid + 9 * sk]], cF);           // branches back to the - pole
    seg([[X.J, mid], [X.J, bot]], cF);
    // source: long thin plate +, short thick plate -
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.line(X.S - 20 * sk, mid - 9 * sk, X.S + 20 * sk, mid - 9 * sk);
    p.strokeWeight(7 * sk); p.line(X.S - 10 * sk, mid + 9 * sk, X.S + 10 * sk, mid + 9 * sk);
    lab('$+$', X.S - 30 * sk, mid - 12 * sk, 'c'); lab('$-$', X.S - 30 * sk, mid + 22 * sk, 'c');
    lab('$U = ' + tx(S.U, 1) + '\\,\\text{V}$', X.S + 20 * sk, mid + 0.36 * fh + (narrow ? 40 : 14), 'l');
    // resistors
    const rw = 56, rh = 20;
    p.fill(255); p.stroke(...INKC); p.strokeWeight(3 * sk);
    p.rect(X.R1 - rw / 2, top - rh / 2 * sk, rw, rh * sk);
    for (const x of [X.J, X.C]) p.rect(x - rh / 2 * sk, mid - rw / 2, rh * sk, rw);
    lab('$R_1$', X.R1, top + (narrow ? 12 * sk + 4 + 0.95 * fh : 26), 'c');
    lab('$R_2$', X.J + 16 * sk, mid + 0.36 * fh, 'l', INKC, true);
    lab('$R_3$', X.C + 16 * sk, mid + 0.36 * fh, 'l', INKC, true);
    p.noStroke(); p.fill(...INKC); p.circle(X.J, top, 10 * sk); p.circle(X.J, bot, 10 * sk);
    // currents: conventional, from + through R1 and down the branches
    head(124, top, 'r'); head(X.J, bot - 26 * sk, 'd'); head(X.C, bot - 26 * sk, 'd');
    if (narrow) {
      lab('$I_1$', X.S + 14 * sk, top + 12 * sk + 4 + 0.95 * fh, 'l', CURC, true);
      lab('$I_2$', X.J + 16 * sk, bot - 18 * sk, 'l', CURC, true);
      lab('$I_3$', X.C + 16 * sk, bot - 18 * sk, 'l', CURC, true);
    } else {
      lab('$I_1 = ' + tx(S.I1, 2) + '\\,\\text{A}$', 76, top + 44, 'l', CURC, true);
      lab('$I_2 = ' + tx(S.I2, 2) + '\\,\\text{A}$', X.J + 14, bot - 16, 'l', CURC, true);
      lab('$I_3 = ' + tx(S.I3, 2) + '\\,\\text{A}$', X.C + 14, bot - 16, 'l', CURC, true);
    }
    // points with their letters and potentials
    for (const k of POINTS) {
      const [x, y] = pos[k], up = y === top, on = k === S.probe;
      p.fill(on ? [...HOTC] : 255); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(x, y, (on ? 13 : 10) * sk);
      const lx = narrow ? x + 10 * sk : x, al = narrow ? 'l' : 'c';             // phone: beside the point, clear of the leads
      lab('$' + k + '$', lx, up ? G.letTop : G.letBot, al);
      lab('$' + tx(S.V[k], 1) + '\\,\\text{V}$', lx, up ? G.potTop : G.potBot, al, POTC);
    }
    // the reference point: an earth symbol
    const [gx, gy] = pos[S.ground];
    earth(gx, gy);
    // the voltmeter: black lead on the reference point, red lead on the probe
    p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(mx, my, 2 * r);
    lab('$\\text{V}$', mx, my + 0.36 * fh, 'c');
    lab('$V_' + S.probe + ' = ' + tx(S.Vp, 1) + '\\,\\text{V}$', mx, narrow ? my + r + 6 + 0.95 * fh : my - r - 12, 'c');
  }
  function earth(x, y) {        // three shortening bars under a short stem, on the side away from the circuit
    const d = y === G.top ? -1 : 1, s0 = y + d * 10 * sk;
    const ex = !narrow ? x - 18 * sk : d > 0 ? X.S : 390;    // phone: on the same wire, away from the labels and the black lead
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ex, y, ex, s0);
    for (let i = 0; i < 3; i++) { const w = (11 - 4 * i) * sk, yy = s0 + d * 4 * i * sk; p.line(ex - w, yy, ex + w, yy); }
  }
  function lead(x0, y0, [x1, y1], col) {
    p.noFill(); p.stroke(...col, 150); p.strokeWeight(2.5 * sk);
    p.bezier(x0, y0, x0 - 40 * sk, y0, x1 + 40 * sk, y1 + (y1 < y0 ? -30 : 30) * sk, x1, y1);
  }
  // phone: a lead as a right-angled wire from the meter's side; a top point is reached round the right edge and from above
  function wireLead(mx, my, r, k, pos, red, outer) {
    const [px, py] = pos[k], o = 8 * sk, y0 = my + (outer ? o : -o), x = px + (red ? 3 : -3) * sk;
    const side = (dir) => mx + dir * Math.sqrt(r * r - o * o);
    let pts;
    if (py === G.bot) pts = Math.abs(x - mx) < r ? [[x, my - Math.sqrt(r * r - (x - mx) ** 2)], [x, py]]
                                                 : [[side(Math.sign(x - mx)), y0], [x, y0], [x, py]];
    else { const xr = outer ? 590 : 574, yl = outer ? 16 : 30; pts = [[side(1), y0], [xr, y0], [xr, yl], [x, yl], [x, py]]; }
    p.noFill(); p.stroke(...(red ? HOTC : INKC), red ? 190 : 170); p.strokeWeight(2.5 * sk); p.strokeJoin(p.ROUND);
    p.beginShape(); for (const [a, b] of pts) p.vertex(a, b); p.endShape();
    leads.push(pts);
  }
  function head(x, y, d) {
    const s = 8 * sk; p.noStroke(); p.fill(...CURC);
    if (d === 'r') p.triangle(x + s, y, x - s, y - 0.8 * s, x - s, y + 0.8 * s);
    else p.triangle(x, y + s, x - 0.8 * s, y - s, x + 0.8 * s, y - s);
  }

  // --- the potential graph of the loop F -> A -> R1 -> B -> R2 -> E -> F ------------------------------------------
  function graph(S) {
    const { ox, oy, gx1, gy1 } = G, L = lo(S), Hh = hi();
    const GX = (s) => ox + s / 9 * (gx1 - ox), GY = (v) => oy - (v - L) / (Hh - L) * (oy - gy1);
    const step = (S.ground === 'F' ? 3 : 6) * (narrow ? 2 : 1);
    p.fill(...GLASSC); p.noStroke();
    for (const [a, b] of [[3, 4], [6, 7]]) p.rect(GX(a), gy1, GX(b) - GX(a), oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let v = Math.ceil(L / step) * step; v <= 12; v += step) if (v !== L) p.line(ox, GY(v), gx1, GY(v));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 16 * sk, oy); p.line(ox, oy, ox, gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, oy, gx1 + 14 * sk, oy - 6 * sk, gx1 + 14 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 26 * sk, ox - 6 * sk, gy1 - 12 * sk, ox + 6 * sk, gy1 - 12 * sk);
    for (let v = Math.ceil(L / step) * step; v <= 12; v += step) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(v), ox, GY(v));
      lab('$' + String(v) + '$', ox - 9 * sk, GY(v) + 0.36 * fh, 'r');
    }
    if (L < 0) { p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.line(ox, GY(0), gx1, GY(0)); }
    lab('$V\\,(\\text{V})$', ox + 12 * sk, gy1 - 14 * sk, 'l');
    lab('$\\text{kohta}$', 598, oy - 10 * sk, 'r');
    const V = S.V, path = [[0, V.F], [1, V.F], [1, V.A], [3, V.A], [4, V.B], [6, V.B], [7, V.E], [9, V.F]];
    p.noFill(); p.stroke(...POTC); p.strokeWeight(3 * sk); p.beginShape();
    for (const [s, v] of path) p.vertex(GX(s), GY(v)); p.endShape();
    const at = { F: 0, A: 2, B: 5, C: 5, D: 8, E: 8 };
    for (const [s, k] of [[0, 'F'], [2, 'A'], [5, 'B'], [8, 'E'], [9, 'F']]) {
      p.fill(...POTC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(s), GY(V[k]), 10 * sk);
      lab('$' + k + '$', GX(s), G.glab, 'c');
    }
    for (const [s, t] of [[1, 'U'], [3.5, 'R_1'], [6.5, 'R_2']]) lab('$' + t + '$', GX(s), G.glab, 'c', MUTEDC);
    // the probe's level, dashed, and its point ringed
    const y = GY(S.Vp), x = GX(at[S.probe]);
    p.stroke(...HOTC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 5 * sk]);
    p.line(ox, y, gx1, y); p.drawingContext.setLineDash([]);
    p.noFill(); p.stroke(...HOTC); p.strokeWeight(2.5 * sk); p.circle(x, y, 22 * sk);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col, bg) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    if (bg) { p.noStroke(); p.fill(255, 255, 255, 225); p.rect(x0 - 3, y - 0.85 * fh, w + 6, 1.15 * fh, 3); }
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
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
