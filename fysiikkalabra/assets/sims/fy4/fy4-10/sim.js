// fy4-10 Liikemäärän säilyminen ja yksiulotteiset törmäykset: two gliders on a level 2,0 m air track (friction and air
// resistance neglected; the weight and the track's normal force cancel). Glider 1 starts at x = 0,40 m, glider 2 at
// x = 1,20 m (centres; each glider is L = 0,20 m long, its end bumpers included). In contact (overlap d = L − (x2 − x1) > 0)
// the bumpers push the gliders apart with equal and opposite forces, F on glider 2 and −F on glider 1 (Newton's third
// law), F = max(0, k d + c (v1 − v2)):
//   kimmoisa  spring bumpers, k = 300 N/m, c = 0 (no energy lost),
//   kimmoton  a soft bumper, k = 300 N/m, c = 3,0 N·s/m (part of E_k to internal energy),
//   tarra     velcro, k = 300 N/m with critical damping c = 2√(kμ), μ = m1 m2/(m1 + m2); the gliders stick together when
//             their relative velocity reaches zero,
//   rajahdys  the gliders at rest at the middle of the track with a spring compressed by 4,0 cm between them (k = 300 N/m,
//             0,24 J), released at t = 0; the velocity sliders do not apply.
// Velocity Verlet steps of 0,2 ms of simulated time. The momenta and kinetic energies are computed from the state, so the
// conservation of the total momentum is a result of the equal and opposite forces, not an input. The "after" values are
// taken when the contact ends (or when the gliders stick). The run ends when a glider reaches an end of the track.
// Top: the track with the gliders, velocity arrows (blue) above and momentum arrows (purple) below the beam, the contact
// forces (red) during the collision. Bottom (stacked on a phone): momentum bars and kinetic energy bars, before and now.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const L = 0.20, K = 300, C_IN = 3.0, D0 = 0.04, DT = 0.0002, TRACK = 2.0, TMAX = 12;
  const BLUE = [25, 113, 194], PURPLE = [112, 72, 232], PURPLE_L = [197, 184, 248], PURPLE_M = [150, 124, 240], RED = [201, 42, 42],
    INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GREEN = [43, 138, 62], GREEN_L = [178, 242, 187], GREEN_M = [105, 190, 120];
  let laid = false, narrow = false, OX = 0, OY = 0, U = 1, fh = 13, labels = [];
  // panels (canvas coordinates within the panel); the wide layout first, setLayout() switches
  const TR = { w: 600, h: 215, t: 18, v2: 34, v1: 58, beam: 140, p1: 176, p2: 200, gh: 50 };
  const CH = { w: 300, h: 185, title: 16, glab: 36, top: 46, bot: 150, name: 172 };
  let btn, slV1, lV1, slV2, lV2, selM1, selM2, selT, selSpeed, readout;
  let x1, x2, w1, w2, F, t, running, done, contact, stuck, after, Pscale, Escale, P0, E0;

  const M = () => ({ m1: Number(selM1.value()), m2: Number(selM2.value()), typ: selT.value(),
                     v1: selT.value() === 'rajahdys' ? 0 : Number(slV1.value()), v2: selT.value() === 'rajahdys' ? 0 : Number(slV2.value()) });
  const damp = (S) => S.typ === 'kimmoton' ? C_IN : S.typ === 'tarra' ? 2 * Math.sqrt(K * S.m1 * S.m2 / (S.m1 + S.m2)) : 0;
  function force(S, a1, a2, u1, u2) { const d = L - (a2 - a1); return d <= 0 ? 0 : Math.max(0, K * d + damp(S) * (u1 - u2)); }
  function restart() {
    const S = M();
    if (S.typ === 'rajahdys') { x1 = 1 - (L - D0) / 2; x2 = 1 + (L - D0) / 2; } else { x1 = 0.40; x2 = 1.20; }
    w1 = S.v1; w2 = S.v2; t = 0; running = false; done = false; contact = false; stuck = false; after = null;
    F = force(S, x1, x2, w1, w2);
    P0 = { p1: S.m1 * w1, p2: S.m2 * w2 }; E0 = { e1: 0.5 * S.m1 * w1 * w1, e2: 0.5 * S.m2 * w2 * w2 };
    // drawing scales: the largest momentum or energy this run can reach (an elastic outcome bounds the collisions)
    const ue1 = ((S.m1 - S.m2) * S.v1 + 2 * S.m2 * S.v2) / (S.m1 + S.m2), ue2 = ((S.m2 - S.m1) * S.v2 + 2 * S.m1 * S.v1) / (S.m1 + S.m2);
    const pr = Math.sqrt(2 * 0.5 * K * D0 * D0 * S.m1 * S.m2 / (S.m1 + S.m2));
    Pscale = 1.1 * Math.max(0.05, Math.abs(P0.p1), Math.abs(P0.p2), Math.abs(P0.p1 + P0.p2), Math.abs(S.m1 * ue1), Math.abs(S.m2 * ue2), S.typ === 'rajahdys' ? pr : 0);
    Escale = 1.1 * Math.max(0.01, E0.e1 + E0.e2, S.typ === 'rajahdys' ? 0.5 * K * D0 * D0 : 0);
    const rj = S.typ === 'rajahdys';
    for (const s of [slV1, slV2]) if (s) s.elt.disabled = rj || !!s.elt.closest('label')?.classList.contains('locked');
  }
  function step(S, dt) {
    if (stuck) { x1 += w1 * dt; x2 += w2 * dt; return; }
    const h1 = w1 - F / S.m1 * dt / 2, h2 = w2 + F / S.m2 * dt / 2;
    x1 += h1 * dt; x2 += h2 * dt;
    F = force(S, x1, x2, h1, h2);
    w1 = h1 - F / S.m1 * dt / 2; w2 = h2 + F / S.m2 * dt / 2;
    const d = L - (x2 - x1);
    if (d > 0) contact = true;
    if (S.typ === 'tarra' && contact && w1 - w2 <= 0) { const V = (S.m1 * w1 + S.m2 * w2) / (S.m1 + S.m2); w1 = w2 = V; stuck = true; F = 0; after = { u1: w1, u2: w2 }; }
    else if (contact && after === null && d <= 0) after = { u1: w1, u2: w2 };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lt = p.createElement('label').parent(controls); p.createSpan(__('tyyppi')).parent(lt); selT = p.createSelect().parent(lt);
    for (const k of ['kimmoisa', 'kimmoton', 'tarra', 'rajahdys']) selT.option(__(k), k);
    selT.selected('kimmoisa');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('massa1')).parent(l1); selM1 = p.createSelect().parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('massa2')).parent(l2); selM2 = p.createSelect().parent(l2);
    for (const s of [selM1, selM2]) { for (const m of ['0.2', '0.4', '0.6']) s.option(m.replace('.', ',') + '0 kg', m); s.selected('0.4'); }
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
    const S = M();
    if (running) {
      let left = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
      while (left > 1e-9 && running) {
        const d = Math.min(DT, left); step(S, d); t += d; left -= d;
        if (x1 - L / 2 <= 0 || x2 + L / 2 >= TRACK || t >= TMAX) { running = false; done = true; }
      }
    }
    const p1 = S.m1 * w1, p2 = S.m2 * w2, e1 = 0.5 * S.m1 * w1 * w1, e2 = 0.5 * S.m2 * w2 * w2;
    const pJ = after ? S.m1 * after.u1 + S.m2 * after.u2 : null, EkJ = after ? 0.5 * S.m1 * after.u1 ** 2 + 0.5 * S.m2 * after.u2 ** 2 : null;
    lV1.html(__('v1', { v: tx(Number(slV1.value()), 1) }));
    lV2.html(__('v2', { v: tx(Number(slV2.value()), 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const dots = '\\ldots';
    readout.html(__('lukemat', { p0: tx(P0.p1 + P0.p2, 3), E0: tx(E0.e1 + E0.e2, 3),
      u1: after ? tx(after.u1, 2) : dots, u2: after ? tx(after.u2, 2) : dots, pJ: after ? tx(pJ, 3) : dots, EJ: after ? tx(EkJ, 3) : dots,
      t: tx(t, 2), w1: tx(w1, 2), w2: tx(w2, 2), p: tx(p1 + p2, 3), E: tx(e1 + e2, 3) }));
    window.simState = { tyyppi: S.typ, m1: S.m1, m2: S.m2, v1: S.v1, v2: S.v2, t, x1, x2, w1, w2, F, p1, p2, p: p1 + p2, Ek: e1 + e2,
      p0: P0.p1 + P0.p2, Ek0: E0.e1 + E0.e2, u1: after ? after.u1 : null, u2: after ? after.u2 : null, pJ, EkJ,
      dEk: after ? EkJ - (E0.e1 + E0.e2) : null, contact, stuck, running, done, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    setLayout(cw < 500);
    U = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;   // phone: about 14 CSS px on screen
    labels = [];
    p.background(250);
    OX = 0; OY = 0; p.push(); trackPanel(S); p.pop();
    if (narrow) {
      OX = 0; OY = TR.h; p.push(); p.translate(OX, OY); chart('p', S, p1, p2); p.pop();
      OX = 0; OY = TR.h + CH.h; p.push(); p.translate(OX, OY); chart('E', S, e1, e2); p.pop();
    } else {
      OX = 0; OY = TR.h; p.push(); p.translate(OX, OY); chart('p', S, p1, p2); p.pop();
      OX = 300; OY = TR.h; p.push(); p.translate(OX, OY); chart('E', S, e1, e2); p.pop();
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
  const SX = () => (TR.w - 40) / TRACK, X = (x) => 20 + x * SX();

  // --- the track: the air track, the gliders with their bumpers, velocity and momentum arrows, contact forces ---
  function trackPanel(S) {
    grect(0, 0, TR.w, TR.h, [[238, 245, 249], [250, 250, 250]], 0);
    const by = TR.beam, bh = 12 * U;
    grect(20, by, TR.w - 40, bh, [[214, 220, 226], [160, 170, 180]], 2 * U);
    p.noStroke(); p.fill(138, 150, 163); for (let x = 32; x < TR.w - 24; x += 16 * U) p.circle(x, by + bh / 2, 2.6 * U);
    p.fill(...INKC); p.rect(14, by - 18 * U, 6, 18 * U + bh); p.rect(TR.w - 20, by - 18 * U, 6, 18 * U + bh);   // end stops
    const d = Math.max(0, L - (x2 - x1)), bump = 0.03;
    glider(x1, S.m1, [241, 223, 181], 1, S, d, bump);
    glider(x2, S.m2, [196, 204, 212], 2, S, d, bump);
    // contact forces: F on glider 2 to the right, −F on glider 1 to the left, from the contact point
    if (F > 0.05) {
      const cx = X((x1 + x2) / 2), cy = by - 2 * U - 0.25 * TR.gh, Lf = Math.min(110 * U, 14 * U + 12 * U * F);
      arrow(cx, cy, cx + Lf, cy, RED, 4 * U); arrow(cx, cy, cx - Lf, cy, RED, 4 * U);
    }
    // velocity (blue) above, momentum (purple) below the beam; each glider on its own row
    const vs = narrow ? 150 : 120, ps = TR.w * 0.3 / Pscale;
    vec(X(x1), TR.v1, w1 * vs, BLUE, '\\overline{v}_1');
    vec(X(x2), TR.v2, w2 * vs, BLUE, '\\overline{v}_2');
    vec(X(x1), TR.p1, S.m1 * w1 * ps, PURPLE, '\\overline{p}_1');
    vec(X(x2), TR.p2, S.m2 * w2 * ps, PURPLE, '\\overline{p}_2');
    lab(`$t = ${tx(t, 2)}\\,\\text{s}$`, 10, TR.t + fh * 0.35, 'l', INKC);
  }
  function glider(x, m, col, num, S, d, bump) {
    const s = SX(), by = TR.beam, h = TR.gh * (0.55 + 0.75 * m), bodyL = (L - 2 * bump) * s;
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
  function vec(x, y, len, col, name) {           // an arrow of signed length len on the row y, its label at the tip
    if (Math.abs(len) < 4 * U) return;
    let x0 = x, xt = x + len;                      // from the glider; near an end of the track it ends at the glider instead
    if (xt > TR.w - 8 || xt < 8) { x0 = x - len; xt = x; }
    arrow(x0, y, xt, y, col, 3 * U);
    p.textSize(fh); const tw = p.textWidth(`$${name}$`), gap = 6 * U;
    let lx = len > 0 ? xt + gap : xt - gap - tw;
    if (lx < 4 || lx + tw > TR.w - 4) lx = len > 0 ? x0 - gap - tw : x0 + gap;
    lab(`$${name}$`, lx, y + fh * 0.35, 'l', col);
  }
  function arrow(x1_, y1_, x2_, y2_, col, sw) {
    const a = Math.atan2(y2_ - y1_, x2_ - x1_), hd = 10 * U;
    p.stroke(...col); p.strokeWeight(sw); p.line(x1_, y1_, x2_ - hd * 0.8 * Math.cos(a), y2_ - hd * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2_, y2_, x2_ - hd * Math.cos(a - 0.42), y2_ - hd * Math.sin(a - 0.42), x2_ - hd * Math.cos(a + 0.42), y2_ - hd * Math.sin(a + 0.42));
  }

  // --- the charts: momentum (signed, zero line in the middle) and kinetic energy, before and now, to one scale per run ---
  function chart(kind, S, a1, a2) {
    p.noStroke(); p.fill(255); p.rect(0, 0, CH.w, CH.h);
    p.stroke(220); p.strokeWeight(1); p.line(0, 0, CH.w, 0); if (!narrow && kind === 'E') p.line(0, 0, 0, CH.h);
    const isP = kind === 'p';
    lab(isP ? `$p\\ (\\text{kg}\\cdot\\text{m/s})$` : `$E_\\text{k}\\ (\\text{J})$`, 10, CH.title, 'l', isP ? PURPLE : GREEN);
    const zero = isP ? (CH.top + CH.bot) / 2 : CH.bot, span = isP ? (CH.bot - CH.top) / 2 : CH.bot - CH.top, sc = span / (isP ? Pscale : Escale);
    const b0 = isP ? [P0.p1, P0.p2, P0.p1 + P0.p2] : [E0.e1, E0.e2, E0.e1 + E0.e2], bn = [a1, a2, a1 + a2];
    const cols = isP ? [PURPLE_L, PURPLE_M, PURPLE] : [GREEN_L, GREEN_M, GREEN];
    const names = isP ? ['p_1', 'p_2', 'p_\\text{kok}'] : ['E_1', 'E_2', 'E_\\text{kok}'];
    const gw = CH.w / 2, bw = Math.min(34 * U, gw / 5);
    [b0, bn].forEach((vals, g) => {
      const xs = [0.2, 0.5, 0.8].map((f) => g * gw + f * gw);
      vals.forEach((v, i) => {
        const hgt = Math.max(-span, Math.min(span, v * sc));
        p.noStroke(); p.fill(...cols[i]); p.rect(xs[i] - bw / 2, Math.min(zero, zero - hgt), bw, Math.abs(hgt));
        lab(`$${names[i]}$`, xs[i], CH.name, 'c', INKC);
      });
      lab(g === 0 ? `$\\text{${__('ennen')}}$` : `$\\text{${__('nyt')}}$`, g * gw + gw / 2, CH.glab, 'c', MUTEDC);
    });
    p.stroke(...INKC); p.strokeWeight(1.5 * U); p.line(8, zero, CH.w - 8, zero);
    p.stroke(220); p.strokeWeight(1); p.line(CH.w / 2, CH.top, CH.w / 2, CH.bot);
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
