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
// i.e. the 2D Maxwell distribution at the current T. After a change of N the vx and vy components are rescaled so the sample has
// exactly <vx²> = <vy²> = kT/m (the simulated temperature is the mean kinetic energy); a change of T rescales all speeds
// by √(T_new/T_old). The physics runs in fixed steps of 1/240 s, so the result does not depend on the frame rate.
// Picture: particle colour = speed (the same scale at every T, so a hotter gas turns orange), a trail = the path of the
// last 0,05 s (length ∝ speed), a flash = one wall hit (more N, higher T or smaller V → more flashes = more pressure).
// The gauge and the bars share one scale; the gauge needle and the measured bar have the colour of the wall flashes.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame, and as test hooks
// window.simAdvance(s) (runs s simulated seconds at once) and window.simRestart() (the state right after loading).
new p5((p) => {
  const DT = 1 / 240, BIN = 24, NBINS = 20, SEED = 31;          // physics step (s), steps per 0,1 s bin, 20 bins = 2 s
  const LY = 280, LXMAX = 310, R = 3;                            // gas region height and full width (px), drawn radius
  const BOX = { x: 16, y: 70 }, WT = 7, PW = 9;                  // top-left corner of the gas region, wall and piston (px)
  const V300 = 240, KT300 = V300 * V300 / 2;                     // v_rms at 300 K (px/s); kT/m = <v²>/2 in 2D
  const P_REF = 100 * KT300 / (LXMAX * LY);                      // p = NkT/A in the reference state (m = 1)
  const BAR = { ax: 414, x: [450, 548], w: 50, y0: 345, y1: 165 };   // pressure axis, bar centres, bar area
  const GA = { x: 48, y: 31, r: 26 };                            // pressure gauge on the top wall
  const LV = { x0: 440, x1: 560, lo: 0.8, hi: 1.2 };             // ratio level: track ends and the range shown
  const MEAS = [205, 45, 125], FLASH = [255, 90, 175], PRED = [140, 147, 160];   // measured pressure, wall hit, prediction
  const SLOW = [60, 130, 255], MID = [245, 215, 80], FAST = [255, 120, 30], VMAX = 420;   // speed scale 0…420 px/s
  const TAIL = 0.05, HN = 256, FL = 30;                          // trail (s), stored hits, flash life (steps = 0,125 s)
  const mix = (a, b, f) => a.map((x, i) => Math.round(x + (b[i] - x) * f));
  const PAL = Array.from({ length: 32 }, (_, i) => i < 16 ? mix(SLOW, MID, i / 15.5) : mix(MID, FAST, (i - 16) / 15));
  const hw = new Int8Array(HN), hs = new Float32Array(HN), hv = new Float32Array(HN), hn = new Int32Array(HN);   // hit ring
  let rnd, parts = [], N = 0, T = 300, Lx = LXMAX, acc = 0, bins = [], hbins = [], cur = 0, hcur = 0, curSteps = 0, top = 0, tStep = 1;
  let sN, lN, sT, lT, sV, lV, readout, nStep = 0, hi = 0, needle = 0;

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
    const u = Math.sqrt(KT300 * T / 300);                        // √(kT/m) at the current T, so new particles are thermal too
    for (let i = 0; i < n; i++) {
      const x = rnd() * Lx, y = rnd() * LY, th = 2 * Math.PI * rnd();
      const s = Math.sqrt(-2 * Math.log(1 - rnd()));            // Box–Muller radius: speed in units of √(kT/m)
      parts.push({ x, y, vx: u * s * Math.cos(th), vy: u * s * Math.sin(th) });
    }
  };
  const thermalize = () => {                                     // exact <vx²> = <vy²> = kT/m for the current T
    const kT = KT300 * T / 300; let sx = 0, sy = 0;
    for (const q of parts) { sx += q.vx * q.vx; sy += q.vy * q.vy; }
    const fx = Math.sqrt(kT * parts.length / sx), fy = Math.sqrt(kT * parts.length / sy);
    for (const q of parts) { q.vx *= fx; q.vy *= fy; }
  };
  const clearAvg = () => { bins = []; hbins = []; cur = 0; hcur = 0; curSteps = 0; };
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
    sync(); clearAvg(); acc = 0; nStep = 0; hn.fill(-FL);
  };
  // wall w (0 left, 1 right, 2 top, 3 bottom), position s along it, normal speed v: kept only for drawing the flash
  const hit = (w, s, v) => { hw[hi] = w; hs[hi] = s; hv[hi] = v; hn[hi] = nStep; hi = (hi + 1) % HN; hcur++; return 2 * v; };
  // one fixed physics step: free flight, elastic wall bounces, impulse 2m|v⊥| per hit collected per unit wall length
  const step = () => {
    let J = 0;
    for (const q of parts) {
      q.x += q.vx * DT; q.y += q.vy * DT;
      if (q.x < 0) { q.x = -q.x; q.vx = -q.vx; J += hit(0, q.y, Math.abs(q.vx)); }
      else if (q.x > Lx) { q.x = 2 * Lx - q.x; q.vx = -q.vx; J += hit(1, q.y, Math.abs(q.vx)); }
      if (q.y < 0) { q.y = -q.y; q.vy = -q.vy; J += hit(2, q.x, Math.abs(q.vy)); }
      else if (q.y > LY) { q.y = 2 * LY - q.y; q.vy = -q.vy; J += hit(3, q.x, Math.abs(q.vy)); }
    }
    cur += J / (2 * (Lx + LY)); nStep++;
    if (++curSteps === BIN) { bins.push(cur); hbins.push(hcur); if (bins.length > NBINS) { bins.shift(); hbins.shift(); } cur = hcur = curSteps = 0; }
  };
  const advance = (sec) => { acc += sec / DT; const n = Math.floor(acc + 1e-6); acc -= n; for (let i = 0; i < n; i++) step(); };
  // moving average of the pressure relative to p_ref, the state equation's prediction and their ratio
  const update = () => {
    const tAvg = (bins.length * BIN + curSteps) * DT, J = bins.reduce((a, b) => a + b, 0) + cur;
    const pMeasured = tAvg > 0 ? J / tAvg / P_REF : 0, Vrel = Number(sV.value()) / 100;
    const pPredicted = (N / 100) * (T / 300) / Vrel, vrms = Math.sqrt(parts.reduce((a, q) => a + q.vx * q.vx + q.vy * q.vy, 0) / N);
    const sp = parts.map((q) => Math.hypot(q.vx, q.vy)).sort((a, b) => a - b), vmed = (sp[(N - 1) >> 1] + sp[N >> 1]) / 2;
    const hitRate = tAvg > 0 ? (hbins.reduce((a, b) => a + b, 0) + hcur) / tAvg : 0;   // wall hits per second = flashes
    window.simState = { N, T, Vrel, pMeasured, pPredicted, ratio: pMeasured / pPredicted, tAvg, vrms, vmed, hitRate };
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
      `<br>Suhde mitattu/ennuste (= pV/(NT) suhteessa vertailutilaan) = <strong>${fi(ratio, 2)}</strong>`);

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k), ctx = p.drawingContext;
    const grad = (x0, y0, x1, y1, stops) => {                    // linear gradient, stops = [[offset, css colour], …]
      const g = ctx.createLinearGradient(x0, y0, x1, y1); for (const [o, c] of stops) g.addColorStop(o, c); return g; };
    const rgb = (c, a = 1) => `rgba(${c[0]},${c[1]},${c[2]},${a})`;
    const rect = (x, y, w, h, fill) => { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); };
    const steel = (x, y, w, h, across) => rect(x, y, w, h, grad(x, y, across ? x + w : x, across ? y : y + h,
      [[0, '#79828d'], [0.45, '#dfe3e8'], [1, '#5d6570']]));
    const labels = [];
    const lab = (str, x, y, align = p.LEFT) => {                 // draws a canvas text and records its box for the label test
      p.textAlign(align); p.text(str, x, y);
      const w = p.textWidth(str), x0l = align === p.CENTER ? x - w / 2 : align === p.RIGHT ? x - w : x;
      labels.push({ s: str, x0: x0l, y0: y - p.textAscent(), x1: x0l + w, y1: y + p.textDescent() });
    };
    p.background(250);
    const v = Math.max(pm, pp);                                  // one scale (1, 2 or 5 · 10ⁿ) for the gauge and the bars
    if (v * 1.05 > top || v < 0.4 * top) [top, tStep] = scale(v);
    const nT = Math.round(top / tStep), yT = 8 + ts(14);

    // the cylinder: dark gas region, air behind the piston, steel walls, piston plate, rod and handle
    const x0 = BOX.x - R, y0 = BOX.y - R, h = LY + 2 * R, wNow = Lx + 2 * R, wFull = LXMAX + 2 * R, xp = x0 + wNow;
    rect(x0, y0, wNow, h, grad(0, y0, 0, y0 + h, [[0, '#24314d'], [1, '#121a2b']]));
    rect(xp, y0, wFull + PW - wNow, h, grad(0, y0, 0, y0 + h, [[0, '#f1f4f8'], [1, '#dce2ea']]));
    steel(x0 - WT, y0 - WT, wFull + PW + WT, WT); steel(x0 - WT, y0 + h, wFull + PW + WT, WT); steel(x0 - WT, y0, WT, h, true);
    steel(xp, y0, PW, h, true); steel(xp + PW, y0 + h / 2 - 3, 20, 6);
    p.noStroke(); p.fill(55, 62, 72); p.rect(xp + PW + 18, y0 + h / 2 - 11, 9, 22, 3);

    // particles: trail back along the velocity (cut at the walls), then a sphere coloured by speed with a highlight
    const col = (q) => PAL[Math.min(31, Math.floor(32 * Math.hypot(q.vx, q.vy) / VMAX))];
    p.strokeWeight(2);
    for (const q of parts) {
      let t = TAIL;
      if (q.vx) t = Math.min(t, Math.max(0, q.vx > 0 ? q.x / q.vx : (q.x - Lx) / q.vx));
      if (q.vy) t = Math.min(t, Math.max(0, q.vy > 0 ? q.y / q.vy : (q.y - LY) / q.vy));
      const c = col(q), x = BOX.x + q.x, y = BOX.y + q.y, hx = x - q.vx * t / 2, hy = y - q.vy * t / 2;   // fading in 2 parts
      p.stroke(c[0], c[1], c[2], 150); p.line(x, y, hx, hy); p.stroke(c[0], c[1], c[2], 60); p.line(hx, hy, x - q.vx * t, y - q.vy * t);
    }
    p.noStroke();
    for (const q of parts) { const c = col(q); p.fill(c[0], c[1], c[2]); p.circle(BOX.x + q.x, BOX.y + q.y, 2 * R + 1); }
    p.fill(255, 255, 255, 190);
    for (const q of parts) p.circle(BOX.x + q.x - 1, BOX.y + q.y - 1, 2.4);

    // wall flashes: one per hit in the last 0,125 s, size ∝ normal speed, fading with age
    for (let i = 0; i < HN; i++) {
      const a = 1 - (nStep - hn[i]) / FL, w = hw[i], s = hs[i];
      if (a <= 0 || a > 1 || (w > 1 && s > Lx)) continue;
      const len = 6 + 16 * Math.min(1, hv[i] / VMAX) * (0.5 + a / 2), side = w < 2;
      const cx = w === 0 ? x0 : w === 1 ? xp : BOX.x + s, cy = w === 2 ? y0 : w === 3 ? y0 + h : BOX.y + s;
      p.fill(...FLASH, 230 * a); p.ellipse(cx, cy, side ? 5 : len, side ? len : 5);
      p.fill(255, 255, 255, 220 * a); p.ellipse(cx, cy, side ? 2 : len / 2, side ? len / 2 : 2);
    }

    // pressure gauge on the top wall: ticks at the bar axis steps, grey mark = prediction, needle = measured pressure
    const ang = (x) => Math.PI * (0.75 + 1.5 * Math.min(x / top, 1.05) / 1.05);
    steel(GA.x - 3, GA.y + GA.r - 2, 6, y0 - WT - GA.y - GA.r + 2, true);
    p.fill(70, 78, 88); p.circle(GA.x, GA.y, 2 * GA.r); p.fill(252, 252, 248); p.circle(GA.x, GA.y, 2 * GA.r - 6);
    p.stroke(60); p.strokeWeight(1.2);
    for (let j = 0; j <= nT; j++) { const a = ang(j * tStep); p.line(GA.x + 15 * Math.cos(a), GA.y + 15 * Math.sin(a), GA.x + 21 * Math.cos(a), GA.y + 21 * Math.sin(a)); }
    const ap = ang(pp); p.noStroke(); p.fill(...PRED); p.circle(GA.x + 18 * Math.cos(ap), GA.y + 18 * Math.sin(ap), 6);
    needle += (Math.min(pm / top, 1.05) - needle) * 0.25;
    const an = Math.PI * (0.75 + 1.5 * needle / 1.05);
    p.stroke(...MEAS); p.strokeWeight(2.5); p.line(GA.x, GA.y, GA.x + 20 * Math.cos(an), GA.y + 20 * Math.sin(an));
    p.noStroke(); p.fill(40); p.circle(GA.x, GA.y, 6);
    p.textSize(ts(11)); lab('p', GA.x, GA.y + GA.r - 6, p.CENTER);

    // speed legend (top), volume as a dimension line and the flash legend (bottom)
    p.textSize(ts(12)); p.fill(40);
    const lx0 = 84 + p.textWidth('hidas') + 5, lw = k > 1.5 ? 32 : 44, xF = 404 - p.textWidth('osuma seinään');
    lab('hidas', 84, yT); rect(lx0, yT - ts(4) - 4, lw, 8, grad(lx0, 0, lx0 + lw, 0, [[0, rgb(SLOW)], [0.5, rgb(MID)], [1, rgb(FAST)]]));
    p.fill(40); lab('nopea', lx0 + lw + 5, yT); lab('osuma seinään', xF, 388);
    p.fill(...FLASH); p.ellipse(xF - 10, 388 - ts(4), 5, 16); p.fill(255); p.ellipse(xF - 10, 388 - ts(4), 2, 8);
    p.textSize(ts(13)); const wV = p.textWidth('V = 100 %') / 2, yD = 368;      // V label between the left edge and the legend
    const xm = Math.min(xF - 30 - wV, Math.max(x0 + 2 + wV, (x0 + xp) / 2));
    p.stroke(80); p.strokeWeight(1.2); p.line(x0, yD, xp, yD); p.line(x0, yD - 5, x0, yD + 5); p.line(xp, yD - 5, xp, yD + 5);
    p.noStroke(); p.fill(80); p.triangle(x0, yD, x0 + 7, yD - 3.5, x0 + 7, yD + 3.5); p.triangle(xp, yD, xp - 7, yD - 3.5, xp - 7, yD + 3.5);
    p.fill(40); lab(`V = ${fi(Vrel * 100, 0)} %`, xm, 388, p.CENTER);

    // ratio measured/predicted as a level: bubble on a 0,8…1,2 track, green zone 0,95…1,05
    const lx = (r) => LV.x0 + (LV.x1 - LV.x0) * (Math.min(Math.max(r, LV.lo), LV.hi) - LV.lo) / (LV.hi - LV.lo), yL = yT + 8 + ts(14);
    p.textSize(ts(13)); lab(`mitattu/ennuste = ${fi(ratio, 2)}`, 590, yT, p.RIGHT);
    p.stroke(150); p.strokeWeight(1); p.fill(238, 241, 236); p.rect(LV.x0 - 7, yL - 7, LV.x1 - LV.x0 + 14, 14, 7);
    p.noStroke(); p.fill(175, 222, 170); p.rect(lx(0.95), yL - 6, lx(1.05) - lx(0.95), 12);
    p.stroke(90); for (const r of [0.9, 1, 1.1]) { p.line(lx(r), yL - 7, lx(r), yL - 3); p.line(lx(r), yL + 3, lx(r), yL + 7); }
    p.noStroke(); p.fill(...MEAS); p.circle(lx(ratio), yL, 10); p.fill(255, 255, 255, 200); p.circle(lx(ratio) - 1.5, yL - 1.5, 3);
    p.fill(60); p.textSize(ts(11)); lab('0,8', LV.x0 - 11, yL + ts(4), p.RIGHT); lab('1,2', LV.x1 + 11, yL + ts(4), p.LEFT);

    // bars: measured and predicted relative pressure, axis scaled to the values shown, gridlines, reference line 1
    const Y = (x) => BAR.y0 - (BAR.y0 - BAR.y1) * Math.min(x, top * 1.05) / top;
    const dec = tStep < 0.1 ? 2 : tStep < 1 ? 1 : 0;              // decimals of the tick labels
    p.stroke(225); p.strokeWeight(1);
    for (let j = 1; j <= nT; j++) p.line(BAR.ax, Y(j * tStep), 590, Y(j * tStep));
    p.stroke(60); p.strokeWeight(2); p.line(BAR.ax, BAR.y0, 590, BAR.y0); p.line(BAR.ax, BAR.y0, BAR.ax, BAR.y1 - 10);
    if (top >= 1) {                                              // dashed line: the reference pressure 1
      p.stroke(120); p.strokeWeight(1.5); ctx.setLineDash([5, 4]); p.line(BAR.ax, Y(1), 590, Y(1)); ctx.setLineDash([]);
    }
    p.noStroke(); p.fill(60); p.textSize(ts(11));
    for (let j = 0; j <= nT; j++) lab(j ? fi(j * tStep, dec) : '0', BAR.ax - 6, Y(j * tStep) + ts(4), p.RIGHT);   // ≥ 43 px apart
    const yName = yL + 14 + ts(13);                              // axis name p/p_ref with a drawn subscript
    p.textSize(ts(11)); lab('ref', 590, yName + ts(3), p.RIGHT); const wSub = p.textWidth('ref');
    p.textSize(ts(13)); lab('p/p', 590 - wSub - 1, yName, p.RIGHT);
    const cols = [MEAS, PRED], vals = [pm, pp], names = ['mitattu', 'ennuste'];
    for (let i = 0; i < 2; i++) {
      const bx = BAR.x[i] - BAR.w / 2, by = Y(vals[i]), c = cols[i];
      rect(bx, by, BAR.w, BAR.y0 - by, grad(bx, 0, bx + BAR.w, 0, [[0, rgb(c, 0.85)], [0.35, rgb(mix(c, [255, 255, 255], 0.35))], [1, rgb(mix(c, [0, 0, 0], 0.25))]]));
      p.fill(40); p.textSize(ts(13)); lab(fi(vals[i], 2), BAR.x[i], by - 6, p.CENTER);
      p.textSize(ts(12)); lab(names[i], BAR.x[i], BAR.y0 + 4 + ts(12), p.CENTER);
    }
    window.simState.labels = labels;
  };

  // smallest axis top n·step ≥ 1,1·v with at most 5 steps of 1, 2 or 5 · 10ⁿ
  const scale = (v) => {
    for (let e = -2; e <= 2; e++) for (const m of [1, 2, 5]) {
      const st = m * 10 ** e, n = Math.max(1, Math.ceil(1.1 * v / st - 1e-9));
      if (n <= 5) return [n * st, st];
    }
    return [100, 20];
  };
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                   // Finnish decimal comma and minus sign
});
