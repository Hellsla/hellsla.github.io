// fy8-14 Säteily lääketieteessä ja teknologiassa: how a PET scanner locates a tracer. A cross-section of a patient
// lies inside a ring of 48 detectors (ring radius 34 cm). The tracer (fluorine-18) is spread evenly in the body, and in
// the cases with a tumour a share of the annihilations comes from a small region (Gaussian, sigma 0,8 cm): 25 % from
// one tumour, or 20 % from each of two. Every annihilation sends two 511 keV photons in opposite directions along a
// random direction; in the coincidence mode the two detectors they hit define a line of response (LOR), and the image
// is built by back-projection: every pixel (41 x 41, 1 cm) whose centre lies within 0,6 cm of a line gets one count.
// The brightest pixel, its distance from the tumour and the share of lines passing within 1,0 cm of the tumour are
// read out. In the singles mode only one detector of each pair is recorded, so no line and no image arise.
// Model: no attenuation or scatter in the body, no random coincidences, no positron range, photons exactly opposite,
// a flat 2D ring that detects every pair. The events come from a seeded generator (seed 73 + 1000 case), so N events
// are always the same N; the slider N chooses how many have been collected, Käynnistä collects more.
// lessons/FY8/fy8-14/lesson-answers.py repeats the same model. Every canvas text goes through lab(). p5.js 1.9 instance mode.
new p5((p) => {
  const RR = 34, AB = 16, BB = 10.5, G = 41, HALF = 0.6, SIG = 0.8, ND = 48, NMAX = 2000;
  const TUM = { '1': [[5, -3]], '2': [[5, -3], [-7, 2]], '0': [] }, PT = { '1': 0.25, '2': 0.4, '0': 0 };
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], PAPER = [246, 241, 230], SKIN = [242, 166, 156], LUNG = [253, 226, 222], BONE = [241, 223, 181],
        ALU = [196, 204, 212], IRONC = [108, 117, 125], GLASSC = [238, 245, 249];
  const CX = 190, CY = 192, K = 4.8;                    // ring centre (px), px per cm
  const IX = 406, IY = 44, IC = 4.4;                    // image panel: left, top, px per pixel
  let sk = 1, fh = 13, labels = [];
  let btnRun, slN, selCase, selMode, selSpeed, lN, readout;
  let N = 0, running = false, acc = 0, ev = [], evCase = null, img = new Array(G * G).fill(0), imgN = 0, hits = new Array(ND).fill(0);
  let flights = [], pg = null, pgDirty = true;

  // the seeded generator (the same as lesson-answers.py): events of one case are always the same sequence
  function makeEvents(c) {
    let seed = 73 + 1000 * Number(c);
    const rand = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
    const T = TUM[c], out = [];
    for (let k = 0; k < NMAX; k++) {
      let x, y;
      if (T.length && rand() < PT[c]) {
        const t = T[Math.floor(rand() * T.length) % T.length];
        const u1 = Math.max(rand(), 1e-12), u2 = rand(), r = SIG * Math.sqrt(-2 * Math.log(u1));
        x = t[0] + r * Math.cos(2 * Math.PI * u2); y = t[1] + r * Math.sin(2 * Math.PI * u2);
      } else {
        do { x = (2 * rand() - 1) * AB; y = (2 * rand() - 1) * BB; } while ((x / AB) ** 2 + (y / BB) ** 2 > 1);
      }
      const th = rand() * Math.PI, ux = Math.cos(th), uy = Math.sin(th);
      const b = x * ux + y * uy, s = Math.sqrt(b * b - (x * x + y * y - RR * RR));
      const d1 = det(x + (-b + s) * ux, y + (-b + s) * uy), d2 = det(x + (-b - s) * ux, y + (-b - s) * uy);
      out.push({ x, y, ux, uy, s1: -b + s, s2: -b - s, d1, d2, one: rand() < 0.5 ? d1 : d2 });
    }
    return out;
  }
  function det(x, y) { return Math.floor((((Math.atan2(y, x) + 2 * Math.PI) % (2 * Math.PI)) / (2 * Math.PI)) * ND) % ND; }
  function addLine(e, sgn) {
    for (let j = 0; j < G; j++) { const cy = -20 + j;
      for (let i = 0; i < G; i++) { const cx = -20 + i;
        if (Math.abs((cx - e.x) * e.uy - (cy - e.y) * e.ux) < HALF) img[j * G + i] += sgn; } }
  }
  // bring the image and the detector counts to the first n events of the current case
  function sync(n) {
    const c = selCase.value();
    if (evCase !== c) { ev = makeEvents(c); evCase = c; img.fill(0); hits.fill(0); imgN = 0; flights = []; }
    if (n < imgN) { img.fill(0); hits.fill(0); imgN = 0; }
    for (let k = imgN; k < n; k++) { addLine(ev[k], 1); hits[ev[k].one]++; }
    if (n !== imgN) pgDirty = true;
    imgN = n;
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnRun = p.createButton(__('kaynnista')).parent(controls);
    btnRun.elt.addEventListener('click', () => { if (running) running = false; else { if (N >= NMAX) { N = 0; slN.value(0); } running = true; } });
    const l1 = p.createElement('label').parent(controls); lN = p.createSpan('').parent(l1); slN = p.createSlider(0, NMAX, 0, 10).parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('kohde')).parent(l2); selCase = p.createSelect().parent(l2);
    selCase.option(__('kohde_1'), '1'); selCase.option(__('kohde_2'), '2'); selCase.option(__('kohde_0'), '0'); selCase.selected('1');
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('ilmaisu')).parent(l3); selMode = p.createSelect().parent(l3);
    selMode.option(__('ilmaisu_1'), '1'); selMode.option(__('ilmaisu_0'), '0'); selMode.selected('1');
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l4); selSpeed = p.createSelect().parent(l4);
    selSpeed.option(__('hidas'), '2'); selSpeed.option(__('normaali'), '10'); selSpeed.option(__('nopea'), '50'); selSpeed.selected('10');
    for (const evn of ['input', 'change']) slN.elt.addEventListener(evn, () => { N = Number(slN.value()); running = false; flights = []; });
    for (const s of [selCase, selMode]) s.elt.addEventListener('change', () => { flights = []; pgDirty = true; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    pg = p.createGraphics(G, G); pg.pixelDensity(1);
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { N: { input: slN.elt, unit: '' }, kohde: { input: selCase.elt, unit: '' }, ilmaisu: { input: selMode.elt, unit: '' } },
      reset: () => { N = 0; slN.value(0); selCase.selected('1'); selMode.selected('1'); running = false; flights = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const dt = Math.min(p.deltaTime, 100) / 1000, rate = Number(selSpeed.value()), coin = selMode.value() === '1';
    if (running) {
      acc += dt * rate;
      while (acc >= 1 && N < NMAX) { acc -= 1; flights.push({ k: N, age: 0 }); N++; }
      if (N >= NMAX) running = false;
      slN.value(N);
    } else acc = 0;
    sync(N);
    const c = selCase.value(), T = TUM[c];
    // the brightest pixel, its distance from the nearest tumour, the share of lines within 1 cm of the first tumour
    let m = 0, km = 0;
    for (let k = 0; k < G * G; k++) if (img[k] > m) { m = img[k]; km = k; }
    const xs = -20 + (km % G), ys = -20 + Math.floor(km / G);
    const ok = coin && N > 0;
    let err = -1, share = 0;
    if (ok && T.length) {
      err = Math.min(...T.map((t) => Math.hypot(xs - t[0], ys - t[1])));
      let nk = 0; for (let k = 0; k < N; k++) { const e = ev[k]; if (Math.abs((T[0][0] - e.x) * e.uy - (T[0][1] - e.y) * e.ux) < 1.0) nk++; }
      share = 100 * nk / N;
    }
    btnRun.html(running ? __('pysayta') : __('kaynnista'));
    lN.html(__('lkm', { n: String(N) }));
    if (!coin) readout.html(__('lukemat_yks', { n: String(N) }));
    else if (N === 0) readout.html(__('lukemat_0'));
    else if (!T.length) readout.html(__('lukemat_ei', { n: String(N), x: tx(xs), y: tx(-ys) }));
    else readout.html(__('lukemat', { n: String(N), x: tx(xs), y: tx(-ys), e: tx1(err), o: String(Math.round(share)) }));
    window.simState = { N, kohde: Number(c), ilmaisu: coin ? 1 : 0, xmax: ok ? xs : 0, ymax: ok ? -ys : 0, virhe: err,
                        osuus: share, running: running ? 1 : 0, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const kk = Math.max(1, 600 / cw);
    sk = cw < 500 ? kk : 1; fh = cw < 500 ? Math.round(14 * kk) : 15;
    labels = [];
    p.background(...PAPER);
    scanner(coin);
    lines(coin);
    photons(dt, coin);
    picture(coin, m);
    window.simState.labels = labels;
  };

  const PX = (x) => CX + x * K, PY = (y) => CY + y * K;

  // --- the gantry: the detector ring, the bed and the patient's cross-section (the tumour is not drawn) ---
  function scanner(coin) {
    p.noStroke(); p.fill(...ALU); p.circle(CX, CY, 2 * (RR * K + 16));
    p.fill(...GLASSC); p.circle(CX, CY, 2 * (RR * K - 4));
    const hmax = Math.max(1, ...hits);
    for (let d = 0; d < ND; d++) {
      const a0 = (d / ND) * 2 * Math.PI, a1 = ((d + 1) / ND) * 2 * Math.PI;
      const fl = flights.some((f) => f.age >= 0.32 && f.age < 0.6 && (coin ? (ev[f.k].d1 === d || ev[f.k].d2 === d) : ev[f.k].one === d));
      const lvl = coin ? 0 : hits[d] / hmax;
      const col = fl ? HEATC : [IRONC[0] + (HEATC[0] - IRONC[0]) * lvl, IRONC[1] + (HEATC[1] - IRONC[1]) * lvl, IRONC[2] + (HEATC[2] - IRONC[2]) * lvl];
      p.fill(...col); p.stroke(...INKC); p.strokeWeight(1.5);
      p.beginShape();
      for (const [a, r] of [[a0 + 0.01, RR * K], [a1 - 0.01, RR * K], [a1 - 0.01, RR * K + 12], [a0 + 0.01, RR * K + 12]]) p.vertex(CX + r * Math.cos(a), CY + r * Math.sin(a));
      p.endShape(p.CLOSE);
    }
    // bed and body
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...RULEC); p.rect(PX(-19), PY(11), 38 * K, 3 * K, 4);
    p.strokeWeight(2.5); p.fill(...SKIN); p.ellipse(CX, CY, 2 * AB * K, 2 * BB * K);
    p.strokeWeight(1.5); p.fill(...LUNG); p.ellipse(PX(-6.5), PY(-1.5), 9 * K, 12 * K); p.ellipse(PX(6.5), PY(-1.5), 9 * K, 12 * K);
    p.fill(...BONE); p.circle(PX(0), PY(6.8), 4.4 * K); p.fill(...SKIN); p.circle(PX(0), PY(6.8), 1.6 * K);
    p.fill(...BONE); p.ellipse(PX(0), PY(-7.5), 4 * K, 2.4 * K);
  }

  // --- lines of response: the last 120 recorded pairs, the newest brightest ---
  function lines(coin) {
    if (!coin) return;
    const k0 = Math.max(0, N - 120);
    p.strokeWeight(1.2);
    for (let k = k0; k < N; k++) {
      if (flights.some((f) => f.k === k && f.age < 0.32)) continue;
      const e = ev[k], a = 40 + 150 * Math.max(0, 1 - (N - 1 - k) / 12);
      p.stroke(HEATC[0], HEATC[1], HEATC[2], a);
      p.line(PX(e.x + e.s1 * e.ux), PY(e.y + e.s1 * e.uy), PX(e.x + e.s2 * e.ux), PY(e.y + e.s2 * e.uy));
    }
  }

  // --- photons in flight: two from each annihilation point in opposite directions (a picture of the model) ---
  function photons(dt, coin) {
    const keep = [];
    p.noStroke();
    for (const f of flights) {
      f.age += dt;
      if (f.age > 0.6) continue;
      keep.push(f);
      const e = ev[f.k];
      if (f.age < 0.08) { p.fill(255, 255, 255, 230); p.circle(PX(e.x), PY(e.y), 14 * (1 - f.age / 0.08) + 4); }
      if (f.age < 0.32) {
        const q = f.age / 0.32;
        for (const [s, d] of [[e.s1, e.d1], [e.s2, e.d2]]) {
          if (!coin && d !== e.one && q > 0.9) continue;
          const x = e.x + s * q * e.ux, y = e.y + s * q * e.uy;
          p.fill(HEATL[0], HEATL[1], HEATL[2], 170); p.circle(PX(x - 1.2 * Math.sign(s) * e.ux), PY(y - 1.2 * Math.sign(s) * e.uy), 8);
          p.fill(...HEATC); p.circle(PX(x), PY(y), 7);
        }
      }
    }
    flights = keep.slice(-200);
    lab('$\\gamma\\!:\\ 511\\,\\text{keV}$', 14, 392, 'l', HEATC);
  }

  // --- the reconstructed image (back-projection), with its axes in cm ---
  function picture(coin, m) {
    if (pgDirty) {
      pg.loadPixels();
      for (let k = 0; k < G * G; k++) {
        const v = coin && m > 0 ? img[k] / m : 0, c = ramp(v);
        const i = 4 * k; pg.pixels[i] = c[0]; pg.pixels[i + 1] = c[1]; pg.pixels[i + 2] = c[2]; pg.pixels[i + 3] = 255;
      }
      pg.updatePixels(); pgDirty = false;
    }
    p.noSmooth(); p.image(pg, IX, IY, G * IC, G * IC); p.smooth();
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2); p.rect(IX, IY, G * IC, G * IC);
    const XI = (x) => IX + (x + 20.5) * IC, YI = (y) => IY + (20.5 - y) * IC;      // y up in the image
    p.stroke(...INKC); p.strokeWeight(1.5);
    for (const v of [-15, 0, 15]) {
      p.line(XI(v), IY + G * IC, XI(v), IY + G * IC + 6 * sk); p.line(IX, YI(v), IX - 6 * sk, YI(v));
      lab('$' + (v < 0 ? '-' : '') + String(Math.abs(v)) + '$', XI(v), IY + G * IC + 6 * sk + 1.1 * fh, 'c', INKC);
      lab('$' + (v < 0 ? '-' : '') + String(Math.abs(v)) + '$', IX - 9 * sk, YI(v) + 0.35 * fh, 'r', INKC);
    }
    lab('$x\\ (\\text{cm})$', IX + G * IC, IY + G * IC + 6 * sk + 2.4 * fh, 'r', INKC);
    lab('$y\\ (\\text{cm})$', IX - 4, IY - 0.55 * fh, 'l', INKC);
    if (!coin) lab(__('ei_kuvaa_kanvas'), IX + G * IC / 2, IY + G * IC / 2 + 0.35 * fh, 'c', PAPER);
    lab('$N = ' + String(N) + '$', IX + G * IC / 2, IY + G * IC + 6 * sk + 3.9 * fh, 'c', HEATC);
  }
  function ramp(v) {                                   // ink -> heat -> light heat -> white
    const st = [[0, INKC], [0.45, HEATC], [0.8, HEATL], [1, [255, 255, 255]]];
    for (let i = 1; i < st.length; i++) if (v <= st[i][0]) {
      const a = st[i - 1], b = st[i], q = (v - a[0]) / (b[0] - a[0]);
      return [0, 1, 2].map((j) => Math.round(a[1][j] + (b[1][j] - a[1][j]) * q));
    }
    return [255, 255, 255];
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
  const tx = (v) => (v < 0 ? '-' : '') + String(Math.abs(Math.round(v)));
  const tx1 = (v) => v.toFixed(1).replace('.', DEC);
});
