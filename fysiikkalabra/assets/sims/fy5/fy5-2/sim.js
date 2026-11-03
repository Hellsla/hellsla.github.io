// fy5-2 Tasapaino kiertymisen suhteen: a uniform plank (4,0 m, 20 kg) rests on two supports at x1 and x2 (from its left
// end); a box of mass m_k sits on it at x_k. Model: the plank is rigid and at rest, so ΣF = 0 and ΣM = 0. Moments about
// support 1 (anticlockwise positive): N2 (x2 − x1) − G (2,0 m − x1) − F_k (x_k − x1) = 0, then N1 = G + F_k − N2, where
// G = m_L g is the plank's weight at its middle and F_k = m_k g the box's push on the plank (the box is at rest on it).
// A support can only push up: when the formula gives N1 < 0 or N2 < 0, the common centre of mass of plank and box
// lies outside the supports and the plank tips over the other support (drawn tipped, its far end on the floor).
// Top: the situation picture (tilannekuva), plank, box, two trestles and a floor scale in metres, with a dashed plumb
// line through the common centre of mass. Bottom: the force diagram (voimakuvio) of the plank alone, a plain
// rectangle aligned with the picture above, every force from its point of application, all to one scale for a given
// box mass (the scale shrinks with a heavier box so that the largest possible support force, G + F_k, still fits).
// No animation, so no speed control. On a narrow screen (#sim-root under 500 px) the two panels stack at the full
// 600 width. Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, L = 4.0, mL = 20, xL = 2.0;                              // m/s²; plank length (m), mass (kg), centre (m)
  const RED = [201, 42, 42], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GOODC = [43, 138, 62], HOTC = [201, 42, 42];
  let narrow = false, laid = false, OY = 0, U = 1, k = 1;
  const LAY = { sitH: 196, diaH: 204, X0: 60, PX: 120, cy: 100, room: 72 };   // panel heights, x of the plank's left end, px per m, plank centre, px for the largest force
  let slX1, slX2, slXk, selM, lX1, lX2, lXk, readout, labels = [];

  const model = () => {
    const x1 = Number(slX1.value()), x2 = Number(slX2.value()), xk = Number(slXk.value()), mk = Number(selM.value());
    const G = mL * g, Fk = mk * g;
    let N2 = (G * (xL - x1) + Fk * (xk - x1)) / (x2 - x1), N1 = G + Fk - N2;
    if (Math.abs(N1) < 1e-6) N1 = 0; if (Math.abs(N2) < 1e-6) N2 = 0;
    const xpp = (mL * xL + mk * xk) / (mL + mk);
    const tip = N1 < 0 ? 2 : N2 < 0 ? 1 : 0;                                // 2: tips over support 2, 1: over support 1
    const MG = -G * (xL - x1), Mk = -Fk * (xk - x1), M2 = N2 * (x2 - x1);  // moments about support 1 (Nm)
    return { x1, x2, xk, mk, G, Fk, N1, N2, xpp, tip, MG, Mk, M2 };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', () => reset());
    const l1 = p.createElement('label').parent(controls); lX1 = p.createSpan('').parent(l1); slX1 = p.createSlider(0, 1.8, 0.5, 0.1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lX2 = p.createSpan('').parent(l2); slX2 = p.createSlider(2.2, 4.0, 3.5, 0.1).parent(l2);
    const l3 = p.createElement('label').parent(controls); lXk = p.createSpan('').parent(l3); slXk = p.createSlider(0.2, 3.8, 1.0, 0.1).parent(l3);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    selM.option(__('ei_laatikkoa'), '0'); for (const m of ['10', '20', '40']) selM.option(m + ' kg', m);
    selM.selected('20');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    for (const e of [slX1.elt, slX2.elt, slXk.elt, selM.elt]) { e.addEventListener('input', () => p.redraw()); e.addEventListener('change', () => p.redraw()); }
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { x1: { input: slX1.elt, unit: 'm' }, x2: { input: slX2.elt, unit: 'm' }, xk: { input: slXk.elt, unit: 'm' }, mk: { input: selM.elt, unit: 'kg' } },
      reset: () => reset(),
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };
  function reset() { slX1.value(0.5); slX2.value(3.5); slXk.value(1.0); selM.selected('20'); p.redraw(); }

  p.draw = () => {
    const M = model();
    const cw = document.getElementById('sim-root').clientWidth || 600; k = Math.max(1, 600 / cw);
    const state = () => ({ x1: M.x1, x2: M.x2, xk: M.xk, mk: M.mk, mL, G: M.G, Fk: M.Fk, N1: M.N1, N2: M.N2, xpp: M.xpp,
      kaatuu: M.tip ? 1 : 0, yli: M.tip, MG: M.MG, Mk: M.Mk, M2: M.M2, sumM: M.tip ? null : M.M2 + M.MG + M.Mk, labels: [] });
    if (setLayout(cw < 500)) { window.simState = state(); p.redraw(); return; }   // the canvas was resized: draw on the next frame
    lX1.html(__('tuki1', { x: tx(M.x1, 1) })); lX2.html(__('tuki2', { x: tx(M.x2, 1) })); lXk.html(__('paikka', { x: tx(M.xk, 1) }));
    const tila = M.tip === 2 ? __('kaatuu2') : M.tip === 1 ? __('kaatuu1') : (M.N1 === 0 || M.N2 === 0) ? __('raja') : __('tasapaino');
    readout.html(M.tip ? __('lukemat_kaatuu', { G: tx(M.G, 1), F: tx(M.Fk, 1), x: tx(M.xpp, 2), tila: tila })
      : __('lukemat', { N1: tx(M.N1, 1), N2: tx(M.N2, 1), G: tx(M.G, 1), F: tx(M.Fk, 1), x: tx(M.xpp, 2), tila: tila,
                        M2: sg(M.M2), MG: sg(M.MG), Mk: sg(M.Mk) }));
    window.simState = state();
    U = narrow ? 0.8 * k : Math.max(1, k * 0.8);
    const fh = Math.round((narrow ? 14 : 13) * k);
    labels = [];
    p.background(250);
    OY = 0; p.push(); situation(M, fh); p.pop();
    OY = LAY.sitH; p.push(); p.translate(0, OY); diagram(M, fh); p.pop();
    window.simState.labels = labels;
  };

  // wide screen: the 600×400 picture; phone (the sim's box under 500 px): the two panels stacked at the full 600 width
  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) Object.assign(LAY, { sitH: 290, diaH: 330, X0: 44, PX: 110, cy: 172, room: 110 });
    else Object.assign(LAY, { sitH: 196, diaH: 204, X0: 60, PX: 120, cy: 100, room: 72 });
    p.resizeCanvas(600, LAY.sitH + LAY.diaH);
    return true;
  }
  const X = (x) => LAY.X0 + x * LAY.PX;
  const boxSize = (m) => { const q = narrow ? 1.25 : 1; return m >= 40 ? [48 * q, 40 * q] : m >= 20 ? [42 * q, 34 * q] : [36 * q, 28 * q]; };

  // --- the situation picture: wall, floor with a metre scale, two trestles, the plank and the box ---
  function situation(M, fh) {
    const H = LAY.sitH, FLOOR = H - (narrow ? 62 : 40), SUP = narrow ? 56 : 46, TH = narrow ? 15 : 12, yb = FLOOR - SUP;
    grect(0, 0, 600, FLOOR, [[236, 242, 247], [222, 230, 238]], 0);
    grect(0, FLOOR, 600, H - FLOOR, [[241, 223, 181], [233, 201, 138]], 0);
    p.stroke(...INKC); p.strokeWeight(2 * U); p.line(0, FLOOR, 600, FLOOR);
    // the floor scale in metres under the plank
    p.strokeWeight(1.5 * U); p.stroke(...MUTEDC);
    for (let i = 0; i <= 8; i++) { const x = X(i / 2); p.line(x, FLOOR, x, FLOOR + (i % 2 ? 5 : 9) * U); }
    const ny = FLOOR + 9 * U + fh * 0.95;
    for (let i = 0; i <= 4; i++) lab(`$${i}$`, X(i), ny, 'c', fh, MUTEDC);
    lab('$x\\ (\\text{m})$', X(4) + 14, ny, 'l', fh, INKC);
    // the trestles: wooden blocks with a numbered face
    for (const [x, nr] of [[M.x1, 1], [M.x2, 2]]) {
      const w = (narrow ? 34 : 28);
      grect(X(x) - w / 2, yb, w, SUP, [[200, 160, 95], [169, 122, 53]], 3);
      p.noStroke(); p.fill(246, 241, 230); p.rect(X(x) - w / 2 + 4 * U, yb + 6 * U, w - 8 * U, fh * 1.2, 2);
      lab(`$${nr}$`, X(x), yb + 6 * U + fh * 0.95, 'c', fh, INKC);
    }
    // the plank (and the box) in their frame: level, or tipped about the support it falls over
    p.push();
    if (M.tip) {
      const xs = M.tip === 2 ? M.x2 : M.x1, far = M.tip === 2 ? L - xs : xs, ang = Math.asin(Math.min(0.95, SUP / (far * LAY.PX)));
      p.translate(X(xs), yb); p.rotate(M.tip === 2 ? ang : -ang); p.translate(-X(xs), -yb);
    }
    grect(X(0), yb - TH, L * LAY.PX, TH, [[233, 201, 138], [200, 160, 95]], 2);
    p.stroke(169, 122, 53); p.strokeWeight(1 * U); for (let x = X(0) + 30; x < X(L) - 20; x += 64) p.line(x, yb - TH * 0.55, x + 30, yb - TH * 0.55);
    // the plank's own centre of mass: the quartered disc
    cmark(X(xL), yb - TH / 2, 6 * U);
    if (M.mk > 0) {
      const [bw, bh] = boxSize(M.mk), bx = X(M.xk);
      grect(bx - bw / 2, yb - TH - bh, bw, bh, [[217, 178, 106], [190, 150, 85]], 3);
      p.stroke(169, 122, 53); p.strokeWeight(1.5 * U); p.line(bx - bw / 2 + 3, yb - TH - bh + bh * 0.3, bx + bw / 2 - 3, yb - TH - bh + bh * 0.3);
    }
    p.pop();
    // the plumb line through the common centre of mass, down to the floor
    if (!M.tip) {
      const xp = X(M.xpp), top = narrow ? fh * 2.6 : fh * 2.2;
      p.stroke(...INKC); p.strokeWeight(1.5 * U); p.drawingContext.setLineDash([5 * U, 4 * U]); p.line(xp, top + fh * 0.5, xp, FLOOR); p.drawingContext.setLineDash([]);
      p.noStroke(); p.fill(...(M.xpp >= M.x1 && M.xpp <= M.x2 ? GOODC : HOTC)); p.circle(xp, FLOOR, 8 * U);
      place('$x_\\text{pp}$', [[xp, top, 'c'], [xp + 6, top + fh * 1.3, 'l'], [xp - 6, top + fh * 1.3, 'r']], fh, INKC);
    }
    lab(__('tilannekuva'), 8, narrow ? fh + 4 : 18, 'l', fh, INKC);
  }

  // --- the force diagram of the plank: a rectangle under the picture, every force from its point of application ---
  function diagram(M, fh) {
    // one force scale per box mass: the largest possible support force, the whole weight G + F_k, just fits
    const H = LAY.diaH, S = LAY.room / (M.G + M.Fk), TH = narrow ? 18 : 14, cy = LAY.cy, top = cy - TH / 2, bot = cy + TH / 2;
    p.noStroke(); p.fill(255); p.rect(0, 0, 600, H);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, 600, 0);
    lab(__('voimakuvio'), 8, narrow ? fh + 4 : 18, 'l', fh, INKC);
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(X(0), top, L * LAY.PX, TH);
    if (M.tip) { lab(__('ei_tasapainoa'), 300, cy + TH + fh * 1.8, 'c', fh, HOTC); return; }
    // labels go where they do not collide: weight first, then the pushes
    const xG = X(xL);
    arrow(xG, cy, xG, cy + M.G * S);                                         // weight from the centre (of mass), down
    if (M.Fk > 0) arrow(X(M.xk), top - M.Fk * S, X(M.xk), top);             // the box pushes down on the top face
    if (M.N1 > 0) arrow(X(M.x1), bot + M.N1 * S, X(M.x1), bot);             // the supports push up on the bottom face
    if (M.N2 > 0) arrow(X(M.x2), bot + M.N2 * S, X(M.x2), bot);
    // labels go where they do not collide: the supports' first (below their tails), then the weight on the side away
    // from the nearer support, then the box's push above its tail
    for (const [x, N, s] of [[M.x1, M.N1, '$\\overline{N}_1$'], [M.x2, M.N2, '$\\overline{N}_2$']]) {
      if (N <= 0) continue;
      const y = bot + N * S, away = x < xL ? -1 : 1;
      place(s, [[X(x) + away * 8, y + fh * 0.4, away < 0 ? 'r' : 'l'], [X(x), y + fh * 1.1, 'c'], [X(x) + away * 8, bot + fh, away < 0 ? 'r' : 'l'],
                [X(x) - away * 8, y + fh * 0.4, away < 0 ? 'l' : 'r']], fh, RED);
    }
    const gy = cy + M.G * S, side = (M.x2 - xL) < (xL - M.x1) ? -1 : 1, al = (sd) => (sd < 0 ? 'r' : 'l');
    place('$\\overline{G}$', [[xG + side * 8, gy - 2, al(side)], [xG + side * 8, gy + fh * 0.9, al(side)], [xG, gy + fh * 1.1, 'c'],
                               [xG - side * 8, gy - 2, al(-side)], [xG + side * 8, cy + TH / 2 + fh, al(side)]], fh, RED);
    if (M.Fk > 0) { const y = top - M.Fk * S; place('$\\overline{F}_\\text{k}$', [[X(M.xk), y - fh * 0.5, 'c'], [X(M.xk) + 8, y + fh * 0.5, 'l'], [X(M.xk) - 8, y + fh * 0.5, 'r'], [X(M.xk) + 8, top - fh * 0.5, 'l'], [X(M.xk) - 8, top - fh * 0.5, 'r']], fh, RED); }
  }
  function arrow(x1, y1, x2, y2) {
    const Ln = Math.hypot(x2 - x1, y2 - y1); if (Ln < 0.5) return;
    const a = Math.atan2(y2 - y1, x2 - x1), Hh = Math.min(11 * U, Math.max(Ln * 0.8, 5 * U));
    p.stroke(...RED); p.strokeWeight(3.2 * U);
    if (Ln > Hh * 0.8) p.line(x1, y1, x2 - Hh * 0.8 * Math.cos(a), y2 - Hh * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - Hh * Math.cos(a - 0.4), y2 - Hh * Math.sin(a - 0.4), x2 - Hh * Math.cos(a + 0.4), y2 - Hh * Math.sin(a + 0.4));
  }
  function cmark(x, y, r) {                                                // the centre-of-mass symbol: a disc in quarters
    p.stroke(...INKC); p.strokeWeight(1.2 * U); p.fill(255); p.circle(x, y, 2 * r);
    p.noStroke(); p.fill(...INKC); p.arc(x, y, 2 * r, 2 * r, -Math.PI / 2, 0); p.arc(x, y, 2 * r, 2 * r, Math.PI / 2, Math.PI);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function box(s, x, y, align, size) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    return { x0, y0: OY + y - 0.75 * size, x1: x0 + w, y1: OY + y + 0.25 * size, w };
  }
  function lab(s, x, y, align, size, col) {
    const b = box(s, x, y, align, size);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, b.x0, y);
    labels.push({ s, x0: b.x0, y0: b.y0, x1: b.x1, y1: b.y1 });
  }
  // the first candidate position whose box stays on the canvas and clear of the labels drawn so far
  function place(s, cands, size, col) {
    const lim = OY + (OY ? LAY.diaH : LAY.sitH);
    const cost = (b) => (b.x0 < 2 || b.x1 > 598 || b.y0 < OY + 2 || b.y1 > lim - 2 ? 1e6 : 0) +
      labels.reduce((sum, o) => sum + Math.max(0, Math.min(b.x1 + 4, o.x1 + 4) - Math.max(b.x0, o.x0)) * Math.max(0, Math.min(b.y1 + 3, o.y1 + 3) - Math.max(b.y0, o.y0)), 0);
    let best = cands[0], bc = Infinity;
    for (const c of cands) { const v = cost(box(s, c[0], c[1], c[2], size)); if (v < bc) { bc = v; best = c; } if (v === 0) break; }
    let c = best; const b = box(s, c[0], c[1], c[2], size);
    if (b.x0 < 2) c = [c[0] + 2 - b.x0, c[1], c[2]]; else if (b.x1 > 598) c = [c[0] - (b.x1 - 598), c[1], c[2]];
    lab(s, c[0], c[1], c[2], size, col);
  }
  function grect(x, y, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.3)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sg = (x) => (Math.abs(x) < 0.5 ? '0' : (x > 0 ? '+' : '-') + tx(Math.abs(x), 0));
});
