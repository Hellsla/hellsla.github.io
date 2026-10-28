// fy1-5 Tasainen liike ja (t,s)-kuvaaja: a cart drives along a straight track at a constant speed and draws the (t,s) graph.
// Model: uniform motion, s = s0 + v t (constant v, no friction, no acceleration, the cart starts at full speed). Controls:
// the starting position s0 (0…10 m), the speed v (0,5…5,0 m/s) and the clock t (0…10 s). Changing s0 or v restarts the run.
// The student reads positions off the track and the graph; the sim shows s and the distance travelled Δs = s − s0, never a
// ratio, so the pattern (s/t constant only when s0 = 0; Δs/t = v always) is for the student to find.
// Time: the slider "Hetki t" scrubs 0…10 s; the main button plays it in simulated time (dt·speed), so "Nopeus (toisto)"
// changes only the pace. The graph is drawn for the times visited so far (tmax); dots mark whole seconds. Once t = 6 s has
// been visited, the slope triangle between t = 2 s and t = 6 s shows Δs / Δt = v on the graph.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode, 600×400.
new p5((p) => {
  const T = 10, SMAX = 60;                                               // run time (s), visible track and graph range (m)
  const COL = [232, 118, 28];                                            // orange = the cart, in the track, the arrow and the graph
  const LANE = { y: 40, h: 40, x0: 36, x1: 496 };                        // road
  const RULER_Y = 116;
  const G = { x0: 74, x1: 520, y0: 345, y1: 185 };                       // graph box: t 0…10, s 0…60
  let btn, sS0, lS0, sV, lV, sT, lT, selSp, readout;
  let tau = 0, tmax = 0, running = false, k = 1, labels = [];

  const X = (s) => LANE.x0 + s / SMAX * (LANE.x1 - LANE.x0);             // track pixel of position s
  const GX = (t) => G.x0 + t / T * (G.x1 - G.x0), GY = (s) => G.y0 - s / SMAX * (G.y0 - G.y1);

  const restart = () => { tau = 0; tmax = 0; running = false; sT.value(0); };
  const toTime = (t) => { tau = Math.min(T, Math.max(0, Number(t))); tmax = Math.max(tmax, tau); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (tau >= T) { tau = 0; tmax = 0; }                                // replay from the start
      running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const slider = (min, max, val, step) => {
      const label = p.createElement('label').parent(controls);
      const span = p.createSpan('').parent(label).style('white-space', 'nowrap');
      return [p.createSlider(min, max, val, step).parent(label), span];
    };
    [sS0, lS0] = slider(0, 10, 0, 1);                                     // starting position s0 (m)
    [sV, lV] = slider(0.5, 5, 2, 0.5);                                    // speed v (m/s)
    [sT, lT] = slider(0, T, 0, 0.5);                                      // the clock t (s)
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus_toisto')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                  // pace only; every quantity follows simulated time
    for (const e of [sS0.elt, sV.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    const scrub = () => { running = false; toTime(sT.value()); };         // the student drags the clock: playback stops
    sT.elt.addEventListener('input', scrub); sT.elt.addEventListener('change', scrub);
    p.createP(__('lippu_alkupaikka')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { s0: { input: sS0.elt, unit: 'm' }, v: { input: sV.elt, unit: 'm/s' }, t: { input: sT.elt, unit: 's' } },
      reset: () => { sS0.value(0); sV.value(2); selSp.selected('1'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s0 = Number(sS0.value()), v = Number(sV.value()), speed = Number(selSp.value());
    if (running) { toTime(tau + Math.min(p.deltaTime, 100) / 1000 * speed); sT.value(tau); if (tau >= T) running = false; }
    const pos = (t) => s0 + v * t;                                        // the model: s = s0 + v t
    const s = pos(tau), ds = v * tau;
    lS0.html(__('alkupaikka', {s0: tx(s0, 0)})); lV.html(__('kappaleen_nopeus', {v: tx(v, 1)})); lT.html(__('hetki', {t: tx(tau, 1)}));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const tri = tmax >= 6 - 1e-9;                                         // the slope triangle needs the graph up to 6 s
    readout.html(__('hetki_paikka', {t: tx(tau, 1), s: tx(s, 1)}) + __('matka_alusta', {ds: tx(ds, 1)}) +
      (tri ? __('kulmakerroin', {ds: tx(pos(6) - pos(2), 1), v: tx(v, 1)}) : ''));
    window.simState = { s0, v, t: tau, s, ds, tmax, running, speed, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(11);
    labels = [];
    p.background(250);
    track(s0, v, pos, ts, fh);
    graph(s0, v, pos, tri, fh);
    window.simState.labels = labels;
  };

  // --- the track: sky, road, start flag, ruler, stroboscopic marks, the cart with its velocity arrow ---
  function track(s0, v, pos, ts, fh) {
    grect(0, 0, 600, RULER_Y - 6, [[196, 224, 250], [238, 247, 255]], false, 0);
    grect(LANE.x0 - 8, LANE.y, LANE.x1 - LANE.x0 + 16, LANE.h, [[96, 100, 108], [72, 76, 84]], false, 4);
    p.stroke(255, 255, 255, 120); p.strokeWeight(1.5); p.drawingContext.setLineDash([8, 8]); p.line(LANE.x0, LANE.y + LANE.h - 6, LANE.x1, LANE.y + LANE.h - 6); p.drawingContext.setLineDash([]);
    // stroboscopic marks: where the cart was at every whole second visited so far
    p.strokeWeight(2); p.stroke(...COL, 190);
    for (let t = 0; t <= Math.min(T, Math.floor(tmax + 1e-9)); t++) { const px = X(pos(t)); p.line(px, LANE.y + 4, px, LANE.y + 13); }
    // start flag at s0: pole and green pennant
    const fx = X(s0);
    p.stroke(40); p.strokeWeight(2); p.line(fx, LANE.y - 20, fx, LANE.y + 2);
    p.noStroke(); p.fill(43, 138, 62); p.triangle(fx, LANE.y - 20, fx + 14, LANE.y - 14, fx, LANE.y - 8);
    const cx = X(pos(tau)), cy = LANE.y + 30;
    cartShape(cx, cy, v * tau * 0.9);
    arrow(cx, LANE.y + 15, cx + v * 11, LANE.y + 15);
    // ruler
    p.stroke(60); p.strokeWeight(1.5); p.line(X(0), RULER_Y, X(SMAX), RULER_Y);
    for (let m = 0; m <= SMAX; m += 5) { p.strokeWeight(m % 10 === 0 ? 1.5 : 1); p.line(X(m), RULER_Y, X(m), RULER_Y + (m % 10 === 0 ? 7 : 4)); }
    for (let m = 0; m <= SMAX; m += 10) lab(`$${m}$`, X(m), RULER_Y + 8 + fh, 'c', fh);
    lab('$s\\ (\\text{m})$', X(SMAX) + ts(16), RULER_Y + 8 + fh, 'l', fh);
  }

  // the cart: gradient body and cabin, two wheels with spokes that turn with the distance driven
  function cartShape(cx, cy, rot) {
    grect(cx - 17, cy - 10, 34, 12, [COL.map((q) => Math.min(255, q + 45)), COL], false, 3);
    grect(cx - 8, cy - 17, 16, 8, [[235, 245, 255], [170, 200, 230]], false, 2);
    for (const wx of [cx - 10, cx + 10]) {
      p.fill(35); p.stroke(20); p.strokeWeight(1); p.circle(wx, cy + 4, 11);
      p.stroke(190); p.strokeWeight(1.2); p.line(wx - 4 * Math.cos(rot), cy + 4 - 4 * Math.sin(rot), wx + 4 * Math.cos(rot), cy + 4 + 4 * Math.sin(rot));
    }
  }
  function arrow(x1, y1, x2, y2) {
    p.stroke(255, 255, 255, 220); p.strokeWeight(6); p.line(x1, y1, x2, y2);
    p.stroke(...COL); p.strokeWeight(3.5); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 8;
    p.fill(...COL); p.stroke(255, 255, 255, 220); p.strokeWeight(1.5);
    p.triangle(x2 + 3 * Math.cos(a), y2 + 3 * Math.sin(a), x2 - L * Math.cos(a - 0.5), y2 - L * Math.sin(a - 0.5), x2 - L * Math.cos(a + 0.5), y2 - L * Math.sin(a + 0.5));
  }

  // --- the (t,s) graph: gridlines, the line drawn so far, whole-second dots, slope triangle, the present moment ---
  function graph(s0, v, pos, tri, fh) {
    p.noStroke(); p.fill(255); p.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1);
    p.stroke(228); p.strokeWeight(1);
    for (let t = 1; t <= T; t++) p.line(GX(t), G.y0, GX(t), G.y1);
    for (let m = 10; m <= SMAX; m += 10) p.line(G.x0, GY(m), G.x1, GY(m));
    p.noFill(); p.stroke(...COL); p.strokeWeight(3.2); p.strokeJoin(p.ROUND);
    if (tmax > 0) { p.beginShape(); for (let t = 0; t < tmax - 1e-9; t += 0.1) p.vertex(GX(t), GY(pos(t))); p.vertex(GX(tmax), GY(pos(tmax))); p.endShape(); }
    p.stroke(255); p.strokeWeight(1.5); p.fill(...COL);
    for (let t = 0; t <= Math.min(T, Math.floor(tmax + 1e-9)); t++) p.circle(GX(t), GY(pos(t)), 8);
    if (tri) {                                                            // slope triangle: right angle above the line, t = 2 s … 6 s
      const xa = GX(2), xb = GX(6), ya = GY(pos(2)), yb = GY(pos(6));
      p.stroke(40); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 4]); p.noFill();
      p.line(xa, ya, xa, yb); p.line(xa, yb, xb, yb); p.drawingContext.setLineDash([]);
      lab('$\\Delta t$', (xa + xb) / 2, yb - 6, 'c', fh);
      lab('$\\Delta s$', xa - 8, ya - yb > 2.2 * fh ? (ya + yb) / 2 + fh * 0.36 : yb - 4, 'r', fh);
    }
    // the present moment: a dashed vertical line and a ring on the line
    p.stroke(90); p.strokeWeight(1.2); p.drawingContext.setLineDash([5, 5]); p.line(GX(tau), G.y0, GX(tau), G.y1); p.drawingContext.setLineDash([]);
    p.fill(255); p.stroke(...COL); p.strokeWeight(3); p.circle(GX(tau), GY(pos(tau)), 12);
    if (s0 > 0) { p.fill(255); p.stroke(43, 138, 62); p.strokeWeight(3); p.circle(G.x0, GY(s0), 12); }   // the starting position on the s axis
    // axes
    p.stroke(60); p.strokeWeight(1.5); p.noFill(); p.line(G.x0, G.y0, G.x1 + 8, G.y0); p.line(G.x0, G.y0, G.x0, G.y1 - 8);
    p.noStroke(); p.fill(60);
    p.triangle(G.x1 + 14, G.y0, G.x1 + 6, G.y0 - 4, G.x1 + 6, G.y0 + 4); p.triangle(G.x0, G.y1 - 14, G.x0 - 4, G.y1 - 6, G.x0 + 4, G.y1 - 6);
    for (let t = 0; t <= T; t += 2) lab(`$${t}$`, GX(t), G.y0 + 4 + fh, 'c', fh);
    for (let m = 10; m <= SMAX; m += 10) lab(`$${m}$`, G.x0 - 8, GY(m) + fh * 0.36, 'r', fh);
    lab('$t\\ (\\text{s})$', G.x1 + 24, G.y0 + 4 + fh, 'l', fh);
    lab('$s\\ (\\text{m})$', G.x0 + 10, G.y1 + 4 + fh, 'l', fh);   // axis title inside the plot's top-left corner, clear of the tick numbers
  }

  // every canvas text: its ink box is pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  // gradient fill (raw canvas, inside save/restore so p5's own fill state is untouched) with a thin outline
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const g = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => g.addColorStop(i / (stops.length - 1), `rgb(${s.map((q) => Math.min(255, Math.round(q))).join(',')})`));
    c.fillStyle = g; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');                  // Finnish decimal comma inside LaTeX
});
