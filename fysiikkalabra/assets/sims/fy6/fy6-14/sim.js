// fy6-14 Puolijohteet, diodi, LED ja aurinkokenno. Two circuits, chosen with the first select:
// 1) LED-piiri: a source U (0–9 V) in series with a resistor R (100–1000 Ω) and a silicon diode, a red LED or a blue LED,
//    forward (päästösuunta) or reverse (estosuunta). Forward: I = I_s (exp(U_D / m) − 1) with I_s chosen so that the
//    current is 10 mA at U_ref (Si 0,70 V, m 0,040 V; red 1,90 V, 0,050 V; blue 2,90 V, 0,060 V); the operating point
//    solves U = U_D + R I by bisection. Reverse: I = 0 (leakage ignored), so U_D = −U and U_R = 0. An LED over 20 mA is
//    overloaded (a warning). The graph is the component's (U, I) characteristic with the operating point.
// 2) Aurinkokenno: a small panel of 10 cells in series, I = I_L − I_0 (exp(U / m) − 1), m = 0,40 V, I_L = 0,200 A · G /
//    (1000 W/m²), I_0 such that the open-circuit voltage is 6,0 V at 1000 W/m², with a load resistor R (0–300 Ω): the
//    point solves U = R I. The graph is the panel's (U, I) curve with the point and the rectangle U·I whose area is the
//    power. The same models as lessons/FY6/fy6-14/lesson-answers.py. A static picture (no animation, no speed control).
// Every canvas text goes through lab(), which pushes its box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], CUR = [112, 72, 232], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], ALU = [196, 204, 212], WHITE = [255, 255, 255], CELL = [47, 116, 181], CELLD = [31, 41, 81];
  const COMP = { piidiodi: { ur: 0.70, m: 0.040, led: null }, punainen: { ur: 1.90, m: 0.050, led: [240, 62, 62] },
                 sininen: { ur: 2.90, m: 0.060, led: [77, 171, 247] } };
  const IMAX_LED = 20;                                              // mA, the LEDs' largest recommended current
  const M_PV = 0.40, ISC = 0.200, UOC = 6.0, I0 = ISC / (Math.exp(UOC / M_PV) - 1);
  // wide: the picture left (design box 330 × 400), the graph right; phone: stacked, the picture scaled by 1,6
  const WIDE = { H: 400, s: 1, px: 0, py: 0, picW: 330, picH: 400, ox: 384, oy: 336, gx1: 552, gy1: 62 };
  const NARROW = { H: 1100, s: 1.6, px: 36, py: 0, picW: 600, picH: 640, ox: 116, oy: 1010, gx1: 540, gy1: 720 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let slU, slR, slG, slK, selP, selC, selS, lU, lR, lG, lK, lC, lS, readout;

  // --- the models ------------------------------------------------------------------------------------------------
  const isOf = (c) => 0.010 / (Math.exp(COMP[c].ur / COMP[c].m) - 1);
  const iLed = (c, u) => (u <= 0 ? 0 : isOf(c) * (Math.exp(u / COMP[c].m) - 1) * 1000);         // mA
  function ledPoint(U, R, c, fwd) {
    if (!fwd || U <= 0) return { UD: fwd ? 0 : -U, I: 0 };
    let lo = 0, hi = U; const Is = isOf(c), m = COMP[c].m;
    for (let k = 0; k < 100; k++) { const mid = (lo + hi) / 2; if (mid + R * Is * (Math.exp(mid / m) - 1) > U) hi = mid; else lo = mid; }
    const UD = (lo + hi) / 2; return { UD, I: (U - UD) / R * 1000 };
  }
  const uOpen = (g) => (g <= 0 ? 0 : M_PV * Math.log(ISC * g / 1000 / I0 + 1));
  const iPv = (g, u) => Math.max(0, ISC * g / 1000 - I0 * (Math.exp(u / M_PV) - 1));             // A
  function pvPoint(g, R) {
    const IL = ISC * g / 1000;
    if (g <= 0) return { U: 0, I: 0 };
    if (R <= 0) return { U: 0, I: IL };
    let lo = 0, hi = uOpen(g);
    for (let k = 0; k < 100; k++) { const mid = (lo + hi) / 2; if (IL - I0 * (Math.exp(mid / M_PV) - 1) - mid / R > 0) lo = mid; else hi = mid; }
    const U = (lo + hi) / 2; return { U, I: U / R };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const sel = (key, opts, def) => {
      const l = p.createElement('label').parent(controls); p.createSpan(__(key)).parent(l); const s = p.createSelect().parent(l);
      for (const o of opts) s.option(__(o), o); s.selected(def); return [l, s];
    };
    const mk = (min, max, v, st) => { const l = p.createElement('label').parent(controls); const s = p.createSpan('').parent(l); return [l, s, p.createSlider(min, max, v, st).parent(l)]; };
    let lP; [lP, selP] = sel('piiri', ['led', 'kenno'], 'led');
    let sU, sR, sG, sK;
    [lU, sU, slU] = mk(0, 9.0, 5.0, 0.1);
    [lR, sR, slR] = mk(100, 1000, 330, 10);
    [lC, selC] = sel('komponentti', ['piidiodi', 'punainen', 'sininen'], 'punainen');
    [lS, selS] = sel('suunta', ['paasto', 'esto'], 'paasto');
    [lG, sG, slG] = mk(0, 1000, 1000, 50);
    [lK, sK, slK] = mk(0, 300, 50, 1);
    lU.span = sU; lR.span = sR; lG.span = sG; lK.span = sK;
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { piiri: { input: selP.elt }, U: { input: slU.elt, unit: 'V' }, R: { input: slR.elt, unit: 'Ω' },
                komponentti: { input: selC.elt }, suunta: { input: selS.elt }, G: { input: slG.elt, unit: 'W/m²' },
                Rk: { input: slK.elt, unit: 'Ω' } },
      reset: () => { selP.selected('led'); slU.value(5.0); slR.value(330); selC.selected('punainen'); selS.selected('paasto'); slG.value(1000); slK.value(50); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function state() {
    const piiri = selP.value(), U = Number(slU.value()), R = Number(slR.value()), c = selC.value(), suunta = selS.value();
    const g = Number(slG.value()), Rk = Number(slK.value());
    const L = ledPoint(U, R, c, suunta === 'paasto'), V = pvPoint(g, Rk);
    const over = COMP[c].led && L.I > IMAX_LED + 1e-9 ? 1 : 0;
    return { piiri, U, R, komponentti: c, suunta, UD: L.UD, UR: R * L.I / 1000,               // U_R = R I (Ohm's law)
             I: L.I, PD: L.UD * L.I, ylikuorma: over, G: g, Rk, Upv: V.U, Ipv: V.I * 1000, Ppv: V.U * V.I,
             Ik: ISC * g / 1000 * 1000, Ut: uOpen(g) };
  }

  p.draw = () => {
    const S = state();
    const ledMode = S.piiri === 'led';
    for (const l of [lU, lR, lC, lS]) l.style('display', ledMode ? '' : 'none');
    for (const l of [lG, lK]) l.style('display', ledMode ? 'none' : '');
    lU.span.html(__('jannite', { U: tx(S.U, 1) }));
    lR.span.html(__('vastus', { R: String(Math.round(S.R)) }));
    lG.span.html(__('valo', { G: String(Math.round(S.G)) }));
    lK.span.html(__('kuorma', { R: String(Math.round(S.Rk)) }));
    if (ledMode) readout.html(__('lukemat-led', { I: sig(S.I), UD: tx(S.UD, Math.abs(S.UD) < 10 ? 2 : 1), UR: tx(S.UR, 2), PD: sig(Math.abs(S.PD)) })
                             + (S.ylikuorma ? '<br><strong>' + __('ylikuorma-teksti') + '</strong>' : ''));
    else readout.html(__('lukemat-kenno', { U: tx(S.Upv, 2), I: String(Math.round(S.Ipv)), P: tx(S.Ppv, 3), Ik: String(Math.round(S.Ik)), Ut: tx(S.Ut, 2) }));
    window.simState = { piiri: S.piiri, U: S.U, R: S.R, komponentti: S.komponentti, suunta: S.suunta, UD: S.UD, UR: S.UR, I: S.I,
                        PD: S.PD, ylikuorma: S.ylikuorma, G: S.G, Rk: S.Rk, Upv: S.Upv, Ipv: S.Ipv, Ppv: S.Ppv, Ik: S.Ik, Ut: S.Ut, labels: null };
    const cw = (p.canvas && p.canvas.parentElement && p.canvas.parentElement.clientWidth) || document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.min(2.4, Math.max(1, 600 / cw));
    G = narrow ? NARROW : WIDE; sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, G.picW, G.picH, [[246, 241, 230], [255, 255, 255]]);
    if (ledMode) ledPicture(S); else pvPicture(S);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, G.picH, 600, G.picH); else p.line(G.picW, 0, G.picW, 400);
    if (ledMode) ledGraph(S); else pvGraph(S);
    window.simState.labels = labels;
  };

  // --- drawing helpers in the picture's design box (330 × 400) -----------------------------------------------------
  const X = (x) => G.px + x * G.s, Y = (y) => G.py + y * G.s, w = (v) => v * G.s;
  function wire(pts) {
    p.noFill(); p.stroke(...INKC); p.strokeWeight(w(3)); p.strokeJoin(p.ROUND);
    p.beginShape(); for (const [x, y] of pts) p.vertex(X(x), Y(y)); p.endShape();
  }
  function head(x, y, dir, col) {                                   // a filled arrowhead on a wire, pointing r l u d
    const s = 9, P = { r: [[s, 0], [-s, -0.8 * s], [-s, 0.8 * s]], l: [[-s, 0], [s, -0.8 * s], [s, 0.8 * s]],
                       d: [[0, s], [-0.8 * s, -s], [0.8 * s, -s]], u: [[0, -s], [-0.8 * s, s], [0.8 * s, s]] }[dir];
    p.noStroke(); p.fill(...(col || CUR)); p.triangle(...P.flatMap(([a, b]) => [X(x + a), Y(y + b)]));
  }
  function resistorH(x, y) { p.fill(255); p.stroke(...INKC); p.strokeWeight(w(3)); p.rect(X(x - 30), Y(y - 12), w(60), w(24)); }
  function resistorV(x, y) { p.fill(255); p.stroke(...INKC); p.strokeWeight(w(3)); p.rect(X(x - 12), Y(y - 30), w(24), w(60)); }
  function source(x, y) {                                           // long thin plate (+) above, short thick (−) below
    p.stroke(...INKC); p.strokeWeight(w(3)); p.line(X(x - 22), Y(y - 6), X(x + 22), Y(y - 6));
    p.strokeWeight(w(7)); p.line(X(x - 11), Y(y + 6), X(x + 11), Y(y + 6));
  }

  // --- the LED circuit -------------------------------------------------------------------------------------------
  function ledPicture(S) {
    const xs = 52, xd = 270, top = 80, bot = 330, yd = 205, fwd = S.suunta === 'paasto', C = COMP[S.komponentti];
    wire([[xs, 199], [xs, top], [xd, top], [xd, yd - 16]]);
    wire([[xd, yd + 16], [xd, bot], [xs, bot], [xs, 211]]);
    source(xs, 205);
    resistorH(160, top);
    // the glow of a lit LED: its brightness grows with the current
    if (C.led && S.I > 0.05) {
      const b = Math.min(1, S.I / IMAX_LED);
      p.noStroke();
      for (let r = 5; r >= 1; r--) { p.fill(...C.led, 34 * b * (6 - r) / 5 + 10 * b); p.circle(X(xd), Y(yd), w(22 + 16 * r * (0.5 + 0.5 * b))); }
    }
    // the diode symbol: a triangle pointing the way the current can go and a bar (cathode)
    const t = fwd ? [[xd - 15, yd - 13], [xd + 15, yd - 13], [xd, yd + 13]] : [[xd - 15, yd + 13], [xd + 15, yd + 13], [xd, yd - 13]];
    p.fill(C.led && S.I > 0.05 ? C.led : [255, 255, 255]); p.stroke(...INKC); p.strokeWeight(w(2.5));
    p.triangle(...t.flatMap(([a, b]) => [X(a), Y(b)]));
    const yb = fwd ? yd + 13 : yd - 13; p.strokeWeight(w(3)); p.line(X(xd - 16), Y(yb), X(xd + 16), Y(yb));
    p.line(X(xd), Y(yd - 16), X(xd), Y(yd - 13)); p.line(X(xd), Y(yd + 13), X(xd), Y(yd + 16));
    if (C.led) for (const dy of [-8, 4]) {                          // the LED's two light arrows
      p.stroke(...INKC); p.strokeWeight(w(2)); p.line(X(xd + 20), Y(yd + dy), X(xd + 34), Y(yd + dy - 12));
      p.noStroke(); p.fill(...INKC); p.triangle(X(xd + 38), Y(yd + dy - 15), X(xd + 29), Y(yd + dy - 12), X(xd + 35), Y(yd + dy - 6));
    }
    // the current (conventional, + to −), only when it flows
    if (S.I > 0.05) { head(105, top, 'r'); head(225, top, 'r'); head(xd, 280, 'd'); head(160, bot, 'l'); lab('$I$', X(105), Y(top - 14), 'c', CUR); }
    lab('$U$', X(xs - 30), Y(205) + 0.36 * fh, 'r');
    lab('$+$', X(xs + 30), Y(186) + 0.36 * fh, 'l');
    lab('$R$', X(160), Y(top - 22), 'c');
    lab('$U_R$', X(160), Y(top + 22) + 0.9 * fh, 'c');
    lab('$U_\\text{D}$', X(xd - 26), Y(yd) + 0.36 * fh, 'r');
    if (S.ylikuorma) lab(__('ylikuorma'), X(165), Y(372), 'c', [201, 42, 42]);
    else if (S.suunta === 'esto') lab(__('estosuunta'), X(165), Y(372), 'c');
  }
  // --- the (U_D, I) graph of the component --------------------------------------------------------------------------
  function ledGraph(S) {
    const { ox, oy, gx1, gy1 } = G, ua = [-2, 4];
    const ymax = nice(Math.max(S.I * 1.3, 10), 4);
    const GX = (u) => ox + (u - ua[0]) / (ua[1] - ua[0]) * (gx1 - ox), GY = (i) => oy - i / ymax.max * (oy - gy1);
    const x0 = GX(0);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let u = ua[0]; u <= ua[1] + 1e-9; u += 1) if (u !== 0) p.line(GX(u), oy, GX(u), gy1);
    for (let i = ymax.s; i <= ymax.max + 1e-9; i += ymax.s) p.line(ox, GY(i), gx1, GY(i));
    // the characteristic: zero in reverse and below the threshold, steep above it
    p.noFill(); p.stroke(...(COMP[S.komponentti].led || INKC)); p.strokeWeight(3 * sk); p.beginShape();
    p.vertex(GX(ua[0]), GY(0));
    for (let u = 0; u <= ua[1] + 1e-9; u += 0.005) { const i = iLed(S.komponentti, u); if (i > ymax.max) { p.vertex(GX(u), GY(ymax.max)); break; } p.vertex(GX(u), GY(i)); }
    p.endShape();
    // axes: the I axis at U = 0
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 14 * sk, oy); p.line(x0, oy, x0, gy1 - 12 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 26 * sk, oy, gx1 + 12 * sk, oy - 6 * sk, gx1 + 12 * sk, oy + 6 * sk);
    p.triangle(x0, gy1 - 24 * sk, x0 - 6 * sk, gy1 - 10 * sk, x0 + 6 * sk, gy1 - 10 * sk);
    for (let u = ua[0]; u <= ua[1] + 1e-9; u += 1) {
      if (u === 0) continue;
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(u), oy, GX(u), oy + 6 * sk);
      lab('$' + (u < 0 ? '-' : '') + Math.abs(u) + '$', GX(u), oy + 8 * sk + 0.9 * fh, 'c');
    }
    const di = Math.max(0, -Math.floor(Math.log10(ymax.s) + 1e-9));
    for (let i = ymax.s; i <= ymax.max + 1e-9; i += ymax.s) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(x0 - 6 * sk, GY(i), x0, GY(i));
      lab('$' + tx(i, di) + '$', x0 - 9 * sk, GY(i) + 0.36 * fh, 'r');
    }
    lab('$0$', x0 - 9 * sk, oy + 8 * sk + 0.9 * fh, 'r');
    lab('$U_\\text{D}\\,(\\text{V})$', 596, oy + 8 * sk + 2.3 * fh, 'r');
    lab('$I\\,(\\text{mA})$', x0 + 12 * sk, gy1 - 12 * sk, 'l');
    // the operating point; in reverse beyond −2 V an arrow at the edge
    const u = Math.max(ua[0], S.UD), off = S.UD < ua[0] - 1e-9;
    p.fill(...CUR); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(u), GY(S.I), 11 * sk);
    if (off) { p.noStroke(); p.fill(...CUR); p.triangle(GX(u) - 16 * sk, GY(0) - 14 * sk, GX(u) - 4 * sk, GY(0) - 20 * sk, GX(u) - 4 * sk, GY(0) - 8 * sk); }
  }

  // --- the solar panel with its load -------------------------------------------------------------------------------
  function pvPicture(S) {
    const g = S.G / 1000, xl = 268, top = 196, bot = 340, xp0 = 30, xp1 = 128, yp0 = 186, yp1 = 350, xv = 196;
    // the sun and its light
    p.noStroke(); p.fill(255, 212, 59, 60 + 195 * g); p.circle(X(66), Y(62), w(52));
    p.stroke(255, 169, 77, 60 + 195 * g); p.strokeWeight(w(4));
    for (let a = 0; a < 8; a++) { const t = a * Math.PI / 4; p.line(X(66 + 34 * Math.cos(t)), Y(62 + 34 * Math.sin(t)), X(66 + 46 * Math.cos(t)), Y(62 + 46 * Math.sin(t))); }
    const nr = Math.round(S.G / 250);
    for (let j = 0; j < nr; j++) { const x = 46 + 22 * j; arrowFill(x + 10, 102, x, 172, HEATC); }
    // the panel: 2 × 5 cells
    p.fill(...CELLD); p.stroke(...INKC); p.strokeWeight(w(3)); p.rect(X(xp0), Y(yp0), w(xp1 - xp0), w(yp1 - yp0), w(4));
    for (let i = 0; i < 2; i++) for (let j = 0; j < 5; j++) {
      p.noStroke(); p.fill(CELL[0] + 60 * g, CELL[1] + 50 * g, CELL[2] + 30 * g); p.rect(X(xp0 + 7 + i * 44), Y(yp0 + 7 + j * 31.5), w(40), w(27), w(2));
      p.stroke(255, 255, 255, 120); p.strokeWeight(w(1)); p.line(X(xp0 + 7 + i * 44 + 20), Y(yp0 + 9 + j * 31.5), X(xp0 + 7 + i * 44 + 20), Y(yp0 + 32 + j * 31.5));
    }
    // wires, the load and the voltmeter
    wire([[xp1, top], [xl, top], [xl, 238]]);
    wire([[xl, 298], [xl, bot], [xp1, bot]]);
    resistorV(xl, 268);
    p.fill(...INKC); p.noStroke(); p.circle(X(xv), Y(top), w(10)); p.circle(X(xv), Y(bot), w(10));
    wire([[xv, top], [xv, 246]]); wire([[xv, 290], [xv, bot]]);
    p.fill(255); p.stroke(...INKC); p.strokeWeight(w(3)); p.circle(X(xv), Y(268), w(40));
    lab('$\\text{V}$', X(xv), Y(268) + 0.36 * fh, 'c');
    lab('$U$', X(xv + 28), Y(268) + 0.36 * fh, 'l');
    lab('$R$', X(xl + 20), Y(268) + 0.36 * fh, 'l');
    lab('$+$', X(xp1 + 8), Y(top - 16), 'l');
    lab('$-$', X(xp1 + 8), Y(bot + 20) + 0.5 * fh, 'l');
    lab('$G$', X(122), Y(70) + 0.36 * fh, 'l');
    if (S.Ipv > 0.5) { head(162, top, 'r'); head(234, top, 'r'); head(xl, 316, 'd'); head(234, bot, 'l'); lab('$I$', X(234), Y(top - 16), 'c', CUR); }
  }
  function arrowFill(x1, y1, x2, y2, col) {
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, hl = 14, hw = 7, bx = x2 - ux * hl, by = y2 - uy * hl;
    p.stroke(...col); p.strokeWeight(w(3)); p.line(X(x1), Y(y1), X(bx), Y(by));
    p.noStroke(); p.fill(...col); p.triangle(X(x2), Y(y2), X(bx - uy * hw), Y(by + ux * hw), X(bx + uy * hw), Y(by - ux * hw));
  }
  // --- the panel's (U, I) curve; the rectangle U · I is the power ---------------------------------------------------
  function pvGraph(S) {
    const { ox, oy, gx1, gy1 } = G, umax = 7, imax = 250;
    const GX = (u) => ox + u / umax * (gx1 - ox), GY = (i) => oy - i / imax * (oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let u = 1; u <= umax; u += 1) p.line(GX(u), oy, GX(u), gy1);
    for (let i = 50; i <= imax; i += 50) p.line(ox, GY(i), gx1, GY(i));
    if (S.Ipv > 0.01 && S.Upv > 0.001) {                            // the power as the area U · I
      p.noStroke(); p.fill(...HEATL, 150); p.rect(GX(0), GY(S.Ipv), GX(S.Upv) - GX(0), GY(0) - GY(S.Ipv));
      p.stroke(...HEATC); p.strokeWeight(1.5 * sk); p.line(GX(S.Upv), GY(0), GX(S.Upv), GY(S.Ipv)); p.line(GX(0), GY(S.Ipv), GX(S.Upv), GY(S.Ipv));
    }
    const curve = (g, col, wt) => {
      if (g <= 0) return; p.noFill(); p.stroke(...col); p.strokeWeight(wt); p.beginShape();
      const ut = uOpen(g); for (let k = 0; k <= 160; k++) { const u = ut * k / 160; p.vertex(GX(u), GY(iPv(g, u) * 1000)); } p.endShape();
    };
    if (S.G < 1000) curve(1000, [190, 200, 214], 2 * sk);           // faint: full sunlight, for comparison
    curve(S.G, CELL, 3 * sk);
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 14 * sk, oy); p.line(ox, oy, ox, gy1 - 12 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 26 * sk, oy, gx1 + 12 * sk, oy - 6 * sk, gx1 + 12 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 24 * sk, ox - 6 * sk, gy1 - 10 * sk, ox + 6 * sk, gy1 - 10 * sk);
    for (let u = 1; u <= umax; u += 1) { p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(u), oy, GX(u), oy + 6 * sk); lab('$' + u + '$', GX(u), oy + 8 * sk + 0.9 * fh, 'c'); }
    for (let i = 50; i <= imax; i += 50) { p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(i), ox, GY(i)); lab('$' + i + '$', ox - 9 * sk, GY(i) + 0.36 * fh, 'r'); }
    lab('$0$', ox - 9 * sk, oy + 8 * sk + 0.9 * fh, 'r');
    lab('$U\\,(\\text{V})$', 596, oy + 8 * sk + 2.3 * fh, 'r');
    lab('$I\\,(\\text{mA})$', ox + 12 * sk, gy1 - 12 * sk, 'l');
    if (GX(S.Upv) - ox > 44 * sk && oy - GY(S.Ipv) > 40 * sk) lab('$P$', (ox + GX(S.Upv)) / 2, (oy + GY(S.Ipv)) / 2 + 0.36 * fh, 'c');
    if (S.G > 0) { p.fill(...CUR); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(S.Upv), GY(S.Ipv), 11 * sk); }
  }

  function nice(v, nmax) {
    const e = Math.floor(Math.log10(v));
    for (let k = e - 2; k <= e + 1; k++) for (const m of [1, 2, 5]) { const s = m * Math.pow(10, k); if (v / s <= nmax + 1e-9) return { s, max: Math.max(s, Math.ceil(v / s - 1e-9) * s) }; }
    return { s: v, max: v };
  }
  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const wd = p.textWidth(s), xa = align === 'r' ? x - wd : align === 'c' ? x - wd / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - wd - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + wd, y1: y + 0.25 * fh });
  }
  function grect(x, y, wd, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, wd, h); c.restore();
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sig = (x) => tx(x, x >= 100 ? 0 : x >= 10 ? 1 : x >= 1 ? 2 : 3);
});
