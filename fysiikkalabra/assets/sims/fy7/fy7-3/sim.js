// fy7-3 Virtajohtimen ja käämin magneettikenttä: a coil of radius R = 2,0 cm with N turns wound evenly over its length l
// carries the current I. A magnetic field probe (Hall sensor) on a rod moves along the coil's axis. The field on the axis
// is the sum of the turns' fields, which for an even winding gives
//   B(x) = mu0 N I / (2 l) · [ (x + l/2) / sqrt((x + l/2)² + R²) − (x − l/2) / sqrt((x − l/2)² + R²) ],
// x measured from the coil's centre. Inside a long coil this is close to mu0 N I / l; at an end it is about half of that.
// No iron core and no Earth's field. The current's direction (front strands down or up) decides which end is N.
// The picture: the coil from the side (turns drawn one per 20 turns), green field lines, violet current marks moving
// along the front strands (their pace is only a picture; the speed select scales it), the probe and the length l.
// Below: the graph B(x) along the axis with the probe's point. Every canvas text goes through lab(), which pushes its
// box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const MU0 = 4 * Math.PI * 1e-7, R = 0.020;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], FIELD = [43, 138, 62], FIELDL = [178, 242, 187],
        CURR = [112, 72, 232], COPPER = [184, 98, 45], TUBE = [238, 245, 249], TUBEE = [138, 150, 163], ALU = [196, 204, 212],
        IRONC = [108, 117, 125], NPOLE = [242, 166, 156], SPOLE = [208, 230, 251], PAPER = [246, 241, 230];
  // wide 600 x 400 (picture above, graph below); narrow (sim-root < 500 px) 600 x 780, panels stacked, larger labels
  const WIDE = { H: 400, yc: 112, rp: 17, probeLab: 22, dim: 196, dimLab: 216, picH: 232,
                 ox: 70, oy: 372, gx1: 520, gy1: 262, xlab: 394, xstep: 10 };
  const NARROW = { H: 780, yc: 190, rp: 17, probeLab: 40, dim: 318, dimLab: 352, picH: 390,
                   ox: 104, oy: 700, gx1: 486, gy1: 470, xlab: 742, xstep: 20 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let slI, selN, slL, slX, selDir, selSpeed, lI, lL, lX, readout, phase = 0;

  const XP = (xcm) => 300 + xcm * 8.4;               // canvas x of a point x cm from the coil's centre (picture and graph share it)
  function field(N, I, l, x) {                         // T, on the axis; l and x in metres
    const a1 = x + l / 2, a2 = x - l / 2;
    return MU0 * N * I / (2 * l) * (a1 / Math.hypot(a1, R) - a2 / Math.hypot(a2, R));
  }
  const params = () => ({ I: Number(slI.value()), N: Number(selN.value()), l: Number(slL.value()), x: Number(slX.value()), dir: Number(selDir.value()) });

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lI = p.createSpan('').parent(l1); slI = p.createSlider(0, 3, 1, 0.1).parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('kierroksia')).parent(l2); selN = p.createSelect().parent(l2);
    for (const k of ['100', '200', '400']) selN.option(__('n' + k), k);
    selN.selected('200');
    const l3 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l3); slL = p.createSlider(10, 40, 20, 5).parent(l3);
    const l4 = p.createElement('label').parent(controls); lX = p.createSpan('').parent(l4); slX = p.createSlider(-30, 30, 0, 1).parent(l4);
    const l5 = p.createElement('label').parent(controls); p.createSpan(__('suunta')).parent(l5); selDir = p.createSelect().parent(l5);
    selDir.option(__('alas'), '1'); selDir.option(__('ylos'), '-1'); selDir.selected('1');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { I: { input: slI.elt, unit: 'A' }, N: { input: selN.elt, unit: '' }, l: { input: slL.elt, unit: 'cm' },
                x: { input: slX.elt, unit: 'cm' }, dir: { input: selDir.elt, unit: '' } },
      reset: () => { slI.value(1); selN.selected('200'); slL.value(20); slX.value(0); selDir.selected('1'); phase = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales only the pace of the current marks; B does not depend on it
    phase = (phase + 0.6 * Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value())) % 1;
    const S = params(), lm = S.l / 100, xm = S.x / 100;
    const B = Math.abs(field(S.N, S.I, lm, xm)) * 1e3, Bc = field(S.N, S.I, lm, 0) * 1e3, Blong = MU0 * S.N * S.I / lm * 1e3, n = S.N / lm;
    lI.html(__('virta', { I: tx(S.I, 1) }));
    lL.html(__('pituus', { l: String(S.l) }));
    lX.html(__('paikka', { x: tx(S.x, 0) }));
    readout.html(__('lukemat', { B: tx(B, 2), n: String(Math.round(n)), d: S.I > 0 ? __(S.dir > 0 ? 'oikealle' : 'vasemmalle') : __('eikenttaa') }));
    window.simState = { I: S.I, N: S.N, l: S.l, x: S.x, dir: S.dir, n, B, Bc, Blong, northRight: S.I > 0 && S.dir > 0 ? 1 : 0, phase, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.picH, [PAPER, [255, 255, 255]]);
    picture(S, B);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.picH, 600, G.picH);
    graph(S, lm, B);
    window.simState.labels = labels;
  };

  function picture(S, B) {
    const { yc, rp } = G, x0 = XP(-S.l / 2), x1 = XP(S.l / 2), on = S.I > 0, sgn = S.dir;
    // field lines: straight inside, spreading at the ends and closing outside (a schematic picture of their shape)
    if (on) {
      const a = 90 + 165 * Math.min(1, S.I / 2);
      for (const s of [-1, 1]) for (const f of [0.45, 0.8]) {
        const yi = yc + s * f * rp * 0.55, yo = yc + s * (rp + (f > 0.5 ? 34 : 18) * sk);
        p.noFill(); p.stroke(...FIELD, a); p.strokeWeight(2.5 * sk);
        p.bezier(x1 - 4, yi, x1 + 70 * f + 30, yi + s * 2, x1 + 40, yo, (x0 + x1) / 2, yo);
        p.noFill(); p.stroke(...FIELD, a); p.strokeWeight(2.5 * sk);
        p.bezier(x0 + 4, yi, x0 - 70 * f - 30, yi + s * 2, x0 - 40, yo, (x0 + x1) / 2, yo);
        arrowHead((x0 + x1) / 2, yo, -sgn, FIELD, a);        // outside the field runs back from N to S
      }
      for (const dy of [-0.55, 0, 0.55]) { p.stroke(...FIELD, a); p.strokeWeight(2.5 * sk); p.line(x0 - 10, yc + dy * rp, x1 + 10, yc + dy * rp); }
      for (const dy of [-0.55, 0.55]) arrowHead((x0 + x1) / 2 + sgn * 18, yc + dy * rp, sgn, FIELD, a);
    }
    // back strands of the turns, the tube, the front strands
    const turns = S.N / 20, step = (x1 - x0) / turns;
    p.stroke(...COPPER, 110); p.strokeWeight(2 * sk);
    for (let i = 0; i < turns; i++) { const x = x0 + (i + 0.5) * step; p.line(x + step * 0.3, yc - rp, x - step * 0.3, yc + rp); }
    p.noStroke(); p.fill(...TUBE, 170); p.rect(x0, yc - rp * 0.82, x1 - x0, rp * 1.64);
    p.noFill(); p.stroke(...TUBEE); p.strokeWeight(1.5 * sk); p.rect(x0, yc - rp * 0.82, x1 - x0, rp * 1.64);
    p.stroke(...COPPER); p.strokeWeight(3 * sk);
    for (let i = 0; i < turns; i++) { const x = x0 + (i + 0.5) * step; p.line(x - step * 0.3, yc - rp, x + step * 0.3, yc + rp); }
    // current marks moving along every other front strand (down when sgn > 0)
    if (on) {
      p.noStroke(); p.fill(...CURR);
      for (let i = 0; i < turns; i += 2) {
        const x = x0 + (i + 0.5) * step, t = sgn > 0 ? phase : 1 - phase;
        for (const u of [t, (t + 0.5) % 1]) {
          const px = x - step * 0.3 + u * step * 0.6, py = yc - rp + u * 2 * rp;
          p.circle(px, py, 6 * sk);
        }
      }
      for (const i of [0, Math.max(0, Math.floor(turns) - 1)]) {   // a current arrow on the first and last strand
        const x = x0 + (i + 0.5) * step;
        arrowHead(x, yc + sgn * rp * 0.2, sgn > 0 ? 2 : -2, CURR, 255);
      }
    }
    // the probe on its rod, entering from the right along the axis
    const px = XP(S.x);
    p.stroke(...IRONC); p.strokeWeight(4 * sk); p.line(px + 6 * sk, yc, 600, yc);
    if (on) {   // poles: the end the field leaves is N
      const xr = x1 + 22 * sk, xl = x0 - 22 * sk;
      pole(sgn > 0 ? xr : xl, 'N'); pole(sgn > 0 ? xl : xr, 'S');
    }
    p.fill(...ALU); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.rect(px - 7 * sk, yc - 5 * sk, 14 * sk, 10 * sk, 2 * sk);
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([4 * sk, 4 * sk]);
    p.line(px, yc - 8 * sk, px, G.probeLab + 0.5 * fh); p.drawingContext.setLineDash([]);
    lab('$B = ' + tx(B, 2) + '\\,\\text{mT}$', px, G.probeLab, 'c', INKC);
    // the length l under the coil
    const y = G.dim;
    p.stroke(...INKC); p.strokeWeight(1.8 * sk); p.line(x0, y, x1, y);
    p.line(x0, y - 7 * sk, x0, y + 7 * sk); p.line(x1, y - 7 * sk, x1, y + 7 * sk);
    lab('$l = ' + S.l + '\\,\\text{cm}$', (x0 + x1) / 2, G.dimLab, 'c', INKC);
  }

  function pole(x, letter) {
    const r = 11 * sk;
    p.fill(...(letter === 'N' ? NPOLE : SPOLE)); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.circle(x, G.yc, 2 * r + 8 * sk);
    lab('$\\text{' + letter + '}$', x, G.yc + 0.36 * fh, 'c', INKC, true);
  }

  function arrowHead(x, y, d, col, a) {     // d = ±1: along x; ±2: along y (2 down, −2 up)
    const s = 7 * sk;
    p.noStroke(); p.fill(...col, a);
    if (Math.abs(d) === 1) p.triangle(x + d * s, y, x - d * s, y - s * 0.75, x - d * s, y + s * 0.75);
    else { const e = d > 0 ? 1 : -1; p.triangle(x, y + e * s, x - s * 0.75, y - e * s, x + s * 0.75, y - e * s); }
  }

  // --- the graph B(x) along the axis, the probe's point ringed ---
  function graph(S, lm, B) {
    const { ox, oy, gx1, gy1 } = G;
    const peak = Math.abs(field(S.N, S.I, lm, 0)) * 1e3, ymax = peak <= 7.6 ? 8 : 16, ystep = ymax / 4;
    const GX = (x) => ox + (x + 30) / 60 * (gx1 - ox), GY = (b) => oy - Math.min(b, ymax) / ymax * (oy - gy1);
    // the coil's extent shaded on the graph
    p.noStroke(); p.fill(...FIELDL, 90); p.rect(GX(-S.l / 2), gy1, GX(S.l / 2) - GX(-S.l / 2), oy - gy1);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let x = -30; x <= 30; x += 10) if (x !== -30) p.line(GX(x), oy, GX(x), gy1);
    for (let b = ystep; b <= ymax; b += ystep) p.line(ox, GY(b), gx1, GY(b));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ox, oy, gx1 + 16 * sk, oy); p.line(ox, oy, ox, gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, oy, gx1 + 14 * sk, oy - 6 * sk, gx1 + 14 * sk, oy + 6 * sk);
    p.triangle(ox, gy1 - 26 * sk, ox - 6 * sk, gy1 - 12 * sk, ox + 6 * sk, gy1 - 12 * sk);
    for (let b = ystep; b <= ymax; b += ystep) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(ox - 6 * sk, GY(b), ox, GY(b));
      lab('$' + b + '$', ox - 9 * sk, GY(b) + 0.36 * fh, 'r', INKC);
    }
    lab('$0$', ox - 9 * sk, oy + 0.36 * fh, 'r', INKC);
    for (let x = -30; x <= 30; x += 10) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(GX(x), oy, GX(x), oy + 6 * sk);
      if (x % G.xstep === 0) lab('$' + x + '$', GX(x), G.xlab, 'c', INKC);
    }
    lab('$B\\,(\\text{mT})$', ox + 12 * sk, gy1 - 14 * sk, 'l', INKC);
    lab('$x\\,(\\text{cm})$', 596, G.xlab, 'r', INKC);
    // the curve
    p.noFill(); p.stroke(...FIELD); p.strokeWeight(3 * sk); p.beginShape();
    for (let j = 0; j <= 240; j++) { const x = -30 + j * 0.25; p.vertex(GX(x), GY(Math.abs(field(S.N, S.I, lm, x / 100)) * 1e3)); }
    p.endShape();
    const x = GX(S.x), y = GY(B);
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 5 * sk]);
    p.line(x, y, x, oy); p.line(ox, y, x, y); p.drawingContext.setLineDash([]);
    p.fill(...FIELD); p.stroke(255); p.strokeWeight(2 * sk); p.circle(x, y, 12 * sk);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(x, y, 22 * sk);
  }

  // every canvas text: its box pushed to simState.labels (canvas coordinates); free: drawn where asked, not clamped
  function lab(s, x, y, align, col, free) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = free ? xa : Math.min(Math.max(xa, 2), 600 - w - 2);
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
