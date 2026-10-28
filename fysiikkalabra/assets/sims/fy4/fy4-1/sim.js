// fy4-1 Paikka, nopeus ja tasainen liike kuvaajina: two carts on a straight track and the (t,x) graph their motion draws.
// Model: a cart moves with a constant velocity v (it starts at full speed, no friction, no acceleration), x = x₀ + v t.
// Case 4 is the exception: cart E drives out at v for 4 s, stands still for 2 s and returns at −v for 4 s, so it ends
// where it started (Δx = 0, path 16 m). The student reads positions off the track, the clock slider or the graph and
// finds the velocities from them: the velocities are not shown as numbers, only as arrows (direction and length).
// Time: the slider "Hetki t" scrubs 0…10 s; the main button plays it in simulated time (dt·speed), so the "Nopeus (toisto)"
// select changes only the pace. The graph is drawn for the times visited so far (tmax), dots mark whole seconds.
// Colour carries meaning: orange = cart A, blue = the other cart, in the track, the arrows, the graph and the legend.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const T = 10, XMIN = -5, XMAX = 45;                                    // run time (s), visible x range (m)
  const CASES = {                                                        // cart A is the same in every case
    '1': { name: 'B', B: { x0: 0, v: 4 } },
    '2': { name: 'C', B: { x0: 20, v: 2 } },
    '3': { name: 'D', B: { x0: 30, v: -3 } },
    '4': { name: 'E', B: { x0: 0, v: 2, back: true } },
  };
  const CART_A = { x0: 0, v: 2 };
  const COL = { A: [232, 118, 28], B: [38, 110, 214] };
  const LANE = { y: [34, 78], h: 40, x0: 30, x1: 570 };                  // road lanes of A and the other cart
  const RULER_Y = 126;
  const G = { x0: 74, x1: 520, y0: 350, y1: 190 };                       // graph box: t 0…10, x −5…45
  let btn, sl, lSl, selCase, lCase, selSp, readout;
  let tau = 0, tmax = 0, running = false, k = 1, labels = [];

  // --- the physics: position, velocity and path of a cart at time t ---
  const vel = (c, t) => (c.back ? (t < 4 ? c.v : t < 6 ? 0 : -c.v) : c.v);
  const pos = (c, t) => (c.back ? (t < 4 ? c.x0 + c.v * t : t < 6 ? c.x0 + 4 * c.v : c.x0 + 4 * c.v - c.v * (t - 6)) : c.x0 + c.v * t);
  const path = (c, t) => (c.back ? (t < 4 ? c.v * t : t < 6 ? 4 * c.v : 4 * c.v + c.v * (t - 6)) : Math.abs(c.v) * t);
  const X = (x) => LANE.x0 + (x - XMIN) / (XMAX - XMIN) * (LANE.x1 - LANE.x0);          // track pixel of position x
  const GX = (t) => G.x0 + t / T * (G.x1 - G.x0), GY = (x) => G.y0 - (x - XMIN) / (XMAX - XMIN) * (G.y0 - G.y1);

  const restart = () => { tau = 0; tmax = 0; running = false; sl.value(0); };
  const toTime = (t) => { tau = Math.min(T, Math.max(0, Number(t))); tmax = Math.max(tmax, tau); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton('Käynnistä').parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (tau >= T) { tau = 0; tmax = 0; }                                // replay from the start
      running = true;
    });
    const bR = p.createButton('Alusta').parent(controls); bR.elt.addEventListener('click', restart);
    lCase = p.createElement('label').parent(controls); p.createSpan('Tapaus').parent(lCase); selCase = p.createSelect().parent(lCase);
    selCase.option('1: sama lähtöpaikka', '1'); selCase.option('2: eri lähtöpaikka', '2');
    selCase.option('3: vastakkaiset suunnat', '3'); selCase.option('4: edestakainen liike', '4');
    const lt = p.createElement('label').parent(controls); lSl = p.createSpan('').parent(lt);
    sl = p.createSlider(0, T, 0, 0.5).parent(lt);
    const lv = p.createElement('label').parent(controls); p.createSpan('Nopeus (toisto)').parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [['hidas', 0.5], ['normaali', 1], ['nopea', 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                  // pace only; every quantity follows simulated time
    for (const e of [selCase.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    const scrub = () => { running = false; toTime(sl.value()); };         // the student drags the clock: playback stops
    sl.elt.addEventListener('input', scrub); sl.elt.addEventListener('change', scrub);
    p.createP('Nuolen suunta ja pituus näyttävät nopeuden. Pisteet merkitsevät kokonaisia sekunteja.').parent('sim-root').class('note');
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
    const speed = Number(selSp.value()), cs = CASES[selCase.value()], B = cs.B;
    if (running) { toTime(tau + Math.min(p.deltaTime, 100) / 1000 * speed); sl.value(tau); if (tau >= T) running = false; }
    const xA = pos(CART_A, tau), xB = pos(B, tau), sA = path(CART_A, tau), sB = path(B, tau);
    lSl.html(`Hetki $t = ${tx(tau, 1)}\\,\\text{s}$`);
    const bt = running ? 'Tauko' : 'Käynnistä'; if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(`<strong>$t = ${tx(tau, 1)}\\,\\text{s}$</strong><br>$\\text{A}$: paikka <strong>$x = ${tx(xA, 1)}\\,\\text{m}$</strong>, matka $s = ${tx(sA, 1)}\\,\\text{m}$<br>` +
      `$\\text{${cs.name}}$: paikka <strong>$x = ${tx(xB, 1)}\\,\\text{m}$</strong>, matka $s = ${tx(sB, 1)}\\,\\text{m}$`);
    window.simState = { tapaus: selCase.value(), t: tau, xA, x2: xB, sA, s2: sB, vA: vel(CART_A, tau), v2: vel(B, tau), tmax, running, speed, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(11);
    labels = [];
    p.background(250);
    track(CART_A, B, cs.name, ts, fh);
    graph(CART_A, B, cs.name, ts, fh);
    window.simState.labels = labels;
  };

  // --- the track: sky, two lanes, ruler, stroboscopic marks, carts with velocity arrows ---
  function track(A, B, name, ts, fh) {
    grect(0, 0, 600, RULER_Y - 4, [[196, 224, 250], [238, 247, 255]], false, 0);
    for (const [i, c, cart, letter] of [[0, COL.A, A, 'A'], [1, COL.B, B, name]]) {
      const ly = LANE.y[i];
      grect(LANE.x0 - 6, ly, LANE.x1 - LANE.x0 + 12, LANE.h, [[96, 100, 108], [72, 76, 84]], false, 4);
      p.stroke(255, 255, 255, 120); p.strokeWeight(1.5); p.drawingContext.setLineDash([8, 8]); p.line(LANE.x0, ly + LANE.h - 4, LANE.x1, ly + LANE.h - 4); p.drawingContext.setLineDash([]);
      // stroboscopic marks: where the cart was at every whole second visited so far
      p.strokeWeight(2); p.stroke(...c, 190);
      for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) { const px = X(pos(cart, s)); p.line(px, ly + 3, px, ly + 11); }
      const cx = X(pos(cart, tau)), v = vel(cart, tau);
      cartShape(cx, ly + 28, c, pos(cart, tau) * 0.9);
      if (v !== 0) arrow(cx, ly + 14, cx + v * 14, ly + 14, c);
      // lane badge on the left: the cart's letter in its colour
      p.noStroke(); p.fill(...c); p.circle(14, ly + LANE.h / 2, 24);
      lab(`$\\text{${letter}}$`, 14, ly + LANE.h / 2 + fh * 0.36, 'c', fh, [255, 255, 255], true);
    }
    // ruler
    p.stroke(60); p.strokeWeight(1.5); p.line(X(XMIN), RULER_Y, X(XMAX), RULER_Y);
    for (let m = XMIN; m <= XMAX; m += 5) { p.strokeWeight(m % 10 === 0 ? 1.5 : 1); p.line(X(m), RULER_Y, X(m), RULER_Y + (m % 10 === 0 ? 7 : 4)); }
    for (let m = 0; m <= 40; m += 10) lab(`$${m}$`, X(m), RULER_Y + 8 + fh, 'c', fh);
    lab('$x\\ (\\text{m})$', 598, RULER_Y + 8 + fh, 'r', fh);   // right-aligned at the edge: room for the larger phone label
  }

  // a cart: gradient body and cabin, two wheels with spokes that turn with the distance driven
  function cartShape(cx, cy, c, rot) {
    grect(cx - 17, cy - 10, 34, 12, [c.map((q) => Math.min(255, q + 45)), c], false, 3);
    grect(cx - 8, cy - 17, 16, 8, [[235, 245, 255], [170, 200, 230]], false, 2);
    for (const wx of [cx - 10, cx + 10]) {
      p.fill(35); p.stroke(20); p.strokeWeight(1); p.circle(wx, cy + 4, 11);
      p.stroke(190); p.strokeWeight(1.2); p.line(wx - 4 * Math.cos(rot), cy + 4 - 4 * Math.sin(rot), wx + 4 * Math.cos(rot), cy + 4 + 4 * Math.sin(rot));
    }
  }
  function arrow(x1, y1, x2, y2, c) {
    p.stroke(255, 255, 255, 220); p.strokeWeight(6); p.line(x1, y1, x2, y2);
    p.stroke(...c); p.strokeWeight(3.5); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 8;
    p.fill(...c); p.stroke(255, 255, 255, 220); p.strokeWeight(1.5);
    p.triangle(x2 + 3 * Math.cos(a), y2 + 3 * Math.sin(a), x2 - L * Math.cos(a - 0.5), y2 - L * Math.sin(a - 0.5), x2 - L * Math.cos(a + 0.5), y2 - L * Math.sin(a + 0.5));
  }

  // --- the (t,x) graph: gridlines, the lines drawn so far, whole-second dots, the present moment ---
  function graph(A, B, name, ts, fh) {
    p.noStroke(); p.fill(255); p.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1);
    p.stroke(228); p.strokeWeight(1);
    for (let s = 1; s <= T; s++) p.line(GX(s), G.y0, GX(s), G.y1);
    for (let m = 0; m <= 40; m += 10) p.line(G.x0, GY(m), G.x1, GY(m));
    p.stroke(150); p.strokeWeight(1.5); p.line(G.x0, GY(0), G.x1, GY(0));            // x = 0
    for (const [c, cart] of [[COL.A, A], [COL.B, B]]) {
      p.noFill(); p.stroke(...c); p.strokeWeight(3.2); p.strokeJoin(p.ROUND);
      if (tmax > 0) { p.beginShape(); for (let s = 0; s < tmax - 1e-9; s += 0.1) p.vertex(GX(s), GY(pos(cart, s))); p.vertex(GX(tmax), GY(pos(cart, tmax))); p.endShape(); }
      p.stroke(255); p.strokeWeight(1.5); p.fill(...c);
      for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) { if (cart === A) p.circle(GX(s), GY(pos(cart, s)), 8); else p.rect(GX(s) - 4, GY(pos(cart, s)) - 4, 8, 8, 1.5); }
    }
    // the present moment: a dashed vertical line and a ring on each line
    p.stroke(90); p.strokeWeight(1.2); p.drawingContext.setLineDash([5, 5]); p.line(GX(tau), G.y0, GX(tau), G.y1); p.drawingContext.setLineDash([]);
    for (const [c, cart] of [[COL.A, A], [COL.B, B]]) { p.fill(255); p.stroke(...c); p.strokeWeight(3); p.circle(GX(tau), GY(pos(cart, tau)), 12); }
    // axes
    p.stroke(60); p.strokeWeight(1.5); p.noFill(); p.line(G.x0, G.y0, G.x1 + 8, G.y0); p.line(G.x0, G.y0 + 0, G.x0, G.y1 - 8);
    p.noStroke(); p.fill(60);
    p.triangle(G.x1 + 14, G.y0, G.x1 + 6, G.y0 - 4, G.x1 + 6, G.y0 + 4); p.triangle(G.x0, G.y1 - 14, G.x0 - 4, G.y1 - 6, G.x0 + 4, G.y1 - 6);
    for (let s = 0; s <= T; s += 2) lab(`$${s}$`, GX(s), G.y0 + 4 + fh, 'c', fh);
    for (let m = 0; m <= 40; m += 10) lab(`$${m}$`, G.x0 - 8, GY(m) + fh * 0.36, 'r', fh);
    lab('$t\\ (\\text{s})$', G.x1 + 24, G.y0 + 4 + fh, 'l', fh);
    lab('$x\\ (\\text{m})$', G.x0 - 8, G.y1 - 12, 'r', fh);
    // legend: the same colours and markers as in the track and the graph
    p.stroke(...COL.A); p.strokeWeight(3.2); p.line(G.x1 + 20, 212, G.x1 + 46, 212); p.fill(...COL.A); p.stroke(255); p.strokeWeight(1.5); p.circle(G.x1 + 33, 212, 8);
    p.stroke(...COL.B); p.strokeWeight(3.2); p.line(G.x1 + 20, 212 + ts(26), G.x1 + 46, 212 + ts(26)); p.fill(...COL.B); p.stroke(255); p.strokeWeight(1.5); p.rect(G.x1 + 29, 208 + ts(26), 8, 8, 1.5);
    lab('$\\text{A}$', G.x1 + 52, 212 + fh * 0.36, 'l', fh);
    lab(`$\\text{${name}}$`, G.x1 + 52, 212 + ts(26) + fh * 0.36, 'l', fh);
  }

  // every canvas text: drawn with a halo, its ink box pushed to simState.labels (canvas coordinates)
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
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');                         // Finnish decimal comma inside LaTeX
});
