// fy5-4 Tasainen ympyräliike ja normaalikiihtyvyys: a car drives round a level circular track of radius r at the
// constant speed v; the student also chooses the car's mass and the road surface (model static-friction coefficients).
// Model: a_n = v²/r towards the centre; vertically N = mg; the only horizontal force is the road's static friction,
// which must be m v²/r towards the centre. The grip holds while m v²/r ≤ μ0 mg; then F_μ = m v²/r. Otherwise the road
// gives at most μ0 mg, still perpendicular to the velocity (the speed stays v), so the car turns on a wider circle of
// radius v²/(μ0 g) and runs off the outside edge of the track, nearly along the tangent. No air or rolling resistance.
// Left (wide) or top (phone): the track seen from above (not to scale: the track keeps its size in the picture, the car
// is drawn larger), the velocity a thin blue arrow outside the car, the acceleration a thin orange arrow inside it, both
// beside the car, never forces. Right or below: the force diagram of the car seen from behind, the car a plain
// rectangle on the road, G from its centre, N from its bottom face, friction from its bottom corner towards the centre,
// one scale per mass (G always the same length); under it a bar of the friction needed against the limit μ0 mg.
// On a narrow screen (#sim-root under 500 px) the panels stack at the full 600 width. Every canvas text goes through
// lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81;
  const SURF = { kuiva: 0.80, marka: 0.50, jaa: 0.10 };                  // model values μ0
  const HN = { top: 420, dia: 370 };                                     // panel heights when stacked on a phone
  const RED = [201, 42, 42], BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const GREEN = [43, 138, 62];
  let narrow = false, laid = false, OY = 0, U = 1;
  const TV = { cx: 180, cy: 212, R: 130, w: 360, h: 400 };               // top view: track centre, radius (px), panel size
  const D = { x0: 360, w: 240, bx: 500, by: 150, bw: 96, bh: 52, L: 95, barY: 334, barX: 372, barW: 216 };   // diagram panel
  let btn, slV, lV, slR, lR, selM, selP, selSpeed, readout;
  let mode = 'rata', running = false, done = false, th = 0, X = 0, Y = 0, psi = 0, trail = [], labels = [];

  const model = () => {
    const v = Number(slV.value()), r = Number(slR.value()), m = Number(selM.value()), mu0 = SURF[selP.value()];
    const an = v * v / r, Ft = m * an, G = m * g, Fmax = mu0 * G, pito = Ft <= Fmax + 1e-9;
    const Fmu = pito ? Ft : Fmax;
    return { v, r, m, mu0, an, Ft, G, N: G, Fmax, pito, Fmu, a: Fmu / m };
  };
  const restart = () => { mode = 'rata'; running = false; done = false; th = 0; trail = []; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(5, 30, 15, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l2); slR = p.createSlider(20, 100, 50, 5).parent(l2);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of ['1000', '1500', '2000']) selM.option(m + ' kg', m);
    selM.selected('1500');
    const lp = p.createElement('label').parent(controls); p.createSpan(__('pinta')).parent(lp); selP = p.createSelect().parent(lp);
    selP.option(__('kuiva'), 'kuiva'); selP.option(__('marka'), 'marka'); selP.option(__('jaa'), 'jaa');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    for (const e of [slR.elt, selM.elt, selP.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    for (const e of [slV.elt]) { const f = () => { if (mode !== 'rata') restart(); }; e.addEventListener('input', f); e.addEventListener('change', f); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { v: { input: slV.elt, unit: 'm/s' }, r: { input: slR.elt, unit: 'm' }, m: { input: selM.elt, unit: 'kg' }, pinta: { input: selP.elt, unit: '' } },
      reset: () => { slV.value(15); slR.value(50); selM.selected('1500'); selP.selected('kuiva'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  const state = (M, labs) => ({ v: M.v, r: M.r, m: M.m, pinta: selP.value(), mu0: M.mu0, an: M.an, Ftarve: M.Ft, Fmax: M.Fmax,
    Fmu: M.Fmu, G: M.G, N: M.N, a: M.a, pito: M.pito ? 1 : 0, liukuu: mode === 'rata' ? 0 : 1, running, done, labels: labs });

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const M = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) { window.simState = state(M, []); p.redraw(); return; }
    advance(M);
    lV.html(__('ratanopeus', { v: tx(M.v, 0), kmh: tx(M.v * 3.6, 0) }));
    lR.html(__('sade', { r: tx(M.r, 0) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const tila = mode !== 'rata' ? __('liukuu') : M.pito ? __('pitaa') : __('eipida');
    readout.html(__('lukemat', { an: tx(M.an, 2), Ft: tx(M.Ft / 1000, 2), Fm: tx(M.Fmax / 1000, 2), F: tx(M.Fmu / 1000, 2), tila: tila }));
    window.simState = state(M, null);
    U = narrow ? 0.9 * k : Math.max(1, k * 0.8);
    const fh = Math.round((narrow ? 15 : 13) * k);
    labels = [];
    p.background(250);
    OY = 0; p.push(); topView(M, fh); p.pop();
    OY = narrow ? HN.top : 0; p.push(); p.translate(0, OY); diagram(M, fh); p.pop();
    window.simState.labels = labels;
  };

  // the motion in simulated time: on the track θ grows at v/r; sliding, the heading turns at μ0 g / v (metres, y up)
  function advance(M) {
    if (!running) return;
    let dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    if (mode === 'rata' && !M.pito) {                                    // the grip fails: slide from where the car is
      mode = 'liuku'; X = M.r * Math.cos(th); Y = M.r * Math.sin(th); psi = th + Math.PI / 2; trail = [[X, Y]];
    }
    if (mode === 'rata') { th = (th + M.v / M.r * dt) % (2 * Math.PI); return; }
    const ppm = TV.R / M.r, w = M.mu0 * g / M.v;
    while (dt > 0) {
      const h = Math.min(dt, 0.02); dt -= h;
      X += M.v * Math.cos(psi) * h; Y += M.v * Math.sin(psi) * h; psi += w * h;
      if (trail.length === 0 || Math.hypot(X - trail[trail.length - 1][0], Y - trail[trail.length - 1][1]) * ppm > 6) trail.push([X, Y]);
      const sx = TV.cx + X * ppm, sy = TV.cy - Y * ppm, out = Math.hypot(X, Y) * ppm;
      if (out > TV.R + 46 * U || sx < 16 || sx > TV.w - 16 || sy < 40 || sy > TV.h - 16) { running = false; done = true; mode = 'ulos'; break; }
    }
  }

  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) {
      Object.assign(TV, { cx: 300, cy: 225, R: 150, w: 600, h: HN.top });
      Object.assign(D, { x0: 0, w: 600, bx: 330, by: 130, bw: 130, bh: 64, L: 112, barY: 290, barX: 24, barW: 552 });
      p.resizeCanvas(600, HN.top + HN.dia);
    } else {
      Object.assign(TV, { cx: 180, cy: 212, R: 130, w: 360, h: 400 });
      Object.assign(D, { x0: 360, w: 240, bx: 500, by: 150, bw: 96, bh: 52, L: 95, barY: 334, barX: 372, barW: 216 });
      p.resizeCanvas(600, 400);
    }
    restart();
    return true;
  }

  // --- the track from above: grass, the asphalt ring, the centre marker, the car, its velocity and acceleration ---
  function topView(M, fh) {
    const { cx, cy, R, w, h } = TV, half = (narrow ? 24 : 19) * U, ppm = R / M.r;
    grect(0, 0, w, h, [[226, 240, 214], [204, 228, 190]], 0);
    p.noFill(); p.stroke(160, 168, 176); p.strokeWeight(2 * half + 4 * U); p.circle(cx, cy, 2 * R);
    p.stroke(196, 204, 212); p.strokeWeight(2 * half); p.circle(cx, cy, 2 * R);
    p.stroke(255); p.strokeWeight(2 * U); p.drawingContext.setLineDash([10 * U, 10 * U]); p.circle(cx, cy, 2 * R); p.drawingContext.setLineDash([]);
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.fill(255); p.circle(cx, cy, 12 * U); p.fill(...INKC); p.circle(cx, cy, 4 * U);
    let sx, sy, head, nin;                                                // the car's place, heading (screen) and inward normal
    if (mode === 'rata') {
      sx = cx + R * Math.cos(th); sy = cy - R * Math.sin(th); head = [-Math.sin(th), -Math.cos(th)]; nin = [-Math.cos(th), Math.sin(th)];
      p.stroke(...INKC); p.strokeWeight(1.5 * U); p.drawingContext.setLineDash([5 * U, 5 * U]);
      p.line(cx, cy, sx + nin[0] * (half + 2), sy + nin[1] * (half + 2)); p.drawingContext.setLineDash([]);
    } else {
      sx = cx + X * ppm; sy = cy - Y * ppm; head = [Math.cos(psi), -Math.sin(psi)]; nin = [-Math.sin(psi), -Math.cos(psi)];
      p.noStroke(); p.fill(...MUTEDC); for (const [a, b] of trail) p.circle(cx + a * ppm, cy - b * ppm, 4 * U);
    }
    car(sx, sy, head);
    const Lv = (narrow ? 3.0 : 2.4) * M.v * U * 0.8, out = 26 * U;          // velocity: outside the car, along the heading
    const vx = sx - nin[0] * out, vy = sy - nin[1] * out;
    thin(vx - head[0] * Lv / 2, vy - head[1] * Lv / 2, vx + head[0] * Lv / 2, vy + head[1] * Lv / 2, BLUE);
    lab('$\\overline{v}$', vx + head[0] * (Lv / 2 + 12 * U) - nin[0] * 8 * U, vy + head[1] * (Lv / 2 + 12 * U) - nin[1] * 8 * U + fh * 0.35, 'c', fh, BLUE);
    const La = Math.max(10, (narrow ? 10 : 8) * M.a * U * 0.8), a0 = 24 * U;  // acceleration: inside the car, towards the turn's centre
    const ax0 = sx + nin[0] * a0, ay0 = sy + nin[1] * a0, ax1 = ax0 + nin[0] * La, ay1 = ay0 + nin[1] * La;
    thin(ax0, ay0, ax1, ay1, ORANGE);
    lab('$\\overline{a}$', ax1 + nin[0] * 12 * U + head[0] * 10 * U, ay1 + nin[1] * 12 * U + head[1] * 10 * U + fh * 0.35, 'c', fh, ORANGE);
    const ty = narrow ? fh + 6 : 20;
    lab(__('ylhaalta'), 8, ty, 'l', fh, INKC);
    lab(`$r = ${tx(M.r, 0)}\\,\\text{m}$`, w - 8, ty, 'r', fh, INKC);
  }
  function car(x, y, head) {                                              // a car seen from above, along its heading
    const L = (narrow ? 40 : 30) * U * 0.9, W = (narrow ? 22 : 17) * U * 0.9, a = Math.atan2(head[1], head[0]);
    p.push(); p.translate(x, y); p.rotate(a);
    p.noStroke(); p.fill(...INKC);
    for (const u of [-0.3, 0.3]) for (const s of [-1, 1]) p.rect(u * L - 4 * U, s * W / 2 - 2 * U, 8 * U, 4 * U, 1);
    p.fill(241, 223, 181); p.stroke(...INKC); p.strokeWeight(1.8 * U); p.rect(-L / 2, -W / 2, L, W, 4 * U);
    p.fill(238, 245, 249); p.strokeWeight(1 * U); p.rect(L * 0.1, -W / 2 + 3 * U, L * 0.18, W - 6 * U, 1); p.rect(-L * 0.32, -W / 2 + 3 * U, L * 0.12, W - 6 * U, 1);
    p.pop();
  }
  function thin(x1, y1, x2, y2, col) {                                    // velocity or acceleration: thin, open head
    const a = Math.atan2(y2 - y1, x2 - x1), H = 9 * U;
    p.stroke(...col); p.strokeWeight(2.6 * U); p.noFill(); p.line(x1, y1, x2, y2);
    p.line(x2, y2, x2 - H * Math.cos(a - 0.5), y2 - H * Math.sin(a - 0.5)); p.line(x2, y2, x2 - H * Math.cos(a + 0.5), y2 - H * Math.sin(a + 0.5));
  }

  // --- the force diagram from behind: the car a rectangle on the road, the centre of the turn to the left ---
  function diagram(M, fh) {
    const H = narrow ? HN.dia : 400;
    p.noStroke(); p.fill(255); p.rect(D.x0, 0, D.w, H);
    p.stroke(220); p.strokeWeight(1); if (narrow) p.line(0, 0, 600, 0); else p.line(360, 0, 360, 400);
    lab(__('takaa'), D.x0 + 8, narrow ? fh + 6 : 20, 'l', fh, INKC);
    const S = D.L / M.G, top = D.by - D.bh / 2, bot = D.by + D.bh / 2, left = D.bx - D.bw / 2;
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(D.x0 + 12, bot, D.x0 + D.w - 10, bot);
    p.stroke(...MUTEDC); p.strokeWeight(1.2 * U); for (let x = D.x0 + 16; x < D.x0 + D.w - 14; x += 12 * U) p.line(x, bot + 1, x - 7 * U, bot + 8 * U);
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(left, top, D.bw, D.bh);
    force(D.bx, D.by, 0, M.G * S);                                        // G from the centre, down
    lab('$\\overline{G}$', D.bx + 20 * U, D.by + M.G * S - 2, 'c', fh, RED);
    force(D.bx + 18 * U, bot, 0, -M.N * S);                               // N from the bottom face, up
    lab('$\\overline{N}$', D.bx + 40 * U, bot - M.N * S + fh * 0.6, 'c', fh, RED);
    const Lf = M.Fmu * S;
    if (Lf > 2) force(left, bot, -Lf, 0);                                 // friction from the bottom corner, towards the centre
    lab('$\\overline{F}_\\mu$', left - Math.max(Lf, 20) / 2, bot + fh * 1.4, 'c', fh, RED);
    const ax = left - 8 * U, ay = D.by - D.bh * 0.2;                     // the acceleration beside the body, left of it
    thin(ax, ay, ax - 46 * U, ay, ORANGE);
    lab('$\\overline{a}$', ax - 23 * U, ay - fh * 0.45, 'c', fh, ORANGE);
    // the bar: friction needed (m v²/r) against the limit μ0 mg; the bar's full width is the weight G
    const bw = D.barW, X0 = D.barX, y = D.barY, bh = (narrow ? 20 : 14) * U, sc = bw / M.G;
    lab(__('tarve'), X0, y - bh / 2 - fh * 0.5, 'l', fh, INKC);
    p.noStroke(); p.fill(236, 232, 222); p.rect(X0, y - bh / 2, bw, bh);
    const wt = Math.min(bw, M.Ft * sc);
    p.fill(...(M.pito ? GREEN : RED)); p.rect(X0, y - bh / 2, wt, bh);
    if (M.Ft * sc > bw) { p.triangle(X0 + bw + 2, y - bh / 2 - 2, X0 + bw + 2, y + bh / 2 + 2, X0 + bw + 12 * U, y); }
    const xm = X0 + M.Fmax * sc;
    p.stroke(...INKC); p.strokeWeight(2.5 * U); p.line(xm, y - bh / 2 - 6 * U, xm, y + bh / 2 + 6 * U);
    lab('$\\mu_0 m g$', Math.max(X0 + 30 * U, Math.min(X0 + bw - 30 * U, xm)), y + bh / 2 + fh * 1.5, 'c', fh, INKC);
  }
  function force(x, y, dx, dy) {                                          // a force: a solid red arrow with a filled head
    const L = Math.hypot(dx, dy); if (L < 1) return;
    const a = Math.atan2(dy, dx), H = Math.min(12 * U, L * 0.7), x2 = x + dx, y2 = y + dy;
    p.stroke(...RED); p.strokeWeight(3.2 * U); p.line(x, y, x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
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
    c.fillStyle = gr; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
