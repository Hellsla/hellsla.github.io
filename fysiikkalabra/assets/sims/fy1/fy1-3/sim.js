// fy1-3 Mittaaminen ja mittauksen luotettavuus: a ball rolls down a ramp and a hand stopwatch gives a reading each time.
// Model: the true rolling time is T = 2,40 s. Reading i is t_i = T + δ_sys + δ_sat · g_i, rounded to the stopwatch's 0,01 s,
// where δ_sys is a constant (systematic) error and g_i is a fixed series of standard random deviates (the same series on
// every run, so a table made today can be checked tomorrow). The slider n shows the first n readings of the series.
// The student sees the readings pile up as a dot plot, the mean, and the true value (known only in the model).
// Time: the main button plays the measurements one by one in simulated time (dt·speed); "Nopeus (toisto)" changes only the pace.
// Colour carries meaning: blue dots = readings, orange dot = the latest reading, ink line = mean, green dashes = true value T.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const T = 2.4, NMAX = 40, DM = 0.8, TMIN = 1.4, TMAX = 3.4, BIN = 0.04;       // true time (s), readings, seconds per measurement, axis (s), dot bin (s)
  const G = [-1.456, 0.349, 1.893, 1.797, -0.027, 0.952, 1.758, -0.424, 0.468, -0.802, -0.526, 1.699, 1.314, 0.066, 0.709, -1.129,
    -0.944, -0.639, 0.965, -1.381, -0.978, 0.13, 0.198, -0.042, 1.333, -0.149, -0.148, -1.166, -0.816, 0.345, 0.271, 0.053,
    -1.585, -1.344, 0.406, 0.146, -0.705, 0.644, -1.141, -0.113];                // standard normal deviates, fixed
  const BLUE = [25, 113, 194], ORANGE = [232, 89, 12], GREEN = [43, 138, 62], INK = [31, 41, 51];
  const PX = { x0: 30, x1: 510, yB: 338 };                                       // dot plot: t axis from x0 (1,4 s) to x1 (3,4 s), baseline y
  const RAMP = { x0: 44, y0: 58, x1: 330, y1: 110 };                             // top and bottom of the ramp's upper surface
  let btn, sN, sSat, sSys, selSp, lN, lSat, lSys, readout;
  let n = 1, u = 0, running = false, k = 1, labels = [];

  const reading = (i, sat, sys) => Math.round((T + sys + sat * G[i]) * 100) / 100;      // reading i (0-based), stopwatch resolution 0,01 s
  const X = (t) => PX.x0 + (t - TMIN) / (TMAX - TMIN) * (PX.x1 - PX.x0);
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');                          // Finnish decimal comma inside LaTeX
  const sg = (x, d) => (x < -1e-9 ? '-' : '+') + tx(Math.abs(x), d);              // signed value for LaTeX

  const restart = () => { n = 1; u = 0; running = false; sN.value(1); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (n >= NMAX) { n = 1; sN.value(1); }                                      // replay from the start
      u = 0; running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const ln = p.createElement('label').parent(controls); lN = p.createSpan('').parent(ln);
    sN = p.createSlider(1, NMAX, 1, 1).parent(ln);
    const la = p.createElement('label').parent(controls); lSat = p.createSpan('').parent(la);
    sSat = p.createSlider(0, 0.3, 0.15, 0.05).parent(la);
    const lb = p.createElement('label').parent(controls); lSys = p.createSpan('').parent(lb);
    sSys = p.createSlider(-0.3, 0.3, 0, 0.05).parent(lb);
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus_toisto')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                          // pace only; every quantity follows simulated time
    const scrub = () => { running = false; u = 0; n = Math.max(1, Math.min(NMAX, Math.round(Number(sN.value())))); };
    sN.elt.addEventListener('input', scrub); sN.elt.addEventListener('change', scrub);
    p.createP(__('legenda')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { n: { input: sN.elt, unit: '' }, sat: { input: sSat.elt, unit: 's' }, sys: { input: sSys.elt, unit: 's' } },
      reset: () => { sSat.value(0.15); sSys.value(0); selSp.selected('1'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const speed = Number(selSp.value()), sat = Number(sSat.value()), sys = Number(sSys.value());
    if (running) {
      u += Math.min(p.deltaTime, 100) / 1000 * speed / DM;
      if (u >= 1) { u = 0; n = Math.min(NMAX, n + 1); sN.value(n); if (n >= NMAX) running = false; }
    }
    const rs = []; for (let i = 0; i < n; i++) rs.push(reading(i, sat, sys));
    const mean = rs.reduce((a, b) => a + b, 0) / n, tmin = Math.min(...rs), tmax = Math.max(...rs);
    lN.html(__('toistot', { n: n })); lSat.html(__('satunnaisvirhe', { v: tx(sat, 2) })); lSys.html(__('systemaattinen', { v: sg(sys, 2) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukema_rivi', { n: n, t: tx(rs[n - 1], 2) }) + __('keskiarvo_rivi', { m: tx(mean, 3), lo: tx(tmin, 2), hi: tx(tmax, 2) }) +
      __('puolikas_rivi', { d: tx((tmax - tmin) / 2, 3), e: sg(mean - T, 3) }));
    window.simState = { n, T, sat, sys, last: rs[n - 1], mean, tmin, tmax, puoli: (tmax - tmin) / 2, vir: mean - T, rs, running, speed, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    p.background(250);
    scene(rs, sat, sys, fh);
    plot(rs, mean, fh);
    window.simState.labels = labels;
  };

  // --- the ramp, the ball and the stopwatch ---
  function scene(rs, sat, sys, fh) {
    grect(0, 0, 600, 128, [[196, 224, 250], [238, 247, 255]], false, 0);
    grect(0, 128, 600, 24, [[176, 132, 88], [134, 96, 60]], false, 0);
    const dx = RAMP.x1 - RAMP.x0, dy = RAMP.y1 - RAMP.y0, L = Math.hypot(dx, dy), th = Math.atan2(dy, dx);
    // support under the ramp's upper end, then the board
    grect(RAMP.x0 + 6, RAMP.y0 + 12, 22, 128 - RAMP.y0 - 12, [[205, 170, 120], [170, 132, 88]], true, 2);
    p.push(); p.translate(RAMP.x0, RAMP.y0); p.rotate(th); grect(-6, 0, L + 12, 11, [[222, 188, 140], [186, 148, 100]], false, 3); p.pop();
    // start gate and finish post with a flag, both on the board
    const nx = Math.sin(th), ny = -Math.cos(th), at = (f) => [RAMP.x0 + dx * f, RAMP.y0 + dy * f];
    p.stroke(INK[0], INK[1], INK[2]); p.strokeWeight(2);
    for (const [f, h] of [[0.05, 26], [1, 34]]) { const [px, py] = at(f); p.line(px, py, px + nx * h, py + ny * h); }
    const [fx, fy] = at(1); p.noStroke(); p.fill(43, 138, 62); p.triangle(fx + nx * 34, fy + ny * 34, fx + nx * 34 + 16, fy + ny * 34 + 5, fx + nx * 22, fy + ny * 22);
    // the ball rolls with uniform acceleration while a measurement is running, otherwise it rests at the bottom
    const roll = running ? Math.min(1, u / 0.75) : 1, phi = running ? roll * roll : 1;
    const f = 0.05 + 0.9 * phi, [bx, by] = at(f), r = 10, cx = bx + nx * r, cy = by + ny * r, ang = (phi * 0.9 * L) / r;
    p.noStroke(); p.fill(0, 0, 0, 40); p.ellipse(cx + 3, by + 1, 2 * r, 5);
    const c = p.drawingContext, g = c.createRadialGradient(cx - 3, cy - 3, 1, cx, cy, r);
    g.addColorStop(0, 'rgb(250,250,250)'); g.addColorStop(1, 'rgb(25,113,194)');
    c.save(); c.fillStyle = g; c.beginPath(); c.arc(cx, cy, r, 0, 2 * Math.PI); c.fill(); c.restore();
    p.stroke(255, 255, 255, 190); p.strokeWeight(1.5);
    p.line(cx + 6 * Math.cos(ang), cy + 6 * Math.sin(ang), cx - 6 * Math.cos(ang), cy - 6 * Math.sin(ang));
    // the stopwatch: LCD with the reading, which counts up while the ball rolls
    grect(392, 14, 156, 118, [[120, 128, 138], [70, 78, 88]], false, 14);
    grect(470 - 8, 4, 16, 12, [[190, 196, 204], [120, 128, 138]], false, 3);
    grect(406, 30, 128, 50, [[214, 232, 208], [188, 212, 184]], false, 6);
    const idx = running ? n + 1 : n, full = reading(idx - 1, sat, sys), shown = running ? full * Math.min(1, u / 0.75) : full;
    lab(`$${tx(shown, 2)}\\,\\text{s}$`, 470, 62, 'c', fh + 3, [25, 40, 25]);
    lab(`$t_{${idx}}$`, 470, 100 + 0.2 * fh, 'c', fh, [245, 245, 245]);
  }

  // --- the dot plot: readings stacked in 0,04 s bins, the mean and the true value ---
  function plot(rs, mean, fh) {
    const yT = 178, yM = yT + fh + 3, yTop = yM + 0.25 * fh + 8, yB = PX.yB;
    // markers behind the dots: true value (green dashes) and mean (ink line)
    p.drawingContext.setLineDash([6, 5]); p.stroke(...GREEN); p.strokeWeight(2.5); p.line(X(T), yT + 0.25 * fh + 2, X(T), yB); p.drawingContext.setLineDash([]);
    p.stroke(...INK); p.strokeWeight(2.5); p.line(X(mean), yM + 0.25 * fh + 2, X(mean), yB);
    // dots
    const bins = {}, nb = Math.round((TMAX - TMIN) / BIN);
    rs.forEach((v, i) => { const b = Math.max(0, Math.min(nb, Math.floor((v - TMIN) / BIN + 0.5 + 1e-9))); (bins[b] = bins[b] || []).push(i); });
    const maxc = Math.max(...Object.values(bins).map((a) => a.length)), d = Math.min(10, (PX.x1 - PX.x0) / nb - 1), step = Math.min(d + 1.5, (yB - 3 - yTop) / maxc);
    for (const b in bins) bins[b].forEach((i, j) => {
      const last = i === rs.length - 1, cx = X(TMIN + b * BIN), cy = yB - 2 - d / 2 - j * step;
      p.stroke(255); p.strokeWeight(1.5); p.fill(...(last ? ORANGE : BLUE)); p.circle(cx, cy, d);
    });
    // axis with arrowhead, ticks every 0,1 s, numbers every 0,4 s
    p.stroke(60); p.strokeWeight(2); p.line(PX.x0 - 12, yB, PX.x1 + 14, yB);
    p.noStroke(); p.fill(60); p.triangle(PX.x1 + 24, yB, PX.x1 + 14, yB - 4.5, PX.x1 + 14, yB + 4.5);
    for (let t = 1.4; t <= 3.4001; t += 0.1) { const big = Math.abs(((t - 1.4) / 0.4) % 1) < 1e-6 || Math.abs(((t - 1.4) / 0.4) % 1 - 1) < 1e-6; p.stroke(60); p.strokeWeight(big ? 2 : 1.2); p.line(X(t), yB, X(t), yB + (big ? 8 : 5)); }
    for (let t = 1.6; t <= 3.2001; t += 0.4) lab(`$${tx(t, 1)}$`, X(t), yB + 10 + fh, 'c', fh);
    lab('$t\\ (\\text{s})$', PX.x1 + 30, yB + 0.36 * fh, 'l', fh);
    // marker labels in their own rows above the dots
    lab('$T$', X(T), yT, 'c', fh, GREEN); lab('$\\bar{t}$', X(mean), yM, 'c', fh, INK);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates); sim-embed draws a $…$ string with KaTeX
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  // gradient fill (raw canvas, inside save/restore so p5's own fill state is untouched) with a thin outline
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const g = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => g.addColorStop(i / (stops.length - 1), `rgb(${s.map((v) => Math.min(255, Math.round(v))).join(',')})`));
    c.fillStyle = g; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
});
