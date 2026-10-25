// fy3-6 Aineen lämpeneminen ja jäähtyminen: a hot or cold body is dropped into water in an insulated calorimeter.
// Physics: the heat the body gives off equals the heat the water takes in (energy is conserved, no losses):
//   c_B m_B (T_B0 − T) = c_W m_W (T − T_W0)  ⇒  T = (c_W m_W T_W0 + c_B m_B T_B0) / (c_W m_W + c_B m_B),
// with c_W = 4190 J/(kg·K). C = cm is the heat capacity of the whole body (J/K); Q = c_B m_B (T_B0 − T) is the heat
// the body gives off (negative when it takes heat in). The approach to T in the animation is ILLUSTRATION ONLY:
// both temperatures relax exponentially, T(t) = T + (T0 − T)·e^(−t/τ) with τ = 1,5 s, so they meet at T after a few
// seconds; the real rate depends on stirring, shape and contact. No phase changes: the body stays 0–100 °C.
// The (t, T) chart's T axis is scaled to the two starting temperatures (rounded to tens) and printed on the axis.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. The readout is DOM text. Exposes window.simState every frame.
new p5((p) => {
  const CW = 4190, TAU = 1.5, T_END = 10;                     // water c (J/(kg·K)), time constant (s), animation length (s)
  const MATERIALS = [['vesi', 4190], ['alumiini', 900], ['hiekka', 800], ['rauta', 450], ['kupari', 385]];
  const VES = { x: 30, w: 210, top: 140, bottom: 370, wall: 14 };   // insulated vessel (outer box)
  const CH = { x0: 320, x1: 510, y0: 345, y1: 70 };           // chart area; right margin holds the T label
  let sMW, lMW, sTW, lTW, sel, lSel, sMB, lMB, sTB, lTB, readout;
  let tAnim = 0, running = false, key = '';                   // animation clock (s), state, inputs at last reset
  const inputKey = () => [sMW, sTW, sel, sMB, sTB].map((e) => e.value()).join();

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label).style('white-space', 'nowrap');   // value never wraps alone onto a second line
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    // controls right under the canvas with Upota first, so canvas + button fit on one phone screen; the long readout follows
    const controls = p.createDiv('').parent('sim-root').class('controls');
    p.createButton('Upota').parent(controls).mousePressed(() => { tAnim = 0; running = true; key = inputKey(); });
    [sMW, lMW] = slider(controls, 0.10, 1.00, 0.30, 0.01);    // veden massa (kg)
    [sTW, lTW] = slider(controls, 5, 60, 20, 0.5);            // veden alkulämpötila (°C)
    const ls = p.createElement('label').parent(controls);
    lSel = p.createSpan('').parent(ls).style('white-space', 'nowrap');
    sel = p.createSelect().parent(ls);
    for (const [name, c] of MATERIALS) sel.option(`${name} (${c} J/(kg·K))`, String(c));
    sel.selected('385');
    [sMB, lMB] = slider(controls, 0.05, 1.00, 0.20, 0.01);    // kappaleen massa (kg)
    [sTB, lTB] = slider(controls, 0, 100, 100, 0.5);          // kappaleen alkulämpötila (°C)
    readout = p.createDiv('').parent('sim-root').class('readout');
    p.createP('Eristetyssä astiassa lämpöä siirtyy kuumemmasta kylmempään, kunnes lämpötilat ovat samat. ' +
              'Lähestymisen nopeus (aikavakio noin 1,5 s) on vain havainnollistus, ei fysikaalinen malli: todellisuudessa se riippuu ' +
              'sekoittamisesta ja kappaleen muodosta. Astian oma lämpökapasiteetti ja lämpöhäviöt jätetään huomiotta.')
      .parent('sim-root').class('note');
    p.textFont('Arial');
  };

  p.draw = () => {
    const mW = Number(sMW.value()), TW0 = Number(sTW.value()), cB = Number(sel.value()), mB = Number(sMB.value()), TB0 = Number(sTB.value());
    const name = MATERIALS.find(([, c]) => c === cB)[0];
    const CWt = CW * mW, CB = cB * mB;                         // heat capacities C = cm (J/K)
    const Teq = (CWt * TW0 + CB * TB0) / (CWt + CB);           // equilibrium: heat given off = heat taken in
    const Q = CB * (TB0 - Teq);                                // heat given off by the body (J); equals CW·mW·(Teq − TW0)
    const QW = CWt * (Teq - TW0);                              // heat taken in by the water (J)
    if (inputKey() !== key) { key = inputKey(); tAnim = 0; running = false; }  // any change of the inputs takes the body out again
    if (running) { tAnim += Math.min(p.deltaTime, 100) / 1000;   // clamped: a resume after an off-screen pause cannot skip the motion
                  if (tAnim >= T_END) { tAnim = T_END; running = false; } }
    const immersed = running || tAnim > 0;
    const decay = tAnim >= T_END ? 0 : Math.exp(-tAnim / TAU); // illustrative exponential approach to Teq
    const TW = Teq + (TW0 - Teq) * decay, TB = Teq + (TB0 - Teq) * decay;
    let lo = Math.floor(Math.min(TW0, TB0) / 10) * 10, hi = Math.ceil(Math.max(TW0, TB0) / 10) * 10;
    if (hi - lo < 10) hi = lo + 10;
    const step = hi - lo > 60 ? 20 : 10;

    lMW.html(`Veden massa m<sub>v</sub> = ${fi(mW, 2)} kg`); lTW.html(`Veden alkulämpötila T<sub>v</sub> = ${fi(TW0, 1)} °C`);
    lSel.html(`Kappaleen aine, c<sub>k</sub> = ${cB} J/(kg·K)`);
    lMB.html(`Kappaleen massa m<sub>k</sub> = ${fi(mB, 2)} kg`); lTB.html(`Kappaleen alkulämpötila T<sub>k</sub> = ${fi(TB0, 1)} °C`);
    let flow;
    if (Math.abs(TB0 - TW0) < 1e-9) flow = 'Lämpötilat ovat samat, joten lämpöä ei siirry.';
    else if (TB0 > TW0) flow = `Kappale luovuttaa Q = c<sub>k</sub>m<sub>k</sub>(T<sub>k</sub> − T) = <strong>${fq(Q)}</strong>, ja vesi vastaanottaa ` +
                               `Q = c<sub>v</sub>m<sub>v</sub>(T − T<sub>v</sub>) = <strong>${fq(QW)}</strong>.` +
                               `<br>Vesi lämpenee ${fi(Teq - TW0, 1)}&nbsp;K ja kappale jäähtyy ${fi(TB0 - Teq, 1)}&nbsp;K.`;
    else flow = `Vesi luovuttaa Q = c<sub>v</sub>m<sub>v</sub>(T<sub>v</sub> − T) = <strong>${fq(-QW)}</strong>, ja kappale vastaanottaa ` +
                `Q = c<sub>k</sub>m<sub>k</sub>(T − T<sub>k</sub>) = <strong>${fq(-Q)}</strong>.` +
                `<br>Kappale lämpenee ${fi(Teq - TB0, 1)}&nbsp;K ja vesi jäähtyy ${fi(TW0 - Teq, 1)}&nbsp;K.`;
    readout.html(`Tasapainolämpötila T = <strong>${fi(Teq, 1)}&nbsp;°C</strong>` +
                 `<br>Lämpökapasiteetit: vesi C<sub>v</sub> = c<sub>v</sub>m<sub>v</sub> = ${fc(CWt)}&nbsp;J/K, kappale (${name}) C<sub>k</sub> = c<sub>k</sub>m<sub>k</sub> = ${fc(CB)}&nbsp;J/K` +
                 `<br>${flow}` +
                 `<br>Lämpömittarit nyt: vesi ${fi(TW, 1)}&nbsp;°C, kappale ${fi(TB, 1)}&nbsp;°C` +
                 `<br><small>Kuvaajan asteikko ${lo}–${hi}&nbsp;°C ja 0–${T_END}&nbsp;s; lähestymisen nopeus on vain havainnollistus.</small>`);
    window.simState = { mW, TW0, cB, mB, TB0, Teq, CW: CWt, CB, Q, QW, running, TW, TB, t: tAnim, Tlo: lo, Thi: hi };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);

    // insulated vessel: grey walls, water coloured by its current temperature, level grows with the mass
    const inX = VES.x + VES.wall, inW = VES.w - 2 * VES.wall, inB = VES.bottom - VES.wall;
    const wH = 50 + 160 * (mW - 0.1) / 0.9, wTop = inB - wH;
    p.noStroke(); p.fill(200); p.rect(VES.x, VES.top, VES.w, VES.bottom - VES.top, 6);
    p.fill(250); p.rect(inX, VES.top, inW, inB - VES.top);
    p.fill(tempColor(TW, 170)); p.rect(inX, wTop, inW, wH);
    p.stroke(30, 80, 160); p.strokeWeight(2); p.line(inX, wTop, inX + inW, wTop);
    // body: size grows with its mass; hangs on a string before "Upota", rests on the bottom after it
    const side = 16 + 28 * Math.sqrt(mB), bx = VES.x + VES.w / 2, by = immersed ? inB - side : VES.top - side - 8;
    const sy = Math.max(76, ts(18) + ts(19) + ts(7));         // the string starts below the "kappale … °C" label
    if (!immersed && sy < by - 4) { p.stroke(80); p.strokeWeight(1.5); p.line(bx, sy, bx, by); }
    p.stroke(40); p.strokeWeight(2); p.fill(tempColor(TB, 255)); p.rect(bx - side / 2, by, side, side, 3);
    if (immersed && Math.abs(TB - TW) > 0.5) {                 // heat-flow arrows, length ∝ temperature difference
      const out = TB > TW, L = 6 + 22 * Math.abs(TB - TW) / 100, cy = by + side / 2, r = side / 2 + 4;
      for (const dx of [-1, 1]) {
        const a = bx + dx * r, b = bx + dx * (r + L);
        arrow(out ? a : b, cy, out ? b : a, cy, p.color(200, 40, 40));
      }
      arrow(bx, out ? by - 4 : by - 4 - L, bx, out ? by - 4 - L : by - 4, p.color(200, 40, 40));
    }
    p.noStroke(); p.textSize(ts(13)); p.textAlign(p.LEFT);
    p.fill(30, 80, 160); p.text(`vesi ${fi(TW, 1)} °C`, 20, ts(18));
    p.fill(170, 70, 20); p.text(`kappale ${fi(TB, 1)} °C`, 20, ts(18) + ts(19));

    // (t, T) chart: both temperatures so far and the equilibrium line
    const X = (t) => CH.x0 + (CH.x1 - CH.x0) * t / T_END, Y = (T) => CH.y0 - (CH.y0 - CH.y1) * (T - lo) / (hi - lo);
    p.stroke(225); p.strokeWeight(1);
    for (let v = lo + step; v <= hi; v += step) p.line(CH.x0, Y(v), CH.x1, Y(v));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    p.noStroke(); p.fill(60); p.textSize(ts(11)); p.textAlign(p.RIGHT);
    for (let v = lo; v <= hi; v += step) p.text(`${v}`, CH.x0 - 6, Y(v) + ts(4));
    p.textAlign(p.CENTER);
    for (let t = 0; t <= T_END; t += 2) p.text(`${t}`, X(t), CH.y0 + ts(16));
    p.textAlign(p.LEFT); p.text('t (s)', CH.x1 + 22, CH.y0 + ts(16));
    p.textAlign(p.LEFT); p.textSize(ts(12)); p.text('T (°C)', CH.x0 - 26, CH.y1 - ts(14));
    p.stroke(110); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(CH.x0, Y(Teq), CH.x1, Y(Teq)); p.drawingContext.setLineDash([]);
    // T label in the right margin: name above and value below the line, kept above the t axis labels; near the top of the
    // axis both go below the line so the name does not touch the legend
    const nearTop = Y(Teq) < CH.y1 + 0.15 * (CH.y0 - CH.y1);
    const vy = nearTop ? Y(Teq) + ts(30) : Math.min(Y(Teq) + ts(12), CH.y0 - 4), ny = nearTop ? Y(Teq) + ts(14) : vy - ts(16);
    p.noStroke(); p.fill(60); p.textSize(ts(12)); p.text('T', CH.x1 + 6, ny); p.text(`${fi(Teq, 1)} °C`, CH.x1 + 6, vy);
    curve(TW0, Teq, tAnim, p.color(30, 80, 160)); curve(TB0, Teq, tAnim, p.color(200, 90, 20));
    p.noStroke(); p.fill(30, 80, 160); p.circle(X(tAnim), Y(TW), 10); p.fill(200, 90, 20); p.circle(X(tAnim), Y(TB), 10);
    // legend above the chart
    p.strokeWeight(3); p.stroke(30, 80, 160); p.line(CH.x0 + 70, ts(14), CH.x0 + 94, ts(14)); p.stroke(200, 90, 20); p.line(CH.x0 + 70, ts(14) + ts(18), CH.x0 + 94, ts(14) + ts(18));
    p.noStroke(); p.fill(60); p.textSize(ts(12)); p.text('vesi', CH.x0 + 100, ts(14) + ts(4)); p.text('kappale', CH.x0 + 100, ts(14) + ts(22));

    function curve(T0, Te, tEnd, col) {                        // analytic curve T(t) from 0 to the current time
      p.stroke(col); p.strokeWeight(3); p.noFill(); p.beginShape();
      for (let i = 0; i <= 100; i++) { const t = tEnd * i / 100; p.vertex(X(t), Y(Te + (T0 - Te) * (t >= T_END ? 0 : Math.exp(-t / TAU)))); }
      p.endShape();
    }
  };

  function tempColor(T, a) {                                   // 0 °C blue, 50 °C yellow, 100 °C red
    const u = Math.min(1, Math.max(0, T / 100));
    const c = u < 0.5 ? p.lerpColor(p.color(50, 110, 230), p.color(245, 195, 70), u * 2) : p.lerpColor(p.color(245, 195, 70), p.color(215, 45, 35), u * 2 - 1);
    c.setAlpha(a); return c;
  }
  function arrow(x1, y1, x2, y2, col) {
    p.stroke(col); p.strokeWeight(2.5); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 7;
    p.fill(col); p.noStroke();
    p.triangle(x2, y2, x2 - L * Math.cos(a - 0.45), y2 - L * Math.sin(a - 0.45), x2 - L * Math.cos(a + 0.45), y2 - L * Math.sin(a + 0.45));
  }
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');   // Finnish decimal comma and minus sign
  const fc = (x) => fi(x, x >= 100 ? 0 : 1);                               // heat capacity (J/K)
  const fq = (x) => (Math.abs(x) >= 1000 ? `${fi(Number((x / 1000).toPrecision(3)), Math.max(0, 2 - Math.floor(Math.log10(Math.abs(x) / 1000))))}&nbsp;kJ` : `${fi(x, 0)}&nbsp;J`);   // three significant figures
});
