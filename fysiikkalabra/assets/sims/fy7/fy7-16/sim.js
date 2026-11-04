// fy7-16 Soveltava luku: langaton lataus. A wireless charger's transmitter coil (radius R1, slider) and a phone's
// receiver coil (radius 20 mm) on the same axis at distance z (slider), seen from the side in cross-section, to scale.
// Model: thin coils of 10 turns each; the transmitter carries a sinusoidal current, peak 1,0 A, 140 kHz; the receiver
// is open (no load). The flux of the transmitter through one receiver turn is the flux of a circular loop through a
// coaxial circle (complete elliptic integrals, AGM): Φ0 = N1 I0 · μ0 √(R1 r) [(2/k − k) K − (2/k) E],
// k² = 4 R1 r / ((R1 + r)² + z²). The receiver's peak voltage is e0 = N2 · 2πf · Φ0. Field lines are contour lines of
// the same flux function at equal flux steps, so the number of lines through the receiver is proportional to Φ0.
// The graph shows e0 against z for the chosen R1. Static: drawn again on every frame, no animation.
// Every canvas text goes through lab().
new p5((p) => {
  const MU0 = 4e-7 * Math.PI, N1 = 10, N2 = 10, I0 = 1.0, F = 140e3, R2 = 20;      // R2, z, R1 in mm
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], FIELDC = [43, 138, 62], COPPERC = [184, 98, 45];
  const CURC = [112, 72, 232], PAPERC = [246, 241, 230], ALU = [196, 204, 212], IRONC = [108, 117, 125], GRIDC = [227, 220, 203];
  const SC = 3.4, CX = 178, Y0 = 300;                      // scene: px per mm, axis x, transmitter plane y
  const GX0 = 418, GX1 = 572, GY0 = 300, GY1 = 92;         // graph plot area
  let slZ, slR, lZ, lR, readout, labels = [], cacheR = null, lines = [];

  function ke(k) {                                          // complete elliptic integrals K(k), E(k)
    let a = 1, b = Math.sqrt(1 - k * k), s = k * k / 2, w = 0.5;
    while (Math.abs(a - b) > 1e-14) { const c = (a - b) / 2, an = (a + b) / 2; b = Math.sqrt(a * b); a = an; w *= 2; s += w * c * c; }
    const K = Math.PI / (2 * a); return [K, K * (1 - s)];
  }
  // flux (Wb) of one transmitter turn with current 1 A through a coaxial circle of radius r at height z (mm)
  function phi1(R, r, z) {
    if (r <= 0) return 0;
    R /= 1000; r /= 1000; z /= 1000;
    const k = Math.sqrt(Math.min(4 * R * r / ((R + r) ** 2 + z * z), 1 - 1e-12)), [K, E] = ke(k);
    return MU0 * Math.sqrt(R * r) * ((2 / k - k) * K - 2 / k * E);
  }
  const e0Of = (R, z) => N2 * 2 * Math.PI * F * N1 * I0 * phi1(R, R2, z);
  const STEP = phi1(20, R2, 3) / 6.5;                       // one field line per this much flux (6 lines at 3 mm, R1 = 20 mm;
                                                            // the half step keeps no line exactly on the receiver wire)

  // one field line around the wire at (R, 0): along each ray from the wire, the point where the flux equals lv
  function fieldLine(R, lv) {
    const pts = [];
    for (let i = 0; i <= 96; i++) {
      const ph = 2 * Math.PI * i / 96, c = Math.cos(ph), s = Math.sin(ph);
      let lo = 0.6, hi = c >= 0 ? 70 : Math.min(70, R / -c);
      if (phi1(R, R + lo * c, lo * s) < lv) continue;
      if (phi1(R, R + hi * c, hi * s) > lv) { pts.push([R + hi * c, hi * s]); continue; }
      for (let j = 0; j < 30; j++) { const m = (lo + hi) / 2; if (phi1(R, R + m * c, m * s) > lv) lo = m; else hi = m; }
      pts.push([R + lo * c, lo * s]);
    }
    return pts;
  }
  function ensureLines(R) {
    if (cacheR === R) return;
    cacheR = R; lines = [];
    for (let k = 1; k <= 16; k++) lines.push({ lv: k * STEP, pts: fieldLine(R, k * STEP) });
  }

  const state = () => {
    const z = Number(slZ.value()), R1 = Number(slR.value());
    const phi0 = N1 * I0 * phi1(R1, R2, z), e0 = N2 * 2 * Math.PI * F * phi0;
    return { z, R1, R2, N1, N2, f: F, I0, phi0: phi0 * 1e6, e0, osuus: 100 * e0 / e0Of(R1, 3), lines: Math.floor(phi0 / (N1 * I0) / STEP + 1e-9) };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lZ = p.createSpan('').parent(l1); slZ = p.createSlider(3, 40, 3, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l2); slR = p.createSlider(10, 40, 20, 5).parent(l2);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { z: { input: slZ.elt, unit: 'mm' }, R1: { input: slR.elt, unit: 'mm' } },
      reset: () => { slZ.value(3); slR.value(20); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lZ.html(__('z', { z: tx(s.z, 0) })); lR.html(__('R1', { r: tx(s.R1, 0) }));
    readout.html(__('lukemat', { phi: tx(s.phi0, 3), e: tx(s.e0, 3), o: tx(s.osuus, 1) }));
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    p.background(...PAPERC);
    ensureLines(s.R1);
    scene(s, fh);
    graph(s, fh);
    window.simState = { z: s.z, R1: s.R1, R2: s.R2, N1: s.N1, N2: s.N2, f: s.f, I0: s.I0, phi0: s.phi0, e0: s.e0, osuus: s.osuus, lines: s.lines, labels };
  };

  // --- the pad, the phone, the coils and the field lines, side view in cross-section ---
  function scene(s, fh) {
    const X = (r) => CX + r * SC, Y = (z) => Y0 - z * SC, yr = Y(s.z);
    // table, pad and phone (behind the field lines)
    p.noStroke(); p.fill(...GRIDC); p.rect(0, Y0 + 34, 372, 400 - Y0 - 34);
    p.stroke(...INKC); p.strokeWeight(2);
    p.fill(...ALU); p.rect(X(-46), Y0 - 6, 92 * SC, 34, 8);
    p.fill(...IRONC); p.rect(X(-40), yr - 30, 80 * SC, 26, 6);
    // field lines, clipped to the scene
    p.drawingContext.save(); p.drawingContext.beginPath(); p.drawingContext.rect(6, 40, 360, 300); p.drawingContext.clip();
    const phiRx = s.phi0 / 1e6 / (N1 * I0);
    p.noFill();
    for (const L of lines) {
      const through = L.lv < phiRx;
      p.stroke(...FIELDC, through ? 255 : 85); p.strokeWeight(through ? 2.5 : 1.5);
      for (const sg of [1, -1]) { p.beginShape(); for (const [r, z] of L.pts) p.vertex(CX + sg * r * SC, Y(z)); p.endShape(); }
    }
    p.drawingContext.restore();
    // upward arrowhead on the axis line: the field points up through the middle at this instant
    p.noStroke(); p.fill(...FIELDC); p.triangle(CX, Y0 - 46, CX - 7, Y0 - 33, CX + 7, Y0 - 33);
    // transmitter coil: current into the page on the right (×), out of it on the left (•)
    wire(X(s.R1), Y0, true); wire(X(-s.R1), Y0, false);
    p.stroke(...INKC); p.strokeWeight(1.5); p.fill(...COPPERC);
    p.circle(X(R2), yr, 11); p.circle(X(-R2), yr, 11);
    // the distance z beside the phone
    const xd = X(48);
    p.stroke(...INKC); p.strokeWeight(1.5);
    p.line(xd - 6, Y0, xd + 6, Y0); p.line(xd - 6, yr, xd + 6, yr); p.line(xd, Y0, xd, yr);
    lab('$z$', xd + 8, (Y0 + yr) / 2 + fh * 0.35, 'l', fh, INKC);
    lab(`$\\text{${__('puhelin')}}$`, X(-21), yr - 17 + fh * 0.35, 'c', fh, [255, 255, 255], IRONC);
    lab(`$\\text{${__('laturi')}}$`, X(46), Y0 + 40 + fh, 'r', fh, INKC, GRIDC);
    lab(`$\\text{${__('vastaanotin')}}$`, X(-40), Math.max(52, yr - 42), 'l', fh, INKC, PAPERC);
    lab(`$\\text{${__('lahetin')}}$`, X(-46), Y0 + 40 + fh, 'l', fh, INKC, GRIDC);
  }

  function wire(x, y, into) {
    p.stroke(...INKC); p.strokeWeight(1.5); p.fill(...COPPERC); p.circle(x, y, 15);
    p.stroke(255); p.strokeWeight(2.5);
    if (into) { p.line(x - 4, y - 4, x + 4, y + 4); p.line(x - 4, y + 4, x + 4, y - 4); }
    else { p.noStroke(); p.fill(255); p.circle(x, y, 5); }
    p.noFill(); p.stroke(...CURC); p.strokeWeight(2); p.circle(x, y, 19);
  }

  // --- e0 against z for the chosen transmitter coil, the current distance marked ---
  function graph(s, fh) {
    const GX = (z) => GX0 + z / 40 * (GX1 - GX0), GY = (e) => GY0 - e / 5 * (GY0 - GY1);
    p.stroke(...GRIDC); p.strokeWeight(1.5);
    for (let z = 10; z <= 40; z += 10) p.line(GX(z), GY0, GX(z), GY1);
    for (let e = 1; e <= 5; e++) p.line(GX0, GY(e), GX1, GY(e));
    p.stroke(...INKC); p.strokeWeight(2.5);
    p.line(GX0, GY0, GX1 + 14, GY0); p.line(GX0, GY0, GX0, GY1 - 14);
    p.noStroke(); p.fill(...INKC);
    p.triangle(GX1 + 22, GY0, GX1 + 10, GY0 - 6, GX1 + 10, GY0 + 6);
    p.triangle(GX0, GY1 - 22, GX0 - 6, GY1 - 10, GX0 + 6, GY1 - 10);
    p.stroke(...INKC); p.strokeWeight(2);
    for (let z = 10; z <= 40; z += 10) { p.line(GX(z), GY0, GX(z), GY0 + 6); lab(`$${z}$`, GX(z), GY0 + 8 + fh, 'c', fh, MUTEDC); }
    for (let e = 1; e <= 5; e++) { p.line(GX0 - 6, GY(e), GX0, GY(e)); lab(`$${e}$`, GX0 - 9, GY(e) + fh * 0.35, 'r', fh, MUTEDC); }
    lab('$0$', GX0 - 9, GY0 + 8 + fh, 'r', fh, MUTEDC);
    lab('$e_0\\ (\\text{V})$', GX0 - 8, GY1 - 30, 'l', fh, INKC);
    lab('$z\\ (\\text{mm})$', 596, GY0 + 22 + 1.9 * fh, 'r', fh, INKC);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.beginShape();
    for (let z = 3; z <= 40; z += 0.5) p.vertex(GX(z), GY(Math.min(5, e0Of(s.R1, z))));
    p.endShape();
    p.stroke(255); p.strokeWeight(2); p.fill(...INKC); p.circle(GX(s.z), GY(Math.min(5, s.e0)), 13);
  }

  // every canvas text: drawn and its ink box pushed to simState.labels (canvas coordinates)
  function lab(str, x, y, align, size, col, bg) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(str), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke();
    if (bg) { p.fill(...bg); p.rect(x0 - 4, y - 0.85 * size, w + 8, 1.15 * size, 3); }   // keeps field lines off the text
    p.fill(...(col || INKC)); p.text(str, x0, y);
    labels.push({ s: str, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
