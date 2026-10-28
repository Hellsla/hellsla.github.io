// fy2-8 Kasvihuoneilmiö: sunlight passes the atmosphere, the warm ground sends heat radiation up, and greenhouse gas
// molecules absorb part of it and send it on in a random direction, some of it back down to the ground.
// Qualitative FY2 model, no radiative balance (that is FY3, "Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos"):
// the four levels of the select carry the ground's mean temperature as rounded source values, the sim does not compute
// them. Without greenhouse gases about −18 °C; pre-industrial (CO2 280 ppm) about +14 °C; CO2 doubled (560 ppm) about
// +17 °C once settled (IPCC AR6 WG1 2021: equilibrium climate sensitivity best estimate 3 °C). Today (420 ppm) the mean
// is about +15 °C measured (IPCC AR6: 1,1 °C warmer in 2011–2020 than in 1850–1900) but not settled: with the same
// sensitivity 420 ppm settles at about 14 + 3 · log2(420 : 280) ≈ +16 °C, so the sim starts at +15 °C and still warms.
// towards the level's value gradually, to show that warming lags the change in the gases (in reality decades).
// The photons are a picture, not to scale: yellow short waves = sunlight, red long waves = heat radiation; the ground
// sends heat radiation the faster the warmer it is ((T/255 K)^4, so the picture brightens as it warms). The share
// absorbed grows with the level (0; 0,80; 0,84; 0,88) to make the change visible; the real atmosphere absorbs most of the
// ground's heat radiation at every level with greenhouse gases. The speed select changes the pace of the picture and of
// the warming, never the settled temperature. Every canvas text goes through lab(). p5.js 1.9 instance mode.
new p5((p) => {
  const LEV = {
    0:   { T: -18, a: 0,    co2: 0, h2o: 0, ch4: 0, name: 'ei' },
    280: { T: 14,  a: 0.80, co2: 4, h2o: 6, ch4: 1, name: 'esi' },
    420: { T: 16,  a: 0.84, co2: 6, h2o: 6, ch4: 1, name: 'nyt' },
    560: { T: 17,  a: 0.88, co2: 8, h2o: 6, ch4: 1, name: 'tupla' },
  };
  const ORDER = ['0', '280', '420', '560'], INIT = '420', T_NOW = 15;   // today's measured mean, still rising towards the 420 ppm value
  const ATM0 = 92, ATM1 = 292, GROUND = 300, XR = 462;                    // atmosphere band, ground line, right edge of the scene
  const TT = 128, TB = 318, TMIN = -30, TMAX = 30, TX = 556;               // thermometer: top/bottom of the scale, tube x
  const SUN = { x: 50, y: 42 };
  const COL = { sun: [245, 159, 0], ir: [201, 42, 42], ink: [31, 41, 51], N: [116, 143, 252], O: [224, 49, 49], C: [73, 80, 87], H: [248, 249, 250] };
  let sel, selSp, readout, labels = [], T = 15, mols = [], ph = [], rings = [], sunAcc = 0, irAcc = 0;

  // --- fixed molecule positions (seeded), so the picture is the same on every load ---
  function seeded(seed) { return () => { seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
  function place() {
    const r = seeded(7), kinds = [];
    for (let i = 0; i < 8; i++) kinds.push(['CO2', i]);
    for (let i = 0; i < 6; i++) kinds.push(['H2O', i]);
    kinds.push(['CH4', 0]);
    for (let i = 0; i < 12; i++) kinds.push(['N2', i]);
    for (let i = 0; i < 4; i++) kinds.push(['O2', i]);
    for (const [kind, i] of kinds) {
      for (let tries = 0; tries < 400; tries++) {
        const x = 26 + r() * (XR - 52), y = ATM0 + 34 + r() * (ATM1 - ATM0 - 52);
        if (x < 170 && y < ATM0 + 44) continue;                            // keep the word "ilmakehä" clear
        if (mols.every((m) => Math.hypot(m.x - x, m.y - y) > 38)) { mols.push({ kind, i, x, y, glow: 0, ang: r() * Math.PI }); break; }
      }
    }
  }
  const shown = (m, L) => (m.kind === 'CO2' ? m.i < L.co2 : m.kind === 'H2O' ? m.i < L.h2o : m.kind === 'CH4' ? m.i < L.ch4 : true);
  const gh = (m) => m.kind === 'CO2' || m.kind === 'H2O' || m.kind === 'CH4';

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l = p.createElement('label').parent(controls); p.createSpan(__('kaasut')).parent(l); sel = p.createSelect().parent(l);
    for (const v of ORDER) sel.option(__('taso_' + LEV[v].name), v);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSp = p.createSelect().parent(ls);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    place();
    reset();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset the level
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { co2: { input: sel.elt, unit: 'ppm' } },
      reset, step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function reset() { sel.selected(INIT); selSp.selected('1'); T = T_NOW; ph = []; rings = []; }

  p.draw = () => {
    const key = sel.value(), L = LEV[key], speed = Number(selSp.value());
    const dt = Math.min(p.deltaTime, 100) / 1000 * speed;
    const Tprev = T;
    T += (L.T - T) * (1 - Math.exp(-dt / 3));                              // warming lags the change of the gases
    if (Math.abs(L.T - T) < 0.05) T = L.T;
    const trend = T === L.T ? 'asettunut' : T < L.T ? 'lampenee' : 'jaahtyy';
    step(L, dt);
    readout.html((key === '0' ? __('lukema_ei') : __('lukema_taso', { taso: __('taso_' + L.name), c: key })) +
      '<br>' + __('lukema_T', { T: fT(Math.round(T)), tila: __(trend) }) + '<br>' + __('lukema_Teq', { T: fT(L.T) }));
    window.simState = { co2: Number(key), a: L.a, T, Teq: L.T, tila: trend, nopeus: speed, kasvihuonekaasuja: L.co2 + L.h2o + L.ch4,
      fotoneja: ph.length, labels: null, dT: T - Tprev };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(Math.max(20, 14 * k));                          // about 18 px on a wide screen, 14 px on a phone
    labels = [];
    scene(L, fh);
    window.simState.labels = labels;
  };

  // --- the photons: sunlight in, heat radiation out, absorbed and sent on by greenhouse gas molecules ---
  function step(L, dt) {
    const v = 150 * dt;
    sunAcc += dt * 8;
    while (sunAcc >= 1) { sunAcc -= 1;                                     // sunlight towards a random point of the ground
      const gx = 110 + Math.random() * (XR - 130), d = Math.hypot(gx - SUN.x, GROUND - SUN.y);
      ph.push({ sun: true, x: SUN.x + 20, y: SUN.y + 16, dx: (gx - SUN.x) / d, dy: (GROUND - SUN.y) / d, to: null }); }
    irAcc += dt * 8 * Math.pow((T + 273) / 255, 4);
    const targets = mols.filter((m) => gh(m) && shown(m, L));
    while (irAcc >= 1) { irAcc -= 1;                                      // heat radiation from the ground
      if (targets.length && Math.random() < L.a) {
        const m = targets[Math.floor(Math.random() * targets.length)], x0 = Math.min(XR - 10, Math.max(10, m.x + (Math.random() - 0.5) * 140));
        aim({ sun: false, x: x0, y: GROUND, to: m }, m.x, m.y);
      } else {
        const ang = (Math.random() - 0.5) * 1.1, x0 = 20 + Math.random() * (XR - 40);
        ph.push({ sun: false, x: x0, y: GROUND, dx: Math.sin(ang), dy: -Math.cos(ang), to: null });
      }
    }
    for (const q of ph) {
      q.x += q.dx * v; q.y += q.dy * v;
      if (q.to && (q.y <= q.to.y || Math.hypot(q.x - q.to.x, q.y - q.to.y) < 6)) {   // absorbed by its molecule: sent on
        const m = q.to; m.glow = 1; rings.push({ x: m.x, y: m.y, r: 4 }); q.dead = true;
        const up = Math.random() < 0.5, ang = (Math.random() - 0.5) * 1.6, above = targets.filter((o) => o.y < m.y - 30 && Math.abs(o.x - m.x) < 120);
        const n = { sun: false, x: m.x, y: m.y, dx: Math.sin(ang), dy: up ? -Math.cos(ang) : Math.cos(ang), to: null, from: m };
        if (up && above.length && Math.random() < L.a * 0.45) { const o = above[Math.floor(Math.random() * above.length)]; aim(n, o.x, o.y); n.to = o; }
        else ph.push(n);
      }
      if (q.sun && q.y >= GROUND) { q.dead = true; rings.push({ x: q.x, y: GROUND, r: 3, sun: true }); }
      if (!q.sun && !q.to && q.dy > 0 && q.y >= GROUND) { q.dead = true; rings.push({ x: q.x, y: GROUND, r: 3 }); }
      if (q.y < -30 || q.x < -30 || q.x > XR + 30) q.dead = true;
    }
    ph = ph.filter((q) => !q.dead).slice(-220);
    for (const r of rings) r.r += 40 * dt;
    rings = rings.filter((r) => r.r < 16);
    for (const m of mols) m.glow = Math.max(0, m.glow - dt * 1.5);
  }
  function aim(q, tx, ty) { const d = Math.hypot(tx - q.x, ty - q.y) || 1; q.dx = (tx - q.x) / d; q.dy = (ty - q.y) / d; ph.push(q); }

  // --- the picture: space, the Sun, the atmosphere with its molecules, the ground, a thermometer, a key ---
  function scene(L, fh) {
    const c = p.drawingContext;
    let g = c.createLinearGradient(0, 0, 0, GROUND);
    g.addColorStop(0, '#0b1d3a'); g.addColorStop(ATM0 / GROUND, '#1c3d6e'); g.addColorStop((ATM0 + 30) / GROUND, '#a5d8ff'); g.addColorStop(1, '#e7f5ff');
    c.fillStyle = g; c.fillRect(0, 0, 600, GROUND);
    // the ground: snow and ice when cold, grass when warm; soil under it
    const w = Math.min(1, Math.max(0, (T + 10) / 20));
    p.noStroke(); p.fill(p.lerpColor(p.color(233, 240, 246), p.color(116, 184, 22), w)); p.rect(0, GROUND, 600, 18);
    p.fill(156, 112, 70); p.rect(0, GROUND + 18, 600, 42);
    p.fill(250); p.rect(0, 360, 600, 40);                                   // the key's strip
    p.stroke(...COL.ink); p.strokeWeight(1.5); p.line(0, GROUND, 600, GROUND); p.line(0, 360, 600, 360);
    // the Sun
    p.noStroke(); p.fill(255, 212, 59, 90); p.circle(SUN.x, SUN.y, 84); p.fill(255, 212, 59); p.stroke(245, 159, 0); p.strokeWeight(2); p.circle(SUN.x, SUN.y, 52);
    // molecules
    for (const m of mols) if (shown(m, L)) molecule(m.kind, m.x, m.y, m.ang, m.glow);
    // photons as short waves along their path
    for (const q of ph) wave(q);
    for (const r of rings) { p.noFill(); p.stroke(...(r.sun ? COL.sun : COL.ir), 200 * (1 - r.r / 16)); p.strokeWeight(2); p.circle(r.x, r.y, 2 * r.r); }
    thermometer(fh);
    // labels
    lab(`$\\text{${__('aurinko')}}$`, 92, 50, 'l', fh, [255, 212, 59]);
    lab(`$\\text{${__('avaruus')}}$`, 300, 40, 'c', fh, [233, 236, 239]);
    lab(`$\\text{${__('ilmakeha')}}$`, 14, ATM0 + 30, 'l', fh, [24, 64, 120]);
    lab(`$\\text{${__('maanpinta')}}$`, 14, GROUND + 50, 'l', fh, [255, 255, 255]);
    let x = 14;                                                             // the key: one of each molecule and its formula
    for (const [kind, tex] of [['N2', '\\text{N}_2'], ['O2', '\\text{O}_2'], ['CO2', '\\text{CO}_2'], ['H2O', '\\text{H}_2\\text{O}'], ['CH4', '\\text{CH}_4']]) {
      molecule(kind, x + 14, 381, 0, 0); x += 34;
      x = lab(`$${tex}$`, x, 381 + 0.35 * fh, 'l', fh, gh({ kind }) ? [24, 24, 24] : [90, 98, 106]) + 18;
    }
  }

  function wave(q) {
    const len = q.sun ? 26 : 34, lam = q.sun ? 7 : 15, amp = q.sun ? 3 : 4.5, nx = -q.dy, ny = q.dx;
    p.noFill(); p.stroke(...(q.sun ? COL.sun : COL.ir)); p.strokeWeight(q.sun ? 2 : 2.5);
    p.beginShape();
    for (let s = 0; s <= len; s += 1.5) { const o = amp * Math.sin((s / lam) * p.TWO_PI); p.vertex(q.x - q.dx * s + nx * o, q.y - q.dy * s + ny * o); }
    p.endShape();
    p.noStroke(); p.fill(...(q.sun ? COL.sun : COL.ir)); p.circle(q.x, q.y, 5);
  }

  function atom(x, y, d, col) { p.stroke(...COL.ink); p.strokeWeight(1); p.fill(...col); p.circle(x, y, d); }
  function molecule(kind, x, y, ang, glow) {
    if (glow > 0) { p.noStroke(); p.fill(255, 146, 43, 160 * glow); p.circle(x, y, 34 + 10 * glow); }
    const ca = Math.cos(ang), sa = Math.sin(ang);
    if (kind === 'N2' || kind === 'O2') { const col = kind === 'N2' ? COL.N : COL.O; atom(x - 4.5 * ca, y - 4.5 * sa, 11, col); atom(x + 4.5 * ca, y + 4.5 * sa, 11, col); }
    else if (kind === 'CO2') { atom(x - 9 * ca, y - 9 * sa, 10, COL.O); atom(x + 9 * ca, y + 9 * sa, 10, COL.O); atom(x, y, 11, COL.C); }
    else if (kind === 'H2O') { for (const s of [-1, 1]) atom(x + 8 * Math.cos(ang + s * 0.9 + 1.57), y + 8 * Math.sin(ang + s * 0.9 + 1.57), 7, COL.H); atom(x, y, 12, COL.O); }
    else { for (const a of [0.3, 1.9, 3.5, 5.1]) atom(x + 8 * Math.cos(a + ang), y + 8 * Math.sin(a + ang), 6, COL.H); atom(x, y, 11, COL.C); }
  }

  // --- a thermometer from −30 °C to +30 °C with the reference values −18 °C, 0 °C and +15 °C ---
  function thermometer(fh) {
    const Y = (t) => TB - (TB - TT) * (t - TMIN) / (TMAX - TMIN);
    p.stroke(...COL.ink); p.strokeWeight(1.5); p.fill(255, 255, 255, 235); p.rect(XR + 4, 74, 600 - XR - 8, 282, 10);
    p.fill(255); p.strokeWeight(2); p.rect(TX - 8, TT - 12, 16, TB - TT + 20, 8); p.circle(TX, TB + 20, 26);
    p.noStroke(); p.fill(224, 49, 49); p.circle(TX, TB + 20, 18); p.rect(TX - 4, Y(T), 8, TB + 14 - Y(T));
    p.stroke(...COL.ink); p.strokeWeight(1.5);
    for (let t = TMIN; t <= TMAX; t += 10) p.line(TX + 8, Y(t), TX + 16, Y(t));
    for (const t of [-18, 0, 15]) { p.strokeWeight(2); p.line(TX - 16, Y(t), TX - 8, Y(t)); lab(`$${fT(t)}$`, TX - 20, Y(t) + 0.35 * fh, 'r', fh); }
    lab(`$${fT(Math.round(T))}$`, (XR + 600) / 2, 74 + 0.95 * fh, 'c', fh, [201, 42, 42]);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates); returns its right edge
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
    return x0 + w;
  }

  // a temperature in LaTeX with its sign: +15 °C, −18 °C, 0 °C
  const fT = (t) => `${t > 0 ? '+' : ''}${t}\\,{}^\\circ\\text{C}`;
});
