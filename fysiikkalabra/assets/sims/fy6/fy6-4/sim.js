// fy6-4 Vastusten sarja- ja rinnankytkennät: an ideal battery of voltage U feeds one resistor R1, or R1 and R2 in
// series, or R1 and R2 in parallel. Ideal wires and meters. Series: R = R1 + R2, one current I = U / R through both,
// U1 = R1 I, U2 = R2 I. Parallel: 1/R = 1/R1 + 1/R2, each branch has the voltage U, I1 = U / R1, I2 = U / R2,
// I = I1 + I2. The picture: an IEC circuit diagram (battery plates, resistors as rectangles, an ammeter in the main
// wire), violet dots moving in the conventional current direction at a pace proportional to the current in that wire
// (equal spacing everywhere, so the dots of the two branches add up to those of the main wire), resistors that glow
// with their power I²R. The speed select scales only the dots' pace. Every canvas text goes through lab(), which
// pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], CUR = [112, 72, 232], VOLTC = [25, 113, 194], HEATL = [255, 192, 120],
        HEATC = [232, 89, 12], PAPERC = [246, 241, 230], IRONC = [108, 117, 125];
  // geometry: wide 600 x 400; narrow (sim-root < 500 px) 600 x 600 with larger labels
  const WIDE = { H: 400, L: 72, T: 112, B: 340, Rx: 548, cy: 226, xa: 236, M: 230, am: 156, gap: 42 };
  const NARROW = { H: 600, L: 72, T: 160, B: 540, Rx: 548, cy: 350, xa: 290, M: 350, am: 130, gap: 56 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let selMode, slU, slR1, slR2, selSpeed, lU, lR1, lR2, readout;
  const offs = {};                     // each wire path's dot offset along it (px)

  const params = () => ({ mode: selMode.value(), U: Number(slU.value()), R1: Number(slR1.value()), R2: Number(slR2.value()) });
  function solve(S) {                  // the circuit's currents (A) and voltages (V)
    if (S.mode === 'sarja') { const R = S.R1 + S.R2, I = S.U / R; return { R, I, I1: I, I2: I, U1: S.R1 * I, U2: S.R2 * I }; }
    if (S.mode === 'rinnan') { const I1 = S.U / S.R1, I2 = S.U / S.R2, I = I1 + I2; return { R: S.U / I, I, I1, I2, U1: S.U, U2: S.U }; }
    const I = S.U / S.R1; return { R: S.R1, I, I1: I, I2: 0, U1: S.U, U2: 0 };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('kytkenta')).parent(l0); selMode = p.createSelect().parent(l0);
    selMode.option(__('yksi'), 'yksi'); selMode.option(__('sarja'), 'sarja'); selMode.option(__('rinnan'), 'rinnan'); selMode.selected('sarja');
    const l1 = p.createElement('label').parent(controls); lU = p.createSpan('').parent(l1); slU = p.createSlider(1, 12, 6, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lR1 = p.createSpan('').parent(l2); slR1 = p.createSlider(10, 200, 100, 10).parent(l2);
    const l3 = p.createElement('label').parent(controls); lR2 = p.createSpan('').parent(l3); slR2 = p.createSlider(10, 200, 50, 10).parent(l3);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { mode: { input: selMode.elt, unit: '' }, U: { input: slU.elt, unit: 'V' }, R1: { input: slR1.elt, unit: 'Ω' }, R2: { input: slR2.elt, unit: 'Ω' } },
      reset: () => { selMode.selected('sarja'); slU.value(6); slR1.value(100); slR2.value(50); for (const k in offs) offs[k] = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params(), C = solve(S);
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    lU.html(__('jannite', { U: tx(S.U, 1) }));
    lR1.html(__('vastus1', { R: String(S.R1) }));
    lR2.html(S.mode === 'yksi' ? __('vastus2pois', { R: String(S.R2) }) : __('vastus2', { R: String(S.R2) }));
    readout.html(__('lukemat', { R: sig(C.R), I: sig(C.I * 1000), I1: sig(C.I1 * 1000), U1: sig(C.U1) }) +
                 (S.mode === 'yksi' ? __('lukemat2pois') : __('lukemat2', { I2: sig(C.I2 * 1000), U2: sig(C.U2) })));
    window.simState = { mode: S.mode, U: S.U, R1: S.R1, R2: S.R2, R: C.R, I: C.I, ImA: C.I * 1000, I1mA: C.I1 * 1000,
                        I2mA: C.I2 * 1000, U1: C.U1, U2: C.U2, P1: C.I1 * C.U1, P2: C.I2 * C.U2, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? Math.min(k, 1.6) : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.H, [PAPERC, [255, 255, 255]]);
    circuit(S, C, dt);
    window.simState.labels = labels;
  };

  // the wire paths of each connection, with the current (A) each carries
  function paths(S, C) {
    const { L, T, B, Rx, cy, xa, M } = G, up = cy - 16 * sk, dn = cy + 16 * sk;
    if (S.mode === 'rinnan') return [
      { id: 'in', I: C.I, pts: [[L, up], [L, T], [xa, T]] },
      { id: 'b1', I: C.I1, pts: [[xa, T], [Rx, T], [Rx, M]] },
      { id: 'b2', I: C.I2, pts: [[xa, T], [xa, M], [Rx, M]] },
      { id: 'out', I: C.I, pts: [[Rx, M], [Rx, B], [L, B], [L, dn]] }];
    return [{ id: 'loop', I: C.I, pts: [[L, up], [L, T], [Rx, T], [Rx, B], [L, B], [L, dn]] }];
  }

  function circuit(S, C, dt) {
    const { L, T, B, Rx, cy, xa, M, am, gap } = G;
    const P = paths(S, C);
    // wires
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3 * sk); p.strokeJoin(p.ROUND);
    for (const w of P) { p.beginShape(); for (const [x, y] of w.pts) p.vertex(x, y); p.endShape(); }
    // current dots: equal spacing, pace proportional to the wire's current (60 px/s per 100 mA); above 0.6 A in the main wire all wires are
    // scaled by the same factor, so the dots of the two branches still add up to those of the main wire
    const space = 30 * sk, kk = Math.min(1, 0.6 / Math.max(C.I, 1e-9));
    p.noStroke(); p.fill(...CUR);
    for (const w of P) {
      const v = 600 * w.I * kk * sk;
      offs[w.id] = ((offs[w.id] || 0) + v * dt) % space;
      const segs = [], tot = w.pts.slice(1).reduce((s, q, i) => { const d = Math.hypot(q[0] - w.pts[i][0], q[1] - w.pts[i][1]); segs.push(d); return s + d; }, 0);
      for (let s = offs[w.id]; s < tot; s += space) {
        let r = s, i = 0; while (r > segs[i]) { r -= segs[i]; i++; }
        const a = w.pts[i], b = w.pts[i + 1], t = r / segs[i];
        p.circle(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, 8 * sk);
      }
    }
    battery(L, cy, S.U);
    ammeter(am, T, C.I);
    if (S.mode === 'sarja') {
      const x1 = G.H > 400 ? 296 : 312, x2 = G.H > 400 ? 450 : 456, drop = G.H > 400 ? 1.3 * fh : 0;
      resistor(x1, T, C.U1 * C.I1); resistor(x2, T, C.U2 * C.I2);
      lab('$R_1 = ' + S.R1 + '\\,\\Omega$', x1, T - gap, 'c', INKC);
      lab('$R_2 = ' + S.R2 + '\\,\\Omega$', x2, T - gap, 'c', INKC);
      lab('$U_1 = ' + sig(C.U1) + '\\,\\text{V}$', x1, T + gap + 0.4 * fh, 'c', VOLTC);
      lab('$U_2 = ' + sig(C.U2) + '\\,\\text{V}$', x2, T + gap + 0.4 * fh + drop, 'c', VOLTC);
      lab(__('samavirta'), Rx - 24 * sk, (T + B) / 2 + 0.3 * fh, 'r', CUR);
    } else if (S.mode === 'rinnan') {
      const xr = (xa + Rx) / 2;
      // dots only where the wire branches or joins, not at the plain corners
      for (const [x, y] of [[xa, T], [Rx, M]]) { p.noStroke(); p.fill(...INKC); p.circle(x, y, 11 * sk); }
      resistor(xr, T, C.U1 * C.I1); resistor(xr, M, C.U2 * C.I2);
      lab('$R_1 = ' + S.R1 + '\\,\\Omega$', xr, T - gap, 'c', INKC);
      lab('$I_1 = ' + sig(C.I1 * 1000) + '\\,\\text{mA}$', xr, T + gap + 0.4 * fh, 'c', CUR);
      lab('$R_2 = ' + S.R2 + '\\,\\Omega$', xr, M - gap + 0.4 * fh, 'c', INKC);
      lab('$I_2 = ' + sig(C.I2 * 1000) + '\\,\\text{mA}$', xr, M + gap + 0.4 * fh, 'c', CUR);
      lab('$U_1 = U_2 = ' + sig(S.U) + '\\,\\text{V}$', xr, B - gap + 0.4 * fh, 'c', VOLTC);
    } else {
      const x1 = 384;
      resistor(x1, T, C.U1 * C.I1);
      lab('$R_1 = ' + S.R1 + '\\,\\Omega$', x1, T - gap, 'c', INKC);
      lab('$U_1 = ' + sig(C.U1) + '\\,\\text{V}$', x1, T + gap + 0.4 * fh, 'c', VOLTC);
    }
  }

  function resistor(cx, cy, Pw) {      // IEC rectangle; its fill glows from white towards orange with the power I²R
    const a = Math.min(1, Pw / 0.5), w = 84 * sk, h = 30 * sk;
    p.stroke(...INKC); p.strokeWeight(3 * sk);
    p.fill(255 + (HEATL[0] - 255) * a, 255 + (HEATL[1] - 255) * a, 255 + (HEATL[2] - 255) * a);
    p.rect(cx - w / 2, cy - h / 2, w, h, 2);
    if (a > 0.6) { p.noStroke(); p.fill(...HEATC, 120 * (a - 0.6) / 0.4); p.rect(cx - w / 2 + 6 * sk, cy - h / 2 + 6 * sk, w - 12 * sk, h - 12 * sk, 2); }
  }

  function battery(x, cy, U) {        // the long thin plate (+) above, the short thick plate (−) below
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.line(x - 30 * sk, cy - 9 * sk, x + 30 * sk, cy - 9 * sk);
    p.strokeWeight(9 * sk); p.line(x - 14 * sk, cy + 9 * sk, x + 14 * sk, cy + 9 * sk);
    lab('$+$', x - 34 * sk, cy - 16 * sk, 'r', INKC);
    lab('$-$', x - 34 * sk, cy + 28 * sk, 'r', INKC);
    lab('$U = ' + tx(U, 1) + '\\,\\text{V}$', x + 40 * sk, cy + 0.35 * fh, 'l', INKC);
  }

  function ammeter(x, y, I) {         // an ammeter in the main wire and its reading under it
    p.fill(255); p.stroke(...INKC); p.strokeWeight(3 * sk); p.circle(x, y, 42 * sk);
    lab('$\\text{A}$', x, y + 0.36 * fh, 'c', INKC);
    lab('$I = ' + sig(I * 1000) + '\\,\\text{mA}$', x, G.H > 400 ? y - G.gap : y + G.gap + 0.4 * fh, 'c', CUR);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);           // never past the canvas edge
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  function grect(x, y, w, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, w, h); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sig = (x) => tx(x, x >= 99.95 ? 0 : x >= 9.995 ? 1 : 2);   // three significant figures
});
