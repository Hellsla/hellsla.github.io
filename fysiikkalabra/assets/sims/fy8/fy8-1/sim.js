// fy8-1 Valosähköinen ilmiö ja fotoni: a lamp shines light of wavelength λ and relative intensity Iv (%) on a metal
// plate in a vacuum tube. The light arrives as photons of energy E = hf = hc/λ; the photon rate in the picture is
// 0,4 · Iv per second. One photon gives its whole energy to one electron: when E ≥ W (work function of the chosen
// metal) the electron leaves the plate with kinetic energy at most E_k,max = E − W (each electron in the picture
// gets a share 0,3–1 of it, the fastest E_k,max), otherwise nothing leaves, however bright the light. The panel on the
// right (below on a phone) draws the energies to scale: the photon's hf beside the electron's W + E_k,max.
// The speed select scales only the pace of the animation; every reading is a model value that does not depend on it.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const h = 6.626e-34, c = 2.998e8, e = 1.602e-19;
  const WORK = { Na: 2.28, Mg: 3.68, Zn: 4.31 };                        // work functions, eV
  const METAL = { Na: [196, 204, 212], Mg: [170, 180, 190], Zn: [138, 150, 163] };
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], GLASSC = [238, 245, 249],
        BLUE = [25, 113, 194], COPPERC = [184, 98, 45], EDGE = [138, 150, 163], UVC = [112, 72, 232];
  // picture: a 400 × 330 box drawn at (PX, PY) with scale S; panel: the energy bars
  const WIDE = { H: 400, PX: 0, PY: 35, S: 1, ax: 432, base: 360, per: 40, A: 448, B: 498, bw: 30, lx: 534, axLab: 52, step: 1 };
  const NARROW = { H: 850, PX: 0, PY: 0, S: 1.5, ax: 170, base: 820, per: 40, A: 200, B: 300, bw: 60, lx: 372, axLab: 520, step: 2 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let slL, slI, selM, selSpeed, lL, lI, readout, acc = 0;
  let photons = [], electrons = [];

  const params = () => ({ lam: Number(slL.value()), Iv: Number(slI.value()), m: selM.value() });
  const physics = (S) => {
    const EJ = h * c / (S.lam * 1e-9), E = EJ / e, W = WORK[S.m], emits = E >= W;
    return { EJ, E, W, emits, Ek: emits ? E - W : 0, f: c / (S.lam * 1e-9), n: emits ? 0.4 * S.Iv : 0 };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l1); slL = p.createSlider(200, 700, 405, 5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lI = p.createSpan('').parent(l2); slI = p.createSlider(0, 100, 50, 10).parent(l2);
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('metalli')).parent(l3); selM = p.createSelect().parent(l3);
    for (const k of ['Na', 'Mg', 'Zn']) selM.option(__('m' + k), k);
    selM.selected('Na');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    const clear = () => { photons = []; electrons = []; acc = 0; };
    for (const el of [slL, slI, selM]) el.elt.addEventListener('input', clear);
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { lambda: { input: slL.elt, unit: 'nm' }, I: { input: slI.elt, unit: '%' }, metal: { input: selM.elt, unit: '' } },
      reset: () => { slL.value(405); slI.value(50); selM.selected('Na'); clear(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params(), F = physics(S);
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    lL.html(__('aallonpituus', { l: String(S.lam) }));
    lI.html(__('intensiteetti', { I: String(S.Iv) }));
    const ek = F.emits ? __('ek', { Ek: tx(F.Ek, 2) }) : __('eiirtoa');
    readout.html(__('lukemat', { f: sci(F.f), E: tx(F.E, 2), EJ: sci(F.EJ), W: tx(F.W, 2), ek: ek, n: String(Math.round(F.n)) }));
    window.simState = { lambda: S.lam, I: S.Iv, metal: S.m, W: F.W, f: F.f, E: F.E, EJ: F.EJ, Ek: F.Ek, n: F.n,
                        emits: F.emits ? 1 : 0, photons: photons.length, electrons: electrons.length, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    step(S, F, dt);
    p.background(255);
    picture(S, F);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, 330 * G.S + 4, 600, 330 * G.S + 4); else p.line(404, 20, 404, 380);
    panel(F, S);
    window.simState.labels = labels;
    window.simState.photons = photons.length; window.simState.electrons = electrons.length;
  };

  // picture coordinates (400 × 330 box) to canvas
  const X = (x) => G.PX + x * G.S, Y = (y) => G.PY + y * G.S;
  const FACE = 78;                                        // the plate's lit face, x in the box

  function step(S, F, dt) {
    acc += 0.4 * S.Iv * dt;
    while (acc >= 1) {
      acc -= 1;
      photons.push({ x0: 160 + 50 * Math.random(), y0: 52, ty: 120 + 150 * Math.random(), s: 0 });
    }
    for (const ph of photons) {
      const L = Math.hypot(FACE - ph.x0, ph.ty - ph.y0);
      ph.s += 230 * dt / L;
      if (ph.s >= 1 && F.emits) {
        const ek = F.Ek * (0.3 + 0.7 * Math.random()), a = (Math.random() - 0.5) * 0.7, v = 40 + 150 * Math.sqrt(ek);
        electrons.push({ x: FACE + 4, y: ph.ty, vx: v * Math.cos(a), vy: v * Math.sin(a) });
      }
    }
    photons = photons.filter((ph) => ph.s < 1);
    for (const el of electrons) { el.x += el.vx * dt; el.y += el.vy * dt; }
    electrons = electrons.filter((el) => el.x < 356 && el.y > 76 && el.y < 296);
  }

  function lightColour(lam) {   // the colour of the light (approximate); ultraviolet as violet
    if (lam < 380) return UVC;
    let r, g, b;
    if (lam < 440) { r = (440 - lam) / 60; g = 0; b = 1; } else if (lam < 490) { r = 0; g = (lam - 440) / 50; b = 1; }
    else if (lam < 510) { r = 0; g = 1; b = (510 - lam) / 20; } else if (lam < 580) { r = (lam - 510) / 70; g = 1; b = 0; }
    else if (lam < 645) { r = 1; g = (645 - lam) / 65; b = 0; } else { r = 1; g = 0; b = 0; }
    const k = lam < 420 ? 0.3 + 0.7 * (lam - 380) / 40 : 1, to = (v) => (v > 0 ? 255 * Math.pow(v * k, 0.8) : 0);
    return [to(r) * 0.86, to(g) * 0.78, to(b) * 0.86];
  }

  function picture(S, F) {
    const col = lightColour(S.lam), s = G.S;
    // vacuum tube
    p.fill(...GLASSC); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(X(40), Y(70), 350 * s, 230 * s, 30 * s);
    // the light beam from the lamp's lens to the plate's lit face, faint, so the light visibly ends at the plate
    if (S.Iv > 0) {
      p.noStroke(); p.fill(...col, 28 + 0.5 * S.Iv);
      p.quad(X(158), Y(51), X(222), Y(51), X(FACE), Y(250), X(FACE), Y(110));
    }
    // emitter plate and collector
    p.fill(...METAL[S.m]); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(X(60), Y(110), 18 * s, 170 * s, 3 * s);
    p.fill(...COPPERC); p.rect(X(356), Y(110), 14 * s, 170 * s, 3 * s);
    // lamp: dark housing, a lens glowing in the light's colour
    p.noStroke(); p.fill(...col, 60); p.ellipse(X(190), Y(46), 120 * s, 40 * s);
    p.fill(...INKC); p.rect(X(150), Y(12), 80 * s, 32 * s, 6 * s);
    p.fill(...col); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.rect(X(158), Y(42), 64 * s, 9 * s, 3 * s);
    // photons: short wavy arrows travelling to the plate, wiggle period proportional to λ
    for (const ph of photons) {
      const x1 = ph.x0, y1 = ph.y0, L = Math.hypot(FACE - x1, ph.ty - y1), ux = (FACE - x1) / L, uy = (ph.ty - y1) / L;
      const tip = Math.min(1, ph.s) * L, len = Math.min(34, tip), per = S.lam / 40, amp = 4;
      p.noFill(); p.stroke(...col); p.strokeWeight(2.2 * sk); p.beginShape();
      for (let q = tip - len; q <= tip - 7; q += 1) {
        const a = amp * Math.sin(2 * Math.PI * q / per);
        p.vertex(X(x1 + ux * q - uy * a), Y(y1 + uy * q + ux * a));
      }
      p.endShape();
      const tx0 = x1 + ux * tip, ty0 = y1 + uy * tip;
      p.noStroke(); p.fill(...col);
      p.triangle(X(tx0), Y(ty0), X(tx0 - ux * 9 - uy * 5), Y(ty0 - uy * 9 + ux * 5), X(tx0 - ux * 9 + uy * 5), Y(ty0 - uy * 9 - ux * 5));
    }
    // electrons: blue dots with a short trail
    for (const el of electrons) {
      const v = Math.hypot(el.vx, el.vy);
      p.stroke(...BLUE, 110); p.strokeWeight(2 * sk); p.line(X(el.x), Y(el.y), X(el.x - el.vx / v * 12), Y(el.y - el.vy / v * 12));
      p.fill(...BLUE); p.stroke(255); p.strokeWeight(1.2 * sk); p.circle(X(el.x), Y(el.y), 9 * s);
    }
    lab('$\\lambda = ' + S.lam + '\\,\\text{nm}$', X(240), Y(28) + 0.36 * fh, 'l', INKC);
    lab('$hf$', X(118), Y(84) + 0.36 * fh, 'r', col);
    if (F.emits && S.Iv > 0) lab('$e^-$', X(88), Y(288) + 0.36 * fh, 'l', BLUE);
    lab('$\\text{' + __('m' + S.m) + '}$', X(69), Y(318) + 0.36 * fh, 'c', INKC);
  }

  // the energies to scale: photon hf beside the electron's W + E_k,max
  function panel(F, S) {
    const { ax, base, per, A, B, bw, lx } = G, top = base - 7 * per, Ycol = (E) => base - E * per;
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let E = 1; E <= 7; E++) p.line(ax, Ycol(E), B + bw + 4, Ycol(E));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ax, base, ax, top - 12 * sk); p.line(ax, base, B + bw + 8, base);
    p.noStroke(); p.fill(...INKC); p.triangle(ax, top - 24 * sk, ax - 6 * sk, top - 10 * sk, ax + 6 * sk, top - 10 * sk);
    for (let E = 0; E <= 7; E++) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ax - 6 * sk, Ycol(E), ax, Ycol(E));
      if (E % G.step === 0) lab('$' + E + '$', ax - 9 * sk, Ycol(E) + 0.36 * fh, 'r', INKC);
    }
    lab('$E\\ (\\text{eV})$', ax + 10 * sk, G.axLab, 'l', INKC);
    // photon bar
    const col = lightColour(S.lam);
    p.fill(...col); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.rect(A, Ycol(F.E), bw, F.E * per);
    lab('$hf$', A + bw / 2, Ycol(F.E) - 8 * sk, 'c', INKC);
    // electron column: W (metal), E_k,max (blue) on top when the photon frees an electron
    p.fill(...METAL[S.m]); p.stroke(...INKC); p.rect(B, Ycol(F.W), bw, F.W * per);
    lab('$W$', lx, Ycol(F.W / 2) + 0.36 * fh, 'l', INKC);
    if (F.emits) {
      p.fill(...BLUE); p.rect(B, Ycol(F.E), bw, F.Ek * per);
      lab('$E_\\text{k,max}$', lx, Math.min(Ycol(F.W + F.Ek / 2), Ycol(F.W) - 0.2 * fh) + 0.36 * fh, 'l', BLUE);
    } else {
      lab('$hf < W$', B + bw / 2, Ycol(F.W) - 8 * sk, 'c', INKC);
    }
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 4 * sk]);
    p.line(A + bw, Ycol(F.E), B, Ycol(F.E)); p.drawingContext.setLineDash([]);
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
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal")
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (err) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  function sci(x) {   // 4{,}91 \cdot 10^{-19}
    let ex = Math.floor(Math.log10(x)), m = x / 10 ** ex;
    if (Number(m.toFixed(2)) >= 10) { m /= 10; ex += 1; }
    return tx(m, 2) + ' \\cdot 10^{' + ex + '}';
  }
});
