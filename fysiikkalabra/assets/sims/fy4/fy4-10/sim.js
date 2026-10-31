// fy4-10 Liikemäärän säilyminen ja yksiulotteiset törmäykset: two gliders on a level air track. The physics is in
// model.js (window.FY410Model, tested by tests/models/fy4-10.test.js): equal and opposite bumper forces, the energy the
// bumpers hold (E_p) and the energy they turn into internal energy (E_sis), so E_k + E_p + E_sis stays the starting
// energy; the velcro case truly sticks, the explosion starts with the spring's 0,24 J. This file only draws the state.
// Top: the track with the gliders, velocity arrows (blue) above and momentum arrows (purple) below the beam, every arrow
// from its own glider, its length to one scale for the whole run and its direction the sign of the quantity; while the
// gliders touch, the bumper forces (red): F_1 on glider 1 to the left and F_2 on glider 2 to the right, equal in size.
// The arrow scales are chosen when the run is set, by playing it ahead to its "after" values, so no arrow tip leaves the
// picture before or during the collision; after it the run ends before an arrow would leave, so none is cut or moved.
// Bottom (stacked on a phone): momentum bars (signed, zero line in the middle) for glider 1, glider 2 and the total, and
// an energy column before and now: E_k (the gliders' kinetic energy), E_p (in the bumper or spring) and E_sis (internal),
// stacked, with the starting total as a dashed line, so the column stays as tall while energy changes form.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const MD = window.FY410Model, L = MD.L, DT = 0.0002, TRACK = MD.TRACK;
  const BLUE = [25, 113, 194], PURPLE = [112, 72, 232], PURPLE_L = [197, 184, 248], PURPLE_M = [150, 124, 240], RED = [201, 42, 42],
    INKC = [31, 41, 51], MUTEDC = [107, 116, 128], EK = [43, 138, 62], EP = [214, 170, 36], ESIS = [150, 100, 70];
  let laid = false, narrow = false, OX = 0, OY = 0, U = 1, fh = 13, labels = [];
  // panels (canvas coordinates within the panel); the wide layout first, setLayout() switches
  const TR = { w: 600, h: 215, t: 18, v2: 34, v1: 58, beam: 140, p1: 176, p2: 200, gh: 50 };
  const CH = { w: 300, h: 185, title: 16, glab: 36, top: 46, bot: 150, name: 172 };
  let btn, slV1, lV1, slV2, lV2, selM1, selM2, selT, selSpeed, readout;
  let R = null, B = null, running = false, Pb = null, FIT = { v: Infinity, p: Infinity };

  const M = () => ({ m1: Number(selM1.value()), m2: Number(selM2.value()), typ: selT.value(), v1: Number(slV1.value()), v2: Number(slV2.value()) });
  function restart() {
    const S = M();
    R = MD.create(S.typ, S.m1, S.m2, S.v1, S.v2); B = MD.bounds(S.typ, S.m1, S.m2, S.v1, S.v2); running = false;
    Pb = { p1: R.m1 * R.w1, p2: R.m2 * R.w2 };
    FIT = fitRun(S);
    const rj = S.typ === 'rajahdys';
    for (const s of [slV1, slV2]) if (s) s.elt.disabled = rj || !!s.elt.closest('label')?.classList.contains('locked');
  }
  // arrow lengths (px) per m/s, kg·m/s and N: one scale for the whole run, so the longest arrow fits on its row and,
  // up to the "after" values, every arrow tip stays inside the track picture (fitRun)
  const VS = () => Math.min((narrow ? 130 : 110) / (1.05 * B.V), FIT.v), PS = () => Math.min((narrow ? 130 : 110) / (1.05 * B.P), FIT.p),
    FS = () => (narrow ? 110 : 90) / (1.05 * B.F);
  // the run played ahead once when it is set: the largest arrow scales that keep each tip inside until the collision is over
  function fitRun(S) {
    const T = MD.create(S.typ, S.m1, S.m2, S.v1, S.v2), fit = { v: Infinity, p: Infinity };
    const room = (x, val) => Math.abs(val) < 1e-9 ? Infinity : (val > 0 ? TR.w - 6 - X(x) : X(x) - 6) / Math.abs(val);
    for (let n = 0; n < 200000 && !T.done; n++) {
      fit.v = Math.min(fit.v, room(T.x1, T.w1), room(T.x2, T.w2));
      fit.p = Math.min(fit.p, room(T.x1, T.m1 * T.w1), room(T.x2, T.m2 * T.w2));
      if (T.after !== null && (T.stuck || MD.overlap(T) <= 0)) break;
      MD.step(T, DT);
    }
    return { v: fit.v * 0.98, p: fit.p * 0.98 };
  }
  const SX = () => (TR.w - 40) / TRACK, X = (x) => 20 + x * SX();
  // the run ends when a glider reaches an end of the track or an arrow's tip would leave the picture
  function outside() {
    for (const [x, len] of [[R.x1, R.w1 * VS()], [R.x2, R.w2 * VS()], [R.x1, R.m1 * R.w1 * PS()], [R.x2, R.m2 * R.w2 * PS()]]) {
      const tip = X(x) + len; if (tip < 6 || tip > TR.w - 6) return true;
    }
    return false;
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (R.done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lt = p.createElement('label').parent(controls); p.createSpan(__('tyyppi')).parent(lt); selT = p.createSelect().parent(lt);
    for (const k of ['kimmoisa', 'kimmoton', 'tarra', 'rajahdys']) selT.option(__(k), k);
    selT.selected('kimmoisa');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('massa1')).parent(l1); selM1 = p.createSelect().parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('massa2')).parent(l2); selM2 = p.createSelect().parent(l2);
    for (const s of [selM1, selM2]) { for (const m of ['0.2', '0.4', '0.6']) s.option((DEC === '.' ? m : m.replace('.', ',')) + '0 kg', m); s.selected('0.4'); }
    const lv1 = p.createElement('label').parent(controls); lV1 = p.createSpan('').parent(lv1); slV1 = p.createSlider(0, 1, 0.6, 0.1).parent(lv1);
    const lv2 = p.createElement('label').parent(controls); lV2 = p.createSpan('').parent(lv2); slV2 = p.createSlider(-1, 1, 0, 0.1).parent(lv2);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.1'); selSpeed.option(__('normaali'), '0.4'); selSpeed.option(__('nopea'), '1'); selSpeed.selected('0.4');
    for (const e of [slV1.elt, slV2.elt, selM1.elt, selM2.elt, selT.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    window.addEventListener('resize', () => p.redraw());
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tyyppi: { input: selT.elt, unit: '' }, m1: { input: selM1.elt, unit: 'kg' }, m2: { input: selM2.elt, unit: 'kg' },
                v1: { input: slV1.elt, unit: 'm/s' }, v2: { input: slV2.elt, unit: 'm/s' } },
      reset: () => { selT.selected('kimmoisa'); selM1.selected('0.4'); selM2.selected('0.4'); slV1.value(0.6); slV2.value(0); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    setLayout(cw < 500);
    if (running) {
      let left = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
      while (left > 1e-9 && running) {
        const d = Math.min(DT, left); MD.step(R, d); left -= d;
        if (R.after !== null && outside()) R.done = true;   // before that the scales keep every tip inside (fitRun)
        if (R.done) running = false;
      }
    }
    const S = R, E = MD.energies(S), p1 = S.m1 * S.w1, p2 = S.m2 * S.w2, af = S.after;
    const pJ = af ? S.m1 * af.u1 + S.m2 * af.u2 : null, EkJ = af ? 0.5 * S.m1 * af.u1 ** 2 + 0.5 * S.m2 * af.u2 ** 2 : null;
    const Ek0 = 0.5 * S.m1 * S.v1 ** 2 + 0.5 * S.m2 * S.v2 ** 2, Ep0 = S.E0 - Ek0;
    lV1.html(__('v1', { v: tx(Number(slV1.value()), 1) }));
    lV2.html(__('v2', { v: tx(Number(slV2.value()), 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const dots = '\\ldots';
    readout.html(__('lukemat', { p0: tx(S.P0, 3), E0: tx(Ek0, 3), Ep0: tx(Ep0, 3),
      u1: af ? tx(af.u1, 2) : dots, u2: af ? tx(af.u2, 2) : dots, pJ: af ? tx(pJ, 3) : dots, EJ: af ? tx(EkJ, 3) : dots,
      t: tx(S.t, 2), w1: tx(S.w1, 2), w2: tx(S.w2, 2), p: tx(p1 + p2, 3), E: tx(E.Ek, 3), Ep: tx(E.Ep, 3), Es: tx(E.Esis, 3),
      Et: tx(E.Ek + E.Ep + E.Esis, 3) }));
    window.simState = { tyyppi: S.typ, m1: S.m1, m2: S.m2, v1: S.v1, v2: S.v2, t: S.t, x1: S.x1, x2: S.x2, w1: S.w1, w2: S.w2, F: S.F, p1, p2,
      p: p1 + p2, Ek: E.Ek, Ep: E.Ep, Esis: E.Esis, Etot: E.Ek + E.Ep + E.Esis, E0: S.E0, Ep0,
      p0: S.P0, Ek0, u1: af ? af.u1 : null, u2: af ? af.u2 : null, pJ, EkJ,
      dEk: af ? EkJ - Ek0 : null, contact: S.contact, stuck: S.stuck, running, done: S.done, labels: null };
    U = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;   // phone: about 14 CSS px on screen
    labels = [];
    p.background(250);
    OX = 0; OY = 0; p.push(); trackPanel(S); p.pop();
    if (narrow) {
      OX = 0; OY = TR.h; p.push(); p.translate(OX, OY); pChart(S, p1, p2); p.pop();
      OX = 0; OY = TR.h + CH.h; p.push(); p.translate(OX, OY); eChart(S, E); p.pop();
    } else {
      OX = 0; OY = TR.h; p.push(); p.translate(OX, OY); pChart(S, p1, p2); p.pop();
      OX = 300; OY = TR.h; p.push(); p.translate(OX, OY); eChart(S, E); p.pop();
    }
    window.simState.labels = labels;
  };

  // wide screen: the track on top, the two charts side by side under it in 600×400; phone (the sim's box under 500 px):
  // the track and the two charts stacked at full width
  function setLayout(n) {
    if (n === narrow && laid) return;
    laid = true; narrow = n;
    if (n) {
      Object.assign(TR, { h: 330, t: 26, v2: 60, v1: 98, beam: 222, p1: 268, p2: 306, gh: 72 });
      Object.assign(CH, { w: 600, h: 250, title: 30, glab: 66, top: 80, bot: 196, name: 232 });
      p.resizeCanvas(600, TR.h + 2 * CH.h);
    } else {
      Object.assign(TR, { h: 215, t: 18, v2: 34, v1: 58, beam: 140, p1: 176, p2: 200, gh: 50 });
      Object.assign(CH, { w: 300, h: 185, title: 16, glab: 36, top: 46, bot: 150, name: 172 });
      p.resizeCanvas(600, 400);
    }
  }

  // --- the track: the air track, the gliders with their bumpers, velocity and momentum arrows, contact forces ---
  function trackPanel(S) {
    grect(0, 0, TR.w, TR.h, [[238, 245, 249], [250, 250, 250]], 0);
    const by = TR.beam, bh = 12 * U;
    grect(20, by, TR.w - 40, bh, [[214, 220, 226], [160, 170, 180]], 2 * U);
    p.noStroke(); p.fill(138, 150, 163); for (let x = 32; x < TR.w - 24; x += 16 * U) p.circle(x, by + bh / 2, 2.6 * U);
    p.fill(...INKC); p.rect(14, by - 18 * U, 6, 18 * U + bh); p.rect(TR.w - 20, by - 18 * U, 6, 18 * U + bh);   // end stops
    const d = MD.overlap(S);
    glider(S.x1, S.m1, [241, 223, 181], 1, S, d);
    glider(S.x2, S.m2, [196, 204, 212], 2, S, d);
    // the bumper forces, from the contact surface: F_1 on glider 1 (left), F_2 on glider 2 (right), equal lengths
    if (S.F > 0.05) {
      const cx = X((S.x1 + S.x2) / 2), cy = by - 2 * U - 0.25 * TR.gh, Lf = Math.max(14 * U, S.F * FS()), gap = 4 * U;
      arrow(cx, cy, cx - Lf, cy, RED, 4 * U); arrow(cx, cy, cx + Lf, cy, RED, 4 * U);
      lab('$\\overline{F}_1$', cx - Lf - gap, cy - 8 * U, 'r', RED);
      lab('$\\overline{F}_2$', cx + Lf + gap, cy - 8 * U, 'l', RED);
    }
    // velocity (blue) above, momentum (purple) below the beam; each glider on its own row
    vec(X(S.x1), TR.v1, S.w1 * VS(), BLUE, '\\overline{v}_1');
    vec(X(S.x2), TR.v2, S.w2 * VS(), BLUE, '\\overline{v}_2');
    vec(X(S.x1), TR.p1, S.m1 * S.w1 * PS(), PURPLE, '\\overline{p}_1');
    vec(X(S.x2), TR.p2, S.m2 * S.w2 * PS(), PURPLE, '\\overline{p}_2');
    lab(`$t = ${tx(S.t, 2)}\\,\\text{s}$`, 10, TR.t + fh * 0.35, 'l', INKC);
  }
  function glider(x, m, col, num, S, d) {
    const s = SX(), by = TR.beam, h = TR.gh * (0.55 + 0.75 * m), bump = MD.BUMP, bodyL = (L - 2 * bump) * s;
    const cx = X(x);
    grect(cx - bodyL / 2, by - h - 2 * U, bodyL, h, [col, col.map((c) => c * 0.82)], 3 * U);
    p.noStroke(); p.fill(138, 150, 163); p.rect(cx - bodyL / 2 + 3, by - 4 * U, bodyL - 6, 4 * U);
    // mass discs: one per 0,20 kg on top of the glider
    const nd = Math.round(m / 0.2);
    for (let i = 0; i < nd; i++) { p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(1); p.rect(cx - bodyL * 0.3, by - h - 2 * U - (i + 1) * 5 * U, bodyL * 0.6, 4 * U, 1); }
    lab(`$${num}$`, cx, by - 2 * U - h + fh * 1.1, 'c', INKC);
    // the facing bumper: compressed by half the overlap each
    const len = Math.max(0.004, bump - d / 2) * s, cy = by - 2 * U - 0.25 * TR.gh, x0 = num === 1 ? cx + bodyL / 2 : cx - bodyL / 2, dir = num === 1 ? 1 : -1;
    if (S.typ === 'kimmoisa' || S.typ === 'rajahdys') {
      p.noFill(); p.stroke(108, 117, 125); p.strokeWeight(1.8 * U); p.beginShape();
      for (let i = 0; i <= 8; i++) p.vertex(x0 + dir * len * i / 8, cy + (i % 2 ? 6 : -6) * U * (i === 0 || i === 8 ? 0 : 1));
      p.endShape();
    } else if (S.typ === 'kimmoton') {
      p.noStroke(); p.fill(169, 122, 53); p.rect(Math.min(x0, x0 + dir * len), cy - 8 * U, len, 16 * U, 4 * U);
    } else {
      p.noStroke(); p.fill(55, 65, 75); p.rect(Math.min(x0, x0 + dir * len), cy - 10 * U, len, 20 * U);
    }
  }
  function vec(x, y, len, col, name) {           // an arrow of signed length len from its glider on the row y, its label at the tip
    if (Math.abs(len) < 4 * U) return;
    const xt = x + len;
    arrow(x, y, xt, y, col, 3 * U);
    p.textSize(fh); const tw = p.textWidth(`$${name}$`), gap = 6 * U;
    let lx = len > 0 ? xt + gap : xt - gap - tw;
    if (lx < 4 || lx + tw > TR.w - 4) lx = len > 0 ? x - gap - tw : x + gap;   // no room beyond the tip: the label behind the tail
    lab(`$${name}$`, lx, y + fh * 0.35, 'l', col);
  }
  function arrow(x1_, y1_, x2_, y2_, col, sw) {
    const a = Math.atan2(y2_ - y1_, x2_ - x1_), hd = 10 * U;
    p.stroke(...col); p.strokeWeight(sw); p.line(x1_, y1_, x2_ - hd * 0.8 * Math.cos(a), y2_ - hd * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2_, y2_, x2_ - hd * Math.cos(a - 0.42), y2_ - hd * Math.sin(a - 0.42), x2_ - hd * Math.cos(a + 0.42), y2_ - hd * Math.sin(a + 0.42));
  }

  // --- momentum: signed bars (zero line in the middle) of glider 1, glider 2 and the total, before and now, one scale ---
  function pChart(S, a1, a2) {
    p.noStroke(); p.fill(255); p.rect(0, 0, CH.w, CH.h);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, CH.w, 0);
    lab(`$p\\ (\\text{kg}\\cdot\\text{m/s})$`, 10, CH.title, 'l', PURPLE);
    const zero = (CH.top + CH.bot) / 2, span = (CH.bot - CH.top) / 2, sc = span / (1.1 * B.P);
    const groups = [[Pb.p1, Pb.p2, Pb.p1 + Pb.p2], [a1, a2, a1 + a2]], cols = [PURPLE_L, PURPLE_M, PURPLE];
    const names = ['p_1', 'p_2', `p_\\text{${__('kok')}}`];
    const gw = CH.w / 2, bw = Math.min(34 * U, gw / 5);
    groups.forEach((vals, g) => {
      const xs = [0.2, 0.5, 0.8].map((f) => g * gw + f * gw);
      vals.forEach((v, i) => {
        const hgt = Math.max(-span, Math.min(span, v * sc));
        p.noStroke(); p.fill(...cols[i]); p.rect(xs[i] - bw / 2, Math.min(zero, zero - hgt), bw, Math.abs(hgt));
        lab(`$${names[i]}$`, xs[i], CH.name, 'c', INKC);
      });
      lab(g === 0 ? `$\\text{${__('ennen')}}$` : `$\\text{${__('nyt')}}$`, g * gw + gw / 2, CH.glab, 'c', MUTEDC);
    });
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(8, zero, CH.w - 8, zero);
    p.noStroke(); lab('$+$', 4, CH.top + fh * 0.4, 'l', MUTEDC); lab('$-$', 4, CH.bot, 'l', MUTEDC);
    p.stroke(220); p.strokeWeight(1); p.line(CH.w / 2, CH.top, CH.w / 2, CH.bot);
  }

  // --- energy: one stacked column before and one now, E_k + E_p + E_sis, one scale; the starting total dashed ---
  function eChart(S, E) {
    p.noStroke(); p.fill(255); p.rect(0, 0, CH.w, CH.h);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, CH.w, 0); if (!narrow) p.line(0, 0, 0, CH.h);
    lab(`$E\\ (\\text{J})$`, 10, CH.title, 'l', EK);
    const span = CH.bot - CH.top, sc = span / (1.1 * B.E), bw = Math.min(46 * U, CH.w * 0.15);
    const Ek0 = 0.5 * S.m1 * S.v1 ** 2 + 0.5 * S.m2 * S.v2 ** 2;
    const cols = [[Ek0, S.E0 - Ek0, 0], [E.Ek, E.Ep, E.Esis]], xs = [CH.w * 0.2, CH.w * 0.45];
    cols.forEach((vals, g) => {
      let y = CH.bot;
      vals.forEach((v, i) => { const hgt = Math.max(0, v) * sc; if (hgt > 0.2) { p.noStroke(); p.fill(...[EK, EP, ESIS][i]); p.rect(xs[g] - bw / 2, y - hgt, bw, hgt); } y -= hgt; });
      lab(g === 0 ? `$\\text{${__('ennen')}}$` : `$\\text{${__('nyt')}}$`, xs[g], CH.name, 'c', MUTEDC);
    });
    const yT = CH.bot - S.E0 * sc;                                       // the starting total: the "now" column reaches it
    p.stroke(...INKC); p.strokeWeight(1.2 * U); p.drawingContext.setLineDash([5 * U, 4 * U]);
    p.line(xs[0] - bw / 2 - 4 * U, yT, xs[1] + bw / 2 + 4 * U, yT); p.drawingContext.setLineDash([]);
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(8, CH.bot, CH.w * 0.6, CH.bot);
    // the legend: one swatch and symbol per form of energy
    const lx = CH.w * 0.66, rows = [[EK, '$E_\\text{k}$'], [EP, '$E_\\text{p}$'], [ESIS, `$E_\\text{${__('sis')}}$`]];
    rows.forEach(([c, t], i) => { const y = CH.top + 10 * U + i * fh * 2; p.noStroke(); p.fill(...c); p.rect(lx, y - fh * 0.7, fh, fh); lab(t, lx + fh * 1.5, y + fh * 0.1, 'l', INKC); });
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const tw = p.textWidth(s), x0 = align === 'r' ? x - tw : align === 'c' ? x - tw / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0: OX + x0, y0: OY + y - 0.75 * fh, x1: OX + x0 + tw, y1: OY + y + 0.25 * fh });
  }
  function grect(x, y, w_, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.map(Math.round).join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w_, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
