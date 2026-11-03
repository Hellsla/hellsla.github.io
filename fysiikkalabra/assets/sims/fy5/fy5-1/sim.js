// fy5-1 Voiman momentti ja kappaleen kiertyminen: a wrench on a stuck wheel nut. The hand pulls the wrench with the force
// F at the distance d from the axis (the middle of the nut) and at the angle α to the handle's extension. Model: the arm
// is r = d sin α (the perpendicular distance from the axis to the line of action), the moment M = F r (counterclockwise,
// the opening direction, for 0° ≤ α ≤ 180°). The nut opens when M reaches the moment its friction needs (tight 30 Nm,
// rusty 60 Nm). That value is not shown: the student finds it from the attempts. Väännä makes an attempt: the wrench
// turns (the nut opens) or only shakes, and the attempt is plotted at (r, F) in the chart, green when the nut opened.
// The turning is a picture only (no rotational dynamics, FY5 scope); the speed select changes its pace, nothing else.
// Wide: the picture (left) and the chart (right) side by side in 600×400; under 500 px of #sim-root the two panels stack
// at the full 600 width (NOTES 4). Every canvas text goes through lab(), which pushes its box to simState.labels.
new p5((p) => {
  const NEED = { tiukka: 30, ruoste: 60 };                                  // Nm, the moment each nut needs (hidden)
  const WRENCH = 0.45;                                                      // m, the wrench's length
  const RED = [201, 42, 42], INKC = [31, 41, 51], MUTED = [107, 116, 128], GREEN = [43, 138, 62], RULEC = [227, 220, 203];
  const HN = { pic: 360, gra: 270 };                                        // panel heights when stacked on a phone
  let btn, slF, slD, slA, lF, lD, lA, selN, selSpeed, cbArm, readout;
  let narrow = false, laid = false, labels = [], points = [], tulos = null, phi = 0, anim = null;
  let L = {};                                                               // the layout of the current width

  const model = () => {
    const F = Number(slF.value()), d = Number(slD.value()), al = Number(slA.value());
    const r = d * Math.sin(al * Math.PI / 180), M = F * r;                  // arm r = d sin α, moment M = F r
    const nutKey = selN.value(), M0 = NEED[nutKey];
    return { F, d, al, r: Math.abs(r) < 1e-12 ? 0 : r, M: Math.abs(M) < 1e-9 ? 0 : M, nut: nutKey, M0, opens: M >= M0 - 1e-6 };
  };
  const clearTry = () => { tulos = null; phi = 0; anim = null; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('vaanna')).parent(controls);
    btn.elt.addEventListener('click', attempt);
    const bR = p.createButton(__('alusta')).parent(controls);
    bR.elt.addEventListener('click', () => { clearTry(); points = []; });
    const l1 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l1); slF = p.createSlider(0, 300, 100, 10).parent(l1);
    const l2 = p.createElement('label').parent(controls); lD = p.createSpan('').parent(l2); slD = p.createSlider(0.10, 0.40, 0.30, 0.05).parent(l2);
    const l3 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l3); slA = p.createSlider(0, 180, 90, 15).parent(l3);
    const ln = p.createElement('label').parent(controls); p.createSpan(__('mutteri')).parent(ln); selN = p.createSelect().parent(ln);
    selN.option(__('tiukka'), 'tiukka'); selN.option(__('ruoste'), 'ruoste'); selN.selected('tiukka');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const lk = p.createElement('label').parent(controls); cbArm = p.createCheckbox('', true).parent(lk); p.createSpan(__('varsi')).parent(lk);
    for (const e of [slF.elt, slD.elt, slA.elt]) { e.addEventListener('input', clearTry); e.addEventListener('change', clearTry); }
    for (const ev of ['input', 'change']) selN.elt.addEventListener(ev, () => { clearTry(); points = []; });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { F: { input: slF.elt, unit: 'N' }, d: { input: slD.elt, unit: 'm' }, alpha: { input: slA.elt, unit: '°' }, mutteri: { input: selN.elt, unit: '' } },
      reset: () => { slF.value(100); slD.value(0.30); slA.value(90); selN.selected('tiukka'); cbArm.checked(true); clearTry(); points = []; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function attempt() {   // one try: the result is decided at once, the picture follows
    const m = model();
    tulos = m.opens ? 1 : 0; phi = 0;
    anim = { t: 0, open: m.opens };
    points.push({ r: m.r, F: m.F, ok: m.opens });
    if (points.length > 60) points.shift();
  }

  // wide: picture and chart side by side; phone (#sim-root under 500 px): stacked at the full 600 width
  function setLayout(n) {
    if (n === narrow && laid) return false;
    laid = true; narrow = n;
    if (n) { L = { W: 600, O: [130, 222], PXM: 700, SF: 0.42, C: { x0: 112, x1: 556, yb: HN.pic + 214, yt: HN.pic + 52 } }; p.resizeCanvas(600, HN.pic + HN.gra); }
    else { L = { W: 352, O: [84, 238], PXM: 400, SF: 0.33, C: { x0: 414, x1: 572, yb: 316, yt: 88 } }; p.resizeCanvas(600, 400); }
    return true;
  }

  p.draw = () => {
    const m = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    if (setLayout(cw < 500)) { publish(m, []); p.redraw(); return; }
    if (anim) {                                                             // the picture of the attempt (simulated time · speed)
      anim.t += Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
      if (anim.open) { phi = Math.min(28, anim.t / 1.2 * 28); if (anim.t >= 1.2) anim = null; }
      else { phi = anim.t < 0.6 ? 2.2 * Math.sin(anim.t * 42) * (1 - anim.t / 0.6) : 0; if (anim.t >= 0.6) anim = null; }
    }
    lF.html(__('voima', { F: tx(m.F, 0) })); lD.html(__('etaisyys', { d: tx(m.d, 2) })); lA.html(__('kulma', { a: tx(m.al, 0) }));
    const tila = tulos === null ? __('ei_yritetty') : tulos ? __('aukesi') : __('ei_liiku');
    readout.html(__('lukemat', { F: tx(m.F, 0), d: tx(m.d, 2), a: tx(m.al, 0), r: tx(m.r, 3), M: tx(m.M, 1), tila: tila }));
    const fh = Math.round((narrow ? 14 : 13) * k), U = narrow ? 0.8 * k : Math.max(1, 0.8 * k);
    labels = [];
    p.background(250);
    picture(m, fh, U, k);
    chart(m, fh, U, k);
    publish(m, labels);
  };

  function publish(m, labs) {
    window.simState = { F: m.F, d: m.d, alpha: m.al, r: m.r, M: m.M, mutteri: m.nut, M0: m.M0, avautuu: m.opens ? 1 : 0, tulos,
                        yrityksia: points.length, phi, varsi: cbArm.checked(), animating: !!anim, narrow, labels: labs };
  }

  // --- the picture: a wheel rim with nuts, the wrench on one of them, the hand's force, its line of action and arm ---
  function picture(m, fh, U, k) {
    const O = L.O, W = L.W, H = narrow ? HN.pic : 400, px = L.PXM;
    grect(0, 0, W, H, [[246, 241, 230], [233, 226, 210]], 0);
    // a steel plate bolted to a frame: the nut on its middle bolt is the one to open
    const pw = 150 * U, ph = 210 * U, px0 = O[0] - pw / 2 - 20 * U, py0 = O[1] - ph / 2;
    p.stroke(138, 150, 163); p.strokeWeight(2 * U);
    grect(px0, py0, pw, ph, [[238, 242, 246], [196, 204, 212]], 10 * U); p.noFill(); p.rect(px0, py0, pw, ph, 10 * U);
    for (const q of [[px0 + 22 * U, py0 + 22 * U], [px0 + 22 * U, py0 + ph - 22 * U]]) hex(q, 11 * U, 0);
    const th = phi * Math.PI / 180, al = m.al * Math.PI / 180;
    const ux = Math.cos(th), uy = -Math.sin(th);                             // the handle's direction on the screen
    const P = [O[0] + m.d * px * ux, O[1] + m.d * px * uy];
    const fx = Math.cos(th + al), fy = -Math.sin(th + al);                    // the force's direction on the screen
    // the line of action (dashed, both ways) and the handle's extension from which α is measured
    p.stroke(...MUTED); p.strokeWeight(1.5 * U); dash([6 * U, 5 * U]);
    p.line(P[0] - fx * 600, P[1] - fy * 600, P[0] + fx * 600, P[1] + fy * 600);
    p.line(P[0], P[1], P[0] + ux * 46 * U, P[1] + uy * 46 * U); dash([]);
    // the wrench: a ring around the nut and the handle
    const E = [O[0] + WRENCH * px * ux, O[1] + WRENCH * px * uy], hw = 8 * U;
    p.fill(196, 204, 212); p.stroke(...INKC); p.strokeWeight(2.2 * U);
    p.quad(O[0] - uy * hw, O[1] + ux * hw, E[0] - uy * hw, E[1] + ux * hw, E[0] + uy * hw, E[1] - ux * hw, O[0] + uy * hw, O[1] - ux * hw);
    p.circle(E[0], E[1], 2 * hw); p.circle(O[0], O[1], 48 * U);
    hex(O, 17 * U, th);
    // the dimension d below the handle (on the side away from the force's usual side)
    const sd = m.al > 90.5 ? 1 : -1;                                          // d on the side of the handle away from the arm
    const off = 26 * U, nxd = -uy * sd, nyd = ux * sd;
    p.stroke(...INKC); p.strokeWeight(1.3 * U);
    p.line(O[0] + nxd * off, O[1] + nyd * off, P[0] + nxd * off, P[1] + nyd * off);
    for (const q of [O, P]) p.line(q[0] + nxd * (off - 6 * U), q[1] + nyd * (off - 6 * U), q[0] + nxd * (off + 6 * U), q[1] + nyd * (off + 6 * U));
    lab('$d$', (O[0] + P[0]) / 2 + nxd * (off + 14 * U), (O[1] + P[1]) / 2 + nyd * (off + 14 * U) + fh * 0.36, 'c', fh, INKC);
    // the arm r: from the axis perpendicular to the line of action
    if (cbArm.checked() && m.r > 0.004) {
      const t = (P[0] - O[0]) * fx + (P[1] - O[1]) * fy, Fo = [P[0] - fx * t, P[1] - fy * t];   // the foot of the perpendicular
      p.stroke(...INKC); p.strokeWeight(2.6 * U); p.line(O[0], O[1], Fo[0], Fo[1]);
      const ax = (O[0] - Fo[0]) / (m.r * px), ay = (O[1] - Fo[1]) / (m.r * px), s = 9 * U;
      const sg = t > 0 ? -1 : 1;                                             // the mark on the line of action's side towards P
      p.strokeWeight(1.3 * U); p.noFill();
      p.beginShape(); p.vertex(Fo[0] - sg * fx * s, Fo[1] - sg * fy * s); p.vertex(Fo[0] - sg * fx * s + ax * s, Fo[1] - sg * fy * s + ay * s); p.vertex(Fo[0] + ax * s, Fo[1] + ay * s); p.endShape();
      const mx = (O[0] + Fo[0]) / 2, my = (O[1] + Fo[1]) / 2, g = 16 * U;     // r's label beside the arm, outside the triangle O, P, foot
      const sx = -ay, sy = ax, toP = sx * (P[0] - mx) + sy * (P[1] - my);
      const side = toP < -1 ? 1 : toP > 1 ? -1 : (sx * -uy + sy * ux > 0 ? 1 : -1);   // at 90° (arm along the handle): below it
      lab('$r$', mx + side * sx * g, my + side * sy * g + fh * 0.36, 'c', fh, INKC);
    }
    // the moment: a curved arrow around the nut, its length growing with M (counterclockwise: the opening direction)
    if (m.M > 0.05) {
      const R = 40 * U, a0 = th + 1.75, span = 0.5 + 2.6 * Math.min(1, m.M / 120);
      p.noFill(); p.stroke(...INKC); p.strokeWeight(2.6 * U);
      p.arc(O[0], O[1], 2 * R, 2 * R, -(a0 + span) + 0.16, -a0);
      const e = a0 + span, hx = O[0] + R * Math.cos(e), hy = O[1] - R * Math.sin(e), tgx = -Math.sin(e), tgy = -Math.cos(e), hh = 10 * U;
      p.noStroke(); p.fill(...INKC);
      p.triangle(hx, hy, hx - tgx * hh - tgy * hh * 0.5, hy - tgy * hh + tgx * hh * 0.5, hx - tgx * hh + tgy * hh * 0.5, hy - tgy * hh - tgx * hh * 0.5);
      const la = a0 + 0.3;
      lab('$M$', O[0] + (R + 16 * U) * Math.cos(la), O[1] - (R + 16 * U) * Math.sin(la) + fh * 0.36, 'c', fh, INKC);
    }
    // the angle α at the point of application
    if (m.al > 0.5) {
      const R = 24 * U; p.noFill(); p.stroke(...INKC); p.strokeWeight(1.3 * U);
      p.arc(P[0], P[1], 2 * R, 2 * R, -(th + al), -th);
      const la = th + al / 2, rr = R + 13 * U;
      lab('$\\alpha$', P[0] + rr * Math.cos(la), P[1] - rr * Math.sin(la) + fh * 0.36, 'c', fh, INKC);
    }
    // the hand's grip and the force: a pull starts at P, a push (cos α < 0) ends at P
    p.noStroke(); p.fill(107, 116, 128); p.circle(P[0], P[1], 13 * U);
    if (m.F > 0) {
      const len = m.F * L.SF, push = Math.cos(al) < -1e-9;
      const a = push ? [P[0] - fx * len, P[1] - fy * len] : P, b = push ? P : [P[0] + fx * len, P[1] + fy * len];
      arrow(a, b, U);
      const q = push ? a : b, sgn = push ? -1 : 1;
      lab('$\\overline{F}$', q[0] + sgn * fx * 15 * U, q[1] + sgn * fy * 15 * U + fh * 0.36, 'c', fh, RED);
    }
  }

  // --- the chart: every attempt at (r, F); filled green when the nut opened, a hollow ring when it did not ---
  function chart(m, fh, U, k) {
    const C = L.C, x0 = C.x0, x1 = C.x1, yb = C.yb, yt = C.yt;
    if (narrow) { p.noStroke(); p.fill(255); p.rect(0, HN.pic, 600, HN.gra); p.stroke(220); p.strokeWeight(1); p.line(0, HN.pic, 600, HN.pic); }
    else { p.noStroke(); p.fill(255); p.rect(L.W, 0, 600 - L.W, 400); p.stroke(220); p.strokeWeight(1); p.line(L.W, 0, L.W, 400); }
    const X = (r) => x0 + r / 0.40 * (x1 - x0 - 14), Y = (F) => yb - F / 300 * (yb - yt - 14);
    p.stroke(...RULEC); p.strokeWeight(1);
    const xt = [0.1, 0.2, 0.3, 0.4], yt_ = [100, 200, 300];
    for (const r of xt) p.line(X(r), yb, X(r), Y(300));
    for (const F of yt_) p.line(x0, Y(F), X(0.4), Y(F));
    p.stroke(...INKC); p.strokeWeight(2); p.line(x0, yb, x1, yb); p.line(x0, yb, x0, yt);
    p.noStroke(); p.fill(...INKC);
    p.triangle(x1 + 2, yb, x1 - 9, yb - 4.5, x1 - 9, yb + 4.5); p.triangle(x0, yt - 2, x0 - 4.5, yt + 9, x0 + 4.5, yt + 9);
    p.stroke(...INKC); p.strokeWeight(1.3);
    const every = k > 1.5 && !narrow ? 2 : 1;
    xt.forEach((r, i) => { p.line(X(r), yb, X(r), yb + 5); if ((i + 1) % every === 0) lab(`$${tx(r, 1)}$`, X(r), yb + 6 + fh * 1.05, 'c', fh, MUTED); });
    yt_.forEach((F, i) => { p.line(x0 - 5, Y(F), x0, Y(F)); if ((i + 1) % every === 0 || i === yt_.length - 1) lab(`$${F}$`, x0 - 8, Y(F) + fh * 0.36, 'r', fh, MUTED); });
    lab('$0$', x0 - 8, yb + fh * 0.36, 'r', fh, MUTED);
    lab('$F\\ (\\text{N})$', x0 + 8, yt - fh * 0.3, 'l', fh, INKC);
    lab('$r\\ (\\text{m})$', x1 - 4, yb - fh * 0.75, 'r', fh, INKC);
    lab(__('yritykset'), 590, (narrow ? HN.pic : 0) + fh * 1.5, 'r', fh, INKC);
    for (const q of points) {
      const x = X(q.r), y = Y(q.F);
      if (q.ok) { p.stroke(255); p.strokeWeight(2); p.fill(...GREEN); p.circle(x, y, 12 * Math.max(1, U * 0.9)); }
      else { p.noFill(); p.stroke(...MUTED); p.strokeWeight(2.2); p.circle(x, y, 11 * Math.max(1, U * 0.9)); }
    }
    // the current setting: a small red cross
    const cx = X(m.r), cy = Y(m.F), s = 6 * Math.max(1, U * 0.9);
    p.stroke(...RED); p.strokeWeight(2); p.line(cx - s, cy, cx + s, cy); p.line(cx, cy - s, cx, cy + s);
  }

  function arrow(a, b, U) {
    const Lh = Math.hypot(b[0] - a[0], b[1] - a[1]); if (Lh < 1) return;
    const an = Math.atan2(b[1] - a[1], b[0] - a[0]), Hh = 13 * U;
    p.stroke(...RED); p.strokeWeight(3.6 * U); p.line(a[0], a[1], b[0] - Hh * 0.8 * Math.cos(an), b[1] - Hh * 0.8 * Math.sin(an));
    p.noStroke(); p.fill(...RED);
    p.triangle(b[0], b[1], b[0] - Hh * Math.cos(an - 0.4), b[1] - Hh * Math.sin(an - 0.4), b[0] - Hh * Math.cos(an + 0.4), b[1] - Hh * Math.sin(an + 0.4));
  }
  function hex(c, r, th) {
    p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2);
    p.beginShape(); for (let i = 0; i < 6; i++) { const a = th + Math.PI / 6 + i * Math.PI / 3; p.vertex(c[0] + r * Math.cos(a), c[1] - r * Math.sin(a)); } p.endShape(p.CLOSE);
    p.fill(138, 150, 163); p.strokeWeight(1.5); p.circle(c[0], c[1], r * 0.9);
  }
  const dash = (pat) => p.drawingContext.setLineDash(pat);

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  function grect(x, y, w, h, stops, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
