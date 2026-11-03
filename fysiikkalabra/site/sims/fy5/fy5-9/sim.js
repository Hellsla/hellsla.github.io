// fy5-9 Harmoninen värähtely ja heiluri: two oscillators, chosen with the select "Värähtelijä".
// Spring (jousi): a block of mass m on a frictionless horizontal track, fixed to a wall by a spring of spring constant k,
// pulled to x = A and released from rest; the only horizontal force is the harmonic force F = −kx, so a = −(k/m)x.
// Pendulum (heiluri): a mathematical pendulum (point mass m on a light string of length l, no air resistance), released
// from rest at the angle α0; the true nonlinear equation α'' = −(g/l) sin α is integrated, so large angles give a
// period a little longer than 2π√(l/g) and small ones agree with it.
// Both are integrated with velocity Verlet (simulated time dt·speed, substeps of at most T/400). The period T shown is
// measured from the integrated motion (the time from the release back to the same extreme position, interpolated
// between steps, in a separate run of 4000 steps per period), never computed from a formula; f = 1/T, T10 = 10T, vmax
// the largest speed in that run, E the mechanical energy (½kA² for the spring, mgl(1 − cos α0) for the pendulum).
// Left (wide) or top (phone): the picture; the spring shows the force F (red, thick), the acceleration (orange, thin)
// and the velocity (blue, thin) in rows above the block; the pendulum the velocity and the acceleration beside the
// bob (one fixed scale for every setting); the spring's arrow lengths are relative to their largest value in the motion. Under the picture the energy as one bar of
// constant length split into E_k and E_p. Right (or below): the displacement against time (x in cm or α in degrees)
// over the last 6 s, with the period marked between the two latest extreme positions, and the stopwatch t and the
// number n of full periods since the release. Every canvas text goes through lab(), which pushes its ink box to
// simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, WIN = 6;                                                // window of the graph (s)
  const RED = [201, 42, 42], BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const EKC = [43, 138, 62], EPC = [112, 72, 232], RULEC = [227, 220, 203];
  let narrow = false, laid = false, U = 1, fh = 13, labels = [];
  const P = {}, G = {}, EB = {};                                          // panels: picture, graph, energy bar
  let btn, selTila, selSpeed, slM, slK, slA, slL, slAl, lM, lK, lA, lL, lAl, boxK, boxA, boxL, boxAl, readout;
  let running = false, x = 0, v = 0, acc = 0, t = 0, trace = [], peaks = [0], key = '', per = { T: 1, vmax: 0 }, nper = 0;

  const prm = () => {
    const tila = selTila.value(), m = Number(slM.value()), k = Number(slK.value()), A = Number(slA.value());
    const l = Number(slL.value()), al0 = Number(slAl.value());
    return { tila, m, k, A, l, al0, X0: tila === 'jousi' ? A : al0 * Math.PI / 180 };
  };
  // the acceleration of the state variable: x'' = −(k/m) x (metres) or α'' = −(g/l) sin α (radians)
  const accel = (P_, X) => (P_.tila === 'jousi' ? -P_.k / P_.m * X : -g / P_.l * Math.sin(X));
  const T0 = (P_) => (P_.tila === 'jousi' ? 2 * Math.PI * Math.sqrt(P_.m / P_.k) : 2 * Math.PI * Math.sqrt(P_.l / g));

  // the period measured from the integrated motion: from the release at rest at X0 to the next return to rest at X0
  function measure(P_) {
    const h = T0(P_) * 1.2 / 4000;
    let X = P_.X0, V = 0, A_ = accel(P_, X), tt = 0, half = false, vmax = 0;
    for (let i = 0; i < 20000; i++) {
      const Vp = V;
      X += V * h + 0.5 * A_ * h * h; const An = accel(P_, X); V += 0.5 * (A_ + An) * h; A_ = An; tt += h;
      vmax = Math.max(vmax, Math.abs(V));
      if (!half && Vp < 0 && V >= 0) half = true;                          // the other extreme (−A or −α0)
      else if (half && Vp > 0 && V <= 0) return { T: tt - h * V / (V - Vp), vmax: P_.tila === 'jousi' ? vmax : vmax * P_.l };
    }
    return { T: NaN, vmax: NaN };
  }
  const energy = (P_, X, V) => {                                          // [E_k, E_p] in joules
    if (P_.tila === 'jousi') return [0.5 * P_.m * V * V, 0.5 * P_.k * X * X];
    return [0.5 * P_.m * (P_.l * V) ** 2, P_.m * g * P_.l * (1 - Math.cos(X))];
  };
  const restart = () => { const P_ = prm(); running = false; x = P_.X0; v = 0; acc = accel(P_, x); t = 0; trace = [[0, x]]; peaks = [0]; nper = 0; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lt = p.createElement('label').parent(controls); p.createSpan(__('varahtelija')).parent(lt); selTila = p.createSelect().parent(lt);
    selTila.option(__('jousi'), 'jousi'); selTila.option(__('heiluri'), 'heiluri'); selTila.selected('jousi');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const slider = (a, b, v0, st) => { const L = p.createElement('label').parent(controls); const s = p.createSpan('').parent(L); return [L, s, p.createSlider(a, b, v0, st).parent(L)]; };
    let boxM; [boxM, lM, slM] = slider(0.10, 2.00, 0.50, 0.05);
    [boxK, lK, slK] = slider(5, 100, 20, 5);
    [boxA, lA, slA] = slider(0.02, 0.20, 0.10, 0.01);
    [boxL, lL, slL] = slider(0.25, 1.50, 1.00, 0.05);
    [boxAl, lAl, slAl] = slider(2, 60, 10, 1);
    for (const e of [selTila.elt, slM.elt, slK.elt, slA.elt, slL.elt, slAl.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    controls.style('column-gap', '0.75rem');
    for (const L of [boxM, boxK, boxA, boxL, boxAl]) L.style('flex', '1 1 10rem');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    { const P0 = prm(); key = [P0.tila, P0.m, P0.k, P0.A, P0.l, P0.al0].join("|"); per = measure(P0); window.simState = state(P0, []); }   // a state before the first frame
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tila: { input: selTila.elt, unit: '' }, m: { input: slM.elt, unit: 'kg' }, k: { input: slK.elt, unit: 'N/m' },
        A: { input: slA.elt, unit: 'm' }, l: { input: slL.elt, unit: 'm' }, alfa: { input: slAl.elt, unit: '°' } },
      reset: () => { selTila.selected('jousi'); slM.value(0.50); slK.value(20); slA.value(0.10); slL.value(1.00); slAl.value(10); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function advance(P_) {
    if (!running) return;
    let dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    const hmax = per.T / 400;
    while (dt > 1e-9) {
      const h = Math.min(dt, hmax); dt -= h;
      const vp = v;
      x += v * h + 0.5 * acc * h * h; const an = accel(P_, x); v += 0.5 * (acc + an) * h; acc = an; t += h;
      if (vp > 0 && v <= 0) { peaks.push(t - h * v / (v - vp)); nper++; }   // back at the release side's extreme position: one full period
      trace.push([t, x]);
    }
    while (trace.length > 2 && trace[1][0] < t - WIN - 0.5) trace.shift();
    if (peaks.length > 3) peaks.splice(0, peaks.length - 3);
  }

  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) { Object.assign(P, { x: 0, y: 0, w: 600, h: 380 }); Object.assign(G, { x: 0, y: 380, w: 600, h: 440 }); Object.assign(EB, { x: 0, y: 820, w: 600, h: 150 }); p.resizeCanvas(600, 970); }
    else { Object.assign(P, { x: 0, y: 0, w: 330, h: 290 }); Object.assign(G, { x: 330, y: 0, w: 270, h: 400 }); Object.assign(EB, { x: 0, y: 290, w: 330, h: 110 }); p.resizeCanvas(600, 400); }
    return true;
  }

  const state = (P_, labs) => {
    const [Ek, Ep] = energy(P_, x, v), E = energy(P_, P_.X0, 0)[1];
    return { tila: P_.tila, m: P_.m, k: P_.k, A: P_.A, l: P_.l, alfa: P_.al0, T: per.T, f: 1 / per.T, T10: 10 * per.T, vmax: per.vmax,
      E, Ek, Ep, x: P_.tila === 'jousi' ? x : x * 180 / Math.PI, v: P_.tila === 'jousi' ? v : v * P_.l, t, n: nper,
      running, labels: labs };
  };

  p.draw = () => {
    const P_ = prm();
    const cw = document.getElementById('sim-root').clientWidth || 600, kk = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) { restart(); p.redraw(); return; }
    const sig = [P_.tila, P_.m, P_.k, P_.A, P_.l, P_.al0].join('|');
    if (sig !== key) { key = sig; per = measure(P_); }
    advance(P_);
    const jousi = P_.tila === 'jousi';
    for (const [b, on] of [[boxK, jousi], [boxA, jousi], [boxL, !jousi], [boxAl, !jousi]]) b.style('display', on ? '' : 'none');
    lM.html(__('massa', { m: tx(P_.m, 2) }));
    lK.html(__('jousivakio', { k: tx(P_.k, 0) }));
    lA.html(__('amplitudi', { A: tx(P_.A, 2) }));
    lL.html(__('pituus', { l: tx(P_.l, 2) }));
    lAl.html(__('kulma', { a: tx(P_.al0, 0) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const [Ek, Ep] = energy(P_, x, v), E = energy(P_, P_.X0, 0)[1];
    readout.html(__('lukemat', { T: tx(per.T, 3), f: tx(1 / per.T, 3), T10: tx(10 * per.T, 2), Ek: en(Ek, E), Ep: en(Ep, E), E: en(E, E) }));
    window.simState = state(P_, null);
    U = narrow ? 0.9 * kk : 1;
    fh = Math.round((narrow ? 15 : 13) * kk);
    labels = [];
    p.background(250);
    if (jousi) spring(P_); else pendulum(P_);
    energyBar(P_, Ek, Ep, E);
    graph(P_);
    window.simState.labels = labels;
  };

  // --- the spring oscillator: wall, spring, block on a frictionless track; F, a and v in rows above the block ---
  function spring(P_) {
    grect(P.x, P.y, P.w, P.h, [[238, 245, 249], [246, 241, 230]], 0);
    lab(__('t_jousi'), P.x + 10, P.y + fh + 6, 'l', INKC);
    const Amax = 0.20, bw = 44 * U, bh = 40 * U, wall = P.x + 16, room = 30 * U;
    const s = (P.w - 16 - room - bw - 22) / (2 * Amax), xeq = wall + room + bw / 2 + Amax * s, ty = P.y + P.h * 0.7;
    p.noStroke(); p.fill(196, 204, 212); p.rect(P.x + 6, ty, P.w - 12, 8 * U, 2);                   // the track
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(P.x + 6, ty, P.x + P.w - 6, ty);
    p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(wall - 12 * U, ty - 70 * U, 12 * U, 70 * U);   // the wall
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * U); p.drawingContext.setLineDash([6 * U, 5 * U]);
    p.line(xeq, ty - bh - 76 * U, xeq, ty + 16 * U); p.drawingContext.setLineDash([]);
    for (const sx of [-1, 1]) { const xa = xeq + sx * P_.A * s; p.stroke(...MUTEDC); p.strokeWeight(2 * U); p.line(xa, ty + 2 * U, xa, ty + 14 * U); }
    lab('$x = 0$', xeq, ty + 16 * U + fh * 1.1, 'c', INKC);
    const cx = xeq + x * s, left = cx - bw / 2;
    // the spring: a zigzag of 12 coils from the wall to the block's left face
    const y0 = ty - bh / 2, n = 12, L = left - wall, amp = 9 * U;
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(2.4 * U); p.beginShape(); p.vertex(wall, y0); p.vertex(wall + 6 * U, y0);
    for (let i = 0; i < 2 * n; i++) p.vertex(wall + 6 * U + (L - 12 * U) * (i + 0.5) / (2 * n), y0 + (i % 2 ? amp : -amp));
    p.vertex(left - 6 * U, y0); p.vertex(left, y0); p.endShape();
    grect(left, ty - bh, bw, bh, [[217, 178, 106], [169, 122, 53]], 4 * U);                          // the block
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(left, ty - bh, bw, bh, 4 * U);
    const vm = per.vmax || 1, Lmax = 70 * U, top = ty - bh;
    const LF = -x / P_.A * Lmax, LV = v / vm * Lmax;                                                 // F and a ∝ −x, v relative to v_max
    arrowRow(cx, top - 14 * U, LF, RED, 4 * U, '$\\overline{F}$');
    arrowRow(cx, top - 38 * U, LF, ORANGE, 2.6 * U, '$\\overline{a}$');
    arrowRow(cx, top - 62 * U, LV, BLUE, 2.6 * U, '$\\overline{v}$');
  }
  function arrowRow(x0, y, L, col, w, s) {                                // a horizontal arrow from x0, length L (signed)
    if (Math.abs(L) < 6 * U) return;
    const x2 = x0 + L, d = Math.sign(L), H = (w > 3 * U ? 12 : 9) * U;
    p.stroke(...col); p.strokeWeight(w); p.noFill();
    if (w > 3 * U) { p.line(x0, y, x2 - d * H * 0.8, y); p.noStroke(); p.fill(...col); p.triangle(x2, y, x2 - d * H, y - H * 0.45, x2 - d * H, y + H * 0.45); }
    else { p.line(x0, y, x2, y); p.line(x2, y, x2 - d * H, y - H * 0.5); p.line(x2, y, x2 - d * H, y + H * 0.5); }
    lab(s, x2 + d * 14 * U, y + fh * 0.35, d > 0 ? 'l' : 'r', col);
  }

  // --- the pendulum: ceiling, string, bob; the velocity beside the bob, the acceleration from its edge ---
  function pendulum(P_) {
    grect(P.x, P.y, P.w, P.h, [[238, 245, 249], [246, 241, 230]], 0);
    lab(__('t_heiluri'), P.x + 10, P.y + fh + 6, 'l', INKC);
    const lmax = 1.5, py = P.y + 26 * U + fh, px = P.x + P.w / 2;
    const sc = Math.min((P.h - (py - P.y) - 30 * U) / lmax, (P.w / 2 - 24 * U) / (lmax * Math.sin(Math.PI / 3)));
    const R = P_.l * sc, br = 12 * U;
    const rx = P.x + 22 * U;                                             // a ruler from the pivot's level down, every 0,25 m
    p.stroke(...MUTEDC); p.strokeWeight(2 * U); p.line(rx, py, rx, py + lmax * sc);
    for (let q = 0; q <= lmax + 1e-9; q += 0.25) { const w = Math.abs(q * 2 - Math.round(q * 2)) < 1e-9 ? 10 : 6; p.line(rx, py + q * sc, rx + w * U, py + q * sc); }
    for (const q of [0.5, 1.0, 1.5]) lab(`$${tx(q, 1)}\\,\\text{m}$`, rx + 14 * U, py + q * sc + fh * 0.35, 'l', MUTEDC);
    p.noStroke(); p.fill(108, 117, 125); p.rect(px - 46 * U, py - 10 * U, 92 * U, 10 * U, 2);
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(px - 46 * U, py, px + 46 * U, py);
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * U); p.drawingContext.setLineDash([6 * U, 5 * U]);
    p.line(px, py, px, py + R + br + 12 * U);
    const a0 = P_.X0; p.noFill(); p.arc(px, py, 2 * R, 2 * R, Math.PI / 2 - a0, Math.PI / 2 + a0); p.drawingContext.setLineDash([]);
    const bx = px + R * Math.sin(x), by = py + R * Math.cos(x);
    p.stroke(...INKC); p.strokeWeight(1.8 * U); p.line(px, py, bx, by);
    p.fill(...INKC); p.noStroke(); p.circle(px, py, 6 * U);
    const c = p.drawingContext; c.save(); const gr = c.createRadialGradient(bx - 4 * U, by - 4 * U, 1, bx, by, br);
    gr.addColorStop(0, 'rgb(233,236,239)'); gr.addColorStop(1, 'rgb(108,117,125)'); c.fillStyle = gr; c.beginPath(); c.arc(bx, by, br, 0, 2 * Math.PI); c.fill(); c.restore();
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * U); p.circle(bx, by, 2 * br);
    // unit vectors (screen): tangent towards growing α and outward along the string
    const tu = [Math.cos(x), -Math.sin(x)], ou = [Math.sin(x), Math.cos(x)];
    const at = -g * Math.sin(x), an = P_.l * v * v;                       // tangential and inward normal acceleration (m/s²)
    // one fixed scale for every setting (a = g is 128 px, v = 1 m/s is 40 px, at most 90 px), so a small swing has small arrows
    const cap = (L) => Math.min(L, 90 * U), sa = 128 * U / g, sv = 40 * U;
    const a_ = Math.hypot(at, an), La = cap(a_ * sa), ax = a_ ? (at * tu[0] - an * ou[0]) / a_ * La : 0, ay = a_ ? (at * tu[1] - an * ou[1]) / a_ * La : 0;
    if (La > 6 * U) { const ux = ax / La, uy = ay / La; thin(bx + ux * (br + 3 * U), by + uy * (br + 3 * U), bx + ux * (br + 3 * U) + ax, by + uy * (br + 3 * U) + ay, ORANGE);
      lab('$\\overline{a}$', bx + ux * (br + 18 * U) + ax, by + uy * (br + 18 * U) + ay + fh * 0.35, 'c', ORANGE); }
    const Lv = Math.sign(v) * cap(Math.abs(v) * P_.l * sv), off = br + 14 * U;
    if (Math.abs(Lv) > 6 * U) { const sx = bx + ou[0] * off, sy = by + ou[1] * off, ex = sx + tu[0] * Lv, ey = sy + tu[1] * Lv;
      thin(sx, sy, ex, ey, BLUE); const d = Math.sign(Lv);
      lab('$\\overline{v}$', ex + tu[0] * d * 14 * U + ou[0] * 6 * U, ey + tu[1] * d * 14 * U + ou[1] * 6 * U + fh * 0.35, 'c', BLUE); }
    lab(`$l = ${tx(P_.l, 2)}\\,\\text{m}$`, P.x + P.w - 10, P.y + fh + 6, 'r', INKC);
  }
  function thin(x1, y1, x2, y2, col) {                                    // velocity or acceleration: thin, open head
    const a = Math.atan2(y2 - y1, x2 - x1), H = 9 * U;
    p.stroke(...col); p.strokeWeight(2.6 * U); p.noFill(); p.line(x1, y1, x2, y2);
    p.line(x2, y2, x2 - H * Math.cos(a - 0.5), y2 - H * Math.sin(a - 0.5)); p.line(x2, y2, x2 - H * Math.cos(a + 0.5), y2 - H * Math.sin(a + 0.5));
  }

  // --- the energy: one bar of constant length E, split into E_k (green) and E_p (violet) ---
  function energyBar(P_, Ek, Ep, E) {
    p.noStroke(); p.fill(255); p.rect(EB.x, EB.y, EB.w, EB.h);
    p.stroke(220); p.strokeWeight(1); p.line(EB.x, EB.y, EB.x + EB.w, EB.y);
    const X0 = EB.x + 16, W = EB.w - 32, bh = 18 * U, y = EB.y + EB.h * 0.52;
    const wk = E > 0 ? W * Ek / (Ek + Ep || 1) : 0;
    p.noStroke(); p.fill(...EKC); p.rect(X0, y - bh / 2, wk, bh); p.fill(...EPC); p.rect(X0 + wk, y - bh / 2, W - wk, bh);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5 * U); p.rect(X0, y - bh / 2, W, bh);
    lab('$E_\\text{k}$', X0, y - bh / 2 - fh * 0.45, 'l', EKC);
    lab('$E_\\text{p}$', X0 + W, y - bh / 2 - fh * 0.45, 'r', EPC);
    lab(`$E = E_\\text{k} + E_\\text{p} = ${en(E, E)}$`, X0 + W / 2, y + bh / 2 + fh * 1.2, 'c', INKC);
  }

  // --- the displacement against time over the last WIN seconds ---
  function graph(P_) {
    const jousi = P_.tila === 'jousi';
    p.noStroke(); p.fill(255); p.rect(G.x, G.y, G.w, G.h);
    p.stroke(220); p.strokeWeight(1); if (narrow) p.line(G.x, G.y, G.x + G.w, G.y); else p.line(G.x, G.y, G.x, G.y + G.h);
    lab(`$t = ${tx(t, 2)}\\,\\text{s}$`, G.x + 12, G.y + fh + 6, 'l', INKC);
    lab(`$n = ${nper}$`, G.x + G.w - 12, G.y + fh + 6, 'r', INKC);
    const x0 = G.x + 18 + fh * 2.4, x1 = G.x + G.w - 18 - fh * 3, yT = G.y + 2.2 * fh + (narrow ? 28 : 40) * U, yB = G.y + G.h - 2 * fh - 18;
    const ym = (yT + yB) / 2, Y0 = jousi ? P_.A * 100 : P_.al0, half = (yB - yT) / 2, Ys = half / (1.25 * Y0);
    const ta = Math.max(0, t - WIN), X = (tt) => x0 + (tt - ta) / WIN * (x1 - x0), Y = (yy) => ym - yy * Ys;
    p.stroke(...RULEC); p.strokeWeight(1.5);
    for (const yy of [-Y0, Y0]) p.line(x0, Y(yy), x1, Y(yy));
    const step = 1, first = Math.ceil(ta);
    const every = fh > 20 ? 2 : 1;
    for (let tt = first; tt <= ta + WIN + 1e-9; tt += step) {
      p.stroke(...RULEC); p.strokeWeight(1.5); p.line(X(tt), yT, X(tt), yB);
      p.stroke(...INKC); p.strokeWeight(2); p.line(X(tt), yB, X(tt), yB + 6);
      if (Math.round(tt) % every === 0) lab(`$${tx(tt, 0)}$`, X(tt), yB + 8 + fh, 'c', MUTEDC);
    }
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(x0, yB, x1 + 6, yB); p.line(x0, yB, x0, yT - 10); p.line(x0, ym, x1, ym);
    p.noStroke(); p.fill(...INKC); p.triangle(x1 + 16, yB, x1 + 4, yB - 5, x1 + 4, yB + 5); p.triangle(x0, yT - 20, x0 - 5, yT - 8, x0 + 5, yT - 8);
    for (const yy of [-Y0, 0, Y0]) { p.stroke(...INKC); p.strokeWeight(2); p.line(x0 - 6, Y(yy), x0, Y(yy)); lab(`$${tx(yy, 0)}$`, x0 - 9, Y(yy) + fh * 0.35, 'r', MUTEDC); }
    lab(jousi ? '$x\\ (\\text{cm})$' : '$\\alpha\\ ({}^\\circ)$', x0 - 4, yT - 20 - fh * 0.6, 'l', INKC);
    lab('$t\\ (\\text{s})$', x1 + 20, yB + fh * 0.35, 'l', INKC);
    // the curve
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.beginShape();
    for (const [tt, xx] of trace) if (tt >= ta - 1e-9) p.vertex(X(tt), Y(jousi ? xx * 100 : xx * 180 / Math.PI));
    p.endShape();
    if (trace.length) { const [tt, xx] = trace[trace.length - 1]; p.noStroke(); p.fill(...INKC); p.circle(X(tt), Y(jousi ? xx * 100 : xx * 180 / Math.PI), 9); }
    // the period between the two latest extreme positions on the release side
    if (peaks.length >= 2) {
      const a = peaks[peaks.length - 2], b = peaks[peaks.length - 1];
      if (a >= ta) {
        const yy = Y(Y0) - 12 * U;
        p.stroke(...INKC); p.strokeWeight(1.8); p.line(X(a), yy, X(b), yy); p.line(X(a), yy - 6, X(a), yy + 6); p.line(X(b), yy - 6, X(b), yy + 6);
        lab('$T$', (X(a) + X(b)) / 2, yy - 6, 'c', INKC);
      }
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x0, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xl = align === 'r' ? x0 - w : align === 'c' ? x0 - w / 2 : x0;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, xl, y);
    labels.push({ s, x0: xl, y0: y - 0.75 * fh, x1: xl + w, y1: y + 0.25 * fh });
  }
  function grect(x0, y0, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x0, y0, x0, y0 + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.beginPath(); c.roundRect(x0, y0, w, h, r); c.fill(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (z, d) => z.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  // an energy in LaTeX with its unit: in mJ when the oscillation's energy E is under 0,1 J, three significant figures
  const en = (z, E) => (E < 0.1 ? sg(z * 1000) + '\\,\\text{mJ}' : sg(z) + '\\,\\text{J}');
  const sg = (z) => (Math.abs(z) < 1e-12 ? '0' : z >= 1 ? z.toFixed(z >= 10 ? 1 : 2) : z.toPrecision(3)).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
