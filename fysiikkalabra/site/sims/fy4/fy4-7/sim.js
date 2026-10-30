// fy4-7 Liike-energia, potentiaalienergia ja mekaaninen energia: a cart starts up a straight ramp from its foot with speed v0,
// stops for a moment at its highest point and rolls back to the foot. Model: a point cart on a straight ramp at α = 25° (loiva) or
// 50° (jyrkkä), g = 9,81 m/s², no air resistance; with "pieni kitka" a friction force μN (μ = 0,10) opposes the motion. Up the ramp
// the deceleration is g(sin α + μ cos α), down it g(sin α − μ cos α); the motion is computed exactly phase by phase, so h_max and
// the return speed v_paluu emerge from the motion: without friction h_max = v0²/(2g) on either ramp and v_paluu = v0, with friction
// both are smaller. Energies every frame: E_k = ½ m v², E_p = m g h (zero level at the foot), E_mek = E_k + E_p.
// Left (phone: top): the ramp with a height staff, the cart with its velocity (blue) and the highest point. Right (phone: below):
// three energy bars on one fixed scale (0–16 J) so that runs can be compared. Every canvas text goes through lab().
new p5((p) => {
  const g = 9.81, MU = 0.10, EMAX = 16, ANG = { loiva: 25, jyrkka: 50 };
  const RH = 0.95;                                                          // the ramp is drawn up to 0,95 m
  const EK_C = [232, 89, 12], EP_C = [43, 138, 62], EM_C = [73, 80, 87], BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  let narrow = false, laid = false, OY = 0, U = 1, labels = [];
  const L = { SY: 146, FX: 82, FL: 378, S: 240, RX: 60, H: 400, bx0: 92, bx1: 530, rows: [30, 64, 98], bh: 22, ax: 122 };   // set per layout
  const SH = 300, BHN = 210, BW = 146;                                      // phone: scene and bar panel heights; wide: bar panel height
  let btn, slV, lV, selM, selR, selK, selSpeed, readout;
  let t = 0, running = false, done = false, P = null;

  const model = () => {
    const v0 = Number(slV.value()), m = Number(selM.value()), rinne = selR.value(), kitka = selK.value();
    const al = ANG[rinne] * Math.PI / 180, mu = kitka === 'pieni' ? MU : 0;
    const aU = g * (Math.sin(al) + mu * Math.cos(al)), aD = g * (Math.sin(al) - mu * Math.cos(al));
    const tUp = v0 / aU, sMax = v0 * v0 / (2 * aU), tDown = Math.sqrt(2 * sMax / aD);
    return { v0, m, rinne, kitka, al, mu, aU, aD, tUp, sMax, tDown, tEnd: tUp + tDown, hMax: sMax * Math.sin(al), vBack: aD * tDown };
  };
  const state = (M, tt) => {                                               // s along the ramp from the foot, v positive up the ramp
    if (tt <= M.tUp) return { s: M.v0 * tt - 0.5 * M.aU * tt * tt, v: M.v0 - M.aU * tt };
    const td = Math.min(tt, M.tEnd) - M.tUp;
    return { s: Math.max(0, M.sMax - 0.5 * M.aD * td * td), v: -M.aD * td };
  };
  const restart = () => { P = model(); t = 0; running = false; done = false; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(1, 4, 2, 0.5).parent(l1);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of ['0.5', '1', '2']) selM.option(Number(m).toFixed(m === '0.5' ? 2 : 1).replace('.', DECP) + ' kg', m);
    selM.selected('1');
    const lr = p.createElement('label').parent(controls); p.createSpan(__('ramppi')).parent(lr); selR = p.createSelect().parent(lr);
    selR.option(__('loiva'), 'loiva'); selR.option(__('jyrkka'), 'jyrkka');
    const lk = p.createElement('label').parent(controls); p.createSpan(__('kitka')).parent(lk); selK = p.createSelect().parent(lk);
    selK.option(__('eikitkaa'), 'ei'); selK.option(__('pienikitka'), 'pieni');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.25'); selSpeed.option(__('normaali'), '0.5'); selSpeed.option(__('nopea'), '1'); selSpeed.selected('0.5');
    for (const e of [slV.elt, selM.elt, selR.elt, selK.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { v0: { input: slV.elt, unit: 'm/s' }, m: { input: selM.elt, unit: 'kg' }, rinne: { input: selR.elt, unit: '' }, kitka: { input: selK.elt, unit: '' } },
      reset: () => { slV.value(2); selM.selected('1'); selR.selected('loiva'); selK.selected('ei'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const M = model();
    if (!P || M.v0 !== P.v0 || M.m !== P.m || M.rinne !== P.rinne || M.kitka !== P.kitka) restart();
    if (running) {
      t = Math.min(t + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()), P.tEnd);
      if (t >= P.tEnd - 1e-9) { t = P.tEnd; running = false; done = true; }
    }
    const st = state(P, t), h = st.s * Math.sin(P.al);
    const Ek = 0.5 * P.m * st.v * st.v, Ep = P.m * g * h, Emek = Ek + Ep, Ek0 = 0.5 * P.m * P.v0 * P.v0;
    const hmax = t >= P.tUp - 1e-9 ? P.hMax : null, vback = done ? P.vBack : null;
    lV.html(__('alkunopeus', { v: tx(P.v0, 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { v: tx(Math.abs(st.v), 2), h: tx(h, 3), Ek: tx(Ek, 2), Ep: tx(Ep, 2), Em: tx(Emek, 2),
                                 hm: hmax === null ? '\\ldots' : tx(hmax, 3), vb: vback === null ? '\\ldots' : tx(vback, 2) }));
    window.simState = { v0: P.v0, m: P.m, rinne: P.rinne, kitka: P.kitka, alpha: ANG[P.rinne], mu: P.mu, t, s: st.s, h, v: st.v,
                        Ek, Ep, Emek, Ek0, hmax, vback, running, done, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) return;                                         // the canvas was resized: draw on the next frame
    U = narrow ? 0.8 * k : Math.max(1, k * 0.8);
    const fh = narrow ? Math.round(14 * k) : Math.round(14 * k * (k > 1.3 ? 1.12 : 1));   // phone: about 14 CSS px on screen
    labels = [];
    p.background(250);
    OY = 0; p.push(); scene(st, h, hmax, fh); p.pop();
    OY = narrow ? SH : 0; p.push(); p.translate(0, OY); bars(Ek, Ep, Emek, Ek0, fh); p.pop();
    window.simState.labels = labels;
  };

  // wide screen: the energy bars in a band across the top, the ramp under them at the full width; phone (the sim's box under
  // 500 px): the ramp on top and the bars under it, both at the full 600 width with larger labels
  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) Object.assign(L, { SY: 0, FX: 126, FL: 272, S: 226, RX: 70, H: SH, bx0: 112, bx1: 480, rows: [34, 84, 134], bh: 34, ax: 166 });
    else Object.assign(L, { SY: BW, FX: 82, FL: 378, S: 240, RX: 60, H: 400, bx0: 92, bx1: 530, rows: [30, 64, 98], bh: 22, ax: 122 });
    p.resizeCanvas(600, n ? SH + BHN : 400);
    return true;
  }

  // --- the scene: wall, floor, the plywood ramp, the height staff, the cart with its velocity and the highest point ---
  function scene(st, h, hmax, fh) {
    const H = L.H, W = 600, al = P.al, ca = Math.cos(al), sa = Math.sin(al);
    grect(0, L.SY, W, L.FL - L.SY, [[240, 244, 248], [222, 230, 238]], 0);
    grect(0, L.FL, W, H - L.FL, [[233, 201, 138], [210, 170, 100]], 0);
    p.stroke(169, 122, 53, 120); p.strokeWeight(1);
    for (let x = 20; x < W; x += 46) p.line(x, L.FL + 6, x - 14, H);
    const hx = L.FX + RH / Math.tan(al) * L.S, hy = L.FL - RH * L.S, xEnd = Math.min(W - 6, hx + 40);
    const c = p.drawingContext; c.save();                                  // the plywood wedge and the deck behind its top
    const gr = c.createLinearGradient(0, hy, 0, L.FL); gr.addColorStop(0, 'rgb(233,201,138)'); gr.addColorStop(1, 'rgb(217,178,106)');
    c.fillStyle = gr; c.strokeStyle = 'rgb(31,41,51)'; c.lineWidth = 2 * U;
    c.beginPath(); c.moveTo(L.FX, L.FL); c.lineTo(hx, hy); c.lineTo(xEnd, hy); c.lineTo(xEnd, L.FL); c.closePath(); c.fill(); c.stroke(); c.restore();
    p.stroke(169, 122, 53, 150); p.strokeWeight(1);
    for (let f = 0.25; f < 1; f += 0.25) { const y = L.FL - f * RH * L.S; p.line(L.FX + f * RH / Math.tan(al) * L.S + 4, y, xEnd - 2, y); }
    p.stroke(...INKC); p.strokeWeight(3 * U); p.line(L.FX, L.FL, hx, hy);
    p.noStroke(); p.fill(...INKC); p.rect(0, L.FL - 1, W, 2.5);
    lab(`$\\alpha = ${ANG[P.rinne]}^\\circ$`, L.FX + (narrow ? 118 : 104), L.FL - (narrow ? 12 : 9), 'l', fh * 0.9, INKC);
    // the height staff with 0,1 m ticks, numbers every 0,2 m
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(L.RX, L.FL, L.RX, L.FL - 0.9 * L.S);
    for (let i = 0; i <= 9; i++) {
      const y = L.FL - i * 0.1 * L.S; p.strokeWeight((i % 2 ? 1.2 : 2) * U); p.line(L.RX, y, L.RX + (i % 2 ? 6 : 11) * U, y);
      if (i % 2 === 0) lab(`$${tx(i / 10, i ? 1 : 0)}$`, L.RX - 6, y + fh * 0.36, 'r', fh, MUTEDC);
    }
    if (narrow) lab('$h\\ (\\text{m})$', L.RX + 14 * U, L.FL - 1.0 * L.S + fh * 0.36, 'l', fh, INKC);   // phone: right of the staff's top
    else lab('$h\\ (\\text{m})$', L.RX - 6, L.FL - 0.9 * L.S + fh * 0.36, 'r', fh, INKC);
    // the highest point: a dashed line from the staff to the ramp, its value above it
    if (hmax !== null) {
      const y = L.FL - hmax * L.S, xr = L.FX + hmax / Math.tan(al) * L.S;
      p.stroke(...MUTEDC); p.strokeWeight(1.5 * U); dashed(L.RX, y, xr, y, 6 * U);
      const hs = `$h_\\text{max} = ${tx(hmax, 3)}\\,\\text{m}$`; p.textSize(fh);
      if (xr + 12 + p.textWidth(hs) < 594) lab(hs, xr + 12, y + fh * 0.36, 'l', fh, INKC);   // on the ramp's face, clear of the cart's way back
      else lab(hs, L.RX + 14 * U, y - 6 * U, 'l', fh, INKC);
    }
    // the cart on the ramp, tilted with it, mass blocks of 0,50 kg on a 0,50 kg cart
    const sc = narrow ? 1.5 : 1.3, sp = st.s * L.S + 16 * sc;               // the rear wheel touches the foot when s = 0
    const cx = L.FX + sp * ca, cy = L.FL - sp * sa;
    p.push(); p.translate(cx, cy); p.rotate(-al);
    grect(-20 * sc, -24 * sc, 40 * sc, 14 * sc, [[120, 160, 200], [60, 100, 150]], 3);
    const nb = Math.round((P.m - 0.5) / 0.5);
    for (let i = 0; i < nb; i++) grect(-17 * sc + (i % 2) * 18 * sc, (-34 - Math.floor(i / 2) * 10) * sc, 16 * sc, 9 * sc, [[160, 166, 172], [100, 106, 112]], 1);
    p.noStroke(); p.fill(...INKC); p.circle(-11 * sc, -6 * sc, 11 * sc); p.circle(11 * sc, -6 * sc, 11 * sc);
    p.fill(196, 204, 212); p.circle(-11 * sc, -6 * sc, 4 * sc); p.circle(11 * sc, -6 * sc, 4 * sc);
    p.pop();
    // the velocity: a blue arrow along the ramp, beside the cart on its outer side
    if (Math.abs(st.v) > 0.02) {
      // up the ramp the arrow starts ahead of the cart; down the ramp it ends just above the cart, so it never leaves the picture
      const d = Math.sign(st.v), kv = narrow ? 30 : 19, off = narrow ? 40 : 34, gap = narrow ? 20 : 18;
      const a1 = d > 0 ? gap : gap - st.v * kv, x1 = cx + a1 * ca - sa * off, y1 = cy - a1 * sa - ca * off, x2 = x1 + st.v * kv * ca, y2 = y1 - st.v * kv * sa;
      p.stroke(...BLUE); p.strokeWeight(3 * U); p.line(x1, y1, x2, y2);
      const hl = 9 * U;
      p.noStroke(); p.fill(...BLUE);
      p.triangle(x2 + d * 2 * ca, y2 - d * 2 * sa, x2 - d * hl * ca - 5 * U * sa, y2 + d * hl * sa - 5 * U * ca, x2 - d * hl * ca + 5 * U * sa, y2 + d * hl * sa + 5 * U * ca);
      const lx = d > 0 ? x2 : x1, ly = d > 0 ? y2 : y1;                    // the name beyond the upper end of the arrow
      lab('$\\overline{v}$', lx + fh * 0.9 * ca, ly - fh * 0.9 * sa + fh * 0.36, 'c', fh, BLUE);
    }
  }

  // --- the bars: horizontal, E_k orange, E_p green, E_mek grey on one fixed scale; the dashed mark is E_mek at the start ---
  function bars(Ek, Ep, Em, Ek0, fh) {
    const PH = narrow ? BHN : BW, X = (e) => L.bx0 + Math.max(0, e) / EMAX * (L.bx1 - L.bx0);
    p.noStroke(); p.fill(255); p.rect(0, 0, 600, PH);
    p.stroke(220); p.strokeWeight(1); p.line(0, narrow ? 0 : PH, 600, narrow ? 0 : PH);
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let e = 2; e <= EMAX; e += 2) p.line(X(e), L.rows[0] - L.bh / 2 - 6, X(e), L.ax);
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(L.bx0, L.ax, L.bx1 + 16, L.ax); p.line(L.bx0, L.ax, L.bx0, L.rows[0] - L.bh / 2 - 8);
    p.noStroke(); p.fill(...INKC); p.triangle(L.bx1 + 24, L.ax, L.bx1 + 14, L.ax - 4 * U, L.bx1 + 14, L.ax + 4 * U);
    const ticks = narrow ? [0, 8, 16] : [0, 4, 8, 12, 16];
    for (const e of ticks) { p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(X(e), L.ax, X(e), L.ax + 5); lab(`$${e}$`, X(e), L.ax + fh * 1.05, 'c', fh, MUTEDC); }
    lab('$E\\ (\\text{J})$', 12, L.ax + fh * 1.05, 'l', fh, INKC);
    const vals = [[Ek, EK_C, '$E_\\text{k}$'], [Ep, EP_C, '$E_\\text{p}$'], [Em, EM_C, '$E_\\text{mek}$']];
    vals.forEach(([e, col, name], i) => {
      const y = L.rows[i];
      p.noStroke(); p.fill(...col); p.rect(L.bx0, y - L.bh / 2, X(e) - L.bx0, L.bh);
      lab(`$${tx(e, e < 10 ? 2 : 1)}\\,\\text{J}$`, X(e) + 8, y + fh * 0.36, 'l', fh, col);
      lab(name, 12, y + fh * 0.36, 'l', fh, col);
    });
    p.noFill(); p.stroke(...EM_C); p.strokeWeight(1.5 * U);                  // the mechanical energy at the start
    const x0 = X(Ek0), y2 = L.rows[2]; dashed(x0, y2 - L.bh / 2 - 4, x0, y2 + L.bh / 2 + 4, 4 * U);
  }

  function dashed(x1, y1, x2, y2, d) { const c = p.drawingContext; c.save(); c.setLineDash([d, d * 0.8]); p.line(x1, y1, x2, y2); c.restore(); }
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
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const DECP = DEC === '.' ? '.' : ',';
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
