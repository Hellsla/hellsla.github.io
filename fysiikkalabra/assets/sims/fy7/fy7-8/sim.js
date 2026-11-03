// fy7-8 Muuntaja ja sähköenergian siirto: a power plant sends the power P to a town along a transmission line.
// The generator gives 20 kV; an ideal step-up transformer raises it to the transmission voltage U (ratio N2 : N1 =
// U : 20 kV), and an ideal step-down transformer in the town lowers it again. Model: the line is treated as one
// two-conductor line whose conductors have the total resistance R = r l with r = 0,040 Ω/km. The line current is
// I = P / U and the power turned into heat in the line is P_h = R I²; the town receives P − P_h. When R I ≥ U the
// loss would be at least the sent power: the transfer is impossible and the sim says so (simState.mahdoton).
// The picture: plant, step-up transformer, pylons with the line (redder as the loss share grows, heat shimmer
// above it), step-down transformer and the town with lit windows; under it two bars to one scale: the delivered
// power (green) and the loss (orange). On a narrow screen the canvas grows taller and the labels larger (NOTES §4).
// Static: drawn again on every frame, no animation. Every canvas text goes through lab() (simState.labels).
new p5((p) => {
  const UG = 20, RKM = 0.040;                                    // generator voltage (kV), line resistance (Ω/km)
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], HOT = [201, 42, 42], HEATC = [232, 89, 12], HEATL = [255, 192, 120];
  const GREEN = [43, 138, 62], GREENL = [178, 242, 187], IRONC = [108, 117, 125], ALU = [196, 204, 212], SANDL = [241, 223, 181];
  const SKY = [238, 245, 249], COPPERC = [184, 98, 45];
  let slU, slP, slL, lU, lP, lL, readout, labels = [];

  const state = () => {
    const U = Number(slU.value()), P = Number(slP.value()), l = Number(slL.value());
    const R = RKM * l, I = P * 1e6 / (U * 1e3), Ph = R * I * I / 1e6;
    const mahdoton = R * I >= U * 1e3;
    return { U, P, l, R, I, Ph, osuus: Ph / P * 100, perille: mahdoton ? 0 : P - Ph, N21: U / UG, mahdoton };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lU = p.createSpan('').parent(l1); slU = p.createSlider(20, 400, 400, 10).parent(l1);
    const l2 = p.createElement('label').parent(controls); lP = p.createSpan('').parent(l2); slP = p.createSlider(50, 500, 200, 50).parent(l2);
    const l3 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l3); slL = p.createSlider(10, 300, 150, 10).parent(l3);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { U: { input: slU.elt, unit: 'kV' }, P: { input: slP.elt, unit: 'MW' }, l: { input: slL.elt, unit: 'km' } },
      reset: () => { slU.value(400); slP.value(200); slL.value(150); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lU.html(__('jannite', { U: tx(s.U, 0) })); lP.html(__('teho', { P: tx(s.P, 0) })); lL.html(__('pituus', { l: tx(s.l, 0) }));
    readout.html(s.mahdoton
      ? __('lukemat_mahdoton', { I: tx(s.I, 0), R: tx(s.R, 1), n: nr(s.N21) })
      : __('lukemat', { Ph: mw(s.Ph), o: tx(s.osuus, s.osuus < 10 ? 2 : 1), I: tx(s.I, 0), R: tx(s.R, 1), Pp: mw(s.perille), n: nr(s.N21) }));
    window.simState = { U: s.U, P: s.P, l: s.l, R: s.R, I: s.I, Ph: s.Ph, osuus: s.osuus, perille: s.perille, N21: s.N21, mahdoton: s.mahdoton, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const narrow = cw < 500, H = narrow ? 600 : 400;
    if (p.__H !== H) { p.__H = H; p.resizeCanvas(600, H); setTimeout(() => p.redraw(), 0); return; }
    const fh = narrow ? Math.round(14 * k) : Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    p.background(250);
    const yg = narrow ? 300 : 236, yl = yg + 16 + fh * 1.15;   // ground line; the labels under it
    scene(s, fh, yg, yl);
    bars(s, fh, yl + fh * 0.4, H - 10);
    window.simState.labels = labels;
  };

  // --- the scene: sky, ground, plant, transformers, pylons, line, town; ground line at y = yg ---
  function scene(s, fh, yg, yl) {
    const c = p.drawingContext, gr = c.createLinearGradient(0, 0, 0, yg);
    gr.addColorStop(0, 'rgb(208,230,251)'); gr.addColorStop(1, `rgb(${SKY.join(',')})`);
    c.fillStyle = gr; c.fillRect(0, 0, 600, yg);
    p.noStroke(); p.fill(...GREENL); p.rect(0, yg, 600, 6); p.fill(...SANDL); p.rect(0, yg + 6, 600, 10);
    p.stroke(220); p.strokeWeight(1.5); p.line(0, yg + 16, 600, yg + 16);
    const top = yg - 150;                                          // the conductors' height at the pylons
    // power plant: hall, roof, generator
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...SANDL); p.rect(14, yg - 70, 70, 70);
    p.fill(...IRONC); p.triangle(8, yg - 70, 49, yg - 96, 90, yg - 70);
    p.fill(...ALU); p.circle(49, yg - 34, 30); p.fill(...INKC); p.circle(49, yg - 34, 8);
    // step-up transformer (two overlapping circles on a box) and step-down transformer
    trafo(120, yg - 40); trafo(480, yg - 40);
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(84, yg - 40, 104, yg - 40);
    // pylons
    const px = [190, 300, 410];
    for (const x of px) pylon(x, yg, top);
    // the line: colour from ink to red with the loss share, thicker when the current is large
    const f = s.mahdoton ? 1 : Math.min(1, s.osuus / 25);
    const col = INKC.map((v, i) => v + (HOT[i] - v) * f);
    const w = 2 + Math.min(3, s.I / 2500);
    p.noFill(); p.stroke(...col); p.strokeWeight(w);
    const pts = [[136, yg - 40], [px[0], top], [px[1], top], [px[2], top], [464, yg - 40]];
    for (let i = 0; i < pts.length - 1; i++) {
      const [x1, y1] = pts[i], [x2, y2] = pts[i + 1];
      p.beginShape(); p.vertex(x1, y1); p.quadraticVertex((x1 + x2) / 2, Math.max(y1, y2) + 18, x2, y2); p.endShape();
    }
    // heat shimmer above the line: as many waves as the loss share asks (none below 0,5 %)
    const nh = s.mahdoton ? 6 : Math.min(6, Math.floor(s.osuus / 2 + (s.osuus >= 0.5 ? 1 : 0)));
    p.stroke(...HEATC, 190); p.strokeWeight(2.5); p.noFill();
    for (let i = 0; i < nh; i++) {
      const x = 215 + i * 34, y0 = top - 4;
      p.beginShape(); for (let t = 0; t <= 1.001; t += 0.1) p.vertex(x + 5 * Math.sin(t * 2 * Math.PI), y0 - 34 * t); p.endShape();
    }
    // the town: houses with windows lit by the delivered share
    const lit = s.mahdoton ? 0 : s.perille / s.P;
    p.stroke(...INKC); p.strokeWeight(2); p.line(496, yg - 40, 512, yg - 40);
    for (const [x, w2, h] of [[512, 36, 56], [550, 40, 80]]) {
      p.fill(...SANDL); p.rect(x, yg - h, w2, h);
      const wc = SKY.map((v, i) => v + (HEATL[i] - v) * lit);
      p.fill(...wc); p.strokeWeight(1.5); p.rect(x + 7, yg - h + 10, 10, 10); p.rect(x + w2 - 17, yg - h + 10, 10, 10); p.strokeWeight(2);
    }
    // labels: generator voltage, transmission voltage and current, town side voltage
    lab(`$U = ${tx(s.U, 0)}\\,\\text{kV}$`, 300, top - 46 - fh * 0.4, 'c', fh, INKC);
    // under the ground line: the generator side and town side voltages and the line current
    lab(`$${UG}\\,\\text{kV}$`, 120, yl, 'c', fh, INKC);
    lab(`$I = ${tx(s.I, 0)}\\,\\text{A}$`, 300, yl, 'c', fh, s.mahdoton ? HOT : INKC);
    lab(`$${UG}\\,\\text{kV}$`, 480, yl, 'c', fh, INKC);
  }

  function trafo(x, y) {
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...ALU); p.rect(x - 16, y - 16, 32, 56, 3);
    p.fill(255); p.circle(x - 5, y, 18); p.noFill(); p.circle(x + 5, y, 18);
  }
  function pylon(x, yg, top) {
    p.stroke(...IRONC); p.strokeWeight(2.5); p.noFill();
    p.line(x - 16, yg, x - 3, top - 10); p.line(x + 16, yg, x + 3, top - 10);
    p.strokeWeight(1.2);
    for (let k = 0; k < 4; k++) {
      const y1 = yg - (yg - top) * k / 4, y2 = yg - (yg - top) * (k + 1) / 4;
      const h1 = 16 - 13 * k / 4, h2 = 16 - 13 * (k + 1) / 4;
      p.line(x - h1, y1, x + h2, y2); p.line(x + h1, y1, x - h2, y2);
    }
    p.strokeWeight(2.5); p.line(x - 24, top - 6, x + 24, top - 6);
    p.stroke(...INKC); p.strokeWeight(1.5); p.line(x, top - 6, x, top);
  }

  // --- the bars: delivered power (green) and loss (orange) to one scale, 500 MW = the full width ---
  function bars(s, fh, y0, y1) {
    const xb = 16 + fh * 5.2, wmax = 600 - xb - 16 - fh * 6.2, bh = Math.max(16, fh * 1.1);
    const sc = wmax / 500, gap = (y1 - y0 - 2 * bh) / 3;
    const ya = y0 + gap, yb = ya + bh + gap;
    p.noStroke(); p.fill(...MUTEDC); p.rect(xb, ya - 4, 1.5, yb - ya + bh + 8);
    lab(__('palkki_perille'), 16, ya + bh * 0.5 + fh * 0.35, 'l', fh, GREEN);
    lab('$P_\\text{h}$', 16, yb + bh * 0.5 + fh * 0.35, 'l', fh, HEATC);
    p.stroke(...INKC); p.strokeWeight(1.5);
    const wa = s.perille * sc, wb = Math.min(s.Ph, 500) * sc;
    p.fill(...GREEN); p.rect(xb, ya, Math.max(wa, 1), bh, 2);
    p.fill(...HEATC); p.rect(xb, yb, Math.max(wb, 1), bh, 2);
    // the sent power P as a dashed outline behind the delivered bar
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]); p.rect(xb, ya - 3, s.P * sc, bh + 6, 2); p.drawingContext.setLineDash([]);
    lab(s.mahdoton ? '$0\\,\\text{MW}$' : `$${mw(s.perille)}\\,\\text{MW}$`, xb + Math.max(wa, s.P * sc) + 8, ya + bh * 0.5 + fh * 0.35, 'l', fh, INKC);
    lab(s.mahdoton ? '$P_\\text{h} > P$' : `$${mw(s.Ph)}\\,\\text{MW}$`, xb + Math.min(wb, wmax) + 8, yb + bh * 0.5 + fh * 0.35, 'l', fh, s.mahdoton ? HOT : INKC);
  }

  // every canvas text: drawn and its ink box pushed to simState.labels (canvas coordinates)
  function lab(str, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(str), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(str, x0, y);
    labels.push({ s: str, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const mw = (x) => tx(x, x < 10 ? 2 : 1);                       // MW with two decimals below 10 MW, one above
  const nr = (x) => tx(x, Math.abs(x - Math.round(x)) < 1e-9 ? 0 : 1);   // a ratio: whole numbers without decimals
});
