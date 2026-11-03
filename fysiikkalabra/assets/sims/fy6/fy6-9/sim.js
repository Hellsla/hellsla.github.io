// fy6-9 Akut ja latauspiiri: a charger of constant voltage U_lat with the resistance R of the charger and its leads
// charges one battery cell of source voltage E and internal resistance R_s = 0,10 ohm. Voltage law round the loop:
// U_lat - R I - R_s I - E = 0, so I = (U_lat - E) / (R + R_s); terminal voltage U = E + R_s I. The model cell: E rises
// linearly with its charge q from E0 = 3,40 V (empty) to E1 = 4,20 V (full), capacity 2,0 Ah, so with x = U_lat - E,
// dq/dt = x / Rt and x(t) = x0 exp(-k t / Rt), k = 0,40 V/Ah. Full: the charger stops; empty: the cell's protection
// stops a discharge. Energies from t = 0: the charger gives U_lat (q - q0), the cell stores the integral of E dq, the
// rest becomes internal energy of R and R_s. A static picture: the student sets the charging time t with a slider
// (no animation, so no speed control). Every canvas text goes through lab(), which pushes its box to simState.labels.
// p5.js 1.9 instance mode.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], CURC = [112, 72, 232], GOODC = [43, 138, 62],
        GOODL = [178, 242, 187], HEATC = [232, 89, 12], HEATL = [255, 192, 120], HOTC = [201, 42, 42], SANDL = [241, 223, 181];
  const E0 = 3.40, E1 = 4.20, QCAP = 2.0, RS = 0.10, K = (E1 - E0) / QCAP, TMAX = 4.0;
  // wide: circuit left, the cell right, the (t, I) graph below; phone: the three stacked, labels without values
  const WIDE = { H: 400, picH: 240, top: 54, bot: 196, xc: 70, xr: 160, xa: 245, xb: 330, boxT: 80, boxB: 170, yrs: 104, ye: 146,
                 cell: [474, 44, 84, 146], ox: 70, oy: 366, gx1: 520, gy1: 262, tickY: 382 };
  const NARROW = { H: 1080, picH: 700, top: 96, bot: 432, xc: 92, xr: 230, xa: 370, xb: 500, boxT: 170, boxB: 370, yrs: 222, ye: 314,
                   ox: 112, oy: 990, gx1: 500, gy1: 772, tickY: 1030 };
  let G = WIDE, sk = 1, fh = 13, narrow = false, labels = [];
  let slU, slR, slS, slT, lU, lR, lS, lT, readout;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const mk = (min, max, v, st) => { const l = p.createElement('label').parent(controls); const s = p.createSpan('').parent(l); return [s, p.createSlider(min, max, v, st).parent(l)]; };
    [lT, slT] = mk(0, TMAX, 0, 0.1);
    [lU, slU] = mk(3.0, 5.0, 4.5, 0.1);
    [lR, slR] = mk(0.1, 1.0, 0.4, 0.1);
    [lS, slS] = mk(0, 100, 0, 10);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { t: { input: slT.elt, unit: 'h' }, Ulat: { input: slU.elt, unit: 'V' }, R: { input: slR.elt, unit: 'Ω' },
                alku: { input: slS.elt, unit: '%' } },
      reset: () => { slT.value(0); slU.value(4.5); slR.value(0.4); slS.value(0); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  // the cell after t hours (the same model as lessons/FY6/fy6-9/lesson-answers.py)
  function cell(U, R, start, t) {
    const Rt = R + RS, q0 = start * QCAP, x0 = U - (E0 + K * q0);
    let x = x0 * Math.exp(-K * t / Rt), q = q0 + (x0 - x) / K;
    if (x0 > 0 && q >= QCAP) { q = QCAP; x = 0; }
    if (x0 < 0 && q <= 0) { q = 0; x = 0; }
    const E = E0 + K * q, I = x / Rt, Wlat = U * (q - q0), Wkem = E0 * (q - q0) + K / 2 * (q * q - q0 * q0);
    const tFull = x0 > 0 && U > E1 && q0 < QCAP ? Rt / K * Math.log(x0 / (U - E1)) : -1;
    return { U, R, Rt, start, t, I, E, Uterm: E + RS * I, q, soc: q / QCAP * 100, dQ: q - q0, Wlat, Wkem,
             Whav: Wlat - Wkem, Ws: (Wlat - Wkem) * RS / Rt, eta: Wlat > 1e-9 ? Wkem / Wlat * 100 : 0, tFull, Ps: RS * I * I };
  }
  const state = (S) => (S.I > 1e-6 ? 'latautuu' : S.I < -1e-6 ? 'purkautuu' : S.soc >= 99.999 ? 'taynna' : S.soc <= 1e-3 ? 'tyhja' : 'eivirtaa');

  p.draw = () => {
    const U = Number(slU.value()), R = Number(slR.value()), start = Number(slS.value()) / 100, t = Number(slT.value());
    const S = cell(U, R, start, t);
    lT.html(__('aika', { t: tx(t, 1) }));
    lU.html(__('ulat', { U: tx(U, 1) }));
    lR.html(__('resistanssi', { R: tx(R, 1) }));
    lS.html(__('alku', { s: String(Math.round(start * 100)) }));
    readout.html(__('lukemat', { I: tx(S.I, 2), E: tx(S.E, 2), U: tx(S.Uterm, 2), soc: tx(S.soc, 0), dQ: tx(S.dQ, 2),
                                 Wlat: tx(S.Wlat, 2), Wkem: tx(S.Wkem, 2), Whav: tx(S.Whav, 2), eta: tx(S.eta, 0) }));
    window.simState = { Ulat: U, R, Rs: RS, alku: start * 100, t, I: S.I, E: S.E, U: S.Uterm, soc: S.soc, dQ: S.dQ, Wlat: S.Wlat,
                        Wkem: S.Wkem, Whav: S.Whav, Ws: S.Ws, eta: S.eta, tFull: S.tFull, state: state(S), labels: null };
    const cw = (p.canvas && p.canvas.parentElement && p.canvas.parentElement.clientWidth) || document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500; const k = Math.min(2.4, Math.max(1, 600 / cw));
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.picH, [[246, 241, 230], [255, 255, 255]]);
    circuit(S);
    gauge(S);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.picH, 600, G.picH);
    graph(S);
    window.simState.labels = labels;
  };

  // --- the charging circuit ---------------------------------------------------------------------------------------
  function wire(pts, w) {
    p.noFill(); p.stroke(...INKC); p.strokeWeight((w || 3) * sk); p.strokeJoin(p.ROUND);
    p.beginShape(); for (const [x, y] of pts) p.vertex(x, y); p.endShape();
  }
  function plates(x, y) {
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.line(x - 20 * sk, y - 6 * sk, x + 20 * sk, y - 6 * sk);
    p.strokeWeight(7 * sk); p.line(x - 10 * sk, y + 6 * sk, x + 10 * sk, y + 6 * sk);
  }
  function circuit(S) {
    const { top, bot, xc, xr, xa, xb, boxT, boxB, yrs, ye } = G, ym = (top + bot) / 2, bh = narrow ? 84 : 44, hw = (narrow ? 30 : 34) * sk;
    // wires
    wire([[xc, ym - bh], [xc, top], [xb, top], [xb, yrs - 17 * sk]]);
    wire([[xb, yrs + 17 * sk], [xb, ye - 6 * sk]]);
    wire([[xb, ye + 6 * sk], [xb, bot], [xc, bot], [xc, ym + bh]]);
    // the charger: a box round its source
    p.fill(...SANDL); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(xc - 32 * sk, ym - bh, 64 * sk, 2 * bh, 8);
    wire([[xc, ym - bh], [xc, ym - 6 * sk]]); wire([[xc, ym + 6 * sk], [xc, ym + bh]]);
    plates(xc, ym);
    // R on the top wire, the ammeter
    p.fill(255); p.stroke(...INKC); p.strokeWeight(3 * sk); p.rect(xr - 26 * sk, top - 10 * sk, 52 * sk, 20 * sk);
    p.circle(xa, top, 34 * sk);
    lab('$\\text{A}$', xa, top + 0.36 * fh, 'c');
    // the cell: R_s and E in a dashed box, the terminals on its edge; it glows when it warms
    const glow = Math.min(1, S.Ps / 0.5);
    if (glow > 0.01) { p.noStroke(); for (let i = 3; i >= 1; i--) { p.fill(...HEATL, 40 * glow); p.rect(xb - hw - 4 * i * sk, boxT - 4 * i * sk, 2 * hw + 8 * i * sk, boxB - boxT + 8 * i * sk, 8 * sk); } }
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(2 * sk); p.drawingContext.setLineDash([7 * sk, 6 * sk]);
    p.rect(xb - hw, boxT, 2 * hw, boxB - boxT, 6); p.drawingContext.setLineDash([]);
    p.fill(255); p.stroke(...INKC); p.strokeWeight(3 * sk); p.rect(xb - 9 * sk, yrs - 17 * sk, 18 * sk, 34 * sk);
    plates(xb, ye);
    for (const y of [boxT, boxB]) { p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(xb, y, 10 * sk); }
    // currents: violet heads in the direction of the current, none when it is zero
    const d = S.I > 1e-6 ? 1 : S.I < -1e-6 ? -1 : 0;
    if (d) { head((xc + xr) / 2 + 4, top, d > 0 ? 'r' : 'l'); head((xc + xb) / 2, bot, d > 0 ? 'l' : 'r'); head(xb, (yrs + ye) / 2 + 2 * sk, d > 0 ? 'd' : 'u'); }
    // labels
    if (narrow) {
      lab('$U_\\text{lat}$', xc + 40 * sk, ym + 0.36 * fh, 'l');
      lab('$R$', xr, top - 16 * sk - 6, 'c');
      lab('$I$', xa, top - 18 * sk - 6, 'c', CURC);
      lab('$R_\\text{s}$', xb - 42 * sk, yrs + 0.36 * fh, 'r');
      lab('$E$', xb - 42 * sk, ye + 0.36 * fh, 'r');
    } else {
      lab('$U_\\text{lat} = ' + tx(S.U, 1) + '\\,\\text{V}$', xc + 40, ym + 5, 'l');
      lab('$R = ' + tx(S.R, 2) + '\\,\\Omega$', xr, top - 18, 'c');
      lab('$I = ' + tx(S.I, 2) + '\\,\\text{A}$', xa, top + 34, 'c', CURC, true);
      lab('$R_\\text{s} = ' + tx(RS, 2) + '\\,\\Omega$', xb - 42, yrs + 5, 'r');
      lab('$E = ' + tx(S.E, 2) + '\\,\\text{V}$', xb - 42, ye + 5, 'r');
      lab('$U = ' + tx(S.Uterm, 2) + '\\,\\text{V}$', xb + 40, (boxT + boxB) / 2 + 5, 'l');
    }
  }
  function head(x, y, d) {
    const s = 8 * sk; p.noStroke(); p.fill(...CURC);
    if (d === 'r') p.triangle(x + s, y, x - s, y - 0.8 * s, x - s, y + 0.8 * s);
    else if (d === 'l') p.triangle(x - s, y, x + s, y - 0.8 * s, x + s, y + 0.8 * s);
    else if (d === 'd') p.triangle(x, y + s, x - 0.8 * s, y - s, x + 0.8 * s, y - s);
    else p.triangle(x, y - s, x - 0.8 * s, y + s, x + 0.8 * s, y + s);
  }

  // --- the cell's level: a battery drawn upright (wide) or lying (phone), filled green to its level -------------------
  function gauge(S) {
    const lvl = Math.max(0, Math.min(1, S.soc / 100)), st = state(S);
    if (!narrow) {
      const [x, y, w, h] = G.cell;
      p.fill(...INKC); p.noStroke(); p.rect(x + w / 2 - 14, y - 10, 28, 12, 3);
      p.fill(255); p.stroke(...INKC); p.strokeWeight(3); p.rect(x, y, w, h, 10);
      p.noStroke(); p.fill(...GOODL); p.rect(x + 6, y + 6 + (h - 12) * (1 - lvl), w - 12, (h - 12) * lvl, 6);
      p.fill(...GOODC); p.rect(x + 6, y + 6 + (h - 12) * (1 - lvl), w - 12, Math.min(4, (h - 12) * lvl), 2);
      lab('$+$', x + w + 12, y + 12, 'c');
      lab('$' + tx(S.soc, 0) + '\\,\\%$', x + w / 2, y + h + 22, 'c');
      lab(__(st), x + w / 2, y + h + 40, 'c', st === 'latautuu' ? GOODC : st === 'purkautuu' ? HOTC : MUTEDC);
    } else {
      const x = 120, y = 500, w = 330, h = 100;
      p.fill(...INKC); p.noStroke(); p.rect(x + w - 2, y + h / 2 - 22, 22, 44, 4);
      p.fill(255); p.stroke(...INKC); p.strokeWeight(3 * sk); p.rect(x, y, w, h, 14);
      p.noStroke(); p.fill(...GOODL); p.rect(x + 8, y + 8, (w - 16) * lvl, h - 16, 8);
      lab('$+$', x + w + 40, y + h / 2 + 0.36 * fh, 'c');
      lab('$' + tx(S.soc, 0) + '\\,\\%$', x + 20, y + h + 30 + 0.36 * fh, 'l');
      lab(__(st), x + w, y + h + 30 + 0.36 * fh, 'r', st === 'latautuu' ? GOODC : st === 'purkautuu' ? HOTC : MUTEDC);
    }
  }

  // --- the (t, I) graph: the whole charge faint, the part up to t strong, the present point ringed -------------------
  function graph(S) {
    const { ox, oy, gx1, gy1 } = G;
    const traj = []; for (let i = 0; i <= 200; i++) { const t = TMAX * i / 200; traj.push([t, cell(S.U, S.R, S.start, t).I]); }
    if (S.tFull > 0 && S.tFull < TMAX) traj.push([S.tFull, (S.U - E1) / S.Rt]), traj.sort((a, b) => a[0] - b[0]);
    const imax = Math.max(0, ...traj.map((q) => q[1])), imin = Math.min(0, ...traj.map((q) => q[1]));
    const span = Math.max(imax - imin, 0.2), steps = narrow ? [0.5, 1, 2, 4] : [0.25, 0.5, 1, 2];
    const step = steps.find((s) => span / s <= (narrow ? 4 : 5)) || 4;
    const lo = imin < -1e-9 ? Math.floor(imin / step - 1e-9) * step : 0, hi = imax > 1e-9 ? Math.max(step, Math.ceil(imax / step - 1e-9) * step) : lo < 0 ? 0 : step;
    const GX = (t) => ox + t / TMAX * (gx1 - ox), GY = (v) => oy - (v - lo) / (hi - lo) * (oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let v = lo + step; v <= hi + 1e-9; v += step) p.line(ox, GY(v), gx1, GY(v));
    for (let t = 1; t <= TMAX; t++) p.line(GX(t), oy, GX(t), gy1);
    if (lo < 0) { p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.line(ox, GY(0), gx1, GY(0)); }
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 16 * sk, oy); p.line(ox, oy, ox, gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, oy, gx1 + 14 * sk, oy - 6 * sk, gx1 + 14 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 26 * sk, ox - 6 * sk, gy1 - 12 * sk, ox + 6 * sk, gy1 - 12 * sk);
    for (let v = lo; v <= hi + 1e-9; v += step) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(v), ox, GY(v));
      lab('$' + tx(v, step < 0.5 ? 2 : step < 1 ? 1 : 0) + '$', ox - 9 * sk, GY(v) + 0.36 * fh, 'r');
    }
    for (let t = 1; t <= TMAX; t++) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(t), oy, GX(t), oy + 6 * sk);
      lab('$' + t + '$', GX(t), G.tickY, 'c');
    }
    lab('$I\\,(\\text{A})$', ox + 12 * sk, gy1 - 14 * sk, 'l');
    lab('$t\\,(\\text{h})$', 598, oy - 12 * sk, 'r');
    // the whole charge, faint; up to t, strong
    p.noFill(); p.stroke(...CURC, 70); p.strokeWeight(3 * sk); p.beginShape();
    for (const [t, i] of traj) p.vertex(GX(t), GY(i)); p.endShape();
    p.stroke(...CURC); p.beginShape();
    for (const [t, i] of traj) if (t <= S.t + 1e-9) p.vertex(GX(t), GY(i));
    p.vertex(GX(S.t), GY(S.I)); p.endShape();
    p.fill(...CURC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(S.t), GY(S.I), 11 * sk);
    p.noFill(); p.stroke(...HOTC); p.strokeWeight(2.5 * sk); p.circle(GX(S.t), GY(S.I), 22 * sk);
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
