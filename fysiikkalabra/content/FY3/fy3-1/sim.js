// fy3-1 Voima vuorovaikutuksen mittana: a mass on a spring scale (voimamittari) on different bodies.
// Physics: weight G = m g, with g the strength of gravity per kilogram (N/kg) on the chosen body.
// Mass is the same everywhere; only the weight changes. The spring stretches in proportion to G,
// and the bar chart compares the weight of the same mass on all four bodies.
// The numeric readout (m, g, G) is DOM text so it stays readable on a phone; the canvas only draws.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const BODIES = [['Kuu', 1.62], ['Mars', 3.71], ['Maa', 9.81], ['Jupiter', 24.8]];   // g in N/kg
  const COLORS = [[150, 150, 150], [190, 90, 60], [47, 120, 160], [200, 150, 90]];
  const SPRING = { x: 110, top: 40, maxLen: 190 };             // spring scale on the left
  const BARS = { x: 270, y: 60, w: 300, h: 250 };              // bar chart on the right
  const G_MAX = 24.8;                                          // largest g, sets the full scale
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
    const stretch = SPRING.maxLen * (G / (m * G_MAX));         // spring stretch relative to the same mass on Jupiter
    lM.html(`Massa m = ${m} kg`);
    readout.html(`<strong>Massa m = ${m} kg</strong> (sama kaikkialla)<br>g = ${fi(g, 2)} N/kg (${body})` +
                 `<br><strong>G = m · g = ${fi(G, 1)} N</strong>`);
    window.simState = { m, body, g, G, stretch };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);

    // spring scale: the spring below the hook stretches in proportion to the weight
    p.stroke(60); p.strokeWeight(3); p.fill(60); p.rect(SPRING.x - 50, SPRING.top - 14, 100, 14, 3);
    const len = 40 + stretch * 0.75, yBottom = SPRING.top + len;
    p.noFill(); p.beginShape(); p.vertex(SPRING.x, SPRING.top);
    const turns = 9; for (let i = 1; i <= turns; i++) p.vertex(SPRING.x + (i % 2 ? -14 : 14), SPRING.top + len * i / (turns + 1));
    p.vertex(SPRING.x, yBottom); p.endShape();
    const bs = 36 + 40 * Math.sqrt(m / 100), by = yBottom;     // block grows a little with mass
    p.fill(COLORS[idx][0], COLORS[idx][1], COLORS[idx][2], 70); p.stroke(60); p.rect(SPRING.x - bs / 2, by, bs, bs, 5);
    p.noStroke(); p.fill(30); p.textAlign(p.CENTER); p.textSize(ts(13)); p.text(`${m} kg`, SPRING.x, by + bs / 2 + ts(5));
    p.stroke(200, 40, 40); p.strokeWeight(3); p.line(SPRING.x + bs / 2 + 18, by + 6, SPRING.x + bs / 2 + 18, by + 6 + 50);   // weight arrow
    p.fill(200, 40, 40); p.noStroke(); p.triangle(SPRING.x + bs / 2 + 18, by + 64, SPRING.x + bs / 2 + 11, by + 50, SPRING.x + bs / 2 + 25, by + 50);
    p.textAlign(p.LEFT); p.textSize(ts(13)); p.text('G', SPRING.x + bs / 2 + 28, by + 40);

    // bar chart: weight of the same mass on every body, chosen body highlighted
    p.stroke(60); p.strokeWeight(2); p.line(BARS.x, BARS.y + BARS.h, BARS.x + BARS.w, BARS.y + BARS.h); p.line(BARS.x, BARS.y + BARS.h, BARS.x, BARS.y);
    const bw = BARS.w / 4 - 16;
    BODIES.forEach(([name, gg], i) => {
      const val = m * gg, h = (val / (m * G_MAX)) * (BARS.h - 30), x = BARS.x + 12 + i * (bw + 16);
      p.noStroke(); p.fill(COLORS[i][0], COLORS[i][1], COLORS[i][2], i === idx ? 255 : 90); p.rect(x, BARS.y + BARS.h - h, bw, h, 3);
      p.fill(60); p.textAlign(p.CENTER); p.textSize(ts(12)); p.text(name, x + bw / 2, BARS.y + BARS.h + ts(16));
      p.text(`${fi(val, val < 100 ? 1 : 0)} N`, x + bw / 2, BARS.y + BARS.h - h - 6);
    });
    p.fill(26, 77, 46); p.textAlign(p.CENTER); p.textSize(ts(13)); p.text('Sama massa, paino eri paikoissa', BARS.x + BARS.w / 2, BARS.y - ts(12));
  };

  const fi = (x, d) => x.toFixed(d).replace('.', ',');         // Finnish decimal comma
});
