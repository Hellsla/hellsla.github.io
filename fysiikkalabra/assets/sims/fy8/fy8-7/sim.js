// fy8-7 Laser ja kvanttirakenteet: a laser medium between two mirrors, pumped with power P_p (0-5,0 W).
// Model (rate equations, steady state, populations as fractions of all atoms; lessons/FY8/fy8-7/lesson-answers.py):
// spontaneous lifetime of the upper laser level tau = 1,0 ms, pump rate W = P_p / (1 W · tau).
// Three levels (ruby-like: ground 1, short-lived pump level 3 empties at once into the long-lived level 2, laser 2 -> 1):
//   below threshold n2 = W tau / (1 + W tau); with the mirrors the laser starts when n2 - n1 exceeds D = 0,10 and the
//   inversion stays clamped there (n2 = 0,55); the output is P_out = 100 mW · (W tau n1 - n2). Without the mirrors no
//   light makes enough passes (D = 1, never reached): inversion without a beam.
// Two levels: the pump light stimulates emission as often as it excites, n2 = W tau / (1 + 2 W tau) < 1/2: never an
// inversion, never a beam.
// The values are evaluated at once from the controls; the animation (atoms flipping, photons bouncing between the
// mirrors, the beam) only shows them, and the speed select changes its pace. Every canvas text goes through lab(),
// which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const D_MIRROR = 0.10, K_OUT = 100, PMAX = 5, NA = 36;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203], LASER = [201, 42, 42],
        LASERL = [242, 166, 156], HEATC = [232, 89, 12], HEATL = [255, 192, 120], COLDC = [25, 113, 194], COLDL = [208, 230, 251],
        PUMP = [43, 138, 62], PUMPL = [178, 242, 187], PAPERC = [246, 241, 230], METAL = [138, 150, 163], GLASSC = [238, 245, 249];
  // panels: cavity on top, the levels with their populations and the P_out(P_p) graph below (wide: side by side,
  // narrow sim-root < 500 px: stacked at double scale)
  const WIDE = { H: 400, cav: { ox: 0, oy: 0, s: 1 }, lev: { ox: 0, oy: 200, s: 1 }, gr: { ox: 300, oy: 200, s: 1 } };
  const NARROW = { H: 1000, cav: { ox: 0, oy: 20, s: 1 }, lev: { ox: 0, oy: 230, s: 2 }, gr: { ox: 0, oy: 620, s: 2 } };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let selLevels, selMirrors, slP, lP, selSpeed, btnRun, readout, running = true;
  let atoms = [], cavPh = [], spont = [], pumpPh = [], clock = 0;

  // seeded random numbers (mulberry32): the atoms' places are the same on every load
  function rng(s) {
    let a = s >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return (((t ^ (t >>> 14)) >>> 0) + 0.5) / 4294967297; };
  }
  const R = rng(7);

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnRun = p.createButton(__('pysayta')).parent(controls);
    btnRun.elt.addEventListener('click', () => { running = !running; btnRun.html(running ? __('pysayta') : __('jatka')); });
    const lv = p.createElement('label').parent(controls); p.createSpan(__('aine')).parent(lv); selLevels = p.createSelect().parent(lv);
    selLevels.option(__('kolme'), '3'); selLevels.option(__('kaksi'), '2'); selLevels.selected('3');
    const lm = p.createElement('label').parent(controls); p.createSpan(__('peilit')).parent(lm); selMirrors = p.createSelect().parent(lm);
    selMirrors.option(__('peilit_on'), '1'); selMirrors.option(__('peilit_off'), '0'); selMirrors.selected('1');
    const lp = p.createElement('label').parent(controls); lP = p.createSpan('').parent(lp); slP = p.createSlider(0, PMAX, 0.5, 0.1).parent(lp);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    for (let i = 0; i < NA; i++) {
      const col = i % 12, row = Math.floor(i / 12);
      atoms.push({ x: 84 + col * 26 + (R() - 0.5) * 10, y: 76 + row * 24 + (R() - 0.5) * 8, up: false, flash: 0 });
    }
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { levels: { input: selLevels.elt, unit: '' }, mirrors: { input: selMirrors.elt, unit: '' }, P: { input: slP.elt, unit: 'W' } },
      reset: () => { selLevels.selected('3'); selMirrors.selected('1'); slP.value(0.5); cavPh = []; spont = []; pumpPh = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  // the steady state of the controls: populations in %, the beam's power in mW
  function model(P, levels, mirrors) {
    const w = P;                                    // W tau = P_p / 1 W
    if (levels === 2) { const n2 = w / (1 + 2 * w); return { n2: 100 * n2, n1: 100 * (1 - n2), Pout: 0 }; }
    let n2 = w / (1 + w);
    if (mirrors && 2 * n2 - 1 > D_MIRROR) {
      n2 = (1 + D_MIRROR) / 2;
      return { n2: 100 * n2, n1: 100 * (1 - n2), Pout: K_OUT * (w * (1 - n2) - n2) };
    }
    return { n2: 100 * n2, n1: 100 * (1 - n2), Pout: 0 };
  }
  function state() {
    const levels = Number(selLevels.value()), mirrors = Number(selMirrors.value()), P = Math.round(Number(slP.value()) * 10) / 10;
    const M = model(P, levels, mirrors);
    return { levels, mirrors, P, n2: M.n2, n1: M.n1, Pout: M.Pout, inv: M.n2 > M.n1 + 1e-9 ? 1 : 0, lasing: M.Pout > 1e-9 ? 1 : 0 };
  }

  p.draw = () => {
    const S = state();
    const dt = running ? Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()) : 0;
    clock += dt;
    animate(S, dt);
    lP.html(__('pumppaus', { P: tx(S.P, 1) }));
    readout.html(__('lukemat', { n2: tx(S.n2, 1), n1: tx(S.n1, 1), inv: S.inv ? __('kylla') : __('ei'), P: tx(S.Pout, 0) }));
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 13; G = narrow ? NARROW : WIDE;
    window.simState = { levels: S.levels, mirrors: S.mirrors, P: S.P, n2: S.n2, n1: S.n1, inv: S.inv, Pout: S.Pout, lasing: S.lasing,
                        photons: cavPh.length, running: running ? 1 : 0, labels: null };
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G === WIDE ? 196 : 226, [PAPERC, [255, 255, 255]]);
    cavity(S); levelsPanel(S); graph(S);
    window.simState.labels = labels;
  };

  // --- the animation: as many excited atoms as the model says, random swaps (a decay and a pump excitation),
  // photons along the axis while the laser runs, short spontaneous photons in random directions ---
  function animate(S, dt) {
    const want = Math.round(S.n2 / 100 * NA);
    let up = atoms.filter((a) => a.up);
    while (up.length > want) { const a = up[Math.floor(R() * up.length)]; a.up = false; up = atoms.filter((b) => b.up); }
    let down = atoms.filter((a) => !a.up);
    while (up.length < want && down.length) { const a = down[Math.floor(R() * down.length)]; a.up = true; a.flash = 0.4; up.push(a); down = atoms.filter((b) => !b.up); }
    for (const a of atoms) a.flash = Math.max(0, a.flash - dt);
    if (dt > 0 && S.P > 0 && up.length && down.length && R() < dt * (2 + 2 * S.P)) {
      const a = up[Math.floor(R() * up.length)], b = down[Math.floor(R() * down.length)];
      a.up = false; b.up = true; b.flash = 0.4;
      if (!S.lasing || R() < 0.3) { const th = R() * 2 * Math.PI; spont.push({ x: a.x, y: a.y, th, t: 0 }); }
      pumpPh.push({ x: b.x, t: 0 });
    }
    for (const s of spont) s.t += dt;
    spont = spont.filter((s) => s.t < 0.7);
    for (const q of pumpPh) q.t += dt;
    pumpPh = pumpPh.filter((q) => q.t < 0.35);
    const target = S.lasing ? Math.min(18, 3 + Math.round(15 * S.Pout / 170)) : 0;
    while (cavPh.length < target) cavPh.push({ x: 70 + R() * 330, dir: R() < 0.5 ? 1 : -1, y: 82 + Math.floor(R() * 4) * 12 });
    while (cavPh.length > target) cavPh.pop();
    for (const q of cavPh) {
      q.x += q.dir * 240 * dt;
      if (q.x > 404) { q.x = 404 - (q.x - 404); q.dir = -1; }
      if (q.x < 64) { q.x = 64 + (64 - q.x); q.dir = 1; }
    }
  }

  // --- the cavity: mirrors, the rod with its atoms, the pump lamp, photons and the beam ---
  function cavity(S) {
    const C = G.cav, X = (x) => C.ox + C.s * x, Y = (y) => C.oy + C.s * y;
    const glow = S.P / PMAX;
    // pump lamp under the rod
    p.noStroke(); p.fill(...PUMPL, 60 + 195 * glow); p.rect(X(70), Y(150), 330, 18, 9);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(X(70), Y(150), 330, 18, 9);
    for (const q of pumpPh) {
      const yy = Y(146) - (Y(146) - Y(136)) * (q.t / 0.35);
      p.stroke(...PUMP); p.strokeWeight(2.5 * sk); p.line(q.x, yy + 8, q.x, yy);
      p.noStroke(); p.fill(...PUMP); p.triangle(q.x, yy - 6, q.x - 4, yy + 1, q.x + 4, yy + 1);
    }
    // the rod
    grect(X(60), Y(62), 346, 72, [[255, 255, 255], LASERL.map((v) => v + (255 - v) * 0.4), [255, 255, 255]]);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(X(60), Y(62), 346, 72, 8);
    // atoms: excited = filled orange with a ring, ground = light blue
    for (const a of atoms) {
      if (a.up) {
        p.noStroke(); p.fill(...HEATL, 140); p.circle(a.x, Y(a.y), 17 * Math.min(sk, 1.3));
        p.fill(...HEATC); p.stroke(255); p.strokeWeight(1.5); p.circle(a.x, Y(a.y), 10 * Math.min(sk, 1.3));
      } else {
        p.fill(...COLDL); p.stroke(...COLDC); p.strokeWeight(1.5); p.circle(a.x, Y(a.y), 10 * Math.min(sk, 1.3));
      }
    }
    // spontaneous photons, in random directions, fading
    for (const s of spont) {
      const d = 8 + s.t * 60, x1 = s.x + d * Math.cos(s.th), y1 = Y(s.y) + d * Math.sin(s.th);
      wave(x1, y1, x1 + 16 * Math.cos(s.th), y1 + 16 * Math.sin(s.th), LASER, 255 * (1 - s.t / 0.7), 1.6);
    }
    // photons along the axis
    for (const q of cavPh) wave(q.x - 9 * q.dir, Y(q.y), q.x + 9 * q.dir, Y(q.y), LASER, 255, 2.2);
    // mirrors
    const mA = S.mirrors ? 255 : 60;
    p.stroke(...INKC, mA); p.strokeWeight(2 * sk); p.fill(...METAL, mA); p.rect(X(40), Y(50), 12, 96, 3);
    p.fill(...GLASSC, mA); p.rect(X(414), Y(50), 9, 96, 3);
    p.stroke(...METAL, mA); p.strokeWeight(3); p.line(X(418.5), Y(54), X(418.5), Y(142));
    // the beam out of the partial mirror
    if (S.lasing) {
      const w = (2 + 6 * S.Pout / 170) * sk;
      p.noStroke(); p.fill(...LASERL, 150); p.rect(X(423), Y(98) - w, 160, 2 * w);
      p.fill(...LASER); p.rect(X(423), Y(98) - w / 2, 160, w);
      for (let k = 0; k < 3; k++) {
        const x = X(430) + ((clock * 240 + k * 53) % 150);
        wave(x, Y(98), x + 18, Y(98), [255, 255, 255], 200, 1.6);
      }
      lab('$\\text{' + __('sade') + '}$', X(588), Y(124) + 0.36 * fh, 'r', LASER);
    }
    lab(S.mirrors ? '$\\text{' + __('peili') + '}\\ 100\\,\\%$' : '$\\text{' + __('eipeilia') + '}$', X(46), Y(50) - 14 * sk + 0.36 * fh - 0.25 * fh, 'c', INKC);
    if (S.mirrors) lab('$\\text{' + __('peili') + '}\\ 99\\,\\%$', X(418), Y(50) - 14 * sk + 0.36 * fh - 0.25 * fh, 'c', INKC);
    lab('$\\text{' + __('pumppauslamppu') + '}$', X(235), Y(186) + 0.36 * fh, 'c', PUMP);
  }

  // --- the energy levels with a population bar on each laser level ---
  function levelsPanel(S) {
    const C = G.lev, X = (x) => C.ox + C.s * x, Y = (y) => C.oy + C.s * y;
    const y1 = 170, y2 = 98, y3 = 34, x0 = 52, L = 112;
    p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    p.line(X(x0), Y(y1), X(x0 + L + 8), Y(y1)); p.line(X(x0), Y(y2), X(x0 + L + 8), Y(y2));
    lab('$E_1$', X(x0 - 8), Y(y1) + 0.36 * fh, 'r', INKC); lab('$E_2$', X(x0 - 8), Y(y2) + 0.36 * fh, 'r', INKC);
    if (S.levels === 3) {
      p.stroke(...MUTEDC); p.strokeWeight(2 * sk); p.line(X(x0), Y(y3), X(x0 + L + 8), Y(y3));
      lab('$E_3$', X(x0 - 8), Y(y3) + 0.36 * fh, 'r', MUTEDC);
      dashedV(X(x0 + L + 2), Y(y3 + 4), Y(y2 - 6), MUTEDC);
    }
    // the 50 % mark
    dashedV(X(x0 + L / 2), Y(y2 - 30), Y(y1 + 4), MUTEDC);
    lab('$50\\,\\%$', X(x0 + L / 2), Y(y2 - 40) + 0.36 * fh, 'c', MUTEDC);
    // bars: share of atoms on the level
    const bar = (y, v, col, edge) => {
      p.noStroke(); p.fill(...col); p.rect(X(x0), Y(y - 20), C.s * L * v / 100, C.s * 16, 2 * sk);
      p.noFill(); p.stroke(...edge); p.strokeWeight(1.5 * sk); p.rect(X(x0), Y(y - 20), C.s * L, C.s * 16, 2 * sk);
    };
    bar(y2, S.n2, HEATC, HEATC); bar(y1, S.n1, COLDC, COLDC);
    lab('$N_2 = ' + tx(S.n2, 0) + '\\,\\%$', X(x0 + L + 14), Y(y2 - 12) + 0.36 * fh, 'l', HEATC);
    lab('$N_1 = ' + tx(S.n1, 0) + '\\,\\%$', X(x0 + L + 14), Y(y1 - 12) + 0.36 * fh, 'l', COLDC);
  }

  // --- P_out against P_p: the model curve faint, the current point marked ---
  function graph(S) {
    const C = G.gr, X = (x) => C.ox + C.s * x, Y = (y) => C.oy + C.s * y;
    const gx0 = 52, gy0 = 166, gx1 = 262, gy1 = 30, PY = 200;
    const px = (P) => X(gx0 + (gx1 - gx0) * P / PMAX), py = (v) => Y(gy0 - (gy0 - gy1) * v / PY);
    p.strokeWeight(1.2 * sk); p.stroke(...GRID);
    for (let P = 1; P <= 5; P++) p.line(px(P), Y(gy0), px(P), Y(gy1));
    for (let v = 50; v <= PY; v += 50) p.line(X(gx0), py(v), X(gx1), py(v));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    p.line(X(gx0), Y(gy0), X(gx1 + 16), Y(gy0)); p.line(X(gx0), Y(gy0), X(gx0), Y(gy1 - 14));
    p.noStroke(); p.fill(...INKC);
    p.triangle(X(gx1 + 24), Y(gy0), X(gx1 + 13), Y(gy0) - 5 * sk, X(gx1 + 13), Y(gy0) + 5 * sk);
    p.triangle(X(gx0), Y(gy1 - 22), X(gx0) - 5 * sk, Y(gy1 - 11), X(gx0) + 5 * sk, Y(gy1 - 11));
    const every = sk > 1.5 ? 2 : 1;
    for (let P = 1; P <= 5; P++) {
      p.stroke(...INKC); p.strokeWeight(1.8 * sk); p.line(px(P), Y(gy0), px(P), Y(gy0) + 5 * sk);
      if (P % every === 0 || every === 1) lab('$' + P + '$', px(P), Y(gy0) + 5 * sk + 1.05 * fh, 'c', MUTEDC);
    }
    for (let v = 50; v <= PY; v += 50) {
      p.stroke(...INKC); p.strokeWeight(1.8 * sk); p.line(X(gx0) - 5 * sk, py(v), X(gx0), py(v));
      if ((v / 50) % every === 0 || every === 1) lab('$' + v + '$', X(gx0) - 8 * sk, py(v) + 0.36 * fh, 'r', MUTEDC);
    }
    lab('$0$', X(gx0) - 8 * sk, Y(gy0) + 5 * sk + 1.05 * fh, 'r', MUTEDC);
    lab('$P_\\text{p}\\ (\\text{W})$', X(gx1 + 4), Y(gy0) - 0.75 * fh, 'r', INKC);
    lab(__('akseli_ulos'), X(gx0) + 10 * sk, Y(gy1 - 16) + 0.36 * fh, 'l', INKC);
    // the model curve for the chosen medium and mirrors
    p.noFill(); p.stroke(...LASER, 90); p.strokeWeight(3 * sk); p.beginShape();
    for (let i = 0; i <= 100; i++) { const P = PMAX * i / 100; p.vertex(px(P), py(model(P, S.levels, S.mirrors).Pout)); }
    p.endShape();
    p.fill(...LASER); p.stroke(255); p.strokeWeight(2 * sk); p.circle(px(S.P), py(S.Pout), 11 * sk);
  }

  function wave(x1, y1, x2, y2, col, alpha, w) {
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, px = -uy, py = ux;
    p.noFill(); p.stroke(...col, alpha); p.strokeWeight(w * sk); p.beginShape();
    for (let i = 0; i <= 16; i++) { const t = i / 16 * L, s = 3 * sk * Math.sin(2 * Math.PI * 1.5 * t / L); p.vertex(x1 + ux * t + px * s, y1 + uy * t + py * s); }
    p.endShape();
    p.noStroke(); p.fill(...col, alpha); p.triangle(x2 + ux * 4 * sk, y2 + uy * 4 * sk, x2 + px * 3 * sk, y2 + py * 3 * sk, x2 - px * 3 * sk, y2 - py * 3 * sk);
  }
  function dashedV(x, ya, yb, col) {
    p.stroke(...col); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 4 * sk]); p.line(x, ya, x, yb); p.drawingContext.setLineDash([]);
  }
  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  function grect(x, y, w, hh, stops) {
    const cx = p.drawingContext; cx.save(); const gr = cx.createLinearGradient(x, y, x, y + hh);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.map(Math.round).join(',')})`));
    cx.fillStyle = gr; cx.fillRect(x, y, w, hh); cx.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (err) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
