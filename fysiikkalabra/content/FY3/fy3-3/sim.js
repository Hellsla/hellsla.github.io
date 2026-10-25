// fy3-3 Kaasun mikromalli: particles in a box, temperature sets their speed, volume sets the box width.
// Physics (2D model): all particles have speed v = V_REF * sqrt(T / 300 K) and random directions, so the
// mean kinetic energy is proportional to T. Pressure is measured from the momentum the particles give the
// walls over the last second and a half, as force per wall length, and shown relative to the state
// 300 K, 1,00 dm³ (= 100). In this model p is proportional to T / V, which the readout also states as
// "teoria" so the measured value can be compared with it.
// The readout is DOM text; the canvas only draws. p5.js 1.9 instance mode, 600×400. Exposes window.simState.
new p5((p) => {
  const N = 80, R = 4, DT = 1 / 60, V_REF = 120;              // particles, radius, fixed time step, speed at 300 K (px/s)
  const BOX = { x: 40, y: 80, h: 200 };                       // left wall and height; width = 200 px per dm³
  const WINDOW = 90;                                          // frames in the pressure window (1,5 s)
  let sT, sV, lT, lV, readout, parts = [], hist = [], lastT = null;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  const speed = (T) => V_REF * Math.sqrt(T / 300);

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    p.randomSeed(7);                                          // fixed seed: the start is the same every time
    for (let i = 0; i < N; i++) {
      const a = p.random(p.TWO_PI);
      parts.push({ x: BOX.x + 20 + p.random(160), y: BOX.y + 20 + p.random(160), vx: Math.cos(a), vy: Math.sin(a) });   // unit direction
    }
    readout = p.createDiv('').parent('sim-root').class('readout');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sT, lT] = slider(controls, 100, 600, 300, 10);           // lämpötila T (K)
    [sV, lV] = slider(controls, 0.5, 2, 1, 0.1);              // tilavuus V (dm³)
    p.createP('Kun hiukkaset liikkuvat nopeammin tai astia on pienempi, ne osuvat seinään useammin ja kovempaa. Paine kasvaa.')
      .parent('sim-root').class('note');
    p.textFont('Arial');
  };

  p.draw = () => {
    const T = sT.value(), V = sV.value(), v = speed(T);
    const W = 200 * V, right = BOX.x + W, top = BOX.y, bottom = BOX.y + BOX.h;
    let ix = 0, iy = 0;                                       // momentum given to the x walls and y walls this frame
    for (const q of parts) {
      q.x += q.vx * v * DT; q.y += q.vy * v * DT;
      if (q.x < BOX.x + R)   { q.x = BOX.x + R;   if (q.vx < 0) { q.vx = -q.vx; ix += 2 * Math.abs(q.vx) * v; } }
      if (q.x > right - R)   { q.x = right - R;   if (q.vx > 0) { q.vx = -q.vx; ix += 2 * Math.abs(q.vx) * v; } }
      if (q.y < top + R)     { q.y = top + R;     if (q.vy < 0) { q.vy = -q.vy; iy += 2 * Math.abs(q.vy) * v; } }
      if (q.y > bottom - R)  { q.y = bottom - R;  if (q.vy > 0) { q.vy = -q.vy; iy += 2 * Math.abs(q.vy) * v; } }
    }
    hist.push([ix, iy]); if (hist.length > WINDOW) hist.shift();
    const t = hist.length * DT;
    const sx = hist.reduce((a, h) => a + h[0], 0), sy = hist.reduce((a, h) => a + h[1], 0);
    const pMeas = (sx / (t * 2 * BOX.h) + sy / (t * 2 * W)) / 2;           // momentum per time per wall length, averaged over both axes
    const pRef = N * V_REF * V_REF / (2 * 200 * BOX.h);                    // same model at 300 K and 1,00 dm³
    const pRel = 100 * pMeas / pRef, pTheory = 100 * (T / 300) / V;
    const theta = T - 273.15;
    lT.html(`Lämpötila T = ${T} K`); lV.html(`Tilavuus V = ${fi(V, 1)} dm³`);
    readout.html(`<strong>T = ${T} K = ${fi(theta, 0)} °C</strong>` +
                 `<br>Hiukkasten keskinopeus: ${fi(Math.sqrt(T / 300), 2)} × 300 K:n keskinopeus` +
                 `<br><strong>Paine p ≈ ${fi(pRel, 0)}</strong> (suhteellinen, 100 = 300 K ja 1,0 dm³), teoria ${fi(pTheory, 0)}`);
    window.simState = { T, theta, V, vRel: v / V_REF, pRel, pTheory, N, speedCheck: Math.hypot(parts[0].vx, parts[0].vy) * v };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (n) => Math.round(n * k);
    p.background(250);
    // box with the right wall as a piston
    p.stroke(60); p.strokeWeight(3); p.noFill(); p.line(BOX.x, top, BOX.x, bottom); p.line(BOX.x, top, right, top); p.line(BOX.x, bottom, right, bottom);
    p.strokeWeight(8); p.line(right, top - 6, right, bottom + 6);
    p.noStroke(); p.fill(26, 77, 46);
    for (const q of parts) p.circle(q.x, q.y, 2 * R);
    p.fill(90); p.textAlign(p.CENTER); p.textSize(ts(12)); p.text(`V = ${fi(V, 1)} dm³`, BOX.x + W / 2, bottom + ts(20));
    // thermometer on the right
    const tx = 540, ty = 70, th = 220, level = th * (T - 100) / 500;
    p.stroke(60); p.strokeWeight(2); p.fill(255); p.rect(tx - 8, ty, 16, th, 8);
    p.noStroke(); p.fill(200, 60, 40); p.rect(tx - 6, ty + th - level - 2, 12, level + 2, 6); p.circle(tx, ty + th + 12, 30);
    p.fill(90); p.textAlign(p.LEFT); p.textSize(ts(11)); p.text('600 K', tx + 14, ty + ts(8)); p.text('100 K', tx + 14, ty + th);
    p.textAlign(p.CENTER); p.text(`${T} K`, tx, ty + th + ts(46));
  };

  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');   // Finnish decimal comma and minus sign
});
