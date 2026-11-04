// fy7-5 Sähkömagneettinen induktio: a square coil (side l = 0,10 m, N turns) moves at a constant speed v through a
// region of uniform magnetic field B (into the page) that is D = 0,20 m wide and zero outside, with a sharp edge. The
// coil's leading side starts 0,05 m before the field and the run ends when its trailing side is 0,05 m past it.
// Model: when the leading side is x inside the field, the flux through one turn is Φ = B l · overlap(x), where overlap is
// the coil's length inside the field. The induced voltage is e = −N ΔΦ/Δt: −N B l v while entering, 0 while the coil is
// wholly inside, +N B l v while leaving. A voltmeter takes no current, so no current flows and nothing brakes the coil.
// The picture: the field region with even crosses, the coil (copper, its part in the field shaded green), the velocity
// arrow; below, the graphs Φ(t) and e(t) drawn during the run on a fixed time axis 0–8 s. After a run simState gives the
// entering voltage e_tulo, its duration t_tulo = l/v and the voltage inside e_sisalla. The speed select scales only the
// pace (dt · speed); every value is computed in simulated time. window.simAdvance(s) advances a run for the tests.
// On a narrow screen (sim-root < 500 px) the canvas is taller and the labels larger (NOTES §4).
// Every canvas text goes through lab(), which pushes its box (canvas coordinates) to simState.labels.
new p5((p) => {
  const L = 0.10, D = 0.20, X0 = -0.05, XEND = D + L + 0.05, TMAX = 8;   // m, m, m, m, s (time axis)
  const PXM = 1000, XF = 200;                                            // canvas px per metre; canvas x of the field's left edge
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], FIELD = [43, 138, 62], FIELDL = [178, 242, 187],
        VEL = [25, 113, 194], COPPER = [184, 98, 45], PAPER = [246, 241, 230];
  const WIDE = { H: 400, bLab: 18, rTop: 26, rBot: 136, ox: 64, gx1: 520, phiT: 160, phiTop: 172, phiBot: 252,
                 eT: 282, eTop: 294, eBot: 374, tLab: 394 };
  const NARROW = { H: 760, bLab: 26, rTop: 40, rBot: 150, ox: 100, gx1: 520, phiT: 196, phiTop: 214, phiBot: 400,
                   eT: 446, eTop: 464, eBot: 704, tLab: 742 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let slV, slB, selN, selSpeed, lV, lB, btn, readout;
  let t = 0, running = false, done = false, res = null;

  const params = () => ({ v: Number(slV.value()), B: Number(slB.value()), N: Number(selN.value()) });
  const overlap = (x) => Math.max(0, Math.min(x, D) - Math.max(x - L, 0));          // m of the coil inside the field
  const xAt = (S, tt) => X0 + S.v * tt;
  const phiAt = (S, tt) => S.B * L * overlap(xAt(S, tt)) * 1e3;                        // mWb through one turn
  function eAt(S, tt) {                                                                 // mV, e = −N ΔΦ/Δt
    const x = xAt(S, tt), e0 = S.N * S.B * L * S.v * 1e3;
    if (x > 0 && x < L) return -e0;
    if (x > D && x < D + L) return e0;
    return 0;
  }
  const runTime = (S) => (XEND - X0) / S.v;
  const nice = (v) => { const k = Math.pow(10, Math.floor(Math.log10(v))); for (const m of [1, 2, 4, 5, 8, 10]) if (m * k >= v - 1e-9) return m * k; return 10 * k; };

  function restart(go) { t = 0; running = go; done = false; res = null; }
  function finish(S) {
    running = false; done = true; t = runTime(S);
    const mid = (0.5 * L - X0) / S.v, inside = ((L + D) / 2 - X0) / S.v;   // halfway through entering; the middle of the inside phase
    res = { e_tulo: Math.round(eAt(S, mid) * 10) / 10 + 0, t_tulo: Math.round(L / S.v * 100) / 100, e_sisalla: Math.round(eAt(S, inside) * 10) / 10 + 0 };
  }
  function advance(sec) {
    if (!running) return;
    const S = params(); t += sec;
    if (t >= runTime(S)) finish(S);
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { restart(true); p.loop(); });
    const l1 = p.createElement('label').parent(controls); lV = p.createSpan('').parent(l1); slV = p.createSlider(0.05, 0.2, 0.1, 0.05).parent(l1);
    const l2 = p.createElement('label').parent(controls); lB = p.createSpan('').parent(l2); slB = p.createSlider(0.1, 0.5, 0.2, 0.1).parent(l2);
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('kierroksia')).parent(l3); selN = p.createSelect().parent(l3);
    for (const k of ['1', '5', '10', '20']) selN.option(__('n' + k), k);
    selN.selected('10');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '3'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    for (const e of [slV.elt, slB.elt, selN.elt]) { e.addEventListener('input', () => { restart(false); p.redraw(); }); e.addEventListener('change', () => { restart(false); p.redraw(); }); }
    window.simAdvance = (sec) => { advance(sec); p.redraw(); };
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { v: { input: slV.elt, unit: 'm/s' }, B: { input: slB.elt, unit: 'T' }, N: { input: selN.elt, unit: '' } },
      reset: () => { slV.value(0.1); slB.value(0.2); selN.selected('10'); restart(false); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    advance(Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
    const S = params(), T = runTime(S), x = xAt(S, t), phi = phiAt(S, t), e = eAt(S, t) + 0;
    lV.html(__('vauhti', { v: tx(S.v, 2) })); lB.html(__('kentta', { B: tx(S.B, 2) }));
    btn.html(running ? __('liikkuu') : done ? __('uudelleen') : __('kaynnista'));
    readout.html(__('lukemat', { e: tx(e, 1), Phi: tx(phi, 2), t: tx(t, 2) }) +
      (res ? __('tulos', { e1: tx(res.e_tulo, 1), dt: tx(res.t_tulo, 2), e2: tx(res.e_sisalla, 1) }) : __('odottaa')));
    window.simState = { v: S.v, B: S.B, N: S.N, t, x, Phi: phi, e, Phi_max: S.B * L * L * 1e3, T, running: running ? 1 : 0,
                        e_tulo: res ? res.e_tulo : null, t_tulo: res ? res.t_tulo : null, e_sisalla: res ? res.e_sisalla : null, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.rBot + 12, [PAPER, [255, 255, 255]]);
    picture(S, x);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.rBot + 12, 600, G.rBot + 12);
    graphs(S, T);
    window.simState.labels = labels;
    if (!running) p.noLoop();
  };

  const CX = (xm) => XF + xm * PXM;

  function picture(S, x) {
    const { rTop, rBot } = G;
    // the field region: tinted, with crosses on an even grid (the field points into the page)
    p.noStroke(); p.fill(...FIELDL, 110); p.rect(CX(0), rTop, D * PXM, rBot - rTop);
    p.noFill(); p.stroke(...FIELD); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([6, 4]);
    p.rect(CX(0), rTop, D * PXM, rBot - rTop); p.drawingContext.setLineDash([]);
    const rows = 4, dy = (rBot - rTop) / rows;
    p.stroke(...FIELD); p.strokeWeight(2);
    for (let i = 0; i < rows; i++) for (let j = 0; j < 8; j++) {
      const cx = CX(0) + 12.5 + 25 * j, cy = rTop + dy * (i + 0.5), d = 4.5;
      p.line(cx - d, cy - d, cx + d, cy + d); p.line(cx + d, cy - d, cx - d, cy + d);
    }
    lab('$\\overline{B}$', CX(D / 2), G.bLab, 'c', FIELD);
    // the coil: its part inside the field shaded, its turns as nested squares
    const x1 = CX(x), x0 = CX(x - L), yc = (rTop + rBot) / 2, h = L * PXM / 2;
    const a = Math.max(x0, CX(0)), b = Math.min(x1, CX(D));
    if (b > a) { p.noStroke(); p.fill(...FIELD, 70); p.rect(a, yc - h, b - a, 2 * h); }
    p.noFill(); p.stroke(...COPPER);
    const turns = Math.min(S.N, 4);
    for (let i = 0; i < turns; i++) { p.strokeWeight(3 * sk); p.rect(x0 + 3 * i, yc - h + 3 * i, 2 * h - 6 * i, 2 * h - 6 * i, 2); }
    // the velocity arrow inside the coil
    const ay = yc + 14 * sk;
    arrow(x1 - h - 26, ay, x1 - h + 26, ay, VEL, 3 * sk, 11 * sk);
    lab('$\\overline{v}$', x1 - h, ay - 10 * sk, 'c', VEL);
  }

  function graphs(S, T) {
    const { ox, gx1 } = G, GX = (tt) => ox + tt / TMAX * (gx1 - ox);
    const t1 = (0 - X0) / S.v, t2 = (L - X0) / S.v, t3 = (D - X0) / S.v, t4 = (D + L - X0) / S.v;
    const phiMax = S.B * L * L * 1e3, phiS = nice(phiMax), e0 = S.N * S.B * L * S.v * 1e3, eS = nice(S.N * S.B * L * 0.2 * 1e3);
    const tc = Math.min(t, T);
    // Φ(t)
    const PY = (v) => G.phiBot - v / phiS * (G.phiBot - G.phiTop);
    axes(G.phiTop, G.phiBot, G.phiBot, GX, '$\\Phi\\,(\\text{mWb})$', G.phiT, [[0, PY(0)], [phiS / 2, PY(phiS / 2)], [phiS, PY(phiS)]], false);
    curve([[0, 0], [t1, 0], [t2, phiMax], [t3, phiMax], [t4, 0], [T, 0]], tc, GX, PY, FIELD);
    // e(t), signed: the time axis at e = 0
    const EY = (v) => (G.eTop + G.eBot) / 2 - v / eS * (G.eBot - G.eTop) / 2;
    axes(G.eTop, G.eBot, EY(0), GX, '$e\\,(\\text{mV})$', G.eT, [[eS, EY(eS)], [0, EY(0)], [-eS, EY(-eS)]], true);
    curve([[0, 0], [t1, 0], [t1, -e0], [t2, -e0], [t2, 0], [t3, 0], [t3, e0], [t4, e0], [t4, 0], [T, 0]], tc, GX, EY, INKC);
    if (t > 0 || done) {
      dot(GX(tc), PY(phiAt(S, tc)), FIELD);
      dot(GX(tc), EY(eAt(S, Math.max(0, tc - 1e-9))), INKC);
    }
  }

  function axes(top, bot, yAxis, GX, title, titleY, yticks, signed) {
    const { ox, gx1 } = G;
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let s = 1; s <= TMAX; s++) p.line(GX(s), top, GX(s), bot);
    for (const [v, y] of yticks) if (y !== yAxis) p.line(ox, y, gx1, y);
    p.stroke(...INKC); p.strokeWeight(2.5 * sk);
    p.line(ox, yAxis, gx1 + 14 * sk, yAxis); p.line(ox, bot, ox, top - 10 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 24 * sk, yAxis, gx1 + 12 * sk, yAxis - 5 * sk, gx1 + 12 * sk, yAxis + 5 * sk);
    p.triangle(ox, top - 20 * sk, ox - 5 * sk, top - 8 * sk, ox + 5 * sk, top - 8 * sk);
    for (const [v, y] of yticks) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, y, ox, y);
      lab('$' + tx(v, v === Math.round(v) ? 0 : 1) + '$', ox - 9 * sk, y + 0.36 * fh, 'r', INKC);
    }
    for (let s = 1; s <= TMAX; s++) { p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(s), yAxis, GX(s), yAxis + 6 * sk); }
    lab(title, ox + 12 * sk, titleY, 'l', INKC);
    if (signed) {          // the time numbers once, under the lower graph
      for (let s = 0; s <= TMAX; s++) if (sk < 1.5 || s % 2 === 0) lab('$' + s + '$', GX(s), G.tLab, 'c', INKC);
      lab('$t\\,(\\text{s})$', 596, G.tLab, 'r', INKC);
    }
  }

  function curve(pts, tc, GX, Y, col) {
    if (tc <= 0 && !done) return;
    p.noFill(); p.stroke(...col); p.strokeWeight(3 * sk); p.strokeJoin(p.ROUND); p.beginShape();
    for (let i = 0; i < pts.length; i++) {
      const [a, b] = pts[i];
      if (a <= tc) { p.vertex(GX(a), Y(b)); continue; }
      const [a0, b0] = pts[i - 1];
      p.vertex(GX(tc), Y(b0 + (b - b0) * (tc - a0) / (a - a0))); break;
    }
    p.endShape();
  }
  function dot(x, y, col) { p.fill(...col); p.stroke(255); p.strokeWeight(2 * sk); p.circle(x, y, 11 * sk); }
  function arrow(x1, y1, x2, y2, col, w, H) {
    const a = Math.atan2(y2 - y1, x2 - x1);
    p.stroke(...col); p.strokeWeight(w); p.line(x1, y1, x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.42), y2 - H * Math.sin(a - 0.42), x2 - H * Math.cos(a + 0.42), y2 - H * Math.sin(a + 0.42));
  }

  // every canvas text: its box pushed to simState.labels (canvas coordinates), kept inside the canvas
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
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
