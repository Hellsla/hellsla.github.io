// fy6-10 Sähkövaraus ja Coulombin laki: two small charged metal spheres on insulating stands on a bench. Sliders set
// the charges q1 and q2 (−40 … +40 nC) and the distance r between the centres (3,0 … 12 cm). Model
// (lessons/FY6/fy6-10/lesson-answers.py): point charges, F = k |q1 q2| / r², k = 8,988 · 10⁹ N m²/C², in mN; the force on
// sphere 1 (F21) and on sphere 2 (F12) are equal and opposite: repulsion for like signs, attraction for unlike, none
// when either charge is zero (the model has no induction). Red force arrows are to scale (30 px per mN, cut at 130 px
// with a break mark); sphere 1's arrow is drawn above the spheres and sphere 2's above that, so that they never cover
// each other. The lower (on a phone: the second) panel is the (r, F) or (1/r², F) graph of the points the student marks
// for the present charges, and the present reading. "Kenttäviivat" draws the field lines of the two point charges,
// traced numerically. Every canvas text goes through lab(), which pushes its box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const K = 8.988e9, SCALE = 30, CAP = 130, PX = 30;           // px per mN, longest arrow, px per cm
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], FORCE = [201, 42, 42], FIELDC = [43, 138, 62];
  const POSL = [242, 166, 156], NEGL = [208, 230, 251], NEG = [25, 113, 194], GLASSC = [238, 245, 249];
  const SAND = [217, 178, 106], SANDL = [241, 223, 181], GRAIN = [169, 122, 53], CURVE = [25, 113, 194];
  let narrow = false, sk = 1, fs = 13, H = 400, labels = [];
  let slQ1, slQ2, slR, lQ1, lQ2, lR, selAxis, selField, readout, marks = [];

  const params = () => ({ q1: Number(slQ1.value()), q2: Number(slQ2.value()), r: Number(slR.value()) });
  // the force in mN between point charges q1, q2 (nC) at r (cm)
  const force = (q1, q2, r) => K * Math.abs(q1 * q2) * 1e-18 / Math.pow(r * 0.01, 2) * 1000;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const bMark = p.createButton(__('merkitse')).parent(controls);
    bMark.elt.addEventListener('click', () => { const P = params(); marks.push({ key: P.q1 + '|' + P.q2, r: P.r, F: force(P.q1, P.q2, P.r) }); });
    const bClear = p.createButton(__('tyhjenna')).parent(controls);
    bClear.elt.addEventListener('click', () => { marks = []; });
    const l1 = p.createElement('label').parent(controls); lQ1 = p.createSpan('').parent(l1); slQ1 = p.createSlider(-40, 40, 20, 5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lQ2 = p.createSpan('').parent(l2); slQ2 = p.createSlider(-40, 40, 20, 5).parent(l2);
    const l3 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l3); slR = p.createSlider(3, 12, 6, 0.5).parent(l3);
    const la = p.createElement('label').parent(controls); p.createSpan(__('akseli')).parent(la); selAxis = p.createSelect().parent(la);
    selAxis.option(__('ax_r'), 'r'); selAxis.option(__('ax_inv'), 'inv'); selAxis.selected('r');
    const lf = p.createElement('label').parent(controls); p.createSpan(__('kentta')).parent(lf); selField = p.createSelect().parent(lf);
    selField.option(__('piilossa'), 'ei'); selField.option(__('nakyvissa'), 'kylla'); selField.selected('ei');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { q1: { input: slQ1.elt, unit: 'nC' }, q2: { input: slQ2.elt, unit: 'nC' }, r: { input: slR.elt, unit: 'cm' } },
      reset: () => { slQ1.value(20); slQ2.value(20); slR.value(6); selAxis.selected('r'); selField.selected('ei'); marks = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = params(), F = force(P.q1, P.q2, P.r), kind = P.q1 * P.q2 > 0 ? 1 : P.q1 * P.q2 < 0 ? -1 : 0;
    // signed x components (mN, + to the right): sphere 1 is on the left, so repulsion pushes it to the left
    const Fx1 = -kind * F, Fx2 = kind * F;
    lQ1.html(__('lbl_q1', { q: sgn(P.q1) })); lQ2.html(__('lbl_q2', { q: sgn(P.q2) })); lR.html(__('lbl_r', { r: tx(P.r, 1) }));
    readout.html(__('lukemat', { f1: fmt(F), f2: fmt(F) }) + '<br>' + __(kind > 0 ? 'hylkivat' : kind < 0 ? 'vetavat' : 'ei_voimaa'));
    const key = P.q1 + '|' + P.q2, mine = marks.filter((m) => m.key === key);
    window.simState = { q1: P.q1, q2: P.q2, r: P.r, F, F12: F, F21: F, Fx1, Fx2, kind, axis: selAxis.value(), field: selField.value() === 'kylla',
      marks: marks.length, shown: mine.length, narrow, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fs = narrow ? Math.round(14 * k) : 13;
    H = narrow ? 820 : 400;
    window.simState.narrow = narrow;
    if (p.__H !== H) { p.__H = H; p.resizeCanvas(600, H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    const L = layout();
    picture(P, F, kind, L);
    graph(P, F, mine, L);
    window.simState.labels = labels;
  };

  // rows of the picture and the graph box, from the font size (a phone draws larger labels)
  function layout() {
    const qy = 1.25 * fs, a2 = qy + 1.9 * fs, a1 = a2 + 1.9 * fs, R = 17 * (narrow ? 1.35 : 1);
    const ys = a1 + 0.9 * fs + R + 8, bench = ys + R + (narrow ? 70 : 54), rlab = bench + 22 * sk + 1.1 * fs;
    const gTop = rlab + 2.4 * fs, gy1 = gTop + 1.6 * fs, gy0 = H - 2.1 * fs;
    return { qy, a2, a1, R, ys, bench, rlab, gy1, gy0, gx0: narrow ? 120 : 80, gx1: narrow ? 470 : 500 };
  }

  // ---- the picture: bench, stands, spheres, force arrows ----
  function picture(P, F, kind, L) {
    const x1 = 150, x2 = x1 + PX * P.r, { ys, R, bench } = L;
    if (selField.value() === 'kylla') fieldLines(P, x1, x2, ys, R, bench);
    // the bench
    p.noStroke(); p.fill(...SANDL); p.rect(12, bench, 576, 16 * sk, 4);
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.noFill(); p.rect(12, bench, 576, 16 * sk, 4);
    p.stroke(...GRAIN); p.strokeWeight(1.2); p.line(20, bench + 8 * sk, 580, bench + 8 * sk);
    // the distance r between the centres, on the stands
    const yd = (ys + R + bench) / 2;
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.line(x1, yd, x2, yd);
    p.noStroke(); p.fill(...MUTEDC);
    p.triangle(x1 + 2, yd, x1 + 12, yd - 5, x1 + 12, yd + 5); p.triangle(x2 - 2, yd, x2 - 12, yd - 5, x2 - 12, yd + 5);
    lab(__('lbl_rc', { r: tx(P.r, 1) }), (x1 + x2) / 2, L.rlab, 'c', MUTEDC);
    for (const [x, q] of [[x1, P.q1], [x2, P.q2]]) {
      // an insulating glass stand on a dark base
      p.fill(...GLASSC); p.stroke(...INKC); p.strokeWeight(1.5 * sk); p.rect(x - 4 * sk, ys + R - 2, 8 * sk, bench - ys - R + 2);
      p.fill(108, 117, 125); p.rect(x - 22 * sk, bench - 8 * sk, 44 * sk, 8 * sk, 2);
      sphere(x, ys, R, q);
    }
    // the force arrows: sphere 1's on row a1, sphere 2's on row a2; the tails above the centres
    const len = Math.min(F * SCALE, CAP), cut = F * SCALE > CAP;
    p.stroke(...MUTEDC); p.strokeWeight(1.2 * sk); p.drawingContext.setLineDash([4 * sk, 4 * sk]);
    p.line(x1, ys - R - 3, x1, L.a1); p.line(x2, ys - R - 3, x2, L.a2); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(...INKC); p.circle(x1, L.a1, 6 * sk); p.circle(x2, L.a2, 6 * sk);
    if (kind !== 0) {
      const d1 = kind > 0 ? -1 : 1, d2 = -d1;
      arrow(x1, L.a1, d1, len, cut); arrow(x2, L.a2, d2, len, cut);
      lab('$\\overline{F}_{21}$', x1 - d1 * 10 * sk, L.a1 + 0.35 * fs, d1 > 0 ? 'r' : 'l', FORCE);
      lab('$\\overline{F}_{12}$', x2 - d2 * 10 * sk, L.a2 + 0.35 * fs, d2 > 0 ? 'r' : 'l', FORCE);
    }
    lab(__('c_q1', { q: sgn(P.q1) }), x1 + 8 * sk, L.qy, 'r');
    lab(__('c_q2', { q: sgn(P.q2) }), x2 - 8 * sk, L.qy, 'l');
    p.stroke(220); p.strokeWeight(1); p.line(8, L.rlab + 1.0 * fs, 592, L.rlab + 1.0 * fs);
  }
  function sphere(x, y, R, q) {
    const g = p.drawingContext.createRadialGradient(x - R * 0.35, y - R * 0.4, 1, x, y, R);
    const tint = q > 0 ? POSL : q < 0 ? NEG : [196, 204, 212];
    g.addColorStop(0, 'rgb(255,255,255)'); g.addColorStop(1, `rgb(${tint.join(',')})`);
    p.drawingContext.fillStyle = g; p.stroke(...INKC); p.strokeWeight(2.2 * sk);
    p.drawingContext.beginPath(); p.drawingContext.arc(x, y, R, 0, 2 * Math.PI); p.drawingContext.fill(); p.circle(x, y, 2 * R);
    p.noFill(); p.strokeWeight(2.4 * sk); p.stroke(...(q < 0 ? [255, 255, 255] : INKC));
    if (q !== 0) { p.line(x - R * 0.5, y, x + R * 0.5, y); if (q > 0) p.line(x, y - R * 0.5, x, y + R * 0.5); }
  }
  function arrow(x, y, d, len, cut) {
    if (len < 3) return;
    const hl = Math.min(14 * sk, len * 0.6), hw = 6 * sk, xe = x + d * len;
    p.stroke(...FORCE); p.strokeWeight(3.5 * sk); p.line(x, y, xe - d * hl * 0.9, y);
    p.noStroke(); p.fill(...FORCE); p.triangle(xe, y, xe - d * hl, y - hw, xe - d * hl, y + hw);
    if (cut) {                                              // the arrow is longer than drawn: a break mark
      const xm = x + d * len * 0.5;
      p.stroke(255); p.strokeWeight(4 * sk); p.line(xm - 4, y + 7 * sk, xm + 2, y - 7 * sk); p.line(xm + 4, y + 7 * sk, xm + 10, y - 7 * sk);
      p.stroke(...FORCE); p.strokeWeight(1.5 * sk); p.line(xm - 6, y + 7 * sk, xm, y - 7 * sk); p.line(xm + 6, y + 7 * sk, xm + 12, y - 7 * sk);
    }
  }
  // field lines of the two point charges, traced from every charge (forward from a positive, backward from a negative
  // one), their number proportional to |q|; a line from a negative charge that ends on the positive one is the same
  // line as one already drawn from the positive charge, so it is left out. Faint, with a small head along the field.
  function fieldLines(P, x1, x2, ys, R, bench) {
    const Q = [[x1, P.q1], [x2, P.q2]].filter((c) => c[1] !== 0);
    if (!Q.length) return;
    const starts = Q;
    const field = (x, y) => { let ex = 0, ey = 0; for (const [cx, q] of Q) { const dx = x - cx, dy = y - ys, r3 = Math.pow(dx * dx + dy * dy, 1.5) + 1e-9; ex += q * dx / r3; ey += q * dy / r3; } return [ex, ey]; };
    p.noFill(); p.stroke(...FIELDC, 200); p.strokeWeight(1.5 * sk);
    for (const [cx, q] of starts) {
      const n = Math.max(4, 2 * Math.round(Math.abs(q) / 5)), dir = q > 0 ? 1 : -1;
      for (let i = 0; i < n; i++) {
        const a = (i + 0.5) / n * 2 * Math.PI;
        let x = cx + (R + 2) * Math.cos(a), y = ys + (R + 2) * Math.sin(a);
        const pts = [[x, y]];
        let ends = false;
        for (let s = 0; s < 260; s++) {
          const [ex, ey] = field(x, y), m = Math.hypot(ex, ey);
          if (m === 0) break;
          x += dir * 4 * ex / m; y += dir * 4 * ey / m;
          if (x < 4 || x > 596 || y < 4 || y > bench - 2) break;
          if (Q.some(([qx]) => qx !== cx && Math.hypot(x - qx, y - ys) < R)) { ends = true; break; }
          pts.push([x, y]);
        }
        if (ends && q < 0 && Q.some((c) => c[1] > 0)) continue;   // drawn already from the positive charge
        p.beginShape(); for (const [a1, b1] of pts) p.vertex(a1, b1); p.endShape();
        if (pts.length > 12) {                              // a head halfway, pointing along the field
          const j = Math.min(pts.length - 2, 10), [ax, ay] = pts[j], [bx, by] = pts[j + 1];
          const ux = (bx - ax) * dir, uy = (by - ay) * dir, m = Math.hypot(ux, uy) || 1, u = [ux / m, uy / m], h = 6 * sk;
          p.push(); p.noStroke(); p.fill(...FIELDC, 230);
          p.triangle(ax + u[0] * h, ay + u[1] * h, ax - u[0] * h - u[1] * h * 0.7, ay - u[1] * h + u[0] * h * 0.7, ax - u[0] * h + u[1] * h * 0.7, ay - u[1] * h - u[0] * h * 0.7);
          p.pop();
        }
      }
    }
  }

  // ---- the graph: F against r or against 1/r² ----
  function graph(P, F, mine, L) {
    const inv = selAxis.value() === 'inv', { gx0, gx1, gy0, gy1 } = L;
    const xmax = inv ? 0.12 : 12, xstep = inv ? 0.02 : 2, X = (v) => gx0 + v / xmax * (gx1 - gx0);
    const top = Math.max(F, ...mine.map((m) => m.F)) * 1.04;
    const ymax = [0.5, 1, 2, 5, 10, 20].find((v) => v >= top) || 20, ystep = ymax / 5, Y = (v) => gy0 - v / ymax * (gy0 - gy1);
    const xv = (r) => (inv ? 1 / (r * r) : r);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let j = 1; j <= 6; j++) p.line(X(j * xstep), gy0, X(j * xstep), gy1);
    for (let j = 1; j <= 5; j++) p.line(gx0, Y(j * ystep), gx1, Y(j * ystep));
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(gx0, gy0, gx1 + 16 * sk, gy0); p.line(gx0, gy0, gx0, gy1 - 16 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(gx1 + 28 * sk, gy0, gx1 + 14 * sk, gy0 - 6 * sk, gx1 + 14 * sk, gy0 + 6 * sk);
    p.triangle(gx0, gy1 - 28 * sk, gx0 - 6 * sk, gy1 - 14 * sk, gx0 + 6 * sk, gy1 - 14 * sk);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let j = 1; j <= 6; j++) p.line(X(j * xstep), gy0, X(j * xstep), gy0 + 6 * sk);
    for (let j = 1; j <= 5; j++) p.line(gx0 - 6 * sk, Y(j * ystep), gx0, Y(j * ystep));
    const xd = inv ? 2 : 0, yd = ystep < 0.2 ? 1 : ystep < 1 ? 1 : 0;
    for (let j = 2; j <= 6; j += 2) lab('$' + tx(j * xstep, xd) + '$', X(j * xstep), gy0 + 8 * sk + fs, 'c');
    for (let j = 1; j <= 5; j += (narrow ? 2 : 1)) lab('$' + tx(j * ystep, yd) + '$', gx0 - 10 * sk, Y(j * ystep) + 0.35 * fs, 'r');
    lab('$0$', gx0 - 8 * sk, gy0 + 8 * sk + fs, 'r');
    lab(inv ? '$\\tfrac{1}{r^2}\\ (\\tfrac{1}{\\text{cm}^2})$' : '$r\\ (\\text{cm})$', gx1 + 30 * sk, gy0 + 0.35 * fs, 'l');
    lab('$F\\ (\\text{mN})$', gx0 + 12 * sk, gy1 - 22 * sk + 0.35 * fs, 'l');
    for (const m of mine) { p.fill(...INKC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(X(xv(m.r)), Y(m.F), 12 * sk); }
    if (F > 0) { p.fill(...FORCE); p.stroke(255); p.strokeWeight(2 * sk); p.circle(X(xv(P.r)), Y(F), 15 * sk); }
  }

  // every canvas text: its box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fs);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fs), H - 0.3 * fs);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fs, x1: x0 + w, y1: y + 0.25 * fs });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sgn = (q) => (q > 0 ? '+' : q < 0 ? '-' : '') + Math.abs(q);
  const fmt = (F) => tx(F, F >= 10 ? 1 : F >= 1 ? 2 : 3);
});
