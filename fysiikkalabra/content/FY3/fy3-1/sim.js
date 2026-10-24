// fy3-1 Työ ja energia: a box pulled along a horizontal floor by a rope at angle α.
// Physics: only the component of the force along the displacement does work,
//   W = F s cos α,   P = W / t.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const W_PX = 600, H_PX = 400, FLOOR_Y = 300, X0 = 60, BOX = 44;
  const PX_PER_M = 24;                       // 20 m fits in the canvas
  let sF, sAlpha, sS, sT, lF, lAlpha, lS, lT, btn;
  let u = 0;                                 // fraction of the distance s covered so far, 0…1
  let running = false;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };

  p.setup = () => {
    p.createCanvas(W_PX, H_PX).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sF, lF] = slider(controls, 0, 100, 60, 1);          // voima F (N)
    [sAlpha, lAlpha] = slider(controls, 0, 80, 30, 1);   // narun kulma α (°)
    [sS, lS] = slider(controls, 1, 20, 10, 0.5);         // matka s (m)
    [sT, lT] = slider(controls, 1, 20, 5, 0.5);          // aika t (s)
    btn = p.createButton('Vedä').parent(controls);
    btn.mousePressed(() => { u = 0; running = true; });
    p.textFont('system-ui, sans-serif');
  };

  p.draw = () => {
    const F = sF.value(), alpha = sAlpha.value(), s = sS.value(), t = sT.value();
    const rad = alpha * Math.PI / 180;
    const Fx = F * Math.cos(rad);            // horizontal component: the one that does work
    const Fy = F * Math.sin(rad);            // vertical component: does no work on a horizontal path
    const W = F * s * Math.cos(rad);         // total work over the whole distance
    const P = W / t;                         // average power

    // Animation: the box covers s in t seconds of real time (constant speed s/t).
    if (running) { u += (p.deltaTime / 1000) / t; if (u >= 1) { u = 1; running = false; } }
    const Wdone = W * u;                     // work done so far grows linearly with distance

    lF.html(`Voima F = ${F} N`);
    lAlpha.html(`Kulma α = ${alpha}°`);
    lS.html(`Matka s = ${fi(s, 1)} m`);
    lT.html(`Aika t = ${fi(t, 1)} s`);
    window.simState = { F, alpha, s, t, Fx, Fy, W, P, u, Wdone, running };

    p.background(250);
    // floor and distance scale
    p.stroke(60); p.strokeWeight(2); p.line(0, FLOOR_Y, W_PX, FLOOR_Y);
    p.strokeWeight(1); p.fill(90); p.noStroke(); p.textSize(12); p.textAlign(p.CENTER);
    for (let m = 0; m <= 20; m += 5) { const x = X0 + m * PX_PER_M; p.stroke(150); p.line(x, FLOOR_Y, x, FLOOR_Y + 6); p.noStroke(); p.text(`${m} m`, x, FLOOR_Y + 20); }
    // target marker at distance s
    const xEnd = X0 + s * PX_PER_M;
    p.stroke(47, 111, 159); p.drawingContext.setLineDash([4, 4]); p.line(xEnd, FLOOR_Y - 90, xEnd, FLOOR_Y); p.drawingContext.setLineDash([]);

    // box
    const bx = X0 + u * s * PX_PER_M, by = FLOOR_Y - BOX;
    p.noStroke(); p.fill(200, 120, 60); p.rect(bx - BOX / 2, by, BOX, BOX, 4);

    // rope and force vector from the box's right edge, scaled so 100 N = 150 px
    const ax = bx + BOX / 2, ay = by + BOX / 2, scale = 1.5;
    const tipX = ax + Fx * scale, tipY = ay - Fy * scale;
    p.stroke(120, 80, 40); p.strokeWeight(2); p.line(ax, ay, tipX, tipY);   // rope
    arrow(ax, ay, tipX, tipY, p.color(200, 40, 40));                         // F
    if (alpha > 0 && F > 0) {
      p.drawingContext.setLineDash([5, 5]);
      arrow(ax, ay, ax + Fx * scale, ay, p.color(47, 111, 159));            // F cos α
      p.stroke(150); p.line(ax + Fx * scale, ay, tipX, tipY);                // vertical component, dashed
      p.drawingContext.setLineDash([]);
    }
    p.noStroke(); p.textAlign(p.LEFT); p.textSize(13);
    p.fill(200, 40, 40); p.text(`F = ${F} N`, tipX + 8, tipY);
    if (alpha > 0) { p.fill(47, 111, 159); p.text(`F·cos α = ${fi(Fx, 1)} N`, ax + Fx * scale / 2 - 30, ay + 18); }

    // readout
    p.fill(30); p.textSize(16);
    p.text(`W = F · s · cos α = ${fi(W, 0)} J`, 20, 30);
    p.text(`P = W / t = ${fi(P, 1)} W`, 20, 54);
    p.textSize(13); p.fill(90);
    p.text(`Tehty työ tähän mennessä: ${fi(Wdone, 0)} J`, 20, 78);

    // work bar: fills as the box moves; full length corresponds to W
    const barX = 20, barY = 350, barW = 560, barH = 18;
    p.noFill(); p.stroke(120); p.rect(barX, barY, barW, barH, 4);
    p.noStroke(); p.fill(47, 111, 159); if (W > 0) p.rect(barX, barY, barW * u, barH, 4);
    p.fill(90); p.textSize(12); p.text('0 J', barX, barY + 32); p.textAlign(p.RIGHT); p.text(`${fi(W, 0)} J`, barX + barW, barY + 32); p.textAlign(p.LEFT);
  };

  function arrow(x1, y1, x2, y2, col) {
    p.stroke(col); p.strokeWeight(3); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 10;
    p.fill(col); p.noStroke();
    p.triangle(x2, y2, x2 - L * Math.cos(a - 0.4), y2 - L * Math.sin(a - 0.4), x2 - L * Math.cos(a + 0.4), y2 - L * Math.sin(a + 0.4));
  }
  const fi = (x, d) => x.toFixed(d).replace('.', ',');   // Finnish decimal comma in the readout
});
