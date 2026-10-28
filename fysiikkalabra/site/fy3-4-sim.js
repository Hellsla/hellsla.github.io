// fy3-4 Paine ja hydrostaattinen paine: a pressure gauge sinks into a pool, and a (h, p) chart shows the line.
// Physics: at depth h in a liquid of density ρ the pressure is p = p₀ + ρgh, with p₀ = 101 kPa (air pressure on
// the surface) and g = 9,81 m/s². The term ρgh is the hydrostatic pressure (ylipaine): the weight of the liquid
// column above the gauge divided by its area. The (h, p) graph is a straight line with slope ρg and intercept p₀;
// with "Näytä vain ylipaine" the chart drops the constant term and the line passes through the origin.
// The chart's p axis is scaled to the line shown over 0–20 m at the current density (rounded up to a round
// number) and the scale is printed on the axis. The readout is DOM text; the canvas only draws.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame, and window.simDebug
// with the ink box of every canvas text and the line obstacles, so a test can check that no labels collide.
new p5((p) => {
  const P0 = 101, G = 9.81, H_MAX = 20;                       // air pressure (kPa), g (m/s²), deepest gauge position (m)
  const TANK = { x: 70, w: 160, top: 70, bottom: 370 };       // pool: 20 m over 300 px
  const CH = { x0: 330, x1: 575, y0: 335, y1: 60 };           // chart area (axes at x0 and y0); h-axis title below the ticks
  const LIQUIDS = { 720: __('bensiini'), 1000: __('vesi'), 1025: __('merivesi'), 1240: __('kuolleenmeren_vesi') };
  let sH, lH, sR, lR, cb, readout, k = 1;                     // k: canvas units per screen px for text (set each frame)

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  // round axis maximum: the smallest of 10, 20, 25, 50, 100 kPa steps that needs at most 6 steps
  const niceMax = (v) => { for (const st of [10, 20, 25, 50, 100]) if (Math.ceil(v / st) <= 6) return [Math.ceil(v / st) * st, st]; return [Math.ceil(v / 100) * 100, 100]; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sH, lH] = slider(controls, 0, H_MAX, 10, 0.5);           // syvyys h (m)
    [sR, lR] = slider(controls, 700, 1300, 1000, 5);          // tiheys ρ (kg/m³)
    const lc = p.createElement('label').parent(controls).style('flex-direction', 'row').style('align-items', 'center').style('gap', '.6rem').style('min-height', '40px');
    cb = p.createElement('input').attribute('type', 'checkbox').parent(lc).style('width', '24px').style('height', '24px').style('margin', '0');
    p.createSpan(__('nayta_vain_ylipaine')).parent(lc);
    p.createP(__('jokainen_syvyysmetri_lisaa'))
      .parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { h: { input: sH.elt, unit: 'm' }, rho: { input: sR.elt, unit: 'kg/m³' } },
      reset: () => { sH.value(10); sR.value(1000); cb.elt.checked = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const h = Number(sH.value()), rho = Number(sR.value()), overOnly = cb.elt.checked;
    const slope = rho * G / 1000;                              // ρg in kPa per metre
    const pOver = slope * h;                                   // hydrostatic pressure ρgh (kPa)
    const pTotal = P0 + pOver;                                 // total pressure p₀ + ρgh (kPa)
    const ratio = pTotal / P0;                                 // how many times the air pressure
    const base = overOnly ? 0 : P0;                            // constant term of the line shown in the chart
    const [pMax, step] = niceMax(base + slope * H_MAX);        // chart scale: the line at 20 m, rounded up
    const name = LIQUIDS[rho] ? ` (${LIQUIDS[rho]})` : '';
    lH.html(__(`syvyys`, {h: tx(h, 1)})); lR.html(__(`tiheys`, {rho: rho, name: name}));
    readout.html(__(`syvyys_tiheys`, {h: tx(h, 1), rho: rho}) +
                 __(`hydrostaattinen_paine`, {pover: tx(pOver, 1)}) +
                 __(`kokonaispaine`, {pover: tx(pOver, 1), ptotal: tx(pTotal, 1)}) +
                 __(`kokonaispaine_on_kertaa`, {ratio: tx(ratio, 2)}) +
                 __(`kuvaajan_asteikko_kulmakerroin`, {pmax: pMax, slope: tx(slope, 2)}));
    window.simState = { h, rho, pOver, pTotal, ratio, overOnly, p0: P0, g: G, slope, chartBase: base, chartValue: base + pOver, pMax };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    const boxes = {};                                          // ink box [left, right, top, bottom] of every canvas text
    p.background(250);

    // pool: air above, liquid below (darker for denser liquid), depth scale on the left
    const PXM = (TANK.bottom - TANK.top) / H_MAX, gy = TANK.top + h * PXM, gx = TANK.x + TANK.w / 2;
    p.noStroke(); p.fill(60 - (rho - 700) / 20, 140 - (rho - 700) / 12, 210, 150); p.rect(TANK.x, TANK.top, TANK.w, TANK.bottom - TANK.top);
    p.fill(255, 255, 255, 90); p.rect(gx - 18, TANK.top, 36, gy - TANK.top);           // liquid column above the gauge
    p.stroke(255); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]); p.noFill(); p.rect(gx - 18, TANK.top, 36, gy - TANK.top); p.drawingContext.setLineDash([]);
    p.stroke(60); p.strokeWeight(3); p.line(TANK.x, TANK.top - 30, TANK.x, TANK.bottom); p.line(TANK.x, TANK.bottom, TANK.x + TANK.w, TANK.bottom); p.line(TANK.x + TANK.w, TANK.bottom, TANK.x + TANK.w, TANK.top - 30);
    p.stroke(30, 80, 160); p.strokeWeight(2); p.line(TANK.x, TANK.top, TANK.x + TANK.w, TANK.top);   // surface
    say(boxes, 'air', __('ilma_p_101'), ts(12), 60, 12, TANK.top - 40);
    for (let d = 0; d <= H_MAX; d += 5) { const y = TANK.top + d * PXM; p.stroke(60); p.strokeWeight(1.5); p.line(TANK.x - 6, y, TANK.x, y); say(boxes, `depth${d}`, `$${d}\\,\\text{m}$`, ts(11), 60, TANK.x - 9, y + ts(4), 'r'); }

    // gauge on a cable; arrows from four sides, length grows with the total pressure (pressure acts in every direction)
    p.stroke(80); p.strokeWeight(1.5); p.line(gx, TANK.top - 30, gx, gy - 10);
    const L = 8 + 20 * pTotal / 360;
    p.stroke(200, 40, 40); p.strokeWeight(2.5); p.fill(200, 40, 40);
    for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      const ex = gx + dx * 12, ey = gy + dy * 12, sx = ex + dx * L, sy = ey + dy * L;
      if (sy > TANK.bottom) continue;                          // no arrow through the floor when the gauge rests on it
      p.line(sx, sy, ex + dx * 5, ey + dy * 5);
      p.triangle(ex, ey, ex + dx * 6 - dy * 4, ey + dy * 6 - dx * 4, ex + dx * 6 + dy * 4, ey + dy * 6 + dx * 4);
    }
    p.stroke(40); p.strokeWeight(2); p.fill(240); p.circle(gx, gy, 20);
    // depth bracket on the right of the pool; its "h" only when the bracket is long enough to carry it
    const bx = TANK.x + TANK.w + 12;
    p.stroke(60); p.strokeWeight(1.5); p.line(bx, TANK.top, bx, gy); p.line(bx - 4, TANK.top, bx + 4, TANK.top); p.line(bx - 4, gy, bx + 4, gy);
    if (h >= 2) say(boxes, 'bracket', '$h$', ts(13), 60, bx + 6, (TANK.top + gy) / 2 + ts(5));

    // (h, p) chart scaled to the line shown; p₀ marked as a dashed line when the constant term is included
    const X = (hh) => CH.x0 + (CH.x1 - CH.x0) * hh / H_MAX, Y = (pp) => CH.y0 - (CH.y0 - CH.y1) * pp / pMax;
    const px = X(h), py = Y(base + pOver), y0 = Y(P0);
    const line = [X(0), Y(base), X(H_MAX), Y(base + slope * H_MAX)];
    const rise = (Y(base) - Y(base + slope)) / (X(1) - X(0));  // canvas units the line rises per unit to the right
    p.stroke(225); p.strokeWeight(1);
    for (let v = step; v <= pMax; v += step) p.line(CH.x0, Y(v), CH.x1, Y(v));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    if (!overOnly) { p.stroke(110); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(CH.x0, y0, CH.x1, y0); p.drawingContext.setLineDash([]); }
    p.stroke(30, 80, 160); p.strokeWeight(3); p.line(...line);
    p.stroke(200, 40, 40); p.strokeWeight(1.5); p.drawingContext.setLineDash([4, 4]); p.line(px, py, px, CH.y0); p.line(CH.x0, py, px, py); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(200, 40, 40); p.circle(px, py, 12);

    // axis text; the h-axis title sits under the tick labels, so the vertical guide (it ends at the axis) never reaches it
    for (let v = 0; v <= pMax; v += step) say(boxes, `p${v}`, `$${v}$`, ts(11), 60, CH.x0 - 8, Y(v) + ts(4), 'r');
    for (let d = 0; d <= H_MAX; d += 5) say(boxes, `h${d}`, `$${d}$`, ts(11), 60, X(d), CH.y0 + ts(16), 'c');
    const mt = meas('$h\\ (\\text{m})$', ts(11));
    say(boxes, 'hTitle', '$h\\ (\\text{m})$', ts(11), 60, 596, boxes.h20[3] + 9 + mt.a, 'r');
    say(boxes, 'pTitle', overOnly ? __('ylipaine') : __('paine_p'), ts(12), 60, CH.x0 - 26, CH.y1 - ts(14));

    // labels inside the chart: each takes the first candidate box that lies in the chart area and clears every
    // obstacle (other text, the dashed lines as thin boxes, the dot, the blue line); text gets a halo as well
    const AREA = [CH.x0 + 3, 598, 2, CH.y0 - 3], PAD = 3;
    const hit = (a, b) => a[0] < b[1] + PAD && b[0] < a[1] + PAD && a[2] < b[3] + PAD && b[2] < a[3] + PAD;
    const obstacles = { vGuide: [px - 1, px + 1, py, CH.y0], hGuide: [CH.x0, px, py - 1, py + 1], dot: [px - 6, px + 6, py - 6, py + 6] };
    if (!overOnly) obstacles.p0line = [CH.x0, CH.x1, y0 - 1, y0 + 1];
    const free = (b, skip, extra) => b[0] >= AREA[0] && b[1] <= AREA[1] && b[2] >= AREA[2] && b[3] <= AREA[3] &&
      !segHit(b, line, 2 + PAD) && !Object.entries({ ...boxes, ...obstacles, ...extra }).some(([n, o]) => !skip.includes(n) && hit(b, o));
    // every free candidate box for text t, in order (cands: functions (w, ht) -> box)
    const fits = (t, size, cands, skip, extra = {}) => {
      const m = meas(t, size), w = m.l + m.r, ht = m.a + m.d;
      return cands.map((c, i) => ({ t, size, m, i, b: c(w, ht) })).filter((o) => free(o.b, skip, extra));
    };
    // p₀ label next to the dashed line: below it at the right end, at the left end, then at other spots along it, then
    // above it; the short form "p₀" when the guide lines block every spot of the long one
    let p0Opts = [null];
    if (!overOnly) {
      const xs = [(w) => CH.x1 - w, () => CH.x0 + 10];
      for (let t = 0.25; t < 1; t += 0.25) xs.push((w) => CH.x0 + 10 + t * (CH.x1 - CH.x0 - 10 - w));
      const spots = [...xs.map((fx) => (w, ht) => [fx(w), fx(w) + w, y0 + 4, y0 + 4 + ht]), ...xs.map((fx) => (w, ht) => [fx(w), fx(w) + w, y0 - 4 - ht, y0 - 4])];
      p0Opts = [...fits('$p_0 = 101\\,\\text{kPa}$', ts(11), spots, ['p0line']), ...fits('$p_0$', ts(11), spots, ['p0line'])];
    }
    // gauge reading next to the point: above-left, above-right, below-right, below-left, then to the right under the
    // line's starting level (p₀ or the h axis) far enough right that the rising line clears it, then down the left side
    const g = 10, txt = `$${tx(base + pOver, 0)}\\,\\text{kPa}$`, NEAR = 5;
    const cands = [(w, ht) => [px - g - w, px - g, py - g - ht, py - g], (w, ht) => [px + g, px + g + w, py - g - ht, py - g],
      (w, ht) => [px + g, px + g + w, py + g, py + g + ht], (w, ht) => [px - g - w, px - g, py + g, py + g + ht],
      (w, ht) => { const bot = Math.min(Y(base) + g + ht, CH.y0 - 4), lp = 2 + PAD, x = px + 1 + Math.max(g, lp + (py - bot + ht + lp) / rise); return [x, x + w, bot - ht, bot]; }];
    for (let top = CH.y1; top < CH.y0; top += 8) cands.push((w, ht) => [CH.x0 + 8, CH.x0 + 8 + w, top, top + ht]);
    // the reading has priority: the p₀ label takes the first of its spots that leaves the reading a place next to the point
    const pairs = p0Opts.map((o) => [o, fits(txt, ts(12), cands, [], o ? { p0: o.b } : {})[0]]).filter(([, r]) => r);
    const [p0, rd] = pairs.find(([, r]) => r.i < NEAR) || pairs[0] || [p0Opts[0], null];
    const put = (name, o, col) => say(boxes, name, o.t, o.size, col, o.b[0] + o.m.l, o.b[3] - o.m.d);
    if (p0) put('p0', p0, 90);
    if (rd) put('reading', rd, [200, 40, 40]); else say(boxes, 'reading', txt, ts(12), [200, 40, 40], px + g, py - g);
    const used = { p0: p0 ? p0.i : -1, reading: rd ? rd.i : -1 }, placed = !!rd;    // which candidate each label took (for tests)
    window.simDebug = { boxes, obstacles, line, area: AREA, used, readingPlaced: placed, k };
  };

  // text with a 3-px halo in the background colour (drawn under the fill) and its ink box recorded in boxes[name]
  // ink box of a $…$ label as KaTeX draws it: width from p.textWidth, height estimated from the font size
  // (subscripts and "(" ")" reach below the baseline)
  const meas = (t, size) => {
    p.textSize(size); p.textAlign(p.LEFT, p.BASELINE);
    const w = p.textWidth(t);
    return { w, l: 0, r: w, a: size * 0.8, d: size * (/_|\(/.test(t) ? 0.35 : 0.1) };
  };
  // text at (x, y) and its ink box recorded in boxes[name]; the KaTeX layer has no halo
  const say = (boxes, name, t, size, col, x, y, align = 'l') => {
    const m = meas(t, size), lx = align === 'r' ? x - m.w : align === 'c' ? x - m.w / 2 : x;
    p.push(); p.fill(...[].concat(col)); p.noStroke(); p.text(t, lx, y); p.pop();
    boxes[name] = [lx - m.l, lx + m.r, y - m.a, y + m.d];
  };
  // does the segment [x1, y1, x2, y2] pass through box b grown by pad? (Liang–Barsky clipping)
  const segHit = (b, [x1, y1, x2, y2], pad) => {
    let t0 = 0, t1 = 1; const dx = x2 - x1, dy = y2 - y1;
    for (const [q, r] of [[-dx, x1 - (b[0] - pad)], [dx, b[1] + pad - x1], [-dy, y1 - (b[2] - pad)], [dy, b[3] + pad - y1]]) {
      if (q === 0) { if (r < 0) return false; continue; }
      const t = r / q;
      if (q < 0) { if (t > t1) return false; t0 = Math.max(t0, t); } else { if (t < t0) return false; t1 = Math.min(t1, t); }
    }
    return true;
  };

  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');   // Finnish decimal comma and minus sign
});
