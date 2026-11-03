// fy5-12 Aaltojen interferenssi: two in-phase point sources of the same frequency in a ripple tank, seen from above.
// Sources S1, S2 at (−d/2, 0) and (d/2, 0) in cm; each sends a circular wave y_i = A sin(2π(f t − s_i/λ)), A = 1,0 mm,
// with no decay with distance (stated in the lesson's Mallin oletukset); f = v/λ with v = 20 cm/s. The water surface is
// the superposition y1 + y2, drawn as a colour map (light = crest, dark = trough). The point P moves on the line y = L =
// 8,0 cm; the readout gives s1, s2, the path difference Δs = |s1 − s2|, Δs/λ and the amplitude at P, which the sim finds
// by adding the two waves at P over one period (largest |y1 + y2| of 360 samples), so the result emerges from the sum.
// The right (or lower) panel draws y1, y2 and y1 + y2 at P against time. Nodal lines Δs = (n + ½)λ on request.
// Time is slowed: the speed select scales simulated time (hidas 0,05 ×, normaali 0,1 ×, nopea 0,25 ×).
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const L = 8.0, A = 1.0, V = 20.0, NS = 360;
  const BLUE = [47, 116, 181], VIOLET = [112, 72, 232], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], GRID = [227, 220, 203];
  const DARK = [22, 78, 132], LIGHT = [238, 247, 253];
  // geometry: wide 600 x 400 (tank left, signals right); narrow (sim-root < 500 px) 600 x 790, stacked
  const WIDE = { H: 400, fw: 360, fh: 400, sc: 15, ox: 180, oy: 372, cell: 4, gx0: 392, gx1: 566, rows: [86, 186, 308], amp: 24, gy: 0 };
  const NARROW = { H: 790, fw: 600, fh: 400, sc: 25, ox: 300, oy: 380, cell: 5, gx0: 96, gx1: 520, rows: [500, 600, 720], amp: 24, gy: 400 };
  let G = WIDE, narrow = false, sk = 1, fs = 13, labels = [];
  let btn, selSpeed, slD, slL, slX, lD, lL, lX, cbNodal, readout;
  let t = 0, running = true, off = null, offCtx = null, img = null, r1 = null, r2 = null, cacheKey = '';

  const params = () => ({ d: Number(slD.value()), lam: Number(slL.value()), x: Number(slX.value()) });
  const wave = (s, lam, f, tt) => A * Math.sin(2 * Math.PI * (f * tt - s / lam));

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('pysayta')).parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; });
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.05'); selSpeed.option(__('normaali'), '0.1'); selSpeed.option(__('nopea'), '0.25'); selSpeed.selected('0.1');
    const l1 = p.createElement('label').parent(controls); lD = p.createSpan('').parent(l1); slD = p.createSlider(2, 10, 6, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l2); slL = p.createSlider(1, 4, 2, 0.5).parent(l2);
    const l3 = p.createElement('label').parent(controls); lX = p.createSpan('').parent(l3); slX = p.createSlider(-11, 11, 0, 0.1).parent(l3);
    const lk = p.createElement('label').parent(controls); cbNodal = p.createCheckbox('', false).parent(lk); p.createSpan(__('solmuviivat')).parent(lk);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { d: { input: slD.elt, unit: 'cm' }, lam: { input: slL.elt, unit: 'cm' }, x: { input: slX.elt, unit: 'cm' } },
      reset: () => { slD.value(6); slL.value(2); slX.value(0); cbNodal.checked(false); t = 0; running = true; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const P = params(), f = V / P.lam;
    if (running) t += Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    const s1 = Math.hypot(P.x + P.d / 2, L), s2 = Math.hypot(P.x - P.d / 2, L), ds = Math.abs(s1 - s2);
    let AP = 0;                                                        // the amplitude at P from the sum of the two waves
    for (let k = 0; k < NS; k++) { const tt = k / NS / f; AP = Math.max(AP, Math.abs(wave(s1, P.lam, f, tt) + wave(s2, P.lam, f, tt))); }
    lD.html(__('vali', { d: tx(P.d, 1) }));
    lL.html(__('aallonpituus', { l: tx(P.lam, 1) }));
    lX.html(__('paikka', { x: tx(P.x, 1) }));
    const bt = running ? __('pysayta') : __('kaynnista');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { s1: tx(s1, 2), s2: tx(s2, 2), ds: tx(ds, 2), r: tx(ds / P.lam, 2), ap: tx(AP, 1), f: sig2(f) }));
    window.simState = { d: P.d, lam: P.lam, x: P.x, L, A, v: V, f, s1, s2, ds, ratio: ds / P.lam, AP, t, running, nodal: cbNodal.checked(), narrow, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;                                               // strokes grow with the label size on a phone
    fs = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    window.simState.narrow = narrow;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); cacheKey = ''; setTimeout(() => p.redraw(), 0); return; }   // the resize clears the drawing state: draw again next frame
    labels = [];
    p.background(255);
    tank(P, f, s1, s2);
    signals(P, f, s1, s2, AP);
    window.simState.labels = labels;
  };

  // --- the ripple tank from above: the summed surface as a colour map, the sources, the line and P ---
  function tank(P, f, s1, s2) {
    const { fw, fh, sc, ox, oy, cell } = G, cols = Math.ceil(fw / cell), rows = Math.ceil(fh / cell);
    const key = [narrow, P.d].join(',');
    if (key !== cacheKey || !off) {                                    // the distances of every cell from both sources
      cacheKey = key; off = document.createElement('canvas'); off.width = cols; off.height = rows;
      offCtx = off.getContext('2d'); img = offCtx.createImageData(cols, rows);
      r1 = new Float32Array(cols * rows); r2 = new Float32Array(cols * rows);
      for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
        const X = ((i + 0.5) * cell - ox) / sc, Y = (oy - (j + 0.5) * cell) / sc;
        r1[j * cols + i] = Math.hypot(X + P.d / 2, Y); r2[j * cols + i] = Math.hypot(X - P.d / 2, Y);
      }
    }
    const ph = 2 * Math.PI * f * t, kk = 2 * Math.PI / P.lam, D = img.data;
    for (let q = 0; q < cols * rows; q++) {
      const u = (Math.sin(ph - kk * r1[q]) + Math.sin(ph - kk * r2[q]) + 2) / 4;
      D[4 * q] = DARK[0] + (LIGHT[0] - DARK[0]) * u; D[4 * q + 1] = DARK[1] + (LIGHT[1] - DARK[1]) * u;
      D[4 * q + 2] = DARK[2] + (LIGHT[2] - DARK[2]) * u; D[4 * q + 3] = 255;
    }
    offCtx.putImageData(img, 0, 0);
    const c = p.drawingContext; c.save(); c.imageSmoothingEnabled = true; c.drawImage(off, 0, 0, cols * cell, rows * cell); c.restore();
    const X = (x) => ox + x * sc, Y = (y) => oy - y * sc;
    // nodal lines Δs = (n + ½)λ: hyperbolas with the sources as foci
    if (cbNodal.checked()) {
      c.save(); c.beginPath(); c.rect(0, 0, fw, fh); c.clip();
      p.noFill(); p.stroke(255, 255, 255); p.strokeWeight(2 * sk); p.drawingContext.setLineDash([7 * sk, 5 * sk]);
      for (let n = 0; (n + 0.5) * P.lam < P.d; n++) {
        const a = (n + 0.5) * P.lam / 2, cc = P.d / 2, b = Math.sqrt(cc * cc - a * a);
        for (const sgn of [-1, 1]) {
          p.beginShape();
          for (let y = (oy - fh) / sc - 1; y <= oy / sc + 1; y += 0.2) p.vertex(X(sgn * a * Math.sqrt(1 + y * y / (b * b))), Y(y));
          p.endShape();
        }
      }
      p.drawingContext.setLineDash([]); c.restore();
    }
    // the measurement line y = L and the paths S1 -> P, S2 -> P
    p.stroke(255); p.strokeWeight(2 * sk); p.drawingContext.setLineDash([9 * sk, 7 * sk]); p.line(6, Y(L), fw - 6, Y(L)); p.drawingContext.setLineDash([]);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    p.line(X(-P.d / 2), Y(0), X(P.x), Y(L)); p.line(X(P.d / 2), Y(0), X(P.x), Y(L));
    // the sources: dippers touching the water
    for (const xs of [-P.d / 2, P.d / 2]) { p.fill(...INKC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(X(xs), Y(0), 12 * sk); }
    // P
    p.fill(255); p.stroke(...INKC); p.strokeWeight(3 * sk); p.circle(X(P.x), Y(L), 16 * sk);
    lab(__('lbl_s1'), X(-P.d / 2) - 10 * sk, Y(0) + fs * 0.35, 'r', INKC, true);
    lab(__('lbl_s2'), X(P.d / 2) + 10 * sk, Y(0) + fs * 0.35, 'l', INKC, true);
    lab(__('lbl_p'), X(P.x) + 12 * sk, Y(L) - 12 * sk, 'l', INKC, true);
    lab(__('lbl_ds1'), (X(-P.d / 2) + X(P.x)) / 2 - 8 * sk, (Y(0) + Y(L)) / 2, 'r', INKC, true);
    lab(__('lbl_ds2'), (X(P.d / 2) + X(P.x)) / 2 + 8 * sk, (Y(0) + Y(L)) / 2, 'l', INKC, true);
    lab(__('lbl_line'), 10, Y(L) + 18 * sk, 'l', INKC, true);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, G.gy, 600, G.gy); else p.line(fw, 0, fw, 400);
  }

  // --- the two waves and their sum at P against time (the last two periods, now at the right end) ---
  function signals(P, f, s1, s2, AP) {
    const { gx0, gx1, rows, amp } = G, T = 1 / f, win = 2 * T;
    const X = (tt) => gx0 + (tt - (t - win)) / win * (gx1 - gx0);
    const traces = [[rows[0], 1, (tt) => wave(s1, P.lam, f, tt), BLUE, __('lbl_y1')],
                    [rows[1], 1, (tt) => wave(s2, P.lam, f, tt), VIOLET, __('lbl_y2')],
                    [rows[2], 2, (tt) => wave(s1, P.lam, f, tt) + wave(s2, P.lam, f, tt), INKC, __('lbl_sum')]];
    lab(__('lbl_otsikko'), (gx0 + gx1) / 2, rows[0] - 2 * amp - 14 * sk, 'c', INKC);
    for (const [yc, span, fn, col, name] of traces) {
      const top = yc - span * amp - 4 * sk, bot = yc + span * amp + 4 * sk;
      p.stroke(...GRID); p.strokeWeight(1.5);
      for (const v of [-2, -1, 1, 2]) if (Math.abs(v) <= span) p.line(gx0, yc - v * amp, gx1, yc - v * amp);
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(gx0, bot, gx0, top - 8 * sk); p.line(gx0, yc, gx1 + 8 * sk, yc);
      p.noStroke(); p.fill(...INKC);
      p.triangle(gx1 + 18 * sk, yc, gx1 + 6 * sk, yc - 5 * sk, gx1 + 6 * sk, yc + 5 * sk);
      p.triangle(gx0, top - 18 * sk, gx0 - 5 * sk, top - 6 * sk, gx0 + 5 * sk, top - 6 * sk);
      p.noFill(); p.stroke(...col); p.strokeWeight(3 * sk); p.beginShape();
      for (let j = 0; j <= 160; j++) { const tt = t - win + win * j / 160; p.vertex(X(tt), yc - fn(tt) * amp); }
      p.endShape();
      p.noStroke(); p.fill(...col); p.circle(gx1, yc - fn(t) * amp, 9 * sk);
      lab(name, gx0 + 12 * sk, top - 6 * sk, 'l', col);
      lab(__('lbl_t'), gx1 + 22 * sk, yc + fs * 0.35, 'l', INKC);
    }
    // the sum's amplitude, read off as dashed guides
    if (AP > 0.05) {
      p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([6 * sk, 5 * sk]);
      p.line(gx0, rows[2] - AP * amp, gx1, rows[2] - AP * amp); p.line(gx0, rows[2] + AP * amp, gx1, rows[2] + AP * amp);
      p.drawingContext.setLineDash([]);
      if (AP > 0.3) lab(__('lbl_ap'), gx1 - 6 * sk, rows[2] - AP * amp - 8 * sk, 'r', INKC, true);
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates); bg puts a white box under it
  function lab(s, x, y, align, col, bg) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fs);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);                 // never past the canvas edge
    y = Math.min(Math.max(y, 0.8 * fs), G.H - 0.3 * fs);
    if (bg) { p.noStroke(); p.fill(255, 255, 255, 225); p.rect(x0 - 3, y - 0.85 * fs, w + 6, 1.15 * fs, 3); }
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fs, x1: x0 + w, y1: y + 0.25 * fs });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sig2 = (x) => tx(x, Math.max(0, 1 - Math.floor(Math.log10(Math.abs(x)) + 1e-9)));
});
