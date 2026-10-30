// fy4-9 Liikemäärä ja impulssi: a laboratory cart of mass m runs to the right (+x) at v1 on a level track and hits a
// bumper at the wall. Model: friction and air resistance are neglected, and the weight and the track's normal force
// cancel, so the only horizontal force is the bumper's. While the bumper is pressed in by c, it pushes the cart to the
// left with F = k c (k: hard 1600, medium 400, soft 100 N/m). "pysahtyy": a crushable bumper that stays crushed, so its
// force ends when the cart stops; "kimpoaa": a spring bumper that pushes the cart back until it leaves the bumper.
// Newton's second law is integrated with RK4 steps of 0,1 ms of simulated time. The force is recorded during the contact
// into a (t, F) graph (t from the first contact), and the impulse I is the area under the recorded force with the minus
// sign of a force to the left; Δp = m v2 − m v1 comes from the velocities, so I = Δp is a result, not an input.
// Top: the situation picture with the cart's velocity (blue), momentum (purple) and the bumper's force on it (red).
// Bottom: the (t, F) graph, the current run red with its area shaded, up to three earlier runs grey for comparison.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const K = { kova: 1600, keski: 400, pehmea: 100 }, DT = 1e-4;
  const XS = 0.30, XB = 1.18, XW = 1.50, LB = XW - XB, LC = 0.25;              // cart front at start, bumper's free end, wall (m); cart length (m)
  const RED = [201, 42, 42], BLUE = [25, 113, 194], PURPLE = [112, 72, 232], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const HN = { sc: 280, gr: 390 };                                              // stacked panel heights on a phone
  let laid = false, narrow = false, OY = 0, U = 1;
  const SC = { h: 150, x0: 26, S: 340, gy: 122 };                               // scene: height, x px of 0 m, px per metre, track top
  const GR = { h: 250, x0: 74, x1: 494, y0: 212, y1: 40 };                      // graph: plot area in panel coordinates
  let btn, slV, lV, selM, selB, selT, selSpeed, readout;
  let x = XS, v = 0, t = 0, running = false, done = false, contact = false, ended = false, crush = 0;
  let tc = 0, area = 0, Fprev = 0, Fmax = 0, curve = [], kesto = null, imp = null, v2 = null, old = [], labels = [];

  const P = () => ({ m: Number(selM.value()), v1: Number(slV.value()), b: selB.value(), k: K[selB.value()], ty: selT.value() });
  function restart() {
    const M = P(); x = XS; v = M.v1; t = 0; running = false; done = false; contact = false; ended = false; crush = 0;
    tc = 0; area = 0; Fprev = 0; Fmax = 0; curve = []; kesto = null; imp = null; v2 = null;
  }
  const comp = () => Math.max(x - XB, 0);                                         // how far the cart presses the bumper in (m)
  function step(M, dt) {
    const acc = (xx) => (M.ty === 'pysahtyy' && ended) ? 0 : -M.k * Math.max(xx - XB, 0) / M.m;
    const k1x = v, k1v = acc(x), k2x = v + dt / 2 * k1v, k2v = acc(x + dt / 2 * k1x);
    const k3x = v + dt / 2 * k2v, k3v = acc(x + dt / 2 * k2x), k4x = v + dt * k3v, k4v = acc(x + dt * k3x);
    let xn = x + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x), vn = v + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
    if (!contact && !ended && xn > XB) {                                         // the first contact inside this step, at its fraction f
      const f = (XB - x) / (xn - x), Fn = M.k * (xn - XB);
      contact = true; tc = (1 - f) * dt; area = Fn / 2 * tc; Fprev = Fn; Fmax = Fn; curve = [[0, 0], [tc, Fn]]; x = xn; v = vn; return;
    }
    if (contact) {
      if (M.ty === 'pysahtyy' && vn <= 0) {                                       // the crushable bumper: the cart stops and stays
        const f = v / (v - vn), xs = x + f * (xn - x), Fs = M.k * (xs - XB);
        area += (Fprev + Fs) / 2 * f * dt; tc += f * dt; Fmax = Math.max(Fmax, Fs); curve.push([tc, Fs], [tc, 0]);
        x = xs; v = 0; crush = xs - XB; finish(M, 0); running = false; done = true; return;
      }
      if (M.ty === 'kimpoaa' && xn <= XB && vn < 0) {                           // the spring bumper: the cart leaves it
        const f = (x - XB) / (x - xn); area += Fprev / 2 * f * dt; tc += f * dt; curve.push([tc, 0]);
        finish(M, v + f * (vn - v)); x = xn; v = vn; return;
      }
      const Fn = M.k * Math.max(xn - XB, 0); area += (Fprev + Fn) / 2 * dt; Fprev = Fn; Fmax = Math.max(Fmax, Fn); tc += dt;
      if (curve.length === 0 || tc - curve[curve.length - 1][0] >= 0.001) curve.push([tc, Fn]);
    }
    x = xn; v = vn;
    if (ended && M.ty === 'kimpoaa' && x <= XS) { x = XS; running = false; done = true; }
  }
  function finish(M, vEnd) {
    contact = false; ended = true; kesto = tc; imp = -area; v2 = vEnd;
    old.push(curve.slice()); if (old.length > 4) old.shift();                    // the run itself plus three earlier ones
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(0.5, 2, 2, 0.5).parent(l1);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    selM.option('0,50 kg', '0.5'); selM.option('1,0 kg', '1'); selM.option('2,0 kg', '2'); selM.selected('1');
    const lb = p.createElement('label').parent(controls); p.createSpan(__('puskuri')).parent(lb); selB = p.createSelect().parent(lb);
    for (const b of ['kova', 'keski', 'pehmea']) selB.option(__(b), b);
    selB.selected('kova');
    const lt = p.createElement('label').parent(controls); p.createSpan(__('tormays')).parent(lt); selT = p.createSelect().parent(lt);
    selT.option(__('pysahtyy'), 'pysahtyy'); selT.option(__('kimpoaa'), 'kimpoaa'); selT.selected('pysahtyy');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.1'); selSpeed.option(__('normaali'), '0.25'); selSpeed.option(__('nopea'), '1'); selSpeed.selected('0.25');
    for (const e of [slV.elt, selM.elt, selB.elt, selT.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { m: { input: selM.elt, unit: 'kg' }, v1: { input: slV.elt, unit: 'm/s' }, puskuri: { input: selB.elt, unit: '' }, tormays: { input: selT.elt, unit: '' } },
      reset: () => { slV.value(2); selM.selected('1'); selB.selected('kova'); selT.selected('pysahtyy'); old = []; restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) setTimeout(() => p.redraw(), 0);                     // the canvas was resized: draw it again once it has settled
    const M = P();
    if (running) {
      let left = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
      while (left > 1e-12 && running) { const d = Math.min(DT, left); step(M, d); t += d; left -= d; }
    }
    const F = (M.ty === 'pysahtyy' && ended) ? 0 : M.k * comp(), p1 = M.m * M.v1;
    lV.html(__('alkunopeus', { v: tx(M.v1, 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const q = (val, d) => val === null ? '\\ldots' : tx(val, d);
    readout.html(__('lukemat', { dt: q(kesto, 4), Fm: q(kesto === null ? null : Fmax, 1), I: q(imp, 2), v1: tx(M.v1, 2), v2: q(v2, 2),
                                 p1: tx(p1, 2), p2: q(v2 === null ? null : M.m * v2, 2), dp: q(v2 === null ? null : M.m * v2 - p1, 2) }));
    window.simState = { m: M.m, v1: M.v1, puskuri: M.b, k: M.k, tormays: M.ty, t, x, v, p: M.m * v, F, running, done,
                        dt: kesto, Fmax: kesto === null ? null : Fmax, I: imp, v2, p1, p2: v2 === null ? null : M.m * v2,
                        dp: v2 === null ? null : M.m * v2 - p1, labels: null };
    U = narrow ? 0.8 * k : Math.max(1, k * 0.8);
    const fh = narrow ? Math.round(14 * k) : Math.round(13 * k);                  // phone: about 14 CSS px on screen
    labels = [];
    p.background(250);
    OY = 0; p.push(); scene(M, F, fh); p.pop();
    OY = SC.h; p.push(); p.translate(0, OY); graph(fh); p.pop();
    window.simState.labels = labels;
  };

  // wide screen: the scene above the graph in 600×400; phone (the sim's box under 500 px): both panels taller, larger text
  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) { Object.assign(SC, { h: HN.sc, x0: 26, S: 340, gy: 244 }); Object.assign(GR, { h: HN.gr, x0: 104, x1: 470, y0: 330, y1: 66 }); p.resizeCanvas(600, HN.sc + HN.gr); }
    else { Object.assign(SC, { h: 150, x0: 26, S: 340, gy: 122 }); Object.assign(GR, { h: 250, x0: 74, x1: 494, y0: 212, y1: 40 }); p.resizeCanvas(600, 400); }
    return true;
  }
  const X = (xm) => SC.x0 + xm * SC.S;

  // --- the scene: the track, the wall with its bumper, the cart and its arrows ---
  function scene(M, F, fh) {
    grect(0, 0, 600, SC.gy, [[232, 240, 246], [246, 241, 230]], 0);
    p.noStroke(); p.fill(233, 201, 138); p.rect(0, SC.gy + 10 * U, 600, SC.h - SC.gy - 10 * U);
    p.fill(196, 204, 212); p.rect(X(0) - 10, SC.gy, X(XW) - X(0) + 10, 10 * U);                 // the aluminium track
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * U); p.line(X(0) - 10, SC.gy, X(XW), SC.gy);
    // the wall, hatched
    const wx = X(XW), wt = SC.gy - 70 * U;
    p.noStroke(); p.fill(201, 194, 178); p.rect(wx, wt, 600 - wx - 12, SC.gy + 10 * U - wt);
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(wx, wt, wx, SC.gy + 10 * U);
    p.strokeWeight(1.2 * U); for (let yy = wt + 8 * U; yy < SC.gy + 10 * U; yy += 12 * U) p.line(wx + 2, yy + 10 * U, Math.min(wx + 14 * U, 588), yy);
    // the bumper: a spring (kimpoaa) or a crushable block (pysahtyy) between the wall and its plate
    const c = M.ty === 'pysahtyy' && ended ? crush : comp(), pxp = X(XB + c), by = SC.gy - 18 * U, bh = 22 * U;
    const sw = { kova: 4, keski: 2.6, pehmea: 1.6 }[M.b] * U;
    if (M.ty === 'kimpoaa') {
      p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(sw); p.beginShape();
      const nz = 9; for (let i = 0; i <= nz * 2; i++) { const xx = pxp + (wx - pxp) * i / (nz * 2); p.vertex(xx, by + (i === 0 || i === nz * 2 ? 0 : (i % 2 ? -bh / 2 : bh / 2))); }
      p.endShape();
    } else {
      p.fill(241, 223, 181); p.stroke(...INKC); p.strokeWeight(1.5 * U); p.rect(pxp, by - bh / 2, wx - pxp, bh);
      p.stroke(169, 122, 53); p.strokeWeight(sw * 0.6); const nh = 7;
      for (let i = 1; i < nh; i++) { const xx = pxp + (wx - pxp) * i / nh; p.line(xx, by - bh / 2 + 2, xx, by + bh / 2 - 2); }
    }
    p.noStroke(); p.fill(...INKC); p.rect(pxp - 4 * U, by - bh * 0.75, 4 * U, bh * 1.5, 1);
    // the cart: wheels, a blue-grey body with a load block
    const xf = X(x), xb = X(x - LC), cy = SC.gy - 9 * U, ch = 26 * U, top = cy - ch - 6 * U;
    p.fill(...INKC); p.circle(xb + 0.22 * (xf - xb), SC.gy - 5 * U, 11 * U); p.circle(xb + 0.78 * (xf - xb), SC.gy - 5 * U, 11 * U);
    grect(xb, cy - ch, xf - xb, ch, [[164, 196, 226], [79, 143, 191]], 3);
    grect(xb + 0.2 * (xf - xb), cy - ch - 10 * U * (0.5 + M.m / 2), 0.6 * (xf - xb), 10 * U * (0.5 + M.m / 2), [[120, 128, 138], [80, 88, 98]], 2);
    // arrows above the cart: velocity (blue, 34 px per m/s) and momentum (purple, 22 px per kg·m/s); the bumper's force (red, 1 px per N)
    const xm = (xf + xb) / 2, loadTop = cy - ch - 10 * U * (0.5 + M.m / 2), yv = loadTop - 14 * U, yp = yv - (narrow ? 34 : 24) * U;
    arrowH(xm, yv, v * 34 * U, BLUE, '$\\overline{v}$', fh);
    arrowH(xm, yp, M.m * v * 22 * U, PURPLE, '$\\overline{p}$', fh);
    if (F > 0.05) arrowH(xf, cy - ch / 2, -F * U, RED, '$\\overline{F}$', fh, true);
    // the positive direction and the clock
    const ax = narrow ? 470 : 500, ay = fh + 4;
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(ax, ay - fh * 0.3, ax + 50 * U, ay - fh * 0.3);
    p.noStroke(); p.fill(...INKC); p.triangle(ax + 58 * U, ay - fh * 0.3, ax + 48 * U, ay - fh * 0.3 - 5 * U, ax + 48 * U, ay - fh * 0.3 + 5 * U);
    lab('$+x$', ax - 6 * U, ay, 'r', fh, INKC);
    lab(`$t = ${tx(t, 2)}\\,\\text{s}$`, 10, ay, 'l', fh, INKC);
  }
  // a horizontal arrow from (x0, y) of signed length L; its label beyond the tail (or below the tip for the force)
  function arrowH(x0, y, L, col, s, fh, below) {
    if (Math.abs(L) < 3) return;
    const sg = Math.sign(L), hd = 9 * U, x1 = x0 + L;
    p.stroke(...col); p.strokeWeight(3 * U); p.line(x0, y, x1 - sg * hd * 0.8, y);
    p.noStroke(); p.fill(...col); p.triangle(x1, y, x1 - sg * hd, y - hd * 0.5, x1 - sg * hd, y + hd * 0.5);
    if (below) lab(s, x1 + 4 * U, y - 8 * U, 'r', fh, col);
    else lab(s, x0 - sg * 6 * U, y + fh * 0.35, sg > 0 ? 'r' : 'l', fh, col);
  }

  // --- the (t, F) graph: earlier runs grey, the current one red with its area shaded ---
  function graph(fh) {
    p.noStroke(); p.fill(255); p.rect(0, 0, 600, GR.h);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, 600, 0);
    const TX = (tt) => GR.x0 + tt / 0.5 * (GR.x1 - GR.x0), FY = (F) => GR.y0 - F / 120 * (GR.y0 - GR.y1);
    p.stroke(227, 220, 203); p.strokeWeight(1.2);
    for (let i = 1; i <= 5; i++) p.line(TX(i / 10), GR.y0, TX(i / 10), GR.y1);
    for (let F = 20; F <= 120; F += 20) p.line(GR.x0, FY(F), GR.x1, FY(F));
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(GR.x0, GR.y0, GR.x1 + 16 * U, GR.y0); p.line(GR.x0, GR.y0, GR.x0, GR.y1 - 16 * U);
    p.noStroke(); p.fill(...INKC);
    p.triangle(GR.x1 + 24 * U, GR.y0, GR.x1 + 14 * U, GR.y0 - 5 * U, GR.x1 + 14 * U, GR.y0 + 5 * U);
    p.triangle(GR.x0, GR.y1 - 24 * U, GR.x0 - 5 * U, GR.y1 - 14 * U, GR.x0 + 5 * U, GR.y1 - 14 * U);
    for (let i = 1; i <= 5; i++) if (!narrow || i % 2 === 0) lab(`$${tx(i / 10, 1)}$`, TX(i / 10), GR.y0 + fh * 1.2, 'c', fh, MUTEDC);
    for (let F = 20; F <= 120; F += 20) if (!narrow || F % 40 === 0) lab(`$${F}$`, GR.x0 - 8 * U, FY(F) + fh * 0.35, 'r', fh, MUTEDC);
    lab('$0$', GR.x0 - 8 * U, GR.y0 + fh * 1.2, 'r', fh, MUTEDC);
    lab('$t\\ (\\text{s})$', GR.x1 + 30 * U, GR.y0 + fh * 0.35, 'l', fh, INKC);
    lab('$F\\ (\\text{N})$', GR.x0 + 10 * U, GR.y1 - 18 * U, 'l', fh, INKC);
    const draw = (cv, col, w, fill) => {
      if (cv.length < 2) return;
      if (fill) { p.noStroke(); p.fill(201, 42, 42, 60); p.beginShape(); p.vertex(TX(cv[0][0]), GR.y0); for (const [a, b] of cv) p.vertex(TX(Math.min(a, 0.5)), FY(b)); p.vertex(TX(Math.min(cv[cv.length - 1][0], 0.5)), GR.y0); p.endShape(p.CLOSE); }
      p.noFill(); p.stroke(...col); p.strokeWeight(w); p.beginShape(); for (const [a, b] of cv) p.vertex(TX(Math.min(a, 0.5)), FY(b)); p.endShape();
    };
    const cur = (contact || ended) ? curve : null;
    for (const cv of (ended ? old.slice(0, -1) : old).slice(-3)) draw(cv, [160, 166, 174], 2 * U, false);
    if (cur) draw(cur, RED, 3 * U, true);
    if (imp !== null) lab(`$|I| = ${tx(Math.abs(imp), 2)}\\,\\text{N}\\cdot\\text{s}$`, GR.x1, GR.y1 + fh * 0.6, 'r', fh, RED);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x0, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const tw = p.textWidth(s), xl = align === 'r' ? x0 - tw : align === 'c' ? x0 - tw / 2 : x0;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, xl, y);
    labels.push({ s, x0: xl, y0: OY + y - 0.75 * size, x1: xl + tw, y1: OY + y + 0.25 * size });
  }
  function grect(x0, y, w_, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x0, y, x0, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x0, y, w_, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (val, d) => val.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
