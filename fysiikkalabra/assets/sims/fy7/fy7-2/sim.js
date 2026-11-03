// fy7-2 Varatun hiukkasen liike sähkö- ja magneettikentässä: a charged particle (proton, deuteron, alpha particle or a
// negative hydrogen ion H⁻) enters a vacuum chamber through a slit in its left wall, moving to the right at the speed
// v. In the chamber a uniform magnetic field B points out of or into the page (green • or ×) and a uniform electric
// field E points up between two plates (bottom plate +, top plate −). The motion is integrated with the Boris method
// (it keeps the speed exactly when E = 0): m dv/dt = q (E + v × B), non-relativistic (v ≤ 2,0 · 10⁶ m/s < 0,01 c),
// gravity left out (mg is about 10⁻¹² of qvB). The whole path is computed when a control changes; "Laukaise" shows
// the particle travelling along it in slowed time (1,0 · 10⁻⁷ s of physical time per second at normal speed).
// Results that emerge from the integration: the hit point d on the detector (the left wall, measured from the slit),
// the deflection y at the right wall, the speed at the end. The model radius r = mv/(qB) is in simState only.
// The chamber is drawn to scale (760 px per metre, grid square 5 cm). Every canvas text goes through lab(), which
// pushes its box to simState.labels; the arrow labels are placed where they overlap nothing. p5.js instance mode.
new p5((p) => {
  const E0 = 1.602e-19;
  const PART = {                                                    // masses (kg) and charges (C) as the lesson gives them
    protoni: { m: 1.673e-27, q: E0, r: 7 }, deuteroni: { m: 3.344e-27, q: E0, r: 8 },
    alfa: { m: 6.645e-27, q: 2 * E0, r: 9 }, vetyioni: { m: 1.674e-27, q: -E0, r: 7 },
  };
  const S = 760, LEN = 0.68, HGT = 340 / 760;                      // px per metre; chamber 0,68 m × 0,447 m
  const X0 = 60, X1 = X0 + LEN * S, Y0 = 40, Y1 = 380, MID = 210, CELL = 0.05 * S;
  const SLOW = 1.0e-7;                                              // physical seconds per display second at normal speed
  const INK = [31, 41, 51], MUTED = [107, 116, 128], RED = [201, 42, 42], BLUE = [25, 113, 194], GREEN = [43, 138, 62];
  const BROWN = [138, 95, 34], RULEC = [201, 194, 178];
  let btn, selP, slV, slB, selDir, slE, selSpeed, readout, lV, lB, lE;
  let labels = [], sig = '', path = null, tShow = 0, running = false, done = false;

  const model = () => {
    const key = selP.value(), P = PART[key] || PART.protoni, v = Number(slV.value()), B = Number(slB.value());
    const dir = selDir.value() === 'sisaan' ? -1 : 1, E = Number(slE.value());
    const vMs = v * 1e6, Fm = Math.abs(P.q) * vMs * B, Fs = Math.abs(P.q) * E * 1e3;
    return { key, P, v, vMs, B, dir, E, Fm, Fs, r: B > 0 ? P.m * vMs / (Math.abs(P.q) * B) : null };
  };

  // the path: Boris steps of about 0,5 mm until the particle leaves the field region
  function compute(m) {
    const qm = m.P.q / m.P.m, Bz = m.dir * m.B, Ey = m.E * 1e3, dt = 0.0005 / m.vMs, h = dt / 2;
    let x = 0, y = 0, vx = m.vMs, vy = 0, t = 0;
    const pts = [[0, 0, 0, vx, vy]];
    let out = { tulos: 'ulos', d: null, puoli: 0, y: null, seina: 0 };
    for (let i = 0; i < 40000; i++) {
      vy += qm * Ey * h;
      const tt = qm * Bz * h, s = 2 * tt / (1 + tt * tt);
      const px = vx + vy * tt, py = vy - vx * tt;
      vx += py * s; vy -= px * s;
      vy += qm * Ey * h;
      const nx = x + vx * dt, ny = y + vy * dt; t += dt;
      if (nx <= 0 && i > 4) {                                       // back on the left wall: the detector
        const f = x / (x - nx), yh = y + f * (ny - y);
        pts.push([0, yh, t - dt + f * dt, vx, vy]); out = { tulos: 'ilmaisin', d: Math.abs(yh) * 100, puoli: yh < 0 ? -1 : 1, y: null, seina: 0 };
        break;
      }
      if (nx >= LEN) {                                              // through the right wall
        const f = (LEN - x) / (nx - x), yh = y + f * (ny - y);
        pts.push([LEN, yh, t - dt + f * dt, vx, vy]); out = { tulos: 'ulos', d: null, puoli: 0, y: Math.abs(yh) < 5e-6 ? 0 : yh * 100, seina: 0 };
        break;
      }
      if (Math.abs(ny) >= HGT / 2) {                                // on the top or the bottom wall (a plate when E > 0)
        const yw = Math.sign(ny) * HGT / 2, f = (yw - y) / (ny - y);
        pts.push([x + f * (nx - x), yw, t - dt + f * dt, vx, vy]); out = { tulos: 'seina', d: null, puoli: 0, y: null, seina: Math.sign(ny) };
        break;
      }
      x = nx; y = ny;
      if (i % 2 === 0) pts.push([x, y, t, vx, vy]);
    }
    const last = pts[pts.length - 1];
    return { pts, T: last[2], vEnd: Math.hypot(last[3], last[4]), ...out };
  }

  const restart = () => { tShow = 0; running = false; done = false; };
  // the path of the current settings: recomputed (and the particle sent back to the slit) when a control has changed
  const sync = () => {
    const m = model(), s = [m.key, m.v, m.B, m.dir, m.E].join('|');
    if (s !== sig) { sig = s; path = compute(m); restart(); }
    return m;
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('laukaise')).parent(controls);
    btn.elt.addEventListener('click', () => { sync(); tShow = 0; done = false; running = true; });
    const lp = p.createElement('label').parent(controls); p.createSpan(__('hiukkanen')).parent(lp); selP = p.createSelect().parent(lp);
    for (const k of ['protoni', 'deuteroni', 'alfa', 'vetyioni']) selP.option(__(k), k);
    selP.selected('protoni');
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(0.5, 2.0, 1.0, 0.1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lB = p.createSpan('').parent(l2); slB = p.createSlider(0, 0.40, 0.20, 0.01).parent(l2);
    const ld = p.createElement('label').parent(controls); p.createSpan(__('suunta')).parent(ld); selDir = p.createSelect().parent(ld);
    selDir.option(__('ulos'), 'ulos'); selDir.option(__('sisaan'), 'sisaan'); selDir.selected('ulos');
    const l3 = p.createElement('label').parent(controls); lE = p.createSpan('').parent(l3); slE = p.createSlider(0, 300, 0, 5).parent(l3);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { hiukkanen: { input: selP.elt, unit: '' }, v: { input: slV.elt, unit: '· 10⁶ m/s' }, B: { input: slB.elt, unit: 'T' },
                suunta: { input: selDir.elt, unit: '' }, E: { input: slE.elt, unit: 'kV/m' } },
      reset: () => { selP.selected('protoni'); slV.value(1.0); slB.value(0.20); selDir.selected('ulos'); slE.value(0); sig = ''; restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const m = sync();
    if (running) {
      tShow += Math.min(p.deltaTime, 100) / 1000 * SLOW * (Number(selSpeed.value()) || 1);
      if (tShow >= path.T) { tShow = path.T; running = false; done = true; }
    }
    const cur = at(tShow), vNow = Math.hypot(cur[3], cur[4]);
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.round(13 * k), U = Math.max(1, 0.75 * k);
    lV.html(__('vauhti', { v: tx(m.v, 1) })); lB.html(__('kentta', { B: tx(m.B, 2) })); lE.html(__('sahko', { E: tx(m.E, 0) }));
    let tila;
    if (!done) tila = running ? __('matkalla') : __('odota');
    else if (path.tulos === 'ilmaisin') tila = __('osuma', { d: tx(path.d, 1), puoli: path.puoli < 0 ? __('alapuolella') : __('ylapuolella') });
    else if (path.tulos === 'ulos') tila = __('poistuu', { y: tx(path.y, 1) });
    else tila = path.seina > 0 ? __('ylareuna') : __('alareuna');
    readout.html(__('lukemat', { nimi: __(m.key), q: m.P.q > 0 ? (m.P.q > 1.5 * E0 ? '+2e' : '+e') : '-e', m: sci(m.P.m, 3),
                                 vn: sci(vNow, 2), Fm: sci(m.Fm, 2), Fs: sci(m.Fs, 2), tila: tila }));
    labels = [];
    p.background(250);
    chamber(m, fh, U, k);
    particle(m, cur, fh, U);
    window.simState = { hiukkanen: m.key, q: m.P.q, m: m.P.m, v: m.v, vMs: m.vMs, B: m.B, suunta: m.dir > 0 ? 'ulos' : 'sisaan', E: m.E,
      Fm: m.Fm, Fs: m.Fs, Fm14: round(m.Fm * 1e14, 3), Fs14: round(m.Fs * 1e14, 3), r: m.r,
      tulos: path.tulos, d: path.d === null ? null : round(path.d, 2), poikkeama: path.y === null ? null : round(path.y, 2), puoli: path.puoli,
      vLoppu: round(path.vEnd / 1e6, 3), vNyt: vNow, x: cur[0], y: cur[1], running, valmis: done, labels };
  };

  // the state on the path at the physical time t (linear between stored points)
  function at(t) {
    const P = path.pts; let lo = 0, hi = P.length - 1;
    if (t <= 0) return P[0]; if (t >= P[hi][2]) return P[hi];
    while (hi - lo > 1) { const mid = (lo + hi) >> 1; if (P[mid][2] <= t) lo = mid; else hi = mid; }
    const a = P[lo], b = P[hi], f = (t - a[2]) / (b[2] - a[2] || 1);
    return a.map((v, i) => v + f * (b[i] - v));
  }
  const SX = (x) => X0 + x * S, SY = (y) => MID - y * S;

  function chamber(m, fh, U, k) {
    // glass chamber with the 5 cm grid
    grect(X0, Y0, X1 - X0, Y1 - Y0, [[245, 249, 252], [226, 236, 243]], 6);
    p.stroke(214, 226, 234); p.strokeWeight(1);
    for (let x = X0 + CELL; x < X1 - 1; x += CELL) p.line(x, Y0, x, Y1);
    for (let y = MID - CELL; y > Y0; y -= CELL) p.line(X0, y, X1, y);
    for (let y = MID + CELL; y < Y1; y += CELL) p.line(X0, y, X1, y);
    // electric field: plates and upward field lines
    if (m.E > 0) {
      p.stroke(...BROWN); p.strokeWeight(1.5 * U);
      for (let x = X0 + CELL; x < X1 - 4; x += CELL) {
        p.line(x, Y1 - 10, x, Y0 + 10);
        for (const yc of [MID + 2 * CELL, MID - 2 * CELL]) { p.noStroke(); p.fill(...BROWN); p.triangle(x, yc - 7 * U, x - 4.5 * U, yc + 4 * U, x + 4.5 * U, yc + 4 * U); p.stroke(...BROWN); }
      }
      p.noStroke(); p.fill(138, 150, 163); p.rect(X0 + 4, Y0, X1 - X0 - 8, 7); p.rect(X0 + 4, Y1 - 7, X1 - X0 - 8, 7);
      lab('$-$', X1 + 11, Y0 + 4 + fh * 0.36, 'c', fh, INK);
      lab('$+$', X1 + 11, Y1 - 4 + fh * 0.36, 'c', fh, INK);
    }
    // magnetic field marks: • out of the page, × into it, one per grid square
    if (m.B > 0) {
      p.stroke(...GREEN); p.strokeWeight(1.8 * U);
      for (let x = X0 + CELL / 2; x < X1 - 8; x += CELL) for (let j = 0; j < 4; j++) for (const sg of [-1, 1]) {
        const y = MID + sg * (j + 0.5) * CELL, a = 5 * U;
        if (m.dir < 0) { p.line(x - a, y - a, x + a, y + a); p.line(x - a, y + a, x + a, y - a); }
        else { p.noFill(); p.circle(x, y, 13 * U); p.noStroke(); p.fill(...GREEN); p.circle(x, y, 4.5 * U); p.stroke(...GREEN); }
      }
    }
    p.noFill(); p.stroke(...INK); p.strokeWeight(2.5); p.rect(X0, Y0, X1 - X0, Y1 - Y0, 6);
    // the detector on the left wall: ticks every centimetre from the slit, numbers every 5 cm (10 cm on a phone)
    p.noStroke(); p.fill(...MUTED); p.rect(X0 - 4, Y0 + 2, 6, MID - 9 - Y0); p.rect(X0 - 4, MID + 7, 6, Y1 - 2 - MID - 7);
    p.stroke(...INK); p.strokeWeight(1.2);
    const every = k > 1.5 ? 10 : 5;
    for (let c = 1; c <= 22; c++) for (const sg of [-1, 1]) {
      const y = MID + sg * c * 0.01 * S, len = c % 5 === 0 ? 9 : 5;
      p.line(X0 - 4 - len, y, X0 - 4, y);
      if (c % every === 0) lab(`$${c}$`, X0 - 16, y + fh * 0.36, 'r', fh, MUTED);
    }
    lab('$d\\ (\\text{cm})$', 6, 4 + 0.8 * fh, 'l', fh, INK);
    // the ion source and its slit
    grect(10, MID - 11, X0 - 18, 22, [[196, 204, 212], [138, 150, 163]], 4);
    p.noFill(); p.stroke(...INK); p.strokeWeight(1.5); p.rect(10, MID - 11, X0 - 18, 22, 4);
    p.noStroke(); p.fill(...INK); p.rect(X0 - 8, MID - 3, 10, 6);
  }

  function particle(m, cur, fh, U) {
    // the track so far
    const P = path.pts; p.noFill(); p.stroke(...INK); p.strokeWeight(2); p.drawingContext.setLineDash([5, 4]);
    p.beginShape(); for (const q of P) { if (q[2] > tShow) break; p.vertex(SX(q[0]), SY(q[1])); } p.vertex(SX(cur[0]), SY(cur[1])); p.endShape();
    p.drawingContext.setLineDash([]);
    const x = SX(cur[0]), y = SY(cur[1]), vx = cur[3], vy = cur[4], sp = Math.hypot(vx, vy) || 1;
    if (!done) {
      // forces on the particle now: magnetic q v × B and electric qE, the longer one 56 px
      const q = m.P.q, Bz = m.dir * m.B;
      const fm = [q * vy * Bz, -q * vx * Bz], fs = [0, q * m.E * 1e3];
      const nm = Math.hypot(...fm), ns = Math.hypot(...fs), big = Math.max(nm, ns);
      const tips = [];
      const v1 = Math.min(120, 34 * sp / 1e6);
      tips.push(['$\\overline{v}$', arrow(x, y, vx / sp, -vy / sp, v1, BLUE, U), BLUE, [vx / sp, -vy / sp]]);
      if (nm > 0) { const L = 56 * nm / big; tips.push(['$\\overline{F}_\\text{m}$', arrow(x, y, fm[0] / nm, -fm[1] / nm, L, RED, U), RED, [fm[0] / nm, -fm[1] / nm]]); }
      if (ns > 0) { const L = 56 * ns / big; tips.push(['$\\overline{F}_\\text{s}$', arrow(x, y, fs[0] / ns, -fs[1] / ns, L, RED, U), RED, [fs[0] / ns, -fs[1] / ns]]); }
      for (const [s, tip, col, d] of tips) place(s, tip, d, fh, col);
    }
    // the particle: a sphere with its sign drawn as strokes
    const R = m.P.r * U;
    p.stroke(...INK); p.strokeWeight(1.8); p.fill(...(m.P.q > 0 ? [242, 166, 156] : [208, 230, 251])); p.circle(x, y, 2 * R);
    p.strokeWeight(2); p.line(x - R * 0.5, y, x + R * 0.5, y); if (m.P.q > 0) p.line(x, y - R * 0.5, x, y + R * 0.5);
  }

  function arrow(x, y, ux, uy, L, col, U) {
    if (L < 2) return [x, y];
    const hh = Math.min(12 * U, L * 0.6), bx = x + ux * (L - hh), by = y + uy * (L - hh), ex = x + ux * L, ey = y + uy * L;
    p.stroke(...col); p.strokeWeight(3 * U); p.line(x, y, bx, by);
    p.noStroke(); p.fill(...col); p.triangle(ex, ey, bx - uy * hh * 0.45, by + ux * hh * 0.45, bx + uy * hh * 0.45, by - ux * hh * 0.45);
    return [ex, ey];
  }

  // an arrow's label beyond its tip, or beside it, wherever it stays in the chamber and overlaps no other label
  function place(s, tip, d, fh, col) {
    p.textSize(fh); const w = p.textWidth(s), g = 5 + fh * 0.3, n = [-d[1], d[0]];
    const ext = (u) => g + Math.abs(u[0]) * w / 2 + Math.abs(u[1]) * fh * 0.55;
    const cand = [];
    for (const k of [1, 1.8]) for (const u of [d, [-n[0], -n[1]], n, [-d[0], -d[1]]])
      cand.push([tip[0] + u[0] * k * ext(u), tip[1] + u[1] * k * ext(u)]);
    for (const [cx, cy] of cand) {
      const bx0 = cx - w / 2 - 2, bx1 = cx + w / 2 + 2, by0 = cy - fh * 0.8, by1 = cy + fh * 0.6;
      if (bx0 < X0 + 2 || bx1 > X1 - 2 || by0 < Y0 + 2 || by1 > Y1 - 2) continue;
      if (labels.some((b) => bx0 < b.x1 && b.x0 < bx1 && by0 < b.y1 && b.y0 < by1)) continue;
      lab(s, cx, cy + fh * 0.36, 'c', fh, col); return;
    }
  }

  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INK)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.8 * size, x1: x0 + w, y1: y + 0.3 * size });
  }
  function grect(x, y, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.restore();
  }
  const round = (x, d) => Math.round(x * Math.pow(10, d)) / Math.pow(10, d);
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  // x in LaTeX as a · 10^n with d decimals in a
  const sci = (x, d) => {
    if (!x) return '0';
    let n = Math.floor(Math.log10(Math.abs(x))), a = x / Math.pow(10, n);
    if (Math.abs(Number(a.toFixed(d))) >= 10) { n += 1; a /= 10; }
    return `${tx(a, d)} \\cdot 10^{${n}}`;
  };
});
