// fy8-3 Vetyatomin energiatasot ja Bohrin malli: a hydrogen atom with the levels E_n = -13,6 eV / n² (given data).
// Emission: the electron drops from n_y (2–6) to n_a (1–3) and one photon leaves with hf = E_y - E_a, lambda = hc / hf;
// each finished transition adds its line to the spectrum strip below (UV, visible and IR zones, each on its own
// linear scale). Absorption: a photon of energy hf (0,50–14,50 eV) meets an atom in state n_a. It is absorbed when hf
// equals E_m - E_a for some m > n_a within 0,03 eV (levels up to n = 30), it ionises the atom when hf >= -E_a (the
// rest is the free electron's kinetic energy), otherwise it passes. The picture: Bohr's orbits (radii schematic, not
// n²), the level diagram to scale above a shortened gap below n = 2, the spectrum strip. The physics is evaluated at
// once from the controls; the animation (jump, photon flight) only shows it, and the speed select changes its pace.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const h = 6.626e-34, c = 2.998e8, e = 1.602e-19, E1 = 13.6, TOL = 0.03, NMAX = 30;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203], HOTC = [201, 42, 42],
        ELC = [25, 113, 194], HEATC = [232, 89, 12], PAPERC = [246, 241, 230], NUC = [201, 42, 42];
  const En = (n) => -E1 / (n * n);
  const lamNm = (eV) => h * c / (eV * e) * 1e9;
  // wide 600 x 400: Bohr picture left, level diagram right, spectrum below; narrow (sim-root < 500 px): stacked, 600 x 1056
  const WIDE = { H: 400, bx: 125, by: 158, r0: 14, dr: 19, ax: 330, eTop: 44, k: 60, gap0: 258, gap1: 268, y1: 282, l0: 340, l1: 500,
                 nx: 508, title: [338, 18], arrowX: 430, elX: 380, zy: 306, sy0: 316, sy1: 344, ty: 360, atY: 386, panel: [0, 0, 600, 296] };
  const NARROW = { H: 1056, bx: 300, by: 208, r0: 20, dr: 34, ax: 110, eTop: 474, k: 90, gap0: 802, gap1: 814, y1: 842, l0: 125, l1: 400,
                   nx: 432, title: [118, 446], arrowX: 300, elX: 200, zy: 888, sy0: 906, sy1: 950, ty: 978, atY: 1034, panel: [0, 0, 600, 868] };
  const ZONES = [{ name: 'uv', a: 90, b: 130, x0: 20, x1: 130, ticks: [100] },
                 { name: 'nakyva', a: 380, b: 700, x0: 150, x1: 450, ticks: [400, 500, 600, 700] },
                 { name: 'ir', a: 1000, b: 1900, x0: 480, x1: 580, ticks: [1500] }];
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let selMode, slNy, slNa, slE, selSpeed, btnGo, btnClear, lNy, lNa, lE, wrapNy, wrapE, readout;
  let anim = null, rest = null, spin = 0, lines = [];     // anim: {kind, t}; rest: the electron's level after a finished run

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnGo = p.createButton(__('siirtyma')).parent(controls); btnGo.elt.addEventListener('click', go);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('tilanne')).parent(lm); selMode = p.createSelect().parent(lm);
    selMode.option(__('emissio'), 'emis'); selMode.option(__('absorptio'), 'abs'); selMode.selected('emis');
    wrapNy = p.createElement('label').parent(controls); lNy = p.createSpan('').parent(wrapNy); slNy = p.createSlider(2, 6, 3, 1).parent(wrapNy);
    const la = p.createElement('label').parent(controls); lNa = p.createSpan('').parent(la); slNa = p.createSlider(1, 3, 2, 1).parent(la);
    wrapE = p.createElement('label').parent(controls); lE = p.createSpan('').parent(wrapE); slE = p.createSlider(0.5, 14.5, 10.2, 0.05).parent(wrapE);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    btnClear = p.createButton(__('tyhjenna')).parent(controls); btnClear.elt.addEventListener('click', () => { lines = []; });
    p.createP(__('selite')).parent('sim-root').class('note');
    for (const el of [selMode, slNy, slNa, slE]) { el.elt.addEventListener('input', changed); el.elt.addEventListener('change', changed); }
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { mode: { input: selMode.elt, unit: '' }, ny: { input: slNy.elt, unit: '' }, na: { input: slNa.elt, unit: '' }, Ef: { input: slE.elt, unit: 'eV' } },
      reset: () => { selMode.selected('emis'); slNy.value(3); slNa.value(2); slE.value(10.2); anim = null; rest = null; lines = []; changed(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function changed() { anim = null; rest = null; }

  // the physics of the current controls, evaluated at once
  function model() {
    const mode = selMode.value(), ny = Number(slNy.value()), na = Number(slNa.value()), Ef = Math.round(Number(slE.value()) * 100) / 100;
    const Ea = En(na);
    if (mode === 'emis') {
      const valid = ny > na ? 1 : 0, Ey = En(ny), dE = valid ? Ey - Ea : 0;
      return { mode, ny, na, Ef, Ey, Ea, dE, lambda: valid ? lamNm(dE) : 0, nEnd: valid ? na : ny, Ek: 0, valid };
    }
    let nEnd = na, Ek = 0;
    if (Ef >= -Ea - 1e-9) { nEnd = 0; Ek = Ef + Ea; }
    else for (let m = na + 1; m <= NMAX; m++) if (Math.abs(En(m) - Ea - Ef) <= TOL) { nEnd = m; break; }
    return { mode, ny, na, Ef, Ey: nEnd > 0 ? En(nEnd) : 0, Ea, dE: Ef, lambda: lamNm(Ef), nEnd, Ek, valid: 1 };
  }

  function go() {
    const S = model();
    if (!S.valid) return;
    anim = { kind: S.mode, t: 0, S }; rest = null;
  }

  p.draw = () => {
    const S = model();
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    spin = (spin + dt * 0.8) % (2 * Math.PI);
    if (anim) {
      anim.t += dt / 1.3;
      if (anim.t >= 2) {
        if (anim.kind === 'emis') { lines.push({ lambda: anim.S.lambda, ny: anim.S.ny, na: anim.S.na }); if (lines.length > 40) lines.shift(); rest = anim.S.na; }
        else rest = anim.S.nEnd;
        anim = null;
      }
    }
    const emis = S.mode === 'emis';
    wrapNy.style('display', emis ? '' : 'none'); wrapE.style('display', emis ? 'none' : '');
    btnGo.html(emis ? __('siirtyma') : __('laheta'));
    btnGo.elt.disabled = !S.valid;
    lNy.html(__('ylempi', { n: String(S.ny) }));
    lNa.html(emis ? __('alempi', { n: String(S.na) }) : __('alkutila', { n: String(S.na) }));
    lE.html(__('energia', { E: tx(S.Ef, 2) }));
    readout.html(emis ? (S.valid ? __('lukemat_emis', { ny: S.ny, na: S.na, Ey: tx(S.Ey, 3), Ea: tx(S.Ea, 3), dE: tx(S.dE, 3), L: tx(S.lambda, 1), alue: __(region(S.lambda)) })
                                 : __('ei_siirtymaa'))
                      : __('lukemat_abs', { E: tx(S.Ef, 2), L: tx(S.lambda, 1), Ea: tx(S.Ea, 3), tulos: outcome(S) }));
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 13; G = narrow ? NARROW : WIDE;
    window.simState = { mode: S.mode, ny: S.ny, na: S.na, Ef: S.Ef, Ey: S.Ey, Ea: S.Ea, dE: S.dE, lambda: S.lambda, nEnd: S.nEnd, Ek: S.Ek,
                        valid: S.valid, lines: lines.length, anim: anim ? anim.t : -1, labels: null };
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.panel[3], [PAPERC, [255, 255, 255]]);
    bohr(S); levels(S); spectrum(S);
    window.simState.labels = labels;
  };

  function region(l) { return l < 380 ? 'uv' : l <= 750 ? 'nakyva' : 'ir'; }
  function outcome(S) {
    if (S.nEnd === 0) return __('ionisoi', { Ek: tx(S.Ek, 2) });
    if (S.nEnd !== S.na) return __('absorboituu', { n: String(S.nEnd) });
    return __('lapi');
  }

  // where the electron is drawn now: a level number (0 = free) and, during a jump, a fraction between two levels
  function electronLevel(S) {
    if (anim) {
      const A = anim.S, t = anim.t;
      if (anim.kind === 'emis') return t < 1 ? { from: A.ny, to: A.na, u: ease(t) } : { from: A.na, to: A.na, u: 0 };
      if (t < 1) return { from: A.na, to: A.na, u: 0 };
      return { from: A.na, to: A.nEnd, u: ease(Math.min(1, t - 1)) };
    }
    if (rest !== null) return { from: rest, to: rest, u: 0 };
    return S.mode === 'emis' ? { from: S.ny, to: S.ny, u: 0 } : { from: S.na, to: S.na, u: 0 };
  }
  const ease = (t) => t * t * (3 - 2 * t);

  // --- Bohr's picture: nucleus, orbits n = 1…6 (schematic radii), the electron, the photon ---
  const R = (n) => (n === 0 ? G.r0 + G.dr * 5.9 : G.r0 + G.dr * (Math.min(n, 6) - 1) + (n > 6 ? G.dr * 0.35 : 0));
  function bohr(S) {
    const { bx, by } = G;
    for (let n = 1; n <= 6; n++) {
      p.noFill(); p.stroke(...(n === S.na ? INKC : RULEC)); p.strokeWeight((n === S.na ? 2.5 : 1.8) * sk);
      p.circle(bx, by, 2 * R(n));
      lab('$' + n + '$', bx, by + R(n) - 3 * sk, 'c', MUTEDC);
    }
    p.fill(...NUC); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.circle(bx, by, 11 * sk);
    const L = electronLevel(S);
    const r = R(L.from) + (R(L.to) - R(L.from)) * L.u, a = -0.7 - spin;
    const ex = bx + r * Math.cos(a), ey = by + r * Math.sin(a);
    // photon
    if (anim) {
      const A = anim.S, col = lineColour(A.lambda);
      if (anim.kind === 'emis' && anim.t >= 1) {
        const u = anim.t - 1, d0 = R(A.na) + 10 * sk, len = 70 * sk;
        const d = d0 + u * 150 * sk;
        wave(bx + d * Math.cos(a), by + d * Math.sin(a), bx + (d + len) * Math.cos(a), by + (d + len) * Math.sin(a), col);
      }
      if (anim.kind === 'abs') {
        const x0 = 8 * sk, tx0 = ex - 12 * sk, ty0 = ey;
        if (anim.t < 1) { const u = anim.t, xs = x0 + u * (tx0 - 60 * sk - x0); wave(xs, ty0, xs + 60 * sk, ty0, col); }
        else if (A.nEnd === A.na) { const u = anim.t - 1, xs = tx0 - 60 * sk + u * 160 * sk; wave(xs, ty0, xs + 60 * sk, ty0, col); }
      }
    }
    p.fill(...ELC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(ex, ey, 13 * sk);
  }

  // --- the level diagram to scale above a shortened gap below n = 2 ---
  function Y(E) { return E >= En(2) ? G.eTop - G.k * E : G.y1; }
  function levels(S) {
    const { ax, l0, l1, nx } = G;
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ax, G.y1 + 10 * sk, ax, G.eTop - 22 * sk);
    p.noStroke(); p.fill(...INKC); p.triangle(ax, G.eTop - 34 * sk, ax - 6 * sk, G.eTop - 20 * sk, ax + 6 * sk, G.eTop - 20 * sk);
    // the break mark on the axis and the dashed gap
    p.stroke(255); p.strokeWeight(6 * sk); p.line(ax - 8 * sk, G.gap0 + 4 * sk, ax + 8 * sk, G.gap0 - 2 * sk); p.line(ax - 8 * sk, G.gap1 + 4 * sk, ax + 8 * sk, G.gap1 - 2 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ax - 8 * sk, G.gap0 + 4 * sk, ax + 8 * sk, G.gap0 - 2 * sk); p.line(ax - 8 * sk, G.gap1 + 4 * sk, ax + 8 * sk, G.gap1 - 2 * sk);
    lab('$E\\ (\\text{eV})$', G.title[0], G.title[1], 'l', INKC);
    dashed(l0, G.eTop, l1, G.eTop, MUTEDC, 1.8);
    for (let n = 1; n <= 6; n++) {
      p.stroke(...((S.mode === 'emis' ? (n === S.ny || n === S.na) : n === S.na) ? INKC : MUTEDC)); p.strokeWeight((n === 1 ? 3 : 2.2) * sk);
      p.line(l0, Y(En(n)), l1, Y(En(n)));
    }
    const vals = [[0, '0'], [En(4), '-0{,}85'], [En(3), '-1{,}51'], [En(2), '-3{,}40'], [En(1), '-13{,}6']];
    for (const [E, s] of vals) lab('$' + s + '$', ax - 8 * sk, (E === En(1) ? G.y1 : Y(E)) + 0.36 * fh, 'r', INKC);
    lab('$n = 1$', nx, G.y1 + 0.36 * fh, 'l', INKC);
    for (const n of [2, 3, 4]) lab('$n = ' + n + '$', nx, Y(En(n)) + 0.36 * fh, 'l', INKC);
    lab('$n = 5, 6$', nx, (Y(En(5)) + Y(En(6))) / 2 + 0.36 * fh, 'l', INKC);
    // the transition: an arrow between the levels, in the line's colour
    const A = anim ? anim.S : S;
    if (A.valid) {
      const x = G.arrowX;
      if (A.mode === 'emis') arrowV(x, Y(A.Ey), Y(A.Ea), lineColour(A.lambda), anim ? 1 : 0.45);
      else if (A.nEnd !== A.na) arrowV(x, Y(A.Ea), A.nEnd === 0 ? G.eTop - 18 * sk : Y(A.Ey), ELC, anim ? 1 : 0.45);
    }
    // the electron on its level
    const L = electronLevel(S);
    const yA = L.from === 0 ? G.eTop - 14 * sk : Y(En(L.from)), yB = L.to === 0 ? G.eTop - 14 * sk : Y(En(L.to));
    p.fill(...ELC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(G.elX, yA + (yB - yA) * L.u, 13 * sk);
  }

  // --- the spectrum strip: UV, visible and IR zones, each on its own linear scale ---
  function zoneX(l) {
    for (const z of ZONES) if (l >= z.a && l <= z.b) return z.x0 + (l - z.a) / (z.b - z.a) * (z.x1 - z.x0);
    return null;
  }
  function spectrum(S) {
    const { sy0, sy1 } = G;
    for (const z of ZONES) {
      p.noStroke(); p.fill(...INKC); p.rect(z.x0, sy0, z.x1 - z.x0, sy1 - sy0, 3 * sk);
      lab('$\\text{' + __('zone_' + z.name) + '}$', (z.x0 + z.x1) / 2, G.zy, 'c', MUTEDC);
      for (const t of z.ticks) {
        const x = z.x0 + (t - z.a) / (z.b - z.a) * (z.x1 - z.x0);
        p.stroke(...INKC); p.strokeWeight(1.8 * sk); p.line(x, sy1, x, sy1 + 6 * sk);
        lab('$' + t + '$', x, G.ty + 0.36 * fh, 'c', MUTEDC);
      }
    }
    for (const L of lines) {
      const x = zoneX(L.lambda); if (x === null) continue;
      p.stroke(...lineColour(L.lambda, true)); p.strokeWeight(4 * sk); p.line(x, sy0 + 3 * sk, x, sy1 - 3 * sk);
    }
    // the current photon's place on the strip, a small ink triangle under it
    const A = anim ? anim.S : S;
    if (A.valid && A.lambda > 0) {
      const x = zoneX(A.lambda);
      if (x !== null) { p.noStroke(); p.fill(...HEATC); p.triangle(x, sy0 - 2 * sk, x - 6 * sk, sy0 - 12 * sk, x + 6 * sk, sy0 - 12 * sk); }
    }
    lab('$\\lambda\\ (\\text{nm})$', 590, G.atY, 'r', INKC);
  }

  // the colour of a wavelength: its spectral colour in the visible, ink (or light grey on the dark strip) outside it
  function lineColour(l, onDark) {
    if (l < 380 || l > 750) return onDark ? [200, 205, 212] : INKC;
    const stops = [[380, [112, 72, 232]], [420, [112, 72, 232]], [440, [66, 99, 235]], [490, [16, 152, 173]], [520, [43, 138, 62]],
                   [575, [240, 200, 40]], [600, [232, 89, 12]], [640, [201, 42, 42]], [750, [160, 20, 20]]];
    for (let i = 1; i < stops.length; i++) if (l <= stops[i][0]) {
      const [a, ca] = stops[i - 1], [b, cb] = stops[i], u = (l - a) / (b - a);
      return ca.map((v, j) => Math.round(v + u * (cb[j] - v)));
    }
    return stops[stops.length - 1][1];
  }

  function wave(x1, y1, x2, y2, col) {
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, px = -uy, py = ux, head = 11 * sk, sh = L - head;
    p.noFill(); p.stroke(...col); p.strokeWeight(3 * sk); p.beginShape();
    for (let i = 0; i <= 40; i++) { const t = i / 40 * sh, s = 6 * sk * Math.sin(2 * Math.PI * 2.5 * t / sh); p.vertex(x1 + ux * t + px * s, y1 + uy * t + py * s); }
    p.endShape();
    const bx = x2 - ux * head, by = y2 - uy * head;
    p.noStroke(); p.fill(...col); p.triangle(x2, y2, bx + px * 6 * sk, by + py * 6 * sk, bx - px * 6 * sk, by - py * 6 * sk);
  }
  function arrowV(x, ya, yb, col, alpha) {
    const dir = yb > ya ? 1 : -1, head = 12 * sk;
    p.stroke(...col, 255 * alpha); p.strokeWeight(3.5 * sk); p.line(x, ya, x, yb - dir * head);
    p.noStroke(); p.fill(...col, 255 * alpha); p.triangle(x, yb, x - 6 * sk, yb - dir * head, x + 6 * sk, yb - dir * head);
  }
  function dashed(x1, y1, x2, y2, col, w) {
    p.stroke(...col); p.strokeWeight(w * sk); p.drawingContext.setLineDash([6 * sk, 5 * sk]); p.line(x1, y1, x2, y2); p.drawingContext.setLineDash([]);
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
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    cx.fillStyle = gr; cx.fillRect(x, y, w, hh); cx.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (err) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
