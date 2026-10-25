// fy3-10 Ideaalikaasun tilanyhtälö: the pressure of an ideal gas measured from wall hits in a 2D box.
// Physics: N point particles (mass m = 1) move freely in a box Lx × Ly and bounce elastically off the walls only
// (no particle–particle collisions: ideal gas). A hit on a side wall delivers the impulse 2m|vx|, on the top or bottom
// 2m|vy|. The measured pressure is the total impulse per unit time per unit wall length (the perimeter 2(Lx + Ly)),
// as a moving average over the last 2 s of simulated time.
// In 2D the area A plays the role of the volume and the ideal gas law reads pA = NkT, where the temperature fixes the
// mean kinetic energy per direction: <vx²> = <vy²> = kT/m. Kinetic theory gives p = Nm<v²>/(2A) = NkT/A, so relative
// to the reference state N = 100, T = 300 K, V = 100 %:   p/p_ref = (N/100)·(T/300 K)·(100 %/V).
// P_REF below is computed from pA = NkT, not measured. Units inside: px and s, v_rms = 240 px/s at 300 K.
// Randomness: positions, directions and speeds come from a seeded PRNG (mulberry32); the speed is the Box–Muller radius,
// i.e. the 2D Maxwell distribution. After a change of N the vx and vy components are rescaled so that the sample has
// exactly <vx²> = <vy²> = kT/m (the simulated temperature is the mean kinetic energy); a change of T rescales all speeds
// by √(T_new/T_old). The physics runs in fixed steps of 1/240 s, so the result does not depend on the frame rate.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame, and as test hooks
// window.simAdvance(s) (runs s simulated seconds at once) and window.simRestart() (the state right after loading).
new p5((p) => {
  const DT = 1 / 240, BIN = 24, NBINS = 20, SEED = 31;          // physics step (s), steps per 0,1 s bin, 20 bins = 2 s
  const LY = 280, LXMAX = 310, R = 3;                            // gas region height and full width (px), drawn radius
  const BOX = { x: 16, y: 76 };                                  // top-left corner of the gas region
  const V300 = 240, KT300 = V300 * V300 / 2;                     // v_rms at 300 K (px/s); kT/m = <v²>/2 in 2D
  const P_REF = 100 * KT300 / (LXMAX * LY);                      // p = NkT/A in the reference state (m = 1)
  const BAR = { ax: 404, x: [446, 540], w: 54, y0: 345, y1: 130 };   // pressure axis, bar centres, bar area
  let rnd, parts = [], N = 0, T = 300, Lx = LXMAX, acc = 0, bins = [], cur = 0, curSteps = 0, top = 0, tStep = 1;
  let sN, lN, sT, lT, sV, lV, readout;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  const mulberry32 = (a) => () => {                              // seeded PRNG, the same particles on every load
    a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  // n more particles from the seeded stream: uniform position, uniform direction, speed from the 2D Maxwell distribution
  const add = (n) => {
    for (let i = 0; i < n; i++) {
      const x = rnd() * Lx, y = rnd() * LY, th = 2 * Math.PI * rnd();
      const s = Math.sqrt(-2 * Math.log(1 - rnd()));            // Box–Muller radius: speed in units of √(kT/m)
      parts.push({ x, y, vx: s * Math.cos(th), vy: s * Math.sin(th) });
    }
  };
  const thermalize = () => {                                     // exact <vx²> = <vy²> = kT/m for the current T
    const kT = KT300 * T / 300; let sx = 0, sy = 0;
    for (const q of parts) { sx += q.vx * q.vx; sy += q.vy * q.vy; }
    const fx = Math.sqrt(kT * parts.length / sx), fy = Math.sqrt(kT * parts.length / sy);
    for (const q of parts) { q.vx *= fx; q.vy *= fy; }
  };
  const clearAvg = () => { bins = []; cur = 0; curSteps = 0; };
  // apply the sliders: wall position, temperature, particle number
  const sync = () => {
    const n = Number(sN.value()), t = Number(sT.value()), lx = LXMAX * Number(sV.value()) / 100;
    if (lx < Lx) for (const q of parts) if (q.x > lx) q.x *= lx / Lx;   // wall moved in: particles left outside go back in
    Lx = lx;
    if (t !== T) { const f = Math.sqrt(t / T); for (const q of parts) { q.vx *= f; q.vy *= f; } T = t; }   // v ∝ √T
    if (n !== N) { if (n > N) add(n - N); else parts.length = n; N = n; thermalize(); }
  };
  const restart = () => {
    rnd = mulberry32(SEED); parts = []; N = 0; T = Number(sT.value()); Lx = LXMAX * Number(sV.value()) / 100;
    sync(); clearAvg(); acc = 0;
  };
  // one fixed physics step: free flight, elastic wall bounces, impulse 2m|v⊥| per hit collected per unit wall length
  const step = () => {
    let J = 0;
    for (const q of parts) {
      q.x += q.vx * DT; q.y += q.vy * DT;
      if (q.x < 0) { q.x = -q.x; q.vx = -q.vx; J += 2 * Math.abs(q.vx); }
      else if (q.x > Lx) { q.x = 2 * Lx - q.x; q.vx = -q.vx; J += 2 * Math.abs(q.vx); }
      if (q.y < 0) { q.y = -q.y; q.vy = -q.vy; J += 2 * Math.abs(q.vy); }
      else if (q.y > LY) { q.y = 2 * LY - q.y; q.vy = -q.vy; J += 2 * Math.abs(q.vy); }
    }
    cur += J / (2 * (Lx + LY));
    if (++curSteps === BIN) { bins.push(cur); if (bins.length > NBINS) bins.shift(); cur = 0; curSteps = 0; }
  };
  const advance = (sec) => { acc += sec / DT; const n = Math.floor(acc + 1e-6); acc -= n; for (let i = 0; i < n; i++) step(); };
  // moving average of the pressure relative to p_ref, the state equation's prediction and their ratio
  const update = () => {
    const tAvg = (bins.length * BIN + curSteps) * DT, J = bins.reduce((a, b) => a + b, 0) + cur;
    const pMeasured = tAvg > 0 ? J / tAvg / P_REF : 0, Vrel = Number(sV.value()) / 100;
    const pPredicted = (N / 100) * (T / 300) / Vrel, vrms = Math.sqrt(parts.reduce((a, q) => a + q.vx * q.vx + q.vy * q.vy, 0) / N);
    window.simState = { N, T, Vrel, pMeasured, pPredicted, ratio: pMeasured / pPredicted, tAvg, vrms };
    return window.simState;
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const btn = p.createButton('Nollaa mittaus').parent(controls);
    btn.elt.addEventListener('click', clearAvg);
    [sN, lN] = slider(controls, 20, 200, 100, 10);               // hiukkasmäärä N
    [sT, lT] = slider(controls, 100, 600, 300, 10);              // lämpötila T (K)
    [sV, lV] = slider(controls, 25, 100, 100, 5);                // tilavuus V (% täydestä)
    p.createP('Hiukkaset törmäävät vain seiniin, eivät toisiinsa. Paine lasketaan seiniin osuvista törmäyksistä ' +
              'keskiarvona 2 s:n ajalta, joten mitattu arvo heiluu hieman. Oikea seinä liikkuu, kun tilavuutta muutetaan. ' +
              'Paineet ovat suhteessa vertailutilaan N = 100, T = 300 K, V = 100 %, jossa paine on 1,00.')
      .parent('sim-root').class('note');
    window.simAdvance = (s) => { sync(); advance(s); return update().pMeasured; };
    window.simRestart = () => { restart(); update(); };
    restart(); update();
    p.textFont('Arial');
  };

  p.draw = () => {
    sync(); advance(Math.min(p.deltaTime, 100) / 1000);
    const { Vrel, pMeasured: pm, pPredicted: pp, ratio, tAvg } = update();
    lN.html(`Hiukkasmäärä N = ${N}`); lT.html(`Lämpötila T = ${T} K`); lV.html(`Tilavuus V = ${fi(Vrel * 100, 0)} %`);
    readout.html(`N = ${N}, T = ${T} K, V = ${fi(Vrel * 100, 0)} % (vertailutila: N = 100, T = 300 K, V = 100 %)` +
      `<br>Mitattu paine p/p<sub>ref</sub> = <strong>${fi(pm, 2)}</strong> (keskiarvo ${fi(tAvg, 1)} s:n ajalta)` +
      `<br>Tilanyhtälön ennuste p/p<sub>ref</sub> = (N/100) · (T/300 K) · (100 %/V) = <strong>${fi(pp, 2)}</strong>` +
      `<br>Suhde mitattu/ennuste = pV/(NT) vertailutilaan verrattuna = <strong>${fi(ratio, 2)}</strong>`);

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);
    p.noStroke(); p.fill(40); p.textSize(ts(14));
    p.textAlign(p.LEFT); p.text(`V = ${fi(Vrel * 100, 0)} %`, BOX.x - R, 8 + ts(14));
    p.textAlign(p.RIGHT); p.text(`mitattu/ennuste = ${fi(ratio, 2)}`, 590, 8 + ts(14));

    // the box: dashed outline = V = 100 %, gas region, particles, fixed walls and the movable right wall (piston)
    const x0 = BOX.x - R, y0 = BOX.y - R, h = LY + 2 * R, wNow = Lx + 2 * R, wFull = LXMAX + 2 * R;
    p.noFill(); p.stroke(150); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]);
    p.rect(x0, y0, wFull, h); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(232, 240, 250); p.rect(x0, y0, wNow, h);
    p.fill(tempColor(T));
    for (const q of parts) p.circle(BOX.x + q.x, BOX.y + q.y, 2 * R);
    p.stroke(60); p.strokeWeight(4); p.noFill();
    p.line(x0, y0, x0 + wNow, y0); p.line(x0, y0 + h, x0 + wNow, y0 + h); p.line(x0, y0, x0, y0 + h);
    p.noStroke(); p.fill(90); p.rect(x0 + wNow, y0 - 8, 8, h + 16);
    p.rect(x0 + wNow + 8, y0 + h / 2 - 3, x0 + wFull + 12 - (x0 + wNow + 8), 6);

    // bars: measured and predicted relative pressure, axis scaled to the values shown (steps 1, 2 or 5 · 10ⁿ)
    const v = Math.max(pm, pp);
    if (v * 1.05 > top || v < 0.4 * top) [top, tStep] = scale(v);
    const Y = (x) => BAR.y0 - (BAR.y0 - BAR.y1) * Math.min(x, top * 1.05) / top, nT = Math.round(top / tStep);
    const dec = tStep < 0.1 ? 2 : tStep < 1 ? 1 : 0;              // decimals of the tick labels
    p.stroke(225); p.strokeWeight(1);
    for (let j = 1; j <= nT; j++) p.line(BAR.ax, Y(j * tStep), 590, Y(j * tStep));
    p.stroke(60); p.strokeWeight(2); p.line(BAR.ax, BAR.y0, 590, BAR.y0); p.line(BAR.ax, BAR.y0, BAR.ax, BAR.y1 - 10);
    if (top >= 1) {                                              // dashed line: the reference pressure 1
      p.stroke(120); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]); p.line(BAR.ax, Y(1), 590, Y(1)); p.drawingContext.setLineDash([]);
    }
    p.noStroke(); p.fill(60); p.textSize(ts(11)); p.textAlign(p.RIGHT);
    for (let j = 0; j <= nT; j++) p.text(j ? fi(j * tStep, dec) : '0', BAR.ax - 6, Y(j * tStep) + ts(4));   // ≥ 43 px apart
    const yName = 14 + ts(14) + ts(13);                          // axis name p/p_ref with a drawn subscript
    p.textSize(ts(10)); p.text('ref', 590, yName + ts(3)); const wSub = p.textWidth('ref');
    p.textSize(ts(13)); p.text('p/p', 590 - wSub - 1, yName);
    const cols = [[205, 80, 40], [60, 100, 170]], vals = [pm, pp], names = ['mitattu', 'ennuste'];
    for (let i = 0; i < 2; i++) {
      p.fill(...cols[i]); p.noStroke(); p.rect(BAR.x[i] - BAR.w / 2, Y(vals[i]), BAR.w, BAR.y0 - Y(vals[i]));
      p.fill(40); p.textAlign(p.CENTER); p.textSize(ts(13)); p.text(fi(vals[i], 2), BAR.x[i], Y(vals[i]) - 6);
      p.textSize(ts(12)); p.text(names[i], BAR.x[i], BAR.y0 + 4 + ts(12));
    }
  };

  // smallest axis top n·step ≥ 1,1·v with at most 5 steps of 1, 2 or 5 · 10ⁿ
  const scale = (v) => {
    for (let e = -2; e <= 2; e++) for (const m of [1, 2, 5]) {
      const st = m * 10 ** e, n = Math.max(1, Math.ceil(1.1 * v / st - 1e-9));
      if (n <= 5) return [n * st, st];
    }
    return [100, 20];
  };
  // 100 K blue, 600 K red
  function tempColor(t) { return p.lerpColor(p.color(40, 100, 210), p.color(215, 50, 40), (t - 100) / 500); }
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                   // Finnish decimal comma and minus sign
});
