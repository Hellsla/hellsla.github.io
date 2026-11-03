// fy6-1 Virtapiiri, sähkövirta ja jännite: a closed circuit of 1–3 cells (1,5 V each), one or two lamps in the same loop
// and a switch. The copper wire is full of free electrons (blue dots, one dot = 0,05 C of charge); they all start to
// move at once when the switch closes, against the conventional current (violet arrows, + → − outside the cells).
// Model (hidden from the student): each lamp a constant 15 Ω, I = U / (n · 15 Ω), so 0,10 A per cell with one lamp.
// Mittaa counts the dots that pass the cross-section A (before the lamps) and B (after them, on the return wire) for
// 10,0 s of simulated time: Q_A and Q_B emerge from the counted dots, and the student finds I = Q / t and that no charge
// is used up in a lamp. The speed select changes only the pace (every count is per simulated time).
// One panel, 600×400 at every width (the picture needs no stacking); labels grow with 600 / clientWidth and every
// canvas text goes through lab(), which pushes its box to simState.labels.
new p5((p) => {
  const R_LAMP = 15, Q_DOT = 0.05, T_MEAS = 10.0, CELL_U = 1.5;           // Ω, C per dot, s, V per cell
  const L = 110, R = 500, T = 118, B = 322, YB = 220;                       // the loop; YB the battery's middle on the left wire
  const SP = 24, P = (YB - T) + (R - L) + (B - T) + (R - L) + (B - YB);     // the dots' spacing and the path's length (1200)
  const GA = (YB - T) + 60, GB = (YB - T) + (R - L) + (YB - T);             // the cross-sections A (x = 170 on the top) and B (y = 220 on the right)
  const INKC = [31, 41, 51], MUTED = [107, 116, 128], CUR = [112, 72, 232], ELE = [25, 113, 194], CU = [184, 98, 45];
  let selP, selL, selK, selSpeed, btn, readout;
  let ph = 0, measuring = false, mt = 0, ph0 = 0, QA = null, QB = null, labels = [];

  const model = () => {
    const cells = Number(selP.value()), lamps = Number(selL.value()), closed = selK.value() === 'suljettu';
    const U = CELL_U * cells, I = closed ? U / (lamps * R_LAMP) : 0;
    return { cells, lamps, closed, U, I };
  };
  const clear = () => { measuring = false; mt = 0; QA = null; QB = null; btn.removeAttribute('disabled'); btn.html(__('mittaa')); };
  const counts = (m) => {                                                    // dots through A and B since the start
    const N = m.I * mt / Q_DOT, c = (g) => Math.floor((ph0 + g) / SP + N + 1e-9) - Math.floor((ph0 + g) / SP + 1e-9);
    return [c(GA), c(GB)];
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('mittaa')).parent(controls);
    btn.elt.addEventListener('click', start);
    const b2 = p.createButton(__('nollaa')).parent(controls);
    b2.elt.addEventListener('click', clear);
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('paristot')).parent(l1); selP = p.createSelect().parent(l1);
    selP.option(__('p1'), '1'); selP.option(__('p2'), '2'); selP.option(__('p3'), '3'); selP.selected('2');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('lamput')).parent(l2); selL = p.createSelect().parent(l2);
    selL.option(__('l1'), '1'); selL.option(__('l2'), '2'); selL.selected('1');
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('kytkin')).parent(l3); selK = p.createSelect().parent(l3);
    selK.option(__('suljettu'), 'suljettu'); selK.option(__('auki'), 'auki'); selK.selected('suljettu');
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l4); selSpeed = p.createSelect().parent(l4);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '3'); selSpeed.selected('1');
    for (const s of [selP, selL, selK]) for (const ev of ['input', 'change']) s.elt.addEventListener(ev, clear);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { paristot: { input: selP.elt, unit: '' }, lamput: { input: selL.elt, unit: '' }, kytkin: { input: selK.elt, unit: '' } },
      reset: () => { selP.selected('2'); selL.selected('1'); selK.selected('suljettu'); clear(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function start() {                                                         // a new 10-s measurement from zero
    measuring = true; mt = 0; ph0 = ph; QA = null; QB = null;
    btn.attribute('disabled', ''); btn.html(__('mitataan'));
  }

  p.draw = () => {
    const m = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());   // simulated seconds this frame
    const v = m.I / Q_DOT * SP;                                                // px per simulated second
    if (measuring) {
      mt = Math.min(T_MEAS, mt + dt); ph = ph0 + v * mt;
      if (mt >= T_MEAS) { const [a, b] = counts(m); QA = a * Q_DOT; QB = b * Q_DOT; measuring = false; btn.removeAttribute('disabled'); btn.html(__('mittaa')); }
    } else ph = (ph + v * dt) % (P * 1000);
    const [na, nb] = measuring || QA !== null ? counts(m) : [0, 0];
    const tila = measuring ? __('kaynnissa') : QA !== null ? __('valmis') : __('aloita');
    readout.html(__('lukemat', { U: tx(m.U, 1), t: tx(mt, 1), qa: tx(na * Q_DOT, 2), qb: tx(nb * Q_DOT, 2), tila: tila }));
    const fh = Math.round(14 * k), U = Math.max(1, 0.75 * k);
    labels = [];
    picture(m, fh, U);
    window.simState = { paristot: m.cells, lamput: m.lamps, kytkin: m.closed ? 'suljettu' : 'auki', U: m.U, I: m.I, t: mt,
                        QA, QB, qa: na * Q_DOT, qb: nb * Q_DOT, mittaa: measuring, kirkkaus: glow(m), dotsPerS: m.I / Q_DOT,
                        narrow: cw < 500, labels };
  };

  const glow = (m) => Math.sqrt(m.I * m.I * R_LAMP / 1.35);                  // one lamp's brightness: √(P / P_max), 0 … 1

  // a point of the loop at the path coordinate s (conventional direction, from the battery's middle up the left wire)
  function at(s) {
    s = ((s % P) + P) % P;
    const segs = [[L, YB, L, T], [L, T, R, T], [R, T, R, B], [R, B, L, B], [L, B, L, YB]];
    for (const [x0, y0, x1, y1] of segs) {
      const len = Math.abs(x1 - x0) + Math.abs(y1 - y0);
      if (s <= len) return [x0 + Math.sign(x1 - x0) * s, y0 + Math.sign(y1 - y0) * s];
      s -= len;
    }
    return [L, YB];
  }

  function picture(m, fh, U) {
    grect(0, 0, 600, 400, [[246, 241, 230], [236, 229, 214]], 0);
    // the wire: insulation and copper core
    p.noFill(); p.strokeJoin(p.ROUND);
    p.stroke(...INKC); p.strokeWeight(17); p.rect(L, T, R - L, B - T);
    p.stroke(...CU); p.strokeWeight(11); p.rect(L, T, R - L, B - T);
    // the free electrons: every dot at (i · SP − ph); they move against the path direction (− → + outside the cells)
    p.noStroke();
    for (let i = 0; i < P / SP; i++) {
      const q = at(i * SP - ph); p.fill(255); p.circle(q[0], q[1], 9); p.fill(...ELE); p.circle(q[0], q[1], 6.5);
    }
    // the cross-sections A and B (dashed rings around the wire)
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2); dash([4, 3]);
    p.ellipse(L + 60, T, 14, 40); p.ellipse(R, YB, 40, 14); dash([]);
    lab('$A$', L + 60, T - 30 - fh * 0.2, 'c', fh, INKC);
    lab('$B$', R + 30, YB + fh * 0.36, 'l', fh, INKC);
    // the cells, + up, stacked on the left wire
    const n = m.cells, ch = 34, top = YB - n * ch / 2;
    for (let i = 0; i < n; i++) {
      const y = top + i * ch;
      grect(L - 17, y + 2, 34, ch - 4, [[196, 204, 212], [138, 150, 163]], 4, true);
      p.noFill(); p.stroke(...INKC); p.strokeWeight(2); p.rect(L - 17, y + 2, 34, ch - 4, 4);
      p.noStroke(); p.fill(241, 223, 181); p.rect(L - 15, y + 4, 30, 8);
      p.fill(138, 150, 163); p.stroke(...INKC); p.strokeWeight(1.5); p.rect(L - 6, y - 2, 12, 5, 1);
    }
    lab('$+$', L - 34, top + fh * 0.36, 'r', fh, INKC);
    lab('$-$', L - 34, top + n * ch + fh * 0.36, 'r', fh, INKC);
    lab(`$U = ${tx(m.U, 1)}\\,\\text{V}$`, L + 26, YB + fh * 0.36, 'l', fh, INKC);
    // the lamps on the top wire
    const xs = m.lamps === 1 ? [305] : [255, 375], b = glow(m);
    for (const x of xs) {
      if (b > 0.01) {
        const c = p.drawingContext; c.save();
        const gr = c.createRadialGradient(x, T - 34, 4, x, T - 34, 26 + 46 * b);
        gr.addColorStop(0, `rgba(255,224,150,${0.95 * b})`); gr.addColorStop(1, 'rgba(255,192,120,0)');
        c.fillStyle = gr; c.beginPath(); c.arc(x, T - 34, 26 + 46 * b, 0, 2 * Math.PI); c.fill(); c.restore();
      }
      p.fill(238, 245, 249, 230); p.stroke(...INKC); p.strokeWeight(2.2); p.circle(x, T - 34, 44);
      p.noFill(); p.strokeWeight(2); p.stroke(b > 0.01 ? p.lerpColor(p.color(107, 116, 128), p.color(232, 89, 12), Math.min(1, 0.3 + b)) : p.color(107, 116, 128));
      p.beginShape(); p.vertex(x - 8, T - 14); p.vertex(x - 8, T - 34); p.vertex(x - 4, T - 40); p.vertex(x, T - 34); p.vertex(x + 4, T - 40); p.vertex(x + 8, T - 34); p.vertex(x + 8, T - 14); p.endShape();
      p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2); p.rect(x - 15, T - 14, 30, 24, 3);
    }
    // the switch on the bottom wire: a base, two posts and a copper lever
    const s0 = 280, s1 = 340;
    p.fill(241, 223, 181); p.stroke(169, 122, 53); p.strokeWeight(2); p.rect(s0 - 16, B - 10, s1 - s0 + 32, 22, 4);
    p.stroke(...CU); p.strokeWeight(6); p.strokeCap(p.ROUND);
    if (m.closed) p.line(s0, B - 3, s1, B - 3); else p.line(s0, B - 3, s0 + 52, B - 33);
    p.strokeCap(p.SQUARE);
    for (const x of [s0, s1]) { p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(1.8); p.circle(x, B - 3, 12); }
    // the conventional current: + up the left wire, right along the top, down the right, left along the bottom
    if (m.I > 0) {
      arrow([440, T + 28], [482, T + 28], U);
      arrow([234, B + 30], [182, B + 30], U);
      lab('$I$', 170, B + 30 + fh * 0.36, 'r', fh, CUR);
    }
    // the measurement time in the middle of the loop
    lab(`$t = ${tx(mt, 1)}\\,\\text{s}$`, 330, 262 + fh * 0.36, 'c', fh, INKC);
  }

  function arrow(a, b, U) {
    const an = Math.atan2(b[1] - a[1], b[0] - a[0]), Hh = 14 * U;
    p.stroke(...CUR); p.strokeWeight(3.5 * U); p.line(a[0], a[1], b[0] - Hh * 0.8 * Math.cos(an), b[1] - Hh * 0.8 * Math.sin(an));
    p.noStroke(); p.fill(...CUR);
    p.triangle(b[0], b[1], b[0] - Hh * Math.cos(an - 0.42), b[1] - Hh * Math.sin(an - 0.42), b[0] - Hh * Math.cos(an + 0.42), b[1] - Hh * Math.sin(an + 0.42));
  }
  const dash = (pat) => p.drawingContext.setLineDash(pat);

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  function grect(x, y, w, h, stops, r = 4, horizontal = false) {
    const c = p.drawingContext; c.save(); const gr = horizontal ? c.createLinearGradient(x, y, x + w, y) : c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
