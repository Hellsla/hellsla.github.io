// fy5-6 Gravitaation alainen ympyräliike: a satellite is launched horizontally at the height h above the Earth's
// surface with the speed v and moves under the Earth's gravity alone. The orbit is not drawn from a formula: the motion
// is integrated step by step with velocity Verlet (a = −γM r̄/r³), so a circle appears only when the student finds the
// right speed. Too slow: the path bends more than the circle, dips lower and comes back up (or hits the Earth); too fast:
// it rises higher. The satellite's mass m changes the force F = γMm/r² but not the path. One full revolution takes about
// 6 s at the normal pace whatever the orbit (the time scale is set from the launch state); the readout gives simulated
// time. After one revolution the lowest and highest height and the period T are fixed in the readout and simState
// (hmin, hmax in km, T in min; null until then). Crash: hmin = 0. A path that leaves the view stops the run.
// Picture: the Earth at the centre (to scale with the orbit, at least 7 px), the dashed circle of the launch radius, the
// path, the satellite, its velocity (thin blue arrow, 8 px per km/s) and the gravitational force on it (red arrow,
// 60 px at launch, ∝ 1/r²), a scale bar. Every canvas text goes through lab(), which pushes its box to simState.labels.
// p5.js 1.9 instance mode.
new p5((p) => {
  const GAM = 6.674e-11, M = 5.97e24, RE = 6.371e6, MU = GAM * M;
  const RED = [201, 42, 42], BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const HS = ['400', '2000', '20200', '35786', '378029'], MS = ['1', '1000', '420000'];
  let btn, slV, lV, selH, selM, selSpeed, readout, labels = [], OY = 0, narrow = false, laid = false;
  const OV = { cx: 190, cy: 200, R: 170, w: 380 }, GP = { x: 380, w: 220, h: 400 };   // orbit view and height graph (wide)
  let S = null;                                                        // the run: position, velocity, time, view, measurements

  const fresh = () => {                                                // the satellite at the launch point, not running
    const h = Number(selH.value()) * 1e3, v = Number(slV.value()) * 1e3, r0 = RE + h;
    const eps = v * v / 2 - MU / r0;
    let Test, far;
    if (eps < 0) { const a = -MU / (2 * eps); Test = 2 * Math.PI * Math.sqrt(a ** 3 / MU); far = Math.max(r0, 2 * a - r0); }
    else { Test = 2 * Math.PI * Math.sqrt(r0 ** 3 / MU); far = Infinity; }
    const viewR = Math.min(Math.max(1.15 * far, 1.25 * r0, 1.6 * RE), 8 * r0);
    S = { r0, v0: v, x: 0, y: r0, vx: v, vy: 0, t: 0, Test, viewR, ang: Math.PI / 2, swept: 0, rmin: r0, rmax: r0,
      tila: 'valmis', running: false, done: false, lap: false, hmin: null, hmax: null, T: null, trail: [[0, r0]], hs: [[0, h / 1e3]],
      yMax: niceUp(1.12 * Math.max((Number.isFinite(far) ? far : viewR) - RE, h) / 1e3) };
    const [ax, ay] = acc(0, r0); S.ax = ax; S.ay = ay;
  };
  const acc = (x, y) => { const r2 = x * x + y * y, k = -MU / (r2 * Math.sqrt(r2)); return [k * x, k * y]; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('laukaise')).parent(controls);
    btn.elt.addEventListener('click', () => { if (S.done) { fresh(); S.running = true; S.tila = 'lentaa'; } else { S.running = !S.running; if (S.running) S.tila = S.lap ? 'kiertaa' : 'lentaa'; } });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', fresh);
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(1, 10, 7, 0.01).parent(l1);
    const lh = p.createElement('label').parent(controls); p.createSpan(__('korkeus')).parent(lh); selH = p.createSelect().parent(lh);
    for (const h of HS) selH.option(__('h' + h), h);
    selH.selected('400');
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of MS) selM.option(__('m' + m), m);
    selM.selected('1000');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    for (const e of [slV.elt, selH.elt, selM.elt]) { e.addEventListener('input', fresh); e.addEventListener('change', fresh); }
    controls.style('column-gap', '0.75rem');
    l1.style('flex', '1 1 14rem');
    for (const l of [lh, lm, ls]) l.style('flex', '1 1 7.5rem');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    fresh();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { v: { input: slV.elt, unit: 'km/s' }, h: { input: selH.elt, unit: 'km' }, m: { input: selM.elt, unit: 'kg' } },
      reset: () => { slV.value(7); selH.selected('400'); selM.selected('1000'); fresh(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  // the motion in simulated time: velocity Verlet, sub-steps of 1/1500 of the local circular period
  function advance() {
    if (!S.running) return;
    let left = Math.min(p.deltaTime, 100) / 1000 * S.Test / 6 * Number(selSpeed.value()), guard = 0;
    while (left > 0 && guard++ < 20000) {
      const r = Math.hypot(S.x, S.y), h = Math.min(left, 2 * Math.PI * Math.sqrt(r ** 3 / MU) / 1500); left -= h;
      S.vx += 0.5 * h * S.ax; S.vy += 0.5 * h * S.ay; S.x += h * S.vx; S.y += h * S.vy;
      [S.ax, S.ay] = acc(S.x, S.y); S.vx += 0.5 * h * S.ax; S.vy += 0.5 * h * S.ay; S.t += h;
      const r1 = Math.hypot(S.x, S.y);
      if (r1 <= RE) {                                                  // the surface: stop on it
        const k = RE / r1; S.x *= k; S.y *= k; S.trail.push([S.x, S.y]); S.hs.push([Math.min(360, S.swept * 180 / Math.PI), 0]);
        stop('tormasi'); if (!S.lap) { S.hmin = 0; S.hmax = (S.rmax - RE) / 1e3; } return;
      }
      if (r1 > S.viewR * 1.02) { stop('pois'); if (!S.lap) { S.hmin = (S.rmin - RE) / 1e3; S.hmax = (S.rmax - RE) / 1e3; } return; }
      if (!S.lap) {
        const a2 = Math.atan2(S.y, S.x); let d = a2 - S.ang; d = ((d + Math.PI) % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI) - Math.PI;
        const sw = S.swept + Math.abs(d); S.ang = a2;
        S.rmin = Math.min(S.rmin, r1); S.rmax = Math.max(S.rmax, r1);
        if (sw >= 2 * Math.PI) {                                       // one revolution: fix the measurements
          const f = (2 * Math.PI - S.swept) / (sw - S.swept);
          S.lap = true; S.T = (S.t - h + f * h) / 60; S.hmin = (S.rmin - RE) / 1e3; S.hmax = (S.rmax - RE) / 1e3; S.tila = 'kiertaa';
          S.trail.push([S.x, S.y]);
        } else S.swept = sw;
        const HL = S.hs[S.hs.length - 1], deg = Math.min(360, (S.lap ? 2 * Math.PI : S.swept) * 180 / Math.PI);
        if (S.lap || deg - HL[0] >= 1) S.hs.push([deg, (r1 - RE) / 1e3]);
        const L = S.trail[S.trail.length - 1];
        if (!S.lap && Math.hypot(S.x - L[0], S.y - L[1]) > S.viewR / 300) S.trail.push([S.x, S.y]);
      }
    }
  }
  function stop(tila) { S.running = false; S.done = true; S.tila = tila; }

  const state = (labs) => {
    const r = Math.hypot(S.x, S.y), m = Number(selM.value());
    return { v: Number(slV.value()), h: Number(selH.value()), m, r: r / 1e3, hnyt: (r - RE) / 1e3, F: MU * m / (r * r), g: MU / (r * r),
      vnyt: Math.hypot(S.vx, S.vy) / 1e3, t: S.t / 60, hmin: S.hmin, hmax: S.hmax, T: S.T, tila: S.tila, kierros: S.lap ? 1 : 0,
      running: S.running, done: S.done, viewR: S.viewR / 1e3, labels: labs };
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) { window.simState = state([]); p.redraw(); return; }
    advance();
    const st = state(null);
    lV.html(__('lahtonopeus', { v: tx(st.v, 2) }));
    const bt = S.running ? __('tauko') : (S.t > 0 && !S.done ? __('jatka') : __('laukaise')); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { r: big(st.r), F: fmtF(st.F), g: tx(st.g, st.g < 1 ? 3 : 2), aika: dur(st.t),
      hmin: st.hmin === null ? '–' : '$' + big(st.hmin) + '\\,\\text{km}$', hmax: st.hmax === null ? '–' : '$' + big(st.hmax) + '\\,\\text{km}$',
      T: st.T === null ? '–' : '$' + dur(st.T) + '$', tila: __('tila_' + S.tila) }));
    window.simState = st;
    const U = Math.max(1, k * 0.8), fh = Math.round(13 * k);
    labels = []; OY = 0;
    picture(U, fh);
    if (narrow) { OY = 400; p.push(); p.translate(0, OY); graph(U, fh, 0, 600, 300); p.pop(); }
    else { OY = 0; graph(U, fh, GP.x, GP.w, GP.h); }
    window.simState.labels = labels;
  };

  function setLayout(n) {                                             // a phone: the graph under the orbit, both 600 wide
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    Object.assign(OV, n ? { cx: 300, cy: 200, R: 176, w: 600 } : { cx: 190, cy: 200, R: 170, w: 380 });
    p.resizeCanvas(600, n ? 700 : 400);
    return true;
  }

  function picture(U, fh) {
    const { cx, cy, R, w: W } = OV, sc = R / S.viewR, P = (x, y) => [cx + x * sc, cy - y * sc];
    grect(0, 0, W, 400, [[247, 249, 252], [233, 240, 247]], 0);
    for (let i = 0; i < 60; i++) {                                      // faint fixed stars
      const a = (Math.sin(i * 12.9898) * 43758.5453) % 1, b = (Math.sin(i * 78.233) * 12543.21) % 1;
      p.noStroke(); p.fill(196, 204, 214); p.circle(Math.abs(a) * W, Math.abs(b) * 400, 1.6 + (i % 3) * 0.6);
    }
    // the Earth: oceans, land, a thin atmosphere
    const re = Math.max(7, RE * sc);
    p.noStroke(); p.fill(165, 216, 255, 110); p.circle(cx, cy, 2 * re * 1.08);
    radial(cx, cy, re, [169, 209, 240], [47, 116, 181]);
    if (re > 14) {
      p.fill(233, 201, 138); p.noStroke();
      p.ellipse(cx - re * 0.3, cy - re * 0.25, re * 0.75, re * 0.55); p.ellipse(cx + re * 0.35, cy + re * 0.3, re * 0.5, re * 0.6);
      p.fill(255, 255, 255, 200); p.ellipse(cx, cy - re * 0.82, re * 0.7, re * 0.22);
    }
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5); p.circle(cx, cy, 2 * re);
    // the circle of the launch radius
    p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(1.5 * U); p.drawingContext.setLineDash([6 * U, 6 * U]); p.circle(cx, cy, 2 * S.r0 * sc); p.drawingContext.setLineDash([]);
    // the path so far
    p.stroke(...INKC); p.strokeWeight(2.4 * U); p.noFill(); p.beginShape();
    for (const [x, y] of S.trail) { const [a, b] = P(x, y); p.vertex(a, b); }
    if (!S.lap) { const [a, b] = P(S.x, S.y); p.vertex(a, b); }
    p.endShape();
    // the satellite, its velocity and the gravitational force on it
    const [sx, sy] = P(S.x, S.y), r = Math.hypot(S.x, S.y), ux = -S.x / r, uy = S.y / r;   // screen unit vector to the centre
    const vlen = Math.hypot(S.vx, S.vy), Lv = 8 * U * vlen / 1000, tvx = S.vx / (vlen || 1), tvy = -S.vy / (vlen || 1);
    if (S.tila !== 'tormasi') {
      const LF = Math.max(8, 60 * U * (S.r0 / r) ** 2);
      force(sx + ux * 9 * U, sy + uy * 9 * U, ux * LF, uy * LF);
      lab('$\\overline{F}$', sx + ux * (LF + 9 * U) - tvx * 16 * U, sy + uy * (LF + 9 * U) - tvy * 16 * U + fh * 0.35, 'c', fh, RED);
      thin(sx + tvx * 10 * U, sy + tvy * 10 * U, sx + tvx * (10 * U + Lv), sy + tvy * (10 * U + Lv), BLUE, U);
      lab('$\\overline{v}$', sx + tvx * (Lv + 24 * U) - ux * 12 * U, sy + tvy * (Lv + 24 * U) - uy * 12 * U + fh * 0.35, 'c', fh, BLUE);
    }
    sat(sx, sy, Math.atan2(tvy, tvx), U);
    // time and a scale bar
    lab(`$t = ${dur(S.t / 60)}$`, 10, fh + 6, 'l', fh, INKC);
    const nice = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000], km = nice.find((d) => d * 1e3 * sc > 70) || 200000, w = km * 1e3 * sc;
    const yb = 400 - 14 - fh * 0.8;
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(14, yb, 14 + w, yb); p.line(14, yb - 6, 14, yb + 6); p.line(14 + w, yb - 6, 14 + w, yb + 6);
    lab(`$${big(km)}\\,\\text{km}$`, 14 + w + 8, yb + fh * 0.35, 'l', fh, INKC);
  }
  // the height above the surface against the angle turned round the Earth: a circle is a level line
  function graph(U, fh, X0, W, H) {
    p.noStroke(); p.fill(255); p.rect(X0, 0, W, H);
    p.stroke(220); p.strokeWeight(1); if (narrow) p.line(0, 0, 600, 0); else p.line(X0, 0, X0, H);
    const ym = S.yMax, yt = [0, ym / 2, ym], tl = yt.map((v) => `$${big(v)}$`);
    p.textSize(fh); const tw = Math.max(...tl.map((s) => p.textWidth(s)));
    const x0 = X0 + 12 + tw + 8, x1 = X0 + W - 14 - fh, y0 = H - 18 - fh * 2.4, y1 = fh * 2 + 18;
    const GX = (d) => x0 + d / 360 * (x1 - x0), GY = (h) => y0 - Math.min(h, ym) / ym * (y0 - y1);
    p.stroke(227, 220, 203); p.strokeWeight(1.2);
    for (const d of [90, 180, 270, 360]) p.line(GX(d), y0, GX(d), y1);
    for (const v of yt.slice(1)) p.line(x0, GY(v), x1, GY(v));
    const h0 = (S.r0 - RE) / 1e3;
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * U); p.drawingContext.setLineDash([5 * U, 5 * U]); p.line(x0, GY(h0), x1, GY(h0)); p.drawingContext.setLineDash([]);
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(x0, y0, x1 + 8, y0); p.line(x0, y0, x0, y1 - 8);
    p.stroke(...INKC); p.strokeWeight(2.4 * U); p.noFill(); p.beginShape();
    for (const [d, h] of S.hs) p.vertex(GX(d), GY(h));
    p.endShape();
    if (!S.lap) {
      const r = Math.hypot(S.x, S.y), d = Math.min(360, S.swept * 180 / Math.PI);
      p.noStroke(); p.fill(...INKC); p.circle(GX(d), GY((r - RE) / 1e3), 8 * U);
    }
    yt.forEach((v, i) => lab(tl[i], x0 - 6, GY(v) + fh * 0.35, 'r', fh, INKC));
    for (const d of [90, 180, 270, 360]) lab(`$${d}$`, GX(d), y0 + fh * 1.3, 'c', fh, INKC);
    lab('$h\\ (\\text{km})$', X0 + 12, fh + 6, 'l', fh, INKC);
    lab(__('akseli_kulma'), (x0 + x1) / 2, H - 10, 'c', fh, INKC);
  }
  const niceUp = (x) => { const e = 10 ** Math.floor(Math.log10(x)); return [1, 2, 2.5, 5, 10].map((m) => m * e).find((m) => m >= x); };

  function sat(x, y, a, U) {                                           // a small satellite: body and two solar panels
    p.push(); p.translate(x, y); p.rotate(a);
    p.stroke(...INKC); p.strokeWeight(1.2 * U); p.fill(25, 113, 194, 60);
    p.rect(-3 * U, -15 * U, 6 * U, 9 * U); p.rect(-3 * U, 6 * U, 6 * U, 9 * U);
    p.fill(196, 204, 212); p.rect(-5 * U, -5 * U, 10 * U, 10 * U, 2);
    p.pop();
  }
  function thin(x1, y1, x2, y2, col, U) {                              // velocity: thin, open head
    const a = Math.atan2(y2 - y1, x2 - x1), H = 9 * U;
    p.stroke(...col); p.strokeWeight(2.6 * U); p.noFill(); p.line(x1, y1, x2, y2);
    p.line(x2, y2, x2 - H * Math.cos(a - 0.5), y2 - H * Math.sin(a - 0.5)); p.line(x2, y2, x2 - H * Math.cos(a + 0.5), y2 - H * Math.sin(a + 0.5));
  }
  function force(x, y, dx, dy) {                                       // a force: a solid red arrow with a filled head
    const L = Math.hypot(dx, dy); if (L < 1) return;
    const a = Math.atan2(dy, dx), H = Math.min(12, L * 0.7), x2 = x + dx, y2 = y + dy;
    p.stroke(...RED); p.strokeWeight(3.2); p.line(x, y, x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
  }
  function radial(x, y, r, c1, c2) {
    const c = p.drawingContext; c.save(); const gr = c.createRadialGradient(x - r * 0.35, y - r * 0.35, r * 0.1, x, y, r);
    gr.addColorStop(0, `rgb(${c1.join(',')})`); gr.addColorStop(1, `rgb(${c2.join(',')})`);
    c.fillStyle = gr; c.beginPath(); c.arc(x, y, r, 0, 2 * Math.PI); c.fill(); c.restore();
  }
  function grect(x, y, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.restore();
  }
  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: OY + y - 0.75 * size, x1: x0 + w, y1: OY + y + 0.25 * size });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const big = (x) => { const s = Math.round(x).toString(); return s.length > 4 ? s.replace(/\B(?=(\d{3})+(?!\d))/g, '\\,') : s; };
  const dur = (min) => min < 600 ? tx(min, 1) + '\\,\\text{min}' : min < 4320 ? tx(min / 60, 1) + '\\,\\text{h}' : tx(min / 1440, 1) + '\\,\\text{d}';
  const fmtF = (F) => F >= 1e6 ? tx(F / 1e6, 2) + '\\,\\text{MN}' : F >= 1e3 ? tx(F / 1e3, 2) + '\\,\\text{kN}' : tx(F, F < 1 ? 3 : 2) + '\\,\\text{N}';
});
