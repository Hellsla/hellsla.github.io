// fy4-2 Kiihtyvyys ja tasaisesti kiihtyvä liike: a cart on a straight road with a constant acceleration, its
// stroboscopic places at whole seconds, and the (t,x) and (t,v) graphs the motion draws.
// Model: constant acceleration a from t = 0, initial velocity v0, x0 = 0: v = v0 + a t, x = v0 t + ½ a t².
// The (t,x) graph shows the tangent at the present moment (its slope is v); the (t,v) graph shades the area under
// the line from 0 to t (its signed area is x − x0). Velocity is blue and acceleration orange everywhere (arrows,
// curves, legend). Time: the slider "Hetki t" scrubs 0…6 s; the main button plays it in simulated time (dt·speed),
// so the speed select changes only the pace. The road ruler and the graph scales follow the chosen v0 and a.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const T = 6;                                                        // run time (s)
  const VEL = [25, 113, 194], ACC = [232, 89, 12], INKC = [31, 41, 51], MUT = [107, 116, 128];
  const ROAD = { x0: 30, x1: 492, y: 78, h: 22 }, RULER_Y = 116;
  const G1 = { x0: 64, x1: 258, y0: 350, y1: 192 }, G2 = { x0: 372, x1: 540, y0: 350, y1: 192 };
  let btn, slV0, slA, slT, lV0, lA, lT, selSp, readout;
  let tau = 0, tmax = 0, running = false, k = 1, labels = [];

  const P = () => ({ v0: Number(slV0.value()), a: Number(slA.value()) });
  const xAt = (q, t) => q.v0 * t + 0.5 * q.a * t * t;
  const vAt = (q, t) => q.v0 + q.a * t;
  const restart = () => { tau = 0; tmax = 0; running = false; slT.value(0); };
  const toTime = (t) => { tau = Math.min(T, Math.max(0, Number(t))); tmax = Math.max(tmax, tau); };
  // a "nice" scale for [lo, hi] with about n steps: {lo, hi, step}, always containing 0
  function scale(lo, hi, n) {
    lo = Math.min(lo, 0); hi = Math.max(hi, 0); if (hi - lo < 1e-9) hi = lo + 1;
    let step = 1; for (const s of [1, 2, 5, 10, 20, 25, 50]) { step = s; if ((hi - lo) / s <= n) break; }
    return { lo: Math.floor(lo / step + 1e-9) * step, hi: Math.ceil(hi / step - 1e-9) * step, step };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (tau >= T) { tau = 0; tmax = 0; }                              // replay from the start
      running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lV0 = p.createSpan('').parent(l1); slV0 = p.createSlider(-6, 6, 0, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l2); slA = p.createSlider(-3, 3, 2, 0.5).parent(l2);
    const l3 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l3); slT = p.createSlider(0, T, 0, 0.5).parent(l3);
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus_toisto')).parent(l4); selSp = p.createSelect().parent(l4);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                 // pace only; every quantity follows simulated time
    for (const e of [slV0.elt, slA.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    const scrub = () => { running = false; toTime(slT.value()); };        // the student drags the clock: playback stops
    slT.elt.addEventListener('input', scrub); slT.elt.addEventListener('change', scrub);
    p.createP(__('legend')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { v0: { input: slV0.elt, unit: 'm/s' }, a: { input: slA.elt, unit: 'm/s²' }, t: { input: slT.elt, unit: 's' } },
      reset: () => { slV0.value(0); slA.value(2); selSp.selected('1'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const speed = Number(selSp.value()), q = P();
    if (running) { toTime(tau + Math.min(p.deltaTime, 100) / 1000 * speed); slT.value(tau); if (tau >= T) running = false; }
    const x = xAt(q, tau), v = vAt(q, tau);
    lV0.html(__('alkunopeus', { v: tx(q.v0, 0) }));
    lA.html(__('kiihtyvyys', { a: tx(q.a, 1) }));
    lT.html(__('hetki', { t: tx(tau, 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { t: tx(tau, 1), x: tx(x, 1), v: tx(v, 1), a: tx(q.a, 1) }));
    window.simState = { v0: q.v0, a: q.a, t: tau, x, v, tmax, running, speed, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    // scales follow the motion over the whole run (0…T): sample x and v
    let xl = 0, xh = 0; for (let s = 0; s <= T; s += 0.1) { const xx = xAt(q, s); xl = Math.min(xl, xx); xh = Math.max(xh, xx); }
    const sx = scale(xl, xh, 4), sv = scale(Math.min(q.v0, vAt(q, T)), Math.max(q.v0, vAt(q, T)), 4);
    p.background(250);
    road(q, sx, fh);
    graphX(q, sx, fh);
    graphV(q, sv, fh);
    window.simState.labels = labels;
  };

  // --- the road: sky, hills, road with lane marks, ruler, ghost carts at whole seconds, the cart with v and a ---
  function road(q, sx, fh) {
    const X = (xx) => ROAD.x0 + (xx - sx.lo) / (sx.hi - sx.lo) * (ROAD.x1 - ROAD.x0);
    grect(0, 0, 600, ROAD.y, [[203, 228, 250], [238, 246, 252]], false, 0);
    p.noStroke(); p.fill(178, 222, 186); p.beginShape(); p.vertex(0, ROAD.y);
    for (let i = 0; i <= 12; i++) p.vertex(i * 50, ROAD.y - 16 - 10 * Math.sin(i * 1.7) - 6 * Math.cos(i * 0.9)); p.vertex(600, ROAD.y); p.endShape(p.CLOSE);
    grect(0, ROAD.y, 600, ROAD.h, [[110, 116, 124], [80, 86, 94]], false, 0);
    p.stroke(255, 255, 255, 170); p.strokeWeight(2); p.drawingContext.setLineDash([14, 12]); p.line(0, ROAD.y + ROAD.h / 2, 600, ROAD.y + ROAD.h / 2); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(241, 223, 181); p.rect(0, ROAD.y + ROAD.h, 600, RULER_Y - ROAD.y - ROAD.h);
    // ruler
    p.stroke(...INKC); p.strokeWeight(1.5); p.line(ROAD.x0, RULER_Y, ROAD.x1, RULER_Y);
    let i = 0;
    for (let m = sx.lo; m <= sx.hi + 1e-9; m += sx.step, i++) {
      p.stroke(...INKC); p.strokeWeight(1.5); p.line(X(m), RULER_Y, X(m), RULER_Y + 6);
      if (k <= 1.5 || i % 2 === 0 || Math.abs(m) < 1e-9) lab(`$${tx(m, 0)}$`, X(m), RULER_Y + 8 + fh, 'c', fh);
    }
    lab('$x\\ (\\text{m})$', 598, RULER_Y + 8 + fh, 'r', fh);
    // the origin x = 0 on the road
    p.stroke(255); p.strokeWeight(2); p.line(X(0), ROAD.y, X(0), ROAD.y + ROAD.h);
    // ghost carts at the whole seconds visited so far
    for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) { if (Math.abs(s - tau) > 0.25) cart(X(xAt(q, s)), 70); }
    const cx = X(xAt(q, tau)), v = vAt(q, tau);
    cart(cx, 255, xAt(q, tau));
    // velocity arrow (blue) above, acceleration arrow (orange) below it; their labels at the tips, inside the canvas
    const vy = 14, ay = 40;
    if (Math.abs(v) > 0.05) { const L = Math.max(-110, Math.min(110, v * 6)); arrow(cx, vy, cx + L, vy, VEL); tipLabel('$\\overline{v}$', cx, L, vy, VEL, fh); }
    if (Math.abs(q.a) > 0.01) { const L = q.a * 14; arrow(cx, ay, cx + L, ay, ACC); tipLabel('$\\overline{a}$', cx, L, ay, ACC, fh); }
  }
  function tipLabel(s, cx, L, y, col, fh) {
    const w = fh * 1.1, right = L >= 0;
    let x = right ? cx + L + 6 : cx + L - 6, al = right ? 'l' : 'r';
    if (right && x + w > 596) { x = cx - 8; al = 'r'; }
    if (!right && x - w < 4) { x = cx + 8; al = 'l'; }
    lab(s, x, y + fh * 0.36, al, fh, col);
  }
  // a small cart: body, window, wheels whose spokes turn with the distance driven; alpha < 255 for a ghost
  function cart(cx, alpha, dist) {
    const y = ROAD.y + 2;
    p.stroke(31, 41, 51, alpha); p.strokeWeight(1.5);
    p.fill(196, 204, 212, alpha); p.rect(cx - 18, y - 24, 36, 15, 4);
    p.fill(208, 230, 251, alpha); p.rect(cx - 8, y - 32, 16, 8, 2);
    for (const wx of [cx - 10, cx + 10]) {
      p.fill(70, 76, 84, alpha); p.circle(wx, y - 6, 11);
      if (dist !== undefined) { const r = dist / 0.25; p.stroke(220); p.strokeWeight(1.2); p.line(wx - 4 * Math.cos(r), y - 6 - 4 * Math.sin(r), wx + 4 * Math.cos(r), y - 6 + 4 * Math.sin(r)); p.stroke(31, 41, 51, alpha); p.strokeWeight(1.5); }
    }
  }
  function arrow(x1, y1, x2, y2, c) {
    p.stroke(255, 255, 255, 220); p.strokeWeight(6); p.line(x1, y1, x2, y2);
    p.stroke(...c); p.strokeWeight(3.5); p.line(x1, y1, x2, y2);
    const ang = Math.atan2(y2 - y1, x2 - x1), L = 9;
    p.fill(...c); p.stroke(255, 255, 255, 220); p.strokeWeight(1.2);
    p.triangle(x2 + 3 * Math.cos(ang), y2 + 3 * Math.sin(ang), x2 - L * Math.cos(ang - 0.5), y2 - L * Math.sin(ang - 0.5), x2 - L * Math.cos(ang + 0.5), y2 - L * Math.sin(ang + 0.5));
  }

  // --- graph frame shared by both graphs: white plot, gridlines, axes with arrowheads, tick labels, titles ---
  function frame(G, sy, ylab, fh) {
    const GX = (t) => G.x0 + t / T * (G.x1 - G.x0), GY = (y) => G.y0 - (y - sy.lo) / (sy.hi - sy.lo) * (G.y0 - G.y1);
    p.noStroke(); p.fill(255); p.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1);
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let s = 1; s <= T; s++) p.line(GX(s), G.y0, GX(s), G.y1);
    for (let y = sy.lo; y <= sy.hi + 1e-9; y += sy.step) p.line(G.x0, GY(y), G.x1, GY(y));
    p.stroke(...MUT); p.strokeWeight(1.5); p.line(G.x0, GY(0), G.x1, GY(0));
    p.stroke(...INKC); p.strokeWeight(2); p.line(G.x0, G.y0, G.x1 + 8, G.y0); p.line(G.x0, G.y0, G.x0, G.y1 - 8);
    p.noStroke(); p.fill(...INKC);
    p.triangle(G.x1 + 14, G.y0, G.x1 + 6, G.y0 - 4, G.x1 + 6, G.y0 + 4); p.triangle(G.x0, G.y1 - 14, G.x0 - 4, G.y1 - 6, G.x0 + 4, G.y1 - 6);
    for (let s = 0; s <= T; s += (k > 1.5 ? 2 : 1)) lab(`$${s}$`, GX(s), G.y0 + 4 + fh, 'c', fh);
    let i = 0;
    for (let y = sy.lo; y <= sy.hi + 1e-9; y += sy.step, i++) if (k <= 1.5 || i % 2 === 0 || Math.abs(y) < 1e-9) lab(`$${tx(y, 0)}$`, G.x0 - 7, GY(y) + fh * 0.36, 'r', fh);
    lab('$t\\ (\\text{s})$', G.x1 + 16, G.y0 + 4 + fh, 'l', fh);
    lab(ylab, G.x0 - 4, G.y1 - 18, 'r', fh);
    return { GX, GY };
  }

  // --- (t,x): the curve so far, ghost dots at whole seconds, the present point and its tangent (slope = v) ---
  function graphX(q, sx, fh) {
    const { GX, GY } = frame(G1, sx, '$x\\ (\\text{m})$', fh);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.strokeJoin(p.ROUND);
    if (tmax > 0) { p.beginShape(); for (let s = 0; s < tmax - 1e-9; s += 0.05) p.vertex(GX(s), GY(xAt(q, s))); p.vertex(GX(tmax), GY(xAt(q, tmax))); p.endShape(); }
    p.stroke(255); p.strokeWeight(1.5); p.fill(...INKC);
    for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) p.circle(GX(s), GY(xAt(q, s)), 7);
    // tangent at the present moment, ±1,2 s, clipped to the plot
    const x = xAt(q, tau), v = vAt(q, tau), ta = Math.max(0, tau - 1.2), tb = Math.min(T, tau + 1.2);
    const c = p.drawingContext; c.save(); c.beginPath(); c.rect(G1.x0, G1.y1, G1.x1 - G1.x0, G1.y0 - G1.y1); c.clip();
    p.stroke(...VEL); p.strokeWeight(2.5); c.setLineDash([7, 5]); p.line(GX(ta), GY(x + v * (ta - tau)), GX(tb), GY(x + v * (tb - tau))); c.setLineDash([]);
    c.restore();
    p.fill(255); p.stroke(...INKC); p.strokeWeight(3); p.circle(GX(tau), GY(x), 11);
  }

  // --- (t,v): the line so far, the area under it to the present moment (= displacement), the present point ---
  function graphV(q, sv, fh) {
    const { GX, GY } = frame(G2, sv, '$v\\ (\\text{m/s})$', fh);
    if (tau > 0) {
      p.noStroke(); p.fill(208, 230, 251, 200);
      p.beginShape(); p.vertex(GX(0), GY(0)); p.vertex(GX(0), GY(q.v0));
      // the area changes sign where v crosses 0: draw it as a polygon along the line, back along v = 0
      for (let s = 0; s <= tau + 1e-9; s += 0.05) p.vertex(GX(Math.min(s, tau)), GY(vAt(q, Math.min(s, tau))));
      p.vertex(GX(tau), GY(vAt(q, tau))); p.vertex(GX(tau), GY(0)); p.endShape(p.CLOSE);
    }
    p.noFill(); p.stroke(...VEL); p.strokeWeight(3);
    if (tmax > 0) p.line(GX(0), GY(q.v0), GX(tmax), GY(vAt(q, tmax)));
    p.stroke(255); p.strokeWeight(1.5); p.fill(...VEL);
    for (let s = 0; s <= Math.min(T, Math.floor(tmax + 1e-9)); s++) p.circle(GX(s), GY(vAt(q, s)), 7);
    p.fill(255); p.stroke(...VEL); p.strokeWeight(3); p.circle(GX(tau), GY(vAt(q, tau)), 11);
  }

  // every canvas text: drawn, its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  // gradient fill (raw canvas, inside save/restore so p5's own fill state is untouched)
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const g = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => g.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = g; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.restore();
  }
  const tx = (v, d) => { const s = (Math.abs(v) < 0.5 * Math.pow(10, -d) ? 0 : v).toFixed(d).replace('.', '{,}'); return s.startsWith('-') ? '-' + s.slice(1) : s; };
});
