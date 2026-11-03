// fy5-15 Äänen voimakkuus: N equal loudspeakers of acoustic power P each stand at one point and radiate evenly in every
// direction; a sound level meter stands at distance r. With no reflections and no absorption the whole power passes
// through the sphere of area A = 4πr² around the speakers, so I = N P / (4π r²), and the meter shows the intensity
// level L = 10 dB · lg(I / I0), I0 = 1,0 · 10⁻¹² W/m². Independent speakers add their intensities, never their decibels.
// The picture: the speakers, wavefront arcs moving outwards (their brightness follows the level at their radius; their
// pace is only a picture, not the speed of sound, and the speed select scales it), the meter on a tripod and the
// distance r. Below: the graph L(r) for the current speakers with the meter's point. Every canvas text goes through
// lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const I0 = 1e-12;
  const HEATC = [232, 89, 12], HEATL = [255, 192, 120], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203],
        IRONC = [108, 117, 125], ALU = [196, 204, 212], EDGE = [138, 150, 163], GLASSC = [238, 245, 249], SANDD = [233, 201, 138],
        WOOD = [169, 122, 53];
  // geometry: wide 600 x 400 (picture above, graph below); narrow (sim-root < 500 px) 600 x 720 with larger labels
  const WIDE = { H: 400, sx: 84, sc: 23.5, yc: 128, ground: 186, dim: 200, dimLab: 222, meterLab: 72, picH: 234,
                 ox: 70, oy: 370, gx1: 520, gy1: 268, xstep: 5, ylabs: [40, 60, 80, 100, 120], xlab: 390 };
  const NARROW = { H: 720, sx: 120, sc: 22, yc: 200, ground: 300, dim: 320, dimLab: 356, meterLab: 108, picH: 380,
                   ox: 112, oy: 664, gx1: 490, gy1: 452, xstep: 10, ylabs: [40, 80, 120], xlab: 706 };
  let G = WIDE, sk = 1, ms = 1, fh = 13, labels = [];   // sk: strokes and labels, ms: size of the speakers and the meter
  let slP, selN, slR, selSpeed, lP, lR, readout, phase = 0;

  const level = (I) => 10 * Math.log10(I / I0);
  const params = () => ({ P: Number(slP.value()), N: Number(selN.value()), r: Number(slR.value()) });
  const intensity = (P, r) => (P / 1000) / (4 * Math.PI * r * r);   // P in mW, I in W/m²

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lP = p.createSpan('').parent(l1); slP = p.createSlider(1, 100, 50, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('kaiuttimia')).parent(l2); selN = p.createSelect().parent(l2);
    for (const k of ['1', '2', '4', '10']) selN.option(__('n' + k), k);
    selN.selected('1');
    const l3 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l3); slR = p.createSlider(1, 20, 2, 0.5).parent(l3);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { P: { input: slP.elt, unit: 'mW' }, N: { input: selN.elt, unit: '' }, r: { input: slR.elt, unit: 'm' } },
      reset: () => { slP.value(50); selN.selected('1'); slR.value(2); phase = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales only the pace of the arcs; I and L do not depend on it
    phase = (phase + 60 * Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value())) % 60;
    const S = params(), Ptot = S.N * S.P, A = 4 * Math.PI * S.r * S.r, I = intensity(Ptot, S.r), L = level(I);
    lP.html(__('teho', { P: String(S.P) }));
    lR.html(__('etaisyys', { r: tx(S.r, 1) }));
    readout.html(__('lukemat', { Pt: String(Ptot), A: tx(A, 1), I: sci(I), L: tx(L, 1) }));
    window.simState = { P: S.P, N: S.N, r: S.r, Ptot: Ptot / 1000, A, I, ImW: I * 1000, L, phase, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    ms = narrow ? Math.min(k, 1.3) : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.picH, [[246, 241, 230], [255, 255, 255]]);
    picture(S, Ptot, L);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.picH, 600, G.picH);
    graph(S, Ptot, L);
    window.simState.labels = labels;
  };

  const XR = (r) => G.sx + r * G.sc;               // canvas x of a point r metres from the speakers' front

  function picture(S, Ptot, L) {
    const { sx, yc, ground } = G;
    // ground with grass edge
    p.noStroke(); p.fill(...SANDD); p.rect(0, ground, 600, 8 * sk);
    p.stroke(...WOOD); p.strokeWeight(2 * sk); p.line(0, ground, 600, ground);
    // wavefront arcs: radius grows with the phase; brightness follows the level at that radius
    const c = p.drawingContext; c.save(); c.beginPath(); c.rect(sx, 0, 600 - sx, ground - 1); c.clip();
    p.noFill();
    for (let rho = phase + 14; rho < 560; rho += 60) {
      const rm = Math.max(rho / G.sc, 0.3), Lr = level(intensity(Ptot, rm));
      const a = Math.min(1, Math.max(0.08, (Lr - 45) / 60));
      p.stroke(...HEATC, 255 * a); p.strokeWeight(4 * sk);
      p.arc(sx, yc, 2 * rho, 2 * rho, -1.05, 1.05);
    }
    c.restore();
    speakers(S.N);
    meter(XR(S.r), L);
    // distance r from the speakers' front to the meter
    const y = G.dim, x1 = XR(S.r);
    p.stroke(...INKC); p.strokeWeight(1.8 * sk); p.line(sx, y, x1, y);
    p.line(sx, y - 7 * sk, sx, y + 7 * sk); p.line(x1, y - 7 * sk, x1, y + 7 * sk);
    lab('$r = ' + tx(S.r, 1) + '\\,\\text{m}$', (sx + x1) / 2, G.dimLab, 'c', INKC);
  }

  function speakers(N) {   // N cabinets in a block in front of x = sx, standing on the ground
    const cols = N <= 2 ? 1 : 2, rows = Math.ceil(N / cols), x0 = G.sx - 58 * ms, w = 58 * ms, top = G.yc - 46 * ms, h = G.ground - top;
    const cwid = w / cols, chgt = h / rows;
    for (let i = 0; i < N; i++) {
      const cx = x0 + (i % cols) * cwid, cy = top + Math.floor(i / cols) * chgt;
      p.fill(...INKC); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.rect(cx + 1, cy + 1, cwid - 2, chgt - 2, 3 * ms);
      const rr = Math.min(cwid, chgt) * 0.34;
      p.fill(...IRONC); p.stroke(...EDGE); p.strokeWeight(2 * ms); p.circle(cx + cwid / 2, cy + chgt / 2, 2 * rr);
      p.noStroke(); p.fill(...EDGE); p.circle(cx + cwid / 2, cy + chgt / 2, 0.7 * rr);
    }
  }

  function meter(x, L) {   // a sound level meter on a tripod, its microphone at the arcs' height
    const { yc, ground } = G;
    p.stroke(...INKC); p.strokeWeight(2 * ms);
    p.line(x, yc + 48 * ms, x - 16 * ms, ground); p.line(x, yc + 48 * ms, x + 16 * ms, ground); p.line(x, yc + 48 * ms, x, ground);
    p.fill(...ALU); p.stroke(...INKC); p.strokeWeight(2 * ms); p.rect(x - 13 * ms, yc + 8 * ms, 26 * ms, 40 * ms, 4 * ms);
    p.fill(...GLASSC); p.strokeWeight(1.2 * ms); p.rect(x - 9 * ms, yc + 13 * ms, 18 * ms, 11 * ms, 2 * ms);
    const bar = Math.max(0, Math.min(1, (L - 40) / 80));               // the display's bar grows with the level
    p.noStroke(); p.fill(...HEATC); p.rect(x - 7 * ms, yc + 15 * ms, 14 * ms * bar, 7 * ms);
    p.stroke(...INKC); p.strokeWeight(3 * ms); p.line(x, yc + 8 * ms, x, yc + 3 * ms);
    p.fill(...IRONC); p.strokeWeight(1.5 * sk); p.circle(x, yc, 10 * ms);
    lab('$L = ' + tx(L, 1) + '\\,\\text{dB}$', x, G.meterLab, 'c', INKC);
  }

  // --- the graph L(r) of the current speakers, the meter's point ringed ---
  function graph(S, Ptot, L) {
    const { ox, oy, gx1, gy1 } = G;
    const GX = (r) => ox + r / 20 * (gx1 - ox), GY = (l) => oy - (Math.min(Math.max(l, 40), 124) - 40) / 80 * (oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let r = 5; r <= 20; r += 5) p.line(GX(r), oy, GX(r), gy1);
    for (let l = 60; l <= 120; l += 20) p.line(ox, GY(l), gx1, GY(l));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 16 * sk, oy); p.line(ox, oy, ox, gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, oy, gx1 + 14 * sk, oy - 6 * sk, gx1 + 14 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 26 * sk, ox - 6 * sk, gy1 - 12 * sk, ox + 6 * sk, gy1 - 12 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let l = 40; l <= 120; l += 20) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(l), ox, GY(l));
      if (G.ylabs.includes(l)) lab('$' + l + '$', ox - 9 * sk, GY(l) + 0.36 * fh, 'r', INKC);
    }
    for (let r = 5; r <= 20; r += 5) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(r), oy, GX(r), oy + 6 * sk);
      if (r % G.xstep === 0) lab('$' + r + '$', GX(r), G.xlab, 'c', INKC);
    }
    lab('$L\\,(\\text{dB})$', ox + 12 * sk, gy1 - 14 * sk, 'l', INKC);
    lab('$r\\,(\\text{m})$', 596, G.xlab, 'r', INKC);
    // the curve from 1 m to 20 m
    p.noFill(); p.stroke(...HEATC); p.strokeWeight(3 * sk); p.beginShape();
    for (let j = 0; j <= 190; j++) { const r = 1 + j * 0.1; p.vertex(GX(r), GY(level(intensity(Ptot, r)))); }
    p.endShape();
    // the meter's point with dashed guides to the axes
    const x = GX(S.r), y = GY(L);
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 5 * sk]);
    p.line(x, y, x, oy); p.line(ox, y, x, y); p.drawingContext.setLineDash([]);
    p.fill(...HEATC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(x, y, 12 * sk);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(x, y, 22 * sk);
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
  // a small intensity in LaTeX powers of ten with three significant figures: 9{,}95 \cdot 10^{-4}
  function sci(x) {
    let e = Math.floor(Math.log10(x)), m = x / 10 ** e;
    if (Number(m.toFixed(2)) >= 10) { m /= 10; e += 1; }
    return tx(m, 2) + ' \\cdot 10^{' + e + '}';
  }
});
