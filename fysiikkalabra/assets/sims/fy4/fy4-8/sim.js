// fy4-8 Mekaanisen energian säilyminen ja energiaperiaate: a roller-coaster car is released from rest at height h1 on
// the left side of a valley and rolls through it up the other side. The valley is a level floor of 6 m between two ramps,
// either circular arcs of radius 21 m ("kaari") or straight 45° slopes ("suora"), 20,5 m high. u is the distance along the
// track from the middle of the floor. Model: the weight and the track's normal force act on the car, and a constant
// resistive force F (rolling and air resistance together) points against the motion; the normal force is perpendicular to
// the motion and does no work. Newton's second law along the track, a = −g·dy/du − F/m, is integrated with RK4 steps of
// 2 ms of simulated time; the energies are computed from the state (E_k = ½mv², E_p = mgh) and the work of the resistive
// force from its definition (W_muut = −F s), so the energy principle ΔE_mek = W_muut is a result, not an input.
// The run ends at the car's first stop: h2 is the height there. v_pohja is the speed at the middle of the floor.
// Left (top on a phone): the situation picture with a measuring pole and the car's velocity (blue). Right (bottom on a
// phone): bars of E_p, E_k, E_mek and W_muut on one scale, with a dashed line at the initial mechanical energy.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, B = 3, R = 21, ANG = 45 * Math.PI / 180, YTOP = 20.5, DT = 0.002;
  const GREEN = [43, 138, 62], BLUE = [25, 113, 194], HEATC = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  let laid = false, narrow = false, OX = 0, OY = 0, U = 1;
  const SC = { w: 400, h: 400, S: 6, cx: 200, gy: 336 };                  // scene panel: width, height, px per metre, centre x, ground y
  const EN = { x: 400, w: 200, y0: 0, h: 400, top: 62, zero: 214, bot: 366, name: 390 };   // energy panel (canvas coordinates within the panel)
  const HN = { sc: 330, en: 360 };                                          // stacked panel heights on a phone
  let btn, slH, lH, slF, lF, selM, selR, selSpeed, readout;
  let u0 = 0, u = 0, w = 0, t = 0, running = false, done = false, vpohja = null, h2 = null, labels = [];

  const P = () => ({ h1: Number(slH.value()), F: Number(slF.value()), m: Number(selM.value()), rata: selR.value() });
  const rampLen = (h, rata) => rata === 'kaari' ? R * Math.acos(1 - h / R) : h / Math.sin(ANG);
  function geo(uu, rata) {                                                  // the track point at u: x, y (m) and slope dy/du, angle
    const q = Math.abs(uu) - B, sg = uu >= 0 ? 1 : -1;
    if (q <= 0) return { x: uu, y: 0, sl: 0, ang: 0 };
    if (rata === 'kaari') { const th = q / R; return { x: sg * (B + R * Math.sin(th)), y: R * (1 - Math.cos(th)), sl: sg * Math.sin(th), ang: sg * th }; }
    return { x: sg * (B + q * Math.cos(ANG)), y: q * Math.sin(ANG), sl: sg * Math.sin(ANG), ang: sg * ANG };
  }
  const restart = () => { const M = P(); u0 = -(B + rampLen(M.h1, M.rata)); u = u0; w = 0; t = 0; running = false; done = false; vpohja = null; h2 = null; };
  function step(M, dt) {                                                    // one RK4 step; the car moves to the right during a run
    const acc = (uu) => -g * geo(uu, M.rata).sl - M.F / M.m;
    const k1u = w, k1w = acc(u), k2u = w + dt / 2 * k1w, k2w = acc(u + dt / 2 * k1u);
    const k3u = w + dt / 2 * k2w, k3w = acc(u + dt / 2 * k2u), k4u = w + dt * k3w, k4w = acc(u + dt * k3u);
    const un = u + dt / 6 * (k1u + 2 * k2u + 2 * k3u + k4u), wn = w + dt / 6 * (k1w + 2 * k2w + 2 * k3w + k4w);
    if (vpohja === null && u < 0 && un >= 0) vpohja = w + (wn - w) * (-u) / (un - u);
    if (wn <= 0 && u > u0 + 0.01) { const f = w / (w - wn); u = u + f * (un - u); w = 0; running = false; done = true; h2 = geo(u, M.rata).y; return; }
    u = un; w = wn;
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lH = p.createSpan('').parent(l1); slH = p.createSlider(5, 20, 10, 2.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l2); slF = p.createSlider(0, 300, 0, 50).parent(l2);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of ['400', '600', '800']) selM.option(m + ' kg', m);
    selM.selected('400');
    const lr = p.createElement('label').parent(controls); p.createSpan(__('rata')).parent(lr); selR = p.createSelect().parent(lr);
    selR.option(__('kaari'), 'kaari'); selR.option(__('suora'), 'suora');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '3'); selSpeed.selected('1');
    for (const e of [slH.elt, slF.elt, selM.elt, selR.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { h1: { input: slH.elt, unit: 'm' }, F: { input: slF.elt, unit: 'N' }, m: { input: selM.elt, unit: 'kg' }, rata: { input: selR.elt, unit: '' } },
      reset: () => { slH.value(10); slF.value(0); selM.selected('400'); selR.selected('kaari'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const M = P();
    if (running) {
      let left = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
      while (left > 1e-9 && running) { const d = Math.min(DT, left); step(M, d); t += d; left -= d; }
    }
    const G = geo(u, M.rata), Ek = 0.5 * M.m * w * w, Ep = M.m * g * G.y, Em = Ek + Ep, Em0 = M.m * g * M.h1, s = u - u0, W = -M.F * s;
    lH.html(__('korkeus', { h: tx(M.h1, 1) }));
    lF.html(__('vastus', { F: tx(M.F, 0) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const kJ = (E) => tx(E / 1000, 2);
    readout.html(__('lukemat', { h: tx(G.y, 2), v: tx(Math.abs(w), 2), s: tx(s, 1), Ep: kJ(Ep), Ek: kJ(Ek), Em: kJ(Em), W: kJ(W), dE: kJ(Em - Em0),
                                 vp: vpohja === null ? '\\ldots' : tx(vpohja, 2), h2: h2 === null ? '\\ldots' : tx(h2, 2) }));
    window.simState = { h1: M.h1, F: M.F, m: M.m, rata: M.rata, t, h: G.y, v: Math.abs(w), s, Ek, Ep, Em, Em0, W, dEm: Em - Em0,
                        vpohja, h2, running, done, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    setLayout(cw < 500);
    U = narrow ? 0.8 * k : Math.max(1, k * 0.8);
    const fh = narrow ? Math.round(14 * k) : Math.round(13 * k);   // phone: about 14 CSS px on screen
    labels = [];
    p.background(250);
    OX = 0; OY = 0; p.push(); scene(M, G, fh); p.pop();
    OX = narrow ? 0 : EN.x; OY = narrow ? HN.sc : 0; p.push(); p.translate(OX, OY); energy(M, Ep, Ek, Em, Em0, W, fh); p.pop();
    window.simState.labels = labels;
  };

  // wide screen: the scene left and the energy bars right in 600×400; phone (the sim's box under 500 px): stacked at full width
  function setLayout(n) {
    if (n === narrow && laid) return;
    laid = true; narrow = n;
    if (n) { Object.assign(SC, { w: 600, h: HN.sc, S: 11.6, cx: 300, gy: 304 }); Object.assign(EN, { x: 0, w: 600, h: HN.en, top: 74, zero: 194, bot: 314, name: 346 }); p.resizeCanvas(600, HN.sc + HN.en); }
    else { Object.assign(SC, { w: 400, h: 400, S: 7.5, cx: 200, gy: 352 }); Object.assign(EN, { x: 400, w: 200, h: 400, top: 62, zero: 214, bot: 366, name: 390 }); p.resizeCanvas(600, 400); }
  }
  const X = (x) => SC.cx + x * SC.S, Y = (y) => SC.gy - y * SC.S;

  // --- the scene: sky, the valley track on its supports, the measuring pole, the start height, the car and its velocity ---
  function scene(M, G, fh) {
    grect(0, 0, SC.w, SC.gy, [[208, 230, 251], [238, 245, 249]], 0);
    grect(0, SC.gy, SC.w, SC.h - SC.gy, [[178, 214, 160], [120, 170, 110]], 0);
    cloud(SC.w * 0.3, SC.gy - 23 * SC.S, SC.S * 0.8); cloud(SC.w * 0.8, SC.gy - 24 * SC.S, SC.S * 0.6);
    const uTop = B + rampLen(YTOP, M.rata);
    const pts = []; for (let k = 0; k <= 160; k++) { const uu = -uTop + 2 * uTop * k / 160; const q = geo(uu, M.rata); pts.push([X(q.x), Y(q.y)]); }
    p.stroke(196, 204, 212); p.strokeWeight(2 * U);                          // supports every 3 m under the track
    for (let x = -24; x <= 24; x += 3) { const q = pts.reduce((b, c) => Math.abs(c[0] - X(x)) < Math.abs(b[0] - X(x)) ? c : b); if (q[1] < SC.gy - 2 && Math.abs(q[0] - X(x)) < 4) p.line(q[0], q[1] + 3, q[0], SC.gy); }
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(5 * U); p.beginShape(); for (const q of pts) p.vertex(q[0], q[1]); p.endShape();
    p.stroke(225); p.strokeWeight(1.5 * U); p.beginShape(); for (const q of pts) p.vertex(q[0], q[1] - 1); p.endShape();
    // measuring pole in the middle of the valley: ticks every 5 m, numbers on its left
    const px = X(0) - 1;
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(px, Y(0), px, Y(20) - 6);
    for (let hm = 5; hm <= 20; hm += 5) { p.line(px - 5 * U, Y(hm), px + 5 * U, Y(hm)); lab(`$${hm}\\,\\text{m}$`, px - 8 * U, Y(hm) + fh * 0.36, 'r', fh, MUTEDC); }
    // the start height h1 as a dashed line across the valley; after the run the reached height h2
    const xTop = geo(uTop, M.rata).x; p.textSize(fh); const gap = p.textWidth('$20\\,\\text{m}$') + 14 * U;   // the line stops short of the pole's numbers
    dashed(X(-xTop), Y(M.h1), px - gap, Y(M.h1), INKC); dashed(px, Y(M.h1), X(xTop), Y(M.h1), INKC);
    lab('$h_1$', px + 8 * U, Y(M.h1) - 6 * U, 'l', fh, INKC);
    if (done && h2 !== null && h2 > 0.05) dashed(px, Y(h2), X(geo(u, M.rata).x), Y(h2), HEATC);
    // the car: a red body with a rider, tilted along the track
    const cx = X(G.x), cy = Y(G.y), L = 4.2 * SC.S, H = 1.5 * SC.S;
    p.push(); p.translate(cx, cy); p.rotate(-G.ang);
    p.noStroke(); p.fill(31, 41, 51); p.circle(-L * 0.3, -H * 0.18, H * 0.42); p.circle(L * 0.3, -H * 0.18, H * 0.42);
    grect(-L / 2, -H * 1.25, L, H, [[226, 70, 70], [170, 34, 34]], 3);
    p.noStroke(); p.fill(241, 223, 181); p.circle(-L * 0.12, -H * 1.55, H * 0.6); p.circle(L * 0.2, -H * 1.55, H * 0.6);
    p.pop();
    // velocity: blue arrow along the track from above the car
    const v = Math.abs(w);
    if (v > 0.05) {
      const ca = Math.cos(G.ang), sa = Math.sin(G.ang), ox = cx - sa * (H * 2.3), oy = cy - ca * (H * 2.3);
      const Lv = Math.max(10, v * 2.6 * U * (narrow ? 1.4 : 1)), tx2 = ox + ca * Lv, ty2 = oy - sa * Lv;
      p.stroke(...BLUE); p.strokeWeight(2.5 * U); p.line(ox, oy, tx2, ty2);
      const a = Math.atan2(ty2 - oy, tx2 - ox), hd = 9 * U;
      p.noStroke(); p.fill(...BLUE); p.triangle(tx2, ty2, tx2 - hd * Math.cos(a - 0.45), ty2 - hd * Math.sin(a - 0.45), tx2 - hd * Math.cos(a + 0.45), ty2 - hd * Math.sin(a + 0.45));
    }
    lab(`$t = ${tx(t, 2)}\\,\\text{s}$`, 10, fh + 6, 'l', fh, INKC);
  }
  function cloud(x, y, k) {                                                // a flat white cloud, k px per metre of its size
    p.noStroke(); p.fill(255, 255, 255, 220);
    for (const [dx, dy, r] of [[-3, 0.6, 2.4], [0, -0.6, 3], [3.2, 0.4, 2.4], [6, 0.9, 1.8], [-5.6, 1, 1.6]]) p.circle(x + dx * k, y + dy * k, 2 * r * k);
    p.rect(x - 5.6 * k, y + 0.9 * k, 11.6 * k, 1.6 * k, 0.8 * k);
  }
  function dashed(x1, y1, x2, y2, col) {
    p.stroke(...col); p.strokeWeight(1.5 * U); const n = Math.max(1, Math.floor(Math.hypot(x2 - x1, y2 - y1) / (10 * U)));
    for (let i = 0; i < n; i += 2) p.line(x1 + (x2 - x1) * i / n, y1 + (y2 - y1) * i / n, x1 + (x2 - x1) * (i + 1) / n, y1 + (y2 - y1) * (i + 1) / n);
  }

  // --- the energy bars: E_p, E_k, E_mek (E_p and E_k stacked) up from zero, W_muut down; all to one scale, E_mek,1 dashed ---
  function energy(M, Ep, Ek, Em, Em0, W, fh) {
    p.noStroke(); p.fill(255); p.rect(0, 0, EN.w, EN.h);
    p.stroke(220); p.strokeWeight(1); if (narrow) p.line(0, 0, EN.w, 0); else p.line(0, 0, 0, EN.h);
    lab('$\\text{Energia}$', 10, narrow ? fh + 6 : fh + 8, 'l', fh, INKC);
    const k = (EN.zero - EN.top) / Em0, bw = narrow ? 70 : 30, xs = [0.14, 0.38, 0.62, 0.86].map((f) => EN.w * f);
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(8, EN.zero, EN.w - 8, EN.zero);
    dashed(8, EN.top, EN.w - 8, EN.top, MUTEDC);
    lab('$E_{\\text{mek},1}$', EN.w - 8, EN.top - 7 * U, 'r', fh, MUTEDC);
    p.noStroke();
    p.fill(...GREEN); p.rect(xs[0] - bw / 2, EN.zero - Ep * k, bw, Ep * k);
    p.fill(...BLUE); p.rect(xs[1] - bw / 2, EN.zero - Ek * k, bw, Ek * k);
    p.fill(...GREEN); p.rect(xs[2] - bw / 2, EN.zero - Ep * k, bw, Ep * k);
    p.fill(...BLUE); p.rect(xs[2] - bw / 2, EN.zero - Em * k, bw, Ek * k);
    p.fill(...HEATC); p.rect(xs[3] - bw / 2, EN.zero, bw, Math.min(-W * k, EN.bot - EN.zero));
    const names = ['$E_\\text{p}$', '$E_\\text{k}$', '$E_\\text{mek}$', '$W_\\text{muut}$'];
    names.forEach((s, i) => lab(s, xs[i], EN.name, 'c', fh, i === 0 ? GREEN : i === 1 ? BLUE : i === 3 ? HEATC : INKC));
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const tw = p.textWidth(s), x0 = align === 'r' ? x - tw : align === 'c' ? x - tw / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0: OX + x0, y0: OY + y - 0.75 * size, x1: OX + x0 + tw, y1: OY + y + 0.25 * size });
  }
  function grect(x, y, w_, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w_, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
