// fy3-7 Olomuodon muutokset: ice at −20 °C is heated with a constant power P until it is steam at 130 °C.
// Physics: the heater transfers Q = P t. The temperature is a piecewise function of Q:
//   ice warms     Q = c_jää m ΔT   (−20 → 0 °C,   c_jää = 2100 J/(kg·K))
//   ice melts     Q = s m          (0 °C plateau,  s = 334 kJ/kg)
//   water warms   Q = c_vesi m ΔT  (0 → 100 °C,    c_vesi = 4190 J/(kg·K))
//   water boils   Q = r m          (100 °C plateau, r = 2260 kJ/kg)
//   steam warms   Q = c_höyry m ΔT (100 → 130 °C,  c_höyry = 2000 J/(kg·K)), where the animation stops.
// On a plateau the energy breaks the bonds between particles, so T stays constant; the plateau lasts sm/P or rm/P.
// Pressure (made explicit 2026-10-26): every value above is the 101 kPa value (boiling at 100 °C, r at 100 °C, c of
// steam at constant pressure), so the system is the water in a vessel closed by a light, freely moving piston: the
// pressure stays at 101 kPa and the steam stays in the system, expanding under the piston (not to scale: about 1700
// times the volume of the water). In an open pot the steam would escape; in a rigid closed vessel the pressure and the
// boiling temperature would rise and there would be no plateau at exactly 100 °C. The piston is drawn on the vessel.
// Every duration is proportional to m/P, so the chart's t axis is scaled to the current end time and printed.
// Time runs 60 times faster than real time at the normal speed; the "Nopeus" select scales that pace (hidas 30×,
// nopea 120×) and nothing else: Q = P t and every value follow the simulated time t. The sliders are locked while heating (so Q = P t holds for the whole run),
// and moving one resets the run. The readout is DOM text below the controls; the canvas only draws.
// Canvas labels go through label(), which records their boxes in window.simLabels (600×400 units) for the layout sweep.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const C_ICE = 2100, S = 334000, C_W = 4190, R = 2260000, C_ST = 2000;  // SI units
  const T0 = -20, T_END = 130, SPEED = 60;                               // start and stop temperature (°C), sim s per real s
  const CH = { x0: 335, x1: 565, y0: 315, y1: 60 };                      // chart area (axes at x0 and y0)
  const BK = { x: 50, w: 160, top: 95, bottom: 300 };                    // container
  const PHASE_TEXT = { 'jää': __('jaa_lampenee'), 'sulaa': __('jaa_sulaa'), 'vesi': __('vesi_lampenee'), 'kiehuu': __('vesi_kiehuu'), 'höyry': __('hoyry_lampenee') };
  const CONTENT = { 'jää': __('jaa'), 'sulaa': __('jaa_ja_vesi'), 'vesi': __('vesi'), 'kiehuu': __('vesi_ja_hoyry'), 'höyry': __('hoyry') };
  let sM, lM, sP, lP, sSp, note, readout, t = 0, running = false, labels = [];

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
    return [Q >= q[4] ? T_END : 100 + (Q - q[3]) / (C_ST * m), 'höyry'];
  };
  // round axis maximum with at most 5 steps
  const niceMax = (v) => { for (const st of [10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000]) if (Math.ceil(v / st) <= 5) return [Math.ceil(v / st) * st, st]; return [Math.ceil(v / 5000) * 5000, 5000]; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');   // controls first: canvas and button fit one phone screen
    button(controls, __('lammita'), () => { const m = Number(sM.value()), P = Number(sP.value()); if (t >= stages(m)[4] / P) t = 0; running = true; });
    button(controls, __('nollaa'), () => { t = 0; running = false; });
    [sM, lM] = slider(controls, 0.1, 1, 0.5, 0.05);           // massa m (kg)
    [sP, lP] = slider(controls, 500, 3000, 1000, 100);        // teho P (W)
    [sM, sP].forEach((s) => s.elt.addEventListener('input', () => { t = 0; running = false; }));   // a new setting starts a new run
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(lv); sSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) sSp.option(txt, v);
    sSp.selected('1');                                                     // pace only: never resets or locks the run
    readout = p.createDiv('').parent('sim-root').class('readout');
    note = p.createP('').parent('sim-root').class('note');                  // the one legend line: the time scale
    window.simSetTime = (sec) => { t = Math.max(0, sec); running = false; };          // for tests: jump to a moment
    window.simSetQ = (Q) => { t = Math.max(0, Q) / Number(sP.value()); running = false; };
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { m: { input: sM.elt, unit: 'kg' }, P: { input: sP.elt, unit: 'W' } },
      reset: () => { sM.value(0.5); sP.value(1000); t = 0; running = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const m = Number(sM.value()), P = Number(sP.value());
    const q = stages(m), tEnd = q[4] / P;                      // time to reach 130 °C
    const pace = SPEED * Number(sSp.value());                  // simulated seconds per real second
    if (running) t += Math.min(p.deltaTime, 100) / 1000 * pace;
    note.html(__(`aika_kuluu_nopeutettuna`, {pace: pace}));
    if (t >= tEnd) { t = tEnd; running = false; }
    const held = (s) => s.elt.getAttribute('aria-disabled') === 'true';   // a guided experiment may hold a slider (sim-embed adapter)
    sM.elt.disabled = running || held(sM); sP.elt.disabled = running || held(sP);   // locked while heating
    const Q = P * t;                                           // transferred energy Q = P t
    const [T, phase] = stateAt(Q, m, q);
    const tMelt = S * m / P, tBoil = R * m / P;                // plateau lengths sm/P and rm/P
    const [tMax, step] = niceMax(tEnd);

    lM.html(__(`massa`, {m: tx(m, 2)})); lP.html(__(`teho`, {p: P}));
    readout.html(__(`vaihe_lampotila`, {phase_text: PHASE_TEXT[phase], t: tx(T, 1)}) +
                 __(`siirtynyt_energia_kulunut`, {q: tx(Q / 1000, 1), t: tx(t, 0)}) +
                 __(`sulaminen_kestaa`, {s: fj(S * m), p: P, tmelt: tx(tMelt, 0)}) +
                 __(`kiehuminen_kestaa`, {r: fj(R * m), p: P, tboil: tx(tBoil, 0)}) +
                 __(`kuvaajan_aika_akseli`, {tmax: tMax}));
    window.simState = { m, P, t, T, phase, Q, tMelt, tBoil, running, tEnd, tMax, content: CONTENT[phase], pace };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    // text box of a label (baseline at y), in canvas units
    const box = (str, x, y, align, size) => {
      p.textSize(size); const w = p.textWidth(str), x0 = align === p.LEFT ? x : align === p.RIGHT ? x - w : x - w / 2;
      return { s: str, x0, y0: y - p.textAscent(), x1: x0 + w, y1: y + p.textDescent() };
    };
    const hit = (a, b, pad) => a.x0 < b.x1 + pad && b.x0 < a.x1 + pad && a.y0 < b.y1 + pad && b.y0 < a.y1 + pad;
    labels = [];
    const label = (str, x, y, align, size, bg) => {
      const b = box(str, x, y, align, size);
      if (bg) { p.noStroke(); p.fill(250, 250, 250, 225); p.rect(b.x0 - 3, b.y0, b.x1 - b.x0 + 6, b.y1 - b.y0, 3); p.fill(...bg); }
      p.textAlign(align, p.BASELINE); p.text(str, x, y); labels.push(b);
    };
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
    if (phase === 'kiehuu') {                                  // bubbles rising through the boiling water, kept below its surface
      p.noFill(); p.stroke(255); p.strokeWeight(1.5); const hw = H * fWater;
      for (let i = 0; i < 8 && hw > 20; i++) p.circle(bx + 12 + (i * 37) % (inner - 24), bb - 6 - ((t * 2 + i * 23) % (hw - 14)), 6 + (i % 3) * 2);
    }
    const rows = Math.max(1, Math.round(H / 30)), nIce = Math.ceil(rows * 5 * fIce - 1e-9);   // ice cubes left
    p.stroke(p.red(col), p.green(col), p.blue(col)); p.strokeWeight(1.5); p.fill(215, 235, 250, 210);
    for (let i = 0; i < nIce; i++) p.rect(bx + 4 + (i % 5) * 30, bb - 30 - Math.floor(i / 5) * 30, 26, 26, 4);
    p.noFill(); p.stroke(60); p.strokeWeight(3);
    p.line(BK.x, BK.top - 10, BK.x, BK.bottom); p.line(BK.x, BK.bottom, BK.x + BK.w, BK.bottom); p.line(BK.x + BK.w, BK.bottom, BK.x + BK.w, BK.top - 10);
    p.stroke(60); p.strokeWeight(1.5); p.fill(150, 156, 166); p.rect(bx, BK.top - 9, inner, 9, 2);   // the light piston that keeps p = 101 kPa

    // heater: glows while heating, brighter for a larger power; its label starts at the heater's left end
    const glow = running ? 0.4 + 0.6 * P / 3000 : 0;
    p.noStroke(); p.fill(90 + 160 * glow, 90 - 40 * glow, 90 - 50 * glow); p.rect(BK.x - 10, BK.bottom + 6, BK.w + 20, 16, 4);
    p.fill(60); label(__(`kuumennin`, {p: P}), BK.x - 10, BK.bottom + 26 + ts(12), p.LEFT, ts(12));

    // thermometer, same −20…130 °C scale as the chart
    const thx = 258, Yt = (TT) => BK.bottom - 30 - (BK.bottom - 30 - BK.top) * (TT - T0) / (T_END - T0);
    p.fill(235); p.stroke(120); p.strokeWeight(1.5); p.rect(thx - 6, BK.top - 5, 12, BK.bottom - BK.top - 10, 6); p.circle(thx, BK.bottom - 18, 24);
    p.noStroke(); p.fill(col); p.rect(thx - 3, Yt(T), 6, BK.bottom - 18 - Yt(T)); p.circle(thx, BK.bottom - 18, 18);

    // container label over the container; the thermometer reading beside it, or one line higher when they would touch
    // each other or the chart's tick labels (on a phone the text is about twice as large)
    p.fill(40); const cy = BK.top - 18, cLabel = `$\\text{${CONTENT[phase]}}$`, cBox = box(cLabel, BK.x + BK.w / 2, cy, p.CENTER, ts(14));
    label(cLabel, BK.x + BK.w / 2, cy, p.CENTER, ts(14));
    const reading = `$${tx(T, 0)}\\,{}^\\circ\\text{C}$`, tickLeft = CH.x0 - 10 - box('$120$', 0, 0, p.LEFT, ts(11)).x1;
    let rBox = box(reading, thx, cy, p.CENTER, ts(13)), ry = cy;
    if (hit(rBox, cBox, 6) || rBox.x1 > tickLeft - 6) { p.textSize(ts(13)); ry = cBox.y0 - 4 - p.textDescent(); }
    label(reading, thx, ry, p.CENTER, ts(13));

    // (t, T) chart: faint whole curve, bold up to the present, plateaus labelled with their length
    const X = (tt) => CH.x0 + (CH.x1 - CH.x0) * tt / tMax, Y = (TT) => CH.y0 - (CH.y0 - CH.y1) * (TT - T0) / (T_END - T0);
    const pts = [[0, T0], [q[0] / P, 0], [q[1] / P, 0], [q[2] / P, 100], [q[3] / P, 100], [tEnd, T_END]];
    p.stroke(225); p.strokeWeight(1);
    for (let v = 0; v <= 120; v += 20) p.line(CH.x0, Y(v), CH.x1, Y(v));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    for (let v = step; v <= tMax; v += step) p.line(X(v), CH.y0, X(v), CH.y0 + 4);                // a tick mark at every step
    p.noStroke(); p.fill(60);
    for (let v = -20; v <= 120; v += 20) label(`$${tx(v, 0)}$`, CH.x0 - 10, Y(v) + ts(4), p.RIGHT, ts(11));
    const every = k > 1.5 ? 2 : 1;                                                                // every second label on a phone
    for (let i = 0; i * step <= tMax; i += every) label(`$${i * step}$`, X(i * step), CH.y0 + ts(17), p.CENTER, ts(11));
    label('$t\\ (\\text{s})$', CH.x1 + 10, CH.y0 + ts(36), p.RIGHT, ts(12));                                  // below the tick labels
    label('$T\\ (^\\circ\\text{C})$', CH.x0 + 6, CH.y1 - 14, p.LEFT, ts(12));                                       // above the T axis
    p.noFill(); p.stroke(205); p.strokeWeight(2); p.beginShape(); pts.forEach(([a, b]) => p.vertex(X(a), Y(b))); p.endShape();
    p.stroke(200, 60, 40); p.strokeWeight(3); p.beginShape();
    pts.filter(([a]) => a < t).forEach(([a, b]) => p.vertex(X(a), Y(b))); p.vertex(X(t), Y(T)); p.endShape();
    // melting label below the 0 °C plateau (only the ice segment, to its left, is there); boiling label above the 100 °C
    // plateau, kept left of the steam segment; both on a light background so the curve never runs through the text
    const green = [26, 77, 46];
    p.textSize(ts(12)); const capH = 0.7 * ts(12);
    label(__(`sulaa`, {tmelt: tx(tMelt, 0)}), X(pts[1][0]) + 4, (Y(0) + CH.y0) / 2 + capH / 2, p.LEFT, ts(12), green);
    const kText = __(`kiehuu`, {tboil: tx(tBoil, 0)}), kw = box(kText, 0, 0, p.LEFT, ts(12)).x1;
    const kx = Math.max(CH.x0 + 6 + kw / 2, Math.min((X(pts[3][0]) + X(pts[4][0])) / 2, X(pts[4][0]) - 4 - kw / 2));
    label(kText, kx, Y(100) - 8, p.CENTER, ts(12), green);
    p.noStroke(); p.fill(200, 60, 40); p.circle(X(t), Y(T), 11);
    window.simLabels = labels;
  };

  // −20 °C blue, 130 °C red
  function tempColor(T) { return p.lerpColor(p.color(40, 100, 210), p.color(215, 50, 40), (T - T0) / (T_END - T0)); }
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');                                   // decimal comma inside LaTeX
  const fj = (x) => String(Math.round(x)).replace(/\B(?=(\d{3})+(?!\d))/g, '\\,');      // joules with a thin space between thousands (LaTeX)
});
