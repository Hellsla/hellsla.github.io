// fy5-7 Jaksollinen liike: fitting a sine to a simulated measurement of a weight oscillating on a spring.
// Three data sets (aineisto 1–3) are simulated measurements: 51 points x_i = A_d sin(2π t_i / T_d) + e_i at t_i = 0,0 … 5,0 s,
// where e_i is a fixed pseudo-random error of at most ±0,25 cm (Park–Miller generator, one seed per set), so the points
// never lie exactly on a sine. The student's model is x = A sin(2πt/T) with A and T on two sliders; the sim shows the
// model curve over the points and the fit's deviation d = mean |x_i − A sin(2π t_i / T)| (cm), the model's f = 1/T and the
// number N of the model's full oscillations in the 5,0 s window. Käynnistä plays the 5 s: the weight (left or top) moves
// as the data set's motion A_d sin(2πt/T_d), a blue marker beside it moves as the model, and a cursor sweeps the graph; the
// weight's height and the graph share the equilibrium line and (on a wide screen) the scale. x is positive upwards.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const TMAX = 5.0, NOISE = 0.25, M = 2147483647;
  const DATA = { 1: { A: 6.0, T: 1.60, seed: 11 }, 2: { A: 4.5, T: 0.80, seed: 23 }, 3: { A: 8.5, T: 2.20, seed: 37 } };
  const BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203];
  // geometry: wide 600 x 400 (weight left, graph right, one scale); narrow (sim-root < 500 px) 600 x 980, stacked
  const WIDE = { H: 400, wx: 104, py0: 200, ps: 13, ceil: 14, gx0: 232, gx1: 552, gy0: 200, gs: 13, bottom: 386, sx: 180 };
  const NARROW = { H: 980, wx: 330, py0: 220, ps: 11, ceil: 18, gx0: 118, gx1: 492, gy0: 658, gs: 19, bottom: 945, sy: 380 };
  let G = WIDE, narrow = false, sk = 1, fh = 13, labels = [];
  let btn, sel, slA, slT, lA, lT, selSpeed, readout;
  let t = 0, running = false, pts = [];

  function dataset(k) {                                                  // the simulated measurement of set k
    const D = DATA[k]; let s = D.seed; const out = [];
    for (let i = 0; i <= 50; i++) {
      s = (s * 16807) % M;
      const ti = i / 10, e = (s / M - 0.5) * 2 * NOISE;
      out.push([ti, D.A * Math.sin(2 * Math.PI * ti / D.T) + e]);
    }
    return out;
  }
  const params = () => ({ k: sel.value(), A: Number(slA.value()), T: Number(slT.value()) });
  const model = (P, tt) => P.A * Math.sin(2 * Math.PI * tt / P.T);
  const newData = () => { pts = dataset(sel.value()); t = 0; running = false; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (t >= TMAX - 1e-9) t = 0;
      running = true;
    });
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('aineisto')).parent(l0); sel = p.createSelect().parent(l0);
    for (const k of ['1', '2', '3']) sel.option(__('aineisto' + k), k);
    sel.selected('1');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const l1 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l1); slA = p.createSlider(0.5, 12, 2, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l2); slT = p.createSlider(0.4, 3, 1, 0.05).parent(l2);
    sel.elt.addEventListener('change', newData); sel.elt.addEventListener('input', newData);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    newData();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { aineisto: { input: sel.elt, unit: '' }, A: { input: slA.elt, unit: 'cm' }, T: { input: slT.elt, unit: 's' } },
      reset: () => { sel.selected('1'); slA.value(2); slT.value(1); newData(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    if (running) { t += Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()); if (t >= TMAX) { t = TMAX; running = false; } }
    const P = params(), D = DATA[P.k], f = 1 / P.T;
    const d = pts.reduce((s, [ti, xi]) => s + Math.abs(xi - model(P, ti)), 0) / pts.length;
    const N = Math.floor(TMAX / P.T + 1e-9);
    const xTrue = D.A * Math.sin(2 * Math.PI * t / D.T), xModel = model(P, t);
    const iNear = Math.min(50, Math.max(0, Math.round(t * 10))), xMeas = pts[iNear][1];
    lA.html(__('amplitudi', { A: tx(P.A, 1) }));
    lT.html(__('jaksonaika', { T: tx(P.T, 2) }));
    const bt = running ? __('pysayta') : __('kaynnista');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { A: tx(P.A, 1), T: tx(P.T, 2), f: sig3(f), d: tx(d, 2), N: String(N),
      t: tx(t, 1), x: tx(xMeas, 1), xm: tx(xModel, 1) }));
    window.simState = { aineisto: P.k, A: P.A, T: P.T, f, d, N, t, running, xTrue, xModel, xMeas, dataA: D.A, dataT: D.T, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;                                                 // strokes grow with the label size on a phone
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state: draw again next frame
    labels = [];
    p.background(255);
    picture(xTrue, xModel);
    graph(P, xTrue, xModel);
    window.simState.labels = labels;
  };

  // --- the weight on its spring, and the model's marker beside it ---
  function picture(xTrue, xModel) {
    const { wx, py0, ps, ceil } = G;
    const pw = narrow ? 600 : G.sx, ph = narrow ? G.sy : 400;
    grect(0, 0, pw, ph, [[246, 241, 230], [255, 255, 255]]);
    // the ceiling bracket
    p.noStroke(); p.fill(138, 150, 163); p.rect(wx - 44 * sk, ceil, 88 * sk, 10 * sk, 2);
    p.stroke(...INKC); p.strokeWeight(1.5 * sk);
    for (let j = 0; j < 7; j++) p.line(wx - 40 * sk + j * 13 * sk, ceil, wx - 46 * sk + j * 13 * sk, ceil - 6 * sk);
    // the equilibrium line through the picture
    const yEq = py0;
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([7 * sk, 6 * sk]);
    p.line(8, yEq, pw - 8, yEq); p.drawingContext.setLineDash([]);
    // the spring from the bracket to the weight's hook
    const hw = 30 * sk, hh = 20 * sk, yc = yEq - xTrue * ps, top = ceil + 10 * sk, bot = yc - hh - 6 * sk;
    p.noFill(); p.stroke(108, 117, 125); p.strokeWeight(3 * sk); p.beginShape(); p.vertex(wx, top); p.vertex(wx, top + 6 * sk);
    const turns = 18, L = bot - top - 12 * sk;
    for (let j = 0; j < turns; j++) p.vertex(wx + (j % 2 ? -1 : 1) * 12 * sk, top + 6 * sk + L * (j + 0.5) / turns);
    p.vertex(wx, bot - 6 * sk); p.vertex(wx, bot); p.endShape();
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(wx, bot, wx, yc - hh);
    // the weight
    p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(wx - hw, yc - hh, 2 * hw, 2 * hh, 5 * sk);
    p.noStroke(); p.fill(138, 150, 163); p.rect(wx - hw + 6 * sk, yc - hh + 6 * sk, 2 * hw - 12 * sk, 6 * sk, 3);
    // the model's marker: a blue triangle pointing at the height the model gives
    const ym = yEq - xModel * ps, tip = wx - hw - 6 * sk;
    p.fill(...BLUE); p.noStroke(); p.triangle(tip, ym, tip - 16 * sk, ym - 9 * sk, tip - 16 * sk, ym + 9 * sk);
    lab(__('lbl_malli'), tip - 4 * sk, ym - 12 * sk, 'r', BLUE);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, ph, 600, ph); else p.line(pw, 0, pw, 400);
  }

  // --- the (t, x) graph: the simulated points, the model curve, the time cursor ---
  function graph(P, xTrue, xModel) {
    const { gx0, gx1, gy0, gs, bottom } = G;
    const X = (tt) => gx0 + tt / TMAX * (gx1 - gx0), Y = (x) => gy0 - x * gs;
    const yTop = Y(12), yBot = Y(-12);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let s = 1; s <= 5; s++) p.line(X(s), yTop, X(s), yBot);
    for (const v of [-10, -5, 5, 10]) p.line(gx0, Y(v), gx1, Y(v));
    // the axes: x through the left edge, t along the equilibrium x = 0
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(gx0, yBot, gx0, yTop - 10 * sk); p.line(gx0, gy0, gx1 + 14 * sk, gy0);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx0, yTop - 22 * sk, gx0 - 6 * sk, yTop - 8 * sk, gx0 + 6 * sk, yTop - 8 * sk);
    p.triangle(gx1 + 26 * sk, gy0, gx1 + 12 * sk, gy0 - 6 * sk, gx1 + 12 * sk, gy0 + 6 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (const v of [-10, -5, 0, 5, 10]) { p.line(gx0 - 6 * sk, Y(v), gx0, Y(v)); lab('$' + (v < 0 ? '-' : '') + Math.abs(v) + '$', gx0 - 9 * sk, Y(v) + fh * 0.36, 'r', INKC); }
    for (let s = 0; s <= 5; s++) { p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(X(s), gy0, X(s), gy0 + 6 * sk); lab('$' + s + '$', X(s), bottom, 'c', INKC); }
    lab('$x\\,(\\text{cm})$', gx0 + 12 * sk, yTop - 10 * sk, 'l', INKC);
    lab('$t\\,(\\text{s})$', 594, bottom, 'r', INKC);
    // the time cursor
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 5 * sk]); p.line(X(t), yTop, X(t), yBot); p.drawingContext.setLineDash([]);
    // the model curve
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(3 * sk); p.beginShape();
    for (let j = 0; j <= 400; j++) { const tt = TMAX * j / 400; p.vertex(X(tt), Y(Math.max(-12.5, Math.min(12.5, model(P, tt))))); }
    p.endShape();
    // the simulated measurement points
    const r = (narrow ? 4.5 : 3.6) * sk;
    for (const [ti, xi] of pts) { p.fill(...INKC); p.stroke(255); p.strokeWeight(1.5 * sk); p.circle(X(ti), Y(xi), 2 * r); }
    // where the weight and the model are now
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(X(t), Y(xTrue), 14 * sk);
    p.noStroke(); p.fill(...BLUE); p.circle(X(t), Y(Math.max(-12.5, Math.min(12.5, xModel))), 9 * sk);
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
  const sig3 = (x) => tx(x, Math.max(0, 2 - Math.floor(Math.log10(Math.abs(x)) + 1e-9)));
});
