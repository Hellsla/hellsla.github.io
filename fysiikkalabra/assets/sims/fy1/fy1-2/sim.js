// fy1-2 Suureet, yksiköt ja SI-järjestelmä: the solar system to true scale, "if the Moon were only 1 pixel".
// Scale: 1 px of the strip = the Moon's diameter, 3474 km, so the Sun is 1 392 000 km / 3474 km = 401 px wide, the Earth 3,7 px
// and Neptune about 1,3 million px from the Sun. The view scrolls (drag, wheel, arrow keys and buttons, a slider for the power
// of ten d = 10^n km, a jump button for every body and for Voyager 2); the picture never zooms.
// Distances: the planets stand at their mean orbital radii (semi-major axes, JPL "Approximate Positions of the Planets"), all on
// one line from the Sun, diameters are equatorial (NASA planetary fact sheets); only the distance along the strip is real.
// Light: c = 299 792,458 km/s = 86,3 px/s. "Matkusta valon nopeudella" sends a light pulse from the view's centre; the clock runs
// in simulated time (dt·speed), so ×1, ×100 and ×10 000 change only the pace: the elapsed time at a given point is the same.
// Voyager 2 (model values, source: model): d = d0 + v (t - t0) with d0 = 119,7 AU on 2018-11-05 (heliopause crossing, NASA/JPL)
// and v = 15,341 km/s (JPL Voyager mission status); 1 AU = 149 597 870,7 km. The marker is drawn larger than the probe (a pin).
// Every canvas text is a LaTeX string drawn through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const W = 600, H = 400, CX = 300, AY = 190;                              // canvas size, view centre column, the strip's axis row
  const MOON_KM = 3474, AU_KM = 149597870.7, C_KMS = 299792.458;           // km per px, km per AU, light speed (km/s)
  const CPX = C_KMS / MOON_KM;                                             // light speed in px per simulated second (86,3)
  const N_MIN = 6, N_MAX = 11, XMAX = 1e11 / MOON_KM;                      // slider d = 10^n km; the strip ends at 10^11 km
  const D0_AU = 119.7, V_KMS = 15.341, T0 = Date.UTC(2018, 10, 5);         // Voyager 2 model: d0, v, t0
  const DATE_MIN = '2018-11-05', DATE_MAX = '2100-12-31';
  const BODIES = [                                                         // semi-major axis (AU), equatorial diameter (km), colour for the bar
    { id: 'aurinko', a: 0, D: 1392000, col: [255, 200, 70] },
    { id: 'merkurius', a: 0.38709927, D: 4879, col: [196, 204, 212] },
    { id: 'venus', a: 0.72333566, D: 12104, col: [241, 223, 181] },
    { id: 'maa', a: 1.00000261, D: 12756, col: [90, 160, 230] },
    { id: 'mars', a: 1.52371034, D: 6792, col: [232, 130, 92] },
    { id: 'jupiter', a: 5.202887, D: 142984, col: [214, 170, 130] },
    { id: 'saturnus', a: 9.53707032, D: 120536, col: [232, 214, 160] },
    { id: 'uranus', a: 19.18916464, D: 51118, col: [170, 226, 232] },
    { id: 'neptunus', a: 30.06992276, D: 49528, col: [70, 100, 220] },
  ];
  const MOON = { D: 3474, fromEarth: 384400 };
  for (const b of BODIES) { b.x = b.a * AU_KM / MOON_KM; b.r = b.D / MOON_KM / 2; }
  const EARTH = BODIES[3];

  let sel, lSel, selSp, sl, lSl, inDate, btn, readout;
  let xc = 0, vel = 0, dragging = false, lastX = 0, lastT = 0, holdDir = 0, holdT = 0, sliderBusy = false;   // view centre (px), drag inertia, held arrow
  let wheelM = 1, wheelT = 0, lastRead = 0, lastHtml = '', k = 1, labels = [];
  const trip = { on: false, active: false, start: 0, pos: 0, end: 0 };    // the light pulse: running, drawn, start/position/stop (px)
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  // --- numbers for LaTeX: decimal comma, three significant figures, powers of ten ---
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}').replace('-', '−');
  const sci = (x) => {                                                    // 2,18\cdot10^{10}
    if (!x) return '0';
    let e = Math.floor(Math.log10(Math.abs(x))), m = x / Math.pow(10, e), s = m.toPrecision(3);
    if (parseFloat(s) >= 10) { m /= 10; e += 1; s = m.toPrecision(3); }
    return `${s.replace('.', '{,}')}\\cdot10^{${e}}`;
  };
  const num3 = (x) => {                                                   // three significant figures, no exponent
    if (!x) return '0';
    if (Math.abs(x) >= 1e5 || Math.abs(x) < 1e-3) return sci(x);
    let s = x.toPrecision(3);
    if (s.includes('e')) s = String(Number(s));
    return s.replace('.', '{,}');
  };
  const group = (v) => String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g, '\\,');
  const tTex = (s) => (s < 100 ? `${num3(s)}\\,\\text{s}` : s < 6000 ? `${num3(s / 60)}\\,\\text{min}` : `${num3(s / 3600)}\\,\\text{h}`);
  const pxTxt = (v) => (v >= 10 ? tx(v, 0) : tx(v, 1));
  const fiDate = (iso) => { const [y, m, d] = iso.split('-').map(Number); return `${d}.${m}.${y}`; };

  // --- Voyager 2, model: uniform motion from the heliopause crossing ---
  const todayIso = () => { const d = new Date(), pad = (n) => String(n).padStart(2, '0'); return clamp0(`${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`); };
  function clamp0(s) { return s < DATE_MIN ? DATE_MIN : s > DATE_MAX ? DATE_MAX : s; }
  const dateIso = () => { const v = inDate.value(); return /^\d{4}-\d{2}-\d{2}$/.test(v) ? clamp0(v) : lastDate; };
  let lastDate = DATE_MIN;
  function voyager(iso) {
    const [y, m, d] = iso.split('-').map(Number), dtS = (Date.UTC(y, m - 1, d) - T0) / 1000;
    const dKm = D0_AU * AU_KM + V_KMS * dtS;
    return { dKm, dAU: dKm / AU_KM, t: dKm / C_KMS, x: dKm / MOON_KM };
  }

  const jump = (x) => { xc = clamp(x, 0, XMAX); vel = 0; trip.on = false; };
  const reset = () => { xc = 0; vel = 0; trip.on = false; trip.active = false; selSp.selected('100'); inDate.value(todayIso()); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const cv = p.canvas;
    cv.style.touchAction = 'pan-y'; cv.style.cursor = 'grab'; cv.tabIndex = 0;
    cv.setAttribute('role', 'img'); cv.setAttribute('aria-label', __('kuva_selite'));
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('matkusta')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (trip.on) { trip.on = false; return; }
      const v = voyager(dateIso());
      if (!(trip.active && Math.abs(xc - trip.pos) < 1 && trip.pos < trip.end - 1)) {      // a new trip from the view's centre
        trip.start = xc; trip.pos = xc; trip.end = xc < v.x ? v.x : XMAX; trip.active = true;
      }
      trip.on = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', reset);
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 1], [__('normaali'), 100], [__('nopea'), 10000]]) selSp.option(txt, v);
    selSp.selected('100');                                                // pace only: the elapsed time is the same at every speed
    const bL = p.createButton('$\\leftarrow$').parent(controls), bRt = p.createButton('$\\rightarrow$').parent(controls);
    bL.attribute('aria-label', __('vasemmalle')); bRt.attribute('aria-label', __('oikealle'));
    for (const [b, dir] of [[bL, -1], [bRt, 1]]) {                       // hold to scroll, faster the longer it is held; a key press steps
      b.elt.addEventListener('pointerdown', (e) => { holdDir = dir; holdT = 0; vel = 0; trip.on = false; e.preventDefault(); });
      for (const ev of ['pointerup', 'pointerleave', 'pointercancel']) b.elt.addEventListener(ev, () => { if (holdDir === dir) holdDir = 0; });
      b.elt.addEventListener('click', (e) => { if (e.detail === 0) jump(xc + dir * 500); });
    }
    lSl = p.createElement('label').parent(controls); const lsp = p.createSpan('').parent(lSl); sl = p.createSlider(N_MIN, N_MAX, N_MIN, 0.01).parent(lSl);
    lSel = lsp;
    sl.elt.addEventListener('input', () => { jump(Math.pow(10, Number(sl.value())) / MOON_KM); });
    sl.elt.addEventListener('pointerdown', () => { sliderBusy = true; });
    for (const ev of ['pointerup', 'pointercancel', 'blur']) sl.elt.addEventListener(ev, () => { sliderBusy = false; });
    const ld = p.createElement('label').parent(controls); p.createSpan(__('voyager_paiva')).parent(ld);
    inDate = p.createInput(todayIso(), 'date').parent(ld); inDate.attribute('min', DATE_MIN); inDate.attribute('max', DATE_MAX);
    inDate.elt.style.cssText = 'min-height:40px;font:inherit;font-size:var(--fs-ui);padding:0 .6rem;border:1px solid #767676;border-radius:.4rem;background:#fff;color:var(--ink)';
    const jumps = p.createDiv('').parent(controls).class('jumps');
    jumps.style('display', 'flex'); jumps.style('flex-wrap', 'wrap'); jumps.style('gap', '.4rem'); jumps.style('flex', '1 1 100%');
    const jb = (label, target) => { const b = p.createButton(label).parent(jumps); b.elt.style.padding = '0 .8rem'; b.elt.addEventListener('click', () => jump(target())); };
    for (const b of BODIES) jb(__(b.id), () => b.x);
    jb(__('voyager_2'), () => voyager(dateIso()).x);
    p.createP(__('selite')).parent('sim-root').class('note');

    // drag, wheel and keys on the picture
    cv.addEventListener('pointerdown', (e) => { dragging = true; lastX = e.clientX; lastT = performance.now(); vel = 0; trip.on = false; try { cv.setPointerCapture(e.pointerId); } catch (err) { /* a synthetic or ended pointer */ } cv.style.cursor = 'grabbing'; });
    cv.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      const dx = (e.clientX - lastX) * (W / cv.getBoundingClientRect().width), now = performance.now();
      xc -= dx; lastX = e.clientX; vel = clamp(0.7 * vel + 0.3 * (-dx / (Math.max(8, now - lastT) / 1000)), -4000, 4000); lastT = now;
    });
    for (const ev of ['pointerup', 'pointercancel']) cv.addEventListener(ev, () => { dragging = false; cv.style.cursor = 'grab'; });
    cv.addEventListener('wheel', (e) => {
      e.preventDefault(); const now = performance.now();
      wheelM = now - wheelT < 250 ? Math.min(200, wheelM * 1.1) : 1; wheelT = now;
      const d = (Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY) * (e.deltaMode === 1 ? 16 : 1);
      xc += d * wheelM; vel = 0; trip.on = false;
    }, { passive: false });
    cv.addEventListener('keydown', (e) => {
      const step = e.shiftKey ? 10000 : 100;
      if (e.key === 'ArrowRight') jump(xc + step); else if (e.key === 'ArrowLeft') jump(xc - step);
      else if (e.key === 'Home') jump(0); else if (e.key === 'End') jump(voyager(dateIso()).x); else return;
      e.preventDefault();
    });
    p.textFont('Arial');
    reset(); lastDate = dateIso();
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { n: { input: sl.elt, unit: '' }, pvm: { input: inDate.elt, unit: '' }, nopeus: { input: selSp.elt, unit: '' } },
      reset, step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const dt = Math.min(p.deltaTime, 100) / 1000, speed = Number(selSp.value());
    // --- motion: held arrow, drag inertia, the light pulse ---
    if (holdDir) { holdT += dt; xc += holdDir * 300 * Math.pow(4, holdT) * dt; }
    else if (!dragging && Math.abs(vel) > 1) { xc += vel * dt; vel *= Math.exp(-3 * dt); }
    if (trip.on) {
      trip.pos = Math.min(trip.end, trip.pos + CPX * dt * speed);       // simulated time dt·speed: the pace is the only thing speed changes
      xc = trip.pos; if (trip.pos >= trip.end) trip.on = false;
    }
    xc = clamp(xc, 0, XMAX);
    const iso = dateIso(); lastDate = iso;
    if (inDate.value() !== iso && /^\d{4}-\d{2}-\d{2}$/.test(inDate.value())) inDate.value(iso);
    const vz = voyager(iso), dKm = xc * MOON_KM, nView = dKm > 1 ? Math.log10(dKm) : 0;
    if (!sliderBusy) sl.value(clamp(nView, N_MIN, N_MAX));
    const tripS = (trip.pos - trip.start) * MOON_KM, tripT = (trip.pos - trip.start) / CPX;

    lSel.html(__('etaisyys_n', { n: tx(Number(sl.value()), 2) }));
    let html = __('nakyma', { km: sci(dKm), au: num3(dKm / AU_KM), t: tTex(dKm / C_KMS) });
    if (trip.active) html += __('matka', { s: sci(tripS), t: tTex(tripT), x: group(speed) });
    html += __('voyager_rivi', { pvm: fiDate(iso), km: sci(vz.dKm), au: num3(vz.dAU), v: tx(V_KMS, 3), t: tTex(vz.t) });
    const now = performance.now();
    if (html !== lastHtml && (!trip.on || now - lastRead > 120)) { readout.html(html); lastHtml = html; lastRead = now; }
    const bt = trip.on ? __('tauko') : __('matkusta'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;

    window.simState = {
      x: xc, n: Number(sl.value()), dKm, dAU: dKm / AU_KM, tLight: dKm / C_KMS,
      pvm: iso, vKm: vz.dKm, vAU: vz.dAU, vKms: V_KMS, vTLight: vz.t, vTh: vz.t / 3600, vx: vz.x,
      running: trip.on, active: trip.active, speed, tTrip: trip.active ? tripT : 0, sTrip: trip.active ? tripS : 0, labels: null,
    };

    k = Math.max(1, W / (document.getElementById('sim-root').clientWidth || W));
    const ts = (v) => Math.round(v * k), fh = ts(11);
    labels = [];
    sky();
    const sx = (w) => CX + (w - xc);
    const tags = [];
    drawSun(sx(0), AY, BODIES[0].r, tags, fh);
    p.stroke(255, 255, 255, 40); p.strokeWeight(1); p.drawingContext.setLineDash([2, 6]); p.line(0, AY + 0.5, W, AY + 0.5); p.drawingContext.setLineDash([]);
    if (trip.active) pulse(sx(trip.start), sx(trip.pos));
    for (const b of BODIES.slice(1)) {
      const x = sx(b.x);
      if (x < -120 || x > W + 120) continue;
      drawBody(b, x);
      tags.push({ x, r: b.r, text: `$\\text{${__(b.id)}},\\ ${pxTxt(b.r * 2)}\\,\\text{px}$`, up: true });
    }
    const mx = sx(EARTH.x + MOON.fromEarth / MOON_KM);                     // the Moon: 1 px, 110 px from the Earth
    if (mx > -120 && mx < W + 120) {
      p.noStroke(); p.fill(205, 208, 214); p.circle(mx, AY, 1); ring(mx);
      tags.push({ x: mx, r: 0.5, text: `$\\text{${__('kuu')}},\\ 1{,}0\\,\\text{px}$`, up: false });
    }
    const vxs = sx(vz.x);
    if (vxs > -120 && vxs < W + 120) { probe(vxs); tags.push({ x: vxs, r: 7, text: `$\\text{${__('voyager_2')}}\\ (\\text{${__('malli')}})$`, up: true, big: true }); }
    ruler(fh);
    for (const t of tags) tag(t, fh);
    scaleBar(fh);
    panel(fh, vz, nView, tripT);
    window.simState.labels = labels;
  };

  // --- the picture ---
  function sky() {
    const c = p.drawingContext, g = c.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, 'rgb(5,8,20)'); g.addColorStop(1, 'rgb(16,22,46)');
    c.save(); c.fillStyle = g; c.fillRect(0, 0, W, H); c.restore();
    p.noStroke();
    for (let i = 0; i < 70; i++) {
      const a = Math.sin(i * 12.9898 + 4.1) * 43758.5453, b = Math.sin(i * 78.233 + 1.7) * 12345.678, r = Math.sin(i * 39.346 + 9.2) * 9876.54;
      p.fill(255, 255, 255, 70 + 140 * (r - Math.floor(r)));
      p.circle(W * (a - Math.floor(a)), H * 0.8 * (b - Math.floor(b)), 0.8 + 1.2 * (r - Math.floor(r)));
    }
  }

  function drawSun(x, y, R, tags, fh) {
    if (x + R * 1.5 < 0 || x - R * 1.5 > W) return;
    const c = p.drawingContext;
    c.save();
    let g = c.createRadialGradient(x, y, R * 0.9, x, y, R * 1.5);
    g.addColorStop(0, 'rgba(255,190,70,0.5)'); g.addColorStop(1, 'rgba(255,150,40,0)');
    c.fillStyle = g; c.beginPath(); c.arc(x, y, R * 1.5, 0, 6.2832); c.fill();
    g = c.createRadialGradient(x - R * 0.12, y - R * 0.12, R * 0.05, x, y, R);
    g.addColorStop(0, '#fff6cf'); g.addColorStop(0.5, '#ffd24a'); g.addColorStop(0.9, '#ffa21a'); g.addColorStop(1, '#e8590c');
    c.fillStyle = g; c.beginPath(); c.arc(x, y, R, 0, 6.2832); c.fill();
    c.clip();                                                            // granulation and two sunspot groups, fixed on the disc
    for (let i = 0; i < 90; i++) {
      const a = Math.sin(i * 12.9898) * 43758.5453, b = Math.sin(i * 78.233) * 12345.678, s = Math.sin(i * 39.346) * 9876.54;
      const ang = 6.2832 * (a - Math.floor(a)), rad = R * 0.95 * Math.sqrt(b - Math.floor(b)), sz = R * (0.025 + 0.045 * (s - Math.floor(s)));
      c.fillStyle = i % 2 ? 'rgba(255,250,210,0.09)' : 'rgba(210,90,0,0.07)';
      c.beginPath(); c.arc(x + rad * Math.cos(ang), y + rad * Math.sin(ang), sz, 0, 6.2832); c.fill();
    }
    for (const [sxp, syp, sr] of [[-0.35, -0.2, 0.035], [-0.28, -0.17, 0.022], [0.3, 0.28, 0.03], [0.36, 0.25, 0.018]]) {
      c.fillStyle = 'rgba(110,40,0,0.55)'; c.beginPath(); c.ellipse(x + sxp * R, y + syp * R, sr * R, sr * R * 0.8, 0, 0, 6.2832); c.fill();
    }
    g = c.createRadialGradient(x, y, R * 0.7, x, y, R);                   // limb darkening
    g.addColorStop(0, 'rgba(120,30,0,0)'); g.addColorStop(1, 'rgba(120,30,0,0.35)');
    c.fillStyle = g; c.fillRect(x - R, y - R, 2 * R, 2 * R);
    c.restore();
    const vis0 = Math.max(0, x - R), vis1 = Math.min(W, x + R);
    if (vis1 - vis0 > 40) tags.push({ x: (vis0 + vis1) / 2, r: R, text: `$\\text{${__('aurinko')}},\\ ${pxTxt(R * 2)}\\,\\text{px}$`, up: true, inside: true });
  }

  // lit from the left, where the Sun is: a soft highlight and a dark limb on the far side
  function shade(c, x, y, r) {
    const g = c.createRadialGradient(x - 0.45 * r, y - 0.1 * r, 0.1 * r, x - 0.2 * r, y, 1.45 * r);
    g.addColorStop(0, 'rgba(255,255,255,0.2)'); g.addColorStop(0.5, 'rgba(0,0,0,0)'); g.addColorStop(1, 'rgba(0,0,0,0.6)');
    c.fillStyle = g; c.fillRect(x - r - 1, y - r - 1, 2 * r + 2, 2 * r + 2);
  }
  function globe(x, y, r, light, dark, extra) {
    const c = p.drawingContext;
    if (r < 2.5) {                                                       // a body of a few pixels: a plain bright disc, shading would only darken it
      c.save(); c.fillStyle = light; c.beginPath(); c.arc(x, y, r, 0, 6.2832); c.fill(); c.restore(); return;
    }
    c.save(); c.beginPath(); c.arc(x, y, r, 0, 6.2832); c.clip();
    const g = c.createLinearGradient(x, y - r, x, y + r); g.addColorStop(0, light); g.addColorStop(1, dark);
    c.fillStyle = g; c.fillRect(x - r, y - r, 2 * r, 2 * r);
    if (extra) extra(c, x, y, r);
    shade(c, x, y, r);
    c.restore();
  }
  function bands(c, x, y, r, list) {
    for (let i = 0; i < list.length - 1; i++) { c.fillStyle = list[i][1]; c.fillRect(x - r, y + r * list[i][0], 2 * r, r * (list[i + 1][0] - list[i][0]) + 0.6); }
    c.fillStyle = list[list.length - 1][1]; c.fillRect(x - r, y + r * list[list.length - 1][0], 2 * r, r);
  }
  function saturnRing(x, y, half) {                                      // half -1: the far side behind the globe, +1: the near side in front
    const c = p.drawingContext, q = 0.36;
    for (const [ri, ro, col] of [[19.3, 26.5, 'rgba(120,100,70,0.5)'], [26.5, 33.8, 'rgba(228,208,164,0.96)'], [35.2, 39.4, 'rgba(204,184,144,0.92)']]) {
      c.save(); c.beginPath(); c.rect(x - ro - 2, half < 0 ? y - ro * q - 2 : y, 2 * ro + 4, ro * q + 2); c.clip();
      c.beginPath(); c.ellipse(x, y, ro, ro * q, 0, 0, 6.2832); c.ellipse(x, y, ri, ri * q, 0, 0, 6.2832, true);
      c.fillStyle = col; c.fill('evenodd'); c.restore();
    }
  }
  function drawBody(b, x) {
    const r = b.r;
    switch (b.id) {
      case 'merkurius': globe(x, AY, r, '#c4ccd4', '#6c757d'); break;
      case 'venus': globe(x, AY, r, '#f6e7bd', '#d9b26a'); break;
      case 'maa': globe(x, AY, r, '#8cc0f0', '#2f74b5'); break;
      case 'mars': globe(x, AY, r, '#ee9a74', '#a8452a'); break;
      case 'jupiter':
        globe(x, AY, r, '#e9dcc2', '#b98458', (c, cx, cy, rr) => {
          bands(c, cx, cy, rr, [[-1, '#e9dcc2'], [-0.72, '#c8946a'], [-0.5, '#efe3cb'], [-0.28, '#b87a4f'], [-0.08, '#ecdcc0'], [0.14, '#c99a72'], [0.34, '#efe2c8'], [0.55, '#b98458'], [0.76, '#e6d6b8']]);
          c.fillStyle = 'rgba(176,72,48,0.92)'; c.beginPath(); c.ellipse(cx + 0.28 * rr, cy + 0.36 * rr, 0.24 * rr, 0.14 * rr, 0, 0, 6.2832); c.fill();
        }); break;
      case 'saturnus':
        saturnRing(x, AY, -1);
        globe(x, AY, r, '#efdfaa', '#c2a46a', (c, cx, cy, rr) => bands(c, cx, cy, rr, [[-1, '#efdfaa'], [-0.55, '#e3cf96'], [-0.2, '#f1e3b4'], [0.2, '#d9c088'], [0.6, '#e8d6a0']]));
        saturnRing(x, AY, 1); break;
      case 'uranus': globe(x, AY, r, '#cdf0f2', '#8cc9d0'); break;
      case 'neptunus':
        globe(x, AY, r, '#5b86e8', '#1f2f8f', (c, cx, cy, rr) => {
          c.fillStyle = 'rgba(190,210,255,0.28)'; c.fillRect(cx - rr, cy - 0.35 * rr, 2 * rr, 0.22 * rr);
          c.fillStyle = 'rgba(15,25,90,0.55)'; c.beginPath(); c.ellipse(cx + 0.1 * rr, cy + 0.3 * rr, 0.22 * rr, 0.12 * rr, 0, 0, 6.2832); c.fill();
        }); break;
    }
    if (r * 2 < 14) ring(x);
  }
  function ring(x) { p.noFill(); p.stroke(255, 255, 255, 90); p.strokeWeight(1); p.circle(x, AY, 16); }   // a finder around a body smaller than 14 px

  function probe(x) {                                                    // a pin for Voyager 2: bigger than the probe, which is far below one pixel
    p.noFill(); p.stroke(255, 215, 120, 160); p.strokeWeight(1.5); p.circle(x, AY, 34);
    p.stroke(225, 230, 240); p.strokeWeight(2); p.line(x + 4, AY, x + 15, AY - 6); p.line(x + 4, AY + 2, x + 14, AY + 8);   // booms
    p.fill(210, 160, 80); p.stroke(70, 50, 30); p.strokeWeight(1.2); p.rect(x - 4, AY - 6, 10, 12, 2);                      // bus
    p.fill(240, 243, 250); p.stroke(110, 120, 140); p.strokeWeight(1.2); p.arc(x - 6, AY, 14, 24, -1.5, 1.5, p.CHORD);      // the dish
  }
  function pulse(xa, xb) {                                                // the light pulse and the path it has travelled
    const a = clamp(xa, -40, W + 40), b = clamp(xb, -40, W + 40);
    p.stroke(255, 226, 140, 140); p.strokeWeight(2.5); p.line(a, AY, b, AY);
    if (xb < -30 || xb > W + 30) return;
    const c = p.drawingContext, g = c.createRadialGradient(xb, AY, 0, xb, AY, 14);
    g.addColorStop(0, 'rgba(255,255,255,1)'); g.addColorStop(0.35, 'rgba(255,236,160,0.8)'); g.addColorStop(1, 'rgba(255,220,120,0)');
    c.save(); c.fillStyle = g; c.beginPath(); c.arc(xb, AY, 14, 0, 6.2832); c.fill(); c.restore();
  }

  // a name and size above or below the strip with a thin leader to the body
  function tag(t, fh) {
    const y = t.up ? 100 : 266, onScreen = t.x > 4 && t.x < W - 4;
    if (!t.inside && onScreen) {
      p.stroke(255, 255, 255, 120); p.strokeWeight(1);
      if (t.up) p.line(t.x, AY - t.r - (t.big ? 16 : 6), t.x, y + 6); else p.line(t.x, AY + t.r + 6, t.x, y - fh - 2);
    }
    if (t.x < -60 || t.x > W + 60) return;
    lab(t.text, clamp(t.x, 0, W), t.inside ? 120 : y, 'c', fh);
  }

  // true-scale ruler: a tick every 0,1 Gm = 10^5 km (28,8 px), a number every 1 Gm = 10^6 km
  function ruler(fh) {
    const step = 1e5 / MOON_KM, m0 = Math.max(0, Math.floor((xc - 330) / step)), m1 = Math.ceil((xc + 330) / step);
    p.stroke(190, 205, 235, 150); p.strokeWeight(1); p.line(0, 296, W, 296);
    for (let m = m0; m <= m1; m++) {
      const x = CX + m * step - xc, major = m % 10 === 0;
      p.line(x, 296, x, major ? 306 : 301);
      if (major && x > 64 && x < W - 64) lab(`$${group(m / 10)}\\,\\text{Gm}$`, x, 322, 'c', fh);   // the widest number (100 001 Gm) is about 110 px: keep it whole inside the canvas whatever the font metrics
    }
  }
  function scaleBar(fh) {
    p.stroke(235, 240, 250); p.strokeWeight(2); p.line(16, 24, 116, 24); p.line(16, 19, 16, 29); p.line(116, 19, 116, 29);
    lab(`$100\\,\\text{px} = ${sci(100 * MOON_KM)}\\,\\text{km}$`, 16, 46, 'l', fh);
  }

  // bottom bar: distance from the Sun on a logarithmic scale 10^6 … 10^11 km, with the bodies, Voyager 2, the view and the pulse
  function panel(fh, vz, nView, tripT) {
    const X0 = 58, X1 = 566, RY = 368, X = (e) => X0 + (clamp(e, N_MIN, N_MAX) - N_MIN) / (N_MAX - N_MIN) * (X1 - X0);
    p.noStroke(); p.fill(8, 12, 28, 205); p.rect(8, 330, W - 16, 66, 8);
    p.stroke(200, 210, 230); p.strokeWeight(1.5); p.line(X0, RY, X1, RY);
    for (let e = N_MIN; e <= N_MAX; e++) {
      p.strokeWeight(1.5); p.line(X(e), RY - 5, X(e), RY + 5);
      if (e < N_MAX) for (let m = 2; m <= 9; m++) { p.strokeWeight(1); p.line(X(e + Math.log10(m)), RY, X(e + Math.log10(m)), RY + 3); }
      if (k <= 1.5 || e % 2 === 0) lab(`$10^{${e}}$`, X(e), 391, 'c', fh);   // every second decade on a phone
    }
    lab('$d\\ (\\text{km})$', 14, 350, 'l', fh);
    p.noStroke();
    for (const b of BODIES.slice(1)) { p.fill(...b.col); p.stroke(8, 12, 28); p.strokeWeight(1); p.circle(X(Math.log10(b.a * AU_KM)), RY, 7); }
    lab(`$\\text{${__('maa')}}$`, X(Math.log10(EARTH.a * AU_KM)), 350, 'c', fh);
    const vxp = X(Math.log10(vz.dKm));
    p.fill(255); p.stroke(8, 12, 28); p.strokeWeight(1); p.quad(vxp, RY - 6, vxp + 5, RY, vxp, RY + 6, vxp - 5, RY);
    lab(`$\\text{${__('voyager_2')}}$`, vxp, 350, 'c', fh);
    if (trip.active) {
      const d = (trip.pos * MOON_KM), px = X(d > 1 ? Math.log10(d) : 0), c = p.drawingContext;
      const g = c.createRadialGradient(px, RY, 0, px, RY, 9); g.addColorStop(0, 'rgba(255,255,255,1)'); g.addColorStop(1, 'rgba(255,220,120,0)');
      c.save(); c.fillStyle = g; c.beginPath(); c.arc(px, RY, 9, 0, 6.2832); c.fill(); c.restore();
    }
    const px = X(nView); p.fill(255); p.stroke(8, 12, 28); p.strokeWeight(1); p.triangle(px - 5, 356, px + 5, 356, px, 364);
  }

  // every canvas text: a pill behind it, its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s);
    let x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    x0 = clamp(x0, 4, W - 4 - w);
    const box = { s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size };
    p.noStroke(); p.fill(8, 12, 28, 150); p.rect(box.x0 - 4, box.y0 - 2, w + 8, size + 4, 4);
    p.fill(...(col || [236, 241, 250])); p.text(s, x0, y);
    labels.push(box);
  }
});
