// fy7-15 Valon polarisaatio: unpolarised light from a lamp passes two or three ideal polarisers in a row and falls on a
// screen. Each polariser's transmission axis is at θ from the vertical (sliders 0–180°, step 5°). Model: the first
// polariser passes half of the unpolarised intensity, I1 = I0 / 2; every later one obeys Malus's law
// I = I_prev cos²(θ − θ_prev). Intensities are given as percentages of I0. Oblique side view, not to scale: the
// electric field of the polarised light is drawn as a wave in the plane of the previous axis, its amplitude
// proportional to √I; under the beam, views along the beam show each stage's oscillation direction. Static: drawn
// again on every frame, no animation, no randomness. Every canvas text goes through lab().
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RAYC = [230, 73, 128], EC = [138, 95, 34], GLASSC = [238, 245, 249];
  const FILM = [201, 194, 178], PAPERC = [250, 250, 250], LAMPC = [255, 192, 120];
  const XL = 48, XP = [170, 300, 430], XS = 548, YB = 125, R = 58, SQ = 0.34, E0 = 40;
  let sel, sl = [], lb = [], readout, labels = [];

  const rad = (d) => d * Math.PI / 180, c2 = (d) => Math.cos(rad(d)) ** 2;
  const state = () => {
    const n = Number(sel.value()), t = sl.map((s) => Number(s.value()));
    const i1 = 50, i2 = n === 3 ? i1 * c2(t[1] - t[0]) : i1;
    const i3 = n === 3 ? i2 * c2(t[2] - t[1]) : i1 * c2(t[2] - t[0]);
    return { n, theta1: t[0], theta2: t[1], theta3: t[2], i1, i2, i3, d: Math.abs(t[2] - t[0]), cos2: c2(t[2] - t[0]) };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('maara')).parent(l0); sel = p.createSelect().parent(l0);
    sel.option(__('kaksi'), '2'); sel.option(__('kolme'), '3'); sel.selected('2');
    const init = [0, 45, 30];
    for (let k = 0; k < 3; k++) {
      const l = p.createElement('label').parent(controls); lb[k] = p.createSpan('').parent(l);
      sl[k] = p.createSlider(0, 180, init[k], 5).parent(l);
    }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { n: { input: sel.elt, unit: '' }, theta1: { input: sl[0].elt, unit: '°' }, theta2: { input: sl[1].elt, unit: '°' }, theta3: { input: sl[2].elt, unit: '°' } },
      reset: () => { sel.selected('2'); sl[0].value(0); sl[1].value(45); sl[2].value(30); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lb[0].html(__('p1', { t: tx(s.theta1, 0) })); lb[1].html(__(s.n === 3 ? 'p2' : 'p2_pois', { t: tx(s.theta2, 0) }));
    lb[2].html(__('p3', { t: tx(s.theta3, 0) }));
    readout.html(__(s.n === 3 ? 'lukemat3' : 'lukemat2', { i1: tx(s.i1, 1), i2: tx(s.i2, 1), i3: tx(s.i3, 1), d: tx(s.d, 0), c: tx(s.cos2, 3) }));
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.round(14 * k), H = k > 1.2 ? 440 : 400;
    if (p.__H !== H) { p.__H = H; p.resizeCanvas(600, H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(...PAPERC);
    scene(s, fh);
    views(s, fh, H);
    window.simState = { n: s.n, theta1: s.theta1, theta2: s.theta2, theta3: s.theta3, i1: s.i1, i2: s.i2, i3: s.i3, d: s.d, cos2: s.cos2, labels };
  };

  // the stages along the beam: [x of the start, x of the end, intensity %, axis angle or null for unpolarised]
  function stages(s) {
    const ps = s.n === 3 ? [0, 1, 2] : [0, 2], out = [[XL + 24, XP[ps[0]] - R * SQ - 4, 100, null]];
    const I = s.n === 3 ? [s.i1, s.i2, s.i3] : [s.i1, s.i3], th = ps.map((k) => [s.theta1, s.theta2, s.theta3][k]);
    for (let j = 0; j < ps.length; j++) {
      const xa = XP[ps[j]] + R * SQ + 4, xb = j + 1 < ps.length ? XP[ps[j + 1]] - R * SQ - 4 : XS - 14;
      out.push([xa, xb, I[j], th[j]]);
    }
    return { out, ps, th };
  }

  function scene(s, fh) {
    const { out, ps, th } = stages(s);
    // the lamp: a glowing bulb on a dark base
    p.noStroke(); p.fill(...LAMPC, 90); p.circle(XL, YB, 64);
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...LAMPC); p.circle(XL, YB, 36);
    p.fill(108, 117, 125); p.rect(XL - 10, YB + 18, 20, 16, 3);
    lab(`$\\text{${__('lamppu')}}$`, 14, 55, 'l', fh, INKC);
    // the beam axis, fainter where the light is weaker
    for (const [xa, xb, I] of out) { p.stroke(...RAYC, 60 + 195 * Math.min(1, I / 50)); p.strokeWeight(2); p.line(xa, YB, xb, YB); }
    // the electric field in each stage
    for (const [xa, xb, I, a] of out) {
      if (a === null) { for (const x of [xa + 14, (xa + xb) / 2, xb - 14]) star(x, YB, E0 * 0.8); continue; }
      wave(xa, xb, E0 * Math.sqrt(I / 50) * 0.95, a);
    }
    // the polarisers: oblique discs with lines along the transmission axis
    ps.forEach((k, j) => disc(XP[k], YB, th[j]));
    ps.forEach((k) => lab(`$\\text{P}_${k + 1}$`, XP[k], 55, 'c', fh, INKC));
    // the screen and its bright spot
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...GLASSC);
    p.quad(XS - 8, YB - 52, XS + 8, YB - 64, XS + 8, YB + 52, XS - 8, YB + 64);
    p.noStroke(); p.fill(...RAYC, 255 * Math.min(1, s.i3 / 50)); p.ellipse(XS, YB, 12, 34);
    lab(`$\\text{${__('varjostin')}}$`, 592, 55, 'r', fh, INKC);
  }

  function disc(x, y, a) {
    p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...FILM, 150); p.ellipse(x, y, 2 * R * SQ, 2 * R);
    const ux = Math.sin(rad(a)), uy = Math.cos(rad(a)), vx = Math.cos(rad(a)), vy = -Math.sin(rad(a));
    p.stroke(...MUTEDC); p.strokeWeight(1.5);
    for (let d = -R + 9; d <= R - 9; d += 9) {
      const h = Math.sqrt(R * R - d * d) - 3;
      const P = (t) => [x + (d * vx + t * ux) * SQ, y - (d * vy + t * uy)];
      const [x1, y1] = P(-h), [x2, y2] = P(h); p.line(x1, y1, x2, y2);
    }
    p.stroke(...INKC); p.strokeWeight(3);
    p.line(x - R * ux * SQ, y + R * uy, x + R * ux * SQ, y - R * uy);
  }

  function wave(xa, xb, A, a) {
    if (A < 1) return;
    const ux = Math.sin(rad(a)) * SQ, uy = -Math.cos(rad(a)), L = 46, pts = [];
    for (let x = xa; x <= xb + 0.01; x += 2) pts.push([x, Math.sin(2 * Math.PI * (x - xa) / L)]);
    p.stroke(...EC, 110); p.strokeWeight(1.5);
    for (let j = 0; j < pts.length; j += 3) { const [x, v] = pts[j]; p.line(x, YB, x + A * v * ux, YB + A * v * uy); }
    p.noFill(); p.stroke(...EC); p.strokeWeight(2.5); p.beginShape();
    for (const [x, v] of pts) p.vertex(x + A * v * ux, YB + A * v * uy);
    p.endShape();
  }

  function star(x, y, L) {
    for (const a of [0, 45, 90, 135]) dbl(x, y, Math.sin(rad(a)) * SQ * 1.6, -Math.cos(rad(a)), L * 0.55, 2, 7);
  }

  // a double arrow through (x, y) along the screen direction (dx, dy) with half-length L
  function dbl(x, y, dx, dy, L, w, h) {
    const m = Math.hypot(dx, dy); dx /= m; dy /= m;
    if (L < 3) return;
    p.stroke(...EC); p.strokeWeight(w); p.line(x - dx * (L - h), y - dy * (L - h), x + dx * (L - h), y + dy * (L - h));
    p.noStroke(); p.fill(...EC);
    for (const sgn of [1, -1]) {
      const tx0 = x + sgn * dx * L, ty0 = y + sgn * dy * L, bx = tx0 - sgn * dx * h, by = ty0 - sgn * dy * h;
      p.triangle(tx0, ty0, bx - dy * h * 0.5, by + dx * h * 0.5, bx + dy * h * 0.5, by - dx * h * 0.5);
    }
  }

  // views along the beam under each stage: the polariser's axis (dashed) and the field's oscillation direction
  function views(s, fh, H) {
    const { out } = stages(s);
    const yc = H - 120, r = 34;
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]);
    for (const [xa, xb] of out) { const x = (xa + xb) / 2; p.line(x, YB + 50, x, yc - r - 6); }
    p.drawingContext.setLineDash([]);
    for (const [xa, xb, I, a] of out) {
      const x = (xa + xb) / 2;
      p.stroke(...INKC); p.strokeWeight(2); p.fill(...GLASSC); p.circle(x, yc, 2 * r);
      if (a === null) { for (const b of [0, 45, 90, 135]) dbl(x, yc, Math.sin(rad(b)), -Math.cos(rad(b)), 26, 2.5, 8); }
      else {
        p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([4, 4]);
        p.line(x - Math.sin(rad(a)) * (r - 3), yc + Math.cos(rad(a)) * (r - 3), x + Math.sin(rad(a)) * (r - 3), yc - Math.cos(rad(a)) * (r - 3));
        p.drawingContext.setLineDash([]);
        dbl(x, yc, Math.sin(rad(a)), -Math.cos(rad(a)), 28 * Math.sqrt(I / 50), 3, 9);
      }
      lab(`$${tx(I, 1)}\\,\\%$`, x, yc + r + 10 + fh, 'c', fh, INKC);
    }
  }

  // every canvas text: drawn and its ink box pushed to simState.labels (canvas coordinates)
  function lab(str, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(str), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(str, x0, y);
    labels.push({ s: str, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
