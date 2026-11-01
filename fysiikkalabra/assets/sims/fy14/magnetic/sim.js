// FY14 Charged particles and magnetic confinement. One charged particle (proton, deuteron, electron, alpha particle;
// CODATA 2022 masses) in a static magnetic field; the physics is in model.js (window.FY14Magnetic), solved exactly in
// the uniform field and with the guiding-centre model (μ = m v⊥²/2B conserved) in the mirror.
//   View "Uniform field": B perpendicular to the page (⊗ into, ⊙ out of it), the velocity in the page, so the particle
//   moves on a circle of radius r = m v / (|q| B) with the period T = 2π m / (|q| B). The blue arrow is the velocity
//   (tangent), the red one the magnetic force q v × B (towards the centre). The checkbox adds an electric field E
//   upward in the page: the circle's centre then drifts at E/B, perpendicular to E and B, the same way for both signs.
//   View "Field along the particle": side view, B along +x. v∥ = v cos θ carries the particle along the field line,
//   v⊥ = v sin θ around it: a helix (its far half drawn fainter). In a straight field every particle with v∥ ≠ 0 leaves
//   through an end; with the magnetic mirror (B up to 4 B0 at the ends, field lines converging) the particle is
//   reflected if sin²θ ≥ B0/Bmax and escapes otherwise (the loss cone, θ < 30°).
// Scales: real gyroradii range from micrometres (electron) to metres (proton at 0.1 T), so the drawing is to scale with
// a grid square chosen from 1, 2, 5 · 10ⁿ m so that the orbit fits; it is said on the canvas. Time runs slowed down by a
// stated factor (per particle, so that one turn in 1 T lasts about 1.5 s; the playback select halves or doubles it).
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const M = window.FY14Magnetic, E_FIELD = 2.0e5;                                // V/m, the checkbox's electric field
  const W = 600, H = 400, G = 40, CX = 300, CY = 212, CY2 = 214, HALF = 250;     // grid square (px), view centres, mirror half-length (px)
  const RED = [201, 42, 42], BLUE = [25, 113, 194], GREEN = [43, 138, 62], INK = [31, 41, 51], MUTED = [92, 101, 112];
  const PURPLE = [156, 54, 181], ION = [194, 37, 92], ELEC = [52, 58, 64];
  const DEF = { view: 'uniform', particle: 'p', v: 2e6, B: 1, dir: 'in', E: false, pitch: 45, mirror: true };
  let selView, selP, slV, slB, selDir, cbE, slPitch, cbMirror, selSpeed, btn, readout;
  let lV, lB, lPitch, rowDir, rowE, rowPitch, rowMirror;
  let running = true, labels = [], sig = '', st = null, trail = [], tShow = 0, scale1 = null, scale2 = null;

  const nice = [];
  for (let n = -9; n <= 1; n++) for (const a of [1, 2, 5]) nice.push(a * Math.pow(10, n));
  // grid square length (m): kept while the orbit's radius stays between lo and hi px, otherwise the nearest to target
  const pickScale = (rM, lo, hi, prev) => {
    if (prev && rM / prev * G >= lo && rM / prev * G <= hi) return prev;
    const target = Math.sqrt(lo * hi);
    return nice.reduce((b, L) => (Math.abs(Math.log(rM / L * G / target)) < Math.abs(Math.log(rM / b * G / target)) ? L : b), nice[0]);
  };
  const base = (P) => { const x = 1.5 / M.period(P.m, P.q, 1), n = Math.floor(Math.log10(x)), a = x / Math.pow(10, n);
    return (a < 1.5 ? 1 : a < 3.5 ? 2 : 5) * Math.pow(10, n); };

  const read = () => {
    const key = selP.value(), P = M.PARTICLES[key], view = selView.value() === 'along' ? 'along' : 'uniform';
    const v = Number(slV.value()), B = Number(slB.value()), dir = selDir.value() === 'out' ? 1 : -1;
    const Eon = view === 'uniform' && cbE.checked(), pitch = view === 'along' ? Number(slPitch.value()) : 90;
    const mirror = view === 'along' && cbMirror.checked(), speed = Number(selSpeed.value()) || 1;
    const vperp = v * Math.sin(pitch * Math.PI / 180), slow = base(P) / speed;
    return { key, P, m: P.m, q: P.q, view, v, B, dir, Eon, E: Eon ? E_FIELD : 0, pitch, mirror, speed, slow, vperp,
             r: M.radius(P.m, P.q, vperp, B), T: M.period(P.m, P.q, B), f: M.frequency(P.m, P.q, B), drift: Eon ? M.driftSpeed(E_FIELD, B) : 0 };
  };

  const restart = (s) => {
    trail = []; tShow = 0;
    if (s.view === 'uniform') {
      const g = M.uniform(s.m, s.q, s.v, s.B, s.dir, s.E, 0);
      scale1 = pickScale(Math.max(M.radius(s.m, s.q, s.v, s.B), g.rg), 28, 150, scale1);
      const k = G / scale1;                                                     // px per metre
      // place the start so that the first circle's centre is in the middle of the view
      const ox = CX - (g.cx) * k, oy = CY + g.cy * k;
      st = { view: 'uniform', t: 0, k, ox, oy };
    } else {
      scale2 = pickScale(M.radius(s.m, s.q, s.v, s.B), 14, 62, scale2);
      const k = G / scale2;
      st = { view: 'along', k, a: M.createAlong(s.m, s.q, s.v, s.pitch, s.B, HALF / k, s.mirror) };
    }
  };

  p.setup = () => {
    p.createCanvas(W, H).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('tauko')).parent(controls); btn.elt.addEventListener('click', () => { running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', () => { restart(read()); running = true; });
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nakyma')).parent(lv); selView = p.createSelect().parent(lv);
    selView.option(__('n_tasainen'), 'uniform'); selView.option(__('n_pitkin'), 'along');
    const lp = p.createElement('label').parent(controls); p.createSpan(__('hiukkanen')).parent(lp); selP = p.createSelect().parent(lp);
    for (const k of ['p', 'd', 'e', 'a']) selP.option(__('h_' + k), k);
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(1e5, 1e7, DEF.v, 1e5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lB = p.createSpan('').parent(l2); slB = p.createSlider(0.1, 5, DEF.B, 0.1).parent(l2);
    rowDir = p.createElement('label').parent(controls); p.createSpan(__('suunta')).parent(rowDir); selDir = p.createSelect().parent(rowDir);
    selDir.option(__('sisaan'), 'in'); selDir.option(__('ulos'), 'out');
    rowE = p.createElement('label').parent(controls); cbE = p.createCheckbox('', false).parent(rowE); p.createSpan(__('sahkokentta')).parent(rowE);
    rowPitch = p.createElement('label').parent(controls); lPitch = p.createSpan('').parent(rowPitch); slPitch = p.createSlider(0, 90, DEF.pitch, 5).parent(rowPitch);
    rowMirror = p.createElement('label').parent(controls); cbMirror = p.createCheckbox('', DEF.mirror).parent(rowMirror); p.createSpan(__('peili')).parent(rowMirror);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart(read());
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { B: { input: slB.elt, unit: 'T' }, v: { input: slV.elt, unit: 'm/s' }, particle: { input: selP.elt, unit: '' },
                view: { input: selView.elt, unit: '' }, pitch: { input: slPitch.elt, unit: '°' } },
      reset: () => { selView.selected(DEF.view); selP.selected(DEF.particle); slV.value(DEF.v); slB.value(DEF.B); selDir.selected(DEF.dir);
                     cbE.checked(DEF.E); slPitch.value(DEF.pitch); cbMirror.checked(DEF.mirror); selSpeed.selected('1');
                     scale1 = scale2 = null; running = true; sig = ''; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = read();
    const ns = [s.view, s.key, s.v, s.B, s.dir, s.Eon, s.pitch, s.mirror].join('|');
    if (ns !== sig) { sig = ns; restart(s); }
    const dt = running ? Math.min(p.deltaTime || 16, 60) / 1000 : 0;          // shown seconds this frame
    // controls of the other view are hidden (their values stay for the adapter)
    rowDir.style('display', s.view === 'uniform' ? '' : 'none'); rowE.style('display', s.view === 'uniform' ? '' : 'none');
    rowPitch.style('display', s.view === 'along' ? '' : 'none'); rowMirror.style('display', s.view === 'along' ? '' : 'none');
    lV.html(__('vauhti', { v: sci(s.v, 2) })); lB.html(__(s.view === 'along' ? 'kentta0' : 'kentta', { B: tx(s.B, 1) }));
    lPitch.html(__('kulma', { a: tx(Number(slPitch.value()), 0) }));
    const bt = running ? __('tauko') : __('jatka'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(14 * k);
    labels = [];
    let escaped = false, trapped = false, extra = {};
    if (s.view === 'uniform') extra = drawUniform(s, dt, fh);
    else { extra = drawAlong(s, dt, fh); escaped = st.a.escaped; trapped = s.mirror && M.mirrorTrapped(s.pitch, M.RM); }

    // readout under the controls
    const head = __(s.view === 'along' ? 'lukemat2' : 'lukemat', { r: si(s.r, 'm'), T: si(s.T, 's'), f: si(s.f, 'Hz') });
    const mline = __('lukemat_m', { m: sci(s.m, 4), q: (s.q > 0 ? '+' : '-') + sci(Math.abs(s.q), 4), v: sci(s.v, 3) });
    let more = '';
    if (s.view === 'uniform' && s.Eon) more = '<br>' + __('lukemat_E', { E: sci(s.E, 2) + '\\,\\text{V/m}', vd: sci(s.drift, 3) + '\\,\\text{m/s}' });
    if (s.view === 'along') {
      more = '<br>' + __('lukemat_v', { vpar: sci(s.v * Math.cos(s.pitch * Math.PI / 180), 3) + '\\,\\text{m/s}', vperp: sci(s.vperp, 3) + '\\,\\text{m/s}' });
      if (s.mirror) {
        const s2 = Math.sin(s.pitch * Math.PI / 180) ** 2;
        more += '<br>' + __('lukemat_peili', { ratio: tx(1 / M.RM, 2), s2: tx(s2, 2) });   // no verdict: students watch the orbit
      } else more += '<br>' + __('lukemat_suora');
    }
    readout.html(head + '<br>' + mline + more);
    window.simState = { view: s.view, particle: s.key, q: s.q, m: s.m, v: s.v, B: s.B, r: s.r, rmm: s.r * 1e3, T: s.T, Tns: s.T * 1e9, f: s.f,
      pitch: s.pitch, mirror: s.mirror, E: s.E, drift: s.drift, escaped, trapped, slowdown: s.slow,
      grid: s.view === 'uniform' ? scale1 : scale2, running, ...extra, labels };
  };

  // ---- view 1: uniform field perpendicular to the page ------------------------------------------------------------
  function drawUniform(s, dt, fh) {
    const k = st.k, ctx = p.drawingContext;
    const at = (t) => { const g = M.uniform(s.m, s.q, s.v, s.B, s.dir, s.E, t); return { g, x: st.ox + g.x * k, y: st.oy - g.y * k }; };
    // advance real time; trail points at most 0.12 rad of gyration apart
    const dReal = dt / s.slow, W0 = Math.abs(M.uniform(s.m, s.q, s.v, s.B, s.dir, s.E, 0).W);
    const n = Math.min(400, Math.max(1, Math.ceil(W0 * dReal / 0.12)));
    for (let i = 1; i <= n; i++) { const t = st.t + dReal * i / n, q = at(t); trail.push({ x: q.x, y: q.y, t: tShow + dt * i / n }); }
    st.t += dReal; tShow += dt;
    let cur = at(st.t);
    // the drifting centre left the view: start again on the other side
    const gx = st.ox + cur.g.cx * k, rgp = cur.g.rg * k;
    if (gx - rgp > W + 10 || gx + rgp < -10) { st.ox += (gx > W ? -1 : 1) * (W + 2 * rgp + 20); trail = []; cur = at(st.t); }
    const Tshow = M.period(s.m, s.q, s.B) * s.slow, keep = s.Eon ? 2.5 * Tshow : 0.92 * Tshow;
    trail = trail.filter((q) => tShow - q.t <= keep);

    chamber();
    ctx.save(); viewport(); ctx.clip();
    grid(CX, CY);
    const sym = s.dir;                                                          // field symbols in the middle of each square
    for (let x = CX - 7 * G - G / 2; x < W; x += G) for (let y = CY - 5 * G - G / 2; y < H; y += G) fieldSymbol(x, y, sym, 6);
    if (s.Eon) for (let x = CX - 6 * G; x < W; x += 3 * G) arrow(x, 384, x, 22, PURPLE, 1.6, false, 8, 120);
    const cx = st.ox + cur.g.cx * k, cy = st.oy - cur.g.cy * k;
    if (!s.Eon) {                                                               // the whole orbit, faint and dashed
      p.noFill(); p.stroke(...pcol(s), 70); p.strokeWeight(1.2);
      const R = cur.g.rg * k, nd = Math.max(24, Math.round(R / 3));
      for (let i = 0; i < nd; i += 2) p.arc(cx, cy, 2 * R, 2 * R, i * 2 * Math.PI / nd, (i + 1) * 2 * Math.PI / nd);
    }
    // trail, fading with age
    p.noFill();
    for (let i = 1; i < trail.length; i++) {
      const a = 1 - (tShow - trail[i].t) / keep; if (a <= 0) continue;
      p.stroke(...pcol(s), 255 * a * a); p.strokeWeight(1 + 2.2 * a); p.line(trail[i - 1].x, trail[i - 1].y, trail[i].x, trail[i].y);
    }
    // radius to the centre of the circle (no drift only: with E the path is not a circle)
    if (!s.Eon) { p.stroke(...MUTED, 150); p.strokeWeight(1.2); dashed(cx, cy, cur.x, cur.y, 5, 4); p.noStroke(); p.fill(...MUTED); p.circle(cx, cy, 5); }
    // arrows: velocity (tangent) and magnetic force q v × B, lengths in proportion to their magnitudes
    const vx = cur.g.vx, vy = cur.g.vy, vm = Math.hypot(vx, vy) || 1, Lv = clamp(58 * vm / s.v, 12, 120);
    const Bz = s.dir * s.B, fx = s.q * vy * Bz, fy = -s.q * vx * Bz, fm = Math.hypot(fx, fy) || 1, Lf = clamp(48 * vm / s.v, 10, 110);
    const ux = vx / vm, uy = -vy / vm, gx2 = fx / fm, gy2 = -fy / fm;
    arrow(cur.x, cur.y, cur.x + ux * Lv, cur.y + uy * Lv, BLUE, 3.2, false, 11);
    arrow(cur.x, cur.y, cur.x + gx2 * Lf, cur.y + gy2 * Lf, RED, 3.2, false, 11);
    let Le = 0;
    if (s.Eon) { Le = clamp(48 * s.E / (s.v * s.B), 8, 110); arrow(cur.x, cur.y, cur.x, cur.y - Math.sign(s.q) * Le, RED, 2.6, true, 10); }
    particle(cur.x, cur.y, s, 1);
    ctx.restore();

    // labels: fixed panels first, then the moving ones placed where they fit
    panel([[__('c_ruutu', { L: siNice(scale1) })], [__('c_hidastus', { k: sci(s.slow, 2, true) })]], 18, 'l', fh);
    panel([[__(s.dir < 0 ? 'c_sisaan' : 'c_ulos'), GREEN], [__('c_B', { B: tx(s.B, 1) })]], W - 18, 'r', fh);
    panelBottom([[__('c_nimi_' + s.key), pcol(s)]], 18, 'l', fh);
    const br = s.Eon ? [[__('c_E', { E: sci(s.E, 2) + '\\,\\text{V/m}' }), PURPLE], [__('c_vd', { vd: sci(s.drift, 3) + '\\,\\text{m/s}' })]]
      : [[__('c_r', { r: si(s.r, 'm') })]];
    panelBottom(br, W - 18, 'r', fh);
    tag('$\\overline{v}$', cur.x + ux * Lv, cur.y + uy * Lv, BLUE, fh);
    tag(s.Eon ? '$\\overline{F}_{B}$' : '$\\overline{F}$', cur.x + gx2 * Lf, cur.y + gy2 * Lf, RED, fh);
    if (s.Eon) tag('$\\overline{F}_{E}$', cur.x, cur.y - Math.sign(s.q) * Le, RED, fh);
    if (!s.Eon) tag('$r$', (cx + cur.x) / 2, (cy + cur.y) / 2, MUTED, fh);
    return { x: (cur.x - CX) / k, y: (CY - cur.y) / k };
  }

  // ---- view 2: side view, B along x, optional magnetic mirror --------------------------------------------------------
  function drawAlong(s, dt, fh) {
    const a = st.a, k = st.k, ctx = p.drawingContext;
    const dReal = dt / s.slow;
    if (dReal > 0 && !a.escaped) {
      const wmax = M.omega(s.m, s.q, s.B * (s.mirror ? M.RM : 1)), h = Math.min(0.1 / wmax, 0.004 * a.L / s.v);
      const n = Math.min(60, Math.max(1, Math.ceil(dReal / (8 * h))));          // trail points per frame; each one exact substeps
      for (let i = 0; i < n; i++) {
        M.stepAlong(a, dReal / n, h);
        const q = M.alongState(a); trail.push({ x: CX + a.x * k, y: CY2 - q.r * Math.cos(a.phi) * k, z: Math.sin(a.phi), t: tShow + dt * (i + 1) / n });
        if (a.escaped) break;
      }
    }
    tShow += dt;
    const keep = 3.2;
    trail = trail.filter((q) => tShow - q.t <= keep).slice(-1800);

    chamber();
    ctx.save(); viewport(); ctx.clip();
    // the vacuum tube and its grid
    p.noStroke(); p.fill(244, 247, 251, 200); p.rect(18, CY2 - 112, W - 36, 224, 16);
    ctx.save(); p.drawingContext.beginPath(); p.drawingContext.rect(18, CY2 - 112, W - 36, 224); ctx.clip(); grid(CX, CY2); ctx.restore();
    // coils: evenly spaced, and with the mirror strong ones at the ends
    p.noStroke();
    for (let x = 85; x <= 515; x += 43) coil(x, 12, 14);
    if (s.mirror) { coil(CX - HALF, 26, 26); coil(CX + HALF, 26, 26); }
    // field lines: B/B0 = g(x), so a line that starts h px from the axis runs at h/√g (the flux in the tube is conserved)
    for (const h0 of [-104, -70, -36, 0, 36, 70, 104]) {
      p.noFill(); p.stroke(...GREEN, h0 === 0 ? 200 : 140); p.strokeWeight(h0 === 0 ? 1.8 : 1.3); p.beginShape();
      for (let x = 18; x <= W - 18; x += 6) p.vertex(x, CY2 - h0 / Math.sqrt(M.profile((x - CX) / HALF, s.mirror ? M.RM : 1).g));
      p.endShape();
      for (const xa of [150, 450]) {
        const g = M.profile((xa - CX) / HALF, s.mirror ? M.RM : 1), g2 = M.profile((xa + 4 - CX) / HALF, s.mirror ? M.RM : 1);
        const y1 = CY2 - h0 / Math.sqrt(g.g), y2 = CY2 - h0 / Math.sqrt(g2.g);
        head(xa + 4, y2, Math.atan2(y2 - y1, 4), GREEN, 7);
      }
    }
    // the helix: the half behind the field line (z < 0) fainter and thinner
    p.noFill();
    for (let i = 1; i < trail.length; i++) {
      const q = trail[i], al = 1 - (tShow - q.t) / keep; if (al <= 0) continue;
      const d = 0.5 + 0.5 * q.z;
      p.stroke(...pcol(s), 255 * al * (0.3 + 0.7 * d)); p.strokeWeight(0.8 + 2.4 * d * al); p.line(trail[i - 1].x, trail[i - 1].y, q.x, q.y);
    }
    const q = M.alongState(a), x = CX + a.x * k, y = CY2 - q.r * Math.cos(a.phi) * k, z = Math.sin(a.phi);
    let vtip = null, ftip = null;
    if (!a.escaped) {
      // velocity (v∥, projected v⊥) and the force: towards the axis, plus the mirror force −μ dB/dx along it
      const sgn = -Math.sign(s.q), vy = -sgn * q.vperp * Math.sin(a.phi);           // ẏ of y = r cos φ with φ̇ = sgn ω
      const Lv = 58 / s.v; vtip = [x + a.vpar * Lv, y - vy * Lv];
      arrow(x, y, vtip[0], vtip[1], BLUE, 3, false, 10);
      if (q.vperp > 1e-9 * s.v) {
        const ratio = q.Fpar / q.Fperp, L0 = 44 * q.vperp / s.v * Math.sqrt(q.B / s.B);
        ftip = [x + ratio * L0, y + Math.cos(a.phi) * L0];
        if (Math.hypot(ratio * L0, Math.cos(a.phi) * L0) > 3) arrow(x, y, ftip[0], ftip[1], RED, 3, false, 10);
        else ftip = null;
      }
      particle(x, y, s, 0.75 + 0.25 * z);
    }
    ctx.restore();

    panel([[__('c_ruutu', { L: siNice(scale2) })], [__('c_hidastus', { k: sci(s.slow, 2, true) })]], 18, 'l', fh);
    const tr = [[__('c_B0', { B: tx(s.B, 1) }), GREEN]];
    if (s.mirror) tr.push([__('c_Bmax', { B: tx(s.B * M.RM, 1) }), GREEN]);
    panel(tr, W - 18, 'r', fh);
    panelBottom([[__('c_nimi_' + s.key), pcol(s)], [__('c_kulma', { a: tx(s.pitch, 0) })]], 18, 'l', fh);
    const status = a.escaped ? __('c_karkasi') : s.pitch >= 90 ? __('c_paikallaan') : a.refl > 0 ? __('c_heijastui', { n: a.refl }) : '';
    if (status) panelBottom([[status, a.escaped ? [138, 59, 26] : INK]], W - 18, 'r', fh);
    tag('$\\overline{B}$', 470, CY2 - 104 / Math.sqrt(M.profile((470 - CX) / HALF, s.mirror ? M.RM : 1).g) + fh + 2, GREEN, fh);
    if (vtip) tag('$\\overline{v}$', vtip[0], vtip[1], BLUE, fh);
    if (ftip) tag('$\\overline{F}$', ftip[0], ftip[1], RED, fh);
    return { x: a.x, reflections: a.refl, vpar: a.vpar };
  }

  // ---- drawing helpers ----------------------------------------------------------------------------------------------
  function viewport() { const c = p.drawingContext; c.beginPath(); if (c.roundRect) c.roundRect(8, 8, W - 16, H - 16, 18); else c.rect(8, 8, W - 16, H - 16); }
  function chamber() {                                                          // steel flange around a vacuum viewport
    const c = p.drawingContext;
    let g = c.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#c9d1da'); g.addColorStop(1, '#a9b3be');
    c.fillStyle = g; c.fillRect(0, 0, W, H);
    g = c.createRadialGradient(CX, CY, 40, CX, CY, 380); g.addColorStop(0, '#fdfeff'); g.addColorStop(0.7, '#eef2f7'); g.addColorStop(1, '#d8e0e9');
    c.fillStyle = g; viewport(); c.fill();
    c.lineWidth = 2; c.strokeStyle = 'rgba(70,82,96,0.55)'; viewport(); c.stroke();
    p.noStroke(); p.fill(120, 130, 142);
    for (const [x, y] of [[4, 4], [W - 4, 4], [4, H - 4], [W - 4, H - 4]]) p.circle(x, y, 5);
  }
  function grid(x0, y0) {
    p.stroke(120, 140, 165, 46); p.strokeWeight(1);
    for (let x = x0 % G; x < W; x += G) p.line(x, 0, x, H);
    for (let y = y0 % G; y < H; y += G) p.line(0, y, W, y);
  }
  function fieldSymbol(x, y, dir, r) {
    p.stroke(...GREEN, 150); p.strokeWeight(1.3); p.fill(255, 255, 255, 120); p.circle(x, y, 2 * r);
    if (dir > 0) { p.noStroke(); p.fill(...GREEN, 170); p.circle(x, y, 3.2); }
    else { const d = r * 0.62; p.line(x - d, y - d, x + d, y + d); p.line(x - d, y + d, x + d, y - d); }
  }
  function coil(x, w, h) {
    for (const yy of [CY2 - 112 - h, CY2 + 112]) {
      const c = p.drawingContext, g = c.createLinearGradient(x - w / 2, 0, x + w / 2, 0);
      g.addColorStop(0, '#9c5a2a'); g.addColorStop(0.5, '#e0a064'); g.addColorStop(1, '#8a4b20');
      c.fillStyle = g; p.noStroke(); c.beginPath(); c.rect(x - w / 2, yy, w, h); c.fill();
    }
  }
  function particle(x, y, s, sc) {
    const c = p.drawingContext, col = pcol(s), R = 7.5 * sc;
    const g = c.createRadialGradient(x - R * 0.35, y - R * 0.35, 1, x, y, R * 2.2);
    g.addColorStop(0, `rgba(${col.join(',')},0.35)`); g.addColorStop(1, `rgba(${col.join(',')},0)`);
    c.fillStyle = g; c.beginPath(); c.arc(x, y, R * 2.2, 0, 2 * Math.PI); c.fill();
    const g2 = c.createRadialGradient(x - R * 0.35, y - R * 0.4, 0.5, x, y, R);
    g2.addColorStop(0, '#ffffff'); g2.addColorStop(0.35, `rgb(${col.join(',')})`); g2.addColorStop(1, `rgb(${col.map((v) => v * 0.6).join(',')})`);
    c.fillStyle = g2; c.beginPath(); c.arc(x, y, R, 0, 2 * Math.PI); c.fill();
    p.stroke(255); p.strokeWeight(1.6 * sc); const d = R * 0.5;
    p.line(x - d, y, x + d, y); if (s.q > 0) p.line(x, y - d, x, y + d);
  }
  const pcol = (s) => (s.q > 0 ? ION : ELEC);
  function head(x, y, ang, col, sz) {
    p.noStroke(); p.fill(...col); p.push(); p.translate(x, y); p.rotate(ang); p.triangle(0, 0, -sz, -sz * 0.45, -sz, sz * 0.45); p.pop();
  }
  function arrow(x1, y1, x2, y2, col, w, dash, hs, alpha) {
    const L = Math.hypot(x2 - x1, y2 - y1); if (L < 2) return;
    const ang = Math.atan2(y2 - y1, x2 - x1), hx = x2 - Math.cos(ang) * hs * 0.8, hy = y2 - Math.sin(ang) * hs * 0.8;
    p.stroke(...col, alpha || 255); p.strokeWeight(w);
    if (dash) dashed(x1, y1, hx, hy, 6, 4); else p.line(x1, y1, hx, hy);
    head(x2, y2, ang, alpha ? [...col, alpha] : col, hs);
  }
  function dashed(x1, y1, x2, y2, on, off) {
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L;
    for (let d = 0; d < L; d += on + off) { const e = Math.min(L, d + on); p.line(x1 + ux * d, y1 + uy * d, x1 + ux * e, y1 + uy * e); }
  }

  // ---- labels ---------------------------------------------------------------------------------------------------------
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INK)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  // a column of labels on a white card, from the top (panel) or the bottom (panelBottom) of the view
  function card(lines, x, align, fh, yTop) {
    p.textSize(fh);
    const lh = fh * 1.5, w = Math.max(...lines.map((l) => p.textWidth(l[0]))), x0 = align === 'r' ? x - w : x;
    p.stroke(160, 172, 186, 160); p.strokeWeight(1); p.fill(255, 255, 255, 222);
    p.rect(x0 - 7, yTop, w + 14, lines.length * lh + 6, 7);
    lines.forEach((l, i) => lab(l[0], align === 'r' ? x : x, yTop + 3 + lh * (i + 0.72), align, fh, l[1] || INK));
    return { x0: x0 - 7, x1: x0 + w + 7, y1: yTop + lines.length * lh + 6 };
  }
  // top cards: the left one first; a right card that would touch it goes under it (narrow canvases)
  let topLeft = null;
  const panel = (lines, x, align, fh) => {
    if (align !== 'r') { topLeft = card(lines, x, align, fh, 14); return; }
    p.textSize(fh);
    const w = Math.max(...lines.map((l) => p.textWidth(l[0])));
    const clash = topLeft && x - w - 7 < topLeft.x1 + 8;
    card(lines, x, align, fh, clash ? topLeft.y1 + 6 : 14); topLeft = null;
  };
  const panelBottom = (lines, x, align, fh) => card(lines, x, align, fh, H - 14 - 6 - lines.length * fh * 1.5);
  // a label at an arrow tip, at the first offset where it overlaps nothing and stays inside the view
  function tag(s, x, y, col, fh) {
    p.textSize(fh);
    const w = p.textWidth(s), pad = 4;
    for (const [dx, dy] of [[6, -6], [6, fh + 2], [-w - 6, -6], [-w - 6, fh + 2], [-w / 2, -10], [-w / 2, fh + 8]]) {
      const x0 = x + dx, yb = y + dy, b = { x0: x0 - pad, y0: yb - 0.75 * fh - pad, x1: x0 + w + pad, y1: yb + 0.25 * fh + pad };
      if (b.x0 < 12 || b.x1 > W - 12 || b.y0 < 12 || b.y1 > H - 12) continue;
      if (labels.some((l) => l.x0 < b.x1 && b.x0 < l.x1 && l.y0 < b.y1 && b.y0 < l.y1)) continue;
      lab(s, x0, yb, 'l', fh, col); return true;
    }
    return false;
  }

  // ---- numbers --------------------------------------------------------------------------------------------------------
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '.'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  // a · 10^n with sig significant figures; trim drops trailing zeros (for the slow-down factor)
  function sci(x, sig, trim) {
    if (x === 0) return '0';
    let n = Math.floor(Math.log10(Math.abs(x))), a = (x / Math.pow(10, n)).toPrecision(sig);
    if (Math.abs(Number(a)) >= 10) { n += 1; a = (x / Math.pow(10, n)).toPrecision(sig); }
    if (trim) a = String(Number(a));
    a = a.replace('.', DEC);
    return n === 0 ? a : `${a} \\cdot 10^{${n}}`;
  }
  const PRE = { '-12': 'p', '-9': 'n', '-6': '\\mu', '-3': 'm', 0: '', 3: 'k', 6: 'M', 9: 'G' };
  const unit = (pre, u) => (pre === '\\mu' ? `\\mu\\text{${u}}` : `\\text{${pre}${u}}`);
  // a value with an SI prefix and 3 significant figures: 10.4\,\text{mm}
  function si(x, u) {
    let e3 = clamp(Math.floor(Math.log10(Math.abs(x)) / 3) * 3, -12, 9), m = (x / Math.pow(10, e3)).toPrecision(3);
    if (Number(m) >= 1000 && e3 < 9) { e3 += 3; m = (x / Math.pow(10, e3)).toPrecision(3); }
    return `${m.replace('.', DEC)}\\,${unit(PRE[e3], u)}`;
  }
  // a grid length 1, 2, 5 · 10^n m with its prefix and no decimals: 500\,\mu\text{m}
  function siNice(x) {
    const e3 = clamp(Math.floor(Math.log10(x * 1.0001) / 3) * 3, -12, 0);
    return `${Math.round(x / Math.pow(10, e3))}\\,${unit(PRE[e3], 'm')}`;
  }
});
