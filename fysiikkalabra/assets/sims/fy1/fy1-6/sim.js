// fy1-6 Putoamiskiihtyvyys: v = gt. Two equally big balls A and B are released from rest and fall past a 0-80 m scale; the (t,v) graph draws itself.
// Model: environment "tyhjiö" (no air): v = g t for every mass, g = 9,81 m/s². Environment "ilma": the air slows the ball by the quadratic
// drag K v² (ball of diameter 0,20 m, drag coefficient 0,47, air density 1,2 kg/m³, K = ½·1,2·0,47·π·0,10² kg/m), so dv/dt = g − (K/m) v².
// Its exact solution is v = vt·tanh(g t / vt) with the terminal speed vt = √(m g / K); the fallen distance is (vt²/g)·ln cosh(g t / vt).
// Time: the slider "Hetki t" scrubs 0…4 s; the main button plays it in simulated time (dt·speed), so the "Nopeus (toisto)" select changes
// only the pace. The graph is drawn for the times visited so far (tmax); dots mark whole seconds; the faint dashed line is v = g t.
// Colour carries meaning: orange = ball A, blue = ball B, in the scene, the arrows, the graph and the legend.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, KDRAG = 0.5 * 1.2 * 0.47 * Math.PI * 0.1 * 0.1, T = 4, H = 80;      // g (m/s²), drag constant (kg/m), run time (s), scale height (m)
  const COL = { A: [232, 118, 28], B: [38, 110, 214] };
  const SC = { x0: 8, x1: 240, top: 46, ppm: 3.75, ground: 360, ax: 110, bx: 184, ruler: 50 };    // scene: pixels per metre, ball columns, ruler x
  const G = { x0: 316, x1: 500, y0: 350, y1: 70 };                         // graph box: t 0…4 s, v 0…40 m/s
  let btn, sl, slA, slB, lSl, lA, lB, selEnv, selSp, readout;
  let tau = 0, tmax = 0, running = false, k = 1, labels = [];

  // --- the physics: speed and fallen distance of a ball of mass m at time t, with or without air ---
  const vt = (m) => Math.sqrt(m * g / KDRAG);
  const speed = (m, t, air) => (air ? vt(m) * Math.tanh(g * t / vt(m)) : g * t);
  const fallen = (m, t, air) => (air ? vt(m) * vt(m) / g * Math.log(Math.cosh(g * t / vt(m))) : 0.5 * g * t * t);
  const SY = (m) => SC.top + m * SC.ppm;                                     // scene pixel of a fallen distance m
  const GX = (t) => G.x0 + t / T * (G.x1 - G.x0), GY = (v) => G.y0 - v / 40 * (G.y0 - G.y1);

  const restart = () => { tau = 0; tmax = 0; running = false; sl.value(0); };
  const toTime = (t) => { tau = Math.min(T, Math.max(0, Number(t))); tmax = Math.max(tmax, tau); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('pudota')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (tau >= T) { tau = 0; tmax = 0; }                                 // replay from the start
      running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const le = p.createElement('label').parent(controls); p.createSpan(__('ymparisto')).parent(le); selEnv = p.createSelect().parent(le);
    selEnv.option(__('tyhjio'), '0'); selEnv.option(__('ilma'), '1');
    lA = p.createElement('label').parent(controls); const sA = p.createSpan('').parent(lA); slA = p.createSlider(0.1, 10, 1, 0.1).parent(lA);
    lB = p.createElement('label').parent(controls); const sB = p.createSpan('').parent(lB); slB = p.createSlider(0.1, 10, 1, 0.1).parent(lB);
    lA.sp = sA; lB.sp = sB;
    const lt = p.createElement('label').parent(controls); lSl = p.createSpan('').parent(lt);
    sl = p.createSlider(0, T, 0, 0.5).parent(lt);
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus_toisto')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                  // pace only; every quantity follows simulated time
    const scrub = () => { running = false; toTime(sl.value()); };         // the student drags the clock: playback stops
    sl.elt.addEventListener('input', scrub); sl.elt.addEventListener('change', scrub);
    p.createP(__('huomautus')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { t: { input: sl.elt, unit: 's' }, ilma: { input: selEnv.elt, unit: '' }, mA: { input: slA.elt, unit: 'kg' }, mB: { input: slB.elt, unit: 'kg' } },
      reset: () => { selEnv.selected('0'); selSp.selected('1'); slA.value(1); slB.value(1); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const sp = Number(selSp.value()), air = selEnv.value() === '1', mA = Number(slA.value()), mB = Number(slB.value());
    if (running) { toTime(tau + Math.min(p.deltaTime, 100) / 1000 * sp); sl.value(tau); if (tau >= T) running = false; }
    const vA = speed(mA, tau, air), vB = speed(mB, tau, air), yA = fallen(mA, tau, air), yB = fallen(mB, tau, air);
    const qA = tau > 0 ? vA / tau : null, qB = tau > 0 ? vB / tau : null;      // v/t: the speed gained per second (starting from rest)
    lSl.html(__('hetki', { tau: tx(tau, 1) }));
    lA.sp.html(__('massa_a', { m: tx(mA, 1) })); lB.sp.html(__('massa_b', { m: tx(mB, 1) }));
    const bt = running ? __('tauko') : __('pudota'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const row = (name, v, q) => (tau > 0
      ? __('rivi', { n: name, v: tx(v, 1), q: tx(q, 2) })
      : __('rivi_alku', { n: name }));
    readout.html(__('rivi_t', { tau: tx(tau, 1) }) + row('A', vA, qA) + row('B', vB, qB));
    window.simState = { ilma: air ? 1 : 0, mA, mB, t: tau, vA, vB, yA, yB, qA, qB, tmax, running, speed: sp, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(11);
    labels = [];
    p.background(250);
    scene(air, mA, mB, vA, vB, yA, yB, ts, fh);
    graph(air, mA, mB, ts, fh);
    window.simState.labels = labels;
  };

  // --- the scene: the 0-80 m scale, the two balls with trail dots and velocity arrows, the glass tube when there is no air ---
  function scene(air, mA, mB, vA, vB, yA, yB, ts, fh) {
    const bgc = air ? [[190, 221, 248], [236, 246, 255]] : [[226, 224, 240], [246, 245, 252]];
    grect(SC.x0, 30, SC.x1 - SC.x0, SC.ground - 30, bgc, false, 0);
    // metre scale: ticks every 10 m, numbers every 20 m, light guide lines across the scene
    p.stroke(60); p.strokeWeight(1.5); p.line(SC.ruler, SY(0), SC.ruler, SY(H));
    for (let m = 0; m <= H; m += 10) {
      p.stroke(255, 255, 255, 150); p.strokeWeight(1); p.line(SC.ruler, SY(m), SC.x1, SY(m));
      p.stroke(60); p.strokeWeight(m % 20 === 0 ? 1.5 : 1); p.line(SC.ruler - (m % 20 === 0 ? 7 : 4), SY(m), SC.ruler, SY(m));
    }
    for (let m = 0; m <= H; m += 20) lab(`$${m}$`, SC.ruler - 10, SY(m) + fh * 0.36, 'r', fh);
    lab('$\\text{m}$', SC.ruler - 10, 22, 'r', fh);
    // glass tube: only the vacuum has one
    if (!air) {
      p.noFill(); p.stroke(120, 150, 180); p.strokeWeight(3); p.rect(SC.ruler + 14, 34, SC.x1 - SC.ruler - 22, SC.ground - 34, 12);
      p.stroke(255, 255, 255, 190); p.strokeWeight(2); p.line(SC.ruler + 22, 48, SC.ruler + 22, SC.ground - 16);
    }
    // ground
    grect(SC.x0, SC.ground, SC.x1 - SC.x0, 14, [[150, 118, 76], [108, 82, 50]], false, 0);
    for (const [bx, m, c, letter, v, y] of [[SC.ax, mA, COL.A, 'A', vA, yA], [SC.bx, mB, COL.B, 'B', vB, yB]]) {
      // trail dots at every whole second visited so far
      for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) { p.noStroke(); p.fill(...c, 170); p.circle(bx - 20, SY(fallen(m, s, air)), 5); }
      ball(bx, SY(y), c);
      if (v > 0.01) arrow(bx + 20, SY(y), bx + 20, SY(y) + v * 1.4, c);
      lab(`$\\text{${letter}}$`, bx, 24 + fh * 0.36, 'c', fh, c);
    }
  }
  function ball(cx, cy, c) {
    const r = 13, ctx = p.drawingContext; ctx.save();
    const gr = ctx.createRadialGradient(cx - 4, cy - 5, 2, cx, cy, r);
    gr.addColorStop(0, `rgb(${c.map((q) => Math.min(255, q + 90)).join(',')})`); gr.addColorStop(1, `rgb(${c.join(',')})`);
    ctx.fillStyle = gr; ctx.strokeStyle = 'rgba(0,0,0,0.45)'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(cx, cy, r, 0, 2 * Math.PI); ctx.fill(); ctx.stroke(); ctx.restore();
  }
  function arrow(x1, y1, x2, y2, c) {
    p.stroke(255, 255, 255, 220); p.strokeWeight(6); p.line(x1, y1, x2, y2 - 6);
    p.stroke(...c); p.strokeWeight(3.5); p.line(x1, y1, x2, y2 - 6);
    p.fill(...c); p.stroke(255, 255, 255, 220); p.strokeWeight(1.5); p.triangle(x2, y2 + 2, x2 - 6, y2 - 8, x2 + 6, y2 - 8);
  }

  // --- the (t,v) graph: gridlines, the faint law v = g t, both lines drawn so far, whole-second dots, the present moment ---
  function graph(air, mA, mB, ts, fh) {
    p.noStroke(); p.fill(255); p.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1);
    p.stroke(228); p.strokeWeight(1);
    for (let s = 1; s <= T; s++) p.line(GX(s), G.y0, GX(s), G.y1);
    for (let v = 10; v <= 40; v += 10) p.line(G.x0, GY(v), G.x1, GY(v));
    // the law v = g t, faint and dashed
    p.stroke(120); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 6]); p.line(GX(0), GY(0), GX(T), GY(g * T)); p.drawingContext.setLineDash([]);
    for (const [c, m, sq] of [[COL.A, mA, true], [COL.B, mB, false]]) {
      p.noFill(); p.stroke(...c); p.strokeWeight(3.2); p.strokeJoin(p.ROUND);
      if (tmax > 0) { p.beginShape(); for (let s = 0; s < tmax - 1e-9; s += 0.05) p.vertex(GX(s), GY(speed(m, s, air))); p.vertex(GX(tmax), GY(speed(m, tmax, air))); p.endShape(); }
      p.stroke(255); p.strokeWeight(1.5); p.fill(...c);
      for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) { if (sq) p.circle(GX(s), GY(speed(m, s, air)), 8); else p.rect(GX(s) - 4, GY(speed(m, s, air)) - 4, 8, 8, 1.5); }
    }
    // the present moment: a dashed vertical line and a ring on each line
    p.stroke(90); p.strokeWeight(1.2); p.drawingContext.setLineDash([5, 5]); p.line(GX(tau), G.y0, GX(tau), G.y1); p.drawingContext.setLineDash([]);
    for (const [c, m] of [[COL.A, mA], [COL.B, mB]]) { p.fill(255); p.stroke(...c); p.strokeWeight(3); p.circle(GX(tau), GY(speed(m, tau, air)), 12); }
    // axes
    p.stroke(60); p.strokeWeight(1.5); p.noFill(); p.line(G.x0, G.y0, G.x1 + 8, G.y0); p.line(G.x0, G.y0, G.x0, G.y1 - 8);
    p.noStroke(); p.fill(60);
    p.triangle(G.x1 + 14, G.y0, G.x1 + 6, G.y0 - 4, G.x1 + 6, G.y0 + 4); p.triangle(G.x0, G.y1 - 14, G.x0 - 4, G.y1 - 6, G.x0 + 4, G.y1 - 6);
    for (let s = 0; s <= T; s++) lab(`$${s}$`, GX(s), G.y0 + 4 + fh, 'c', fh);
    for (let v = 10; v <= 40; v += 10) lab(`$${v}$`, G.x0 - 8, GY(v) + fh * 0.36, 'r', fh);
    lab('$t\\ (\\text{s})$', G.x1 + 22, G.y0 + 4 + fh, 'l', fh);
    lab('$v\\ (\\text{m/s})$', G.x0 - 8, G.y1 - 24, 'r', fh);
    // legend: the same colours and markers as in the scene and the graph
    const lx = G.x0 + 14, ly = G.y1 + 18;
    p.stroke(...COL.A); p.strokeWeight(3.2); p.line(lx, ly, lx + 26, ly); p.fill(...COL.A); p.stroke(255); p.strokeWeight(1.5); p.circle(lx + 13, ly, 8);
    p.stroke(...COL.B); p.strokeWeight(3.2); p.line(lx, ly + ts(24), lx + 26, ly + ts(24)); p.fill(...COL.B); p.stroke(255); p.strokeWeight(1.5); p.rect(lx + 9, ly + ts(24) - 4, 8, 8, 1.5);
    lab('$\\text{A}$', lx + 34, ly + fh * 0.36, 'l', fh);
    lab('$\\text{B}$', lx + 34, ly + ts(24) + fh * 0.36, 'l', fh);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  // gradient fill (raw canvas, inside save/restore so p5's own fill state is untouched) with a thin outline
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.map((v) => Math.min(255, Math.round(v))).join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');                         // Finnish decimal comma inside LaTeX
});
