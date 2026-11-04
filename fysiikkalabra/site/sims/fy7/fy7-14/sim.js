// fy7-14 Ohuen kalvon interferenssi: light from air falls at normal incidence on a thin film of thickness d. Two
// situations: a soap film in air (n = 1,33, air on both sides) or a MgF2 coating (n = 1,38) on glass (n = 1,52).
// Model: the Fresnel amplitudes r = (n_a − n_b) / (n_a + n_b) at the two surfaces (a negative r is the half-wavelength
// shift of a reflection against a larger refractive index) and the phase lag δ = 2π · 2nd / λ of wave 2; the reflected
// share is the exact single-layer value R = |(r1 + r2 e^(−iδ)) / (1 + r1 r2 e^(−iδ))|² (the weak multiple reflections
// inside the film included). Dispersion and absorption are left out; the glass is thick and its back face is not drawn.
// The picture: the film in cross-section (thickness magnified, rays drawn slanted so that they separate), the reflected
// waves 1 and 2 and their sum for the chosen λ, the graph R(λ) over 400–700 nm and the colour of the reflected white
// light (CIE 1931 multi-lobe fit of Wyman, Sloan & Shirley 2013, sRGB; brightness scaled: the soap film's strongest
// reflection, or bare glass for the coating, is white). Static: drawn again on every frame, no animation.
// Every canvas text goes through lab() (simState.labels).
new p5((p) => {
  const SIT = { saippua: { n: 1.33, ns: 1.0 }, pinnoite: { n: 1.38, ns: 1.52 } };
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEL = [227, 220, 203], RAYC = [230, 73, 128];
  const AIRC = [250, 250, 250], FILM = { saippua: [214, 232, 244], pinnoite: [226, 218, 242] }, GLASSC = [208, 230, 251];
  let selS, slD, slL, lD, lL, readout, labels = [], cache = {};

  // --- the model ---
  const amps = (n, ns) => [(1 - n) / (1 + n), (n - ns) / (n + ns)];
  function R(d, lam, n, ns) {
    const [r1, r2] = amps(n, ns), dl = 4 * Math.PI * n * d / lam, c = Math.cos(dl), s = -Math.sin(dl);
    const nr = r1 + r2 * c, ni = r2 * s, dr = 1 + r1 * r2 * c, di = r1 * r2 * s;
    return (nr * nr + ni * ni) / (dr * dr + di * di);
  }
  const gl = (x, mu, s1, s2) => { const t = (x - mu) / (x < mu ? s1 : s2); return Math.exp(-0.5 * t * t); };
  const cmf = (l) => [1.056 * gl(l, 599.8, 37.9, 31.0) + 0.362 * gl(l, 442.0, 16.0, 26.7) - 0.065 * gl(l, 501.1, 20.4, 26.2),
    0.821 * gl(l, 568.8, 46.9, 40.5) + 0.286 * gl(l, 530.9, 16.3, 31.1),
    1.217 * gl(l, 437.0, 11.8, 36.0) + 0.681 * gl(l, 459.0, 26.0, 13.8)];
  const lin = (X, Y, Z) => [3.2406 * X - 1.5372 * Y - 0.4986 * Z, -0.9689 * X + 1.8758 * Y + 0.0415 * Z, 0.0557 * X - 0.2040 * Y + 1.0570 * Z];
  const gam = (v) => 255 * (v <= 0.0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - 0.055);
  function spectral(w) { let X = 0, Y = 0, Z = 0; for (let l = 400; l <= 700; l += 2) { const c = cmf(l), v = w(l); X += v * c[0]; Y += v * c[1]; Z += v * c[2]; } return lin(X, Y, Z); }
  const WH = spectral(() => 1);
  function colour(t, d) {
    const S = SIT[t], norm = t === 'saippua' ? R(550 / (4 * S.n), 550, S.n, S.ns) : R(0, 550, S.n, S.ns);
    return spectral((l) => R(d, l, S.n, S.ns) / norm).map((v, i) => Math.round(gam(Math.min(1, Math.max(0, v / WH[i])))));
  }
  function lamColour(l) {                                    // the colour of monochromatic light, full brightness
    const c = cmf(l), v = lin(...c).map((x) => Math.max(0, x)), m = Math.max(...v) || 1;
    return v.map((x) => Math.round(gam(x / m)));
  }
  function state() {
    const t = selS.value() === 'pinnoite' ? 'pinnoite' : 'saippua', S = SIT[t];
    const d = Number(slD.value()), lam = Number(slL.value()), s = 2 * S.n * d, q = s / lam;
    const shifts = t === 'saippua' ? 1 : 2;
    const f = ((q + shifts / 2) % 1 + 1) % 1;
    let kind = Math.min(f, 1 - f) <= 0.05 ? 'vahvistava' : Math.abs(f - 0.5) <= 0.05 ? 'heikentava' : 'osittain';
    if (t === 'pinnoite' && d === 0) kind = 'paljas';
    const key = t + d;
    if (cache.key !== key) cache = { key, rgb: colour(t, d) };
    return { tilanne: t, n: S.n, ns: S.ns, d, lam, s, q, shifts, R: R(d, lam, S.n, S.ns) * 100, kind, rgb: cache.rgb };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('tilanne')).parent(l0); selS = p.createSelect().parent(l0);
    selS.option(__('saippua'), 'saippua'); selS.option(__('pinnoite'), 'pinnoite'); selS.selected('saippua');
    const l1 = p.createElement('label').parent(controls); lD = p.createSpan('').parent(l1); slD = p.createSlider(0, 1000, 200, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l2); slL = p.createSlider(400, 700, 550, 1).parent(l2);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tilanne: { input: selS.elt, unit: '' }, d: { input: slD.elt, unit: 'nm' }, lam: { input: slL.elt, unit: 'nm' } },
      reset: () => { selS.selected('saippua'); slD.value(200); slL.value(550); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const st = state();
    lD.html(__('paksuus', { d: tx(st.d, 0) })); lL.html(__('aallonpituus', { l: tx(st.lam, 0) }));
    readout.html(__('lukemat', { tila: __('tila_' + st.kind), s: tx(st.s, 1), q: tx(st.q, 2), m: String(st.shifts), R: tx(st.R, 2), l: tx(st.lam, 0) }));
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const narrow = cw < 500, Hc = narrow ? 960 : 400;
    if (p.__H !== Hc) { p.__H = Hc; p.resizeCanvas(600, Hc); setTimeout(() => p.redraw(), 0); return; }
    const fh = narrow ? Math.round(14 * k) : Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    p.background(...AIRC);
    if (narrow) {
      film(st, 12, 10, 576, 300, fh);
      waves(st, 12, 324, 576, 230, fh);
      graph(st, 18 + fh * 2.6, 588 - fh * 1.2, 590 + fh * 1.6, 860 - fh * 1.6, fh, k);
      swatch(st, 300, Hc - 14 - fh * 0.6, 200, fh, true);
    } else {
      film(st, 12, 10, 280, 228, fh);
      waves(st, 306, 10, 282, 228, fh);
      graph(st, 50, 420, 268 + fh * 0.6, 400 - 14 - fh * 2.4, fh, k);
      swatch(st, 520, 300, 110, fh, false);
    }
    p.stroke(...RULEL); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]);
    if (!narrow) { p.line(298, 14, 298, 236); p.line(12, 248, 588, 248); } else { p.line(12, 316, 588, 316); p.line(12, 564, 588, 564); }
    p.drawingContext.setLineDash([]);
    window.simState = { tilanne: st.tilanne, n: st.n, ns: st.ns, d: st.d, lam: st.lam, s: st.s, q: st.q, shifts: st.shifts,
      R: st.R, kind: st.kind, rgb: st.rgb, labels };
  };

  // --- the film in cross-section with the two reflected rays ---
  function film(st, bx, by, bw, bh, fh) {
    const ytop = by + bh * 0.42, th = 4 + st.d / 1000 * bh * 0.2, ybot = ytop + th;
    const below = st.tilanne === 'saippua' ? AIRC : GLASSC;
    p.noStroke(); p.fill(...below); p.rect(bx, ybot, bw, by + bh - ybot);
    p.fill(...FILM[st.tilanne]); p.rect(bx, ytop, bw, th);
    p.stroke(...INKC); p.strokeWeight(2); p.line(bx, ytop, bx + bw, ytop); p.line(bx, ybot, bx + bw, ybot);
    // rays: in at 20° from the normal (drawn slanted only so that they separate), out as rays 1 and 2
    const a = 20 * Math.PI / 180, b = Math.asin(Math.sin(a) / st.n), yr = by + fh * 2.4;
    const Ax = bx + bw * 0.42, Bx = Ax + th * Math.tan(b), Cx = Ax + 2 * th * Math.tan(b), up = (ytop - yr) * Math.tan(a);
    dashed(Ax, yr + fh * 0.4, Ax, ytop + th + 14);
    rayLine(Ax - up, yr, Ax, ytop, 3); arrowHead(Ax - up, yr, Ax, ytop);
    rayLine(Ax, ytop, Ax + up, yr, 3); arrowHead(Ax, ytop, Ax + up, yr);
    rayLine(Ax, ytop, Bx, ybot, 2.5); rayLine(Bx, ybot, Cx, ytop, 2.5); rayLine(Cx, ytop, Cx + up, yr, 3); arrowHead(Cx, ytop, Cx + up, yr);
    lab('$1$', Ax + up, yr - fh * 0.5, 'c', fh, INKC);
    lab('$2$', Cx + up + fh * 0.7, yr + fh * 0.6, 'l', fh, INKC);
    // the half-wavelength shifts: at the top surface always, at the bottom surface only on glass
    lab('$\\tfrac{1}{2}\\lambda$', Ax - up * 0.35 - fh * 0.8, ytop - fh * 0.5, 'r', fh, RAYC);
    if (st.shifts === 2) lab('$\\tfrac{1}{2}\\lambda$', Bx - fh * 0.6, ybot + fh * 1.5, 'r', fh, RAYC);
    // thickness
    const xd = bx + bw * 0.16;
    p.stroke(...INKC); p.strokeWeight(1.5); p.line(xd, ytop - 16, xd, ytop); p.line(xd, ybot, xd, ybot + 16);
    p.noStroke(); p.fill(...INKC); p.triangle(xd, ytop, xd - 4, ytop - 8, xd + 4, ytop - 8); p.triangle(xd, ybot, xd - 4, ybot + 8, xd + 4, ybot + 8);
    lab('$d$', xd - 8, ytop + th / 2 + fh * 0.35, 'r', fh, INKC);
    // media
    const nf = tx(st.n, 2);
    lab(`$\\text{${__('ilma')}},\\ n = 1{,}00$`, bx + bw - 4, by + fh * 1.2, 'r', fh, INKC);
    lab(`$\\text{${__(st.tilanne === 'saippua' ? 'kalvo_s' : 'kalvo_p')}},\\ n = ${nf}$`, bx + bw - 4, ybot + fh * 1.4, 'r', fh, INKC);
    lab(st.tilanne === 'saippua' ? `$\\text{${__('ilma')}},\\ n = 1{,}00$` : `$\\text{${__('lasi')}},\\ n = 1{,}52$`, bx + bw - 4, by + bh - fh * 0.4, 'r', fh, INKC);
  }

  // --- waves 1 and 2 and their sum, for the chosen wavelength ---
  function waves(st, bx, by, bw, bh, fh) {
    const [r1, r2] = amps(st.n, st.ns), a2 = r2 * (1 - r1 * r1), m = Math.max(Math.abs(r1), Math.abs(a2));
    const amp = bh * 0.085, A1 = r1 / m * amp, A2 = a2 / m * amp, del = 2 * Math.PI * st.q;
    const x0 = bx + fh * 3.6, x1 = bx + bw - 6, L = (x1 - x0) / 2.5, rows = [by + bh * 0.16, by + bh * 0.42, by + bh * 0.76];
    const wv = (x, i) => { const ph = 2 * Math.PI * (x - x0) / L; return i === 0 ? A1 * Math.sin(ph) : i === 1 ? A2 * Math.sin(ph - del) : A1 * Math.sin(ph) + A2 * Math.sin(ph - del); };
    // a dashed line through a crest of wave 1, to compare the phases
    const xc = x0 + L * (A1 < 0 ? 0.75 : 0.25);
    dashed(xc, rows[0] - amp - 6, xc, rows[2] + 2 * amp + 4);
    for (let i = 0; i < 3; i++) {
      p.stroke(...MUTEDC); p.strokeWeight(1); p.line(x0, rows[i], x1, rows[i]);
      p.noFill(); p.stroke(...(i < 2 ? RAYC : INKC)); p.strokeWeight(i < 2 ? 2.5 : 3);
      p.beginShape(); for (let x = x0; x <= x1 + 0.1; x += 2) p.vertex(x, rows[i] - wv(x, i)); p.endShape();
      lab(i === 0 ? '$1$' : i === 1 ? '$2$' : '$1 + 2$', bx + 4, rows[i] + fh * 0.35, 'l', fh, INKC);
    }
  }

  // --- R(λ) over the visible range, the chosen λ marked ---
  function graph(st, x0, x1, y1, y0, fh, k) {
    const S = SIT[st.tilanne], X = (l) => x0 + (l - 400) / 300 * (x1 - x0), Y = (v) => y0 - v / 8 * (y0 - y1);
    p.stroke(...RULEL); p.strokeWeight(1);
    for (let v = 2; v <= 8; v += 2) p.line(x0, Y(v), x1, Y(v));
    for (let l = 450; l <= 700; l += 50) p.line(X(l), y0, X(l), y1);
    for (let l = 400; l < 700; l += 2) { p.noStroke(); p.fill(...lamColour(l + 1)); p.rect(X(l), y0 - 8, X(l + 2) - X(l) + 0.5, 8); }
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.beginShape();
    for (let l = 400; l <= 700; l += 2) p.vertex(X(l), Y(R(st.d, l, S.n, S.ns) * 100)); p.endShape();
    const xm = X(st.lam), ym = Y(st.R);
    dashed(xm, ym, xm, y0);
    p.fill(...RAYC); p.stroke(255); p.strokeWeight(2); p.circle(xm, ym, 13);
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(x0, y0, x1 + 4, y0); p.line(x0, y0, x0, y1 - 14);
    p.noStroke(); p.fill(...INKC);
    p.triangle(x1 + 14, y0, x1 + 2, y0 - 6, x1 + 2, y0 + 6); p.triangle(x0, y1 - 24, x0 - 6, y1 - 12, x0 + 6, y1 - 12);
    p.stroke(...INKC); p.strokeWeight(2);
    const xo = k > 1.2 ? 12 + fh * 1.15 : 8 + fh;            // x tick labels lower on a phone, clear of the origin 0
    for (let l = 450; l <= 700; l += 50) { p.line(X(l), y0, X(l), y0 + 6); if (l % 100 === 0) lab(`$${l}$`, X(l), y0 + xo, 'c', fh, INKC); }
    lab('$400$', x0, y0 + xo, 'c', fh, INKC);
    for (let v = 2; v <= 8; v += 2) { p.line(x0 - 6, Y(v), x0, Y(v)); if (k <= 1.5 || v % 4 === 0) lab(`$${v}$`, x0 - 9, Y(v) + fh * 0.35, 'r', fh, INKC); }
    lab('$0$', x0 - 9, y0 + fh * 0.35, 'r', fh, INKC);
    lab('$\\lambda\\ (\\text{nm})$', x1 + 14, y0 + xo + fh * 1.4, 'r', fh, INKC);
    lab('$R\\ (\\%)$', x0 + 10, y1 - 24 + fh * 0.1, 'l', fh, INKC);
  }

  // --- the colour of the reflected white light ---
  function swatch(st, cx, cy, w, fh, wide) {
    const h = wide ? fh * 1.6 : w * 0.6, x = cx - w / 2, y = wide ? cy - h : cy - h / 2;
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...st.rgb); p.rect(x, y, w, h, 4);
    lab(`$\\text{${__('vari')}}$`, wide ? x - 8 : cx, wide ? y + h / 2 + fh * 0.35 : y - fh * 0.6, wide ? 'r' : 'c', fh, INKC);
  }

  function rayLine(x1, y1, x2, y2, w) { p.stroke(...RAYC); p.strokeWeight(w); p.line(x1, y1, x2, y2); }
  function arrowHead(x1, y1, x2, y2) {
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, mx = (x1 + x2) / 2 + ux * 6, my = (y1 + y2) / 2 + uy * 6;
    p.noStroke(); p.fill(...RAYC); p.triangle(mx, my, mx - ux * 12 - uy * 5, my - uy * 12 + ux * 5, mx - ux * 12 + uy * 5, my - uy * 12 - ux * 5);
  }
  function dashed(x1, y1, x2, y2) {
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(x1, y1, x2, y2); p.drawingContext.setLineDash([]);
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
