// fy3-1 Voima vuorovaikutuksen mittana: a mass on a spring scale (voimamittari) on different bodies.
// Physics: weight G = m g, with g the acceleration of free fall (m/s²) on the chosen body.
// Mass is the same everywhere; only the weight changes. The spring stretch and the weight arrow are proportional
// to G, and the bar heights are proportional to G at the current mass. The spring and the arrow use one fixed scale whose full value is the
// largest possible weight (100 kg on Jupiter, 2480 N), so they visibly change with the mass slider and with
// the chosen body. The bar chart is scaled to the current mass (full height = m · 24,8 m/s², the Jupiter bar),
// so the four bars always compare the bodies at a readable size; the scale is printed above the chart.
// The stretch and the arrow in simState are the pure proportional values (stretch = G / G_FULL * maxLen,
// arrow = G / G_FULL * ARROW_FULL, no offset); the drawing adds a fixed rest length to the spring, a 2 px
// minimum bar height and a 3 px minimum arrow length, only so that the smallest weights stay visible. The bar chart compares the weight of the same mass on all four bodies.
// Picture: a lab stand on the surface of the chosen body, a steel spring with a newton ruler (N, labelled every 500 N, ticks every 100 N) beside it and a red pointer
// that reads the weight, a steel weight (grey: the mass, same everywhere) and a red weight arrow. Red always means the weight G
// (arrow, pointer, bars); each body has its own colour (ground, planet discs under the bars). When m or the body changes,
// the spring settles to its new stretch with a short damped oscillation (drawing only; simState holds the rest values).
// The numeric readout (m, g, G) is DOM text so it stays readable on a phone; the canvas only draws.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const BODIES = [['Kuu', 1.62], ['Mars', 3.71], ['Maa', 9.81], ['Jupiter', 24.8]];   // g in m/s²
  const LOOK = [                                               // body colours: disc dark/light, ground, ground pattern
    { c: [112, 112, 122], l: [222, 222, 228], gr: [150, 150, 156], dk: [105, 105, 112] },
    { c: [168, 72, 42], l: [238, 150, 100], gr: [178, 92, 58], dk: [130, 58, 36] },
    { c: [32, 96, 168], l: [130, 190, 238], gr: [92, 140, 70], dk: [62, 106, 48] },
    { c: [168, 112, 58], l: [244, 214, 160], gr: [206, 160, 104], dk: [160, 108, 64] }];
  const RED = [200, 40, 40];                                   // the weight G: arrow, pointer and bars
  const SPRING = { x: 124, top: 40, maxLen: 190 };             // spring scale on the left
  const BARS = { x: 270, y: 60, w: 300, h: 250 };              // bar chart on the right
  const RULER = { x: 24, w: 46 }, GROUND = 372, REST = 40;     // newton ruler beside the spring, surface level, unloaded spring length
  const G_MAX = 24.8;                                          // largest g
  const G_FULL = 100 * G_MAX;                                  // full scale: 100 kg on Jupiter = 2480 N
  const ARROW_FULL = 110;                                      // arrow length (px) at full scale; fits the canvas below the block
  const still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let sM, lM, sel, lSel, readout, shown = null, vel = 0, k = 1;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');   // controls first, then the readout
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls);
    lSel = p.createSpan(__('taivaankappale')).parent(l1);
    sel = p.createSelect().parent(l1);
    BODIES.forEach(([name]) => sel.option(name));
    sel.selected('Maa');
    const l2 = p.createElement('label').parent(controls);
    lM = p.createSpan('').parent(l2);
    sM = p.createSlider(1, 100, 10, 1).parent(l2);             // massa m (kg)
    p.createP(__('massa_on_sama'))
      .parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { m: { input: sM.elt, unit: 'kg' }, body: { input: sel.elt, unit: '' } },
      reset: () => { sM.value(10); sel.selected('Maa'); shown = null; vel = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const m = sM.value();
    const idx = Math.max(0, BODIES.findIndex(([name]) => name === sel.value()));
    const [body, g] = BODIES[idx];
    const G = m * g;                                           // weight in newtons
    const stretch = SPRING.maxLen * G / G_FULL;                // spring stretch (px), proportional to the weight G
    lM.html(__(`massa`, {m: m}));
    const chartFull = m * G_MAX;                                // bar chart full scale: this mass on Jupiter
    readout.html(__(`massa_sama_kaikkialla`, {m: m, g: tx(g, 2), body: __v(body)}) +
                 `<br><strong>$G = mg = ${tx(G, 1)}\\,\\text{N}$</strong>` +
                 __(`palkkikaavion_asteikko_on`, {chartfull: tx(chartFull, chartFull < 100 ? 1 : 0)}));
    const arrow = ARROW_FULL * G / G_FULL;                     // weight arrow length (px), purely proportional to G
    const bars = BODIES.map(([, gg]) => (m * gg / chartFull) * (BARS.h - 30));   // bar heights (px), proportional to the weight at this mass
    window.simState = { m, body, g, G, stretch, arrow, bars, chartFull };

    // drawn stretch: a damped spring (ω = 10 1/s, ζ = 0,55) relaxes towards the rest stretch; this only animates the picture
    if (shown === null || still) { shown = stretch; vel = 0; }
    for (let left = Math.min(p.deltaTime || 0, 100) / 1000; left > 0; left -= 1 / 240) {
      const dt = Math.min(left, 1 / 240);
      vel += (-100 * (shown - stretch) - 11 * vel) * dt; shown += vel * dt;
    }
    const disp = Math.max(-REST + 10, Math.min(SPRING.maxLen + 8, shown));

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const L = LOOK[idx];
    p.background(250);
    grad(0, 0, 0, GROUND, [[0, 'rgba(255,255,255,1)'], [1, rgb(L.l, 0.35)]]); p.noStroke(); p.rect(0, 0, 600, GROUND);   // sky tinted by the body
    drawGround(idx);
    drawStand();
    const yS = SPRING.top + REST + disp;                       // lower end of the spring
    drawRuler(yS);
    drawSpring(SPRING.x, SPRING.top, yS - SPRING.top);

    // steel weight: the mass, the same on every body (grey), size grows a little with m
    p.textSize(ts(11)); p.textStyle(p.BOLD);
    const bs = Math.max(36 + 40 * Math.sqrt(m / 100), p.textWidth(`$${m}\\,\\text{kg}$`) + 16), bh = bs * 0.8, e = bs * 0.12;
    const by = yS + 8, bx = SPRING.x - bs / 2;
    p.stroke(70); p.strokeWeight(2); p.noFill(); p.line(SPRING.x, yS, SPRING.x, by - 2); p.arc(SPRING.x, by - 2, 8, 8, p.PI, 0);   // hook
    p.noStroke(); p.fill(0); grad(bx, 0, bx + bs, 0, [[0, '#5d636b'], [0.35, '#e4e7eb'], [0.6, '#b9bec5'], [1, '#4d525a']]);
    p.rect(bx, by + e / 2, bs, bh - e / 2, 0, 0, 4, 4);
    p.fill(0); grad(bx, by, bx + bs, by, [[0, '#9aa0a8'], [0.4, '#f4f6f8'], [1, '#8a9098']]); p.ellipse(SPRING.x, by + e / 2, bs, e);
    p.stroke(60); p.strokeWeight(1.5); p.noFill(); p.rect(bx, by + e / 2, bs, bh - e / 2, 0, 0, 4, 4); p.ellipse(SPRING.x, by + e / 2, bs, e);
    p.noStroke(); p.fill(25); p.textAlign(p.CENTER, p.CENTER); p.text(`$${m}\\,\\text{kg}$`, SPRING.x, by + e / 2 + (bh - e / 2) / 2);
    p.textStyle(p.NORMAL);

    // weight arrow: length proportional to G (3 px floor only for the smallest weights), red like every weight in the picture
    const ax = SPRING.x + bs / 2 + 12, a0 = by + 6, aLen = Math.max(3, arrow), hl = Math.min(14, aLen), hw = Math.max(3, hl / 2);
    p.drawingContext.shadowColor = 'rgba(0,0,0,0.25)'; p.drawingContext.shadowBlur = 4;
    p.fill(...RED); p.noStroke(); p.rect(ax - 2.5, a0, 5, aLen - hl);
    p.triangle(ax, a0 + aLen, ax - hw, a0 + aLen - hl, ax + hw, a0 + aLen - hl);
    p.drawingContext.shadowBlur = 0;
    p.textAlign(p.LEFT, p.CENTER); p.textSize(ts(12)); p.textStyle(p.BOLD); p.text('$G$', ax + 7, a0 + aLen / 2); p.textStyle(p.NORMAL);

    drawChart(idx, m, bars, chartFull);
    drawLegend(idx);
  };

  function drawGround(i) {                                     // surface of the chosen body with a fixed pattern
    const L = LOOK[i];
    grad(0, GROUND, 0, 400, [[0, rgb(L.gr)], [1, rgb(L.dk)]]); p.noStroke(); p.rect(0, GROUND, 600, 400 - GROUND);
    p.fill(...L.dk, 160);
    for (let j = 0; j < 12; j++) {
      const x = 22 + j * 51 + (j % 3) * 9;
      if (i === 0) p.ellipse(x, GROUND + 9 + (j % 2) * 9, 18 - (j % 3) * 4, 5);          // craters
      else if (i === 1) p.ellipse(x, GROUND + 6 + (j % 3) * 6, 7 + (j % 2) * 4, 4);      // rocks
      else if (i === 2) { p.stroke(...L.dk); p.strokeWeight(2); p.line(x, GROUND, x - 3, GROUND - 5); p.line(x + 5, GROUND, x + 7, GROUND - 6); p.noStroke(); }   // grass
      else p.rect(0, GROUND + 4 + j * 6, 600, 2);                                        // cloud bands
    }
  }

  function drawStand() {                                       // lab stand: base, rod, arm and the top hook of the spring
    p.noStroke(); p.fill(0); grad(0, GROUND - 10, 0, GROUND, [[0, '#6b7079'], [1, '#2e3238']]); p.rect(4, GROUND - 10, 70, 10, 3);
    p.fill(0); grad(12, 0, 20, 0, [[0, '#6f757d'], [0.5, '#e3e6ea'], [1, '#5a6068']]); p.rect(12, 14, 8, GROUND - 24);
    p.fill(0); grad(0, 14, 0, 22, [[0, '#e3e6ea'], [1, '#6f757d']]); p.rect(12, 14, SPRING.x - 2, 8, 2);
    p.stroke(70); p.strokeWeight(2.5); p.line(SPRING.x, 22, SPRING.x, SPRING.top);
  }

  function drawRuler(yS) {                                     // newton ruler: 0 at the unloaded spring end, same fixed scale as the stretch
    const y0 = SPRING.top + REST, x1 = RULER.x + RULER.w;
    p.stroke(120); p.strokeWeight(1); p.fill(0); grad(RULER.x, 0, x1, 0, [[0, '#ffffff'], [1, '#e6e8ea']]);
    p.rect(RULER.x, 34, RULER.w, 252, 3);
    p.textSize(ts(9)); p.textAlign(p.RIGHT, p.CENTER);                // numbers right-aligned before the ticks, 2500 fits the ruler
    for (let F = 0; F <= 2500; F += 100) {
      const y = y0 + SPRING.maxLen * F / G_FULL, major = F % 500 === 0;
      p.stroke(60); p.strokeWeight(major ? 1.5 : 1); p.line(x1 - (major ? 10 : 5), y, x1, y);
      if (major) { p.noStroke(); p.fill(40); p.text(`$${F}$`, x1 - 12, y); }
    }
    p.noStroke(); p.fill(40); p.text('$\\text{N}$', x1 - 12, y0 - 1.5 * ts(10));
    p.stroke(...RED); p.strokeWeight(2); p.line(x1 + 6, yS, SPRING.x - 14, yS);   // pointer at the spring end reads the weight
    p.noStroke(); p.fill(...RED); p.triangle(x1 + 1, yS, x1 + 9, yS - 5, x1 + 9, yS + 5);
  }

  function drawSpring(x, y0, len) {                            // helical steel spring: back strands dark, front strands with a highlight
    const n = 12, w = 13, h = len / n;
    p.stroke(80, 84, 92); p.strokeWeight(2);
    for (let i = 0; i < n; i++) p.line(x + w, y0 + (i + 0.5) * h, x - w, y0 + (i + 1) * h);
    for (const [c, wt, dy] of [[[50, 54, 62], 4, 0], [[220, 224, 230], 1.5, -0.8]]) {
      p.stroke(...c); p.strokeWeight(wt);
      for (let i = 0; i < n; i++) p.line(x - w, y0 + i * h + dy, x + w, y0 + (i + 0.5) * h + dy);
    }
    p.stroke(50, 54, 62); p.strokeWeight(3); p.line(x - w, y0 + len, x, y0 + len);
  }

  function drawChart(idx, m, bars, chartFull) {                // bar chart: weight of the same mass on every body, chosen body highlighted
    const base = BARS.y + BARS.h, top = BARS.y + 30, H = BARS.h - 30;
    const raw = chartFull / 6, mag = Math.pow(10, Math.floor(Math.log10(raw)));
    const step = [1, 2, 2.5, 5, 10].map((f) => f * mag).find((s) => s >= raw);       // gridline step, a round number
    p.textSize(ts(10)); p.textAlign(p.RIGHT, p.CENTER);
    for (let v = step; v < 0.8 * chartFull; v += step) {
      const y = base - H * v / chartFull;
      p.stroke(0, 0, 0, 30); p.strokeWeight(1); p.line(BARS.x, y, BARS.x + BARS.w, y);
      p.noStroke(); p.fill(70); p.text(`$${fi(v, 0)}$`, BARS.x - 6, y);
    }
    p.stroke(0, 0, 0, 45); p.line(BARS.x, top, BARS.x + BARS.w, top);                 // full-scale gridline
    p.noStroke(); p.fill(40); p.textStyle(p.BOLD); p.text('$G\\ (\\text{N})$', BARS.x - 6, top + ts(3)); p.textStyle(p.NORMAL);
    p.stroke(60); p.strokeWeight(2); p.line(BARS.x, base, BARS.x + BARS.w, base);
    p.line(BARS.x, base, BARS.x, top); p.line(BARS.x - 5, top, BARS.x + 5, top);   // y axis ends at full scale, with a tick
    const bw = BARS.w / 4 - 16;
    BODIES.forEach(([name, gg], i) => {
      const val = m * gg, h = Math.max(2, bars[i]), x = BARS.x + 12 + i * (bw + 16), on = i === idx;
      const ctx = p.drawingContext;
      if (on) { ctx.shadowColor = 'rgba(200,40,40,0.55)'; ctx.shadowBlur = 10; }
      p.noStroke(); p.fill(0);
      grad(x, 0, x + bw, 0, [[0, rgb(RED, on ? 0.95 : 0.3)], [0.4, rgb([240, 110, 100], on ? 1 : 0.35)], [1, rgb([150, 25, 25], on ? 1 : 0.35)]]);
      p.rect(x, base - h, bw, h, 3, 3, 0, 0); ctx.shadowBlur = 0;
      if (on) { p.stroke(120, 20, 20); p.strokeWeight(2); p.noFill(); p.rect(x, base - h, bw, h, 3, 3, 0, 0); }
      planet(i, x + bw / 2, base + 13, on ? 10 : 8, on);
      p.noStroke(); p.fill(on ? 20 : 70); p.textAlign(p.CENTER, p.BASELINE); p.textSize(ts(12)); p.textStyle(on ? p.BOLD : p.NORMAL);
      p.text(`$\\text{${__v(name)}}$`, x + bw / 2, 336 + 0.75 * ts(12));
      const vt = `$${tx(val, val < 100 ? 1 : 0)}\\,\\text{N}$`;                  // value label, shrunk if it would touch the neighbour's label
      if (p.textWidth(vt) > bw + 12) p.textSize(Math.max(10 * k, ts(12) * (bw + 12) / p.textWidth(vt)));   // never below 10 rendered px
      p.fill(on ? 120 : 70, on ? 20 : 70, on ? 20 : 70); p.text(vt, x + bw / 2, base - h - 6); p.textStyle(p.NORMAL);
    });
    p.noStroke(); p.fill(26, 77, 46); p.textAlign(p.CENTER, p.BASELINE); p.textSize(ts(13));   // title: shrunk to fit inside the canvas when scaled down
    const title = __('sama_massa_paino'), titleMax = 2 * (600 - (BARS.x + BARS.w / 2)) - 10;
    if (p.textWidth(title) > titleMax) p.textSize(ts(13) * titleMax / p.textWidth(title));
    p.text(title, BARS.x + BARS.w / 2, BARS.y - ts(6));
    p.fill(60); p.textSize(ts(11));                               // scale line: short, the explanation is in the readout
    p.textAlign(p.LEFT); p.text(__(`asteikko_0`, {chartfull: tx(chartFull, chartFull < 100 ? 1 : 0)}), BARS.x + 9, top - ts(4));
  }

  function planet(i, x, y, r, on) {                            // small shaded disc of the body, in its own colour
    const L = LOOK[i], ctx = p.drawingContext;
    ctx.save(); ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.clip();
    const g = ctx.createRadialGradient(x - 0.4 * r, y - 0.4 * r, 0.1 * r, x, y, 1.1 * r);
    g.addColorStop(0, rgb(L.l)); g.addColorStop(1, rgb(L.c)); ctx.fillStyle = g; ctx.fillRect(x - r, y - r, 2 * r, 2 * r);
    ctx.fillStyle = i === 2 ? 'rgba(70,150,70,0.85)' : i === 1 ? 'rgba(255,255,255,0.85)' : 'rgba(0,0,0,0.18)';
    if (i === 0) [[-0.3, 0.2, 0.25], [0.35, -0.2, 0.18], [0.1, 0.5, 0.14]].forEach(([u, v, s]) => { ctx.beginPath(); ctx.arc(x + u * r, y + v * r, s * r, 0, 7); ctx.fill(); });
    if (i === 1) { ctx.beginPath(); ctx.ellipse(x, y - 0.92 * r, 0.45 * r, 0.2 * r, 0, 0, 7); ctx.fill(); }
    if (i === 2) [[-0.3, -0.1, 0.35, 0.5], [0.4, 0.3, 0.25, 0.35]].forEach(([u, v, a, b]) => { ctx.beginPath(); ctx.ellipse(x + u * r, y + v * r, a * r, b * r, 0.4, 0, 7); ctx.fill(); });
    if (i === 3) { ctx.fillStyle = 'rgba(140,80,40,0.45)'; [-0.45, -0.05, 0.4].forEach((v) => ctx.fillRect(x - r, y + v * r, 2 * r, 0.18 * r)); }
    ctx.restore();
    p.noFill(); p.stroke(on ? 30 : 120); p.strokeWeight(on ? 2 : 1); p.circle(x, y, 2 * r);
  }

  function drawLegend(idx) {                                   // colour key in a pill on the ground, bottom right
    p.textSize(ts(11)); p.textAlign(p.LEFT, p.CENTER);
    const items = [[__('paino'), RED], [__('massa_2'), [150, 156, 164]], [`$\\text{${BODIES[idx][0]}}$`, null]], y = 386, sw = 16 + 5, gap = 12;
    const w = items.reduce((s, [t]) => s + sw + p.textWidth(t), 0) + gap * (items.length - 1) + 16, h = ts(11) + 8;
    let x = 594 - w + 8;
    p.noStroke(); p.fill(255, 235); p.rect(594 - w, y - h / 2, w, h, 6);
    for (const [t, c] of items) {
      if (c) { p.noStroke(); p.fill(...c); p.rect(x, y - 6, 16, 12, 2); } else planet(idx, x + 8, y, 7, false);
      p.noStroke(); p.fill(40); p.text(t, x + sw, y); x += sw + p.textWidth(t) + gap;
    }
  }

  const ts = (n) => Math.round(n * k);
  const rgb = (c, a = 1) => `rgba(${c[0]},${c[1]},${c[2]},${a})`;
  const grad = (x0, y0, x1, y1, stops) => {                    // linear gradient as the current fill (call after p.fill)
    const g = p.drawingContext.createLinearGradient(x0, y0, x1, y1);
    stops.forEach(([o, c]) => g.addColorStop(o, c)); p.drawingContext.fillStyle = g;
  };
  const fi = (x, d) => x.toFixed(d).replace('.', ',');         // Finnish decimal comma
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');       // the same inside LaTeX
});
