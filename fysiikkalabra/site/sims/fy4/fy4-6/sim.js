// fy4-6 Paino, kitka ja kalteva taso: a box released at rest on a plank tilted at the angle α, with a choice of mass and
// surfaces (model friction coefficients). Model: weight G = mg vertical; components G_x = mg sin α down the slope and
// G_y = mg cos α into it; the plank's normal force N = mg cos α (no acceleration across the slope). The box stays at rest
// when the static friction needed, G_x, is at most μ0 N (tan α ≤ μ0): then F_μ = G_x up the slope and a = 0. Otherwise it
// slides with kinetic friction F_μ = μN up the slope and a = g(sin α − μ cos α) down it. Air resistance is neglected.
// Top left: the situation picture (tilannekuva), the plank on a post with the box; the velocity is a thin blue arrow
// beside the box, never a force. Right: the force diagram (voimakuvio), the box a plain rectangle tilted with the slope,
// every force from its point of application (G from the centre, N from the bottom face, friction from the uphill bottom
// corner outside the box), all to one scale for the chosen mass, the weight's components dashed (checkbox). Bottom left: an (α, F_μ) graph
// that marks the friction at every angle the student has tried (a filled point at rest, a ring while sliding).
// On a narrow screen (#sim-root under 500 px) the three panels stack at the full 600 width. Every canvas text goes
// through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, LEN = 2.0;                                              // m/s²; the plank's length (m)
  const SURF = { puu: [0.50, 0.30], muovi: [0.30, 0.20], kumi: [0.80, 0.60] };   // model values μ0, μ
  const YR = { 2: [14, 2], 3: [20, 4], 4: [28, 4] };                       // graph: F_μ range and tick step (N) per mass
  const HN = { sit: 250, dia: 400, gra: 230 };                            // panel heights when stacked on a phone
  const RED = [201, 42, 42], BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203];
  let narrow = false, laid = false, OY = 0, U = 1, W = 360, S = 4.2, S0 = 4.2;      // layout; panel offset; stroke scale; situation width; px per newton
  const D = { x: 468, y: 175, w: 92, h: 58 };                             // force diagram: the box's rectangle (set per layout)
  const GR = { x0: 52, x1: 330, y0: 128, h: 100 };                        // graph: origin and plot size (panel-local, set per layout)
  let btn, slA, lA, selM, selP, selSpeed, cbKomp, readout;
  let d = 0, v = 0, running = false, done = false, trail = {}, trailKey = '', labels = [];

  const model = () => {
    const al = Number(slA.value()), r = al * Math.PI / 180, m = Number(selM.value()), [mu0, mu] = SURF[selP.value()];
    const G = m * g, Gx = G * Math.sin(r), Gy = G * Math.cos(r), N = Gy, Fmax = mu0 * N;
    const slides = Gx > Fmax + 1e-9;
    const Fmu = slides ? mu * N : Gx, a = slides ? (Gx - Fmu) / m : 0;
    return { al, r, m, mu0, mu, G, Gx, Gy, N, Fmax, Fmu, a, slides };
  };
  const restart = () => { d = 0; v = 0; running = false; done = false; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l1); slA = p.createSlider(0, 45, 10, 1).parent(l1);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of ['2', '3', '4']) selM.option(Number(m).toFixed(1).replace('.', DECP) + ' kg', m);
    selM.selected('2');
    const lp = p.createElement('label').parent(controls); p.createSpan(__('pinnat')).parent(lp); selP = p.createSelect().parent(lp);
    selP.option(__('puu'), 'puu'); selP.option(__('muovi'), 'muovi'); selP.option(__('kumi'), 'kumi');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.25'); selSpeed.option(__('normaali'), '0.5'); selSpeed.option(__('nopea'), '1'); selSpeed.selected('0.5');
    const lk = p.createElement('label').parent(controls); cbKomp = p.createCheckbox('', false).parent(lk); p.createSpan(__('komponentit')).parent(lk);
    for (const e of [slA.elt, selM.elt, selP.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { alpha: { input: slA.elt, unit: '°' }, m: { input: selM.elt, unit: 'kg' }, pinta: { input: selP.elt, unit: '' } },
      reset: () => { slA.value(10); selM.selected('2'); selP.selected('puu'); cbKomp.checked(false); trail = {}; restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const M = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) {                                            // the canvas was resized: draw on the next frame
      window.simState = Object.assign({}, window.simState || {}, { alpha: M.al, m: M.m, pinta: selP.value(), mu0: M.mu0, mu: M.mu,
        komponentit: cbKomp.checked(), G: M.G, Gx: M.Gx, Gy: M.Gy, N: M.N, Fmax: M.Fmax, Fmu: M.Fmu, a: M.a, liukuu: M.slides ? 1 : 0,
        v, d, running, done, labels: [] });
      p.redraw(); return;
    }
    const PL = plankLen(), sMax = LEN * 0.62, sMin = boxSize(M.m)[0] / 2 / (PL / LEN) + 0.03;   // box bottom centre along the plank (m)
    if (running && M.slides) {
      const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
      v += M.a * dt; d += v * dt;
      if (sMax - d <= sMin) { d = sMax - sMin; running = false; done = true; }
    } else if (running && !M.slides) running = false;
    const key = selM.value() + selP.value();
    if (key !== trailKey) { trail = {}; trailKey = key; }
    trail[M.al] = [M.Fmu, M.slides];
    lA.html(__('kulma', { a: tx(M.al, 0) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { G: tx(M.G, 1), Gx: tx(M.Gx, 1), N: tx(M.N, 1), F: tx(M.Fmu, 1), Fm: tx(M.Fmax, 1),
                                 tila: M.slides ? __('liukuu') : __('levossa'), a: tx(M.a, 2), v: tx(v, 2) }));
    window.simState = { alpha: M.al, m: M.m, pinta: selP.value(), mu0: M.mu0, mu: M.mu, komponentit: cbKomp.checked(),
                        G: M.G, Gx: M.Gx, Gy: M.Gy, N: M.N, Fmax: M.Fmax, Fmu: M.Fmu, a: M.a, liukuu: M.slides ? 1 : 0,
                        v, d, running, done, labels: null };
    U = narrow ? 0.8 * k : Math.max(1, k * 0.8);
    const fh = Math.round((narrow ? 14 : 13) * k);
    labels = [];
    p.background(250);
    OY = 0; p.push(); situation(M, sMax - d, fh); p.pop();
    OY = narrow ? HN.sit : 0; p.push(); p.translate(narrow ? 0 : 0, OY); diagram(M, fh); p.pop();
    OY = narrow ? HN.sit + HN.dia : 236; p.push(); p.translate(0, OY); graph(M, fh, k); p.pop();
    window.simState.labels = labels;
  };

  // wide screen: the 600×400 picture; phone (the sim's box under 500 px): the three panels stacked at the full 600 width
  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) { W = 600; S0 = 4.5; D.x = 300; D.y = 190; D.w = 120; D.h = 74; GR.x0 = 86; GR.x1 = 560; GR.y0 = 170; GR.h = 130; p.resizeCanvas(600, HN.sit + HN.dia + HN.gra); }
    else { W = 360; S0 = 4.2; D.x = 468; D.y = 175; D.w = 92; D.h = 58; GR.x0 = 52; GR.x1 = 330; GR.y0 = 128; GR.h = 100; p.resizeCanvas(600, 400); }
    return true;
  }
  const plankLen = () => narrow ? 270 : 250;
  const boxSize = (m) => { const q = narrow ? 1.3 : 1; return [(m === 2 ? 40 : m === 3 ? 48 : 56) * q, (m === 2 ? 30 : m === 3 ? 36 : 42) * q]; };

  // --- the situation picture: a wall, the floor, the plank on a post, the box on the plank, the velocity beside it ---
  function situation(M, s, fh) {
    const H = narrow ? HN.sit : 236, FLOOR = H - 30, X0 = narrow ? 40 : 24, PL = plankLen(), px = PL / LEN;
    grect(0, 0, W, FLOOR, [[236, 242, 247], [222, 230, 238]], 0);
    grect(0, FLOOR, W, H - FLOOR, [[217, 178, 106], [190, 150, 85]], 0);
    p.stroke(169, 122, 53); p.strokeWeight(1.5 * U); for (let x = 12; x < W; x += 46) p.line(x, FLOOR + 6, x + 22, FLOOR + 6);
    const c = Math.cos(M.r), sn = Math.sin(M.r), ex = X0 + PL * c, ey = FLOOR - PL * sn;
    // the post under the plank's upper end and the hinge at its foot
    if (ey < FLOOR - 4) grect(ex - 8, ey + 4, 16, FLOOR - ey - 4, [[233, 201, 138], [200, 160, 95]], 2);
    // the plank: a wooden board with its top surface on the line from (X0, FLOOR) at the angle α
    p.push(); p.translate(X0, FLOOR); p.rotate(-M.r);
    p.noStroke(); p.fill(233, 201, 138); p.rect(0, 0, PL, 10 * U);
    p.stroke(169, 122, 53); p.strokeWeight(2 * U); p.noFill(); p.rect(0, 0, PL, 10 * U);
    p.strokeWeight(1 * U); for (let x = 30; x < PL - 10; x += 52) p.line(x, 3 * U, x + 26, 3 * U);
    // the box: its bottom centre s metres up the plank
    const [bw, bh] = boxSize(M.m), bx = s * px;
    p.fill(241, 223, 181); p.stroke(169, 122, 53); p.strokeWeight(2 * U); p.rect(bx - bw / 2, -bh, bw, bh, 2);
    p.strokeWeight(1.5 * U); p.line(bx, -bh, bx, -bh * 0.55);
    p.noStroke(); p.fill(169, 122, 53); p.rect(bx - bw * 0.3, -bh * 0.45, bw * 0.6, 3 * U);
    // the velocity: beside the box, parallel to the plank, thin and blue; not a force
    if (v > 0.01) {
      const L = Math.min(70, 16 + v * 26), y = -bh - 18 * U, x1 = bx + 4, x2 = x1 - L;
      p.stroke(...BLUE); p.strokeWeight(2.5 * U); p.line(x1, y, x2, y); p.line(x2, y, x2 + 9 * U, y - 5 * U); p.line(x2, y, x2 + 9 * U, y + 5 * U);
    }
    p.pop();
    // the angle at the foot of the plank
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5 * U);
    if (M.al > 0) p.arc(X0, FLOOR, 90, 90, -M.r, 0);
    p.drawingContext.setLineDash([4, 4]); p.line(X0, FLOOR, X0 + 70, FLOOR); p.drawingContext.setLineDash([]);
    const ty = narrow ? fh + 4 : 18;
    lab(__('tilannekuva'), 8, ty, 'l', fh, INKC);
    lab(`$\\alpha = ${tx(M.al, 0)}^\\circ$`, W * 0.5, ty, 'c', fh, INKC);
    lab(`$v = ${tx(v, 2)}\\,\\text{m/s}$`, W - 8, ty, 'r', fh, BLUE);
  }

  // --- the force diagram: the box a rectangle tilted with the slope; one scale for every setting ---
  function diagram(M, fh) {
    p.noStroke(); p.fill(255);
    if (narrow) { p.rect(0, 0, 600, HN.dia); p.stroke(220); p.strokeWeight(1); p.line(0, 0, 600, 0); lab(__('voimakuvio'), 8, fh + 4, 'l', fh, INKC); }
    else { p.rect(360, 0, 240, 400); p.stroke(220); p.strokeWeight(1); p.line(360, 0, 360, 400); lab(__('voimakuvio'), 368, 18, 'l', fh, INKC); }
    S = S0 * 4 / M.m;                                                      // one scale per mass: the arrows fill the panel
    const c = Math.cos(M.r), sn = Math.sin(M.r), t = [c, sn], nr = [-sn, c];        // up the slope and out of it (y up)
    const P = (u, w) => [D.x + u * c - w * sn, D.y - (u * sn + w * c)];              // body frame (u along, w across) to canvas
    p.push(); p.translate(D.x, D.y); p.rotate(-M.r); p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(-D.w / 2, -D.h / 2, D.w, D.h); p.pop();
    const ctr = [D.x, D.y], pN = P(14, -D.h / 2), pF = P(D.w / 2, -D.h / 2);
    arrow(ctr, [0, -M.G], '$\\overline{G}$', fh, [-1, 0.2]);
    arrow(pN, [M.N * nr[0], M.N * nr[1]], '$\\overline{N}$', fh, null);
    if (M.Fmu > 0.05) arrow(pF, [M.Fmu * t[0], M.Fmu * t[1]], '$\\overline{F}_\\mu$', fh, null);
    if (cbKomp.checked() && M.al > 0) {                                     // on a level plank G_y would be G itself
      dashed(ctr, [-M.Gx * t[0], -M.Gx * t[1]], '$\\overline{G}_x$', fh, [-1, -0.2]);
      dashed(ctr, [-M.Gy * nr[0], -M.Gy * nr[1]], '$\\overline{G}_y$', fh, [1, 0.6]);
    }
  }
  // an arrow from at (canvas) along vec (newtons, y up); the label beyond its tip, or at the side given (in label widths)
  function arrow(at, vec, name, fh, side) {
    const x2 = at[0] + vec[0] * S, y2 = at[1] - vec[1] * S, L = Math.hypot(x2 - at[0], y2 - at[1]);
    if (L < 1) return;
    const a = Math.atan2(y2 - at[1], x2 - at[0]), H = Math.min(11 * U, L * 0.7);
    p.stroke(...RED); p.strokeWeight(3.2 * U); p.line(at[0], at[1], x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
    tipLabel(name, x2, y2, a, fh, side, RED);
  }
  function dashed(at, vec, name, fh, side) {
    const x2 = at[0] + vec[0] * S, y2 = at[1] - vec[1] * S, L = Math.hypot(x2 - at[0], y2 - at[1]);
    if (L < 6) return;
    const a = Math.atan2(y2 - at[1], x2 - at[0]);
    p.stroke(...RED, 210); p.strokeWeight(2 * U); p.drawingContext.setLineDash([6, 5]); p.line(at[0], at[1], x2, y2); p.drawingContext.setLineDash([]);
    p.noFill(); p.line(x2, y2, x2 - 10 * U * Math.cos(a - 0.5), y2 - 10 * U * Math.sin(a - 0.5)); p.line(x2, y2, x2 - 10 * U * Math.cos(a + 0.5), y2 - 10 * U * Math.sin(a + 0.5));
    tipLabel(name, x2, y2, a, fh, side, RED);
  }
  function tipLabel(name, x2, y2, a, fh, side, col) {                   // kept inside the diagram's panel
    p.textSize(fh); const w = p.textWidth(name), left = narrow ? 4 : 364;
    let x = side ? x2 + side[0] * (w / 2 + 8) : x2 + Math.cos(a) * (w / 2 + 8);
    const y = side ? y2 + side[1] * fh + fh * 0.36 : y2 + Math.sin(a) * (fh * 0.8) + fh * 0.36;
    x = Math.max(left + w / 2, Math.min(596 - w / 2, x));
    lab(name, x, y, 'c', fh, col);
  }

  // --- the (α, F_μ) graph: the friction at every angle tried with this mass and these surfaces ---
  function graph(M, fh, k) {
    const H = narrow ? HN.gra : 164, [ymax, ystep] = YR[M.m];
    const X = (al) => GR.x0 + al / 45 * (GR.x1 - GR.x0), Y = (F) => GR.y0 - F / ymax * GR.h;
    p.noStroke(); p.fill(255); p.rect(0, 0, W, H);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, W, 0);
    p.stroke(...GRID); p.strokeWeight(1);
    for (let al = 5; al <= 45; al += 5) p.line(X(al), Y(0), X(al), Y(ymax));
    for (let F = ystep; F <= ymax; F += ystep) p.line(X(0), Y(F), X(45), Y(F));
    p.stroke(...INKC); p.strokeWeight(2 * U);
    p.line(X(0), Y(0), X(45) + 12, Y(0)); p.line(X(0), Y(0), X(0), Y(ymax) - 12);
    p.noStroke(); p.fill(...INKC);
    p.triangle(X(45) + 18, Y(0), X(45) + 9, Y(0) - 4 * U, X(45) + 9, Y(0) + 4 * U); p.triangle(X(0), Y(ymax) - 18, X(0) - 4 * U, Y(ymax) - 9, X(0) + 4 * U, Y(ymax) - 9);
    const xt = narrow || k <= 1.3 ? [15, 30, 45] : [15, 45];
    for (const al of xt) lab(`$${al}$`, X(al), Y(0) + fh * 1.25, 'c', fh, MUTEDC);
    lab('$0$', X(0) - 6, Y(0) + fh * 1.25, 'r', fh, MUTEDC);
    for (let F = ystep * 2; F <= ymax; F += ystep * 2) lab(`$${F}$`, X(0) - 6, Y(F) + fh * 0.36, 'r', fh, MUTEDC);
    lab('$F_\\mu\\ (\\text{N})$', X(0) + 8, Y(ymax) - 6, 'l', fh, INKC);
    lab('$\\alpha\\ (^\\circ)$', X(45) + 6, Y(0) - fh * 0.8, 'r', fh, INKC);
    for (const key of Object.keys(trail)) {
      const [F, sl] = trail[key], x = X(Number(key)), y = Y(Math.min(F, ymax));
      if (sl) { p.noFill(); p.stroke(...RED); p.strokeWeight(2 * U); p.circle(x, y, 7 * U); }
      else { p.noStroke(); p.fill(...RED); p.circle(x, y, 7 * U); }
    }
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5 * U); p.circle(X(M.al), Y(Math.min(M.Fmu, ymax)), 13 * U);   // the current angle
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: OY + y - 0.75 * size, x1: x0 + w, y1: OY + y + 0.25 * size });
  }
  function grect(x, y, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.3)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const DECP = DEC === '.' ? '.' : ',';
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
