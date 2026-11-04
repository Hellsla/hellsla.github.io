// fy8-6 LEDin valo ja Planckin vakion mittaaminen: an LED in a circuit with an adjustable voltage, a protective
// resistor, an ammeter in series and a voltmeter across the LED. The student picks one of six LEDs (peak wavelength λ)
// and sets the LED's voltage U; the model current is I = (s/R) · ln(1 + exp((U − U_k)/s)) with s = 0,035 V and
// R = 18 Ω: practically zero below the LED's threshold voltage U_k and a straight line I = (U − U_k)/R above it, so
// the straight part extended to I = 0 meets the U axis at U_k. The model's U_k is a little below hc/(eλ), as in real
// LEDs. The LED glows in its own colour, brighter with more current; every voltage visited is kept as a point of the
// (U, I) graph in the LED's colour until the graph is cleared. Nothing moves, so there is no speed control.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const S = 0.035, R = 18;                                                // V, Ω
  const LED = { 630: 1.88, 605: 1.95, 590: 2.00, 525: 2.30, 470: 2.52, 405: 2.95 };   // λ (nm): U_k (V)
  const NAME = { 630: 'punainen', 605: 'oranssi', 590: 'keltainen', 525: 'vihrea', 470: 'sininen', 405: 'violetti' };
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], WIRE = [31, 41, 51],
        CASE = [196, 204, 212], EDGE = [138, 150, 163], HOTC = [201, 42, 42], PAPER = [251, 248, 240];
  // the picture: a 300 × 360 box drawn at (PX, PY) with scale PS; the graph's plot area in canvas coordinates
  const WIDE = { H: 400, PX: 0, PY: 20, PS: 1, gx0: 352, gy0: 336, gx1: 572, gy1: 66, tick: 1 };
  const NARROW = { H: 960, PX: 75, PY: 0, PS: 1.5, gx0: 120, gy0: 890, gx1: 548, gy1: 600, tick: 1 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let selL, slU, lU, readout, bClear;
  let visited = {};                                                       // λ: {U in hundredths of a volt: I in mA}

  const current = (U, Uk) => S / R * Math.log1p(Math.exp((U - Uk) / S)) * 1000;   // mA
  const params = () => ({ lam: Number(selL.value()), U: Number(slU.value()) });
  const remember = () => {
    const P = params(), Uk = LED[P.lam];
    (visited[P.lam] = visited[P.lam] || {})[Math.round(P.U * 100)] = current(P.U, Uk);
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('led')).parent(l1); selL = p.createSelect().parent(l1);
    for (const lam of [630, 605, 590, 525, 470, 405]) selL.option(__(NAME[lam]), String(lam));
    selL.selected('630');
    const l2 = p.createElement('label').parent(controls); lU = p.createSpan('').parent(l2); slU = p.createSlider(0, 3.5, 2.0, 0.01).parent(l2);
    bClear = p.createButton(__('tyhjenna')).parent(controls);
    bClear.elt.addEventListener('click', () => { visited = {}; remember(); });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    for (const el of [slU, selL]) { el.elt.addEventListener('input', remember); el.elt.addEventListener('change', remember); }
    remember();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { lambda: { input: selL.elt, unit: 'nm' }, U: { input: slU.elt, unit: 'V' } },
      reset: () => { selL.selected('630'); slU.value(2.0); visited = {}; remember(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = params(), Uk = LED[P.lam], I = current(P.U, Uk);
    lU.html(__('jannite', { U: tx(P.U, 2) }));
    readout.html(__('lukemat', { U: tx(P.U, 2), I: tx(I, 2), l: String(P.lam) }) + (I > 30 ? '<br>' + __('varoitus') : ''));
    window.simState = { lambda: P.lam, U: P.U, I: I, Uk: Uk, over: I > 30 ? 1 : 0,
                        points: Object.values(visited).reduce((s, m) => s + Object.keys(m).length, 0), labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    picture(P, I);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, 556, 600, 556); else p.line(312, 20, 312, 380);
    graph(P, I);
    window.simState.labels = labels;
  };

  // picture coordinates (300 × 360 box) to canvas
  const X = (x) => G.PX + x * G.PS, Y = (y) => G.PY + y * G.PS;

  function ledColour(lam) {   // the colour of the LED's light (approximate), as in the lesson's figures
    let r, g, b;
    if (lam < 440) { r = (440 - lam) / 60; g = 0; b = 1; } else if (lam < 490) { r = 0; g = (lam - 440) / 50; b = 1; }
    else if (lam < 510) { r = 0; g = 1; b = (510 - lam) / 20; } else if (lam < 580) { r = (lam - 510) / 70; g = 1; b = 0; }
    else if (lam < 645) { r = 1; g = (645 - lam) / 65; b = 0; } else { r = 1; g = 0; b = 0; }
    const k = lam < 420 ? 0.3 + 0.7 * (lam - 380) / 40 : 1, to = (v) => (v > 0 ? 255 * Math.pow(v * k, 0.8) : 0);
    return [to(r) * 0.86, to(g) * 0.78, to(b) * 0.86];
  }

  function wire(pts) {
    p.noFill(); p.stroke(...WIRE); p.strokeWeight(2.5 * sk); p.beginShape();
    for (const [x, y] of pts) p.vertex(X(x), Y(y));
    p.endShape();
  }

  function meter(x, y, letter) {
    p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(X(x), Y(y), 36 * G.PS);
    lab('$\\text{' + letter + '}$', X(x), Y(y) + 0.36 * fh, 'c', INKC);
  }

  function picture(P, I) {
    const col = ledColour(P.lam), s = G.PS, glow = Math.min(1, I / 20);
    // wires: supply (left) – resistor – ammeter – LED (right) – back; voltmeter across the LED
    wire([[54, 150], [54, 70], [200, 70], [200, 150]]);
    wire([[200, 230], [200, 320], [54, 320], [54, 250]]);
    wire([[200, 130], [140, 130], [140, 172]]);
    wire([[140, 208], [140, 250], [200, 250]]);
    p.noStroke(); p.fill(...INKC); p.circle(X(200), Y(130), 7 * s); p.circle(X(200), Y(250), 7 * s);
    // adjustable supply: a case with a knob, its + terminal at the top
    p.fill(...CASE); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(X(24), Y(150), 60 * s, 100 * s, 6 * s);
    p.fill(...EDGE); p.circle(X(54), Y(214), 26 * s); p.stroke(...INKC); p.line(X(54), Y(214), X(54 + 8), Y(214 - 10));
    p.noStroke(); p.fill(...HOTC); p.circle(X(54), Y(166), 9 * s);
    // protective resistor on the top wire
    p.fill(...PAPER); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(X(84), Y(62), 44 * s, 16 * s, 2 * s);
    meter(165, 70, 'A');
    meter(140, 190, 'V');
    // the LED: a glow in its colour, the diode symbol (triangle pointing with the current, a bar), photons out
    if (glow > 0.01) {
      for (let r = 1; r >= 0.2; r -= 0.2) { p.noStroke(); p.fill(...col, 60 * glow * (1.2 - r)); p.circle(X(200), Y(190), (40 + 110 * glow) * r * s); }
    }
    p.fill(...(glow > 0.01 ? col : [235, 235, 235])); p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    p.triangle(X(184), Y(172), X(216), Y(172), X(200), Y(204));
    p.line(X(182), Y(206), X(218), Y(206));
    p.line(X(200), Y(150), X(200), Y(172)); p.line(X(200), Y(206), X(200), Y(230));
    const nPh = glow > 0.6 ? 3 : glow > 0.15 ? 2 : glow > 0.01 ? 1 : 0;
    for (let q = 0; q < nPh; q++) {
      const y0 = 172 + 20 * q - 2 * (nPh - 1) * 5, x0 = 226, x1 = 282, per = P.lam / 50;
      p.noFill(); p.stroke(...col); p.strokeWeight(2.2 * sk); p.beginShape();
      for (let xx = x0; xx <= x1 - 8; xx += 1) p.vertex(X(xx), Y(y0 - 0.35 * (xx - x0) + 4 * Math.sin(2 * Math.PI * (xx - x0) / per)));
      p.endShape();
      const tx0 = x1, ty0 = y0 - 0.35 * (x1 - x0);
      p.noStroke(); p.fill(...col); p.triangle(X(tx0), Y(ty0), X(tx0 - 10), Y(ty0 - 1.5), X(tx0 - 7), Y(ty0 + 6));
    }
    if (nPh > 0) lab('$hf$', X(262), Y(196) + 0.36 * fh, 'l', col);
    // meter readings and the LED's wavelength
    lab('$' + tx(I, 2) + '\\,\\text{mA}$', X(165), Y(36) + 0.36 * fh, 'c', INKC);
    lab('$' + tx(P.U, 2) + '\\,\\text{V}$', X(140), Y(285) + 0.36 * fh, 'c', INKC);
    lab('$\\lambda = ' + P.lam + '\\,\\text{nm}$', X(150), Y(348) + 0.36 * fh, 'c', INKC);
  }

  // the (U, I) graph: every visited point in its LED's colour, the present one large
  function graph(P, I) {
    const { gx0, gy0, gx1, gy1 } = G, gX = (U) => gx0 + U / 3.5 * (gx1 - gx0), gY = (i) => gy0 - i / 30 * (gy0 - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let U = 0.5; U <= 3.51; U += 0.5) p.line(gX(U), gy0, gX(U), gy1);
    for (let i = 5; i <= 30; i += 5) p.line(gx0, gY(i), gx1, gY(i));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    p.line(gx0, gy0, gx1 + 14 * sk, gy0); p.line(gx0, gy0, gx0, gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 24 * sk, gy0, gx1 + 12 * sk, gy0 - 5 * sk, gx1 + 12 * sk, gy0 + 5 * sk);
    p.triangle(gx0, gy1 - 24 * sk, gx0 - 5 * sk, gy1 - 12 * sk, gx0 + 5 * sk, gy1 - 12 * sk);
    for (let U = 0.5; U <= 3.51; U += 0.5) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(gX(U), gy0, gX(U), gy0 + 6 * sk);
      if (Math.round(U * 2) % 2 === 0) lab('$' + tx(U, 0) + '$', gX(U), gy0 + 8 * sk + fh, 'c', INKC);
    }
    for (let i = 5; i <= 30; i += 5) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(gx0 - 6 * sk, gY(i), gx0, gY(i));
      if (i % 10 === 0) lab('$' + i + '$', gx0 - 9 * sk, gY(i) + 0.36 * fh, 'r', INKC);
    }
    lab('$0$', gx0 - 9 * sk, gy0 + 8 * sk + fh, 'r', INKC);
    lab('$U\\ (\\text{V})$', gx1 - 4 * sk, gy0 - 0.9 * fh, 'r', INKC);
    lab('$I\\ (\\text{mA})$', gx0 + 10 * sk, gy1 - 8 * sk, 'l', INKC);
    for (const lam of Object.keys(visited)) {
      const col = ledColour(Number(lam));
      for (const [u, i] of Object.entries(visited[lam])) {
        if (i > 30) continue;
        p.noStroke(); p.fill(...col); p.circle(gX(u / 100), gY(i), 6 * sk);
      }
    }
    if (I <= 30) { p.fill(...ledColour(P.lam)); p.stroke(255); p.strokeWeight(2 * sk); p.circle(gX(P.U), gY(I), 13 * sk); }
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
});
