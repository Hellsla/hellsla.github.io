// fy5-3 Ympyräliike ja ratanopeus: a puck tied to a string circles a stake on frictionless ice (top view), uniformly and
// counterclockwise, on a circle of radius r with period T. Model: the position on the circle follows from the simulated
// time exactly (one lap takes T), the speed is v = 2πr/T and f = 1/T; s = v·t is the path travelled and N the number of
// full laps. The main button starts the run and then becomes "Katkaise naru", which releases the puck: from then on nothing acts on it in the plane, so it moves on a straight
// line with the velocity it had at the release until it reaches the rink's boards (radius 3,8 m), where the run ends.
// After the release the sim measures, from the puck's actual displacement, the angle α between its path and the string's
// direction at the release and its speed after the release.
// Left (wide) or top (narrow): the rink with the path, the string, the puck and its velocity as a blue arrow tangent to
// the path; optionally the puck's places and velocities at twelve equal time steps over the last lap. Right or bottom:
// the velocity a twelfth of a lap ago (v̄₁, blue) and now (v̄₂, blue) drawn from one point, and their difference
// Δv̄ (ink). That panel has its own scale: the speed is drawn at a fixed length, so it shows only directions and the
// change relative to the speed. Every canvas text goes through lab(), which pushes its ink box to simState.labels.
// p5.js 1.9 instance mode.
new p5((p) => {
  const FENCE = 3.8, LAPS = 12;                                         // m: the boards; strobe steps per lap
  const BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178];
  // geometry: wide 600 x 400 (rink left, vectors right); narrow (sim-root < 500 px) 600 x 960, stacked at full width
  const WIDE = { cx: 190, cy: 200, z: 46, ox: 488, oy: 235, L: 94, H: 400, pw: 380 };
  const NARROW = { cx: 300, cy: 292, z: 72, ox: 330, oy: 772, L: 150, H: 960, pw: 600 };
  let G = WIDE, narrow = false, sk = 1, fh = 11, labels = [];
  let btn, slR, slT, lR, lT, selSpeed, cbTrail, readout;
  let t, running, phase, rel;                                            // rel: {t, x, y, vx, vy} at the release

  const params = () => ({ r: Number(slR.value()), T: Number(slT.value()) });
  const restart = () => { t = 0; running = false; phase = 'ympyra'; rel = null; };
  // the puck's place (m, y up) and velocity (m/s) at time tt, on the circle or after the release on the straight line
  function state(tt, P) {
    const v = 2 * Math.PI * P.r / P.T;
    if (rel && tt >= rel.t) { const d = tt - rel.t; return { x: rel.x + rel.vx * d, y: rel.y + rel.vy * d, vx: rel.vx, vy: rel.vy }; }
    const th = 2 * Math.PI * tt / P.T;
    return { x: P.r * Math.cos(th), y: P.r * Math.sin(th), vx: -v * Math.sin(th), vy: v * Math.cos(th) };
  }
  function release() {
    const P = params(), s = state(t, P);
    rel = { t, x: s.x, y: s.y, vx: s.vx, vy: s.vy }; phase = 'irti';
  }
  function advance(dt) {
    const P = params();
    t += dt;
    if (phase === 'irti') {                                              // the boards: |P_r + v̄ τ| = FENCE, P_r ⟂ v̄
      const v = Math.hypot(rel.vx, rel.vy), tau = Math.sqrt(FENCE * FENCE - P.r * P.r) / v;
      if (t - rel.t >= tau) { t = rel.t + tau; phase = 'loppu'; running = false; }
    }
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    // one main button walks through the run: Käynnistä -> (circling) Katkaise naru -> (at the boards) Käynnistä again
    btn.elt.addEventListener('click', () => {
      if (phase === 'loppu') { restart(); running = true; }
      else if (phase === 'ympyra' && running) release();
      else if (phase === 'ympyra') running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l1); slR = p.createSlider(0.5, 3, 2, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l2); slT = p.createSlider(2, 10, 4, 1).parent(l2);
    const lk = p.createElement('label').parent(controls); cbTrail = p.createCheckbox('', true).parent(lk); p.createSpan(__('aiemmat')).parent(lk);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    for (const e of [slR.elt, slT.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { r: { input: slR.elt, unit: 'm' }, T: { input: slT.elt, unit: 's' } },
      reset: () => { slR.value(2); slT.value(4); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    if (running) advance(Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
    const P = params(), v = 2 * Math.PI * P.r / P.T, f = 1 / P.T, dtStep = P.T / LAPS;
    const now = state(t, P), before = state(rel ? Math.max(t - dtStep, rel.t) : t - dtStep, P);
    const dvx = now.vx - before.vx, dvy = now.vy - before.vy, dv = Math.hypot(dvx, dvy);
    const tCircle = rel ? rel.t : t, N = Math.floor(tCircle / P.T + 1e-9);
    let alpha = null, vIrti = null;
    if (rel && t - rel.t > 1e-6) {                                       // measured from the puck's actual displacement
      const dx = now.x - rel.x, dy = now.y - rel.y, d = Math.hypot(dx, dy), rr = Math.hypot(rel.x, rel.y);
      alpha = Math.acos(Math.min(1, Math.abs(dx * rel.x + dy * rel.y) / (d * rr))) * 180 / Math.PI;
      vIrti = d / (t - rel.t);
    }
    lR.html(__('sade', { r: tx(P.r, 1) }));
    lT.html(__('kierrosaika', { T: tx(P.T, 0) }));
    const bt = phase === 'ympyra' && !running || phase === 'loppu' ? __('kaynnista') : __('katkaise');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    btn.elt.disabled = phase === 'irti';
    readout.html(__('lukemat', { f: tx(f, 3), v: tx(v, 2), t: tx(t, 2), s: tx(v * t, 2), N: String(N), dv: tx(dv, 2) })
      + '<br>' + (alpha === null ? __('ehja') : __('irti', { a: tx(alpha, 1), vi: tx(vIrti, 2) })));
    window.simState = { r: P.r, T: P.T, f, v, t, s: v * t, N, dv, dvRatio: v > 0 ? dv / v : 0, phase, running, released: !!rel,
      alpha, vIrti, x: now.x, y: now.y, vx: now.vx, vy: now.vy, trail: cbTrail.checked(), labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;                                                 // strokes grow with the label size on a phone
    fh = narrow ? Math.round(14 * k) : Math.round(13 * k);
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state: draw again next frame
    labels = [];
    p.background(255);
    rink(P, v, now, dtStep);
    vectors(now, before, dv, v);
    window.simState.labels = labels;
  };

  // --- the rink seen from above ---
  function rink(P, v, now, dtStep) {
    const { cx, cy, z } = G, X = (xm) => cx + xm * z, Y = (ym) => cy - ym * z;
    const pw = G.pw, ph = narrow ? 584 : 400;
    grect(0, 0, pw, ph, [[208, 230, 251], [238, 245, 249]]);
    const c = p.drawingContext; c.save();                               // the ice inside the boards
    const gr = c.createRadialGradient(cx - 40 * sk, cy - 50 * sk, 10, cx, cy, FENCE * z);
    gr.addColorStop(0, '#ffffff'); gr.addColorStop(1, '#eef5f9'); c.fillStyle = gr;
    c.beginPath(); c.arc(cx, cy, FENCE * z, 0, 2 * Math.PI); c.fill(); c.restore();
    p.stroke(165, 216, 255); p.strokeWeight(1.5 * sk);
    for (const [a, b, l] of [[-0.9, 1.4, 1.1], [0.6, -1.7, 0.9], [-2.0, -0.6, 0.7], [1.9, 1.2, 0.8]]) p.line(X(a), Y(b), X(a + l), Y(b - 0.15));
    p.noFill(); p.stroke(255); p.strokeWeight(10 * sk); p.circle(cx, cy, 2 * FENCE * z + 8 * sk);   // the boards
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(cx, cy, 2 * FENCE * z); p.circle(cx, cy, 2 * FENCE * z + 16 * sk);
    // the path
    p.stroke(...RULEC); p.strokeWeight(2 * sk); p.drawingContext.setLineDash([7 * sk, 6 * sk]); p.circle(cx, cy, 2 * P.r * z); p.drawingContext.setLineDash([]);
    const A = 12 * z / 50;                                               // px per (m/s) in the picture
    // the places and velocities at twelve equal steps over the last lap
    if (cbTrail.checked()) for (let j = LAPS; j >= 1; j--) {
      const tt = t - j * dtStep; if (tt < -1e-9) continue;
      const s = state(tt, P);
      p.noStroke(); p.fill(31, 41, 51, 70); p.circle(X(s.x), Y(s.y), 13 * sk);
      vArrow(X(s.x), Y(s.y), s.vx * A, -s.vy * A, [...BLUE, 110], 2.5 * sk);
    }
    // the stake, the string (or its stub after the release) and the flight path
    if (rel) {
      p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 5 * sk]);
      p.line(X(rel.x), Y(rel.y), X(now.x), Y(now.y)); p.drawingContext.setLineDash([]);
      p.stroke(...MUTEDC); p.strokeWeight(2.5 * sk); p.line(cx, cy, X(rel.x * 0.35), Y(rel.y * 0.35));
    } else {
      p.stroke(...MUTEDC); p.strokeWeight(2.5 * sk); p.line(cx, cy, X(now.x), Y(now.y));
      const mx = (cx + X(now.x)) / 2, my = (cy + Y(now.y)) / 2, sp = Math.hypot(now.vx, now.vy);
      lab('$r$', mx - now.vx / sp * fh * 0.9, my + now.vy / sp * fh * 0.9 + fh * 0.36, 'c', MUTEDC);
    }
    p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(cx, cy, 12 * sk);
    // the puck and its velocity
    p.fill(...INKC); p.noStroke(); p.circle(X(now.x), Y(now.y), 20 * sk);
    p.noFill(); p.stroke(138, 150, 163); p.strokeWeight(2 * sk); p.circle(X(now.x), Y(now.y), 12 * sk);
    if (phase !== 'loppu') {
      const sp = Math.hypot(now.vx, now.vy), len = Math.max(14 * sk, sp * A), ux = now.vx / sp, uy = -now.vy / sp;
      const x0 = X(now.x) + ux * 11 * sk, y0 = Y(now.y) + uy * 11 * sk;
      vArrow(x0, y0, ux * len, uy * len, BLUE, 3.5 * sk);
      const lx = Math.min(pw - fh, Math.max(fh, x0 + ux * (len + fh * 0.9))), ly = Math.min(ph - 4, Math.max(fh * 1.2, y0 + uy * (len + fh * 0.9) + fh * 0.36));
      lab('$\\overline{v}$', lx, ly, 'c', BLUE);
    }
    // the scale
    const sy = ph - 16 * sk;
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(14, sy, 14 + z, sy); p.line(14, sy - 5 * sk, 14, sy + 5 * sk); p.line(14 + z, sy - 5 * sk, 14 + z, sy + 5 * sk);
    lab('$1\\,\\text{m}$', 14 + z / 2, sy - 8 * sk, 'c', INKC);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, ph, 600, ph); else p.line(pw, 0, pw, 400);
  }

  // --- the velocities a twelfth of a lap apart from one point, and their difference ---
  function vectors(now, before, dv, v) {                                 // larger labels: this panel carries the point
    const fh0 = fh;
    try { vectors2(now, before, dv, v); } finally { fh = fh0; }
  }
  function vectors2(now, before, dv, v) {
    const fV = Math.round(fh * (narrow ? 1.25 : 1.15));       // the vector labels; the title and Δt keep the base size
    const { L } = G;
    const tx0 = narrow ? 14 : 392, ty0 = narrow ? 584 + fh * 1.4 : 14 + fh;
    lab(__('muutos'), tx0, ty0, 'l', INKC);
    lab('$\\Delta t = \\tfrac{T}{12}$', tx0, ty0 + fh * 2, 'l', MUTEDC);
    fh = fV;
    const s1 = Math.hypot(before.vx, before.vy), s2 = Math.hypot(now.vx, now.vy);
    if (phase === 'loppu' || s2 < 1e-9) return;
    const u1 = [before.vx / s1, -before.vy / s1], u2 = [now.vx / s2, -now.vy / s2];
    // the triangle is centred in its panel: its bounding box (origin, both tips) sits on the panel's centre
    const bx = [0, L * u1[0], L * u2[0]], by = [0, L * u1[1], L * u2[1]];
    const ox = G.ox - (Math.min(...bx) + Math.max(...bx)) / 2, oy = G.oy - (Math.min(...by) + Math.max(...by)) / 2;
    const a1 = [ox + L * u1[0], oy + L * u1[1]], a2 = [ox + L * u2[0], oy + L * u2[1]];
    p.noStroke(); p.fill(...INKC); p.circle(ox, oy, 7 * sk);
    if (dv / v < 1e-6) {
      vArrow(ox, oy, L * u2[0], L * u2[1], BLUE, 3.5 * sk);
      lab('$\\overline{v}_1 = \\overline{v}_2$', a2[0] + u2[0] * fh * 1.2, a2[1] + u2[1] * fh * 1.2 + fh * 0.36, 'c', BLUE);
      lab('$\\Delta\\overline{v} = 0$', tx0, ty0 + fh * 4, 'l', INKC);
      return;
    }
    vArrow(ox, oy, L * u1[0], L * u1[1], BLUE, 3.5 * sk);
    vArrow(ox, oy, L * u2[0], L * u2[1], BLUE, 3.5 * sk);
    vArrow(a1[0], a1[1], a2[0] - a1[0], a2[1] - a1[1], INKC, 3 * sk, true);
    lab('$\\overline{v}_1$', a1[0] + u1[0] * fh * 0.9, a1[1] + u1[1] * fh * 0.9 + fh * 0.36, 'c', BLUE);
    lab('$\\overline{v}_2$', a2[0] + u2[0] * fh * 0.9, a2[1] + u2[1] * fh * 0.9 + fh * 0.36, 'c', BLUE);
    const mx = (a1[0] + a2[0]) / 2, my = (a1[1] + a2[1]) / 2, md = Math.hypot(mx - ox, my - oy);
    lab('$\\Delta\\overline{v}$', mx + (mx - ox) / md * fh * 2.3, my + (my - oy) / md * fh * 2.3 + fh * 0.36, 'c', INKC);
  }

  // an arrow from (x, y) along (dx, dy) px with a filled head
  function vArrow(x, y, dx, dy, col, w, small) {
    const L = Math.hypot(dx, dy); if (L < 0.5) return;
    const ux = dx / L, uy = dy / L, H = Math.min((small ? 10 : 12) * sk, L * 0.6), x2 = x + dx, y2 = y + dy, a = Math.atan2(uy, ux);
    p.stroke(...col); p.strokeWeight(w); p.line(x, y, x2 - H * 0.8 * ux, y2 - H * 0.8 * uy);
    p.noStroke(); p.fill(...col);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.42), y2 - H * Math.sin(a - 0.42), x2 - H * Math.cos(a + 0.42), y2 - H * Math.sin(a + 0.42));
  }
  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);           // never past the canvas edge
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  function grect(x, y, w, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, w, h); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
