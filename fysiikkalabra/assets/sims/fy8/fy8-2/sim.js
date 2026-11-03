// fy8-2 Spektrit paljastavat atomin energiatasot: the hydrogen atom's energy levels E_n = -13,6 eV / n² (data, FY8
// scope) and one transition between an upper level n_y and a lower level n_a. Emission: the atom drops from n_y to n_a
// and a photon of energy ΔE = E_y - E_a leaves the glowing gas for the spectroscope. Absorption: white light passes
// hydrogen gas (cold when n_a = 1, hot when n_a > 1); a photon of exactly ΔE is absorbed and the atom rises from n_a to n_y. λ = hc/ΔE with h = 6,626e-34 J s,
// c = 2,998e8 m/s, 1 eV = 1,602e-19 J (the lesson's constants). Every transition the student tries is kept as a line
// on the spectrum strip (80–900 nm) of the current mode, so the spectrum builds up from single transitions. The pace
// of the animation is only a picture; the speed select scales it and changes no value. Every canvas text goes through
// lab(), which pushes its box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const HC = 6.626e-34 * 2.998e8 / 1.602e-19 * 1e9;   // eV·nm
  const En = (k) => -13.6 / (k * k);
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], GLASSC = [238, 245, 249], COLDC = [25, 113, 194],
        IRONC = [108, 117, 125], ALU = [196, 204, 212], EDGE = [138, 150, 163], HOTL = [242, 166, 156], HEATL = [255, 192, 120],
        PAPERC = [246, 241, 230];
  const WIDE = { H: 400, xl: 72, xr: 228, xa: 150, y0: 36, ppe: 15.6, elab: 66, nlab: 236, tx: 8, ty: 16,
                 bx: 300, by: 20, bs: 1, sx0: 40, sx1: 560, rl: 286, st: 294, sh: 40, nb: 356, tb: 384 };
  const NARROW = { H: 860, xl: 160, xr: 440, xa: 300, y0: 60, ppe: 22, elab: 150, nlab: 450, tx: 10, ty: 26,
                   bx: 60, by: 370, bs: 1.6, sx0: 40, sx1: 560, rl: 690, st: 702, sh: 56, nb: 798, tb: 836 };
  let G = WIDE, sk = 1, fh = 13, labels = [], phase = 0;
  let selMode, selNy, selNa, selSpeed, readout;
  const seen = { emissio: new Map(), absorptio: new Map() };

  const state = () => {
    const mode = selMode.value(), ny = Number(selNy.value()), na = Number(selNa.value());
    const Ey = En(ny), Ea = En(na), valid = ny > na, dE = valid ? Ey - Ea : 0, lam = valid ? HC / dE : 0;
    const region = !valid ? '' : lam < 380 ? 'uv' : lam > 750 ? 'ir' : 'vis';
    return { mode, ny, na, Ey, Ea, valid, dE, lam, region };
  };
  // an upper level must lie above the lower one: the levels n_y ≤ n_a cannot be picked (an experiment that locks n_a
  // never records an empty transition)
  const syncNy = () => { for (const o of selNy.elt.options) o.disabled = Number(o.value) <= Number(selNa.value()); };
  const note = () => { const S = state(); if (S.valid) seen[S.mode].set(S.ny + '-' + S.na, S.lam); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('tila')).parent(l0); selMode = p.createSelect().parent(l0);
    selMode.option(__('emissio'), 'emissio'); selMode.option(__('absorptio'), 'absorptio'); selMode.selected('emissio');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('ylempi')).parent(l1); selNy = p.createSelect().parent(l1);
    for (let k = 2; k <= 6; k++) selNy.option(String(k), String(k));
    selNy.selected('3');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('alempi')).parent(l2); selNa = p.createSelect().parent(l2);
    for (let k = 1; k <= 4; k++) selNa.option(String(k), String(k));
    selNa.selected('2');
    syncNy();
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l3); selSpeed = p.createSelect().parent(l3);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const bClear = p.createButton(__('tyhjenna')).parent(controls);
    bClear.elt.addEventListener('click', () => { seen[selMode.value()].clear(); });
    for (const s of [selMode, selNy, selNa]) s.changed(() => { phase = 0; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tila: { input: selMode.elt, unit: '' }, ny: { input: selNy.elt, unit: '' }, na: { input: selNa.elt, unit: '' } },
      reset: () => { selMode.selected('emissio'); selNy.selected('3'); selNa.selected('2'); seen.emissio.clear(); seen.absorptio.clear(); phase = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    phase = (phase + Math.min(p.deltaTime, 100) / 3000 * Number(selSpeed.value())) % 1;   // one cycle in 3 s at normal pace
    syncNy();
    note();   // the drawn transition joins the strip; settings made between two frames (an experiment's setup) never do
    const S = state();
    readout.html(S.valid
      ? __('lukemat', { Ey: tx(S.Ey, 2), Ea: tx(S.Ea, 2), dE: tx(S.dE, 2), lam: tx(S.lam, 0), alue: __('alue_' + S.region) })
      : __('virhe'));
    window.simState = { mode: S.mode, ny: S.ny, na: S.na, Ey: S.Ey, Ea: S.Ea, valid: S.valid ? 1 : 0, dE: S.dE, lam: S.lam,
                        visible: S.region === 'vis' ? 1 : 0, region: S.region, lines: seen[S.mode].size, phase, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    p.noStroke(); p.fill(...PAPERC); p.rect(0, 0, 600, G.rl - 22 * (narrow ? 1.4 : 1));
    diagram(S);
    apparatus(S);
    spectrum(S);
    window.simState.labels = labels;
  };

  const Y = (E) => G.y0 + (-E) * G.ppe;
  // electron's level and the photon's progress in the cycle: the jump happens at 0,45
  const jumped = () => phase >= 0.45;

  function diagram(S) {
    const { xl, xr, xa } = G;
    lab('$E\\,(\\text{eV})$', G.tx, G.ty, 'l');
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([6 * sk, 5 * sk]); p.line(xl, Y(0), xr, Y(0)); p.drawingContext.setLineDash([]);
    for (let k = 1; k <= 6; k++) {
      const sel = S.valid && (k === S.ny || k === S.na);
      p.stroke(...(sel ? INKC : MUTEDC)); p.strokeWeight((sel ? 3.5 : 2) * sk); p.line(xl, Y(En(k)), xr, Y(En(k)));
    }
    const yc = (E) => Y(E) + 0.36 * fh;
    lab('$0$', G.elab, yc(0), 'r');
    if (G === WIDE) lab('$-1{,}51$', G.elab, yc(En(3)), 'r');   // on a phone the readout gives it: no room beside 0
    lab('$-3{,}40$', G.elab, yc(En(2)), 'r');
    lab('$-13{,}6$', G.elab, yc(En(1)), 'r');
    lab('$n = 1$', G.nlab, yc(En(1)), 'l');
    lab('$n = 2$', G.nlab, yc(En(2)), 'l');
    lab('$n = 3$', G.nlab, yc(En(3)) + 2 * sk, 'l');
    lab('$n = 4, 5, 6$', G.nlab, G === WIDE ? yc(0) - 4 : yc(0) - 0.9 * fh, 'l');
    if (!S.valid) return;
    const col = lineColour(S.lam), yU = Y(S.Ey), yL = Y(S.Ea);
    const down = S.mode === 'emissio';
    // the transition arrow: down for emission, up for absorption, drawn once the jump has happened
    const a0 = down ? yU : yL, a1 = down ? yL : yU;
    p.stroke(...col, jumped() ? 255 : 90); p.strokeWeight(4 * sk);
    p.line(xa, a0, xa, a1 + (down ? -10 : 10) * sk);
    p.noStroke(); p.fill(...col, jumped() ? 255 : 90);
    const d = down ? 1 : -1;
    p.triangle(xa, a1, xa - 7 * sk, a1 - d * 14 * sk, xa + 7 * sk, a1 - d * 14 * sk);
    // the electron: on the start level before the jump, on the end level after it
    const yE = down ? (jumped() ? yL : yU) : (jumped() ? yU : yL);
    p.fill(...COLDC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(xa + 26 * sk, yE, 12 * sk);
  }

  // the apparatus in local coordinates (u 0–300, v 0–190), scaled by bs
  const U = (u) => G.bx + u * G.bs, V = (v) => G.by + v * G.bs;
  function apparatus(S) {
    const s = G.bs, em = S.mode === 'emissio', col = S.valid ? lineColour(S.lam) : MUTEDC;
    // spectroscope: a box with a slit
    p.fill(...IRONC); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(U(210), V(60), 76 * s, 50 * s, 5 * s);
    p.fill(...INKC); p.noStroke(); p.rect(U(210) - 3 * s, V(78), 6 * s, 14 * s);
    p.fill(...ALU); p.rect(U(262), V(68), 16 * s, 34 * s, 3 * s);
    lab('$\\text{' + __('spektroskooppi') + '}$', U(248), V(140), 'c');
    if (em) {
      // a glowing hydrogen tube
      p.fill(...HOTL); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(U(20), V(70), 120 * s, 30 * s, 15 * s);
      p.fill(...IRONC); p.rect(U(8), V(76), 14 * s, 18 * s, 2 * s); p.rect(U(138), V(76), 14 * s, 18 * s, 2 * s);
      lab('$\\text{' + __('kaasu_kuuma') + '}$', U(80), V(140), 'c');
    } else {
      // a lamp, a white beam, a cell of gas: cold when the atoms start in the ground state, hot otherwise
      p.noStroke(); p.fill(255, 255, 255, 230); p.rect(U(40), V(78), 170 * s, 14 * s);
      p.fill(...HEATL); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(U(30), V(85), 30 * s);
      p.fill(...GLASSC); p.stroke(...INKC); p.rect(U(90), V(58), 70 * s, 54 * s, 6 * s);
      p.noStroke(); p.fill(...COLDC);
      for (const [a, b] of [[102, 70], [120, 96], [138, 74], [148, 100], [110, 88], [132, 64]]) p.circle(U(a), V(b), 5 * s);
      lab('$\\text{' + __('lamppu') + '}$', U(30), V(140), 'c');
      lab('$\\text{' + __(S.na === 1 ? 'kaasu_kylma' : 'kaasu_kuuma') + '}$', U(125), V(140) + (G === WIDE ? 0 : 1.5 * fh), 'c');   // a row lower on a phone
    }
    if (!S.valid) return;
    // the photon: a short wavy packet with an arrowhead; emission: after the jump, from the tube to the spectroscope;
    // absorption: before the jump, from the lamp into the cell, where it is absorbed
    let u = null;
    if (em && jumped()) u = 150 + (phase - 0.45) / 0.55 * 50;
    if (!em && !jumped()) u = 46 + phase / 0.45 * 70;
    if (u !== null) {
      const v = 85, Lw = 34;
      p.noFill(); p.stroke(...col); p.strokeWeight(3 * sk); p.beginShape();
      for (let i = 0; i <= 30; i++) { const t = i / 30; p.vertex(U(u + t * Lw), V(v + 6 * Math.sin(t * 2 * Math.PI * 2.5))); }
      p.endShape();
      p.noStroke(); p.fill(...col);
      p.triangle(U(u + Lw + 10), V(v), U(u + Lw), V(v - 6), U(u + Lw), V(v + 6));
    }
    lab('$hf$', U(em ? 180 : 70), V(48), 'c');
  }

  function spectrum(S) {
    const { sx0, sx1, st, sh } = G, lo = 80, hi = 900, X = (l) => sx0 + (l - lo) / (hi - lo) * (sx1 - sx0);
    const em = S.mode === 'emissio';
    lab('$\\text{UV}$', X(230), G.rl, 'c');
    lab('$\\text{' + __('nakyva') + '}$', X(565), G.rl, 'c');
    lab('$\\text{IR}$', X(830), G.rl, 'c');
    const c = p.drawingContext;
    if (em) { p.noStroke(); p.fill(...INKC); p.rect(sx0, st, sx1 - sx0, sh); }
    else {
      c.save(); const gr = c.createLinearGradient(sx0, 0, sx1, 0);
      for (let l = lo; l <= hi; l += 10) { const [r, g, b] = continuum(l); gr.addColorStop((l - lo) / (hi - lo), `rgb(${r},${g},${b})`); }
      c.fillStyle = gr; c.fillRect(sx0, st, sx1 - sx0, sh); c.restore();
    }
    // the visible band's edges
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); c.setLineDash([4 * sk, 4 * sk]);
    p.line(X(380), st - 6 * sk, X(380), st + sh + 6 * sk); p.line(X(750), st - 6 * sk, X(750), st + sh + 6 * sk); c.setLineDash([]);
    // the lines of the transitions tried in this mode; beyond 900 nm an arrow at the edge
    for (const lam of seen[S.mode].values()) {
      const x = X(Math.min(lam, hi)), w = 4 * sk;
      if (em) { p.noStroke(); p.fill(...lineColour(lam)); } else { p.noStroke(); p.fill(...INKC); }
      if (lam <= hi) p.rect(x - w / 2, st, w, sh);
      else { p.triangle(sx1 + 12 * sk, st + sh / 2, sx1 + 2 * sk, st + sh / 2 - 8 * sk, sx1 + 2 * sk, st + sh / 2 + 8 * sk); }
    }
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(sx0, st, sx1 - sx0, sh);
    // the current transition's marker under the strip
    if (S.valid) {
      const x = X(Math.min(S.lam, hi) ), yb = st + sh + 2 * sk;
      p.noStroke(); p.fill(...INKC); p.triangle(x, yb, x - 7 * sk, yb + 12 * sk, x + 7 * sk, yb + 12 * sk);
    }
    for (let l = 100; l <= 900; l += 100) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(X(l), st + sh, X(l), st + sh + 5 * sk);
      if (l % 200 === 100) lab('$' + l + '$', X(l), G.nb, 'c');
    }
    lab('$\\lambda\\,(\\text{nm})$', sx1, G.tb, 'r');
  }

  // the colour of light of wavelength lam (nm) (Bruton); ultraviolet and infrared, which the eye does not see, in grey
  function wl(lam) {
    let r = 0, g = 0, b = 0;
    if (lam < 440) { r = -(lam - 440) / 60; b = 1; } else if (lam < 490) { g = (lam - 440) / 50; b = 1; }
    else if (lam < 510) { g = 1; b = -(lam - 510) / 20; } else if (lam < 580) { r = (lam - 510) / 70; g = 1; }
    else if (lam < 645) { r = 1; g = -(lam - 645) / 65; } else r = 1;
    const f = lam < 420 ? 0.3 + 0.7 * (lam - 380) / 40 : lam > 700 ? 0.3 + 0.7 * (750 - lam) / 50 : 1;
    return [r, g, b].map((v) => Math.round(255 * Math.pow(Math.max(0, Math.min(1, v)) * f, 0.8)));
  }
  const lineColour = (lam) => (lam >= 380 && lam <= 750 ? wl(lam) : ALU);
  const continuum = (lam) => (lam < 380 ? [150, 156, 168] : lam > 750 ? [96, 100, 108] : wl(lam));

  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
