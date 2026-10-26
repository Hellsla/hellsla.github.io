// fy3-8 Lämpölaajeneminen: a micro-model lattice and a rod of the chosen material, heated or cooled from 20 °C.
// Physics: the length L₀ is measured at the reference temperature 20 °C. At temperature T the change is
//   ΔT = T − 20 °C (in kelvins),  ΔL = α L₀ ΔT,  L = L₀ + ΔL,
// so the relative change ΔL/L₀ = αΔT is the same for every bond in the solid as for the whole rod.
// Micro model: particles vibrate about their equilibrium positions with an amplitude ∝ √T (T in kelvins, the
// thermal energy of a vibration is proportional to T). The mean spacing grows by the same factor 1 + αΔT as the rod.
// Real changes are under 0,3 %, so both the spacing change and the rod change are drawn E = 100 times larger;
// the particles themselves keep their size. The vibration phase is fixed by the particle index and time (no randomness).
// Speed control: the vibration clock advances by (real frame time)·speed ("Nopeus"), a pace for the picture only;
// ΔL, L and every value depend on T, L₀ and the material, never on time.
// The chart's ΔL axis is scaled to the steepest line (aluminium) at the current L₀ and printed. The readout is DOM text.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const T_REF = 20, E = 100, T_MIN = -40, T_MAX = 120;          // reference temperature (°C), exaggeration, slider range
  const MATERIALS = [                                            // name, α (1/K), line colour
    ['teräs', 12e-6, [60, 90, 150]], ['alumiini', 23e-6, [150, 100, 200]], ['kupari', 17e-6, [200, 110, 40]],
    ['tavallinen lasi', 9e-6, [30, 150, 140]], ['borosilikaattilasi', 3.3e-6, [110, 160, 50]]];
  const A_MAX = 23e-6;                                           // largest α, sets the chart scale
  const CH = { x0: 335, x1: 575, y0: 330, y1: 160 };             // chart area (axes at x0 and y0)
  const ROD = { x: 280, y: 90, h: 22, w: 220 };                  // rod at 20 °C: 220 px
  const LAT = { cx: 125, cy: 210, n: 5, d0: 36, r: 7, a0: 6.5 }; // lattice: spacing at 20 °C, particle radius, amplitude at 20 °C (px)
  let sL, lL, sT, lT, sel, sSp, btn, readout, tAnim = 0, running = true;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  // chart range for ΔL in mm: steps of 1, 2, 2,5 or 5 · 10ⁿ, at most 6 steps from the coldest to the hottest aluminium value
  const chartRange = (L0) => {
    const hi = A_MAX * L0 * (T_MAX - T_REF) * 1000, lo = A_MAX * L0 * (T_REF - T_MIN) * 1000;
    for (let e = -2; e <= 3; e++) for (const m of [1, 2, 2.5, 5]) {
      const st = m * 10 ** e, nUp = Math.ceil(hi / st - 1e-9), nDown = Math.ceil(lo / st - 1e-9);
      if (nUp + nDown <= 6) return [-nDown * st, nUp * st, st, nDown, nUp];
    }
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const ls = p.createElement('label').parent(controls);
    p.createSpan('Aine').parent(ls);
    sel = p.createSelect().parent(ls);
    for (const [name, a] of MATERIALS) sel.option(`${name} (α = ${fa(a)} · 10⁻⁶ 1/K)`, name);
    sel.selected('teräs');
    [sL, lL] = slider(controls, 1, 100, 10, 1);                 // alkupituus L₀ (m)
    [sT, lT] = slider(controls, T_MIN, T_MAX, T_REF, 1);         // lämpötila T (°C)
    btn = p.createButton('Pysäytä värähtely').parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; btn.html(running ? 'Pysäytä värähtely' : 'Jatka värähtelyä'); });
    const lv = p.createElement('label').parent(controls); p.createSpan('Nopeus').parent(lv); sSp = p.createSelect().parent(lv);
    for (const [txt, v] of [['hidas', 0.5], ['normaali', 1], ['nopea', 2]]) sSp.option(txt, v);
    sSp.selected('1');                                           // pace of the vibration only
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { material: { input: sel.elt, unit: '' }, L0: { input: sL.elt, unit: 'm' }, T: { input: sT.elt, unit: '°C' } },
      reset: () => { sel.selected('teräs'); sL.value(10); sT.value(T_REF); tAnim = 0; running = true; btn.html('Pysäytä värähtely'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const material = sel.value(), alpha = MATERIALS.find((m) => m[0] === material)[1];
    const L0 = Number(sL.value()), T = Number(sT.value());
    const dT = T - T_REF;                                        // temperature change from 20 °C, K
    const dL = alpha * L0 * dT;                                  // ΔL = αL₀ΔT, m
    const L = L0 + dL;                                           // new length, m
    const rel = alpha * dT;                                      // relative change ΔL/L₀
    const spacing = 1 + E * rel;                                 // drawn spacing and rod length relative to 20 °C
    const amp = LAT.a0 * Math.sqrt((T + 273.15) / (T_REF + 273.15));   // vibration amplitude ∝ √T (px)
    const [yMin, yMax, yStep, nDown, nUp] = chartRange(L0);
    const dec = (String(+yStep.toFixed(4)).split('.')[1] || '').length;   // decimals of the ΔL scale
    if (running) tAnim += Math.min(p.deltaTime, 100) / 1000 * Number(sSp.value());
    const decL = dL === 0 ? 4 : Math.min(8, Math.max(4, Math.ceil(-Math.log10(Math.abs(dL))) + 1));   // show the change in L

    lL.html(`Alkupituus L₀ = ${nw(`${L0} m`)}`); lT.html(`Lämpötila T = ${nw(`${fi(T, 0)} °C`)}`);
    readout.html(`Aine: <strong>${material}</strong>, α = ${nw(`${fa(alpha)} · 10⁻⁶ 1/K`)}, alkupituus L₀ = ${nw(`${L0} m`)} (${nw('20 °C:ssa')})` +
                 `<br>Lämpötilan muutos ΔT = T − ${nw('20 °C')} = ${nw(`${fi(T, 0)} °C`)} − ${nw('20 °C')} = <strong>${nw(`${fi(dT, 0)} K`)}</strong>` +
                 `<br>Pituuden muutos ΔL = αL₀ΔT = <strong>${nw(`${sgn(dL * 1000)} mm`)}</strong>` +
                 `<br>Uusi pituus L = L₀ + ΔL = <strong>${nw(`${fi(L, decL)} m`)}</strong>` +
                 `<br>Suhteellinen muutos ΔL/L₀ = αΔT = ${nw(`${sgn(rel * 100)} %`)}` +
                 `<br>Kuvaajan ΔL-akseli ${nw(`${fi(yMin, dec)}…${fi(yMax, dec)} mm`)}, kun L₀ = ${nw(`${L0} m`)}.`);
    window.simState = { material, alpha, L0, T, dT, dL, L, rel, E, spacing, amp, chartMin: yMin, chartMax: yMax, running, t: tAnim };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);
    const col = tempColor(T);
    p.noStroke(); p.fill(40); p.textAlign(p.CENTER); p.textSize(ts(13));
    p.text(`Pituuden muutokset liioiteltu ×${E}`, 300, 8 + ts(13));

    // micro model: 5 × 5 particles, mean spacing d₀(1 + EαΔT), each vibrating with amplitude ∝ √T
    const d = LAT.d0 * spacing, half = (LAT.n - 1) / 2, ref = 2 * half * LAT.d0;
    p.textSize(ts(14)); p.text('mikromalli', LAT.cx, 40 + ts(14));
    p.noFill(); p.stroke(150); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]);
    p.rect(LAT.cx - ref / 2, LAT.cy - ref / 2, ref, ref); p.drawingContext.setLineDash([]);
    p.stroke(255); p.strokeWeight(1.5); p.fill(col);
    for (let r = 0; r < LAT.n; r++) for (let c = 0; c < LAT.n; c++) {
      const i = r * LAT.n + c;                                   // phases from the index: golden-angle spread, no randomness
      const x = LAT.cx + (c - half) * d + amp * Math.sin(2 * Math.PI * 1.3 * tAnim + i * 2.39996);
      const y = LAT.cy + (r - half) * d + amp * Math.sin(2 * Math.PI * 1.1 * tAnim + i * 1.7 + 0.5);
      p.circle(x, y, 2 * LAT.r);
    }
    p.noStroke(); p.fill(60); p.textSize(ts(12));
    p.text('katkoviiva: 20 °C', LAT.cx, 330 + ts(6));
    p.text(`välit ${sgn(rel * 100)} %`, LAT.cx, 340 + ts(12) + ts(12));

    // rod with its left end fixed; dashed outline = length at 20 °C, solid = length now (change ×E)
    const wNow = ROD.w * spacing, xRef = ROD.x + ROD.w, xNow = ROD.x + wNow;
    p.fill(40); p.textAlign(p.LEFT); p.textSize(ts(14)); p.text(`sauva, L₀ = ${L0} m`, ROD.x - 10, 40 + ts(14));
    p.fill(110); p.rect(ROD.x - 10, ROD.y - 10, 10, ROD.h + 20);
    p.fill(col); p.stroke(60); p.strokeWeight(1.5); p.rect(ROD.x, ROD.y, wNow, ROD.h);
    p.noFill(); p.stroke(60); p.drawingContext.setLineDash([5, 4]); p.rect(ROD.x, ROD.y, ROD.w, ROD.h); p.drawingContext.setLineDash([]);
    if (Math.abs(xNow - xRef) > 1) {                             // ΔL marker between the two ends
      const yA = ROD.y + ROD.h + 12, s = Math.sign(xNow - xRef);
      p.stroke(200, 50, 40); p.strokeWeight(2); p.line(xRef, yA, xNow, yA); p.line(xRef, yA - 5, xRef, yA + 5);
      p.fill(200, 50, 40); p.triangle(xNow, yA, xNow - 7 * s, yA - 4, xNow - 7 * s, yA + 4);
      p.noStroke(); p.textAlign(p.CENTER); p.textSize(ts(13));
      p.text('ΔL', Math.min((xRef + xNow) / 2, 590 - p.textWidth('ΔL') / 2), yA + 4 + ts(13));
    }

    // (T, ΔL) chart: thin lines for every material, thick for the chosen one, the current point
    const X = (TT) => CH.x0 + (CH.x1 - CH.x0) * (TT - T_MIN) / (T_MAX - T_MIN);
    const Y = (v) => CH.y0 - (CH.y0 - CH.y1) * (v - yMin) / (yMax - yMin);
    p.stroke(225); p.strokeWeight(1);
    for (let TT = T_MIN; TT <= T_MAX; TT += 20) p.line(X(TT), CH.y0, X(TT), CH.y1);
    for (let j = -nDown; j <= nUp; j++) p.line(CH.x0, Y(j * yStep), CH.x1, Y(j * yStep));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    p.stroke(120); p.strokeWeight(1.5); p.line(CH.x0, Y(0), CH.x1, Y(0));
    p.noStroke(); p.fill(60); p.textSize(ts(11)); p.textAlign(p.RIGHT);
    for (let j = -nDown; j <= nUp; j++) p.text(fi(j * yStep, dec), CH.x0 - 6, Y(j * yStep) + ts(4));
    p.textAlign(p.CENTER);
    for (let TT = T_MIN; TT <= T_MAX; TT += 40) p.text(fi(TT, 0), X(TT), CH.y0 + ts(16));
    p.textAlign(p.RIGHT); p.textSize(ts(12)); p.text('T (°C)', CH.x1 + 10, CH.y0 + ts(32));
    p.textAlign(p.LEFT); p.text('ΔL (mm)', CH.x0 + 8, CH.y1 + ts(8));
    for (const [name, a, c] of MATERIALS) {
      if (name === material) continue;
      p.stroke(...c, 150); p.strokeWeight(1.5); p.line(X(T_MIN), Y(a * L0 * (T_MIN - T_REF) * 1000), X(T_MAX), Y(a * L0 * (T_MAX - T_REF) * 1000));
    }
    const cs = MATERIALS.find((m) => m[0] === material)[2];
    p.stroke(...cs); p.strokeWeight(4); p.line(X(T_MIN), Y(alpha * L0 * (T_MIN - T_REF) * 1000), X(T_MAX), Y(alpha * L0 * (T_MAX - T_REF) * 1000));
    p.stroke(255); p.strokeWeight(2); p.fill(200, 50, 40); p.circle(X(T), Y(dL * 1000), 12);
  };

  // −40 °C blue, 120 °C red
  function tempColor(T) { return p.lerpColor(p.color(40, 100, 210), p.color(215, 50, 40), (T - T_MIN) / (T_MAX - T_MIN)); }
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                   // Finnish decimal comma and minus sign
  const nw = (t) => `<span style="white-space:nowrap">${t}</span>`;                     // keep a value and its unit on one line
  const fa = (a) => String(+(a * 1e6).toFixed(1)).replace('.', ',');                       // α in units of 10⁻⁶ 1/K
  // three significant figures with an explicit sign
  const sgn = (x) => {
    if (x === 0) return '0';
    const s = fi(Math.abs(x), Math.max(0, 2 - Math.floor(Math.log10(Math.abs(x)))));
    return (x > 0 ? '+' : '−') + s;
  };
});
