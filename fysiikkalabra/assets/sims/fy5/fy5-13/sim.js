// fy5-13 Seisovat aallot: the steady state of a driven, weakly damped wave on a string fixed at both ends, in a pipe open
// at both ends and in a pipe closed at one end. The drive is at the left end x = 0 (string: a vibrator moving the end by
// a = 1,0 mm; pipe: a loudspeaker at the open end). With the complex wave number k = 2πf/v − iα, α = 0,06 / L, and s = L − x
// the displacement amplitude is   string U = a sin(ks)/sin(kL),   open pipe U = a cos(ks)/sin(kL),   closed pipe
// U = a sin(ks)/cos(kL): the wave travelling to the right end plus its reflection. The amplitude grows large (about 16,7 a)
// only at the eigenfrequencies, which the sim never computes for the picture: f_n = n v/(2L) (string, open pipe) and
// n v/(4L), n odd (closed pipe) emerge from the boundary conditions. The picture moves u(x, t) = Re(U e^{iφ}) with a slowed
// phase φ (one swing per 1,25 s at normaali); A = max|U|, nodes and antinodes are read off the envelope |U|. The pipe shows
// the air's longitudinal displacement as moving columns of particles and as a graph. Below, every frequency the student
// has tried leaves a point (f, A), cleared when the case, L or v changes. Every canvas text goes through lab(), which pushes
// its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const ALPHA_L = 0.06, AMM = 1.0, V_AIR = 340, SC = 300;               // damping αL, drive amplitude (mm), sound speed, px per metre
  const BLUE = [47, 116, 181], BLUE_L = [169, 209, 240], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178],
        GRID = [227, 220, 203], IRONC = [108, 117, 125], ALU = [196, 204, 212], EDGE = [138, 150, 163], GLASSC = [238, 245, 249],
        SANDL = [241, 223, 181], SANDD = [233, 201, 138], WOOD = [169, 122, 53];
  // geometry: wide 600 x 400 (picture above, graph below); narrow (sim-root < 500 px) 600 x 700 with larger labels
  const WIDE = { H: 400, x0: 72, sk: 3.2, row: 32, yc: 118, table: 190, dim: 216, tube: 93, hh: 29, gc: 162, gs: 1.6,
                 ox: 72, oy: 368, gx1: 520, gy1: 262, ytk: [0, 5, 10, 15, 20], xtk: 100, xlab: 388, picH: 236 };
  const NARROW = { H: 700, x0: 64, sk: 5.2, row: 36, yc: 152, table: 262, dim: 300, tube: 120, hh: 46, gc: 228, gs: 2.2,
                   ox: 112, oy: 636, gx1: 520, gy1: 392, ytk: [0, 10, 20], xtk: 200, xlab: 670, picH: 324 };
  let G = WIDE, narrow = false, sk = 1, fh = 13, labels = [];
  let selMode, slF, slL, slV, lF, lL, lV, selSpeed, readout;
  let phase = 0, seen = new Map(), seenKey = '';

  // --- complex arithmetic for the steady state ---
  const C = (re, im) => ({ re, im });
  const cmul = (a, b) => C(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
  const cdiv = (a, b) => { const d = b.re * b.re + b.im * b.im; return C((a.re * b.re + a.im * b.im) / d, (a.im * b.re - a.re * b.im) / d); };
  const csin = (z) => C(Math.sin(z.re) * Math.cosh(z.im), Math.cos(z.re) * Math.sinh(z.im));
  const ccos = (z) => C(Math.cos(z.re) * Math.cosh(z.im), -Math.sin(z.re) * Math.sinh(z.im));
  const cabs = (z) => Math.hypot(z.re, z.im);

  const params = () => {
    const tila = selMode.value(), L = Number(slL.value());
    return { tila, f: Number(slF.value()), L, v: tila === 'kieli' ? Number(slV.value()) : V_AIR };
  };
  // U(x) at 301 points from x = 0 (drive) to x = L
  function field(P) {
    const k = C(2 * Math.PI * P.f / P.v, -ALPHA_L / P.L), kL = cmul(k, C(P.L, 0));
    const den = P.tila === 'suljettu' ? ccos(kL) : csin(kL);
    const U = [];
    for (let j = 0; j <= 300; j++) {
      const ks = cmul(k, C(P.L * (1 - j / 300), 0));
      const num = P.tila === 'avoin' ? ccos(ks) : csin(ks);
      const z = cdiv(num, den); U.push(C(z.re * AMM, z.im * AMM));
    }
    return U;
  }
  // nodes: local minima of |U| under 0,15 A; antinodes: local maxima over 0,85 A (the ends count when they qualify)
  function marks(env, A) {
    const out = [], N = env.length - 1;
    for (let j = 0; j <= N; j++) {
      const l = j > 0 ? env[j - 1] : Infinity, r = j < N ? env[j + 1] : Infinity;
      const l2 = j > 0 ? env[j - 1] : -Infinity, r2 = j < N ? env[j + 1] : -Infinity;
      if (env[j] < l && env[j] <= r && env[j] < 0.15 * A) out.push({ j, t: 'S' });
      else if (env[j] > l2 && env[j] >= r2 && env[j] > 0.85 * A) out.push({ j, t: 'K' });
    }
    return out;
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('tilanne')).parent(l0); selMode = p.createSelect().parent(l0);
    selMode.option(__('kieli'), 'kieli'); selMode.option(__('avoin'), 'avoin'); selMode.option(__('suljettu'), 'suljettu'); selMode.selected('kieli');
    const l1 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l1); slF = p.createSlider(50, 700, 50, 5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l2); slL = p.createSlider(0.4, 1.5, 0.6, 0.05).parent(l2);
    const l3 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l3); slV = p.createSlider(60, 300, 120, 5).parent(l3);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const modeChanged = () => { slV.elt.disabled = selMode.value() !== 'kieli'; };
    selMode.elt.addEventListener('change', modeChanged); selMode.elt.addEventListener('input', modeChanged);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tila: { input: selMode.elt, unit: '' }, f: { input: slF.elt, unit: 'Hz' }, L: { input: slL.elt, unit: 'm' }, v: { input: slV.elt, unit: 'm/s' } },
      reset: () => { selMode.selected('kieli'); slF.value(50); slL.value(0.6); slV.value(120); modeChanged(); seen.clear(); phase = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales only the pace of the slowed picture; A, nodes and the graph do not depend on it
    phase = (phase + 2 * Math.PI * 0.8 * Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value())) % (2 * Math.PI);
    const P = params(), U = field(P), env = U.map(cabs), A = Math.max(...env), M = marks(env, A);
    const solmut = M.filter((m) => m.t === 'S').length, kuvut = M.filter((m) => m.t === 'K').length, lambda = P.v / P.f;
    const f1 = P.tila === 'suljettu' ? P.v / (4 * P.L) : P.v / (2 * P.L);
    const key = `${P.tila}|${P.L}|${P.v}`;
    if (key !== seenKey) { seen.clear(); seenKey = key; }
    seen.set(P.f, A);
    lF.html(__('taajuus', { f: String(P.f) }));
    lL.html(__('pituus', { L: tx(P.L, 2) }));
    lV.html(P.tila === 'kieli' ? __('nopeus_kieli', { v: String(P.v) }) : __('nopeus_ilma', { v: String(V_AIR) }));
    readout.html(__('lukemat', { lam: tx(lambda, 2), A: tx(A, 1), S: String(solmut), K: String(kuvut) }));
    window.simState = { tila: P.tila, f: P.f, L: P.L, v: P.v, lambda, A, solmut, kuvut, f1, pisteet: seen.size, phase, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.picH, [[246, 241, 230], [255, 255, 255]]);
    const x1 = G.x0 + P.L * SC;
    if (P.tila === 'kieli') stringPicture(P, U, x1); else pipePicture(P, U, x1);
    markLabels(M, x1);
    dimension(P, x1);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.picH, 600, G.picH);
    graph(P, A);
    window.simState.labels = labels;
  };

  const X = (j, x1) => G.x0 + (x1 - G.x0) * j / 300;
  const now = (z) => z.re * Math.cos(phase) - z.im * Math.sin(phase);  // u(x, t) = Re(U e^{iφ})

  // --- the string: vibrator, string over a pulley, a weight whose size grows with the tension (∝ v²) ---
  function stringPicture(P, U, x1) {
    const { x0, yc, table } = G, s = G.sk;
    p.noStroke(); p.fill(...SANDD); p.rect(x0 - 64 * sk, table, x1 - x0 + 90 * sk, 10 * sk, 2);
    p.stroke(...WOOD); p.strokeWeight(2 * sk); p.line(x0 - 64 * sk, table, x1 + 26 * sk, table);
    // envelope and the swing between it
    p.noStroke(); p.fill(...BLUE_L, 120); p.beginShape();
    for (let j = 0; j <= 300; j++) p.vertex(X(j, x1), yc - cabs(U[j]) * s);
    for (let j = 300; j >= 0; j--) p.vertex(X(j, x1), yc + cabs(U[j]) * s);
    p.endShape(p.CLOSE);
    dashedCurve(U, x1, yc, s);
    // the vibrator and its rod
    const yd = yc - now(U[0]) * s;
    p.fill(...IRONC); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(x0 - 56 * sk, yc - 26 * sk, 40 * sk, table - yc + 26 * sk, 5 * sk);
    p.fill(...ALU); p.strokeWeight(1.5 * sk); p.rect(x0 - 18 * sk, yd - 4 * sk, 18 * sk, 8 * sk, 2);
    // pulley, its clamp and the weight
    const r = 13 * sk, pcx = x1 + r * 0.9, pcy = yc + r;
    p.fill(...EDGE); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(pcx - 5 * sk, pcy, 10 * sk, table - pcy, 2);
    p.fill(...ALU); p.strokeWeight(2.5 * sk); p.circle(pcx, pcy, 2 * r); p.fill(...INKC); p.circle(pcx, pcy, 6 * sk);
    const side = (12 + 26 * (P.v / 300) ** 2) * sk, wy = pcy + 20 * sk;
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(pcx + r, pcy, pcx + r, wy);
    p.fill(...IRONC); p.strokeWeight(2.5 * sk); p.rect(pcx + r - side / 2, wy, side, side, 3);
    // the string now
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(3.5 * sk); p.beginShape();
    for (let j = 0; j <= 300; j++) p.vertex(X(j, x1), yc - now(U[j]) * s);
    p.endShape();
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(3.5 * sk); p.arc(pcx, pcy, 2 * r, 2 * r, -Math.PI, 0);
  }

  // --- the pipe: loudspeaker at the open left end, air columns moving along the pipe, and the displacement graph ---
  function pipePicture(P, U, x1) {
    const { x0, tube, hh, gc, gs } = G;
    p.fill(...GLASSC); p.noStroke(); p.rect(x0, tube - hh, x1 - x0, 2 * hh);
    // air columns: each moves along the pipe by its displacement (0,55 px per mm on a wide screen)
    const px = 0.55 * sk, cols = Math.round((x1 - x0) / (11 * sk));
    p.noStroke(); p.fill(...BLUE);
    for (let c = 0; c <= cols; c++) {
      const j = Math.round(300 * c / cols), xb = X(j, x1) + now(U[j]) * px;
      for (let r = 0; r < 4; r++) p.circle(Math.min(Math.max(xb, x0 + 3), x1 - 3), tube - hh + 2 * hh * (r + 0.375 + (c % 2) * 0.25) / 4, 4.2 * sk);
    }
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.line(x0, tube - hh, x1, tube - hh); p.line(x0, tube + hh, x1, tube + hh);
    if (P.tila === 'suljettu') { p.fill(...IRONC); p.strokeWeight(2 * sk); p.rect(x1 - 2, tube - hh - 4 * sk, 11 * sk, 2 * hh + 8 * sk, 2); }
    // loudspeaker
    const sx = x0 - 8 * sk;
    p.fill(...INKC); p.noStroke(); p.rect(sx - 30 * sk, tube - 12 * sk, 14 * sk, 24 * sk, 2);
    p.fill(...IRONC); p.stroke(...INKC); p.strokeWeight(2 * sk);
    p.quad(sx - 16 * sk, tube - 12 * sk, sx, tube - 24 * sk, sx, tube + 24 * sk, sx - 16 * sk, tube + 12 * sk);
    // displacement graph under the pipe
    p.stroke(...RULEC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([4 * sk, 5 * sk]); p.line(x0, gc, x1, gc); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(...BLUE_L, 120); p.beginShape();
    for (let j = 0; j <= 300; j++) p.vertex(X(j, x1), gc - cabs(U[j]) * gs * sk);
    for (let j = 300; j >= 0; j--) p.vertex(X(j, x1), gc + cabs(U[j]) * gs * sk);
    p.endShape(p.CLOSE);
    dashedCurve(U, x1, gc, gs * sk);
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(3 * sk); p.beginShape();
    for (let j = 0; j <= 300; j++) p.vertex(X(j, x1), gc - now(U[j]) * gs * sk);
    p.endShape();
  }

  function dashedCurve(U, x1, yc, s) {   // the two extreme shapes ±|U| as dashed lines
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([6 * sk, 5 * sk]);
    for (const sg of [1, -1]) { p.beginShape(); for (let j = 0; j <= 300; j++) p.vertex(X(j, x1), yc - sg * cabs(U[j]) * s); p.endShape(); }
    p.drawingContext.setLineDash([]);
  }

  // node and antinode letters in one row above the picture, when there is room for them; dots on the axis always
  function markLabels(M, x1) {
    const xs = M.map((m) => X(m.j, x1));
    let gap = Infinity;
    for (let i = 1; i < xs.length; i++) gap = Math.min(gap, xs[i] - xs[i - 1]);
    const y = G.row, ya = selMode.value() === 'kieli' ? G.yc : G.gc;
    M.forEach((m, i) => {
      if (m.t === 'S') { p.fill(...INKC); p.stroke(255); p.strokeWeight(1.5 * sk); p.circle(xs[i], ya, 9 * sk); }
      if (gap >= 1.3 * fh + 2) {
        lab(m.t === 'S' ? '$\\text{S}$' : '$\\text{K}$', xs[i], y, 'c', INKC);
        p.stroke(...MUTEDC); p.strokeWeight(1.2 * sk); p.drawingContext.setLineDash([2 * sk, 4 * sk]);
        p.line(xs[i], y + 0.5 * fh, xs[i], ya - 10 * sk); p.drawingContext.setLineDash([]);
      }
    });
  }

  function dimension(P, x1) {
    const y = G.dim, x0 = G.x0;
    p.stroke(...INKC); p.strokeWeight(1.8 * sk); p.line(x0, y, x1, y);
    p.line(x0, y - 7 * sk, x0, y + 7 * sk); p.line(x1, y - 7 * sk, x1, y + 7 * sk);
    const s = '$L = ' + tx(P.L, 2) + '\\,\\text{m}$', w = textW(s) + 12 * sk, xm = (x0 + x1) / 2;
    p.noStroke(); p.fill(255); p.rect(xm - w / 2, y - 0.7 * fh, w, 1.4 * fh);
    lab(s, xm, y + 0.36 * fh, 'c', INKC);
  }

  // --- the (f, A) graph of the frequencies tried ---
  function graph(P, A) {
    const { ox, oy, gx1, gy1 } = G;
    const GX = (f) => ox + f / 700 * (gx1 - ox), GY = (a) => oy - Math.min(a, 21) / 20 * (oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let f = 100; f <= 700; f += 100) p.line(GX(f), oy, GX(f), gy1);
    for (const a of [5, 10, 15, 20]) p.line(ox, GY(a), gx1, GY(a));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 16 * sk, oy); p.line(ox, oy, ox, gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, oy, gx1 + 14 * sk, oy - 6 * sk, gx1 + 14 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 26 * sk, ox - 6 * sk, gy1 - 12 * sk, ox + 6 * sk, gy1 - 12 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (const a of G.ytk) { p.line(ox - 6 * sk, GY(a), ox, GY(a)); lab('$' + a + '$', ox - 9 * sk, GY(a) + 0.36 * fh, 'r', INKC); }
    for (let f = G.xtk; f <= 600; f += G.xtk) { p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(f), oy, GX(f), oy + 6 * sk); lab('$' + f + '$', GX(f), G.xlab, 'c', INKC); }
    lab('$A\\,(\\text{mm})$', ox + 12 * sk, gy1 - 14 * sk, 'l', INKC);
    lab('$f\\,(\\text{Hz})$', 596, G.xlab, 'r', INKC);
    const r = (narrow ? 4.5 : 3.8) * sk;
    for (const [f, a] of seen) { p.fill(...BLUE); p.stroke(255); p.strokeWeight(1.5 * sk); p.circle(GX(f), GY(a), 2 * r); }
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(GX(P.f), GY(A), 5 * r);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function textW(s) { p.textStyle(p.NORMAL); p.textSize(fh); return p.textWidth(s); }
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
