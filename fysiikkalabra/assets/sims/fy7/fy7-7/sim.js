// fy7-7 Generaattori ja vaihtovirta: a rectangular coil (N turns, A = 4,0 cm · 5,0 cm = 20 cm²) turns at the rotation
// frequency f in a uniform horizontal field B between an N pole (left) and an S pole (right). The coil is seen end-on
// (along its axle). θ is the angle between the coil's normal and the field; θ = 0 at t = 0 (the coil's plane
// perpendicular to the field). Model: the flux through one turn is Φ = B A cos θ, θ = θ0 + 2πf t. The voltage is
// computed from the flux with the induction law of the previous chapter, e = −N ΔΦ/Δt (a central difference over
// 2 · 10⁻⁵ s), not from the formula e0 = NBA · 2πf; the peak e0 is the largest |e| found over one turn (720 samples).
// Two graphs, Φ(t) and e(t), are drawn as a sweep of 2,0 s of model time; any change of N, B or f starts a new sweep.
// Time runs at dt · speed (hidas · normaali · nopea = 0,125 · 0,25 · 0,5 of real time); Pysäytä freezes the picture.
// The sides' velocities (blue) and the induced current in the sides (dot or cross, violet) are drawn.
// Every canvas text goes through lab(), which pushes its ink box (canvas coordinates) to simState.labels.
new p5((p) => {
  const A = 4.0e-2 * 5.0e-2;                                     // m², the coil's area
  const TW = 2.0;                                                // s, the sweep's length of model time
  const SLOW = 0.25;                                             // model seconds per real second at normal speed
  const VIOLET = [112, 72, 232], GREEN = [43, 138, 62], BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const NPOLE = [242, 166, 156], SPOLE = [208, 230, 251], COPPERC = [184, 98, 45], GRID = [227, 220, 203];
  let btn, selN, slB, slF, selSpeed, lB, lF, readout, labels = [];
  let running = true, t = 0, th0 = 0, sig = '';
  let OX = 0, OY = 0, SC = 1;

  const par = () => ({ N: Number(selN.value()), B: Number(slB.value()), f: Number(slF.value()) });
  const phiAt = (m, th) => m.B * A * Math.cos(th);              // Wb, one turn
  // the induction law on the model's flux: e = −N ΔΦ/Δt at the model time τ of the current sweep
  const eAt = (m, tau) => {
    const d = 1e-5, a1 = th0 + 2 * Math.PI * m.f * (tau + d), a0 = th0 + 2 * Math.PI * m.f * (tau - d);
    return -m.N * (phiAt(m, a1) - phiAt(m, a0)) / (2 * d);
  };
  const peak = (m) => { let mx = 0; const T = 1 / m.f; for (let k = 0; k < 720; k++) mx = Math.max(mx, Math.abs(eAt(m, k * T / 720))); return mx; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('pysayta')).parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; btn.html(running ? __('pysayta') : __('jatka')); p.redraw(); });
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('kierrokset')).parent(l1); selN = p.createSelect().parent(l1);
    for (const v of ['250', '500', '1000']) selN.option(v, v);
    selN.selected('500');
    const l2 = p.createElement('label').parent(controls); lB = p.createSpan('').parent(l2); slB = p.createSlider(0.05, 0.30, 0.20, 0.05).parent(l2);
    const l3 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l3); slF = p.createSlider(1.0, 5.0, 2.0, 0.5).parent(l3);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { N: { input: selN.elt, unit: '' }, B: { input: slB.elt, unit: 'T' }, f: { input: slF.elt, unit: 'Hz' } },
      reset: () => { selN.selected('500'); slB.value(0.20); slF.value(2.0); t = 0; th0 = 0; sig = ''; running = true; btn.html(__('pysayta')); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const m = par();
    const s = `${m.N}|${m.B}|${m.f}`;
    if (s !== sig) { if (sig) th0 += 2 * Math.PI * Number(sig.split('|')[2]) * t; t = 0; sig = s; }   // a new sweep from the angle reached
    if (running) {
      t += Math.min(p.deltaTime, 100) / 1000 * SLOW * (Number(selSpeed.value()) || 1);
      if (t >= TW) { th0 = th0 + 2 * Math.PI * m.f * TW; t -= TW; }
    }
    th0 = ((th0 % (2 * Math.PI)) + 2 * Math.PI) % (2 * Math.PI);
    const th = th0 + 2 * Math.PI * m.f * t;
    const phi = phiAt(m, th), e = eAt(m, t), e0 = peak(m), U = e0 / Math.SQRT2, T = 1 / m.f;
    const deg = ((th * 180 / Math.PI) % 360 + 360) % 360;
    lB.html(__('kentta', { B: tx(m.B, 2) })); lF.html(__('taajuus', { f: tx(m.f, 1) }));
    readout.html(__('lukemat', { e0: tx(e0, 2), U: tx(U, 2), T: tx(T, 2), th: tx(deg, 0), phi: tx(phi * 1e3, 3), e: tx(e, 2) }));
    window.simState = { N: m.N, B: m.B, f: m.f, A, e0, U, T, theta: deg, phi: phi * 1e3, e, t, running, speed: Number(selSpeed.value()), labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const narrow = cw < 500;
    const Hc = narrow ? 1190 : 400;
    if (p.__H !== Hc) { p.__H = Hc; p.resizeCanvas(600, Hc); setTimeout(() => p.redraw(), 0); return; }
    const fhc = narrow ? Math.round(14 * k) : Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    p.background(250);
    if (narrow) {
      panel(112, 0, 1.5, () => coil(m, th, e, e0, fhc / 1.5));
      p.stroke(220); p.strokeWeight(1.5); p.line(0, 604, 600, 604);
      panel(45, 610, 1.5, () => graphs(m, phi, e, fhc / 1.5, k > 1.5));
    } else {
      panel(0, 0, 1, () => coil(m, th, e, e0, fhc));
      p.stroke(220); p.strokeWeight(1); p.line(252, 0, 252, 400);
      panel(256, 10, 1, () => graphs(m, phi, e, fhc, k > 1.5));
    }
    window.simState.labels = labels;
  };

  function panel(ox, oy, sc, fn) { OX = ox; OY = oy; SC = sc; p.push(); p.translate(ox, oy); p.scale(sc); fn(); p.pop(); OX = 0; OY = 0; SC = 1; }

  // --- the generator seen along its axle (local 250 × 400) ---
  function coil(m, th, e, e0, fh) {
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...NPOLE); p.rect(10, 70, 40, 260, 4);
    p.fill(...SPOLE); p.rect(200, 70, 40, 260, 4);
    lab('$\\text{N}$', 30, 206, 'c', fh, INKC); lab('$\\text{S}$', 220, 206, 'c', fh, INKC);
    const a = 90 + 70 * m.B / 0.30;                              // field lines: more opaque in a stronger field
    for (const y of [92, 140, 260, 308]) fieldLine(56, 194, y, 2, a);
    lab('$\\overline{B}$', 125, 52, 'c', fh, GREEN);
    const cx = 125, cy = 200, R = 62;
    const d = [Math.sin(th), Math.cos(th)], nv = [Math.cos(th), -Math.sin(th)];
    const p1 = [cx + R * d[0], cy + R * d[1]], p2 = [cx - R * d[0], cy - R * d[1]];
    p.stroke(...COPPERC); p.strokeWeight(6); p.strokeCap(p.ROUND); p.line(p2[0], p2[1], p1[0], p1[1]); p.strokeCap(p.SQUARE);
    p.noStroke(); p.fill(...INKC); p.circle(cx, cy, 8);
    // the sides' velocities: along the normal, length grows with f
    const L = 14 + 8 * m.f;
    arrow(p1[0] + nv[0] * 13, p1[1] + nv[1] * 13, p1[0] + nv[0] * (13 + L), p1[1] + nv[1] * (13 + L), BLUE, 2.5, 10);
    arrow(p2[0] - nv[0] * 13, p2[1] - nv[1] * 13, p2[0] - nv[0] * (13 + L), p2[1] - nv[1] * (13 + L), BLUE, 2.5, 10);
    // the induced current in the sides: e > 0 into the page at p1, out at p2
    side(p1, e, e0, +1); side(p2, e, e0, -1);
    lab(`$\\theta = ${tx(((th * 180 / Math.PI) % 360 + 360) % 360, 0)}^\\circ$`, 125, 372, 'c', fh, INKC);
  }
  function side(c, e, e0, sg) {
    p.fill(255); p.stroke(...VIOLET); p.strokeWeight(2.5); p.circle(c[0], c[1], 20);
    if (Math.abs(e) < 0.05 * e0) return;                         // hardly any voltage: no current symbol
    if (e * sg > 0) { p.line(c[0] - 5, c[1] - 5, c[0] + 5, c[1] + 5); p.line(c[0] + 5, c[1] - 5, c[0] - 5, c[1] + 5); }
    else { p.noStroke(); p.fill(...VIOLET); p.circle(c[0], c[1], 6); }
  }

  // --- Φ(t) and e(t) (local 340 × 380): Φ in mWb on ±0,6, e in V on ±20 ---
  function graphs(m, phi, e, fh, sparse) {
    const x0 = 58, x1 = 294;
    plot(m, 14, 160, x0, x1, 0.6, [0.3, 0.6], fh, sparse, '$\\Phi\\ (\\text{mWb})$', GREEN, (tau, th) => phiAt(m, th) * 1e3, phi * 1e3);
    plot(m, 204, 350, x0, x1, 20, [10, 20], fh, sparse, '$e\\ (\\text{V})$', VIOLET, (tau) => eAt(m, tau), e);
  }
  function plot(m, yt, yb, x0, x1, ymax, ticks, fh, sparse, title, col, fn, now) {
    const ym = (yt + yb) / 2 + 8, hh = (yb - yt - 16) / 2;
    const X = (tau) => x0 + tau / TW * (x1 - x0), Y = (v) => ym - v / ymax * hh;
    p.strokeWeight(1);
    for (let q = 0.5; q <= TW + 1e-9; q += 0.5) { p.stroke(...GRID); p.line(X(q), Y(ymax), X(q), Y(-ymax)); }
    for (const v of ticks) { p.stroke(...GRID); p.line(x0, Y(v), x1, Y(v)); p.line(x0, Y(-v), x1, Y(-v)); }
    p.stroke(...INKC); p.strokeWeight(2); p.line(x0, Y(-ymax) + 4, x0, Y(ymax) - 10); p.line(x0, ym, x1 + 10, ym);
    p.noStroke(); p.fill(...INKC); p.triangle(x0, Y(ymax) - 16, x0 - 5, Y(ymax) - 6, x0 + 5, Y(ymax) - 6);
    p.triangle(x1 + 16, ym, x1 + 6, ym - 5, x1 + 6, ym + 5);
    lab(title, x0 + 8, Y(ymax) - 6, 'l', fh, INKC);
    lab('$t\\ (\\text{s})$', x1 + 4, ym + fh * 1.3, 'l', fh, INKC);
    for (const v of ticks) {
      if (sparse && v !== ticks[ticks.length - 1]) continue;
      lab(`$${tx(v, ymax < 1 ? 1 : 0)}$`, x0 - 6, Y(v) + fh * 0.35, 'r', fh * 0.9, MUTEDC);
      lab(`$${tx(-v, ymax < 1 ? 1 : 0)}$`, x0 - 6, Y(-v) + fh * 0.35, 'r', fh * 0.9, MUTEDC);
    }
    for (let q = 0.5; q <= TW + 1e-9; q += 0.5) {
      if (sparse && Math.abs(q - Math.round(q)) > 1e-9) continue;
      lab(`$${tx(q, 1)}$`, X(q), Y(-ymax) + fh * 1.1, 'c', fh * 0.9, MUTEDC);
    }
    // the trace of the current sweep, up to now
    p.noFill(); p.stroke(...col); p.strokeWeight(2.5); p.beginShape();
    const n = Math.max(2, Math.ceil((X(t) - x0) / 1.5));
    for (let i = 0; i <= n; i++) { const tau = t * i / n; p.vertex(X(tau), Y(Math.max(-ymax, Math.min(ymax, fn(tau, th0 + 2 * Math.PI * m.f * tau))))); }
    p.endShape();
    p.noStroke(); p.fill(...col); p.stroke(255); p.strokeWeight(2); p.circle(X(t), Y(Math.max(-ymax, Math.min(ymax, now))), 10);
  }

  function fieldLine(x1, x2, y, w, alpha) {
    p.stroke(...GREEN, alpha); p.strokeWeight(w); p.line(x1, y, x2, y);
    const xm = (x1 + x2) / 2 + 40;
    p.noStroke(); p.fill(...GREEN, alpha); p.triangle(xm + 9, y, xm - 3, y - 5, xm - 3, y + 5);
  }
  function arrow(x1, y1, x2, y2, col, w, Hh) {
    const L = Math.hypot(x2 - x1, y2 - y1); if (L < 2) return;
    const a = Math.atan2(y2 - y1, x2 - x1), hh = Math.min(Hh, L * 0.6);
    p.stroke(...col); p.strokeWeight(w); p.line(x1, y1, x2 - hh * 0.8 * Math.cos(a), y2 - hh * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2, y2, x2 - hh * Math.cos(a - 0.42), y2 - hh * Math.sin(a - 0.42), x2 - hh * Math.cos(a + 0.42), y2 - hh * Math.sin(a + 0.42));
  }
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0: OX + x0 * SC, y0: OY + (y - 0.75 * size) * SC, x1: OX + (x0 + w) * SC, y1: OY + (y + 0.25 * size) * SC });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (err) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
