// fy4-11 Liikenneturvallisuus: a car drives at v0 (30–120 km/h); the driver notices a danger at the dashed line, reacts
// during t_r (0,5–2,0 s) at constant speed and then brakes with a constant deceleration a set by the road (dry 9,0, wet 6,0,
// snowy 3,0, icy 1,5 m/s²; the dry value is Liikenneturva's, the others rounded example values). Optionally a stopped car
// stands 25 m or 50 m ahead: if the stopping distance is longer, the car hits it and the speed at impact is recorded.
// The motion is computed exactly from the model: x = v0 t while t ≤ t_r, then x = s_r + v0 τ − ½ a τ², v = v0 − a τ.
// Top: the situation picture (tilannekuva) to scale along the road (the cars are not to scale): the velocity (blue) and the
// acceleration (orange) beside the car, never forces; the reaction distance (green) and the braking distance (copper) as bars
// under the ruler. Bottom: the (t, v) graph with the areas under it shaded in the same colours: the area is the distance.
// On a phone the two panels stack at the full 600 width. Every canvas text goes through lab(), which pushes its ink box to
// simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const DEC = { kuiva: 9.0, marka: 6.0, luminen: 3.0, jainen: 1.5 };
  const BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GREEN = [43, 138, 62], COPPERC = [184, 98, 45];
  const ROADC = { kuiva: [108, 117, 125], marka: [78, 88, 98], luminen: [226, 231, 236], jainen: [196, 222, 240] };
  const NICE = [10, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120, 150, 200, 250, 300, 400, 500];
  const TNICE = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30];
  let narrow = false, laid = false, kk = 1, fh = 14, U = 1, OY = 0, RH = 224, CH = 400, labels = [];
  let selV, selTr, selKeli, selEste, selSpeed, btn, readout;
  let t = 0, running = false, done = false, hit = false, res = null;

  const params = () => ({ v0: Number(selV.value()), tr: Number(selTr.value()), keli: selKeli.value(), este: selEste.value() });
  const model = (P) => {                                                   // the planned stop (for the scales) and the obstacle
    const v0 = P.v0 / 3.6, a = DEC[P.keli], sr = v0 * P.tr, sj = v0 * v0 / (2 * a), d = P.este === 'ei' ? null : Number(P.este);
    let thit = null;
    if (d !== null && d < sr + sj) thit = d <= sr ? d / v0 : P.tr + (v0 - Math.sqrt(v0 * v0 - 2 * a * (d - sr))) / a;
    return { v0, a, sr, sj, sp: sr + sj, tj: v0 / a, tp: P.tr + v0 / a, d, thit };
  };
  const motion = (M, P, tt) => {                                           // position (m from the dashed line) and speed (m/s)
    if (tt <= P.tr) return [M.v0 * tt, M.v0];
    if (tt - P.tr >= M.tj - 1e-9) return [M.sp, 0];                             // stopped
    const tau = tt - P.tr;
    return [M.sr + M.v0 * tau - 0.5 * M.a * tau * tau, Math.max(0, M.v0 - M.a * tau)];
  };
  const restart = () => { t = 0; running = false; done = false; hit = false; res = null; };
  const advance = (P, M, dt) => {
    const tEnd = M.thit !== null ? M.thit : M.tp;
    t = Math.min(t + dt, tEnd);
    if (t >= tEnd - 1e-12) {
      running = false; done = true; hit = M.thit !== null;
      const vEnd = motion(M, P, t)[1];
      res = hit ? { vImpact: vEnd * 3.6, sR: null, sJ: null, sP: null, tP: null }
                : { vImpact: M.d === null ? null : 0, sR: M.sr, sJ: M.sj, sP: M.sp, tP: M.tp };
    }
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const mk = (key) => { const l = p.createElement('label').parent(controls); p.createSpan(__(key)).parent(l); return p.createSelect().parent(l); };
    selV = mk('ajonopeus'); for (const v of ['30', '40', '50', '60', '80', '100', '120']) selV.option(v + ' km/h', v); selV.selected('50');
    selTr = mk('reaktioaika'); for (const [v, s] of [['0.5', '0,5 s'], ['1', '1,0 s'], ['1.5', '1,5 s'], ['2', '2,0 s']]) selTr.option(s, v); selTr.selected('1');
    selKeli = mk('keli'); for (const k of ['kuiva', 'marka', 'luminen', 'jainen']) selKeli.option(__(k), k); selKeli.selected('kuiva');
    selEste = mk('este'); for (const k of ['ei', '25', '50']) selEste.option(__('este_' + k), k); selEste.selected('ei');
    selSpeed = mk('nopeus'); selSpeed.option(__('hidas'), '0.25'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '4'); selSpeed.selected('1');
    for (const s of [selV, selTr, selKeli, selEste]) { s.elt.addEventListener('input', restart); s.elt.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { v0: { input: selV.elt, unit: 'km/h' }, tr: { input: selTr.elt, unit: 's' }, keli: { input: selKeli.elt, unit: '' }, este: { input: selEste.elt, unit: '' } },
      reset: () => { selV.selected('50'); selTr.selected('1'); selKeli.selected('kuiva'); selEste.selected('ei'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const P = params(), M = model(P);
    if (running) advance(P, M, Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
    const [x, v] = motion(M, P, t);
    const braking = t > P.tr && v > 0 && !(done && hit);
    const bt = running ? __('tauko') : (t > 0 && !done ? __('jatka') : __('kaynnista')); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const R = res || {};
    const dots = '\\ldots';
    readout.html(__('lukemat', { v0: P.v0, v0ms: tx(M.v0, 1), a: tx(M.a, 1), t: tx(t, 2), v: tx(v * 3.6, 0), s: tx(x, 1) })
      + (done && hit ? '' : '<br>' + __('lukemat_pysahdys', { sr: R.sR == null ? dots : tx(R.sR, 1), sj: R.sJ == null ? dots : tx(R.sJ, 1),
                                                              sp: R.sP == null ? dots : tx(R.sP, 1), tp: R.tP == null ? dots : tx(R.tP, 2) }))
      + (M.d === null ? '' : '<br>' + __('lukemat_este', { d: M.d, vi: !done ? dots : tx(R.vImpact, 0) })));
    window.simState = { v0: P.v0, tr: P.tr, keli: P.keli, este: P.este, a: M.a, t, x, v, vkmh: v * 3.6, braking, running, done, hit,
                        sR: done ? R.sR : null, sJ: done ? R.sJ : null, sP: done ? R.sP : null, tP: done ? R.tP : null,
                        vImpact: done ? R.vImpact : null, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    kk = Math.max(1, 600 / cw);
    fh = Math.round((cw < 500 ? 16 : 14) * kk);
    U = cw < 500 ? kk : Math.max(1, kk * 0.85);
    setLayout(cw < 500);
    labels = [];
    p.background(250);
    OY = 0; p.push(); situation(P, M, x, v, braking); p.pop();
    OY = RH; p.push(); p.translate(0, OY); graph(P, M, v); p.pop();
    window.simState.labels = labels;
  };

  // the road panel's rows follow the font: wide canvas 600×400 (graph below), phone 600 wide and taller (graph stacked)
  let L = {};
  function setLayout(n) {
    const sky = n ? 4.2 * fh : 3.4 * fh, road0 = sky + 0.5 * fh, road1 = road0 + (n ? 3.0 : 2.4) * fh;
    const ruler = road1 + 0.6 * fh, tickLab = ruler + 1.35 * fh, bar0 = tickLab + 0.6 * fh, bar1 = bar0 + 0.6 * fh, sLab = bar1 + 1.25 * fh;
    L = { sky, road0, road1, ruler, tickLab, bar0, bar1, sLab, XS: 40 + 2.2 * fh, XE: 600 - 3.2 * fh };
    RH = Math.round(sLab + 0.6 * fh);
    const H = n ? RH + Math.max(300, Math.round(11 * fh)) : 400;
    if (!laid || n !== narrow || CH !== H) { laid = true; narrow = n; CH = H; p.resizeCanvas(600, H); }
  }

  // --- the situation picture: the road to scale, the car, the stopped car ahead, v and a beside the car ---
  function situation(P, M, x, v, braking) {
    const c = p.drawingContext; c.save();
    const gr = c.createLinearGradient(0, 0, 0, L.sky); gr.addColorStop(0, 'rgb(208,230,251)'); gr.addColorStop(1, 'rgb(238,245,249)');
    c.fillStyle = gr; c.fillRect(0, 0, 600, L.sky); c.restore();
    p.noStroke(); p.fill(178, 242, 187); p.rect(0, L.sky, 600, L.road0 - L.sky);
    p.fill(43, 138, 62, 120);                                             // a row of spruces on the horizon
    for (let i = 0; i < 16; i++) { const tx0 = i * 40 + 10, h = (0.9 + 0.5 * ((i * 37) % 7) / 7) * fh; p.triangle(tx0 - 0.45 * h, L.sky, tx0 + 0.45 * h, L.sky, tx0, L.sky - h); }
    p.fill(...ROADC[P.keli]); p.rect(0, L.road0, 600, L.road1 - L.road0);
    p.stroke(...INKC); p.strokeWeight(2); p.line(0, L.road0, 600, L.road0); p.line(0, L.road1, 600, L.road1);
    const mid = (L.road0 + L.road1) / 2;
    p.noStroke(); p.fill(P.keli === 'luminen' ? 170 : 255);
    for (let xx = 10; xx < 600; xx += 60) p.rect(xx, mid - 2, 30, 4);
    if (P.keli === 'marka') { p.fill(165, 216, 255, 110); for (let i = 0; i < 8; i++) p.ellipse(40 + i * 75, mid + (i % 2 ? 0.25 : -0.25) * (L.road1 - L.road0), 46, 6); }
    if (P.keli === 'jainen') { p.fill(255, 255, 255, 180); for (let i = 0; i < 10; i++) p.rect(20 + i * 60, mid + (i % 2 ? 6 : -10), 26, 3, 2); }
    if (P.keli === 'luminen') { p.fill(190, 196, 204); p.rect(0, mid + 0.18 * (L.road1 - L.road0), 600, 3); p.rect(0, mid + 0.38 * (L.road1 - L.road0), 600, 3); }
    // the scale: metres along the road from the dashed line where the driver notices the danger
    const Lm = NICE.find((q) => q >= (M.d !== null ? M.d + 12 : M.sp * 1.03 + 2)) || 500;
    const px = (L.XE - L.XS) / Lm, X = (s) => L.XS + s * px;
    const steps = [2, 5, 10, 20, 25, 50, 100], step = steps.find((q) => Lm / q <= (narrow ? 5 : 6));
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(X(0), L.ruler, X(Lm), L.ruler);
    for (let s = 0; s <= Lm + 1e-9; s += step) { p.line(X(s), L.ruler, X(s), L.ruler + 6 * U); lab(`$${s}$`, X(s), L.tickLab, 'c', MUTEDC); }
    lab('$\\text{m}$', 600 - 6, L.tickLab, 'r', MUTEDC);
    const laneY = L.road0 + 0.68 * (L.road1 - L.road0), CL = 58 * U;
    if (M.d !== null) car(X(M.d) + CL, laneY, [190, 196, 204], false, true);        // the stopped car: its rear at d metres
    dash(X(0)); if (t >= P.tr) dash(X(M.sr));
    // the bars: the reaction distance green, the braking distance copper, as far as the car has come
    const xr = Math.min(x, M.sr);
    p.noStroke(); p.fill(...GREEN); if (xr > 0) p.rect(X(0), L.bar0, xr * px, L.bar1 - L.bar0);
    p.fill(...COPPERC); if (x > M.sr) p.rect(X(M.sr), L.bar0, (x - M.sr) * px, L.bar1 - L.bar0);
    if (done) barLabels(X(0), X(Math.min(x, M.sr)), X(x), x > M.sr);
    car(X(x), laneY, [230, 236, 240], braking || (done && !hit), false);
    if (done && hit) { p.stroke(201, 42, 42); p.strokeWeight(3 * U); p.noFill(); const cx = X(x) + 2, cy = laneY - 14 * U;
      for (let i = 0; i < 8; i++) { const an = i * Math.PI / 4; p.line(cx + 6 * U * Math.cos(an), cy + 6 * U * Math.sin(an), cx + 14 * U * Math.cos(an), cy + 14 * U * Math.sin(an)); } }
    const yv = L.road0 - 0.75 * fh, ya = yv - 1.3 * fh, cx = X(x) - CL * 0.5;
    if (v > 0.01 && !(done && hit)) motionArrow(cx, yv, 1, Math.max(16 * U, v * 1.8 * U), BLUE, '$\\overline{v}$');
    if (braking) motionArrow(cx, ya, -1, Math.max(16 * U, M.a * 5 * U), ORANGE, '$\\overline{a}$');
  }
  function dash(xx) { p.stroke(...INKC); p.strokeWeight(1.5 * U); for (let y = L.road0 - 0.4 * fh; y < L.ruler; y += 8) p.line(xx, y, xx, Math.min(y + 4, L.ruler)); }
  function barLabels(x0, xb, x1, both) {                                  // s_r left of the boundary, s_j right of it, never overlapping
    const sr = `$s_\\text{r}$`, sj = __(`lab_sj`);
    p.textSize(fh); const wr = p.textWidth(sr), wj = p.textWidth(sj);
    let r1 = Math.max(both ? xb - 4 : (x0 + xb) / 2 + wr / 2, 4 + wr), j0 = Math.max(xb + 4, r1 + 10);
    if (j0 + wj > 596) { j0 = 596 - wj; r1 = Math.min(r1, j0 - 10); }
    if (xb - x0 > 1) lab(sr, r1, L.sLab, 'r', GREEN);
    if (both) lab(sj, j0, L.sLab, 'l', COPPERC);
  }
  function car(front, yg, body, brake, parked) {                          // a car facing right, its front bumper at x = front
    const w = 58 * U, h = 18 * U, x0 = front - w;
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.fill(...body);
    p.rect(x0, yg - h, w, h * 0.62, 4 * U);
    p.beginShape(); p.vertex(x0 + w * 0.22, yg - h); p.vertex(x0 + w * 0.34, yg - h * 1.55); p.vertex(x0 + w * 0.7, yg - h * 1.55); p.vertex(x0 + w * 0.84, yg - h); p.endShape(p.CLOSE);
    p.fill(238, 245, 249); p.rect(x0 + w * 0.36, yg - h * 1.45, w * 0.15, h * 0.4, 2); p.rect(x0 + w * 0.54, yg - h * 1.45, w * 0.14, h * 0.4, 2);
    p.fill(brake ? [201, 42, 42] : [242, 166, 156]); p.rect(x0 - 1, yg - h * 0.9, 4 * U, 4 * U);
    if (!parked) { p.fill(255, 192, 120); p.rect(front - 4 * U, yg - h * 0.9, 4 * U, 4 * U); }
    p.fill(...INKC); p.circle(x0 + w * 0.22, yg - h * 0.32, h * 0.62); p.circle(x0 + w * 0.8, yg - h * 0.32, h * 0.62);
    p.fill(196, 204, 212); p.circle(x0 + w * 0.22, yg - h * 0.32, h * 0.26); p.circle(x0 + w * 0.8, yg - h * 0.32, h * 0.26);
  }
  function motionArrow(x, y, dir, len, col, name) {                       // a thin horizontal arrow with an open head: not a force
    const x2 = x + dir * len;
    p.stroke(...col); p.strokeWeight(2.5 * U); p.line(x, y, x2, y);
    p.line(x2, y, x2 - dir * 8 * U, y - 5 * U); p.line(x2, y, x2 - dir * 8 * U, y + 5 * U);
    p.textSize(fh); const w = p.textWidth(name);
    const right = Math.max(x, x2) + 6 * U, left = Math.min(x, x2) - 6 * U;
    if (right + w < 596) lab(name, right, y + fh * 0.36, 'l', col); else lab(name, left, y + fh * 0.36, 'r', col);
  }

  // --- the (t, v) graph: the reaction rectangle green, the braking triangle copper, the line blue, the current point ---
  function graph(P, M, v) {
    const PH = CH - RH;
    p.noStroke(); p.fill(255); p.rect(0, 0, 600, PH);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, 600, 0);
    const vmax = Math.ceil((M.v0 + 1) / 10) * 10, tmax = TNICE.find((q) => q >= M.tp * 1.12) || 30;
    const gx0 = 20 + 2.4 * fh, gx1 = 600 - 3.6 * fh, gy0 = PH - 1.9 * fh, gy1 = 2.1 * fh;
    const X = (tt) => gx0 + tt / tmax * (gx1 - gx0), Y = (vv) => gy0 - vv / vmax * (gy0 - gy1);
    const tStep = [0.5, 1, 2, 5, 10].find((q) => tmax / q <= (narrow ? 5 : 6)), vStep = vmax <= 20 ? 5 : 10;
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let s = tStep; s <= tmax + 1e-9; s += tStep) p.line(X(s), Y(0), X(s), Y(vmax));
    for (let s = vStep; s <= vmax + 1e-9; s += vStep) p.line(X(0), Y(s), X(tmax), Y(s));
    // the areas under the line so far: their areas are the distances
    const tt = t, trr = Math.min(tt, P.tr);
    p.noStroke(); p.fill(43, 138, 62, 70); if (trr > 0) p.rect(X(0), Y(M.v0), X(trr) - X(0), Y(0) - Y(M.v0));
    if (tt > P.tr) { p.fill(184, 98, 45, 80); p.beginShape(); p.vertex(X(P.tr), Y(0)); p.vertex(X(P.tr), Y(M.v0)); p.vertex(X(tt), Y(v)); p.vertex(X(tt), Y(0)); p.endShape(p.CLOSE); }
    p.stroke(...INKC); p.strokeWeight(2 * U);
    p.line(X(0), Y(0), X(tmax) + 12, Y(0)); p.line(X(0), Y(0), X(0), Y(vmax) - 12);
    p.noStroke(); p.fill(...INKC);
    p.triangle(X(tmax) + 18, Y(0), X(tmax) + 9, Y(0) - 4, X(tmax) + 9, Y(0) + 4); p.triangle(X(0), Y(vmax) - 18, X(0) - 4, Y(vmax) - 9, X(0) + 4, Y(vmax) - 9);
    for (let s = vStep; s <= vmax + 1e-9; s += vStep) lab(`$${s}$`, X(0) - 6, Y(s) + fh * 0.36, 'r', MUTEDC);
    for (let s = tStep; s < tmax - 1e-9; s += tStep) lab(`$${tx(s, s % 1 ? 1 : 0)}$`, X(s), Y(0) + fh * 1.3, 'c', MUTEDC);
    lab('$0$', X(0) - 6, Y(0) + fh * 1.3, 'r', MUTEDC);
    lab('$v\\ (\\text{m/s})$', X(0) + 10, Y(vmax) - 12 - fh * 0.45, 'l', INKC);
    lab('$t\\ (\\text{s})$', 600 - 6, Y(0) + fh * 1.3, 'r', INKC);
    // the line so far
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(2.5 * U); p.beginShape();
    p.vertex(X(0), Y(M.v0)); p.vertex(X(trr), Y(M.v0)); if (tt > P.tr) p.vertex(X(tt), Y(v)); p.endShape();
    p.noStroke(); p.fill(...BLUE); p.circle(X(tt), Y(v), 8 * U); p.fill(255); p.circle(X(tt), Y(v), 3 * U);
    if (done && !hit) {                                                   // name the areas when they are big enough to hold a label
      p.textSize(fh); const wr = p.textWidth('$s_\\text{r}$');
      if (X(P.tr) - X(0) > wr + 8 && Y(0) - Y(M.v0) > fh * 1.6) lab('$s_\\text{r}$', (X(0) + X(P.tr)) / 2, (Y(0) + Y(M.v0)) / 2 + fh * 0.36, 'c', INKC);
      if (X(M.tp) - X(P.tr) > 3 * wr && Y(0) - Y(M.v0) > fh * 3) lab(__('lab_sj'), X(P.tr + M.tj / 3), Y(M.v0 / 3) + fh * 0.36, 'c', INKC);
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, yy, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, yy);
    labels.push({ s, x0, y0: OY + yy - 0.75 * fh, x1: x0 + w, y1: OY + yy + 0.25 * fh });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DECS = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DECS);
});
