// fy6-13 Kondensaattori ja sen energia: a plate capacitor with plate area A (cm²), gap d (mm) and a dielectric that
// fills the gap (relative permittivity eps_r, breakdown strength E_max). C = eps0 eps_r A / d. Connected to the source:
// U = U0 and Q = C U0. Disconnected: the charge Q stays what it was at the moment the source was removed, U = Q / C.
// The field E = U / d (kV/mm = MV/m), the energy W = 1/2 Q U (nC · kV = µJ). Breakdown when E > E_max: connected, the
// sim shows a spark and a warning; disconnected, the capacitor discharges (Q = 0) until the source is reconnected.
// A static picture (no animation, so no speed control): the side view of the plates with their charges and field
// lines, and the (Q, U) graph whose triangle is the energy. Every canvas text goes through lab(), which pushes its box
// to simState.labels. The same model as lessons/FY6/fy6-13/lesson-answers.py. p5.js 1.9 instance mode.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], PLUSC = [201, 42, 42], MINUSC = [25, 113, 194],
        HEATC = [232, 89, 12], HEATL = [255, 192, 120], FIELDC = [43, 138, 62], ALU = [196, 204, 212], WHITE = [255, 255, 255];
  const EPS0 = 8.854e-12;
  const MAT = { ilma: { er: 1.0, Emax: 3, fill: null }, teflon: { er: 2.1, Emax: 60, fill: [227, 220, 203] },
                paperi: { er: 3.7, Emax: 16, fill: [241, 223, 181] }, lasi: { er: 5.6, Emax: 14, fill: [238, 245, 249] } };
  // wide: the plates left, the graph right; phone: the two stacked, larger labels
  const WIDE = { H: 400, picW: 344, cx: 200, cy: 200, gap: [20, 170], h: [80, 240], src: 40, wTop: 40, wBot: 372, sw: [66, 104],
                 ox: 392, oy: 330, gx1: 568, gy1: 64, xt: 18, xtitle: 42, status: [172, 392], nt: 4 };
  const NARROW = { H: 1040, picW: 600, cx: 320, cy: 290, gap: [44, 290], h: [128, 384], src: 64, wTop: 56, wBot: 560, sw: [120, 190],
                   ox: 112, oy: 920, gx1: 556, gy1: 650, status: [320, 588], nt: 4 };
  let G = WIDE, sk = 1, fh = 13, narrow = false, labels = [];
  let slD, slA, slU, selE, selL, lD, lA, lU, readout;
  let Qheld = null, burnt = false;

  const cap = (A, d, er) => EPS0 * er * A * 1e-4 / (d * 1e-3) * 1e12;            // pF
  const cur = () => ({ A: Number(slA.value()), d: Number(slD.value()), U0: Number(slU.value()), m: selE.value(), lahde: selL.value() });

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const mk = (min, max, v, st) => { const l = p.createElement('label').parent(controls); const s = p.createSpan('').parent(l); return [s, p.createSlider(min, max, v, st).parent(l)]; };
    [lD, slD] = mk(1.0, 10.0, 2.0, 0.5);
    [lA, slA] = mk(100, 400, 200, 50);
    [lU, slU] = mk(0, 4.0, 1.0, 0.1);
    const le = p.createElement('label').parent(controls); p.createSpan(__('eriste')).parent(le); selE = p.createSelect().parent(le);
    for (const k of ['ilma', 'teflon', 'paperi', 'lasi']) selE.option(__(k), k);
    selE.selected('ilma');
    const ll = p.createElement('label').parent(controls); p.createSpan(__('lahde')).parent(ll); selL = p.createSelect().parent(ll);
    selL.option(__('kytketty'), 'kytketty'); selL.option(__('irrotettu'), 'irrotettu'); selL.selected('kytketty');
    const onSource = () => {
      const c = cur();
      if (c.lahde === 'irrotettu') {
        const C = cap(c.A, c.d, MAT[c.m].er), broken = c.U0 / c.d > MAT[c.m].Emax + 1e-9;
        Qheld = broken ? 0 : C * c.U0; burnt = broken;
      } else { Qheld = null; burnt = false; }
      p.redraw();
    };
    selL.elt.addEventListener('change', onSource); selL.elt.addEventListener('input', onSource);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { d: { input: slD.elt, unit: 'mm' }, A: { input: slA.elt, unit: 'cm²' }, U0: { input: slU.elt, unit: 'kV' },
                eriste: { input: selE.elt }, lahde: { input: selL.elt } },
      reset: () => { slD.value(2.0); slA.value(200); slU.value(1.0); selE.selected('ilma'); selL.selected('kytketty'); Qheld = null; burnt = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function model() {
    const c = cur(), M = MAT[c.m], C = cap(c.A, c.d, M.er);
    let Q, U, lap = 0;
    if (c.lahde === 'kytketty' || Qheld === null) {
      U = c.U0; Q = C * U;
      if (U / c.d > M.Emax + 1e-9) lap = 1;
    } else {
      Q = Qheld; U = Q / C;
      if (U / c.d > M.Emax + 1e-9) { Qheld = 0; burnt = true; Q = 0; U = 0; }
      if (burnt) lap = 1;
    }
    return { ...c, er: M.er, Emax: M.Emax, fill: M.fill, C, Q, U, E: U / c.d, W: 0.5 * Q * U, lap, burnt: burnt && c.lahde === 'irrotettu' };
  }

  p.draw = () => {
    const S = model();
    const locked = (e) => e.getAttribute('aria-disabled') === 'true';
    slU.elt.disabled = S.lahde === 'irrotettu' || locked(slU.elt);
    lD.html(__('etaisyys', { d: tx(S.d, 1) }));
    lA.html(__('ala', { A: String(Math.round(S.A)) }));
    lU.html(__('jannite', { U: tx(S.U0, 1) }));
    readout.html(__('lukemat', { C: sig(S.C), Q: sig(S.Q), U: tx(S.U, S.U < 10 ? 2 : 1), E: tx(S.E, S.E < 10 ? 2 : 1), Emax: String(S.Emax), W: sig(S.W) })
                 + (S.burnt ? '<br><strong>' + __('purkautui-teksti') + '</strong>' : S.lap ? '<br><strong>' + __('lapilyonti-teksti') + '</strong>' : ''));
    window.simState = { A: S.A, d: S.d, U0: S.U0, eriste: S.m, lahde: S.lahde, er: S.er, Emax: S.Emax, C: S.C, Q: S.Q, U: S.U,
                        E: S.E, W: S.W, lapilyonti: S.lap, purkautui: S.burnt ? 1 : 0, labels: null };
    const cw = (p.canvas && p.canvas.parentElement && p.canvas.parentElement.clientWidth) || document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500; const k = Math.min(2.4, Math.max(1, 600 / cw));
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    const picH = narrow ? 600 : 400;
    grect(0, 0, G.picW, picH, [[246, 241, 230], [255, 255, 255]]);
    picture(S);
    p.stroke(220); p.strokeWeight(1);
    if (narrow) p.line(0, picH, 600, picH); else p.line(G.picW, 0, G.picW, 400);
    graph(S);
    window.simState.labels = labels;
  };

  // --- the capacitor seen from the side ------------------------------------------------------------------------
  function wire(pts) {
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3 * sk); p.strokeJoin(p.ROUND);
    p.beginShape(); for (const [x, y] of pts) p.vertex(x, y); p.endShape();
  }
  function picture(S) {
    const { cx, cy, src, wTop, wBot, sw } = G;
    const side = Math.sqrt(S.A);                                     // 10…20 cm
    const g = G.gap[0] + (S.d - 1) / 9 * (G.gap[1] - G.gap[0]), h = G.h[0] + (side - 10) / 10 * (G.h[1] - G.h[0]);
    const pt = 10 * sk, xl = cx - g / 2 - pt / 2, xr = cx + g / 2 + pt / 2, top = cy - h / 2, bot = cy + h / 2;
    // wires: + to the left plate over the top, − to the right plate under the bottom, a switch on the top wire
    wire([[src, cy - 8 * sk], [src, wTop], [sw[0], wTop]]);
    wire([[sw[1], wTop], [xl, wTop], [xl, top]]);
    wire([[src, cy + 8 * sk], [src, wBot], [xr, wBot], [xr, bot]]);
    p.fill(...INKC); p.noStroke(); p.circle(sw[0], wTop, 7 * sk); p.circle(sw[1], wTop, 7 * sk);
    p.stroke(...INKC); p.strokeWeight(3 * sk);
    if (S.lahde === 'kytketty') p.line(sw[0], wTop, sw[1], wTop);
    else p.line(sw[0], wTop, sw[1] - 6 * sk, wTop - 22 * sk);
    // the source: the long thin plate (+) above, the short thick plate (−) below
    p.noStroke(); p.fill(255); p.rect(src - 26 * sk, cy - 12 * sk, 52 * sk, 24 * sk);
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.line(src - 22 * sk, cy - 7 * sk, src + 22 * sk, cy - 7 * sk);
    p.strokeWeight(7 * sk); p.line(src - 11 * sk, cy + 7 * sk, src + 11 * sk, cy + 7 * sk);
    lab('$U_0$', src - 28 * sk, cy - 22 * sk, 'r');
    // the dielectric and its polarised molecules
    if (S.fill) {
      p.noStroke(); p.fill(...S.fill); p.rect(xl + pt / 2, top, g, h);
      const n = Math.max(1, Math.floor(g / (24 * sk))), m = Math.max(1, Math.floor(h / (26 * sk)));
      const rx = Math.min(8 * sk, g / n * 0.32), ry = 4 * sk;
      for (let i = 0; i < n; i++) for (let j = 0; j < m; j++) {
        const x = xl + pt / 2 + g * (i + 0.5) / n, y = top + h * (j + 0.5) / m;
        p.noStroke(); p.fill(...MINUSC, 150); p.arc(x, y, 2 * rx, 2 * ry, p.HALF_PI, 3 * p.HALF_PI, p.CHORD);
        p.fill(...PLUSC, 150); p.arc(x, y, 2 * rx, 2 * ry, -p.HALF_PI, p.HALF_PI, p.CHORD);
      }
    }
    // field lines: their spacing shows E
    if (S.E > 1e-9 && g > 12 * sk) {
      const sp = Math.min(90, Math.max(10, 30 / Math.sqrt(S.E / 0.5))) * sk, m = Math.max(1, Math.floor(h / sp));
      // where a line would run into a row of charges (the same count), the lines run between the charges instead
      const ys = m === nq(S, h) && m > 1 ? Array.from({ length: m - 1 }, (_, j) => top + h * (j + 1) / m) : Array.from({ length: m }, (_, j) => top + h * (j + 0.5) / m);
      for (const y of ys) {
        const x0 = xl + pt / 2 + 6 * sk, x1 = xr - pt / 2 - 6 * sk, xm = (x0 + x1) / 2, s = Math.min(7 * sk, (x1 - x0) / 4);
        p.stroke(...FIELDC); p.strokeWeight(1.8 * sk); p.line(x0, y, x1, y);
        p.noStroke(); p.fill(...FIELDC); p.triangle(xm + s, y, xm - s, y - 0.7 * s, xm - s, y + 0.7 * s);
      }
    }
    // the plates and their charges: the spacing of the charges shows the charge per area
    p.fill(...ALU); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(xl - pt / 2, top, pt, h); p.rect(xr - pt / 2, top, pt, h);
    const n = nq(S, h);
    if (n > 0) {
      for (let j = 0; j < n; j++) { const y = top + h * (j + 0.5) / n; charge(xl + pt / 2 + 1 * sk, y, 1); charge(xr - pt / 2 - 1 * sk, y, -1); }
    }
    // a spark across the gap at breakdown
    if (S.lap && !S.burnt) {
      const pts = []; for (let i = 0; i <= 6; i++) pts.push([xl + pt / 2 + g * i / 6, cy + (i % 2 ? -1 : 1) * Math.min(14 * sk, h / 6) * (i > 0 && i < 6 ? 1 : 0)]);
      p.noFill(); p.stroke(...HEATL); p.strokeWeight(8 * sk); p.beginShape(); for (const q of pts) p.vertex(...q); p.endShape();
      p.stroke(...HEATC); p.strokeWeight(3 * sk); p.beginShape(); for (const q of pts) p.vertex(...q); p.endShape();
    }
    // labels
    lab('$+Q$', xl - pt / 2 - 10 * sk, cy + 0.36 * fh, 'r', PLUSC);
    lab('$-Q$', xr + pt / 2 + 10 * sk, cy + 0.36 * fh, 'l', MINUSC);
    lab('$\\overline{E}$', cx, top - 12 * sk, 'c', FIELDC);
    p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.line(xl + pt / 2, bot + 12 * sk, xr - pt / 2, bot + 12 * sk);
    p.line(xl + pt / 2, bot + 6 * sk, xl + pt / 2, bot + 18 * sk); p.line(xr - pt / 2, bot + 6 * sk, xr - pt / 2, bot + 18 * sk);
    lab('$d$', cx, bot + 22 * sk + 0.8 * fh, 'c');
    if (S.burnt) lab(__('purkautui'), G.status[0], G.status[1], 'c', PLUSC);
    else if (S.lap) lab(__('lapilyonti'), G.status[0], G.status[1], 'c', PLUSC);
  }
  // the number of charges drawn on a plate of h px: their spacing shows the charge per area
  function nq(S, h) {
    const sig = S.Q / S.A; if (!(sig > 1e-9)) return 0;
    return Math.max(1, Math.floor(h / (Math.min(60, Math.max(9, 26 / Math.sqrt(sig / 0.4427))) * sk)));
  }
  function charge(x, y, sign) {
    const r = 4.5 * sk; p.noStroke(); p.fill(...(sign > 0 ? PLUSC : MINUSC)); p.circle(x, y, 2 * r);
    p.stroke(255); p.strokeWeight(1.4 * sk); p.line(x - r * 0.55, y, x + r * 0.55, y);
    if (sign > 0) p.line(x, y - r * 0.55, x, y + r * 0.55);
  }

  // --- the (Q, U) graph: the line U = Q / C, the triangle under it up to the present Q is the energy ---------------
  function nice(v, nmax) {
    const e = Math.floor(Math.log10(v));
    for (let k = e - 2; k <= e + 1; k++) for (const m of [1, 2, 5]) { const s = m * Math.pow(10, k); if (v / s <= nmax + 1e-9) return { s, max: Math.max(s, Math.ceil(v / s - 1e-9) * s) }; }
    return { s: v, max: v };
  }
  function graph(S) {
    const { ox, oy, gx1, gy1, nt } = G;
    const qa = nice(Math.max(S.Q, S.C * 0.1) * 1.25, nt), ua = nice(Math.max(S.U, 0.1) * 1.25, nt);
    const GX = (q) => ox + q / qa.max * (gx1 - ox), GY = (u) => oy - u / ua.max * (oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let q = qa.s; q <= qa.max + 1e-9; q += qa.s) p.line(GX(q), oy, GX(q), gy1);
    for (let u = ua.s; u <= ua.max + 1e-9; u += ua.s) p.line(ox, GY(u), gx1, GY(u));
    // the energy triangle and the line
    if (S.Q > 1e-12) {
      p.noStroke(); p.fill(...HEATL, 170); p.triangle(GX(0), GY(0), GX(S.Q), GY(S.U), GX(S.Q), GY(0));
      p.stroke(...HEATC); p.strokeWeight(1.5 * sk); p.line(GX(S.Q), GY(0), GX(S.Q), GY(S.U));
    }
    const qEnd = Math.min(qa.max, S.C * ua.max);
    p.stroke(...MINUSC); p.strokeWeight(3 * sk); p.line(GX(0), GY(0), GX(qEnd), GY(qEnd / S.C));
    // axes
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 14 * sk, oy); p.line(ox, oy, ox, gy1 - 12 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 26 * sk, oy, gx1 + 12 * sk, oy - 6 * sk, gx1 + 12 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 24 * sk, ox - 6 * sk, gy1 - 10 * sk, ox + 6 * sk, gy1 - 10 * sk);
    const dq = Math.max(0, -Math.floor(Math.log10(qa.s) + 1e-9)), du = Math.max(0, -Math.floor(Math.log10(ua.s) + 1e-9));
    for (let q = qa.s; q <= qa.max + 1e-9; q += qa.s) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(q), oy, GX(q), oy + 6 * sk);
      lab('$' + tx(q, dq) + '$', GX(q), oy + 8 * sk + 0.9 * fh, 'c');
    }
    for (let u = ua.s; u <= ua.max + 1e-9; u += ua.s) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(u), ox, GY(u));
      lab('$' + tx(u, du) + '$', ox - 9 * sk, GY(u) + 0.36 * fh, 'r');
    }
    lab('$0$', ox - 9 * sk, oy + 8 * sk + 0.9 * fh, 'r');
    lab('$Q\\,(\\text{nC})$', 596, oy + 8 * sk + 2.3 * fh, 'r');
    lab('$U\\,(\\text{kV})$', ox + 12 * sk, gy1 - 12 * sk, 'l');
    if (S.Q > 1e-12) {
      if (GX(S.Q) - ox > 60 * sk && oy - GY(S.U) > 46 * sk) lab('$W$', GX(S.Q * 0.68), GY(S.U * 0.24) + 0.36 * fh, 'c');
      p.fill(...MINUSC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(GX(S.Q), GY(S.U), 11 * sk);
      p.noFill(); p.stroke(...PLUSC); p.strokeWeight(2.5 * sk); p.circle(GX(S.Q), GY(S.U), 22 * sk);
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  function grect(x, y, w, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, w, h); c.restore();
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sig = (x) => tx(x, x >= 100 ? 0 : x >= 10 ? 1 : x >= 1 ? 2 : 3);
});
