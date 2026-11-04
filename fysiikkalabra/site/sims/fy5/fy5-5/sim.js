// fy5-5 Newtonin gravitaatiolaki: two boulders far out in space, far from every other body. The student chooses their
// masses m1 and m2 (1–10 t) and the distance r between their centres (2,0–10 m). Model: homogeneous spheres of rock
// (density 3000 kg/m³, drawn to scale: 40 px per metre), so each attracts as if its mass were at its centre;
// F = γ m1 m2 / r² on each body, towards the other (Newton III: F1 = F2); the accelerations a1 = F/m1 = γ m2/r² and
// a2 = F/m2 = γ m1/r². The bodies are shown at one instant (they are not animated: at these accelerations they would
// move at most about 0,3 mm in a minute), so there is no speed control. Above the bodies the forces (red, one shared
// scale), below them the accelerations (orange, one shared scale); each scale is a 1-2-5 step chosen so that the
// longer arrow is 52–130 px, and a bar at the top right shows it. Under the picture a graph of F against r collects a
// point for every distance visited at the current masses (cleared when a mass changes or by the button).
// simState: m1, m2 (t), r (m), F1, F2 (µN), a1, a2 (nm/s²), Fr2 (µN·m²), npts, uF (µN per bar), uA (nm/s² per bar).
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const GAMMA = 6.674e-11, RHO = 3000, PPM = 40, BAR = 50, LMAX = 130;
  const RED = [201, 42, 42], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [227, 220, 203];
  const WIDE = { H: 400, x1: 95, yS1: 16, yS2: 38, yF1: 40, yF2: 66, cy: 122, yA1: 178, yA2: 200, yR: 222, gTop: 236,
                 gx0: 70, gy0: 368, gy1: 274, gx1: 470 };
  const NARROW = { H: 700, x1: 95, yS1: 24, yS2: 60, yF1: 104, yF2: 146, cy: 214, yA1: 278, yA2: 318, yR: 358, gTop: 386,
                   gx0: 96, gy0: 632, gy1: 440, gx1: 470 };
  let L = WIDE, narrow = false, laid = false, labels = [], pts = new Map(), massKey = '';
  let slM1, slM2, slR, lM1, lM2, lR, readout;

  const model = () => {
    const m1 = Number(slM1.value()), m2 = Number(slM2.value()), r = Number(slR.value());
    const F = GAMMA * m1 * 1e3 * m2 * 1e3 / (r * r);                    // N
    return { m1, m2, r, F1: F * 1e6, F2: F * 1e6, a1: F / (m1 * 1e3) * 1e9, a2: F / (m2 * 1e3) * 1e9 };
  };
  const radius = (mt) => Math.cbrt(3 * mt * 1e3 / (4 * Math.PI * RHO)) * PPM;   // px, to scale

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const bC = p.createButton(__('tyhjenna')).parent(controls); bC.elt.addEventListener('click', () => pts.clear());
    const l1 = p.createElement('label').parent(controls); lM1 = p.createSpan('').parent(l1); slM1 = p.createSlider(1, 10, 10, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lM2 = p.createSpan('').parent(l2); slM2 = p.createSlider(1, 10, 2, 1).parent(l2);
    const l3 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l3); slR = p.createSlider(2, 10, 4, 0.5).parent(l3);
    for (const sl of [slM1, slM2, slR]) sl.elt.addEventListener('input', record);
    controls.style('column-gap', '0.75rem');
    for (const l of [l1, l2, l3]) l.style('flex', '1 1 9rem');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    window.addEventListener('resize', () => p.redraw());
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { m1: { input: slM1.elt, unit: 't' }, m2: { input: slM2.elt, unit: 't' }, r: { input: slR.elt, unit: 'm' } },
      reset: () => { slM1.value(10); slM2.value(2); slR.value(4); pts.clear(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  const state = (M, labs, uF, uA) => ({ m1: M.m1, m2: M.m2, r: M.r, F1: M.F1, F2: M.F2, a1: M.a1, a2: M.a2,
    Fr2: M.F1 * M.r * M.r, npts: pts.size, uF, uA, labels: labs });

  p.draw = () => {
    const M = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) { window.simState = state(M, [], 0, 0); p.redraw(); return; }
    record();
    lM1.html(__('massa1', { m: tx(M.m1, 0) }));
    lM2.html(__('massa2', { m: tx(M.m2, 0) }));
    lR.html(__('etaisyys', { r: tx(M.r, 1) }));
    readout.html(__('lukemat', { F1: sig(M.F1), F2: sig(M.F2), a1: sig(M.a1), a2: sig(M.a2) }));
    const fh = Math.round((narrow ? 15 : 13) * k), U = narrow ? 1.6 : 1;
    const uF = unit(Math.max(M.F1, M.F2)), uA = unit(Math.max(M.a1, M.a2));
    window.simState = state(M, null, uF, uA);
    labels = [];
    p.background(250);
    picture(M, fh, U, uF, uA);
    graph(M, fh, U);
    window.simState.labels = labels;
  };

  // the graph's point for the current distance; a new pair of masses starts the graph again
  function record() {
    const M = model(), key = M.m1 + '/' + M.m2;
    if (key !== massKey) { massKey = key; pts.clear(); }
    pts.set(M.r, M.F1);
  }

  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n; L = n ? NARROW : WIDE;
    p.resizeCanvas(600, L.H);
    return true;
  }
  // the smallest 1-2-5 step u for which the longer arrow (value / u · BAR px) is at most LMAX px
  function unit(v) {
    if (!(v > 0)) return 1;
    let e = Math.floor(Math.log10(v / (LMAX / BAR)));
    for (let i = 0; i < 4; i++, e++) for (const s of [1, 2, 5]) { const u = s * Math.pow(10, e); if (v / u * BAR <= LMAX + 1e-9) return u; }
    return Math.pow(10, e);
  }

  // --- space with two boulders: forces above, accelerations below, the distance under them ---
  function picture(M, fh, U, uF, uA) {
    const H = L.gTop - 6, x1 = L.x1, x2 = x1 + M.r * PPM, R1 = radius(M.m1), R2 = radius(M.m2), cy = L.cy;
    const c = p.drawingContext, gr = c.createLinearGradient(0, 0, 0, H);
    gr.addColorStop(0, 'rgb(23,30,44)'); gr.addColorStop(1, 'rgb(41,52,70)');
    c.save(); c.fillStyle = gr; c.fillRect(0, 0, 600, H); c.restore();
    p.noStroke();
    for (let i = 0; i < 70; i++) { const sx = rnd(i) * 600, sy = rnd(i + 300) * H; p.fill(255, 255, 255, 90 + 120 * rnd(i + 700)); p.circle(sx, sy, 1 + 1.6 * rnd(i + 900)); }
    rock(x1, cy, R1, 1); rock(x2, cy, R2, 2);
    lab('$m_1$', x1 - R1 - 6 * U, cy + fh * 0.35, 'r', fh, [255, 255, 255]);
    lab('$m_2$', x2 + R2 + 6 * U, cy + fh * 0.35, 'l', fh, [255, 255, 255]);
    // forces: from above each centre, towards the other body, the same scale
    const LF1 = M.F1 / uF * BAR, LF2 = M.F2 / uF * BAR;
    guide(x1, cy - R1, L.yF1); guide(x2, cy - R2, L.yF2);
    arrow(x1, L.yF1, x1 + LF1, L.yF1, RED, 3.2 * U, 12 * U);
    arrow(x2, L.yF2, x2 - LF2, L.yF2, RED, 3.2 * U, 12 * U);
    lab('$\\overline{F}_1$', x1 - 8 * U, L.yF1 + fh * 0.35, 'r', fh, [255, 168, 168]);
    lab('$\\overline{F}_2$', x2 + 8 * U, L.yF2 + fh * 0.35, 'l', fh, [255, 168, 168]);
    // accelerations: from below each centre, towards the other body, the same scale
    const LA1 = M.a1 / uA * BAR, LA2 = M.a2 / uA * BAR;
    guide(x1, cy + R1, L.yA1); guide(x2, cy + R2, L.yA2);
    arrow(x1, L.yA1, x1 + Math.max(LA1, 1), L.yA1, ORANGE, 2.6 * U, 10 * U, true);
    arrow(x2, L.yA2, x2 - Math.max(LA2, 1), L.yA2, ORANGE, 2.6 * U, 10 * U, true);
    lab('$\\overline{a}_1$', x1 - 8 * U, L.yA1 + fh * 0.35, 'r', fh, [255, 192, 120]);
    lab('$\\overline{a}_2$', x2 + 8 * U, L.yA2 + fh * 0.35, 'l', fh, [255, 192, 120]);
    // the distance between the centres
    p.stroke(220); p.strokeWeight(1.5 * U); p.line(x1, L.yR, x2, L.yR); p.line(x1, L.yR - 6 * U, x1, L.yR + 6 * U); p.line(x2, L.yR - 6 * U, x2, L.yR + 6 * U);
    const sR = `$r = ${tx(M.r, 1)}\\,\\text{m}$`; p.textSize(fh); const wR = p.textWidth(sR) + 10 * U;
    p.noStroke(); p.fill(31, 41, 51); p.rect((x1 + x2) / 2 - wR / 2, L.yR - fh * 0.7, wR, fh * 1.3, 3);
    lab(sR, (x1 + x2) / 2, L.yR + fh * 0.35, 'c', fh, [255, 255, 255]);
    // the scales at the top right: a bar of BAR px and what it stands for
    scaleBar(L.yS1, RED, `$${num(uF)}\\,\\mu\\text{N}$`, fh, U);
    scaleBar(L.yS2, ORANGE, `$${num(uA)}\\,\\text{nm/s}^2$`, fh, U);
  }
  function rock(x, y, R, seed) {
    const c = p.drawingContext; c.save();
    const g = c.createRadialGradient(x - R * 0.35, y - R * 0.35, R * 0.1, x, y, R);
    g.addColorStop(0, 'rgb(196,186,170)'); g.addColorStop(1, 'rgb(108,100,92)');
    c.fillStyle = g; c.beginPath(); c.arc(x, y, R, 0, 2 * Math.PI); c.fill(); c.restore();
    p.noStroke(); p.fill(90, 84, 78, 150);
    for (let i = 0; i < 4; i++) { const a = rnd(seed * 10 + i) * 6.28, d = R * 0.55 * rnd(seed * 20 + i); p.circle(x + d * Math.cos(a), y + d * Math.sin(a), R * (0.16 + 0.12 * rnd(seed * 30 + i))); }
    p.noFill(); p.stroke(60, 56, 52); p.strokeWeight(1.5); p.circle(x, y, 2 * R);
    p.noStroke(); p.fill(255); p.circle(x, y, 4);
  }
  function guide(x, yFrom, yTo) {
    p.stroke(200, 206, 214); p.strokeWeight(1.2); p.drawingContext.setLineDash([3, 4]); p.line(x, yFrom, x, yTo); p.drawingContext.setLineDash([]);
  }
  function arrow(xa, ya, xb, yb, col, w, H, open) {                       // forces solid with a filled head, accelerations thin and open
    const dx = xb - xa, len = Math.abs(dx), s = Math.sign(dx) || 1, h = Math.min(H, len * 0.8);
    p.stroke(...col); p.strokeWeight(w);
    if (open) { p.line(xa, ya, xb, yb); p.line(xb, yb, xb - s * h, yb - h * 0.55); p.line(xb, yb, xb - s * h, yb + h * 0.55); return; }
    p.line(xa, ya, xb - s * h * 0.8, yb);
    p.noStroke(); p.fill(...col); p.triangle(xb, yb, xb - s * h, yb - h * 0.45, xb - s * h, yb + h * 0.45);
  }
  function scaleBar(y, col, s, fh, U) {
    p.textSize(fh); const w = p.textWidth(s), xr = 590, xb1 = xr - w - 8 * U, xb0 = xb1 - BAR;
    p.stroke(...col); p.strokeWeight(3 * U); p.line(xb0, y, xb1, y);
    p.strokeWeight(1.5 * U); p.line(xb0, y - 5 * U, xb0, y + 5 * U); p.line(xb1, y - 5 * U, xb1, y + 5 * U);
    lab(s, xr, y + fh * 0.35, 'r', fh, [235, 238, 242]);
  }

  // --- F against r: a point for every distance visited at these masses, the current one in red ---
  function graph(M, fh, U) {
    const { gTop, gx0, gy0, gy1, gx1 } = L;
    p.noStroke(); p.fill(255); p.rect(0, gTop, 600, L.H - gTop);
    p.stroke(220); p.strokeWeight(1); p.line(0, gTop, 600, gTop);
    const Fmax = GAMMA * M.m1 * M.m2 * 1e6 / 4 * 1e6, step = nice(Fmax / 4), ymax = Math.ceil(Fmax / step) * step;
    const X = (r) => gx0 + r / 10 * (gx1 - gx0), Y = (F) => gy0 - F / ymax * (gy0 - gy1);
    p.stroke(...RULEC); p.strokeWeight(1.5);
    for (let r = 2; r <= 10; r += 2) p.line(X(r), gy0, X(r), gy1);
    for (let F = step; F <= ymax + 1e-9; F += step) p.line(gx0, Y(F), gx1, Y(F));
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(gx0, gy0, gx1 + 22, gy0); p.line(gx0, gy0, gx0, gy1 - 22);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 30, gy0, gx1 + 18, gy0 - 5, gx1 + 18, gy0 + 5); p.triangle(gx0, gy1 - 30, gx0 - 5, gy1 - 18, gx0 + 5, gy1 - 18);
    const every = narrow ? 2 : 1;
    for (let r = 2, i = 0; r <= 10; r += 2, i++) { p.stroke(...INKC); p.strokeWeight(2); p.line(X(r), gy0, X(r), gy0 + 6); if (i % every === 1 % every || !narrow) lab(`$${r}$`, X(r), gy0 + 6 + fh * 1.05, 'c', fh, INKC); }
    for (let F = step, i = 0; F <= ymax + 1e-9; F += step, i++) { p.stroke(...INKC); p.strokeWeight(2); p.line(gx0 - 6, Y(F), gx0, Y(F)); if (!narrow || i % 2 === 1) lab(`$${num(F)}$`, gx0 - 10, Y(F) + fh * 0.35, 'r', fh, INKC); }
    lab('$0$', gx0 - 8, gy0 + 6 + fh * 1.05, 'r', fh, INKC);
    lab('$r\\ (\\text{m})$', gx1 + 36, gy0 + fh * 0.35, 'l', fh, INKC);
    lab('$F\\ (\\mu\\text{N})$', gx0 + 12, gy1 - 24, 'l', fh, INKC);
    for (const [r, F] of pts) { p.stroke(255); p.strokeWeight(2); p.fill(...INKC); p.circle(X(r), Y(F), 11 * U); }
    p.stroke(255); p.strokeWeight(2); p.fill(...RED); p.circle(X(M.r), Y(M.F1), 14 * U);
  }
  function nice(v) { const e = Math.pow(10, Math.floor(Math.log10(v))), f = v / e; return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10) * e; }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  function rnd(i) { return Math.abs(Math.sin(i * 12.9898 + 78.233) * 43758.5453) % 1; }
  // numbers in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace('.', DEC);
  function sig(x) {                                                       // three significant figures, no exponent
    if (!(x > 0)) return '0';
    const d = Math.max(0, 2 - Math.floor(Math.log10(x)));
    return Number(x.toPrecision(3)).toFixed(d).replace('.', DEC);
  }
  function num(v) { return (v >= 1 ? String(Math.round(v)) : String(Number(v.toPrecision(2)))).replace('.', DEC); }
});
