// fy8-13 Säteilyannos ja säteilyturvallisuus Suomessa: protection from a gamma point source by distance, shielding
// and time. A model source (a gamma capsule in a lead pot open towards the dosimeter) gives the dose rate
// 40,0 µSv/h at 1,0 m. The dosimeter's window (area A) catches the share A / (4 pi r^2) of the photons sent out in all
// directions, so the dose rate falls as 1 / r^2; a lead plate of thickness x lets through the share (1/2)^(x / d½)
// with the half-value layer d½ = 6,0 mm (narrow-beam model, no build-up, no absorption in air, no background).
// The stay time t runs with Käynnistä at the chosen speed (simulated minutes per second) or is set with its slider;
// the dose is H = Hdot t. The picture: the pot, the photons flying out as orange dots (those stopped in the lead flash
// there, those reaching the window flash it), the lead plate drawn as thick as x, the dosimeter on a stand at r on a
// floor with a metre scale. The photons are a picture of the model, not a count: the readout is computed. Every canvas
// text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const H1 = 40.0, DHALF = 6.0, TMAX = 60;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], PAPER = [246, 241, 230], IRONC = [108, 117, 125], EDGE = [138, 150, 163], ALU = [196, 204, 212],
        GLASSC = [238, 245, 249], METAL = [138, 150, 163];
  const SX = 70, PX = 120, FLOOR = 300, SY = 214, SLAB = 116;     // source x, px per metre, floor, beam height, plate's left edge
  let sk = 1, fh = 13, labels = [];
  let btnRun, slR, slX, slT, selSpeed, lR, lX, lT, readout;
  let t = 0, running = false, photons = [], flashes = [], emitAcc = 0, seed = 7;

  const rand = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };   // the picture only
  const params = () => ({ r: Number(slR.value()), x: Number(slX.value()) });
  const X = (r) => SX + r * PX;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnRun = p.createButton(__('kaynnista')).parent(controls);
    btnRun.elt.addEventListener('click', () => { if (running) running = false; else { if (t >= TMAX - 1e-9) t = 0; running = true; } });
    const l1 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l1); slR = p.createSlider(1, 4, 1, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lX = p.createSpan('').parent(l2); slX = p.createSlider(0, 30, 0, 3).parent(l2);
    const l3 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l3); slT = p.createSlider(0, TMAX, 0, 1).parent(l3);
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l4); selSpeed = p.createSelect().parent(l4);
    selSpeed.option(__('hidas'), '1'); selSpeed.option(__('normaali'), '3'); selSpeed.option(__('nopea'), '10'); selSpeed.selected('3');
    for (const ev of ['input', 'change']) slT.elt.addEventListener(ev, () => { t = Number(slT.value()); running = false; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { r: { input: slR.elt, unit: 'm' }, x: { input: slX.elt, unit: 'mm' }, t: { input: slT.elt, unit: 'min' } },
      reset: () => { slR.value(1); slX.value(0); t = 0; slT.value(0); running = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = params(), dt = Math.min(p.deltaTime, 100) / 1000, speed = Number(selSpeed.value());
    if (running) {
      t = Math.min(TMAX, t + dt * speed);
      if (t >= TMAX) running = false;
      slT.value(Math.round(t));
    }
    const trans = Math.pow(0.5, S.x / DHALF);
    const share = 1 / (4 * Math.PI * S.r * S.r);                 // the window's share per unit area at r
    const Hdot = H1 * share * 4 * Math.PI * trans;                // calibrated: H1 at 1 m without lead
    const H = Hdot * t / 60;
    btnRun.html(running ? __('pysayta') : __('kaynnista'));
    lR.html(__('etaisyys', { r: tx(S.r, 1) }));
    lX.html(__('lyijy', { x: String(S.x) }));
    lT.html(__('aika', { t: tx(t, 0) }));
    readout.html(__('lukemat', { r: tx(S.r, 1), x: String(S.x), f: sig(100 * trans), Hd: sig(Hdot), t: tx(t, 0), H: sig(H) }));
    window.simState = { r: S.r, x: S.x, t, Hdot, H, trans, running: running ? 1 : 0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const kk = Math.max(1, 600 / cw);
    sk = cw < 500 ? kk : 1; fh = cw < 500 ? Math.round(14 * kk) : 15;
    labels = [];
    p.background(255);
    room();
    beam(S, trans, dt * Math.max(1, speed / 3));
    pot();
    plate(S);
    meter(S, Hdot);
    window.simState.labels = labels;
  };

  // --- the room: wall, floor and the metre scale ---
  function room() {
    p.noStroke(); p.fill(...PAPER); p.rect(0, 0, 600, FLOOR);
    p.fill(...GRID); p.rect(0, FLOOR, 600, 400 - FLOOR);
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(16, FLOOR, 584, FLOOR);
    for (let r = 0; r <= 4.0001; r += 0.5) {
      const xx = X(r), major = Math.abs(r - Math.round(r)) < 1e-9;
      p.stroke(...INKC); p.strokeWeight(2); p.line(xx, FLOOR, xx, FLOOR + (major ? 9 : 5) * sk);
      if (major) lab('$' + String(Math.round(r)) + '$', xx, FLOOR + 1.7 * fh, 'c', INKC);
    }
    lab('$r\\ (\\text{m})$', 590, FLOOR + 3.2 * fh, 'r', INKC);
  }

  // --- the lead pot with the source capsule, open towards the dosimeter ---
  function pot() {
    p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...IRONC);
    p.beginShape(); p.vertex(SX - 44, FLOOR - 120); p.vertex(SX + 24, FLOOR - 120); p.vertex(SX + 24, SY - 18);
    p.vertex(SX - 6, SY - 18); p.vertex(SX - 6, SY + 18); p.vertex(SX + 24, SY + 18); p.vertex(SX + 24, FLOOR);
    p.vertex(SX - 44, FLOOR); p.endShape(p.CLOSE);
    p.noStroke(); p.fill(...METAL); p.rect(SX - 40, FLOOR - 116, 10, 112, 3);
    p.fill(...HEATL); p.circle(SX + 6, SY, 24); p.fill(...HEATC); p.circle(SX + 6, SY, 13);
    lab(__('lahde_kanvas'), SX - 10, FLOOR - 120 - 0.8 * fh, 'c', INKC);
  }

  // --- the lead plate, as thick as x (1,5 px per mm) ---
  function plate(S) {
    const w = S.x * 1.5;
    if (w > 0) {
      p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...IRONC); p.rect(SLAB, FLOOR - 156, w, 156);
      p.noStroke(); p.fill(...EDGE); p.rect(SLAB + 2, FLOOR - 154, Math.max(1, w * 0.25), 152);
    } else {
      p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]);
      p.line(SLAB, FLOOR - 156, SLAB, FLOOR); p.drawingContext.setLineDash([]);
    }
    lab('$d = ' + String(S.x) + '\\,\\text{mm}$', SLAB + w / 2, FLOOR + 3.2 * fh, 'c', INKC);
  }

  // --- the dosimeter on a stand at r ---
  function meter(S, Hdot) {
    const xm = X(S.r);
    p.stroke(...INKC); p.strokeWeight(4); p.line(xm, SY + 44, xm, FLOOR); p.strokeWeight(3); p.line(xm - 28, FLOOR, xm + 28, FLOOR);
    p.strokeWeight(2.5); p.fill(...ALU); p.rect(xm - 26, SY - 46, 62, 90, 9);
    p.fill(...GLASSC); p.rect(xm - 14, SY - 34, 38, 24, 4);
    p.fill(...INKC); p.rect(xm - 10, SY + 6, 30, 6, 3); p.rect(xm - 10, SY + 20, 30, 6, 3);
    p.noStroke(); p.circle(xm - 26, SY, 22);
    const hit = flashes.some((f) => f.kind === 'win' && f.age < 0.25);
    if (hit) { p.fill(...HEATC); p.circle(xm - 26, SY, 15); }
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 5]); p.line(xm, SY - 52, xm, 3.4 * fh); p.drawingContext.setLineDash([]);
    lab('$\\dot{H} = ' + sig(Hdot) + '\\,\\mu\\text{Sv/h}$', xm, 1.4 * fh, 'c', HEATC);
    lab('$r = ' + tx(S.r, 1) + '\\,\\text{m}$', xm, 2.9 * fh, 'c', INKC);
  }

  // --- photons: a picture of the model (rays spread out; the lead stops a share of them) ---
  function beam(S, trans, dts) {
    const v = 260, wPlate = S.x * 1.5;
    emitAcc += dts * 90;
    while (emitAcc >= 1) {
      emitAcc -= 1;
      const a = (rand() - 0.5) * 0.9;
      const stop = rand() > trans ? SLAB + rand() * Math.max(wPlate, 1) : Infinity;
      photons.push({ x: SX + 10, y: SY, vx: v * Math.cos(a), vy: v * Math.sin(a), stop });
    }
    const xm = X(S.r);
    const keep = [];
    for (const ph of photons) {
      const x0 = ph.x;
      ph.x += ph.vx * dts; ph.y += ph.vy * dts;
      if (ph.x >= ph.stop) { flashes.push({ x: ph.stop, y: ph.y, age: 0, kind: 'lead' }); continue; }
      if (x0 < xm - 26 && ph.x >= xm - 26 && Math.abs(ph.y - SY) < 11) { flashes.push({ x: xm - 26, y: SY, age: 0, kind: 'win' }); continue; }
      if (ph.x > 600 || ph.y < 0 || ph.y > FLOOR) continue;
      keep.push(ph);
    }
    photons = keep.slice(-400);
    p.noStroke();
    for (const ph of photons) {
      p.fill(HEATL[0], HEATL[1], HEATL[2], 160); p.circle(ph.x - ph.vx * 0.025, ph.y - ph.vy * 0.025, 7);
      p.fill(...HEATC); p.circle(ph.x, ph.y, 7);
    }
    flashes = flashes.filter((f) => (f.age += dts) < 0.4);
    for (const f of flashes) {
      if (f.kind !== 'lead') continue;
      p.fill(HEATL[0], HEATL[1], HEATL[2], 255 * (1 - f.age / 0.4)); p.circle(f.x, f.y, 6 + 18 * f.age);
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), 400 - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (v, d) => v.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  // three significant figures
  const sig = (v) => v === 0 ? '0' : tx(v, v >= 99.95 ? 0 : v >= 9.995 ? 1 : v >= 0.9995 ? 2 : v >= 0.09995 ? 3 : 4);
});
