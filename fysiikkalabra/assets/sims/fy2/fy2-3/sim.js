// fy2-3 Teho: two devices, each on its own energy meter, and their energy against time on one graph.
// Model: a device converts energy at a steady power P (a typical rounded rating, the same values as the lesson's table),
// so after a time t it has converted E = P t. The meter disc turns at a rate proportional to the power, as in an
// old household meter (a fixed number of turns per kilowatt-hour): the kettle's disc spins, the lamp's barely moves.
// The graph E(t) draws both devices to one scale: each line starts at the origin and its slope is the power, solid up
// to the device's own time t and dashed beyond it. Colour carries the device: blue = A, orange = B (picture, graph and
// legend line). The speed select changes only the pace of the discs, never the physics. Every canvas text goes
// through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const DEV = { lamppu: 10, televisio: 80, jaakaappi: 100, tosteri: 1000, kuivain: 1800, keitin: 2000, kiuas: 8000 };   // W
  const ORDER = ['lamppu', 'televisio', 'jaakaappi', 'tosteri', 'kuivain', 'keitin', 'kiuas'];
  const INIT = { A: 'kuivain', tA: 5, B: 'lamppu', tB: 60 };              // t in minutes
  const COL = { A: [28, 95, 168], B: [217, 72, 15], ink: [31, 41, 51], grid: [222, 226, 230] };
  const GX0 = 92, GX1 = 512, GY0 = 210, GY1 = 346;                         // the graph's plot box (canvas units)
  let selA, selB, slA, slB, selSp, lA, lB, readout, labels = [], turn = { A: 0, B: 0 };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const dev = (name) => {
      const l = p.createElement('label').parent(controls); p.createSpan(__('laite_' + name)).parent(l);
      const s = p.createSelect().parent(l); for (const k of ORDER) s.option(__('d_' + k), k); return s;
    };
    const time = () => {
      const l = p.createElement('label').parent(controls), span = p.createSpan('').parent(l);
      return [p.createSlider(1, 1440, 1, 1).parent(l), span];
    };
    selA = dev('A'); [slA, lA] = time();
    selB = dev('B'); [slB, lB] = time();
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSp = p.createSelect().parent(ls);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    reset();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { A: { input: selA.elt, unit: '' }, tA: { input: slA.elt, unit: 'min' }, B: { input: selB.elt, unit: '' }, tB: { input: slB.elt, unit: 'min' } },
      reset, step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function reset() {
    selA.selected(INIT.A); selB.selected(INIT.B); slA.value(INIT.tA); slB.value(INIT.tB); selSp.selected('1');
    turn = { A: 0, B: 0 };
  }

  p.draw = () => {
    const kA = selA.value(), kB = selB.value(), PA = DEV[kA], PB = DEV[kB];
    const tA = Number(slA.value()), tB = Number(slB.value()), speed = Number(selSp.value());
    const EA = PA * tA * 60, EB = PB * tB * 60;                            // E = P t, t in seconds
    const dt = Math.min(p.deltaTime, 100) / 1000;
    turn.A = (turn.A + dt * speed * PA / 4000) % 1;                        // turns per second: 0,5 at 2000 W (normaali)
    turn.B = (turn.B + dt * speed * PB / 4000) % 1;
    lA.html(__('aika', { X: 'A', t: tA, h: sig(tA / 60) }));
    lB.html(__('aika', { X: 'B', t: tB, h: sig(tB / 60) }));
    readout.html(__('rivi', { X: 'A', P: PA, E: fE(EA), kwh: sig(EA / 3.6e6) }) + '<br>' + __('rivi', { X: 'B', P: PB, E: fE(EB), kwh: sig(EB / 3.6e6) }));
    window.simState = { A: kA, B: kB, PA, PB, tA, tB, EA, EB, EA_kJ: EA / 1000, EB_kJ: EB / 1000,
      EA_kWh: EA / 3.6e6, EB_kWh: EB / 3.6e6, nopeus: speed, labels: null };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(Math.max(20, 14 * k));                          // about 18 px on a wide screen, 14 px on a phone
    labels = [];
    p.background(250);
    row('A', kA, PA, EA, 10, fh);
    row('B', kB, PB, EB, 94, fh);
    graph([['A', PA, tA, EA], ['B', PB, tB, EB]], fh);
    window.simState.labels = labels;
  };

  // --- one device row: the meter with its turning disc, the device and its power, the energy so far ---
  function row(X, key, P, E, y, fh) {
    const c = COL[X];
    p.stroke(...COL.ink); p.strokeWeight(2); p.fill(238, 241, 244); p.rect(14, y, 76, 70, 8);   // meter case
    p.fill(255); p.rect(22, y + 8, 60, 28, 4);                                                     // its window
    p.noStroke(); p.fill(196, 204, 212); p.ellipse(52, y + 24, 52, 10);                            // the disc, edge on
    const a = turn[X] * p.TWO_PI, mx = 52 + 24 * Math.sin(a), front = Math.cos(a) > 0;
    if (front) { p.fill(201, 42, 42); p.rect(mx - 3, y + 19, 6, 10, 1); }                          // the red mark when in front
    p.stroke(...COL.ink); p.strokeWeight(1.5); p.noFill(); p.ellipse(52, y + 24, 52, 10);
    p.noStroke(); p.fill(...c); p.rect(22, y + 46, 60, 14, 3);                                    // the device's colour
    p.stroke(...c); p.strokeWeight(4); p.line(90, y + 53, 106, y + 53);                            // the cord to the device
    lab(`$\\text{${X}:}\\ \\text{${__('d_' + key)}}$`, 112, y + 24, 'l', fh, c);
    lab(`$P_\\text{${X}} = ${fP(P)}$`, 112, y + 62, 'l', fh);
    lab(`$E_\\text{${X}} = ${fE(E)}$`, 588, y + 42, 'r', fh, c);
  }

  // --- the graph E(t): both lines to one scale, the slope is the power ---
  function graph(rows, fh) {
    const tMax = nice(Math.max(rows[0][2], rows[1][2]) / 60, 5), uE = unit(Math.max(rows[0][3], rows[1][3]));
    const eMax = nice(Math.max(rows[0][3], rows[1][3]) / uE.f, 4);
    const X = (th) => GX0 + (GX1 - GX0) * th / tMax.max, Y = (e) => GY1 - (GY1 - GY0) * e / eMax.max;
    p.stroke(...COL.grid); p.strokeWeight(1);
    for (let i = 1; i <= eMax.n; i++) p.line(GX0, Y(i * eMax.step), GX1, Y(i * eMax.step));
    for (let i = 1; i <= tMax.n; i++) p.line(X(i * tMax.step), GY0, X(i * tMax.step), GY1);
    const c = p.drawingContext;
    for (const [Xn, P, t, E] of rows) {                                   // dashed beyond the device's time, clipped to the box
      const slope = P * 3600 / uE.f;                                       // energy in the axis unit per hour
      const tEnd = Math.min(tMax.max, eMax.max / slope);
      c.save(); c.beginPath(); c.rect(GX0, GY0 - 2, GX1 - GX0 + 2, GY1 - GY0 + 2); c.clip();
      p.stroke(...COL[Xn]); p.strokeWeight(2.5); c.setLineDash([7, 6]); p.line(X(0), Y(0), X(tEnd), Y(slope * tEnd));
      c.setLineDash([]); p.strokeWeight(4); p.line(X(0), Y(0), X(t / 60), Y(E / uE.f));
      c.restore();
      p.stroke(255); p.strokeWeight(2); p.fill(...COL[Xn]); p.circle(X(t / 60), Y(E / uE.f), 12);
    }
    p.stroke(...COL.ink); p.strokeWeight(2); p.line(GX0, GY1, GX1 + 10, GY1); p.line(GX0, GY1, GX0, GY0 - 10);
    p.noStroke(); p.fill(...COL.ink);
    p.triangle(GX1 + 16, GY1, GX1 + 6, GY1 - 5, GX1 + 6, GY1 + 5); p.triangle(GX0, GY0 - 16, GX0 - 5, GY0 - 6, GX0 + 5, GY0 - 6);
    for (let i = 0; i <= tMax.n; i++) lab(`$${sig(i * tMax.step)}$`, X(i * tMax.step), GY1 + fh + 4, 'c', fh);
    for (let i = 0; i <= eMax.n; i++) lab(`$${sig(i * eMax.step)}$`, GX0 - 8, Y(i * eMax.step) + 0.35 * fh, 'r', fh);
    lab(`$E\\ (\\text{${uE.u}})$`, GX0 + 10, GY0 - 14, 'l', fh);
    lab(`$t\\ (\\text{h})$`, GX1 + 24, GY1 - 8, 'l', fh);
  }

  // an axis from 0 to a round number: steps of 1, 2 or 5 times a power of ten, at most nmax of them
  function nice(v, nmax) {
    const raw = Math.max(v, 1e-9) / nmax, m = Math.pow(10, Math.floor(Math.log10(raw)));
    const step = [1, 2, 5, 10].map((x) => x * m).find((s) => s >= raw * (1 - 1e-9));
    const n = Math.max(1, Math.ceil(v / step - 1e-9));
    return { step, n, max: n * step };
  }
  const unit = (e) => (e >= 1e7 ? { u: 'MJ', f: 1e6 } : e >= 1e4 ? { u: 'kJ', f: 1e3 } : { u: 'J', f: 1 });

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }

  // numbers inside LaTeX: three significant figures, decimal comma as {,}; powers and energies with a fitting unit
  const sig = (x) => String(parseFloat(Number(x).toPrecision(3))).replace('.', '{,}');
  const fP = (w) => (w >= 1000 ? `${sig(w / 1000)}\\,\\text{kW}` : `${sig(w)}\\,\\text{W}`);
  const fE = (j) => (j >= 1e6 ? `${sig(j / 1e6)}\\,\\text{MJ}` : j >= 1000 ? `${sig(j / 1000)}\\,\\text{kJ}` : `${sig(j)}\\,\\text{J}`);
});
