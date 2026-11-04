// fy7-6 Lenzin laki ja pyörrevirrat: a magnet (or an unmagnetised steel piece of the same size and mass) is dropped
// from rest into a vertical tube 1,00 m long: plastic, aluminium, copper, or copper with a lengthwise slit.
// Model: in a conducting tube the moving magnet induces eddy currents (rings below and above it) whose force opposes
// the motion and is proportional to the speed, F_j = k v; the magnet then approaches the terminal speed vt = m g / k:
// v(t) = vt (1 - e^(-t/τ)), y(t) = vt (t - τ (1 - e^(-t/τ))), τ = vt / g. k is chosen so that vt = 0,15 m/s in copper
// (the order of magnitude of school demonstrations with a strong neodymium magnet); aluminium conducts 0,633 of
// copper (σ 3,77 · 10⁷ vs 5,96 · 10⁷ S/m at 20 °C), so k is 0,633 times as large; the slit cuts the currents that
// circulate round the tube, and the model keeps one tenth of k. Plastic, and the steel piece in any tube: free fall.
// No air resistance, no friction with the wall, end effects ignored. The fall ends when the body has fallen 1,00 m.
// Energies: ΔEp = m g y, Ek = 1/2 m v², Q = ΔEp - Ek (internal energy of the tube). Simulated time advances by
// dt · speed; every value is computed from the simulated time, so the speed select changes nothing but the pace.
// Three panels: the tube (picture, eddy-current rings, forces), the graph y(t) with the last run of each tube, the
// energy bars. On a narrow screen they stack (NOTES §4). Every canvas text goes through lab() (simState.labels).
new p5((p) => {
  const g = 9.81, H = 1.00, M = 0.020;                            // m/s², tube length (m), mass of the body (kg)
  const VT = { kupari: 0.15, alumiini: 0.15 * 5.96e7 / 3.77e7, rako: 1.5 };   // terminal speeds (m/s); plastic: none
  const RED = [201, 42, 42], VIOLET = [112, 72, 232], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [227, 220, 203];
  const NPOLE = [242, 166, 156], SPOLE = [208, 230, 251], HEATC = [232, 89, 12], COLDC = [25, 113, 194];
  const TRACE = { muovi: INKC, alumiini: [138, 150, 163], kupari: [184, 98, 45], rako: [184, 98, 45] };
  const TUBE = { muovi: [[238, 245, 249], [201, 214, 224]], alumiini: [[226, 231, 236], [160, 170, 181]],
                 kupari: [[222, 150, 104], [150, 76, 34]], rako: [[222, 150, 104], [150, 76, 34]] };
  let btn, selT, selK, selSpeed, readout, labels = [];
  let t = 0, running = false, done = false, sig = '', traces = {};  // simulated time (s); finished runs by tube
  let OX = 0, OY = 0, SC = 1;                                      // the current panel's offset and scale (lab() boxes)

  // the model of the current settings: terminal speed (null = free fall) and the fall time through the tube
  const model = () => {
    const putki = selT.value(), kappale = selK.value();
    const vt = kappale === 'magneetti' && VT[putki] ? VT[putki] : null;
    return { putki, kappale, vt, T: fallTime(vt) };
  };
  const motion = (vt, s) => {                                      // position y (m) and speed v (m/s) at the time s
    if (vt === null) return { y: 0.5 * g * s * s, v: g * s };
    const tau = vt / g, e = Math.exp(-s / tau);
    return { y: vt * (s - tau * (1 - e)), v: vt * (1 - e) };
  };
  function fallTime(vt) {
    if (vt === null) return Math.sqrt(2 * H / g);
    let T = H / vt + vt / g;
    for (let i = 0; i < 60; i++) { const m = motion(vt, T); T -= (m.y - H) / m.v; }
    return T;
  }
  const restart = () => { t = 0; running = false; done = false; };
  const sync = () => { const m = model(), s = [m.putki, m.kappale].join('|'); if (s !== sig) { sig = s; restart(); } return m; };
  const finish = () => {                                           // the run reaches the bottom: keep it as this tube's trace
    const m = model(); t = m.T; running = false; done = true;
    if (m.kappale === 'magneetti') traces[m.putki] = { vt: m.vt, T: m.T };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('pudota')).parent(controls);
    btn.elt.addEventListener('click', () => { sync(); t = 0; done = false; running = true; });
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('putki')).parent(l1); selT = p.createSelect().parent(l1);
    for (const k of ['muovi', 'alumiini', 'kupari', 'rako']) selT.option(__(k), k);
    selT.selected('kupari');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('kappale')).parent(l2); selK = p.createSelect().parent(l2);
    selK.option(__('magneetti'), 'magneetti'); selK.option(__('teras'), 'teras'); selK.selected('magneetti');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    for (const e of [selT.elt, selK.elt]) e.addEventListener('change', () => { sync(); p.redraw(); });
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { putki: { input: selT.elt, unit: '' }, kappale: { input: selK.elt, unit: '' } },
      reset: () => { selT.selected('kupari'); selK.selected('magneetti'); sig = ''; restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
    window.fy76 = { finish: () => { sync(); finish(); p.redraw(); } };   // test hook: completes the current run at once
  };

  p.draw = () => {
    const m = sync();
    if (running) {
      t += Math.min(p.deltaTime, 100) / 1000 * (Number(selSpeed.value()) || 1);
      if (t >= m.T) finish();
    }
    const s = Math.min(t, m.T), mo = done ? motion(m.vt, m.T) : motion(m.vt, s);
    const y = done ? H : Math.min(mo.y, H), v = mo.v;
    const Ep = M * g * y, Ek = 0.5 * M * v * v, Q = Math.max(0, Ep - Ek);
    const Fj = m.vt === null ? 0 : M * g * v / m.vt;                 // braking force k v (N)
    const tila = done ? __('perilla') : running ? __('matkalla') : __('odota');
    readout.html(__('lukemat', { t: tx(s, 2), v: tx(v, 2), Ep: tx(Ep * 1e3, 1), Ek: tx(Ek * 1e3, 1), Q: tx(Q * 1e3, 1), tila: tila }));
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const narrow = cw < 500, CH = narrow ? 1210 : 400;
    if (p.__H !== CH) { p.__H = CH; p.resizeCanvas(600, CH); setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state
    const fhc = narrow ? Math.round(14 * k) : Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    p.background(250);
    const st = { m, s, y, v, Fj, Ep, Ek, Q };
    if (narrow) {
      panel(150, 0, 1.5, () => tube(st, fhc / 1.5));
      p.stroke(220); p.strokeWeight(1.5); p.line(0, 604, 600, 604);
      panel(0, 606, 1.5, () => graph(st, fhc / 1.5));
      p.line(0, 960, 600, 960);
      panel(0, 962, 1.5, () => bars(st, fhc / 1.5));
    } else {
      panel(0, 0, 1, () => tube(st, fhc));
      p.stroke(220); p.strokeWeight(1); p.line(200, 0, 200, 400); p.line(200, 236, 600, 236);
      panel(200, 0, 1, () => graph(st, fhc));
      panel(200, 238, 1, () => bars(st, fhc));
    }
    window.simState = { putki: m.putki, kappale: m.kappale, vt: m.vt === null ? 0 : m.vt, T: m.T, t: s, y, v, Fj, G: M * g,
      Ep: Ep * 1e3, Ek: Ek * 1e3, Q: Q * 1e3, aika: done ? m.T : 0, vLoppu: done ? v : 0, lampo: done ? Q * 1e3 : 0,
      running, valmis: done, jaljet: Object.keys(traces).length, labels };
  };

  function panel(ox, oy, sc, fn) { OX = ox; OY = oy; SC = sc; p.push(); p.translate(ox, oy); p.scale(sc); fn(); p.pop(); OX = 0; OY = 0; SC = 1; }

  // --- the tube (local 200 × 400): a longitudinal section, the body, its eddy-current rings and the forces ---
  const TOP = 72, BOT = 342, CX = 110, RO = 22, WALL = 6;          // 270 px = 1,00 m
  function tube(st, fh) {
    const { m } = st, cols = TUBE[m.putki];
    // dimension line: the tube's length
    p.stroke(...MUTEDC); p.strokeWeight(1.5);
    p.line(70, TOP, 70, BOT); p.line(64, TOP, 76, TOP); p.line(64, BOT, 76, BOT);
    lab('$1{,}00\\,\\text{m}$', 6, (TOP + BOT) / 2 + fh * 0.35, 'l', fh, MUTEDC);
    // the back wall seen through the cut-away front, then the two walls in section
    gr(CX - RO + WALL, TOP, 2 * (RO - WALL), BOT - TOP, [cols[0], cols[1]], true, 0, 0.35);
    if (m.putki === 'rako') { p.noStroke(); p.fill(...INKC); p.rect(CX - 2, TOP, 4, BOT - TOP); }
    gr(CX - RO, TOP, WALL, BOT - TOP, cols, true, 1, 1);
    gr(CX + RO - WALL, TOP, WALL, BOT - TOP, [cols[1], cols[0]], true, 1, 1);
    // the cushion under the tube
    p.noStroke(); p.fill(...RULEC); p.rect(CX - 40, BOT + 8, 80, 10, 4);
    // the body: a magnet with the N pole down, or a grey steel piece
    const yc = TOP - 20 + st.y * (BOT - TOP), w = 26, hh = 40;
    if (m.kappale === 'magneetti') {
      p.stroke(...INKC); p.strokeWeight(1.5); p.fill(...SPOLE); p.rect(CX - w / 2, yc - hh / 2, w, hh / 2, 3, 3, 0, 0);
      p.fill(...NPOLE); p.rect(CX - w / 2, yc, w, hh / 2, 0, 0, 3, 3);
      lab('$\\text{S}$', CX, yc - 5, 'c', fh * 0.85, INKC); lab('$\\text{N}$', CX, yc + 15, 'c', fh * 0.85, INKC);
    } else gr(CX - w / 2, yc - hh / 2, w, hh, [[173, 181, 189], [108, 117, 125]], true, 3, 1);
    // eddy-current rings in the wall below and above the magnet, their width the braking force (Lenz: below the
    // current is anticlockwise seen from above, above it clockwise)
    if (running && st.Fj > 1e-4) {
      const wgt = 1 + 3.5 * Math.min(1, st.Fj / (M * g));
      ring(yc + hh / 2 + 10, wgt, 1); ring(yc - hh / 2 - 10, wgt, -1);
    }
    // the forces on the body while it falls: the weight and the braking force, the same scale (45 px = m g)
    if (running) {
      const S = 45 / (M * g), xa = CX + RO + 10;
      arrow(xa, yc, xa, yc + M * g * S, RED, 3, 10);
      lab('$\\overline{G}$', xa + 8, yc + 30, 'l', fh, RED);
      if (st.Fj * S > 3) { arrow(xa + 18, yc, xa + 18, yc - st.Fj * S, RED, 3, 10); lab('$\\overline{F}_\\text{j}$', xa + 26, yc - 24, 'l', fh, RED); }
    }
    lab(__(`n_${m.putki}`), CX, BOT + 44, 'c', fh, INKC);
  }
  function ring(yr, wgt, dir) {
    if (yr < TOP + 4 || yr > BOT - 4) return;
    const a = RO - 1;
    p.noFill(); p.stroke(...VIOLET, 120); p.strokeWeight(wgt); p.arc(CX, yr, 2 * a, 12, Math.PI, 2 * Math.PI);
    p.stroke(...VIOLET); p.arc(CX, yr, 2 * a, 12, 0, Math.PI);
    // the arrowhead on the front arc: to the right = anticlockwise seen from above
    p.noStroke(); p.fill(...VIOLET);
    const x = CX + dir * 2, yy = yr + 6;
    p.triangle(x + dir * 7, yy, x - dir * 3, yy - 4.5, x - dir * 3, yy + 4.5);
  }

  // --- the graph y(t) (local 400 × 235): the run now and the last finished run of each tube ---
  const GX0 = 54, GY0 = 205, GX1 = 334, GY1 = 85, TMAX = 8;          // 1,00 m at GY1
  const X = (s) => GX0 + s / TMAX * (GX1 - GX0), Y = (y) => GY0 - y * (GY0 - GY1);
  function graph(st, fh) {
    p.stroke(...RULEC); p.strokeWeight(1);
    for (let s = 1; s <= TMAX; s++) p.line(X(s), GY0, X(s), GY1);
    for (const y of [0.25, 0.5, 0.75, 1]) p.line(GX0, Y(y), GX1, Y(y));
    arrow(GX0, GY0, GX1 + 24, GY0, INKC, 2, 9); arrow(GX0, GY0, GX0, GY1 - 26, INKC, 2, 9);
    p.stroke(...INKC); p.strokeWeight(1.5);
    for (let s = 1; s <= TMAX; s++) p.line(X(s), GY0, X(s), GY0 + 5);
    for (const y of [0.25, 0.5, 0.75, 1]) p.line(GX0 - 5, Y(y), GX0, Y(y));
    for (let s = 2; s <= TMAX; s += 2) lab(`$${s}$`, X(s), GY0 + 8 + fh, 'c', fh, MUTEDC);
    lab('$0$', GX0 - 8, GY0 + 8 + fh, 'r', fh, MUTEDC);
    for (const y of [0.5, 1]) lab(`$${tx(y, 1)}$`, GX0 - 9, Y(y) + fh * 0.35, 'r', fh, MUTEDC);
    lab('$t\\ (\\text{s})$', GX1 + 30, GY0 + fh * 0.35, 'l', fh, INKC);
    lab('$y\\ (\\text{m})$', GX0 - 6, GY1 - 30, 'r', fh, INKC);
    lab(__('kuvaaja'), GX0 + 14, 18, 'l', fh, INKC);
    // the finished runs, then the run now on top of them
    const placed = [];
    for (const key of ['muovi', 'rako', 'alumiini', 'kupari']) {
      const tr = traces[key]; if (!tr) continue;
      curve(tr.vt, tr.T, TRACE[key], 2.5, key === 'rako');
      const txt = __(`n_${key}`), x0 = X(tr.T) + 5;
      p.textSize(fh); const wdt = p.textWidth(txt);
      let row = 0;
      while (placed.some((b) => b.row === row && x0 < b.x1 + 4 && b.x0 < x0 + wdt + 4)) row++;
      placed.push({ row, x0, x1: x0 + wdt });
      lab(txt, x0, GY1 - 8 - row * fh * 1.3, 'l', fh, TRACE[key]);
    }
    if (running || done) {
      const m = st.m; curve(m.vt, st.s, m.kappale === 'magneetti' ? TRACE[m.putki] : MUTEDC, 3.5, m.putki === 'rako');
      const pt = motion(m.vt, st.s); p.noStroke(); p.fill(...COLDC); p.circle(X(st.s), Y(Math.min(pt.y, H)), 9);
    }
  }
  function curve(vt, T, col, w, dash) {
    p.noFill(); p.stroke(...col); p.strokeWeight(w);
    if (dash) p.drawingContext.setLineDash([7, 5]);
    p.beginShape(); const n = 80;
    for (let i = 0; i <= n; i++) { const s = T * i / n, y = Math.min(motion(vt, s).y, H); p.vertex(X(s), Y(y)); }
    p.endShape(); p.drawingContext.setLineDash([]);
  }

  // --- the energy bars (local 400 × 165): the loss of potential energy, the kinetic energy and the tube's internal energy ---
  function bars(st, fh) {
    const L = 96, W = 270, Emax = M * g * H, rows = [['$\\Delta E_\\text{p}$', st.Ep, MUTEDC], ['$E_\\text{k}$', st.Ek, COLDC], ['$Q$', st.Q, HEATC]];
    lab(__('energia'), 14, 22, 'l', fh, INKC);
    rows.forEach(([name, E, col], i) => {
      const yr = 52 + i * 38;
      p.noFill(); p.stroke(...RULEC); p.strokeWeight(1.5); p.rect(L, yr - 11, W, 22, 3);
      p.noStroke(); p.fill(...col); p.rect(L, yr - 11, W * Math.min(1, E / Emax), 22, 3);
      lab(name, L - 12, yr + fh * 0.35, 'r', fh, col === MUTEDC ? INKC : col);
    });
  }

  function arrow(x1, y1, x2, y2, col, w, Hh) {
    const L = Math.hypot(x2 - x1, y2 - y1); if (L < 2) return;
    const a = Math.atan2(y2 - y1, x2 - x1), hh = Math.min(Hh, L * 0.6);
    p.stroke(...col); p.strokeWeight(w); p.line(x1, y1, x2 - hh * 0.8 * Math.cos(a), y2 - hh * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2, y2, x2 - hh * Math.cos(a - 0.42), y2 - hh * Math.sin(a - 0.42), x2 - hh * Math.cos(a + 0.42), y2 - hh * Math.sin(a + 0.42));
  }
  // a rectangle with a linear gradient (horizontal when horiz), corner radius r, opacity op
  function gr(x, y, w, h, stops, horiz, r, op) {
    const c = p.drawingContext; c.save(); c.globalAlpha = op;
    const g2 = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => g2.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = g2; c.strokeStyle = 'rgba(31,41,51,0.55)'; c.lineWidth = 1.5; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); if (op === 1) c.stroke(); c.restore();
  }
  // every canvas text: drawn in the panel's coordinates, its ink box pushed to simState.labels in canvas coordinates
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0: OX + x0 * SC, y0: OY + (y - 0.75 * size) * SC, x1: OX + (x0 + w) * SC, y1: OY + (y + 0.25 * size) * SC });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
