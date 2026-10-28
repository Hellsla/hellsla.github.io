// fy3-14 Lämpötasapaino olomuodon muuttuessa: ice is dropped into water in an insulated calorimeter.
// Physics (energy is conserved, no losses): the heat the water gives off cooling to 0 °C is Q_v = c_v m_v T_v. The ice needs
// Q_lämm = c_j m_j (0 − T_j) to warm to 0 °C and Q_sul = s m_j to melt completely (c_v = 4190, c_j = 2100 J/(kg·K), s = 334 kJ/kg).
//   Q_v ≥ Q_lämm + Q_sul : all ice melts, T = (Q_v − Q_lämm − Q_sul) / (c_v (m_v + m_j)) ≥ 0 °C.
//   Q_lämm ≤ Q_v < Q_lämm + Q_sul : ice remains, T = 0 °C, melted mass (Q_v − Q_lämm)/s.
//   Q_v < Q_lämm : the cold ice freezes part of the water, m_f = (Q_lämm − Q_v)/s; while m_f ≤ m_v the mixture stays at 0 °C,
//     otherwise all water freezes and T = (c_v m_v T_v + s m_v + c_j m_j T_j) / (c_j (m_j + m_v)) < 0 °C.
// Animation: the heat q that has flowed from the water to the ice grows as q = u(t)·Q_end, where Q_end is the heat moved by
// the end state and u(t) = (1 − e^(−t/τ)) / (1 − e^(−T_END/τ)), τ = 1,8 s, so the run lasts 8 s (the pace is ILLUSTRATION ONLY;
// the real rate depends on stirring and cube size). Every displayed state is derived from q in sequence, never interpolated:
//   water side (gives off q): cools to 0 °C (q ≤ Q_v), then freezes at 0 °C, then (all frozen) the new ice cools below 0 °C;
//   ice side (receives q): warms to 0 °C (q ≤ Q_lämm), then melts at 0 °C, then (all melted) the melt water warms.
// So liquid water is never shown below 0 °C and ice never above 0 °C, and ice melts only once it has reached 0 °C.
// The chart on the right is the energy budget, to scale: what the water gives off against what the ice needs. Its axis
// is the smallest of 0–50, 0–100 and 0–250 kJ that holds both bars, so the decisive comparison fills the chart.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. The readout is DOM text: quantities and values only; the model's
// assumptions and the formulas are in the lesson's "Mallin oletukset" and "Laskennan selitys" boxes (inquiry.json).
// Speed control: the animation clock advances by (real frame time)·speed, so "Nopeus" changes only the pace; the end state
// and every quantity at a given point of the animation clock are the same at every speed.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels (test_sims.py sweeps them).
new p5((p) => {
  const CV = 4190, CJ = 2100, S = 334000;                       // c water, c ice (J/(kg·K)), specific heat of fusion (J/kg)
  const TAU = 1.8, T_END = 8, SCALES = [50, 100, 250];          // time constant (s), animation length (s), chart axis maxima (kJ)
  const VES = { x: 34, w: 210, top: 150, bottom: 358, wall: 14 };   // insulated vessel (outer box)
  const CH = { ax: 352, y0: 318, y1: 62, bw: 52, bx: [380, 478] };   // chart: axis x, bottom y, top y (axis max), bar width, bar x
  let sMW, lMW, sTW, lTW, sMI, lMI, sTI, lTI, sSp, readout;
  let tAnim = 0, running = false, key = '', labels = [], k = 1;
  const inputKey = () => [sMW, sTW, sMI, sTI].map((e) => e.value()).join();

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label).style('white-space', 'nowrap');   // value never wraps alone onto a second line
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    // controls right under the canvas with Sekoita first, so canvas + button fit on one phone screen; the long readout follows
    const controls = p.createDiv('').parent('sim-root').class('controls');
    p.createButton(__('sekoita')).parent(controls).mousePressed(() => { tAnim = 0; running = true; key = inputKey(); });
    [sMW, lMW] = slider(controls, 0.10, 0.50, 0.30, 0.01);    // veden massa (kg)
    [sTW, lTW] = slider(controls, 0, 80, 20, 0.5);            // veden alkulämpötila (°C)
    [sMI, lMI] = slider(controls, 0.05, 0.50, 0.10, 0.01);    // jään massa (kg)
    [sTI, lTI] = slider(controls, -40, 0, 0, 1);              // jään alkulämpötila (°C)
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(lv); sSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) sSp.option(txt, v);
    sSp.selected('1');                                         // pace only: not part of inputKey, so it never resets the run
    readout = p.createDiv('').parent('sim-root').class('readout');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { mW: { input: sMW.elt, unit: 'kg' }, TW0: { input: sTW.elt, unit: '°C' }, mI: { input: sMI.elt, unit: 'kg' }, TI0: { input: sTI.elt, unit: '°C' } },
      reset: () => { sMW.value(0.30); sTW.value(20); sMI.value(0.10); sTI.value(0); sSp.selected('1'); tAnim = 0; running = false; key = inputKey(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  // the end state from the initial values (SI units): heats in J, masses in kg, temperatures in °C
  const solve = (mW, TW0, mI, TI0) => {
    const Qv = CV * mW * TW0, Qwarm = CJ * mI * (0 - TI0), Qmelt = S * mI;
    let Tf, iceLeft, tapaus;
    if (Qv >= Qwarm + Qmelt) { tapaus = 1; Tf = (Qv - Qwarm - Qmelt) / (CV * (mW + mI)); iceLeft = 0; }          // all ice melts
    else if (Qv >= Qwarm) { tapaus = 2; Tf = 0; iceLeft = mI - (Qv - Qwarm) / S; }                              // ice remains at 0 °C
    else {
      const mF = (Qwarm - Qv) / S;                                                                              // water frozen by the cold ice
      if (mF <= mW) { tapaus = 3; Tf = 0; iceLeft = mI + mF; }
      else { tapaus = 4; Tf = (Qv + S * mW + CJ * mI * TI0) / (CJ * (mI + mW)); iceLeft = mI + mW; }           // everything freezes, below 0 °C
    }
    // heat moved from the water to the ice by the end state (J)
    const Qend = [Qv - CV * mW * Tf, Qv, Qwarm, Qv + S * mW - CJ * mW * Tf][tapaus - 1];
    return { Qv, Qwarm, Qmelt, Tf, iceLeft, tapaus, Qend };
  };

  // the state after heat q (J) has flowed from the water to the ice, each side in sequence
  const stateAt = (mW, TW0, mI, TI0, R, q) => {
    let TW, frozen, TI, melted, Tmelt = 0;
    if (q <= R.Qv) { TW = TW0 - q / (CV * mW); frozen = 0; }                                  // water cools to 0 °C
    else if (q <= R.Qv + S * mW) { TW = 0; frozen = (q - R.Qv) / S; }                          // then freezes at 0 °C
    else { TW = -(q - R.Qv - S * mW) / (CJ * mW); frozen = mW; }                               // all frozen: the new ice cools
    if (q <= R.Qwarm) { TI = Math.min(0, TI0 + q / (CJ * mI)); melted = 0; }              // ice warms to 0 °C
    else if (q <= R.Qwarm + R.Qmelt) { TI = 0; melted = (q - R.Qwarm) / S; }                   // then melts at 0 °C
    else { TI = 0; melted = mI; Tmelt = (q - R.Qwarm - R.Qmelt) / (CV * mI); }                 // all melted: the melt water warms
    return { TW, TI, Tmelt, iceNow: mI - melted + frozen, waterNow: mW - frozen + melted };
  };

  p.draw = () => {
    const mW = Number(sMW.value()), TW0 = Number(sTW.value()), mI = Number(sMI.value()), TI0 = Number(sTI.value());
    const R = solve(mW, TW0, mI, TI0), { Qv, Qwarm, Qmelt, Tf, iceLeft, tapaus, Qend } = R, M = mW + mI;
    if (inputKey() !== key) { key = inputKey(); tAnim = 0; running = false; }   // any change of the inputs takes the ice out again
    if (running) { tAnim += Math.min(p.deltaTime, 100) / 1000 * Number(sSp.value());   // clamped: a resume after an off-screen pause cannot skip the motion
                  if (tAnim >= T_END) { tAnim = T_END; running = false; } }
    const immersed = running || tAnim > 0;
    const u = tAnim >= T_END ? 1 : (1 - Math.exp(-tAnim / TAU)) / (1 - Math.exp(-T_END / TAU));   // illustrative progress 0 → 1
    const q = u * Qend, { TW, TI, Tmelt, iceNow, waterNow } = stateAt(mW, TW0, mI, TI0, R, q);   // the state after heat q, in sequence
    // once all the ice has melted a stirred thermometer reads the mixed temperature, not the original water's
    const allMelted = tapaus === 1 && iceNow < 0.0005, TWd = allMelted ? (mW * TW + mI * Tmelt) / M : TW;
    const meltedG = (mI - iceLeft) * 1000;                      // net mass melted (g); negative when water freezes

    lMW.html(__(`veden_massa`, {mw: tx(mW, 2)})); lTW.html(__(`veden_alkulampotila`, {tw0: tx(TW0, 1), deg: DEG}));
    lMI.html(__(`jaan_massa`, {mi: tx(mI, 2)})); lTI.html(__(`jaan_alkulampotila`, {ti0: tx(TI0, 0), deg: DEG}));
    readout.html(__(`lopputila_jaata_jaljella`, {tf: tx(Tf, 1), deg: DEG, iceleft: tx(iceLeft * 1000, 1)}) +
                 __(`vesi_luovuttaa_jaahtyessaan`, {deg: DEG, qv: tk(Qv)}) +
                 __(`jaan_lammitys_seen`, {deg: DEG, qwarm: tk(Qwarm), qmelt: tk(Qmelt)}));
    const JMAX = SCALES.find((v) => v * 1000 >= Math.max(Qv, Qwarm + Qmelt)) || SCALES[SCALES.length - 1];   // chart axis max (kJ)
    window.simState = { mW, TW0, mI, TI0, Qv, Qwarm, Qmelt, Tf, iceLeftG: iceLeft * 1000, meltedG, tapaus, running, TW, TI, iceNowG: iceNow * 1000,
                        waterNowG: waterNow * 1000, q, Qend, JMAX, t: tAnim, labels: [] };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    labels = [];
    p.background(250);

    // insulated vessel: grey walls, water coloured by its temperature, one constant level (floating ice displaces its own weight)
    const inX = VES.x + VES.wall, inW = VES.w - 2 * VES.wall, inB = VES.bottom - VES.wall;
    const wH = 70 + 90 * (M - 0.15) / 0.85, wTop = inB - wH, bx = VES.x + VES.w / 2;
    p.noStroke(); p.fill(200); p.rect(VES.x, VES.top, VES.w, VES.bottom - VES.top, 6);
    p.fill(250); p.rect(inX, VES.top, inW, inB - VES.top);
    if (waterNow > 0.0005) p.fill(tempColor(TW, 175)); else p.fill(190, 225, 250, 235);   // all frozen: the block is ice
    p.rect(inX, wTop, inW, wH);
    p.stroke(30, 80, 160); p.strokeWeight(2); p.line(inX, wTop, inX + inW, wTop);
    // ice cubes: four, total area ∝ ice mass; on a plate above the vessel before Sekoita, floating after it
    const side = Math.min(40, 36 * Math.sqrt(Math.max(iceNow, 0) / 0.5)), offs = [-66, -22, 22, 66];
    if (!immersed) {
      const plateY = VES.top - 22;
      p.noStroke(); p.fill(215); p.rect(bx - 96, plateY, 192, 7, 3);
      for (const dx of offs) cube(bx + dx - side / 2, plateY - side, side);
    } else {
      if (iceNow > 0.0005 && running && u < 0.97) {             // heat flows from the water up into the ice: arrows, orange
        const t = p.millis() / 1000;
        for (const dx of [-44, 0, 44]) { const ph = (t * 0.9 + (dx + 44) / 132) % 1, ya = wTop + 46 - 34 * ph; arrow(bx + dx, ya + 14, bx + dx, ya, p.color(232, 89, 12)); }
      }
      if (iceNow > 0.0005 && waterNow > 0.0005) for (const dx of offs) cube(bx + dx - side / 2, wTop - side * 0.6, side);
    }
    // labels: temperatures top left, ice mass under the vessel
    p.noStroke();
    lab(waterNow > 0.0005 ? __(`vesi`, {twd: tx(TWd, 1), deg: DEG}) : __('vesi_jaatyi'), 14, ts(18), 'l', ts(13), [30, 80, 160], 320);
    lab(iceNow > 0.0005 ? __(`jaa`, {ti: tx(TI, 1), deg: DEG}) : __('jaa_ei_jaljella'), 14, ts(18) + ts(19), 'l', ts(13), [60, 120, 150], 320);
    lab(__(`jaata`, {icenow: tx(iceNow * 1000, 0)}), bx, VES.bottom + ts(15), 'c', ts(12));

    // energy budget chart: bars to scale, gridlines, axis in kJ
    const Y = (J) => CH.y0 - (CH.y0 - CH.y1) * (J / 1000) / JMAX;
    p.stroke(225); p.strokeWeight(1);
    const tick = JMAX / 5;                                      // five gridline steps on every scale
    for (let v = tick; v <= JMAX; v += tick) p.line(CH.ax, Y(v * 1000), 590, Y(v * 1000));
    const [xv, xj] = CH.bx, Qj = Qwarm + Qmelt;
    // the part of the ice stack above the water's heat is drawn pale: that heat is not available
    const part = (x, a, b, fill, edge) => {                    // segment from a to b (J), solid up to Qv, pale above it
      const lo = Math.min(b, Math.max(a, Qv));
      p.stroke(edge); p.strokeWeight(1.5);
      if (lo > a) { p.fill(...fill, 255); p.rect(x, Y(lo), CH.bw, Y(a) - Y(lo)); }
      if (b > lo) { p.fill(...fill, 70); p.drawingContext.setLineDash([5, 4]); p.rect(x, Y(b), CH.bw, Y(lo) - Y(b)); p.drawingContext.setLineDash([]); }
    };
    p.stroke(150, 70, 10); p.strokeWeight(1.5); grad(xv, Y(Qv), CH.bw, Y(0) - Y(Qv), [255, 192, 120], [232, 89, 12]);
    part(xj, 0, Qwarm, [25, 113, 194], [20, 80, 150]);
    part(xj, Qwarm, Qj, [165, 216, 255], [79, 143, 191]);
    p.stroke(110); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(xv + CH.bw, Y(Qv), xj + CH.bw + 6, Y(Qv)); p.drawingContext.setLineDash([]);
    p.stroke(60); p.strokeWeight(2); p.line(CH.ax, CH.y0, 590, CH.y0); p.line(CH.ax, CH.y0, CH.ax, CH.y1 - 6);
    p.noStroke();
    for (let v = 0; v <= JMAX; v += tick) lab(`$${v}$`, CH.ax - 6, Y(v * 1000) + ts(4), 'r', ts(11), [60, 60, 60]);
    lab('$Q\\ (\\text{kJ})$', CH.ax - 6, CH.y1 - ts(18), 'l', ts(12), [60, 60, 60]);
    lab(`$${tk(Qv)}$`, xv + CH.bw / 2, Y(Qv) - 6, 'c', ts(11));
    lab(`$${tk(Qj)}$`, xj + CH.bw / 2, Y(Math.max(Qj, Qv)) - 8, 'c', ts(11));
    lab(__('vesi_2'), xv + CH.bw / 2, CH.y0 + ts(16), 'c', ts(12));
    lab(__('jaa_2'), xj + CH.bw / 2, CH.y0 + ts(16), 'c', ts(12));
    // one legend line: colour → what the bar says
    const ly = CH.y0 + ts(16) + ts(20);
    let lx = 250;
    for (const [txt, col] of [[__('luovuttaa'), [232, 89, 12]], [__('lammitys'), [25, 113, 194]], [__('sulatus'), [120, 185, 235]]]) {
      p.noStroke(); p.fill(...col); p.rect(lx, ly - ts(9), ts(9), ts(9), 2);
      lab(txt, lx + ts(12), ly, 'l', ts(10));
      const b = labels[labels.length - 1]; lx = b.x1 + ts(7);
    }
    window.simState.labels = labels;
  };

  function tempColor(T, a) {                                   // cold blue at 0 °C, light cyan 25 °C, amber 50 °C, red 80 °C
    const stops = [[0, [45, 110, 215]], [25, [125, 200, 238]], [50, [250, 205, 105]], [80, [220, 60, 40]]];
    const x = Math.min(80, Math.max(0, T));
    let i = 0; while (i < stops.length - 2 && x > stops[i + 1][0]) i++;
    const [t0, c0] = stops[i], [t1, c1] = stops[i + 1], f = (x - t0) / (t1 - t0);
    const c = p.lerpColor(p.color(...c0), p.color(...c1), f);
    c.setAlpha(a); return c;
  }
  function cube(x, y, s) {                                     // an ice cube: pale blue, edge, a bright corner
    if (s < 1) return;
    p.stroke(79, 143, 191); p.strokeWeight(2); p.fill(165, 216, 255, 235); p.rect(x, y, s, s, Math.min(4, s / 4));
    p.stroke(255, 255, 255, 220); p.strokeWeight(2); p.line(x + s * 0.2, y + s * 0.3, x + s * 0.2, y + s * 0.18); p.line(x + s * 0.2, y + s * 0.18, x + s * 0.32, y + s * 0.18);
  }
  function arrow(x1, y1, x2, y2, col) {
    p.stroke(col); p.strokeWeight(2.5); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 7;
    p.fill(col); p.noStroke();
    p.triangle(x2, y2, x2 - L * Math.cos(a - 0.45), y2 - L * Math.sin(a - 0.45), x2 - L * Math.cos(a + 0.45), y2 - L * Math.sin(a + 0.45));
  }
  function grad(x, y, w, h, c1, c2) {                          // vertical gradient bar with the current stroke
    if (h < 0.5) return;
    const c = p.drawingContext; c.save(); const g = c.createLinearGradient(x, y, x, y + h);
    g.addColorStop(0, `rgb(${c1.join(',')})`); g.addColorStop(1, `rgb(${c2.join(',')})`);
    c.fillStyle = g; c.strokeStyle = 'rgb(150,70,10)'; c.lineWidth = 1.5; c.beginPath(); c.rect(x, y, w, h); c.fill(); c.stroke(); c.restore();
  }
  // every canvas text: drawn once as KaTeX (no halo), its ink box pushed to the labels list (simState.labels)
  function lab(s, x, y, align, size, col, maxW) {
    p.textStyle(p.NORMAL); p.textSize(size); p.textAlign(p.LEFT, p.BASELINE);
    if (maxW && p.textWidth(s) > maxW) { size *= maxW / p.textWidth(s); p.textSize(size); }   // shrunk to fit its room when the canvas is scaled down
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.8 * size, x1: x0 + w, y1: y + 0.3 * size });
  }
  const tx = (x, d) => { const t = x.toFixed(d); return (Number(t) === 0 ? t.replace('-', '') : t).replace('.', '{,}'); };   // decimal comma inside LaTeX, no -0,0
  const tk = (J) => tx(J / 1000, J / 1000 >= 100 ? 0 : 1);                 // heat in kJ
  const DEG = '{}^\\circ\\text{C}';
});
