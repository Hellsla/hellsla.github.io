// fy3-2 Työ ja energia: a box pulled along a horizontal floor by a constant force along the motion.
// Physics: W = F s (force along the displacement), P = W / t.
// Work is also the area under the (s,F) graph; the right-hand plot fills that area as the box moves.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const FLOOR_Y = 250, X0 = 40, BOX = 40, PX_PER_M = 14;      // 20 m fits in the left half
  const G = { x: 360, y: 60, w: 220, h: 190 };                // (s,F) graph box
  let sF, sS, sT, lF, lS, lT, btn;
  let u = 0;                                                  // fraction of s covered so far, 0…1
  let running = false;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sF, lF] = slider(controls, 0, 100, 60, 1);      // voima F (N)
    [sS, lS] = slider(controls, 1, 20, 10, 0.5);     // matka s (m)
    [sT, lT] = slider(controls, 1, 20, 5, 0.5);      // aika t (s)
    btn = p.createButton('Vedä').parent(controls);
    btn.mousePressed(() => { u = 0; running = true; });
    p.textFont('system-ui, sans-serif');
  };

  p.draw = () => {
    const F = sF.value(), s = sS.value(), t = sT.value();
    const W = F * s;                       // work over the whole distance
    const P = W / t;                       // average power
    if (running) { u += (p.deltaTime / 1000) / t; if (u >= 1) { u = 1; running = false; } }
    const Wdone = W * u;                   // constant force: work grows linearly with distance

    lF.html(`Voima F = ${F} N`); lS.html(`Matka s = ${fi(s, 1)} m`); lT.html(`Aika t = ${fi(t, 1)} s`);
    window.simState = { F, s, t, W, P, u, Wdone, running };

    p.background(250);
    // readout
    p.noStroke(); p.fill(30); p.textAlign(p.LEFT); p.textSize(16);
    p.text(`W = F · s = ${fi(W, 0)} J`, 20, 30);
    p.text(`P = W / t = ${fi(P, 1)} W`, 20, 54);
    p.textSize(13); p.fill(90); p.text(`Tehty työ tähän mennessä: ${fi(Wdone, 0)} J`, 20, 78);

    // floor with a metre scale
    p.stroke(60); p.strokeWeight(2); p.line(0, FLOOR_Y, 330, FLOOR_Y);
    p.strokeWeight(1); p.textSize(11); p.textAlign(p.CENTER);
    for (let m = 0; m <= 20; m += 5) { const x = X0 + m * PX_PER_M; p.stroke(150); p.line(x, FLOOR_Y, x, FLOOR_Y + 5); p.noStroke(); p.fill(90); p.text(`${m} m`, x, FLOOR_Y + 18); }
    const xEnd = X0 + s * PX_PER_M;
    p.stroke(47, 111, 159); p.drawingContext.setLineDash([4, 4]); p.line(xEnd, FLOOR_Y - 70, xEnd, FLOOR_Y); p.drawingContext.setLineDash([]);

    // box and force arrow (100 N = 120 px)
    const bx = X0 + u * s * PX_PER_M, by = FLOOR_Y - BOX;
    p.noStroke(); p.fill(200, 120, 60); p.rect(bx - BOX / 2, by, BOX, BOX, 4);
    const ax = bx + BOX / 2, ay = by + BOX / 2, tipX = ax + F * 1.2;
    if (F > 0) { arrow(ax, ay, tipX, ay, p.color(200, 40, 40)); p.noStroke(); p.fill(200, 40, 40); p.textAlign(p.LEFT); p.textSize(13); p.text(`F = ${F} N`, ax + 6, ay - 12); }

    // (s,F) graph: the work done so far is the shaded area under the constant force
    p.stroke(60); p.strokeWeight(2); p.noFill();
    p.line(G.x, G.y + G.h, G.x + G.w, G.y + G.h); p.line(G.x, G.y + G.h, G.x, G.y);
    const yF = G.y + G.h - (F / 100) * (G.h - 20), xS = G.x + (s / 20) * (G.w - 20);
    p.noStroke(); p.fill(47, 111, 159, 90); if (F > 0) p.rect(G.x, yF, (xS - G.x) * u, G.y + G.h - yF);
    p.stroke(47, 111, 159); p.strokeWeight(3); if (F > 0) p.line(G.x, yF, xS, yF);
    p.strokeWeight(1); p.stroke(150); p.drawingContext.setLineDash([4, 4]); p.line(xS, yF, xS, G.y + G.h); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(90); p.textSize(12); p.textAlign(p.CENTER);
    p.text('s (m)', G.x + G.w, G.y + G.h + 30); p.text(`${fi(s, 1)}`, xS, G.y + G.h + 16);
    p.textAlign(p.RIGHT); p.text('F (N)', G.x - 6, G.y + 8); p.text(`${F}`, G.x - 6, yF + 4);
    p.textAlign(p.CENTER); p.fill(47, 111, 159); p.textSize(13); p.text('W = pinta-ala', G.x + G.w / 2, G.y - 10);

    // progress bar at the bottom
    const barX = 20, barY = 340, barW = 560, barH = 16;
    p.noFill(); p.stroke(120); p.strokeWeight(1); p.rect(barX, barY, barW, barH, 4);
    p.noStroke(); p.fill(47, 111, 159); if (W > 0) p.rect(barX, barY, barW * u, barH, 4);
    p.fill(90); p.textSize(12); p.textAlign(p.LEFT); p.text('0 J', barX, barY + 30); p.textAlign(p.RIGHT); p.text(`${fi(W, 0)} J`, barX + barW, barY + 30);
  };

  function arrow(x1, y1, x2, y2, col) {
    p.stroke(col); p.strokeWeight(3); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 10;
    p.fill(col); p.noStroke();
    p.triangle(x2, y2, x2 - L * Math.cos(a - 0.4), y2 - L * Math.sin(a - 0.4), x2 - L * Math.cos(a + 0.4), y2 - L * Math.sin(a + 0.4));
  }
  const fi = (x, d) => x.toFixed(d).replace('.', ',');   // Finnish decimal comma in the readout
});
