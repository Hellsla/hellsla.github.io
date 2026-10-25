// fy3-7 Olomuodon muutokset: ice at −20 °C is heated with a constant power P until it is steam at 130 °C.
// Physics: the heater transfers Q = P t. The temperature is a piecewise function of Q:
//   ice warms     Q = c_jää m ΔT   (−20 → 0 °C,   c_jää = 2100 J/(kg·K))
//   ice melts     Q = s m          (0 °C plateau,  s = 334 kJ/kg)
//   water warms   Q = c_vesi m ΔT  (0 → 100 °C,    c_vesi = 4190 J/(kg·K))
//   water boils   Q = r m          (100 °C plateau, r = 2260 kJ/kg)
//   steam warms   Q = c_höyry m ΔT (100 → 130 °C,  c_höyry = 2000 J/(kg·K)), where the animation stops.
// On a plateau the energy breaks the bonds between particles, so T stays constant; the plateau lasts sm/P or rm/P.
// Every duration is proportional to m/P, so the chart's t axis is scaled to the current end time and printed.
// Time runs 60 times faster than real time. The readout is DOM text; the canvas only draws.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const C_ICE = 2100, S = 334000, C_W = 4190, R = 2260000, C_ST = 2000;  // SI units
  const T0 = -20, T_END = 130, SPEED = 60;                               // start and stop temperature (°C), sim s per real s
  const CH = { x0: 335, x1: 580, y0: 340, y1: 60 };                      // chart area (axes at x0 and y0)
  const BK = { x: 50, w: 160, top: 95, bottom: 300 };                    // container
  const PHASE_TEXT = { 'jää': 'jää lämpenee', 'sulaa': 'jää sulaa (0 °C)', 'vesi': 'vesi lämpenee', 'kiehuu': 'vesi kiehuu (100 °C)', 'höyry': 'höyry lämpenee' };
  const CONTENT = { 'jää': 'jää', 'sulaa': 'jää ja vesi', 'vesi': 'vesi', 'kiehuu': 'vesi ja höyry', 'höyry': 'höyry' };
  let sM, lM, sP, lP, readout, t = 0, running = false;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  const button = (parent, text, fn) => { const b = p.createButton(text).parent(parent); b.elt.addEventListener('click', fn); return b; };
  // energy needed to reach the end of each stage, in J
  const stages = (m) => {
    const q1 = C_ICE * m * (0 - T0), q2 = q1 + S * m, q3 = q2 + C_W * m * 100, q4 = q3 + R * m, q5 = q4 + C_ST * m * (T_END - 100);
    return [q1, q2, q3, q4, q5];
  };
  // temperature and phase after the energy Q has been transferred
  const stateAt = (Q, m, q) => {
    if (Q < q[0]) return [T0 + Q / (C_ICE * m), 'jää'];
    if (Q < q[1]) return [0, 'sulaa'];
    if (Q < q[2]) return [(Q - q[1]) / (C_W * m), 'vesi'];
    if (Q < q[3]) return [100, 'kiehuu'];
    return [Math.min(T_END, 100 + (Q - q[3]) / (C_ST * m)), 'höyry'];
  };
  // round axis maximum with at most 5 steps
  const niceMax = (v) => { for (const st of [10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000]) if (Math.ceil(v / st) <= 5) return [Math.ceil(v / st) * st, st]; return [Math.ceil(v / 5000) * 5000, 5000]; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sM, lM] = slider(controls, 0.1, 1, 0.5, 0.05);           // massa m (kg)
    [sP, lP] = slider(controls, 500, 3000, 1000, 100);        // teho P (W)
    button(controls, 'Lämmitä', () => { const m = Number(sM.value()), P = Number(sP.value()); if (t >= stages(m)[4] / P) t = 0; running = true; });
    button(controls, 'Nollaa', () => { t = 0; running = false; });
    p.createP(`Aika kuluu nopeutettuna: 1 s animaatiota vastaa ${SPEED} s eli 1 min. Kaikki kuumentimen energia siirtyy aineeseen.`)
      .parent('sim-root').class('note');
    window.simSetTime = (sec) => { t = Math.max(0, sec); running = false; };          // for tests: jump to a moment
    window.simSetQ = (Q) => { t = Math.max(0, Q) / Number(sP.value()); running = false; };
    p.textFont('Arial');
  };

  p.draw = () => {
    const m = Number(sM.value()), P = Number(sP.value());
    const q = stages(m), tEnd = q[4] / P;                      // time to reach 130 °C
    if (running) t += Math.min(p.deltaTime, 100) / 1000 * SPEED;
    if (t >= tEnd) { t = tEnd; running = false; }
    const Q = P * t;                                           // transferred energy Q = P t
    const [T, phase] = stateAt(Q, m, q);
    const tMelt = S * m / P, tBoil = R * m / P;                // plateau lengths sm/P and rm/P
    const [tMax, step] = niceMax(tEnd);

    lM.html(`Massa m = ${fi(m, 2)} kg`); lP.html(`Teho P = ${P} W`);
    readout.html(`Vaihe: <strong>${PHASE_TEXT[phase]}</strong>, lämpötila T = <strong>${fi(T, 1)} °C</strong>` +
                 `<br>Siirtynyt energia Q = Pt = <strong>${fi(Q / 1000, 1)} kJ</strong>, kulunut aika t = ${fi(t, 0)} s` +
                 `<br>Sulaminen kestää sm/P = ${fj(S * m)} J / ${P} W = <strong>${fi(tMelt, 0)} s</strong>` +
                 `<br>Kiehuminen kestää rm/P = ${fj(R * m)} J / ${P} W = <strong>${fi(tBoil, 0)} s</strong>` +
                 `<br>Kuvaajan aika-akseli 0–${tMax} s, lämpötila-akseli −20…130 °C.`);
    window.simState = { m, P, t, T, phase, Q, tMelt, tBoil, running, tEnd, tMax };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);
    const col = tempColor(T);

    // container: content shows the phase, colour shows the temperature
    const H = 30 + 170 * m, inner = BK.w - 8, bx = BK.x + 4, bb = BK.bottom - 4;
    const fIce = phase === 'jää' ? 1 : phase === 'sulaa' ? 1 - (Q - q[0]) / (S * m) : 0;              // ice fraction left
    const fWater = phase === 'kiehuu' ? 1 - (Q - q[2]) / (R * m) : phase === 'höyry' ? 0 : 1 - fIce;  // liquid fraction
    if (phase === 'kiehuu' || phase === 'höyry') {             // steam above the liquid
      p.noStroke(); p.fill(200, 200, 210, phase === 'höyry' ? 150 : 70); p.rect(bx, BK.top, inner, bb - BK.top - H * fWater);
      p.noFill(); p.stroke(255); p.strokeWeight(2);
      for (let i = 0; i < 4; i++) { const x = bx + 25 + i * 37, y0 = BK.top + 20 + ((t * 0.8 + i * 30) % 60); if (y0 + 40 < bb - H * fWater) p.bezier(x, y0 + 40, x - 10, y0 + 25, x + 10, y0 + 15, x, y0); }
    }
    if (fWater > 0) { p.noStroke(); p.fill(p.red(col), p.green(col), p.blue(col), 150); p.rect(bx, bb - H * fWater, inner, H * fWater); }
    if (phase === 'kiehuu') {                                  // bubbles rising through the boiling water
      p.noFill(); p.stroke(255); p.strokeWeight(1.5); const hw = H * fWater;
      for (let i = 0; i < 8 && hw > 10; i++) p.circle(bx + 12 + (i * 37) % (inner - 24), bb - ((t * 2 + i * 23) % hw), 6 + (i % 3) * 2);
    }
    const rows = Math.max(1, Math.round(H / 30)), nIce = Math.ceil(rows * 5 * fIce - 1e-9);   // ice cubes left
    p.stroke(p.red(col), p.green(col), p.blue(col)); p.strokeWeight(1.5); p.fill(215, 235, 250);
    for (let i = 0; i < nIce; i++) p.rect(bx + 4 + (i % 5) * 30, bb - 30 - Math.floor(i / 5) * 30, 26, 26, 4);
    p.noFill(); p.stroke(60); p.strokeWeight(3);
    p.line(BK.x, BK.top - 10, BK.x, BK.bottom); p.line(BK.x, BK.bottom, BK.x + BK.w, BK.bottom); p.line(BK.x + BK.w, BK.bottom, BK.x + BK.w, BK.top - 10);
    p.noStroke(); p.fill(40); p.textAlign(p.CENTER); p.textSize(ts(15)); p.text(CONTENT[phase], BK.x + BK.w / 2, BK.top - 20);

    // heater: glows while heating, brighter for a larger power
    const glow = running ? 0.4 + 0.6 * P / 3000 : 0;
    p.fill(90 + 160 * glow, 90 - 40 * glow, 90 - 50 * glow); p.rect(BK.x - 10, BK.bottom + 6, BK.w + 20, 16, 4);
    p.fill(60); p.textSize(ts(13)); p.text(`kuumennin ${P} W`, BK.x + BK.w / 2, BK.bottom + 26 + ts(14));

    // thermometer, same −20…130 °C scale as the chart
    const thx = 258, Yt = (TT) => BK.bottom - 30 - (BK.bottom - 30 - BK.top) * (TT - T0) / (T_END - T0);
    p.fill(235); p.stroke(120); p.strokeWeight(1.5); p.rect(thx - 6, BK.top - 5, 12, BK.bottom - BK.top - 10, 6); p.circle(thx, BK.bottom - 18, 24);
    p.noStroke(); p.fill(col); p.rect(thx - 3, Yt(T), 6, BK.bottom - 18 - Yt(T)); p.circle(thx, BK.bottom - 18, 18);
    p.fill(40); p.textSize(ts(13)); p.text(`${fi(T, 0)} °C`, thx, BK.top - 20);

    // (t, T) chart: faint whole curve, bold up to the present, plateaus labelled with their length
    const X = (tt) => CH.x0 + (CH.x1 - CH.x0) * tt / tMax, Y = (TT) => CH.y0 - (CH.y0 - CH.y1) * (TT - T0) / (T_END - T0);
    const pts = [[0, T0], [q[0] / P, 0], [q[1] / P, 0], [q[2] / P, 100], [q[3] / P, 100], [tEnd, T_END]];
    p.stroke(225); p.strokeWeight(1);
    for (let v = 0; v <= 120; v += 20) p.line(CH.x0, Y(v), CH.x1, Y(v));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    p.noStroke(); p.fill(60); p.textSize(ts(11)); p.textAlign(p.RIGHT);
    for (let v = -20; v <= 120; v += 20) p.text(fi(v, 0), CH.x0 - 6, Y(v) + ts(4));
    p.textAlign(p.CENTER);
    for (let v = 0; v <= tMax; v += step) p.text(`${v}`, X(v), CH.y0 + ts(16));
    p.textAlign(p.RIGHT); p.textSize(ts(12)); p.text('t (s)', CH.x1, CH.y0 - 8);
    p.textAlign(p.LEFT); p.text('T (°C)', CH.x0 - 26, CH.y1 - ts(14));
    p.noFill(); p.stroke(205); p.strokeWeight(2); p.beginShape(); pts.forEach(([a, b]) => p.vertex(X(a), Y(b))); p.endShape();
    p.stroke(200, 60, 40); p.strokeWeight(3); p.beginShape();
    pts.filter(([a]) => a < t).forEach(([a, b]) => p.vertex(X(a), Y(b))); p.vertex(X(t), Y(T)); p.endShape();
    p.noStroke(); p.fill(26, 77, 46); p.textSize(ts(12));
    p.textAlign(p.LEFT); p.text(`sulaa ${fi(tMelt, 0)} s`, X(pts[1][0]) + 4, Y(0) + ts(16));
    p.textAlign(p.CENTER); p.text(`kiehuu ${fi(tBoil, 0)} s`, (X(pts[3][0]) + X(pts[4][0])) / 2, Y(100) - 8);
    p.fill(200, 60, 40); p.circle(X(t), Y(T), 11);
  };

  // −20 °C blue, 130 °C red
  function tempColor(T) { return p.lerpColor(p.color(40, 100, 210), p.color(215, 50, 40), (T - T0) / (T_END - T0)); }
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                   // Finnish decimal comma and minus sign
  const fj = (x) => String(Math.round(x)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');      // joules with a space between thousands
});
