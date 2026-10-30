// fy4-14 Ilmanvastus ja putoaminen ilmassa: a skydiver (mass with the equipment 60, 80 or 100 kg) leaves a plane at rest and
// falls belly down or head down; the parachute stays closed or opens 20 s into the fall. Model: the air resistance points
// against the velocity and is computed numerically as F_v = k v² (k = 0,26 kg/m belly down, 0,10 kg/m head down, 30 kg/m with
// the canopy open; while the canopy opens, k grows over 3,0 s as k0 + (k1 − k0)·s², s = elapsed/3,0 s). The motion is integrated
// with steps of 2 ms of simulated time from the equation of motion G − F_v = m a (positive direction down); g = 9,81 m/s², the
// air's density is taken as constant, buoyancy is neglected. A run lasts 40 s; when it ends, the final speed and the largest
// air resistance of the run are recorded.
// Top left: the situation picture (tilannekuva): the sky scrolls past the jumper, the velocity (blue) and the acceleration
// (orange) are drawn beside the jumper, never forces. Right: the force diagram (voimakuvio), the jumper as a plain rectangle,
// G from the centre, F_v ending at the lower face the air presses on in free fall, starting at the top once the canopy opens
// (the canopy pulls from above), both to one scale; an arrow longer than the panel is cut with a break mark. Bottom: the (t, v) graph. On a phone the panels stack at the
// full 600 width. Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, K = { vatsa: 0.26, paa: 0.10 }, KV = 30, TOPEN = 20, TOPENING = 3.0, TEND = 40, H0 = 4000, DT = 0.002, SAMPLE = 0.5;
  const RED = [201, 42, 42], BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const SUIT = [43, 138, 62], SKIN = [241, 223, 181], RIG = [73, 80, 87], CANOPY = [233, 201, 138], CANOPY2 = [217, 178, 106];
  const HN = { sit: 260, dia: 380, gra: 290 };                          // panel heights when stacked on a phone (canvas 600 wide)
  let laid = false, narrow = false, W = 406, SH = 196, OY = 0, U = 1, S = 0.12;
  const D = { x: 503, y: 240, w: 56, h: 40, top: 46 };                  // the force diagram's rectangle; top: the highest arrow tip
  const GR = { x0: 56, x1: 380, y0: 172, y1: 34 };                      // graph: t = 0 and t = 40 s, v = 0 and v = 100 m/s (panel-local)
  let btn, selM, selAsento, selVarjo, selSpeed, readout, labels = [];
  let t = 0, v = 0, y = 0, a = g, Fv = 0, k = K.vatsa, open = 0, running = false, done = false, samples = [], FvMax = 0, vT = null;

  const params = () => ({ m: Number(selM.value()), asento: selAsento.value(), varjo: selVarjo.value() });
  const drag = (P, tt) => {                                             // k at time tt (kg/m) and the canopy's opening fraction
    const k0 = K[P.asento];
    if (P.varjo !== 'auki' || tt < TOPEN) return [k0, 0];
    const s = Math.min(1, (tt - TOPEN) / TOPENING);
    return [k0 + (KV - k0) * s * s, s];
  };
  const restart = () => { t = 0; v = 0; y = 0; running = false; done = false; FvMax = 0; vT = null; samples = [[0, 0]]; state(params()); };
  const state = (P) => { [k, open] = drag(P, t); Fv = k * v * v; a = (P.m * g - Fv) / P.m; };
  const advance = (P, dt) => {                                          // Euler steps of 2 ms of simulated time
    let left = dt;
    while (left > 1e-9) {
      const h = Math.min(DT, left, TEND - t); if (h <= 0) break;
      state(P); v += a * h; y += v * h; t += h; left -= h;
      state(P); FvMax = Math.max(FvMax, Fv);
      if (t >= samples[samples.length - 1][0] + SAMPLE - 1e-9) samples.push([Math.round(t / SAMPLE) * SAMPLE, v]);
    }
    if (t >= TEND - 1e-9) { running = false; done = true; vT = v; }
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of ['60', '80', '100']) selM.option(m + ' kg', m);
    selM.selected('80');
    const la = p.createElement('label').parent(controls); p.createSpan(__('asento')).parent(la); selAsento = p.createSelect().parent(la);
    selAsento.option(__('vatsa'), 'vatsa'); selAsento.option(__('paa'), 'paa');
    const lv = p.createElement('label').parent(controls); p.createSpan(__('varjo')).parent(lv); selVarjo = p.createSelect().parent(lv);
    selVarjo.option(__('ei'), 'ei'); selVarjo.option(__('auki'), 'auki');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '1'); selSpeed.option(__('normaali'), '4'); selSpeed.option(__('nopea'), '10'); selSpeed.selected('4');
    for (const e of [selM.elt, selAsento.elt, selVarjo.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { m: { input: selM.elt, unit: 'kg' }, asento: { input: selAsento.elt, unit: '' }, varjo: { input: selVarjo.elt, unit: '' } },
      reset: () => { selM.selected('80'); selAsento.selected('vatsa'); selVarjo.selected('ei'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const P = params();
    if (running) advance(P, Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
    state(P);
    const G = P.m * g, sumF = G - Fv;
    const bt = running ? __('tauko') : (t > 0 && !done ? __('jatka') : __('kaynnista')); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { G: tx(G, 0), Fv: tx(Fv, 0), sF: tx(sumF, 0), t: tx(t, 1), h: tx(H0 - y, 0), v: tx(v, 1), a: tx(a, 1),
                                 vT: vT === null ? '\\ldots' : tx(vT, 1), Fmax: vT === null ? '\\ldots' : tx(FvMax, 0) }));
    window.simState = { m: P.m, asento: P.asento, varjo: P.varjo, t, h: H0 - y, v, a, G, Fv, sumF, k, open, vT, FvMax: done ? FvMax : null,
                        running, done, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, kk = Math.max(1, 600 / cw);
    setLayout(cw < 500);
    U = narrow ? 0.8 * kk : Math.max(1, kk * 0.8);
    const fh = Math.round((narrow ? 16 : 14) * kk * (!narrow && kk > 1.3 ? 1.12 : 1));   // about 15 CSS px on a phone, at least 14 on a wide screen
    labels = [];
    p.background(250);
    OY = 0; p.push(); situation(P, fh); p.pop();
    OY = narrow ? HN.sit : 0; p.push(); p.translate(0, OY); diagram(P, G, fh); p.pop();
    OY = narrow ? HN.sit + HN.dia : SH; p.push(); p.translate(0, OY); graph(fh, kk); p.pop();
    window.simState.labels = labels;
  };

  // wide screen: the 600×400 picture; phone (the sim's box under 500 px): the three panels stacked at the full 600 width
  function setLayout(n) {
    if (n === narrow && laid) return;
    laid = true; narrow = n;
    if (n) { W = 600; SH = HN.sit; S = 0.13; D.x = 300; D.y = 200; D.w = 76; D.h = 46; D.top = 46; GR.x0 = 76; GR.x1 = 560; GR.y0 = 236; GR.y1 = 64; p.resizeCanvas(600, HN.sit + HN.dia + HN.gra); }
    else { W = 406; SH = 196; S = 0.12; D.x = 503; D.y = 240; D.w = 56; D.h = 40; D.top = 46; GR.x0 = 56; GR.x1 = 380; GR.y0 = 172; GR.y1 = 34; p.resizeCanvas(600, 400); }
  }

  // --- the situation picture: the sky scrolling past the jumper, the canopy when it opens, v and a beside the jumper ---
  function situation(P, fh) {
    const c = p.drawingContext; c.save();
    const gr = c.createLinearGradient(0, 0, 0, SH); gr.addColorStop(0, 'rgb(165,216,255)'); gr.addColorStop(1, 'rgb(238,245,249)');
    c.fillStyle = gr; c.fillRect(0, 0, W, SH); c.restore();
    p.noStroke();                                                          // clouds drift up as the jumper falls past them (0,5 px per metre)
    for (let i = 0; i < 5; i++) {
      const span = SH + 120, cy = ((i * 97 + 40 - y * 0.5) % span + span) % span - 60, cx = (i * 151 + 30) % (W - 40) + 20;
      p.fill(255, 255, 255, 215); p.ellipse(cx, cy, 70 * U, 26 * U); p.ellipse(cx + 22 * U, cy - 8 * U, 44 * U, 24 * U); p.ellipse(cx - 20 * U, cy - 5 * U, 36 * U, 20 * U);
    }
    const jx = narrow ? 210 : 170, jy = narrow ? 170 : 112;
    jumper(P, jx, jy);
    const vx = jx + (narrow ? 120 : 100), ax = vx + (narrow ? 90 : 62);
    vArrow(vx, jy, v, narrow ? 1.25 : 0.95, BLUE, '$\\overline{v}$', fh, 0.5);
    if (t > 0) vArrow(ax, jy, a, narrow ? 5 : 4, ORANGE, '$\\overline{a}$', fh, 0.3);
    const ty = fh + 4;
    lab(__('tilannekuva'), 10, ty, 'l', fh, INKC);
    lab(`$h = ${tx(H0 - y, 0)}\\,\\text{m}$`, W - 8, ty, 'r', fh, INKC);
  }
  function jumper(P, x, yy) {                                              // a skydiver in a green suit, the rig on the back
    const s = narrow ? 1.35 : 1.2;
    p.push(); p.translate(x, yy); p.scale(s);
    if (open > 0) {                                                        // the canopy: grows from a bag to a full wing
      const w = 24 + 116 * open, hgt = 8 + 16 * open, ch = -40 - 12 * open;   // width, rise above the chord, the chord's height
      p.stroke(...MUTEDC); p.strokeWeight(1);
      for (const fx of [-0.5, -0.2, 0.2, 0.5]) p.line(fx * 14, -16, fx * w * 0.9, ch);
      p.stroke(...INKC); p.strokeWeight(1.5); p.fill(...CANOPY); p.arc(0, ch, w, hgt * 2, p.PI, p.TWO_PI, p.CHORD);
      p.stroke(...CANOPY2); for (let i = 1; i < 6; i++) { const xx = -w / 2 + i * w / 6; p.line(xx, ch, xx, ch - hgt * Math.sin(Math.PI * i / 6) * 0.95); }
    }
    p.stroke(...INKC); p.strokeWeight(1.5);
    if (open > 0) {                                                        // hanging upright under the canopy
      p.fill(...SUIT); p.rect(-8, -18, 16, 28, 5); p.rect(-7, 8, 6, 20, 3); p.rect(1, 8, 6, 20, 3);
      p.fill(...RIG); p.rect(-6, -16, 12, 12, 2); p.fill(...SKIN); p.circle(0, -25, 13);
      p.fill(...INKC); p.arc(0, -26, 13, 12, p.PI, p.TWO_PI);
    } else if (P.asento === 'paa') {                                       // head down, arms along the body
      p.fill(...SUIT); p.rect(-8, -24, 16, 34, 5); p.rect(-7, -44, 6, 22, 3); p.rect(1, -44, 6, 22, 3);
      p.fill(...RIG); p.rect(6, -20, 6, 16, 2); p.fill(...SKIN); p.circle(0, 17, 13); p.fill(...INKC); p.arc(0, 18, 13, 12, 0, p.PI);
    } else {                                                               // belly down, arms and legs spread and bent up
      p.fill(...SUIT);
      p.push(); p.translate(-16, -3); p.rotate(-0.6); p.rect(-4, -18, 7, 18, 3); p.pop();
      p.push(); p.translate(18, -3); p.rotate(0.5); p.rect(-3, -18, 7, 18, 3); p.pop();
      p.rect(-20, -6, 40, 14, 6);
      p.push(); p.translate(-20, 0); p.rotate(0.9); p.rect(-24, -3, 22, 7, 3); p.pop();
      p.fill(...RIG); p.rect(-10, -11, 20, 7, 2);
      p.fill(...SKIN); p.circle(26, 1, 13); p.fill(...INKC); p.arc(27, 1, 13, 13, -p.HALF_PI, p.HALF_PI);
    }
    p.pop();
  }
  function vArrow(x, y0, val, scale, col, name, fh, eps) {                // a thin vertical arrow with an open head: positive = down
    if (Math.abs(val) < eps) return;
    const dir = Math.sign(val), room = dir > 0 ? SH - 10 - y0 : y0 - fh * 2.2;
    const L = Math.max(14, Math.min(Math.abs(val) * scale, room)), y2 = y0 + dir * L;
    p.stroke(...col); p.strokeWeight(2.5 * U); p.line(x, y0, x, y2);
    p.line(x, y2, x - 5 * U, y2 - dir * 8 * U); p.line(x, y2, x + 5 * U, y2 - dir * 8 * U);
    lab(name, x + 8 * U, y0 + dir * L * 0.5 + fh * 0.36, 'l', fh, col);
  }

  // --- the force diagram: the jumper as a plain rectangle; G from the centre, F_v from the face the air presses on ---
  function diagram(P, G, fh) {
    p.noStroke(); p.fill(255);
    if (narrow) { p.rect(0, 0, 600, HN.dia); p.stroke(220); p.strokeWeight(1); p.line(0, 0, 600, 0); }
    else { p.rect(406, 0, 194, 400); p.stroke(220); p.strokeWeight(1); p.line(406, 0, 406, 400); }
    lab(__('voimakuvio'), narrow ? 10 : 414, fh + 4, 'l', fh, INKC);
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2); p.rect(D.x - D.w / 2, D.y - D.h / 2, D.w, D.h);
    arrow(D.x, D.y, G * S, 1, '$\\overline{G}$', fh, 'r');
    if (open > 0) arrow(D.x - 16, D.y - D.h / 2, Fv * S, -1, '$\\overline{F}_\\text{v}$', fh, 'l', false);   // the canopy pulls up from above
    else arrow(D.x - 16, D.y + D.h / 2, Fv * S, -1, '$\\overline{F}_\\text{v}$', fh, 'l', true);           // the air presses on the lower face
  }
  function arrow(x, y0, len, dir, name, fh, side, push) {                 // dir 1 = down, −1 = up; push: the arrow ends at y0, coming from outside
    if (len < 1) return;
    const room = push || dir > 0 ? (narrow ? HN.dia : 400) - 10 - y0 : y0 - D.top;
    const cut = len > room, L = Math.min(len, room);
    const ya = push ? y0 - dir * L : y0, y2 = push ? y0 : y0 + dir * L;   // tail and tip
    const H = Math.min(11 * U, L * 0.7);
    p.stroke(...RED); p.strokeWeight(3.5 * U); p.line(x, ya, x, y2 - dir * H * 0.8);
    p.noStroke(); p.fill(...RED); p.triangle(x, y2, x - H * 0.42, y2 - dir * H, x + H * 0.42, y2 - dir * H);
    if (cut) {                                                             // two slanted strokes on a white gap: the arrow goes on
      const ym = (ya + y2) / 2; p.stroke(255); p.strokeWeight(6 * U); p.line(x - 7, ym + 3, x + 7, ym - 3);
      p.stroke(...RED); p.strokeWeight(1.5 * U); p.line(x - 8, ym, x + 8, ym - 6); p.line(x - 8, ym + 6, x + 8, ym);
    }
    const end = push ? ya : y2, below = push ? dir < 0 : dir > 0;          // label at the free end, away from the body
    const lx = side === 'r' ? x + 10 * U : x - 10 * U, ly = below ? end - fh * 0.2 : end + fh * 0.9;
    lab(name, lx, ly, side === 'r' ? 'l' : 'r', fh, RED);
  }

  // --- the (t, v) graph: the samples so far as a blue line, the current point highlighted ---
  function graph(fh, kk) {
    const PH = narrow ? HN.gra : 400 - SH, X = (tt) => GR.x0 + tt / TEND * (GR.x1 - GR.x0), Y = (vv) => GR.y0 - vv / 100 * (GR.y0 - GR.y1);
    p.noStroke(); p.fill(255); p.rect(0, 0, W, PH);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, W, 0);
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let i = 1; i <= 8; i++) p.line(X(i * 5), Y(0), X(i * 5), Y(100));
    for (let j = 1; j <= 5; j++) p.line(X(0), Y(j * 20), X(TEND), Y(j * 20));
    p.stroke(...INKC); p.strokeWeight(2 * U);
    p.line(X(0), Y(0), X(TEND) + 12, Y(0)); p.line(X(0), Y(0), X(0), Y(100) - 12);
    p.noStroke(); p.fill(...INKC);
    p.triangle(X(TEND) + 18, Y(0), X(TEND) + 9, Y(0) - 4, X(TEND) + 9, Y(0) + 4); p.triangle(X(0), Y(100) - 18, X(0) - 4, Y(100) - 9, X(0) + 4, Y(100) - 9);
    const vt = kk > 1.5 ? [50, 100] : [20, 40, 60, 80, 100];
    for (const j of vt) lab(`$${j}$`, X(0) - 6, Y(j) + fh * 0.36, 'r', fh, MUTEDC);
    const tt = kk > 1.5 && !narrow ? [20, 40] : [10, 20, 30, 40];
    for (const s of tt) lab(`$${s}$`, X(s), Y(0) + fh * 1.25, 'c', fh, MUTEDC);
    lab('$0$', X(0) - 6, Y(0) + fh * 1.25, 'r', fh, MUTEDC);
    lab('$v\\ (\\text{m/s})$', X(0) + 8, Y(100) - 12 - fh * 0.2, 'l', fh, INKC);
    lab('$t\\ (\\text{s})$', W - 6, Y(0) - fh * 0.6, 'r', fh, INKC);
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(2.5 * U); p.beginShape();
    for (const [a1, b1] of samples) if (a1 <= t + 1e-9) p.vertex(X(a1), Y(b1));
    if (t > samples[samples.length - 1][0]) p.vertex(X(t), Y(v));
    p.endShape();
    p.noStroke(); p.fill(...BLUE); p.circle(X(t), Y(v), 8 * U); p.fill(255); p.circle(X(t), Y(v), 3 * U);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, yy, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, yy);
    labels.push({ s, x0, y0: OY + yy - 0.75 * size, x1: x0 + w, y1: OY + yy + 0.25 * size });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
