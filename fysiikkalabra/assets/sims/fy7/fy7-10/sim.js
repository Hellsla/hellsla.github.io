// fy7-10 Valon heijastuminen ja taittuminen: a laser ray meets a plane interface between two materials on a
// protractor. The student chooses the material above and below the interface and the angle of incidence α1 (from the
// normal). Model: law of reflection β = α1; Snell n1 sin α1 = n2 sin α2 with the refractive indices of 589 nm light
// (air 1,00, water 1,33, acrylic 1,49, glass 1,52, diamond 2,42). When n1 sin α1 / n2 > 1 there is no refracted ray
// and all the light reflects (simState.tir). The reflected share R (unpolarised light, Fresnel's equations) sets the
// brightness of the reflected ray and is shown in the readout; the refracted ray carries the rest, T = 1 − R.
// The picture: the two materials in their own colours (their names in the upper right and lower left corners), the protractor ring with ticks every 10°, the dashed normal,
// the laser and the three rays with their angle arcs. On a narrow screen the labels grow (NOTES §4).
// Static: drawn again on every frame, no animation. Every canvas text goes through lab() (simState.labels).
new p5((p) => {
  const N = { ilma: 1.00, vesi: 1.33, akryyli: 1.49, lasi: 1.52, timantti: 2.42 };
  const FILL = { ilma: [250, 251, 252], vesi: [169, 209, 240], akryyli: [226, 236, 244], lasi: [212, 234, 229], timantti: [232, 229, 246] };
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RAY = [230, 73, 128], RULEC = [201, 194, 178], IRONC = [108, 117, 125];
  const RAD = Math.PI / 180;
  let selA, selB, slA, lA, readout, labels = [];

  const state = () => {
    const m1 = selA.value(), m2 = selB.value(), a1 = Number(slA.value());
    const n1 = N[m1], n2 = N[m2], s = n1 * Math.sin(a1 * RAD) / n2;
    const tir = s > 1 + 1e-12;
    const a2 = tir ? null : Math.asin(Math.min(1, s)) / RAD;
    let R = 1;
    if (!tir) {
      const ci = Math.cos(a1 * RAD), ct = Math.cos(a2 * RAD);
      const rs = ((n1 * ci - n2 * ct) / (n1 * ci + n2 * ct)) ** 2, rp = ((n1 * ct - n2 * ci) / (n1 * ct + n2 * ci)) ** 2;
      R = (rs + rp) / 2;
    }
    return { m1, m2, n1, n2, alpha: a1, alpha1: a1, beta: a1, alpha2: a2, sin1: Math.sin(a1 * RAD), sin2: tir ? null : s, tir, R: R * 100, T: (1 - R) * 100 };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('ylempi')).parent(l1); selA = p.createSelect().parent(l1);
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('alempi')).parent(l2); selB = p.createSelect().parent(l2);
    for (const k of Object.keys(N)) { selA.option(__(k), k); selB.option(__(k), k); }
    selA.selected('ilma'); selB.selected('vesi');
    const l3 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l3); slA = p.createSlider(0, 89, 40, 1).parent(l3);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { alpha: { input: slA.elt, unit: '°' }, m1: { input: selA.elt, unit: '' }, m2: { input: selB.elt, unit: '' } },
      reset: () => { selA.selected('ilma'); selB.selected('vesi'); slA.value(40); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lA.html(__('tulokulma', { a: tx(s.alpha1, 0) }));
    readout.html(s.tir
      ? __('lukemat_tir', { a1: tx(s.alpha1, 1), b: tx(s.beta, 1), p: tx(s.n1 * s.sin1, 3), n2: tx(s.n2, 2) })
      : __('lukemat', { a1: tx(s.alpha1, 1), b: tx(s.beta, 1), a2: tx(s.alpha2, 1), s1: tx(s.sin1, 3), s2: tx(s.sin2, 3), R: tx(s.R, s.R < 10 ? 1 : 0) }));
    window.simState = { ...s, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.round((k > 1.2 ? 14 : 13) * k);
    labels = [];
    picture(s, fh);
    window.simState.labels = labels;
  };

  function picture(s, fh) {
    const cx = 300, cy = 200, Rp = 132;
    p.noStroke(); p.fill(...FILL[s.m1]); p.rect(0, 0, 600, cy); p.fill(...FILL[s.m2]); p.rect(0, cy, 600, 400 - cy);
    // protractor ring with ticks every 10°, longer every 30°
    p.noFill(); p.stroke(...RULEC); p.strokeWeight(2); p.circle(cx, cy, 2 * Rp);
    p.stroke(...MUTEDC); p.strokeWeight(1.5);
    for (let a = 0; a < 360; a += 10) {
      const L = a % 30 === 0 ? 14 : 8, sx = Math.sin(a * RAD), sy = -Math.cos(a * RAD);
      p.line(cx + Rp * sx, cy + Rp * sy, cx + (Rp - L) * sx, cy + (Rp - L) * sy);
    }
    // the interface and the dashed normal
    p.stroke(...INKC); p.strokeWeight(2.5); p.line(0, cy, 600, cy);
    p.stroke(...MUTEDC); p.strokeWeight(2); p.drawingContext.setLineDash([8, 6]); p.line(cx, 16, cx, 384); p.drawingContext.setLineDash([]);
    // directions: incident from the upper left, reflected to the upper right, refracted to the lower right
    const a1 = s.alpha1 * RAD, Lr = Rp + 26;
    const inc = [cx - (Rp + 14) * Math.sin(a1), cy - (Rp + 14) * Math.cos(a1)];
    // angle arcs
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.8);
    if (s.alpha1 > 0.5) { p.arc(cx, cy, 100, 100, -Math.PI / 2 - a1, -Math.PI / 2); p.arc(cx, cy, 100, 100, -Math.PI / 2, -Math.PI / 2 + a1); }
    if (!s.tir && s.alpha2 > 0.5) p.arc(cx, cy, 116, 116, Math.PI / 2 - s.alpha2 * RAD, Math.PI / 2);
    // rays: the refracted one carries T, the reflected one R (brightness)
    beam(inc[0], inc[1], cx, cy, 4.5, 255, 0.4);
    beam(cx, cy, cx + Lr * Math.sin(a1), cy - Lr * Math.cos(a1), 1.5 + 3 * s.R / 100, 70 + 185 * s.R / 100, 0.8);
    if (!s.tir) beam(cx, cy, cx + Lr * Math.sin(s.alpha2 * RAD), cy + Lr * Math.cos(s.alpha2 * RAD), 1.5 + 3 * s.T / 100, 70 + 185 * s.T / 100, 0.8);
    laser(inc[0], inc[1], a1);
    // labels: the upper material in the upper right corner (the laser is on the left), the lower one in the lower
    // left corner (the refracted ray goes right), the angles beside their arcs
    lab(`$\\text{${__(s.m1)}},\\ n_1 = ${tx(s.n1, 2)}$`, 588, 14 + fh, 'r', fh, INKC);
    lab(`$\\text{${__(s.m2)}},\\ n_2 = ${tx(s.n2, 2)}$`, 12, 400 - 14, 'l', fh, INKC);
    angLab('$\\alpha_1$', cx, cy, -s.alpha1 / 2, 78, -1, fh);
    angLab('$\\beta$', cx, cy, s.alpha1 / 2, 78, 1, fh);
    if (!s.tir) angLab('$\\alpha_2$', cx, cy, 180 - s.alpha2 / 2, 88, 1, fh);
  }

  // a label on the bisector of an angle (degrees clockwise from up), at least a little to the given side of the normal
  function angLab(str, cx, cy, ang, r, side, fh) {
    p.textSize(fh); const w = p.textWidth(str);
    let x = cx + r * Math.sin(ang * RAD), y = cy - r * Math.cos(ang * RAD) + fh * 0.35;
    const minOff = w / 2 + 8;
    if (side * (x - cx) < minOff) x = cx + side * minOff;
    lab(str, x, y, 'c', fh, INKC);
  }

  function beam(x1, y1, x2, y2, w, alpha, at) {
    p.stroke(...RAY, alpha); p.strokeWeight(w); p.line(x1, y1, x2, y2);
    // an arrowhead at the fraction `at` of the way, clear of the angle labels
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, hx = x1 + ux * L * at, hy = y1 + uy * L * at, h = 9 + w;
    p.noStroke(); p.fill(...RAY, alpha);
    p.triangle(hx + ux * h * 0.6, hy + uy * h * 0.6, hx - ux * h * 0.6 - uy * h * 0.5, hy - uy * h * 0.6 + ux * h * 0.5, hx - ux * h * 0.6 + uy * h * 0.5, hy - uy * h * 0.6 - ux * h * 0.5);
  }

  function laser(x, y, a1) {
    // the laser body behind the ray's start, pointing at the centre
    p.push(); p.translate(x, y); p.rotate(Math.PI - a1);
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...IRONC); p.rect(-8, -2, 16, 40, 3);
    p.fill(...RAY); p.noStroke(); p.rect(-4, -4, 8, 4, 1);
    p.pop();
  }

  // every canvas text: drawn and its ink box pushed to simState.labels (canvas coordinates)
  function lab(str, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(str), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(str, x0, y);
    labels.push({ s: str, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
