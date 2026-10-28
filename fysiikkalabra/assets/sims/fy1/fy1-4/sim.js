// fy1-4 Suoran sovittaminen: example data points, a straight line the student sets with two sliders, and the deviations.
// Model: the line is y = k x + b. For each data point the vertical deviation is y_i − (k x_i + b); the readout shows the
// root-mean-square deviation d = sqrt(mean of the squares). The student looks for the k and b with the smallest d.
// The checkbox draws the least-squares line of the same data (the line with the smallest possible d) for comparison.
// Three data sets (example data, not real measurements): 1 a cart on a track (line through the origin), 2 a liquid in a
// measuring glass (mass of glass + liquid against volume: the line has a constant term b), 3 a cooling coffee cup
// (a curve: no line fits, and the deviations lie in a pattern).
// Colour carries meaning: blue = data points, orange = the student's line, dashed green = the calculated best line,
// red = deviations. Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9.
new p5((p) => {
  const DS = {
    '1': { xs: [1, 2, 3, 4, 5, 6], ys: [0.6, 0.8, 1.6, 2.1, 2.4, 2.9], xr: [0, 7], yr: [0, 3.5], xt: [1, 2, 3, 4, 5, 6], yt: [1, 2, 3],
           xl: '$t\\ (\\text{s})$', yl: '$s\\ (\\text{m})$', ku: '\\text{m/s}', bu: '\\text{m}', yu: '\\text{m}',
           kr: [0, 1.2, 0.01], br: [-0.5, 1, 0.01], k0: 0.3, b0: 0, dec: 2, ddec: 3 },
    '2': { xs: [20, 40, 60, 80, 100, 120], ys: [78.5, 92.3, 110.9, 124.0, 142.2, 156.1], xr: [0, 140], yr: [0, 200], xt: [20, 40, 60, 80, 100, 120, 140], yt: [50, 100, 150, 200],
           xl: '$V\\ (\\text{ml})$', yl: '$m\\ (\\text{g})$', ku: '\\text{g/ml}', bu: '\\text{g}', yu: '\\text{g}',
           kr: [0, 2, 0.01], br: [0, 150, 0.5], k0: 0.4, b0: 40, dec: 1, ddec: 2 },
    '3': { xs: [0, 5, 10, 15, 20, 25, 30], ys: [90.0, 69.6, 55.3, 45.3, 38.3, 33.4, 30.0], xr: [0, 32], yr: [0, 100], xt: [5, 10, 15, 20, 25, 30], yt: [20, 40, 60, 80, 100],
           xl: '$t\\ (\\text{min})$', yl: '$T\\ ({}^\\circ\\text{C})$', ku: '\\tfrac{{}^\\circ\\text{C}}{\\text{min}}', bu: '{}^\\circ\\text{C}', yu: '{}^\\circ\\text{C}',
           kr: [-3, 1, 0.01], br: [0, 120, 0.5], k0: -1, b0: 80, dec: 1, ddec: 1 },
  };
  const COL = { pt: [25, 113, 194], line: [232, 118, 28], best: [43, 138, 62], dev: [201, 42, 42] };
  const G = { x0: 72, x1: 470, y0: 340, y1: 44 };                        // plot box
  let selData, slK, slB, chkBest, sK, sB, readout, k = 1, labels = [];

  // --- the physics: the line, the deviations and the least-squares line of a data set ---
  const dev = (ds, kk, bb) => ds.xs.map((x, i) => ds.ys[i] - (kk * x + bb));
  const rms = (ds, kk, bb) => Math.sqrt(dev(ds, kk, bb).reduce((s, e) => s + e * e, 0) / ds.xs.length);
  const fit = (ds) => {
    const n = ds.xs.length, mx = ds.xs.reduce((s, v) => s + v, 0) / n, my = ds.ys.reduce((s, v) => s + v, 0) / n;
    let sxy = 0, sxx = 0;
    ds.xs.forEach((x, i) => { sxy += (x - mx) * (ds.ys[i] - my); sxx += (x - mx) * (x - mx); });
    const kk = sxy / sxx; return { k: kk, b: my - kk * mx };
  };
  const GX = (ds, x) => G.x0 + (x - ds.xr[0]) / (ds.xr[1] - ds.xr[0]) * (G.x1 - G.x0);
  const GY = (ds, y) => G.y0 - (y - ds.yr[0]) / (ds.yr[1] - ds.yr[0]) * (G.y0 - G.y1);

  const setRanges = (ds) => {
    for (const [sl, r] of [[slK, ds.kr], [slB, ds.br]]) { sl.elt.min = r[0]; sl.elt.max = r[1]; sl.elt.step = r[2]; }
    slK.value(ds.k0); slB.value(ds.b0);
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const ld = p.createElement('label').parent(controls); p.createSpan(__('aineisto')).parent(ld); selData = p.createSelect().parent(ld);
    selData.option(__('1_karry_radalla'), '1'); selData.option(__('2_neste_mittalasissa'), '2'); selData.option(__('3_kahvin_jaahtuminen'), '3');
    const lk = p.createElement('label').parent(controls); sK = p.createSpan('').parent(lk); slK = p.createSlider(0, 1, 0, 0.01).parent(lk);
    const lb = p.createElement('label').parent(controls); sB = p.createSpan('').parent(lb); slB = p.createSlider(0, 1, 0, 0.01).parent(lb);
    chkBest = p.createCheckbox(__('nayta_laskettu_paras_suora'), false).parent(controls);
    for (const e of [selData.elt]) { const f = () => setRanges(DS[selData.value()]); e.addEventListener('input', f); e.addEventListener('change', f); }
    p.createP(__('pisteet_ovat_esimerkkiaineistoa')).parent('sim-root').class('note');
    p.textFont('Arial');
    setRanges(DS['1']);
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { aineisto: { input: selData.elt, unit: '' }, k: { input: slK.elt, unit: '' }, b: { input: slB.elt, unit: '' } },
      reset: () => { selData.selected('1'); chkBest.checked(false); setRanges(DS['1']); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const ds = DS[selData.value()], kk = Number(slK.value()), bb = Number(slB.value()), best = fit(ds), showBest = chkBest.checked();
    const d = rms(ds, kk, bb), dBest = rms(ds, best.k, best.b);
    sK.html(__('kulmakerroin', { k: tx(kk, 2), ku: ds.ku }));
    sB.html(__('vakiotermi', { b: tx(bb, ds.dec), bu: ds.bu }));
    readout.html(__('poikkeama', { d: tx(d, ds.ddec), yu: ds.yu }) +
      (showBest ? __('paras_suora', { k: tx(best.k, 2), ku: ds.ku, b: tx(best.b, ds.dec), bu: ds.bu, d: tx(dBest, ds.ddec), yu: ds.yu }) : ''));
    window.simState = { aineisto: selData.value(), k: kk, b: bb, d, kBest: best.k, bBest: best.b, dBest, n: ds.xs.length, showBest, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(11);
    labels = [];
    p.background(250);
    plot(ds, kk, bb, best, showBest, fh);
    window.simState.labels = labels;
  };

  function plot(ds, kk, bb, best, showBest, fh) {
    const c = p.drawingContext;
    p.noStroke(); p.fill(255); p.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1);
    p.stroke(228); p.strokeWeight(1);
    for (const t of ds.xt) p.line(GX(ds, t), G.y0, GX(ds, t), G.y1);
    for (const t of ds.yt) p.line(G.x0, GY(ds, t), G.x1, GY(ds, t));
    // the lines are clipped to the plot box
    c.save(); c.beginPath(); c.rect(G.x0, G.y1, G.x1 - G.x0, G.y0 - G.y1); c.clip();
    if (showBest) {
      p.stroke(...COL.best); p.strokeWeight(3); c.setLineDash([9, 6]);
      p.line(GX(ds, ds.xr[0]), GY(ds, best.k * ds.xr[0] + best.b), GX(ds, ds.xr[1]), GY(ds, best.k * ds.xr[1] + best.b)); c.setLineDash([]);
    }
    p.stroke(...COL.line); p.strokeWeight(3.5);
    p.line(GX(ds, ds.xr[0]), GY(ds, kk * ds.xr[0] + bb), GX(ds, ds.xr[1]), GY(ds, kk * ds.xr[1] + bb));
    // the deviations: a vertical segment from each point to the student's line
    p.stroke(...COL.dev, 200); p.strokeWeight(2);
    ds.xs.forEach((x, i) => p.line(GX(ds, x), GY(ds, ds.ys[i]), GX(ds, x), GY(ds, kk * x + bb)));
    c.restore();
    p.fill(...COL.pt); p.stroke(255); p.strokeWeight(2);
    ds.xs.forEach((x, i) => p.circle(GX(ds, x), GY(ds, ds.ys[i]), 12));
    // axes with arrowheads
    p.stroke(60); p.strokeWeight(1.8); p.noFill(); p.line(G.x0, G.y0, G.x1 + 10, G.y0); p.line(G.x0, G.y0, G.x0, G.y1 - 10);
    p.noStroke(); p.fill(60);
    p.triangle(G.x1 + 18, G.y0, G.x1 + 9, G.y0 - 4.5, G.x1 + 9, G.y0 + 4.5); p.triangle(G.x0, G.y1 - 18, G.x0 - 4.5, G.y1 - 9, G.x0 + 4.5, G.y1 - 9);
    for (const t of ds.xt) { p.stroke(60); p.strokeWeight(1.5); p.line(GX(ds, t), G.y0, GX(ds, t), G.y0 + 5); lab(`$${tx(t, 0)}$`, GX(ds, t), G.y0 + 6 + fh, 'c', fh); }
    for (const t of ds.yt) { p.stroke(60); p.strokeWeight(1.5); p.line(G.x0 - 5, GY(ds, t), G.x0, GY(ds, t)); lab(`$${tx(t, 0)}$`, G.x0 - 8, GY(ds, t) + fh * 0.36, 'r', fh); }
    lab('$0$', G.x0 - 8, G.y0 + 6 + fh, 'r', fh);
    lab(ds.xl, G.x1 + 24, G.y0 + fh * 0.36, 'l', fh);
    lab(ds.yl, G.x0 + 12, G.y1 - 12, 'l', fh);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.noStroke(); p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');         // Finnish decimal comma inside LaTeX
});
