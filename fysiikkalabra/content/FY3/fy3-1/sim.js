// fy3-1 Voima vuorovaikutuksen mittana: a mass on a spring scale (voimamittari) on different bodies.
// Physics: weight G = m g, with g the strength of gravity per kilogram (N/kg) on the chosen body.
// Mass is the same everywhere; only the weight changes. The spring stretch, the weight arrow and the bar
// heights are all proportional to G. The spring and the arrow use one fixed scale whose full value is the
// largest possible weight (100 kg on Jupiter, 2480 N), so they visibly change with the mass slider and with
// the chosen body. The bar chart is scaled to the current mass (full height = m · 24,8 N, the Jupiter bar),
// so the four bars always compare the bodies at a readable size; the scale is printed above the chart.
// The stretch and the arrow in simState are the pure proportional values (stretch = G / G_FULL * maxLen,
// arrow = G / G_FULL * ARROW_FULL, no offset); the drawing adds a fixed rest length to the spring, a 2 px
// minimum bar height and a 3 px minimum arrow length, only so that the smallest weights stay visible. The bar chart compares the weight of the same mass on all four bodies.
// The numeric readout (m, g, G) is DOM text so it stays readable on a phone; the canvas only draws.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const BODIES = [['Kuu', 1.62], ['Mars', 3.71], ['Maa', 9.81], ['Jupiter', 24.8]];   // g in N/kg
  const COLORS = [[110, 110, 110], [190, 90, 60], [47, 120, 160], [176, 120, 50]];
  const SPRING = { x: 110, top: 40, maxLen: 190 };             // spring scale on the left
  const BARS = { x: 270, y: 60, w: 300, h: 250 };              // bar chart on the right
  const G_MAX = 24.8;                                          // largest g
  const G_FULL = 100 * G_MAX;                                  // full scale: 100 kg on Jupiter = 2480 N
  const ARROW_FULL = 110;                                      // arrow length (px) at full scale; fits the canvas below the block
  let sM, lM, sel, lSel, readout;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    const l1 = p.createElement('label').parent(controls);
    lSel = p.createSpan('Taivaankappale').parent(l1);
    sel = p.createSelect().parent(l1);
    BODIES.forEach(([name]) => sel.option(name));
    sel.selected('Maa');
    const l2 = p.createElement('label').parent(controls);
    lM = p.createSpan('').parent(l2);
    sM = p.createSlider(1, 100, 10, 1).parent(l2);             // massa m (kg)
    p.createP('Massa on sama kaikkialla. Vain paino muuttuu, koska vuorovaikutus taivaankappaleen kanssa on erilainen.')
      .parent('sim-root').class('note');
    p.textFont('Arial');
  };

  p.draw = () => {
    const m = sM.value();
    const idx = Math.max(0, BODIES.findIndex(([name]) => name === sel.value()));
    const [body, g] = BODIES[idx];
    const G = m * g;                                           // weight in newtons
    const stretch = SPRING.maxLen * G / G_FULL;                // spring stretch (px), proportional to the weight G
    lM.html(`Massa m = ${m} kg`);
    readout.html(`<strong>Massa m = ${m} kg</strong> (sama kaikkialla)<br>g = ${fi(g, 2)} N/kg (${body})` +
                 `<br><strong>G = m · g = ${fi(G, 1)} N</strong>`);
    const arrow = ARROW_FULL * G / G_FULL;                     // weight arrow length (px), purely proportional to G
    const chartFull = m * G_MAX;                                // bar chart full scale: this mass on Jupiter
    const bars = BODIES.map(([, gg]) => (m * gg / chartFull) * (BARS.h - 30));   // bar heights (px), proportional to the weight at this mass
    window.simState = { m, body, g, G, stretch, arrow, bars, chartFull };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);

    // spring scale: the spring below the hook stretches in proportion to the weight
    p.stroke(60); p.strokeWeight(3); p.fill(60); p.rect(SPRING.x - 50, SPRING.top - 14, 100, 14, 3);
    const REST = 40, len = REST + stretch, yBottom = SPRING.top + len;
    p.noFill(); p.beginShape(); p.vertex(SPRING.x, SPRING.top);
    const turns = 9; for (let i = 1; i <= turns; i++) p.vertex(SPRING.x + (i % 2 ? -14 : 14), SPRING.top + len * i / (turns + 1));
    p.vertex(SPRING.x, yBottom); p.endShape();
    p.stroke(110); p.strokeWeight(2); p.drawingContext.setLineDash([5, 4]);                  // unloaded end of the spring
    p.line(SPRING.x - 62, SPRING.top + REST, SPRING.x - 24, SPRING.top + REST); p.drawingContext.setLineDash([]);
    p.stroke(60); p.strokeWeight(3);
    p.textSize(ts(13));
    const bs = Math.max(36 + 40 * Math.sqrt(m / 100), p.textWidth(`${m} kg`) + 16), by = yBottom;     // block grows a little with mass, never narrower than its label plus margin
    p.fill(COLORS[idx][0], COLORS[idx][1], COLORS[idx][2], 70); p.stroke(60); p.rect(SPRING.x - bs / 2, by, bs, bs, 5);
    p.noStroke(); p.fill(30); p.textAlign(p.CENTER); p.text(`${m} kg`, SPRING.x, by + bs / 2 + ts(5));
    const ax = SPRING.x + bs / 2 + 18, aLen = Math.max(3, arrow), hl = Math.min(14, aLen);   // weight arrow: length proportional to G (3 px floor only for the smallest weights)
    p.stroke(200, 40, 40); p.strokeWeight(3); p.line(ax, by + 6, ax, by + 6 + aLen - hl);
    p.fill(200, 40, 40); p.noStroke(); p.triangle(ax, by + 6 + aLen, ax - Math.max(3, hl / 2), by + 6 + aLen - hl, ax + Math.max(3, hl / 2), by + 6 + aLen - hl);
    p.textAlign(p.LEFT); p.textSize(ts(13)); p.text('G', ax + 10, by + 6 + aLen / 2 + 5);

    // bar chart: weight of the same mass on every body, chosen body highlighted
    p.stroke(60); p.strokeWeight(2); p.line(BARS.x, BARS.y + BARS.h, BARS.x + BARS.w, BARS.y + BARS.h); p.line(BARS.x, BARS.y + BARS.h, BARS.x, BARS.y);
    const bw = BARS.w / 4 - 16;
    BODIES.forEach(([name, gg], i) => {
      const val = m * gg, h = Math.max(2, bars[i]), x = BARS.x + 12 + i * (bw + 16);
      p.noStroke(); p.fill(COLORS[i][0], COLORS[i][1], COLORS[i][2], i === idx ? 255 : 200); p.rect(x, BARS.y + BARS.h - h, bw, h, 3);
      p.fill(60); p.textAlign(p.CENTER); p.textSize(ts(12)); p.text(name, x + bw / 2, BARS.y + BARS.h + ts(16));
      const vt = `${fi(val, val < 100 ? 1 : 0)} N`;                  // value label, shrunk if it would touch the neighbour's label
      if (p.textWidth(vt) > bw + 12) p.textSize(ts(12) * (bw + 12) / p.textWidth(vt));
      p.text(vt, x + bw / 2, BARS.y + BARS.h - h - 6);
    });
    p.fill(26, 77, 46); p.textAlign(p.CENTER); p.textSize(ts(13));   // title: shrunk to fit inside the canvas when the canvas is scaled down
    const title = 'Sama massa, paino eri paikoissa', titleMax = 2 * (600 - (BARS.x + BARS.w / 2)) - 10;
    if (p.textWidth(title) > titleMax) p.textSize(ts(13) * titleMax / p.textWidth(title));
    p.text(title, BARS.x + BARS.w / 2, BARS.y - ts(12));
    p.fill(60); p.textSize(ts(11)); p.text(`asteikko 0 – ${fi(chartFull, chartFull < 100 ? 1 : 0)} N (tämä massa Jupiterissa)`, BARS.x + BARS.w / 2, BARS.y + ts(2));
  };

  const fi = (x, d) => x.toFixed(d).replace('.', ',');         // Finnish decimal comma
});
