// fy4-12 Kahden kappaleen liike: kohtaaminen ja ohitus: a car (A) and a cyclist (B) on one straight road, their positions on
// one shared ruler (the x axis) and their (t,x) graphs in one coordinate system.
// Model: each body moves with a constant acceleration, x = x0 + v0 t + a t²/2, v = v0 + a t (a = 0 for a uniform motion);
// no friction, no air drag, bodies are points on the x axis (they pass through each other without touching).
// Five cases: 1 head-on, uniform; 2 chase, uniform; 3 the car starts from rest and catches the cyclist; 4 the cyclist
// ahead is faster, so they never meet; 5 a bus starts from rest in front of a runner, which gives two meetings.
// Colours (teacher 2026-10-29): velocity arrows blue, acceleration arrows orange, never a body's colour; body A green, body B brown.
// Time: the slider "Hetki t" scrubs 0…12 s; the main button plays it in simulated time (dt·speed), so the speed select
// changes only the pace. The graph is drawn for the times visited so far (tmax); a ring marks each meeting once it is reached.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const T = 12;                                                          // run time (s)
  const CASES = {                                                        // A: the car, B: the cyclist; x0 (m), v0 (m/s), a (m/s²)
    '1': { A: { x0: 10, v0: 4, a: 0 }, B: { x0: 70, v0: -2, a: 0 }, xmin: -5, xmax: 85, tick: 20 },
    '2': { A: { x0: 0, v0: 7, a: 0 }, B: { x0: 20, v0: 3, a: 0 }, xmin: -5, xmax: 105, tick: 20 },
    '3': { A: { x0: 0, v0: 0, a: 2 }, B: { x0: 16, v0: 6, a: 0 }, xmin: -5, xmax: 155, tick: 30 },
    '4': { A: { x0: 0, v0: 3, a: 0 }, B: { x0: 20, v0: 5, a: 0 }, xmin: -5, xmax: 85, tick: 20 },
    '5': { A: { x0: 0, v0: 0, a: 1 }, B: { x0: -5, v0: 4, a: 0 }, xmin: -10, xmax: 85, tick: 20 },
  };
  const COL = { A: [43, 138, 62], B: [138, 95, 34] }, BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51];
  // Two layouts (NOTES.md §4 "Readable on a phone"): 600×400 side by side on a wide screen; on a phone (#sim-root narrower
  // than 500 px) the canvas is 600×575, the road and the (t,x) graph each at the full width, one under the other.
  const WIDE = { lane: { x0: 24, x1: 520, yA: 8, yB: 122, h: 56 }, ruler: 84, g: { x0: 78, x1: 470, y0: 356, y1: 204 }, H: 400 };
  const NARROW = { lane: { x0: 24, x1: 505, yA: 8, yB: 126, h: 56 }, ruler: 84, g: { x0: 62, x1: 490, y0: 476, y1: 252 }, H: 575 };
  let LANE = WIDE.lane, RULER_Y = WIDE.ruler, G = WIDE.g, narrow = false, CH = 400;   // road lanes, ruler row, graph box (t 0…12, x xmin…xmax), layout, canvas height
  let btn, sl, lSl, selCase, selSp, readout;
  let fixing = false, curH = 400, tau = 0, tmax = 0, running = false, k = 1, K = 1, labels = [];   // k: canvas px per CSS px; K: stroke/marker scale on a narrow screen

  // --- the physics: position and velocity of a body at time t ---
  const pos = (c, t) => c.x0 + c.v0 * t + 0.5 * c.a * t * t;
  const vel = (c, t) => c.v0 + c.a * t;
  const meetings = (cs) => {                                             // the times 0 < t ≤ T with x_A = x_B: a t²/2 + b t + c = 0
    const q = 0.5 * (cs.A.a - cs.B.a), b = cs.A.v0 - cs.B.v0, c = cs.A.x0 - cs.B.x0, out = [];
    if (Math.abs(q) < 1e-12) { if (Math.abs(b) > 1e-12) out.push(-c / b); }
    else { const d = b * b - 4 * q * c; if (d >= 0) { out.push((-b - Math.sqrt(d)) / (2 * q), (-b + Math.sqrt(d)) / (2 * q)); } }
    return out.filter((t) => t > 1e-9 && t <= T + 1e-9).sort((u, w) => u - w);
  };
  let cs = CASES['1'];
  const X = (x) => LANE.x0 + (x - cs.xmin) / (cs.xmax - cs.xmin) * (LANE.x1 - LANE.x0);
  const GX = (t) => G.x0 + t / T * (G.x1 - G.x0), GY = (x) => G.y0 - (x - cs.xmin) / (cs.xmax - cs.xmin) * (G.y0 - G.y1);

  const restart = () => { tau = 0; tmax = 0; running = false; sl.value(0); };
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
    const lc = p.createElement('label').parent(controls); p.createSpan(__('tapaus')).parent(lc); selCase = p.createSelect().parent(lc);
    selCase.option(__('1_kohtaaminen'), '1'); selCase.option(__('2_ohitus_tasaisesti'), '2'); selCase.option(__('3_auto_lahtee_levosta'), '3');
    selCase.option(__('4_ei_ohitusta'), '4'); selCase.option(__('5_juoksija_ja_bussi'), '5');
    const lt = p.createElement('label').parent(controls); lSl = p.createSpan('').parent(lt);
    sl = p.createSlider(0, T, 0, 0.5).parent(lt);
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus_toisto')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                  // pace only; every quantity follows simulated time
    for (const e of [selCase.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    const scrub = () => { running = false; toTime(sl.value()); };         // the student drags the clock: playback stops
    sl.elt.addEventListener('input', scrub); sl.elt.addEventListener('change', scrub);
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { t: { input: sl.elt, unit: 's' }, tapaus: { input: selCase.elt, unit: '' } },
      reset: () => { selCase.selected('1'); selSp.selected('1'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const speed = Number(selSp.value()); cs = CASES[selCase.value()];
    if (running) { toTime(tau + Math.min(p.deltaTime, 100) / 1000 * speed); sl.value(tau); if (tau >= T) running = false; }
    const A = cs.A, B = cs.B, xA = pos(A, tau), xB = pos(B, tau), vA = vel(A, tau), vB = vel(B, tau), mt = meetings(cs);
    lSl.html(__('hetki', { tau: tx(tau, 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat_t', { tau: tx(tau, 1) }) +
      __('lukemat_a', { xa: tx(xA, 1), va: tx(vA, 1), aa: tx(A.a, 1) }) +
      __('lukemat_b', { xb: tx(xB, 1), vb: tx(vB, 1), ab: tx(B.a, 1) }) +
      __('lukemat_ero', { gap: tx(xB - xA, 1) }));
    window.simState = { tapaus: selCase.value(), t: tau, xA, xB, vA, vB, aA: A.a, aB: B.a, gap: xB - xA,
      meetings: mt.filter((m) => m <= tmax + 1e-9).length, tmax, running, speed, labels: null };

    narrow = document.getElementById('sim-root').clientWidth < 500;
    ({ lane: LANE, ruler: RULER_Y, g: G, H: CH } = narrow ? NARROW : WIDE);
    if (curH !== CH && !fixing) { fixing = true; setTimeout(() => { fixing = false; curH = CH; p.resizeCanvas(600, CH, true); p.redraw(); }, 0); }   // sim-embed.js keeps the 600 width and scales the box
    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    K = Math.min(k, 1.6);
    const ts = (x) => Math.round(x * k), fh = ts(14);                    // 14 CSS px labels at every width
    labels = [];
    p.background(250);
    track(A, B, ts, fh);
    graph(A, B, mt, ts, fh);
    window.simState.labels = labels;
  };

  // --- the road: two lanes above and below one shared ruler, vehicles with velocity (blue) and acceleration (orange) arrows ---
  function track(A, B, ts, fh) {
    grect(0, 0, 600, 192, [[196, 224, 250], [238, 247, 255]], false, 0);
    for (const [y, c, cart, who] of [[LANE.yA, COL.A, A, 'A'], [LANE.yB, COL.B, B, 'B']]) {
      grect(LANE.x0 - 6, y, LANE.x1 - LANE.x0 + 12, LANE.h, [[96, 100, 108], [72, 76, 84]], false, 4);
      p.stroke(255, 255, 255, 120); p.strokeWeight(1.5); p.drawingContext.setLineDash([8, 8]); p.line(LANE.x0, y + LANE.h - 3, LANE.x1, y + LANE.h - 3); p.drawingContext.setLineDash([]);
      const x = pos(cart, tau), v = vel(cart, tau), cx = X(x), dir = v < 0 || (v === 0 && cart.v0 < 0) ? -1 : 1;
      if (who === 'A') carShape(cx, y + LANE.h - 6, dir, c, x); else cycleShape(cx, y + LANE.h - 6, dir, c, x);
      if (Math.abs(v) > 0.05) arrow(cx, y + 11, cx + Math.sign(v) * (Math.abs(v) * 2.8 + 6), y + 11, BLUE);
      if (Math.abs(cart.a) > 0.05) arrow(cx, y + 25, cx + Math.sign(cart.a) * (Math.abs(cart.a) * 16 + 6), y + 25, ORANGE);
      // lane badge: the body's letter in its colour
      p.noStroke(); p.fill(...c); p.circle(11 * K, y + 14, 18 * K);
      lab(`$\\text{${who}}$`, 11 * K, y + 14 + fh * 0.36, 'c', fh, [255, 255, 255], true);
    }
    // the shared ruler (the x axis) with a marker for each body: A points down at it from above, B up at it from below
    p.stroke(60); p.strokeWeight(1.5); p.line(X(cs.xmin), RULER_Y, X(cs.xmax), RULER_Y);
    for (let m = 0; m <= cs.xmax; m += cs.tick / 2) { p.strokeWeight(m % cs.tick === 0 ? 1.5 : 1); p.line(X(m), RULER_Y, X(m), RULER_Y + (m % cs.tick === 0 ? 7 : 4)); }
    for (let m = Math.ceil(cs.xmin / cs.tick) * cs.tick; m <= cs.xmax; m += cs.tick) lab(`$${m}$`, X(m), RULER_Y + 10 + fh, 'c', fh);
    lab('$x\\ (\\text{m})$', 598, RULER_Y + 10 + fh, 'r', fh);
    p.noStroke(); p.fill(...COL.A); p.triangle(X(pos(A, tau)) - 6, RULER_Y - 12, X(pos(A, tau)) + 6, RULER_Y - 12, X(pos(A, tau)), RULER_Y - 1);
    p.fill(...COL.B); p.triangle(X(pos(B, tau)) - 6, RULER_Y + 12, X(pos(B, tau)) + 6, RULER_Y + 12, X(pos(B, tau)), RULER_Y + 1);
  }

  // a car: gradient body and cabin, two wheels with spokes that turn with the distance driven; dir mirrors it
  function carShape(cx, base, dir, c, x) {
    p.push(); p.translate(cx, base); p.scale(dir, 1);
    grect(-19, -18, 38, 12, [c.map((q) => Math.min(255, q + 45)), c], false, 3);
    grect(-9, -26, 18, 9, [[235, 245, 255], [170, 200, 230]], false, 2);
    for (const wx of [-11, 11]) {
      p.fill(35); p.stroke(20); p.strokeWeight(1); p.circle(wx, -5, 11);
      p.stroke(190); p.strokeWeight(1.2); p.line(wx - 4 * Math.cos(x * 0.9), -5 - 4 * Math.sin(x * 0.9), wx + 4 * Math.cos(x * 0.9), -5 + 4 * Math.sin(x * 0.9));
    }
    p.pop();
  }
  // a cyclist: two wheels, a frame in the body's colour, a rider with a helmet
  function cycleShape(cx, base, dir, c, x) {
    p.push(); p.translate(cx, base); p.scale(dir, 1);
    for (const wx of [-11, 11]) {
      p.noFill(); p.stroke(30); p.strokeWeight(2); p.circle(wx, -8, 16);
      p.stroke(150); p.strokeWeight(1); p.line(wx - 7 * Math.cos(x * 0.8), -8 - 7 * Math.sin(x * 0.8), wx + 7 * Math.cos(x * 0.8), -8 + 7 * Math.sin(x * 0.8));
    }
    p.stroke(...c); p.strokeWeight(2.5); p.line(-11, -8, -2, -18); p.line(-2, -18, 8, -18); p.line(8, -18, 11, -8); p.line(-2, -18, 0, -8); p.line(0, -8, -11, -8); p.line(8, -18, 7, -23);
    p.stroke(60); p.strokeWeight(4); p.line(-3, -20, 4, -30);                                     // the rider's body
    p.noStroke(); p.fill(242, 214, 170); p.circle(6, -34, 8); p.fill(201, 42, 42); p.arc(6, -35, 9, 9, Math.PI, 2 * Math.PI);
    p.pop();
  }
  function arrow(x1, y1, x2, y2, c) {
    p.stroke(255, 255, 255, 220); p.strokeWeight(6 * K); p.line(x1, y1, x2, y2);
    p.stroke(...c); p.strokeWeight(3.5 * K); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 8 * K;
    p.fill(...c); p.stroke(255, 255, 255, 220); p.strokeWeight(1.5);
    p.triangle(x2 + 3 * Math.cos(a), y2 + 3 * Math.sin(a), x2 - L * Math.cos(a - 0.5), y2 - L * Math.sin(a - 0.5), x2 - L * Math.cos(a + 0.5), y2 - L * Math.sin(a + 0.5));
  }

  // --- the (t,x) graph: gridlines, the lines drawn so far, whole-second dots, the present moment, a ring at each meeting ---
  function graph(A, B, mt, ts, fh) {
    p.noStroke(); p.fill(255); p.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1);
    p.stroke(228); p.strokeWeight(1);
    for (let s = 2; s <= T; s += 2) p.line(GX(s), G.y0, GX(s), G.y1);
    for (let m = Math.ceil(cs.xmin / cs.tick) * cs.tick; m <= cs.xmax; m += cs.tick) p.line(G.x0, GY(m), G.x1, GY(m));
    p.stroke(150); p.strokeWeight(1.5 * K); p.line(G.x0, GY(0), G.x1, GY(0));            // x = 0
    for (const [c, cart] of [[COL.A, A], [COL.B, B]]) {
      p.noFill(); p.stroke(...c); p.strokeWeight(3.2 * K); p.strokeJoin(p.ROUND);
      if (tmax > 0) { p.beginShape(); for (let s = 0; s < tmax - 1e-9; s += 0.1) p.vertex(GX(s), GY(pos(cart, s))); p.vertex(GX(tmax), GY(pos(cart, tmax))); p.endShape(); }
      p.stroke(255); p.strokeWeight(1.5); p.fill(...c);
      for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) { if (cart === A) p.circle(GX(s), GY(pos(cart, s)), 8 * K); else p.rect(GX(s) - 4 * K, GY(pos(cart, s)) - 4 * K, 8 * K, 8 * K, 1.5); }
    }
    // the present moment: a dashed vertical line and a ring on each line
    p.stroke(90); p.strokeWeight(1.2); p.drawingContext.setLineDash([5, 5]); p.line(GX(tau), G.y0, GX(tau), G.y1); p.drawingContext.setLineDash([]);
    for (const [c, cart] of [[COL.A, A], [COL.B, B]]) { p.fill(255); p.stroke(...c); p.strokeWeight(3 * K); p.circle(GX(tau), GY(pos(cart, tau)), 12 * K); }
    // each meeting reached so far: a black ring where the two lines cross
    for (const m of mt) if (m <= tmax + 1e-9) { p.noFill(); p.stroke(...INKC); p.strokeWeight(2.5 * K); p.circle(GX(m), GY(pos(A, m)), 20 * K); }
    // axes
    p.stroke(60); p.strokeWeight(1.5 * K); p.noFill(); p.line(G.x0, G.y0, G.x1 + 8, G.y0); p.line(G.x0, G.y0, G.x0, G.y1 - 8);
    p.noStroke(); p.fill(60);
    p.triangle(G.x1 + 14, G.y0, G.x1 + 6, G.y0 - 4, G.x1 + 6, G.y0 + 4); p.triangle(G.x0, G.y1 - 14, G.x0 - 4, G.y1 - 6, G.x0 + 4, G.y1 - 6);
    for (let s = 0; s <= T; s += 2) lab(`$${s}$`, GX(s), G.y0 + (narrow ? 10 : 4) + fh, 'c', fh);
    const ystep = Math.max(1, Math.ceil(1.3 * fh / ((G.y0 - G.y1) * cs.tick / (cs.xmax - cs.xmin))));   // thin the x ticks when 14 px labels would touch
    for (let m = Math.ceil(cs.xmin / cs.tick) * cs.tick, i = 0; m <= cs.xmax; m += cs.tick, i++) if (i % ystep === 0) lab(`$${m}$`, G.x0 - 8, GY(m) + fh * 0.36, 'r', fh);
    lab('$t\\ (\\text{s})$', G.x1 + (narrow ? 26 : 20), G.y0 + (narrow ? 10 : 4) + fh, 'l', fh);
    lab('$x\\ (\\text{m})$', G.x0 + 8, G.y1 - (narrow ? 16 : 10), 'l', fh);
    // legend: bodies (graph colours and markers) and the two arrows
    const ll = 24 * K, dy = ts(20);
    const slot = (i) => narrow ? [60 + i * 135, G.y0 + 10 + fh + 40] : [490, 208 + 4 * K + i * dy];   // a row under the graph on a phone, a column beside it otherwise
    let [lx, ly] = slot(0);
    p.stroke(...COL.A); p.strokeWeight(3.2 * K); p.line(lx, ly, lx + ll, ly); p.fill(...COL.A); p.stroke(255); p.strokeWeight(1.5); p.circle(lx + ll / 2, ly, 8 * K);
    [lx, ly] = slot(1);
    p.stroke(...COL.B); p.strokeWeight(3.2 * K); p.line(lx, ly, lx + ll, ly); p.fill(...COL.B); p.stroke(255); p.strokeWeight(1.5); p.rect(lx + ll / 2 - 4 * K, ly - 4 * K, 8 * K, 8 * K, 1.5);
    [lx, ly] = slot(2); arrow(lx, ly, lx + ll, ly, BLUE);
    [lx, ly] = slot(3); arrow(lx, ly, lx + ll, ly, ORANGE);
    [['$\\text{A}$', 0], ['$\\text{B}$', 1], ['$\\overline{v}$', 2], ['$\\overline{a}$', 3]].forEach(([s, i]) => { const [x, y] = slot(i); lab(s, x + ll + 10, y + fh * 0.36, 'l', fh); });
  }

  // every canvas text: drawn at its place, its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col, plain) {
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
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');            // Finnish decimal comma inside LaTeX
});
