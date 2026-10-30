// fy4-13 Liikeyhtälö kytketyille kappaleille: two bodies joined by a light, inextensible string over a light, frictionless pulley.
// Situation 1 (karry): a cart m1 on a level table (no friction) is pulled by a hanging weight m2. Each body has its own equation:
// cart T = m1 a, weight m2 g − T = m2 a, so a = m2 g/(m1 + m2) and T = m1 m2 g/(m1 + m2) < m2 g.
// Situation 2 (kaksi): two bodies hang from the string; the heavier one falls, the lighter one rises, with the same acceleration:
// a = |m2 − m1| g/(m1 + m2) and T = 2 m1 m2 g/(m1 + m2), between the two weights. Air resistance and the pulley's mass are neglected.
// The run lasts until the bodies have moved 0,60 m (or never, if the masses in the second situation are equal). The speed select
// scales the simulated time only. The values (a, T, forces) are the model's, shown before the run too.
// Left (or top on a phone): the situation picture (tilannekuva) with the velocity (blue) and the acceleration (orange) beside the
// bodies, never forces. Right (or below): the force diagram (voimakuvio) of each body, a plain rectangle with every force from its
// point of application, all to one scale. On a phone (the sim's box under 500 px) the panels stack at the full 600 width.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, SMAX = 0.60, PX = 150;                                   // m/s²; the run length (m); px per metre in the situation picture
  const WHITE = [255, 255, 255], RED = [201, 42, 42], BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  const M1 = ['0.3', '0.5', '1', '1.5'], M2 = ['0.3', '0.5', '0.6', '1'];
  let laid = false, narrow = false, S = 5, SW = 380, OX = 0, OY = 0, U = 1, HD = 200, SC = 1, HS = 400;   // px per newton; scene width; offsets of the panel being drawn
  let btn, selTapa, selM1, selM2, selSpeed, readout;
  let t = 0, running = false, done = false, labels = [], SCL = 1;                 // SCL: the scale of the panel being drawn (the situation picture is enlarged on a phone)

  const model = () => {
    const kaksi = selTapa.value() === 'kaksi', m1 = Number(selM1.value()), m2 = Number(selM2.value());
    const M = m1 + m2, G1 = m1 * g, G2 = m2 * g;
    let a, T, sum1, sum2, dir;                                             // dir: +1 when the body on the right (m2) goes down, −1 when m1 does (second situation)
    if (!kaksi) { a = G2 / M; T = m1 * a; sum1 = T; sum2 = G2 - T; dir = 1; }
    else { dir = m2 >= m1 ? 1 : -1; a = Math.abs(m2 - m1) * g / M; T = 2 * m1 * m2 * g / M; sum1 = dir > 0 ? T - G1 : G1 - T; sum2 = dir > 0 ? G2 - T : T - G2; }
    return { kaksi, m1, m2, G1, G2, a, T, sum1, sum2, dir };
  };
  const restart = () => { t = 0; running = false; done = false; };
  const tEnd = (M) => (M.a > 1e-9 ? Math.sqrt(2 * SMAX / M.a) : 0);
  const fmtM = (m) => (m < 1 ? m.toFixed(2) : m.toFixed(1)).replace('.', DECP);

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { const M = model(); if (M.a < 1e-9) return; if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lt = p.createElement('label').parent(controls); p.createSpan(__('tapa')).parent(lt); selTapa = p.createSelect().parent(lt);
    selTapa.option(__('karry'), 'karry'); selTapa.option(__('kaksi'), 'kaksi');
    const l1 = p.createElement('label').parent(controls); p.createSpan('').parent(l1).html(__('m1')); selM1 = p.createSelect().parent(l1);
    for (const m of M1) selM1.option(fmtM(Number(m)) + ' kg', m);
    selM1.selected('1');
    const l2 = p.createElement('label').parent(controls); p.createSpan('').parent(l2).html(__('m2')); selM2 = p.createSelect().parent(l2);
    for (const m of M2) selM2.option(fmtM(Number(m)) + ' kg', m);
    selM2.selected('0.5');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.2'); selSpeed.option(__('normaali'), '0.4'); selSpeed.option(__('nopea'), '1'); selSpeed.selected('0.4');
    for (const e of [selTapa.elt, selM1.elt, selM2.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tapa: { input: selTapa.elt, unit: '' }, m1: { input: selM1.elt, unit: 'kg' }, m2: { input: selM2.elt, unit: 'kg' } },
      reset: () => { selTapa.selected('karry'); selM1.selected('1'); selM2.selected('0.5'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const M = model(), te = tEnd(M);
    if (running) {
      t = Math.min(t + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()), te);
      if (t >= te - 1e-9) { running = false; done = true; }
    }
    const s = M.a * t * t / 2, v = M.a * t;
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__(M.kaksi ? 'lukemat2' : 'lukemat1', { G1: tx(M.G1, 2), G2: tx(M.G2, 2), T: tx(M.T, 2), s1: tx(M.sum1, 2), s2: tx(M.sum2, 2), a: tx(M.a, 2), v: tx(v, 2), t: tx(t, 2) }));
    window.simState = { tapa: selTapa.value(), m1: M.m1, m2: M.m2, G1: M.G1, G2: M.G2, N: M.kaksi ? null : M.G1, T: M.T, a: M.a, sumF1: M.sum1, sumF2: M.sum2,
                        s, v, t, running, done, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    setLayout(cw < 500);
    U = narrow ? 0.8 * k : Math.max(1, k * 0.8);
    const fh = narrow ? Math.round(14 * k) : Math.round(11 * k * (k > 1.3 ? 1.12 : 1));   // phone: about 14 CSS px on screen
    labels = [];
    p.background(250);
    const U0 = U;
    OX = narrow ? (600 - SW * SC) / 2 : 0; OY = 0; U = U0 / SC; SCL = SC; p.push(); p.translate(OX, OY); p.scale(SC); situation(M, s, v, fh / SC); p.pop();
    U = U0; OX = 0; SCL = 1; diagrams(M, fh);
    window.simState.labels = labels;
  };

  // wide screen: the 600×400 picture; phone (the sim's box under 500 px): the panels stacked at the full 600 width, so labels stay readable
  function setLayout(n) {
    if (n === narrow && laid) return;
    laid = true; narrow = n;
    if (n) { S = 6; HD = 250; SC = 1.35; HS = Math.round(400 * SC); p.resizeCanvas(600, HS + 2 * HD); }
    else { S = 5; HD = 200; SC = 1; HS = 400; p.resizeCanvas(600, 400); }
  }

  // --- the situation picture: lab wall, table (or ceiling), pulley, string, cart and weights; v and a beside the moving bodies ---
  function situation(M, s, v, fh) {
    grect(0, 0, SW, 372, [[240, 244, 248], [225, 232, 240]], 0);
    grect(0, 372, SW, 28, [[233, 201, 138], [217, 178, 106]], 0);
    const sp = s * PX;
    if (!M.kaksi) {
      const TOP = 200, PXC = 304, PYC = 184, PR = 13;
      grect(14, TOP, 284, 14, [[217, 178, 106], [190, 150, 80]], 2);                          // the table top
      grect(30, TOP + 14, 16, 158, [[205, 165, 92], [180, 140, 72]], 2); grect(236, TOP + 14, 16, 158, [[205, 165, 92], [180, 140, 72]], 2);
      p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(0, 372, SW, 372);
      p.stroke(120); p.strokeWeight(5 * U); p.line(PXC - 8, TOP + 3, PXC - 8, PYC + 4);       // the clamp rod
      pulley(PXC, PYC, PR);
      const cx = 56 + sp, cr = cx + 64;                                                        // the cart: left end and right end
      grect(cx, TOP - 35, 64, 21, [[150, 190, 228], [74, 120, 170]], 3);
      p.noStroke(); p.fill(...INKC); p.circle(cx + 14, TOP - 8, 16); p.circle(cx + 50, TOP - 8, 16);
      p.fill(196, 204, 212); p.circle(cx + 14, TOP - 8, 6); p.circle(cx + 50, TOP - 8, 6);
      const nb = { 0.3: 0, 0.5: 1, 1: 2, 1.5: 3 }[M.m1];
      for (let i = 0; i < nb; i++) grect(cx + 10 + (i % 2) * 22, TOP - 47 - Math.floor(i / 2) * 12, 20, 12, [[170, 176, 182], [100, 106, 112]], 1);
      const hh = 20 + 22 * M.m2, hy = 232 + sp;                                                // the hanging weight
      p.stroke(120, 90, 50); p.strokeWeight(2 * U); p.noFill();
      p.line(cr, TOP - 29, PXC, TOP - 29); p.arc(PXC, PYC, 2 * PR, 2 * PR, -p.HALF_PI, 0); p.line(PXC + PR, PYC, PXC + PR, hy);
      grect(PXC + PR - 18, hy, 36, hh, [[170, 176, 182], [100, 106, 112]], 3);
      lab('$m_1$', cx + 32, TOP - 21 + fh * 0.36, 'c', fh, WHITE); lab('$m_2$', PXC + PR, hy + hh / 2 + fh * 0.36, 'c', fh, WHITE);
      motion(cx + 32, 112, v, 22, BLUE, '$\\overline{v}$', fh);
      if (t > 0) motion(cx + 32, 84, M.a, 12, ORANGE, '$\\overline{a}$', fh);
      if (t > 0) fallArrows(PXC + PR + 24, hy, hh, v, M.a, fh, 1);
    } else {
      const PCX = 190, PCY = 66, PR = 28, X1 = PCX - PR, X2 = PCX + PR;
      p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(0, 372, SW, 372);
      grect(120, 8, 140, 12, [[150, 156, 162], [110, 116, 122]], 2);                          // the ceiling bracket
      p.stroke(110); p.strokeWeight(5 * U); p.line(PCX, 20, PCX, PCY);
      pulley(PCX, PCY, PR);
      const h1 = 18 + 22 * M.m1, h2 = 18 + 22 * M.m2;
      const y1 = 200 - M.dir * sp, y2 = 200 + M.dir * sp;                                      // tops of the bodies: m2 down for dir = +1
      p.stroke(120, 90, 50); p.strokeWeight(2 * U); p.noFill();
      p.line(X1, PCY, X1, y1); p.line(X2, PCY, X2, y2); p.arc(PCX, PCY, 2 * PR, 2 * PR, p.PI, 2 * p.PI);
      grect(X1 - 18, y1, 36, h1, [[170, 176, 182], [100, 106, 112]], 3);
      grect(X2 - 18, y2, 36, h2, [[170, 176, 182], [100, 106, 112]], 3);
      lab('$m_1$', X1, y1 + h1 / 2 + fh * 0.36, 'c', fh, WHITE); lab('$m_2$', X2, y2 + h2 / 2 + fh * 0.36, 'c', fh, WHITE);
      if (t > 0 && M.a > 1e-9) { fallArrows(X1 - 32, y1, h1, M.dir > 0 ? -v : v, M.dir > 0 ? -M.a : M.a, fh, -1); fallArrows(X2 + 32, y2, h2, M.dir > 0 ? v : -v, M.dir > 0 ? M.a : -M.a, fh, 1); }
    }
    lab(__('tilannekuva'), 10, narrow ? fh + 2 : 22, 'l', fh, INKC);
    lab(`$t = ${tx(t, 2)}\\,\\text{s}$`, SW - 8, narrow ? fh + 2 : 22, 'r', fh, INKC);
  }
  // a horizontal thin arrow with an open head, in the situation picture (positive = right)
  function motion(x0, y, val, scale, col, name, fh) {
    if (Math.abs(val) < 0.02) return;
    const L = Math.max(10, Math.min(Math.abs(val) * scale, 120)), x2 = x0 + Math.sign(val) * L;
    p.stroke(...col); p.strokeWeight(2.5 * U); p.line(x0, y, x2, y);
    p.line(x2, y, x2 - Math.sign(val) * 8 * U, y - 5 * U); p.line(x2, y, x2 - Math.sign(val) * 8 * U, y + 5 * U);
    lab(name, x2 + Math.sign(val) * 6, y + fh * 0.36, val > 0 ? 'l' : 'r', fh, col);
  }
  // vertical thin arrows beside a hanging body: velocity (blue, nearer the body) and acceleration (orange); val > 0 downward
  function fallArrows(x, y, h, v, a, fh, side) {
    const yc = y + h / 2;
    const arr = (xx, val, scale, col, name) => {
      if (Math.abs(val) < 0.02) return;
      const L = Math.max(10, Math.min(Math.abs(val) * scale, 44)), d = Math.sign(val), y2 = yc + d * L;
      p.stroke(...col); p.strokeWeight(2.5 * U); p.line(xx, yc, xx, y2);
      p.line(xx, y2, xx - 5 * U, y2 - d * 8 * U); p.line(xx, y2, xx + 5 * U, y2 - d * 8 * U);
      lab(name, xx, d > 0 ? y2 + 6 + fh * 0.8 : y2 - 6, 'c', fh, col);
    };
    arr(x, v, 16, BLUE, '$\\overline{v}$'); arr(x + side * 24, a, 9, ORANGE, '$\\overline{a}$');
  }
  function pulley(x, y, r) {
    p.stroke(...INKC); p.strokeWeight(2 * U); p.fill(196, 204, 212); p.circle(x, y, 2 * r);
    p.fill(255); p.stroke(138, 150, 163); p.strokeWeight(1.5 * U); p.circle(x, y, 2 * r - 10);
    p.fill(...INKC); p.noStroke(); p.circle(x, y, 5);
  }

  // --- the force diagrams: each body a plain rectangle, every force from its point of application, one scale for both ---
  function diagrams(M, fh) {
    const x0 = narrow ? 0 : 380, w = narrow ? 600 : 220, cx = x0 + w / 2 + (narrow ? 70 : 10), y0 = narrow ? HS : 0;
    for (const [i, top] of [[1, y0], [2, y0 + HD]]) {
      OX = 0; OY = top;
      p.push(); p.translate(0, top);
      p.noStroke(); p.fill(255); p.rect(x0, 0, w, HD);
      p.stroke(220); p.strokeWeight(1); p.line(x0, 0, x0 + w, 0); if (!narrow) p.line(x0, 0, x0, HD);
      const title = i === 1 ? (M.kaksi ? '$\\text{Voimakuvio: }m_1$' : __('vk1')) : (M.kaksi ? '$\\text{Voimakuvio: }m_2$' : __('vk2'));
      lab(title, x0 + 10, narrow ? fh + 2 : 22, 'l', fh, INKC);
      if (i === 1 && !M.kaksi) cartDiagram(M, cx, narrow ? 120 : 108, fh);
      else hangDiagram(M, i, cx, narrow ? 145 : 116, fh);
      p.pop();
    }
    OX = 0; OY = 0;
  }
  function cartDiagram(M, cx, cy, fh) {
    const w = 56, h = 26, lo = 12 + fh * 0.7;
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(cx - w / 2, cy - h / 2, w, h);
    arrow([cx, cy], [0, -M.G1], '$\\overline{G}_1$', fh, [0, fh * 0.9 + 4]);
    arrow([cx - 18, cy + h / 2], [0, M.G1], '$\\overline{N}$', fh, [-lo, 0]);
    arrow([cx + w / 2, cy - 4], [M.T, 0], '$\\overline{T}_1$', fh, [lo, -fh * 0.1]);
  }
  function hangDiagram(M, i, cx, cy, fh) {
    const w = 36, h = 28, lo = 28 + fh * 0.3, G = i === 1 ? M.G1 : M.G2, sub = i === 1 ? '1' : '2';
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2 * U); p.rect(cx - w / 2, cy - h / 2, w, h);
    arrow([cx, cy], [0, -G], `$\\overline{G}_${sub}$`, fh, [lo, fh * 0.6]);
    arrow([cx, cy - h / 2], [0, M.T], `$\\overline{T}_${sub}$`, fh, [lo, -fh * 0.3]);
  }
  function arrow(at, vec, name, fh, off) {
    const x2 = at[0] + vec[0] * S, y2 = at[1] - vec[1] * S, L = Math.hypot(x2 - at[0], y2 - at[1]);
    if (L < 1) return;
    const a = Math.atan2(y2 - at[1], x2 - at[0]), H = Math.min(11 * U, L * 0.7);
    p.stroke(...RED); p.strokeWeight(3.5 * U); p.line(at[0], at[1], x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
    lab(name, x2 + off[0], y2 + off[1] + fh * 0.36, 'c', fh, RED);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0: OX + x0 * SCL, y0: OY + (y - 0.75 * size) * SCL, x1: OX + (x0 + w) * SCL, y1: OY + (y + 0.25 * size) * SCL });
  }
  function grect(x, y, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const DECP = DEC === '.' ? '.' : ',';
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
