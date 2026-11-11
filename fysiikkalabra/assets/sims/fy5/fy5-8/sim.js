// fy5-8 Harmoninen voima ja jousen potentiaalienergia: a frictionless cart on a level track is fixed to a horizontal
// spring whose other end is in a wall; a hand holds the cart at rest at the position x (the slider, -0,20 ... 0,20 m,
// origin at the equilibrium position, where the spring has its rest length). The student also chooses the spring
// A, B or C (model spring constants 20, 50 and 80 N/m, never shown: the student finds them from the graph).
// Model: the spring's force on the cart F = -k x (towards the equilibrium position); the cart is at rest, so the hand's
// force on the cart F_k = -F = k x; the cart pushes or pulls the spring as hard as the hand pushes or pulls the cart, so the
// force stretching (x > 0) or compressing (x < 0) the spring is F_v = k x; spring potential energy E_p = 1/2 k x², the
// area of the triangle under the (x, F_v) line from 0 to x. No friction; only the horizontal forces are drawn.
// Top: the situation (wall, spring, cart, hand), the equilibrium position dashed, the position x a thin ink dimension
// arrow (never red), the spring's force F and the hand's force F_k on the cart solid red arrows at one scale (6 px per N).
// Below: the (x, F_v) graph; every position the student has set for the current spring stays as a point, the current one
// in red, the triangle under it shaded light orange (E_p). No theory line: the line emerges from the points.
// Static: no animation, so no speed control. On a narrow screen (#sim-root under 500 px) the canvas grows taller and the
// labels bigger. Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const K = { A: 20, B: 50, C: 80 };                                     // model spring constants (N/m), hidden
  const RED = [201, 42, 42], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203];
  const CARTC = [241, 223, 181], HANDC = [233, 201, 138], HEATL = [255, 192, 120];
  const X0 = 300, PPM = 600, FS = 6, CW = 80, CH = 40;                   // equilibrium (px), px per metre, px per newton, cart size
  let narrow = false, laid = false, OY = 0, Hs = 175, Hg = 225, fh = 13, S = 1;
  let slX, lX, selJ, btnC, readout, labels = [];
  const pts = { A: new Map(), B: new Map(), C: new Map() };              // the positions set for each spring: x (2 decimals) -> F_v

  const model = () => {
    const x = Math.round(Number(slX.value()) * 100) / 100, s = selJ.value(), k = K[s];
    const F = -k * x;
    return { x, s, k, F, Fk: -F, Fv: k * x, Ep: 0.5 * k * x * x };
  };
  const record = () => { const M = model(); pts[M.s].set(M.x.toFixed(2), M.Fv); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lX = p.createSpan('').parent(l1); slX = p.createSlider(-0.2, 0.2, 0, 0.01).parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('jousi')).parent(l2); selJ = p.createSelect().parent(l2);
    selJ.option(__('jousiA'), 'A'); selJ.option(__('jousiB'), 'B'); selJ.option(__('jousiC'), 'C'); selJ.selected('B');
    btnC = p.createButton(__('tyhjenna')).parent(controls);
    btnC.elt.addEventListener('click', () => { pts[selJ.value()].clear(); record(); });
    for (const e of [slX.elt, selJ.elt]) { e.addEventListener('input', record); e.addEventListener('change', record); }
    controls.style('column-gap', '0.75rem');
    l1.style('flex', '1 1 16rem'); l2.style('flex', '1 1 8rem');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    record();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { x: { input: slX.elt, unit: 'm' }, jousi: { input: selJ.elt, unit: '' } },
      reset: () => { slX.value(0); selJ.selected('B'); for (const s in pts) pts[s].clear(); record(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  const state = (M, labs) => ({ x: M.x, jousi: M.s, k: M.k, F: M.F, Fk: M.Fk, Fv: M.Fv, Ep: M.Ep, pisteet: pts[M.s].size,
    narrow, labels: labs });

  p.draw = () => {
    const M = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) { window.simState = state(M, []); p.redraw(); return; }
    fh = Math.round((narrow ? 15 : 13) * k); S = narrow ? Math.min(1.6, 0.9 * k) : 1;
    lX.html(__('paikka', { x: tx(M.x, 2) }));
    readout.html(__('lukemat', { x: tx(M.x, 2), F: tx(M.F, 1), Fk: tx(M.Fk, 1), Fv: tx(M.Fv, 1), Ep: tx(M.Ep, 3) }));
    window.simState = state(M, null);
    labels = [];
    p.background(250);
    OY = 0; p.push(); situation(M, k); p.pop();
    OY = Hs; p.push(); p.translate(0, OY); graph(M, k); p.pop();
    window.simState.labels = labels;
  };

  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) { Hs = 240; Hg = 340; p.resizeCanvas(600, Hs + Hg); }
    else { Hs = 175; Hg = 225; p.resizeCanvas(600, 400); }
    return true;
  }

  // --- the situation: wall, spring, cart and hand; the equilibrium position, the position x and the forces on the cart ---
  function situation(M, k) {
    const yTop = fh + 4, dimLab = yTop + fh * 1.5, dimY = dimLab + 10, arY = dimY + 18 + fh, cy = arY + 15;
    const rail = cy + CH / 2 + 14, axY = rail + 16, tickLab = axY + 8 + fh;
    grect(0, 0, 600, Hs, [[246, 241, 230], [238, 232, 218]], 0);
    // track and wall
    p.stroke(...INKC); p.strokeWeight(2.5 * S); p.line(30, rail, 585, rail);
    p.noStroke(); p.fill(...GRID); p.rect(14, cy - 44, 16, rail - cy + 44);
    p.stroke(...INKC); p.strokeWeight(3 * S); p.line(30, cy - 44, 30, rail);
    p.stroke(...MUTEDC); p.strokeWeight(1.5); for (let y = cy - 38; y < rail - 4; y += 12) p.line(29, y, 16, y + 10);
    // the position axis under the track: ticks every 0,05 m, numbers every 0,1 m (every 0,2 m on a phone)
    p.stroke(...INKC); p.strokeWeight(1.5 * S); p.line(X0 - 0.2 * PPM, axY, X0 + 0.2 * PPM, axY);
    for (let i = -4; i <= 4; i++) {
      const xx = X0 + i * 0.05 * PPM; p.line(xx, axY - 5, xx, axY + (i % 2 ? 3 : 6));
      if (i % 2 === 0 && (k <= 1.5 || i % 4 === 0)) lab(`$${tx(i * 0.05, i === 0 ? 0 : 1)}$`, xx, tickLab, 'c', fh, INKC);
    }
    lab('$x\\ (\\text{m})$', X0 + 0.2 * PPM + 10 + fh * 1.6, axY + fh * 0.35, 'l', fh, INKC);
    // the equilibrium position
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(X0, yTop + 6, X0, rail); p.drawingContext.setLineDash([]);
    lab('$x = 0$', X0, yTop, 'c', fh, MUTEDC);
    // spring from the wall to the cart's left face, the cart, its knob and the hand
    const cx = X0 + M.x * PPM, lf = cx - CW / 2, rf = cx + CW / 2;
    coil(30, lf, cy + 6, 12, 8);
    p.fill(...CARTC); p.stroke(...INKC); p.strokeWeight(2 * S); p.rect(lf, cy - CH / 2, CW, CH, 6);
    p.fill(...INKC); p.noStroke(); for (const d of [-22, 22]) p.circle(cx + d, cy + CH / 2 + 7, 14);
    p.fill(255); for (const d of [-22, 22]) p.circle(cx + d, cy + CH / 2 + 7, 5);
    p.stroke(...INKC); p.strokeWeight(2 * S); p.line(rf, cy + 6, rf + 8, cy + 6);
    p.fill(...HANDC); p.rect(rf + 8, cy - 4, 40, 22, 9); p.rect(rf + 44, cy - 1, 34, 16, 5);
    p.strokeWeight(1.2); for (let i = 1; i < 4; i++) p.line(rf + 8 + i * 9, cy - 1, rf + 8 + i * 9, cy + 6);
    // the position x: a thin ink dimension arrow from the equilibrium position to the cart's centre (not a force)
    if (Math.abs(M.x) >= 0.005) {
      p.stroke(...INKC); p.strokeWeight(1.5 * S); p.line(X0, dimY - 6, X0, dimY + 6);
      thin(X0, dimY, cx, dimY, INKC);
      lab('$x$', (X0 + cx) / 2, dimLab, 'c', fh, INKC);
    }
    // the forces on the cart, one scale: the spring's force at its left face, the hand's force at its right face
    const L = Math.abs(M.F) * FS;
    if (L >= 2) {
      if (M.x > 0) force(lf, arY, lf - L, arY); else force(lf - L, arY, lf, arY);        // pull from the face / push onto it
      if (M.x > 0) force(rf, arY, rf + L, arY); else force(rf + L, arY, rf, arY);
      if (L >= 10) {
        lab('$\\overline{F}$', lf - L / 2, arY - 9, 'c', fh, RED);
        lab('$\\overline{F}_\\text{k}$', rf + L / 2, arY - 9, 'c', fh, RED);
      }
    }
  }
  function coil(x1, x2, y, n, amp) {                                    // the spring: straight leads, then a zigzag
    const lead = 8, a = x1 + lead, b = x2 - lead;
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2.2 * S);
    p.beginShape(); p.vertex(x1, y); p.vertex(a, y);
    for (let i = 0; i < 2 * n; i++) p.vertex(a + (b - a) * (i + 0.5) / (2 * n), y + (i % 2 ? amp : -amp));
    p.vertex(b, y); p.vertex(x2, y); p.endShape();
  }
  function force(x1, y1, x2, y2) {                                      // a force: a solid red arrow with a filled head
    const L = Math.hypot(x2 - x1, y2 - y1); if (L < 1) return;
    const a = Math.atan2(y2 - y1, x2 - x1), H = Math.min(12 * S, L * 0.7);
    p.stroke(...RED); p.strokeWeight(3.2 * S); p.line(x1, y1, x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
  }
  function thin(x1, y1, x2, y2, col) {                                  // a dimension arrow: thin, open head
    const a = Math.atan2(y2 - y1, x2 - x1), H = 8 * S;
    p.stroke(...col); p.strokeWeight(1.8 * S); p.noFill(); p.line(x1, y1, x2, y2);
    p.line(x2, y2, x2 - H * Math.cos(a - 0.5), y2 - H * Math.sin(a - 0.5)); p.line(x2, y2, x2 - H * Math.cos(a + 0.5), y2 - H * Math.sin(a + 0.5));
  }

  // --- the (x, F_v) graph: gridlines, axes through the origin, the student's points, the triangle under the current one ---
  function graph(M, k) {
    p.noStroke(); p.fill(255); p.rect(0, 0, 600, Hg);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, 600, 0);
    const gx0 = 92, gx1 = 500, gt = fh + 16, gb = Hg - fh - 14, XR = 0.22, YR = 17;
    const X = (v) => (gx0 + gx1) / 2 + v / XR * (gx1 - gx0) / 2, Y = (v) => (gt + gb) / 2 - v / YR * (gb - gt) / 2;
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (const v of [-0.2, -0.1, 0.1, 0.2]) p.line(X(v), gt, X(v), gb);
    for (const v of [-15, -10, -5, 5, 10, 15]) p.line(gx0, Y(v), gx1, Y(v));
    // E_p: the triangle under the current point
    if (Math.abs(M.x) > 0.001) {
      p.noStroke(); p.fill(...HEATL, 190); p.triangle(X(0), Y(0), X(M.x), Y(0), X(M.x), Y(M.Fv));
    }
    // axes through the origin with arrowheads
    p.stroke(...INKC); p.strokeWeight(2 * S); p.line(gx0, Y(0), gx1 + 10, Y(0)); p.line(X(0), gb, X(0), gt - 6);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 18, Y(0), gx1 + 8, Y(0) - 5, gx1 + 8, Y(0) + 5); p.triangle(X(0), gt - 14, X(0) - 5, gt - 4, X(0) + 5, gt - 4);
    // tick numbers on the frame: x under the plot, F_v left of it
    for (const v of [-0.2, -0.1, 0.1, 0.2]) if (k <= 1.5 || Math.abs(v) > 0.15) lab(`$${tx(v, 1)}$`, X(v), gb + fh + 2, 'c', fh, MUTEDC);
    for (const v of [-15, -10, -5, 5, 10, 15]) if (k <= 1.5 || Math.abs(v) === 10) lab(`$${tx(v, 0)}$`, gx0 - 8, Y(v) + fh * 0.35, 'r', fh, MUTEDC);
    {   // the axis name stands after the arrow tip; where a phone's larger text would cross the picture's edge, it stands above the axis end
      p.textSize(fh); const axisTex = '$x\\ (\\text{m})$', axisWide = p.textWidth(axisTex), axisFits = gx1 + 24 + axisWide <= 594;
      lab(axisTex, axisFits ? gx1 + 24 : 594 - axisWide, axisFits ? Y(0) + fh * 0.35 : Y(0) - 10, 'l', fh, INKC);
    }
    lab('$F_\\text{v}\\ (\\text{N})$', X(0) + 10, gt - 4, 'l', fh, INKC);
    // the points set for this spring, the current one in red
    p.stroke(255); p.strokeWeight(2);
    for (const [xs, Fv] of pts[M.s]) { p.fill(...INKC); p.circle(X(Number(xs)), Y(Fv), 10 * S); }
    p.fill(...RED); p.circle(X(M.x), Y(M.Fv), 14 * S);
    if (Math.abs(M.x) >= 0.12) lab('$E_\\text{p}$', X(M.x * 2 / 3), Y(M.Fv / 3) + fh * 0.35, 'c', fh, INKC);
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
