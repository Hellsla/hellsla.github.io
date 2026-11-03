// fy5-10 Mekaaninen aaltoliike: a wave on a long rope (transverse) or a long coil spring (longitudinal).
// The source at x = 0 starts at t = 0 and moves as y_s(τ) = A sin(2πf τ) (continuous wave) or only for 0 ≤ τ ≤ 1/(2f)
// (one pulse, a single crest). Every point x of the medium repeats the source's motion after the delay x/v:
// y(x, t) = y_s(t − x/v), zero ahead of the front x = v t. Transverse: the displacement is across the rope (up);
// longitudinal: along the spring. A = 5,0 cm; v = 2,0 m/s (suuri jännitys) or 1,0 m/s (pieni jännitys); f on a slider;
// λ = v/f. The medium continues past the picture, so no reflected wave comes back (reflection is the next chapter).
// Top panel: the medium at one instant (a snapshot) with a ruler in metres and the marked point P at x = 1,00 m; bottom
// panel: P's displacement against time over the last 4,0 s. The largest displacements of P across and along the medium
// since the start are kept in simState (dyMax, dxMax) for the guided experiments. Velocity (the propagation) is blue.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const A = 5.0, XP = 1.0, XMAXM = 4.6, WIN = 4.0;
  const SPEED = { suuri: 2.0, pieni: 1.0 };
  const BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203];
  const ROPE = [169, 122, 53], SPRING = [138, 150, 163], HANDLE = [233, 201, 138];
  // geometry: wide 600 x 400 (medium on top, graph under it); narrow (sim-root < 500 px) 600 x 660, larger labels
  const WIDE = { H: 400, x0: 40, sx: 120, y0: 112, ys: 7, coil: 30, brk: 168, ruler: 192, rlab: 214, sep: 232,
    gx0: 70, gx1: 540, gy0: 318, gs: 9, gtop: 262, bottom: 390 };
  const NARROW = { H: 660, x0: 40, sx: 120, y0: 150, ys: 9, coil: 40, brk: 224, ruler: 262, rlab: 298, sep: 322,
    gx0: 92, gx1: 470, gy0: 470, gs: 12, gtop: 380, bottom: 630 };
  let G = WIDE, narrow = false, sk = 1, fh = 13, labels = [];
  let btn, btnReset, selType, selSrc, selTen, slF, lF, selSpeed, readout;
  let t = 0, running = false, dyMax = 0, dxMax = 0;

  const params = () => ({ aalto: selType.value(), lahde: selSrc.value(), jannitys: selTen.value(), f: Number(slF.value()) });
  function src(tau, P) {                                                  // the source's displacement (cm) at time τ
    if (tau < 0) return 0;
    if (P.lahde === 'pulssi' && tau > 1 / (2 * P.f)) return 0;
    return A * Math.sin(2 * Math.PI * P.f * tau);
  }
  const disp = (x, tt, P, v) => src(tt - x / v, P);
  const restart = () => { t = 0; running = false; dyMax = 0; dxMax = 0; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; });
    btnReset = p.createButton(__('alusta')).parent(controls);
    btnReset.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('aalto')).parent(l1); selType = p.createSelect().parent(l1);
    selType.option(__('poik'), 'poik'); selType.option(__('pitk'), 'pitk'); selType.selected('poik');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('lahde')).parent(l2); selSrc = p.createSelect().parent(l2);
    selSrc.option(__('jatkuva'), 'jatkuva'); selSrc.option(__('pulssi'), 'pulssi'); selSrc.selected('jatkuva');
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('jannitys')).parent(l3); selTen = p.createSelect().parent(l3);
    selTen.option(__('suuri'), 'suuri'); selTen.option(__('pieni'), 'pieni'); selTen.selected('suuri');
    const l4 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l4); slF = p.createSlider(0.5, 2.5, 1, 0.25).parent(l4);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.25'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    for (const el of [selType, selSrc, selTen, slF]) { el.elt.addEventListener('input', restart); el.elt.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { aalto: { input: selType.elt, unit: '' }, lahde: { input: selSrc.elt, unit: '' },
        jannitys: { input: selTen.elt, unit: '' }, f: { input: slF.elt, unit: 'Hz' } },
      reset: () => { selType.selected('poik'); selSrc.selected('jatkuva'); selTen.selected('suuri'); slF.value(1); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const P = params(), v = SPEED[P.jannitys], T = 1 / P.f, lam = v / P.f;
    if (running) t += Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    const yP = disp(XP, t, P, v);
    if (P.aalto === 'poik') dyMax = Math.max(dyMax, Math.abs(yP)); else dxMax = Math.max(dxMax, Math.abs(yP));
    const xFront = v * t;
    lF.html(__('taajuus', { f: tx(P.f, 2) }));
    const bt = running ? __('pysayta') : __('kaynnista');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const fs = tx(P.f, 2), Ts = tx(T, T < 1 ? 2 : 1), vs = tx(v, 1), ts = tx(t, 1), xs = tx(xFront, 1), dys = tx(dyMax, 1), dxs = tx(dxMax, 1);
    readout.html(P.lahde === 'pulssi'
      ? __('lukemat_pulssi', { f: fs, v: vs, lp: tx(lam / 2, 2), t: ts, xf: xs, dy: dys, dx: dxs })
      : __('lukemat', { f: fs, T: Ts, v: vs, l: tx(lam, 2), t: ts, xf: xs, dy: dys, dx: dxs }));
    window.simState = { aalto: P.aalto, lahde: P.lahde, jannitys: P.jannitys, f: P.f, T, v, lambda: lam, A, t, running,
      xFront, yP, dyMax, dxMax, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;                                                 // strokes grow with the label size on a phone
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state: draw again next frame
    labels = [];
    p.background(255);
    medium(P, v, lam);
    graph(P, v);
    window.simState.labels = labels;
  };

  // --- the rope or the spring at this instant ---
  function medium(P, v, lam) {
    const { x0, sx, y0, ys, coil, brk, ruler, rlab, sep } = G;
    const X = (xm) => x0 + xm * sx;
    grect(0, 0, 600, sep, [[246, 241, 230], [255, 255, 255]]);
    // the equilibrium line
    p.stroke(...RULEC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([7 * sk, 6 * sk]);
    p.line(x0, y0, 596, y0); p.drawingContext.setLineDash([]);
    const ySrc = disp(0, t, P, v);
    if (P.aalto === 'poik') {
      // the rope, drawn every 2 px; the displacement is drawn enlarged (ys px per cm, the ruler is in metres)
      p.noFill(); p.stroke(...ROPE); p.strokeWeight(5 * sk); p.beginShape();
      for (let xp = x0; xp <= 596; xp += 2) p.vertex(xp, y0 - disp((xp - x0) / sx, t, P, v) * ys);
      p.endShape();
      p.noStroke(); p.fill(...INKC);
      for (let j = 0; j <= 23; j++) { const xm = j * 0.2; if (Math.abs(xm - XP) < 1e-6) continue; p.circle(X(xm), y0 - disp(xm, t, P, v) * ys, 6 * sk); }
      // the source's handle
      p.fill(...HANDLE); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(x0 - 26 * sk, y0 - ySrc * ys - 9 * sk, 24 * sk, 18 * sk, 3);
      const yPp = y0 - disp(XP, t, P, v) * ys;
      p.fill(...INKC); p.stroke(255); p.strokeWeight(2.5 * sk); p.circle(X(XP), yPp, 15 * sk);
      lab('$P$', X(XP), yPp - 14 * sk, 'c', INKC);
    } else {
      // the spring: a shade where the coils crowd (compression −ds/dx > 0), then coils every 0,10 m, each shifted
      // along the spring by its displacement (to the ruler's scale)
      p.noStroke();
      for (let xp = x0; xp < 596; xp += 3) {
        const xm = (xp + 1.5 - x0) / sx, h = 0.02;
        const e = -(disp(xm + h, t, P, v) - disp(xm - h, t, P, v)) / (2 * h) * 0.01;   // strain (cm per m -> m per m)
        if (e > 0.02) { p.fill(108, 117, 125, Math.min(1, e / 0.5) * 110); p.rect(xp, y0 - coil, 3, 2 * coil); }
      }
      p.noFill();
      for (let j = 0; j <= 46; j++) {
        const xm = j * 0.1, xp = X(xm) + disp(xm, t, P, v) * 0.01 * sx;
        const isP = Math.abs(xm - XP) < 1e-6;
        p.stroke(...(isP ? INKC : SPRING)); p.strokeWeight((isP ? 3.5 : 2.5) * sk);
        p.ellipse(xp, y0, 5 * sk, 2 * coil);
      }
      const xPp = X(XP) + disp(XP, t, P, v) * 0.01 * sx;
      p.fill(...INKC); p.stroke(255); p.strokeWeight(2.5 * sk); p.circle(xPp, y0 - coil, 13 * sk);
      lab('$P$', xPp, y0 - coil - 13 * sk, 'c', INKC);
      // the pusher at the left end
      const xs = x0 + ySrc * 0.01 * sx;
      p.fill(...HANDLE); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(xs - 22 * sk, y0 - coil, 14 * sk, 2 * coil, 3);
    }
    // the propagation direction: a blue arrow (velocity colour)
    const ay = narrow ? 30 * sk : 26;
    p.stroke(...BLUE); p.strokeWeight(3.5 * sk); p.line(486, ay, 576 - 14 * sk, ay);
    p.noStroke(); p.fill(...BLUE); p.triangle(578, ay, 576 - 16 * sk, ay - 8 * sk, 576 - 16 * sk, ay + 8 * sk);
    lab('$v$', 478, ay + fh * 0.36, 'r', BLUE);
    // λ between two neighbouring crests (transverse) or compressions (longitudinal), continuous wave only
    if (P.lahde === 'jatkuva') {
      const front = Math.min(v * t, XMAXM), off = P.aalto === 'poik' ? 0.25 : 1.0, xs = [];
      for (let kk = 0; kk < 40; kk++) { const xc = v * t - lam * (off + kk); if (xc < 0) break; if (xc <= front - 1e-9 && xc <= XMAXM) xs.push(xc); }
      xs.sort((a, b) => a - b);
      if (xs.length >= 2) {
        const a = X(xs[0]), b = X(xs[1]);
        p.stroke(...INKC); p.strokeWeight(2 * sk);
        p.line(a, brk, b, brk); p.line(a, brk - 7 * sk, a, brk + 7 * sk); p.line(b, brk - 7 * sk, b, brk + 7 * sk);
        p.stroke(...MUTEDC); p.strokeWeight(1.2 * sk); p.drawingContext.setLineDash([4 * sk, 4 * sk]);
        const ya = P.aalto === 'poik' ? y0 - A * ys : y0 + coil;
        p.line(a, ya, a, brk); p.line(b, ya, b, brk); p.drawingContext.setLineDash([]);
        lab('$\\lambda$', (a + b) / 2, brk + fh + 3 * sk, 'c', INKC);
      }
    }
    // the ruler in metres
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(x0, ruler, X(4), ruler);
    for (let j = 0; j <= 8; j++) { const xx = X(j / 2); p.line(xx, ruler, xx, ruler + (j % 2 ? 4 : 8) * sk); }
    for (let j = 0; j <= 4; j++) lab(j === 0 ? '$0$' : '$' + j + '\\,\\text{m}$', X(j), rlab, 'c', INKC);
    p.stroke(220); p.strokeWeight(1); p.line(0, sep, 600, sep);
  }

  // --- P's displacement against time over the last 4,0 s ---
  function graph(P, v) {
    const { gx0, gx1, gy0, gs, gtop, bottom } = G;
    const t0 = Math.max(0, t - WIN);
    const X = (tt) => gx0 + (tt - t0) / WIN * (gx1 - gx0), Y = (y) => gy0 - y * gs;
    const yTop = Y(6), yBot = Y(-6);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let s = Math.ceil(t0 + 1e-9); s <= t0 + WIN + 1e-9; s++) p.line(X(s), yTop, X(s), yBot);
    for (const yy of [-5, 5]) p.line(gx0, Y(yy), gx1, Y(yy));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(gx0, yBot, gx0, yTop - 8 * sk); p.line(gx0, gy0, gx1 + 14 * sk, gy0);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx0, yTop - 20 * sk, gx0 - 6 * sk, yTop - 6 * sk, gx0 + 6 * sk, yTop - 6 * sk);
    p.triangle(gx1 + 26 * sk, gy0, gx1 + 12 * sk, gy0 - 6 * sk, gx1 + 12 * sk, gy0 + 6 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (const yy of [-5, 0, 5]) { p.line(gx0 - 6 * sk, Y(yy), gx0, Y(yy)); lab('$' + (yy < 0 ? '-' : '') + Math.abs(yy) + '$', gx0 - 9 * sk, Y(yy) + fh * 0.36, 'r', INKC); }
    for (let s = Math.ceil(t0 - 1e-9); s <= t0 + WIN + 1e-9; s++) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(X(s), gy0, X(s), gy0 + 6 * sk);
      if (X(s) > gx0 + 10 * sk || s === 0) lab('$' + s + '$', X(s), bottom, 'c', INKC);
    }
    lab('$y\\,(\\text{cm})$', gx0 + 12 * sk, gtop, 'l', INKC);
    lab(__('lbl_p'), 594, gtop, 'r', INKC);
    lab('$t\\,(\\text{s})$', 594, bottom, 'r', INKC);
    // P's displacement up to now
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3 * sk); p.beginShape();
    const steps = 400;
    for (let j = 0; j <= steps; j++) { const tt = t0 + (t - t0) * j / steps; p.vertex(X(tt), Y(disp(XP, tt, P, v))); }
    p.endShape();
    p.fill(...INKC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(X(t), Y(disp(XP, t, P, v)), 12 * sk);
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
