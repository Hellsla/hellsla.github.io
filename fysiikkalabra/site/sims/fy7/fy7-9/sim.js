// fy7-9 Sähkömagneettinen säteily ja mustan kappaleen spektri: the spectrum of a black body at the temperature T.
// Model: the curve is the spectral exitance M_λ(λ, T) = 2πhc² / λ⁵ / (exp(hc / (λ k T)) − 1) (Planck's law, exact SI
// constants); λ_max is found as the curve's highest point by a golden-section search, not from Wien's law, so the
// student can find λ_max T = constant from the model values. The share of the power in visible light (380–750 nm) is
// the integral of M_λ over that band divided by σT⁴. The glow colour comes from the curve through the CIE 1931
// colour-matching functions (the multi-lobe fit of Wyman, Sloan & Shirley 2013) and sRGB; its brightness grows with
// the luminance (no glow below 800 K). The picture: the hot body on the left (above on a narrow screen), the
// curve on the right with the visible band in colour and the peak marked; the vertical scale follows the curve.
// Static: drawn again on every frame, no animation. Every canvas text goes through lab() (simState.labels).
new p5((p) => {
  const H = 6.62607015e-34, C = 2.99792458e8, KB = 1.380649e-23, SIGMA = 5.670374419e-8;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEL = [227, 220, 203], HEATC = [232, 89, 12], HEATL = [255, 192, 120];
  const IRONC = [108, 117, 125], METAL = [138, 150, 163], SANDL = [241, 223, 181];
  const RANGES = { lyhyt: { max: 3000, step: 500, unit: 'nm', f: 1 }, pitka: { max: 30000, step: 5000, unit: '\\mu\\text{m}', f: 1e-3 } };
  let slT, selA, lT, readout, labels = [], cache = {};

  const M = (lam, T) => { const x = H * C / (lam * KB * T); return x > 700 ? 0 : 2 * Math.PI * H * C * C / Math.pow(lam, 5) / Math.expm1(x); };
  const peak = (T) => {                                    // golden-section search for the curve's highest point
    let lo = 50e-9, hi = 50e-6; const g = (Math.sqrt(5) - 1) / 2;
    for (let i = 0; i < 120; i++) { const a1 = hi - g * (hi - lo), a2 = lo + g * (hi - lo); if (M(a1, T) > M(a2, T)) hi = a2; else lo = a1; }
    return (lo + hi) / 2;
  };
  const gl = (x, mu, s1, s2) => { const t = (x - mu) / (x < mu ? s1 : s2); return Math.exp(-0.5 * t * t); };
  const cmf = (l) => [1.056 * gl(l, 599.8, 37.9, 31.0) + 0.362 * gl(l, 442.0, 16.0, 26.7) - 0.065 * gl(l, 501.1, 20.4, 26.2),
    0.821 * gl(l, 568.8, 46.9, 40.5) + 0.286 * gl(l, 530.9, 16.3, 31.1),
    1.217 * gl(l, 437.0, 11.8, 36.0) + 0.681 * gl(l, 459.0, 26.0, 13.8)];
  let LUM = null;
  const lum = (T) => { let yy = 0; for (let i = 0; i < 740; i++) { const l = 380 + (i + 0.5) * 0.5; yy += M(l * 1e-9, T) * cmf(l)[1]; } return yy * 0.5; };
  function model(T) {
    if (cache.T === T) return cache;
    const lm = peak(T);
    let vis = 0, X = 0, Y = 0, Z = 0; const n = 740, d = (750 - 380) / n;
    for (let i = 0; i < n; i++) {
      const l = 380 + (i + 0.5) * d, m = M(l * 1e-9, T), c = cmf(l);
      vis += m * d * 1e-9; X += m * c[0]; Y += m * c[1]; Z += m * c[2];
    }
    const s = X + Y + Z || 1, x = X / s, y = Y / s;      // chromaticity, then sRGB at full brightness
    const Xn = x / y, Zn = (1 - x - y) / y;
    let rgb = [3.2406 * Xn - 1.5372 - 0.4986 * Zn, -0.9689 * Xn + 1.8758 + 0.0415 * Zn, 0.0557 * Xn - 0.2040 + 1.0570 * Zn].map((v) => Math.max(0, v));
    const mx = Math.max(...rgb) || 1;
    rgb = rgb.map((v) => { v /= mx; return 255 * (v <= 0.0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - 0.055); });
    if (!LUM) LUM = [lum(800), lum(1700)].map(Math.log10);  // the glow starts at 800 K and is full at 1700 K
    const glow = Y > 0 ? Math.min(1, Math.max(0, (Math.log10(Y * d) - LUM[0]) / (LUM[1] - LUM[0]))) : 0;
    const vari = T < 800 ? 'v0' : T < 1000 ? 'v1' : T < 1300 ? 'v2' : T < 1600 ? 'v3' : T < 2400 ? 'v4' : T < 4500 ? 'v5' : T < 7500 ? 'v6' : 'v7';
    cache = { T, lm, Mpk: M(lm, T), nakyva: vis / (SIGMA * T ** 4) * 100, rgb, glow, vari };
    return cache;
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l1); slT = p.createSlider(200, 10000, 5800, 100).parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('alue')).parent(l2); selA = p.createSelect().parent(l2);
    selA.option(__('alue_lyhyt'), 'lyhyt'); selA.option(__('alue_pitka'), 'pitka'); selA.selected('lyhyt');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { T: { input: slT.elt, unit: 'K' }, alue: { input: selA.elt, unit: '' } },
      reset: () => { slT.value(5800); selA.selected('lyhyt'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const T = Number(slT.value()), alue = selA.value() === 'pitka' ? 'pitka' : 'lyhyt', m = model(T);
    const lmax = m.lm * 1e9, huippu = lmax < 380 ? 'uv' : lmax <= 750 ? 'nakyva' : 'ir';
    lT.html(__('lampotila', { T: tx(T, 0) }));
    const where = { uv: __('huippu_uv'), nakyva: __('huippu_nakyva'), ir: __('huippu_ir') }[huippu];
    const colour = { v0: __('v0'), v1: __('v1'), v2: __('v2'), v3: __('v3'), v4: __('v4'), v5: __('v5'), v6: __('v6'), v7: __('v7') }[m.vari];
    const share = m.nakyva < 0.01 ? __('alle') : `$${tx(m.nakyva, m.nakyva < 10 ? 2 : 1)}\\,\\%$`;
    readout.html(__('lukemat', { l: tx(lmax, 0), a: where, T: tx(T, 0), t: tx(T - 273.15, 0), o: share, v: colour }));
    window.simState = { T, alue, lmax, tC: T - 273.15, nakyva: m.nakyva, huippu, vari: m.vari, glow: m.glow, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const narrow = cw < 500, Hc = narrow ? 660 : 400;
    if (p.__H !== Hc) { p.__H = Hc; p.resizeCanvas(600, Hc); setTimeout(() => p.redraw(), 0); return; }
    const fh = narrow ? Math.round(14 * k) : Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    p.background(250);
    if (narrow) { body(m, T, 170, 100, 56, fh, true); graph(m, T, alue, 26 + fh * 3.2, 600 - 30, 250 + fh * 1.8, Hc - 18 - fh * 3.0, fh, k); }
    else { body(m, T, 92, 170, 54, fh); graph(m, T, alue, 236, 572, 52, 400 - 18 - fh * 3.0, fh, k); }
    window.simState.labels = labels;
  };

  // --- the hot body: an iron ball on a stand that glows in the colour of its spectrum ---
  function body(m, T, cx, cy, r, fh, side) {
    const g = m.glow, c = m.rgb, ctx = p.drawingContext;
    if (g > 0) {                                           // halo
      const gr = ctx.createRadialGradient(cx, cy, r * 0.6, cx, cy, r * 2.1);
      gr.addColorStop(0, `rgba(${c.map(Math.round).join(',')},${0.55 * g})`); gr.addColorStop(1, `rgba(${c.map(Math.round).join(',')},0)`);
      ctx.fillStyle = gr; ctx.beginPath(); ctx.arc(cx, cy, r * 2.1, 0, 2 * Math.PI); ctx.fill();
    }
    p.stroke(...INKC); p.strokeWeight(2.5); p.fill(...IRONC);
    p.rect(cx - 8, cy + r - 2, 16, r * 0.5); p.fill(...METAL); p.rect(cx - r * 0.9, cy + r * 1.45, r * 1.8, 10, 3);
    const mix = IRONC.map((v, i) => v + (c[i] - v) * g);
    const gr2 = ctx.createRadialGradient(cx - r * 0.35, cy - r * 0.35, r * 0.1, cx, cy, r);
    const hi = mix.map((v) => Math.min(255, v + 60 * (1 - g) + 40 * g));
    gr2.addColorStop(0, `rgb(${hi.map(Math.round).join(',')})`); gr2.addColorStop(1, `rgb(${mix.map((v) => Math.round(v * (0.75 + 0.25 * g))).join(',')})`);
    ctx.fillStyle = gr2; p.stroke(...INKC); p.strokeWeight(2.5); ctx.beginPath(); ctx.arc(cx, cy, r, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
    // infrared: wavy arrows out of the ball at every temperature (every body radiates)
    p.stroke(...HEATC); p.strokeWeight(2); p.noFill();
    for (const a of [-2.4, -0.7, 0.7]) {
      const ux = Math.cos(a), uy = Math.sin(a), x0 = cx + ux * (r + 8), y0 = cy + uy * (r + 8), L = r * 0.55;
      p.beginShape(); for (let t = 0; t <= 1.001; t += 0.1) { const s = 4 * Math.sin(t * 3 * Math.PI); p.vertex(x0 + ux * L * t - uy * s, y0 + uy * L * t + ux * s); } p.endShape();
      const xe = x0 + ux * L, ye = y0 + uy * L; p.noStroke(); p.fill(...HEATC);
      p.triangle(xe + ux * 8, ye + uy * 8, xe - uy * 5, ye + ux * 5, xe + uy * 5, ye - ux * 5); p.stroke(...HEATC); p.noFill();
    }
    if (side) lab(`$T = ${tx(T, 0)}\\,\\text{K}$`, cx + r * 2.3, cy + fh * 0.35, 'l', fh, INKC);   // narrow: beside the ball
    else lab(`$T = ${tx(T, 0)}\\,\\text{K}$`, cx, cy + r * 1.45 + 18 + fh, 'c', fh, INKC);
  }

  // --- the graph: M_λ against λ, the visible band in colour, the peak marked ---
  function graph(m, T, alue, x0, x1, y1, y0, fh, k) {
    const R = RANGES[alue], X = (l) => x0 + l / R.max * (x1 - x0);   // l in nm
    // the vertical scale: the curve's highest point inside the range sits at 80 % of the plot's height
    const lTop = Math.min(m.lm * 1e9, R.max), top = M(lTop * 1e-9, T) / 1e6;   // W/(m²·µm)
    const e3 = Math.max(-3, Math.min(3, Math.floor(Math.log10(top) / 3)));        // a unit prefix nW … GW
    const pref = [PREF[e3 + 3], Math.pow(1000, e3)];
    const vmax = top / pref[1] / 0.8, st = nice(vmax / 4), Y = (v) => y0 - v / vmax * (y0 - y1);
    // visible band: faint colours over the plot, a solid strip along the axis
    const ctx = p.drawingContext, gr = ctx.createLinearGradient(X(380), 0, X(750), 0);
    [[0, '#7a1fd1'], [0.12, '#3b3bf0'], [0.3, '#1aa0e6'], [0.45, '#2fbf3f'], [0.6, '#e6e01a'], [0.75, '#f08a1a'], [1, '#c81e1e']].forEach(([o, col]) => gr.addColorStop(o, col));
    ctx.globalAlpha = 0.22; ctx.fillStyle = gr; ctx.fillRect(X(380), y1, X(750) - X(380), y0 - y1);
    ctx.globalAlpha = 1; ctx.fillRect(X(380), y0 - 9, Math.max(X(750) - X(380), 2), 9);
    // gridlines and ticks
    p.stroke(...RULEL); p.strokeWeight(1);
    for (let v = st; v <= vmax + 1e-9; v += st) p.line(x0, Y(v), x1, Y(v));
    for (let l = R.step; l <= R.max; l += R.step) p.line(X(l), y0, X(l), y1);
    // the curve, filled faintly underneath
    const pts = []; for (let i = 0; i <= 300; i++) { const l = R.max * i / 300; pts.push([X(l), Y(i === 0 ? 0 : M(l * 1e-9, T) / 1e6 / pref[1])]); }
    p.noStroke(); p.fill(...HEATL, 70); p.beginShape(); p.vertex(x0, y0); for (const q of pts) p.vertex(q[0], q[1]); p.vertex(x1, y0); p.endShape(p.CLOSE);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.beginShape(); for (const q of pts) p.vertex(q[0], q[1]); p.endShape();
    // the peak: a dashed guide to the axis and a dot, or an arrow to the right when the peak is beyond the range
    const lm = m.lm * 1e9;
    if (lm <= R.max) {
      const xp = X(lm), yp = Y(m.Mpk / 1e6 / pref[1]);
      p.stroke(...MUTEDC); p.strokeWeight(1.5); ctx.setLineDash([6, 5]); p.line(xp, yp, xp, y0); ctx.setLineDash([]);
      p.fill(...HEATC); p.stroke(255); p.strokeWeight(2); p.circle(xp, yp, 13);
      const al = xp > x1 - fh * 3 ? 'r' : xp < x0 + fh * 3 ? 'l' : 'c';
      lab('$\\lambda_\\text{max}$', al === 'r' ? xp + fh * 0.6 : al === 'l' ? xp - fh * 0.6 : xp, yp - fh * 0.9, al, fh, HEATC);
    } else {
      p.noStroke(); p.fill(...HEATC); const ya = y1 + fh * 2.6;
      p.triangle(x1, ya, x1 - 12, ya - 7, x1 - 12, ya + 7); p.stroke(...HEATC); p.strokeWeight(2.5); p.line(x1 - 40, ya, x1 - 10, ya);
      lab('$\\lambda_\\text{max}$', x1 - 46, ya + fh * 0.35, 'r', fh, HEATC);
    }
    // region words along the top of the plot, left out where the peak's label would meet them
    const xpk = lm <= R.max ? X(lm) : x1 - 46;
    if (alue === 'lyhyt' && Math.abs(X(190) - xpk) > fh * 3) lab('$\\text{UV}$', X(190), y1 + fh * 0.9, 'c', fh, MUTEDC);
    const xir = alue === 'lyhyt' ? X(1900) : X(15000);
    if (Math.abs(xir - xpk) > fh * 5) lab(__('alue_ir'), xir, y1 + fh * 0.9, 'c', fh, MUTEDC);
    // axes with arrowheads
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(x0, y0, x1 + 4, y0); p.line(x0, y0, x0, y1 - 14);
    p.noStroke(); p.fill(...INKC);
    p.triangle(x1 + 14, y0, x1 + 2, y0 - 6, x1 + 2, y0 + 6); p.triangle(x0, y1 - 24, x0 - 6, y1 - 12, x0 + 6, y1 - 12);
    p.stroke(...INKC); p.strokeWeight(2);
    const every = k > 1.5 ? 2 : 1;
    let i = 0;
    for (let l = R.step; l <= R.max; l += R.step, i++) {
      p.line(X(l), y0, X(l), y0 + 6);
      if ((i + 1) % every === 0) lab(`$${tx(l * R.f, 0)}$`, X(l), y0 + 8 + fh, 'c', fh, INKC);
    }
    i = 0;
    for (let v = st; v <= vmax + 1e-9; v += st, i++) {
      p.line(x0 - 6, Y(v), x0, Y(v));
      if ((i + 1) % every === 0) lab(`$${tx(v, decimals(st))}$`, x0 - 9, Y(v) + fh * 0.35, 'r', fh, INKC);
    }
    lab('$0$', x0 - 9, y0 + 8 + fh, 'r', fh, INKC);
    lab(`$\\lambda\\ (${R.unit === 'nm' ? '\\text{nm}' : R.unit})$`, x1 + 14, y0 + 8 + fh * 2.6, 'r', fh, INKC);
    lab(`$M_\\lambda\\ (${pref[0]}/(\\text{m}^2 \\cdot \\mu\\text{m}))$`, x0 - 2, y1 - 24 - fh * 0.5, 'l', fh, INKC);
  }

  const PREF = ['\\text{nW}', '\\mu\\text{W}', '\\text{mW}', '\\text{W}', '\\text{kW}', '\\text{MW}', '\\text{GW}'];
  const decimals = (st) => { let d = 0; while (d < 3 && Math.abs(st * 10 ** d - Math.round(st * 10 ** d)) > 1e-6) d++; return d; };
  function nice(v) {
    const e = Math.pow(10, Math.floor(Math.log10(v))), f = v / e;
    return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * e;
  }

  // every canvas text: drawn and its ink box pushed to simState.labels (canvas coordinates)
  function lab(str, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(str), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(str, x0, y);
    labels.push({ s: str, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
