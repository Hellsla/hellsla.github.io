// fy7-4 Voima virtajohtimeen: a current balance (virtavaaka). A U-shaped magnet stands on a digital scale; a rigid
// wire frame held by a stand dips into the gap between the poles, so that its horizontal bottom segment of length l
// lies in the uniform field B. Model: the field is uniform in the gap and zero outside; only the bottom segment is in
// the field. The leads are vertical, so their forces (if any) are horizontal and do not change the scale reading.
// The force on the segment is vertical: F = I l B sin α, up for a positive current with the poles drawn here (N right,
// S left, B to the left; the current I > 0 runs along the segment's direction d = (cos α, sin α) in the top view).
// By Newton's third law the wire pushes the magnet with the opposite force, so the scale reads m = m0 + F / g.
// The field strength of each magnet is not shown: the student determines it from the readings (calc box).
// Two pictures: the side view (scale, magnet, wire, force arrow) and the top view (poles, field lines, the segment at
// the angle α, the current, the force out of or into the page). On a narrow screen they stack (NOTES §4).
// Every canvas text goes through lab(), which pushes its ink box (canvas coordinates) to simState.labels.
new p5((p) => {
  const g = 9.81, M0 = 245.30;                                  // m/s², the magnet's reading without current (g)
  const FIELD = { A: 0.080, B: 0.12 };                           // T, the magnets' fields (not shown to the student)
  const RED = [201, 42, 42], VIOLET = [112, 72, 232], GREEN = [43, 138, 62], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const NPOLE = [242, 166, 156], SPOLE = [208, 230, 251], IRONC = [108, 117, 125], COPPERC = [184, 98, 45], ALU = [196, 204, 212];
  const SF = 2500;                                               // side view: px per newton of the force arrow
  const ST = 2400;                                               // top view: px per metre of wire
  let slI, slA, lI, lA, selM, selL, readout, labels = [];
  let OX = 0, OY = 0, SC = 1;                                    // the current panel's offset and scale (lab() boxes)

  const state = () => {
    const I = Number(slI.value()), al = Number(slA.value()), B = FIELD[selM.value()], l = Number(selL.value()) / 100;
    const F = I * l * B * Math.sin(al * Math.PI / 180);          // vertical force on the wire, + up (N)
    const dm = F / g * 1000;                                     // the scale's change (g): the magnet is pushed down by F
    return { I, al, B, l, F, dm, m: Math.round((M0 + dm) * 100) / 100 };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lI = p.createSpan('').parent(l1); slI = p.createSlider(-6, 6, 0, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l2); slA = p.createSlider(0, 90, 90, 5).parent(l2);
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('magneetti')).parent(l3); selM = p.createSelect().parent(l3);
    selM.option(__('magneetti_a'), 'A'); selM.option(__('magneetti_b'), 'B'); selM.selected('A');
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('pituus')).parent(l4); selL = p.createSelect().parent(l4);
    selL.option(__('pituus_lyhyt'), '2.5'); selL.option(__('pituus_pitka'), '5'); selL.selected('5');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    for (const e of [slI.elt, slA.elt, selM.elt, selL.elt]) { e.addEventListener('input', () => p.redraw()); e.addEventListener('change', () => p.redraw()); }
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { I: { input: slI.elt, unit: 'A' }, alpha: { input: slA.elt, unit: '°' }, magneetti: { input: selM.elt, unit: '' }, l: { input: selL.elt, unit: 'cm' } },
      reset: () => { slI.value(0); slA.value(90); selM.selected('A'); selL.selected('5'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lI.html(__('virta', { I: tx(s.I, 1) })); lA.html(__('kulma', { a: tx(s.al, 0) }));
    readout.html(__('lukemat', { m: tx(s.m, 2), I: tx(s.I, 1), a: tx(s.al, 0), l: tx(s.l * 100, 1) }));
    window.simState = { I: s.I, alpha: s.al, magneetti: selM.value(), B: s.B, l: s.l * 100, F: s.F, dm: s.dm, lukema: s.m, m0: M0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const narrow = cw < 500;
    const H = narrow ? 1020 : 400;
    if (p.__H !== H) { p.__H = H; p.resizeCanvas(600, H); setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state: draw again next frame
    const fhc = narrow ? Math.round(14 * k) : Math.round((k > 1.2 ? 14 : 13) * k);   // label size in canvas px
    labels = [];
    p.background(250);
    if (narrow) {
      panel(52, 0, 1.5, () => side(s, fhc / 1.5));
      p.stroke(220); p.strokeWeight(1.5); p.line(0, 572, 600, 572);
      panel(97.5, 572, 1.5, () => top(s, fhc / 1.5));
    } else {
      panel(0, 10, 1, () => side(s, fhc));
      p.stroke(220); p.strokeWeight(1); p.line(334, 0, 334, 400);
      panel(330, 50, 1, () => top(s, fhc));
    }
    window.simState.labels = labels;
  };

  function panel(ox, oy, sc, fn) { OX = ox; OY = oy; SC = sc; p.push(); p.translate(ox, oy); p.scale(sc); fn(); p.pop(); OX = 0; OY = 0; SC = 1; }

  // --- side view (local 330 × 380): stand, wire frame, magnet on the scale, the force on the wire ---
  function side(s, fh) {
    lab(__('sivukuva'), 12, 22, 'l', fh, INKC);
    // stand: base, rod, arm and clamp
    grect(10, 350, 74, 14, [[150, 158, 168], [108, 117, 125]], false, 3);
    grect(32, 44, 9, 306, [[196, 204, 212], [138, 150, 163]], true, 2);
    grect(32, 50, 182, 9, [[196, 204, 212], [138, 150, 163]], false, 2);
    p.fill(...INKC); p.noStroke(); p.rect(190, 46, 22, 17, 3);
    // scale: platform, body and its display
    grect(84, 298, 232, 54, [[214, 220, 226], [176, 186, 196]], false, 6);
    grect(98, 290, 204, 9, [[160, 168, 178], [120, 128, 138]], false, 2);
    p.fill(...INKC); p.rect(206, 308, 100, 34, 4);
    lab(`$${tx(s.m, 2)}\\,\\text{g}$`, 298, 331, 'r', fh * 1.05, [255, 255, 255]);
    // magnet: iron yoke with the S pole piece on the left and the N pole piece on the right
    grect(110, 260, 180, 30, [[138, 146, 156], [96, 104, 112]], false, 3);
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...SPOLE); p.rect(110, 150, 40, 112, 3);
    p.fill(...NPOLE); p.rect(250, 150, 40, 112, 3);
    lab('$\\text{S}$', 130, 214, 'c', fh, INKC); lab('$\\text{N}$', 270, 214, 'c', fh, INKC);
    // field lines across the gap, from N to S
    for (const y of [170, 236]) fieldLine(246, 154, y, 1.5);
    // the wire frame: leads from the clamp, the bottom segment's projection (its length l cos α across the page)
    const dx = s.l * 1600 / 2 * Math.abs(Math.cos(s.al * Math.PI / 180));
    p.noFill(); p.stroke(...COPPERC); p.strokeWeight(4); p.strokeCap(p.ROUND);
    if (dx < 3) { p.line(201, 62, 201, 196); }
    else { p.line(201 - dx, 62, 201 - dx, 196); p.line(201 + dx, 62, 201 + dx, 196); p.line(201 - dx, 196, 201 + dx, 196); }
    p.strokeCap(p.SQUARE);
    if (dx < 12 && s.I !== 0) {                                  // the segment runs into or out of the page: show the current's sense
      p.fill(255); p.stroke(...VIOLET); p.strokeWeight(2.5); p.circle(201, 196, 18);
      const into = s.I > 0;                                      // I > 0 along +y of the top view = away from the viewer
      if (into) { p.line(195.5, 190.5, 206.5, 201.5); p.line(206.5, 190.5, 195.5, 201.5); } else { p.noStroke(); p.fill(...VIOLET); p.circle(201, 196, 6); }
    }
    // the force on the wire: vertical, its length the force
    if (Math.abs(s.F) > 1e-6) {
      const L = s.F * SF;
      arrowV(201, 196, L, RED, 3.5);
      lab('$\\overline{F}$', 214, 196 - L + (L > 0 ? fh * 0.4 : 0), 'l', fh, RED);
    }
  }

  // --- top view (local 270 × 300): the poles from above, the field, the segment at the angle α ---
  function top(s, fh) {
    lab(__('ylakuva'), 12, 16, 'l', fh, INKC);
    lab('$\\overline{B}$', 135, 30, 'c', fh, GREEN);
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...SPOLE); p.rect(16, 50, 34, 230, 3);
    p.fill(...NPOLE); p.rect(220, 50, 34, 230, 3);
    lab('$\\text{S}$', 33, 170, 'c', fh, INKC); lab('$\\text{N}$', 237, 170, 'c', fh, INKC);
    for (let y = 62; y <= 270; y += 34) fieldLine(216, 54, y, 2);
    const cx = 135, cy = 165, a = s.al * Math.PI / 180, d = [Math.cos(a), -Math.sin(a)], n = [Math.sin(a), Math.cos(a)];
    const h = s.l * ST / 2;
    // the angle α between the wire and the field direction
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]); p.line(cx, cy, cx + 78, cy); p.drawingContext.setLineDash([]);
    if (s.al > 0) {
      p.noFill(); p.stroke(...INKC); p.strokeWeight(2); p.arc(cx, cy, 64, 64, -a, 0);
      lab('$\\alpha$', cx + 46 * Math.cos(a / 2), cy - 46 * Math.sin(a / 2) + fh * 0.35, 'c', fh, INKC);
    }
    // the segment and the leads (seen from above as dots)
    p.stroke(...COPPERC); p.strokeWeight(6); p.strokeCap(p.ROUND);
    p.line(cx - h * d[0], cy - h * d[1], cx + h * d[0], cy + h * d[1]); p.strokeCap(p.SQUARE);
    p.noStroke(); p.fill(...INKC); p.circle(cx - h * d[0], cy - h * d[1], 9); p.circle(cx + h * d[0], cy + h * d[1], 9);
    if (s.I !== 0) {
      // the current: a violet arrow beside the segment, on the side away from the angle's arc
      const sg = Math.sign(s.I), off = 15, q = h * 0.8;
      const x1 = cx - n[0] * off - sg * q * d[0], y1 = cy - n[1] * off - sg * q * d[1];
      const x2 = cx - n[0] * off + sg * q * d[0], y2 = cy - n[1] * off + sg * q * d[1];
      arrow(x1, y1, x2, y2, VIOLET, 2.5, 10);
      lab('$I$', x2 - n[0] * 14 + sg * d[0] * 8, y2 - n[1] * 14 + sg * d[1] * 8 + fh * 0.35, 'c', fh, VIOLET);
    }
    if (Math.abs(s.F) > 1e-6) {
      // the force on the segment: out of the page (up) as a dot, into the page (down) as a cross
      p.fill(255); p.stroke(...RED); p.strokeWeight(2.5); p.circle(cx, cy, 22);
      if (s.F > 0) { p.noStroke(); p.fill(...RED); p.circle(cx, cy, 7); }
      else { p.line(cx - 6, cy - 6, cx + 6, cy + 6); p.line(cx + 6, cy - 6, cx - 6, cy + 6); }
      const u = [n[0] - d[0], n[1] - d[1]], ul = Math.hypot(u[0], u[1]) || 1;
      lab('$\\overline{F}$', cx + u[0] / ul * 30, cy + u[1] / ul * 30 + fh * 0.35, 'c', fh, RED);
    }
  }

  // a field line from x1 to x2 (N to S) at height y, with an arrowhead in the middle
  function fieldLine(x1, x2, y, w) {
    p.stroke(...GREEN, 170); p.strokeWeight(w); p.line(x1, y, x2, y);
    const xm = (x1 + x2) / 2 - 18, dir = Math.sign(x2 - x1);
    p.noStroke(); p.fill(...GREEN); p.triangle(xm + dir * 9, y, xm - dir * 3, y - 5, xm - dir * 3, y + 5);
  }
  function arrowV(x, y, L, col, w) { arrow(x, y, x, y - L, col, w, 12); }
  function arrow(x1, y1, x2, y2, col, w, H) {
    const L = Math.hypot(x2 - x1, y2 - y1); if (L < 2) return;
    const a = Math.atan2(y2 - y1, x2 - x1), hh = Math.min(H, L * 0.6);
    p.stroke(...col); p.strokeWeight(w); p.line(x1, y1, x2 - hh * 0.8 * Math.cos(a), y2 - hh * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2, y2, x2 - hh * Math.cos(a - 0.42), y2 - hh * Math.sin(a - 0.42), x2 - hh * Math.cos(a + 0.42), y2 - hh * Math.sin(a + 0.42));
  }

  // every canvas text: drawn in the panel's coordinates, its ink box pushed to simState.labels in canvas coordinates
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0: OX + x0 * SC, y0: OY + (y - 0.75 * size) * SC, x1: OX + (x0 + w) * SC, y1: OY + (y + 0.25 * size) * SC });
  }
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((st, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${st.join(',')})`));
    c.fillStyle = gr; c.strokeStyle = 'rgba(31,41,51,0.45)'; c.lineWidth = 1.5; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
