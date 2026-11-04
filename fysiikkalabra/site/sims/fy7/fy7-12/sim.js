// fy7-12 Kokonaisheijastuminen ja valokuitu: a laser in air shines into the flat end face of a straight fibre core
// (n1 = 1,48) that is surrounded by a medium of refractive index n2 (slider, 1,00 = air ... 1,47). Side view, not to
// scale. Model: at the end face 1,00 · sin θ = n1 sin θ1 (θ from the fibre axis, the face's normal); inside, the ray
// meets the core wall at α = 90° − θ1 from the wall's normal. The critical angle is sin α_r = n2 / n1. When α > α_r
// the ray reflects totally at every hit; otherwise at every hit part of it refracts out (n1 sin α = n2 sin β) and the
// part that reflects is drawn fainter (illustration only: the brightness is not computed). Only the transmitted ray
// is drawn at the end face. Static: drawn again on every frame, no animation. Every canvas text goes through lab().
new p5((p) => {
  const N1 = 1.48;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RAYC = [230, 73, 128], CORE = [165, 216, 255], AIR = [250, 250, 250];
  const CLADMAX = [208, 230, 251], LASER = [73, 80, 87];
  const XF = 150, XE = 600, YT = 64, YB = 326, YC = 195, HC = 60;          // end face, medium block, core
  let slT, slN, lT, lN, readout, labels = [];

  const deg = (r) => r * 180 / Math.PI, rad = (d) => d * Math.PI / 180;
  const state = () => {
    const theta = Number(slT.value()), n2 = Number(slN.value());
    const theta1 = deg(Math.asin(Math.sin(rad(theta)) / N1));
    const alpha = 90 - theta1, alphar = deg(Math.asin(n2 / N1));
    return { theta, n1: N1, n2, theta1, alpha, alphar, tir: alpha > alphar };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lT = p.createSpan('').parent(l1); slT = p.createSlider(0, 60, 10, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lN = p.createSpan('').parent(l2); slN = p.createSlider(1, 1.47, 1.46, 0.01).parent(l2);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { theta: { input: slT.elt, unit: '°' }, n2: { input: slN.elt, unit: '' } },
      reset: () => { slT.value(10); slN.value(1.46); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lT.html(__('kulma', { t: tx(s.theta, 0) })); lN.html(__('n2', { n: tx(s.n2, 2) }));
    readout.html(__(s.tir ? 'lukemat_pysyy' : 'lukemat_vuoto', { a: tx(s.alpha, 2), ar: tx(s.alphar, 2), t1: tx(s.theta1, 2) }));
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.round((k > 1.2 ? 14 : 13) * k), H = k > 1.2 ? 470 : 400;   // a phone: room for the larger legend
    if (p.__H !== H) { p.__H = H; p.resizeCanvas(600, H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(...AIR);
    const hits = scene(s, fh);
    legend(s, fh);
    window.simState = { theta: s.theta, n1: s.n1, n2: s.n2, theta1: s.theta1, alpha: s.alpha, alphar: s.alphar, tir: s.tir, hits, labels };
  };

  // --- the medium block, the core, the laser and the ray; returns the number of wall hits drawn ---
  function scene(s, fh) {
    const t = (s.n2 - 1) / 0.47, med = AIR.map((v, i) => v + (CLADMAX[i] - v) * t);
    const y1 = YC - HC / 2, y2 = YC + HC / 2;
    p.noStroke(); p.fill(...med); p.rect(XF, YT, XE - XF, YB - YT);
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.line(XF, YT, XE, YT); p.line(XF, YB, XE, YB);
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...CORE); p.rect(XF, y1, XE - XF + 4, HC);
    p.line(XF, YT, XF, YB);
    // the end face's normal = the fibre axis, dashed, out into the air
    dashed(XF - 110, YC, XF + 30, YC);
    // the laser in air, aimed at the middle of the end face at θ above the axis
    const th = rad(s.theta), L = 80;
    const lx = XF - L * Math.cos(th), ly = YC - L * Math.sin(th);
    p.push(); p.translate(lx, ly); p.rotate(th);
    p.stroke(...INKC); p.strokeWeight(2); p.fill(...LASER); p.rect(-60, -11, 54, 22, 4);
    p.fill(...RAYC); p.noStroke(); p.rect(-8, -5, 3, 10); p.pop();
    rayLine(lx, ly, XF, YC, 255, 3);
    // the angle θ at the end face
    if (s.theta > 0) { p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5); p.arc(XF, YC, 70, 70, Math.PI, Math.PI + th); }
    if (s.theta >= 15) lab('$\\theta$', XF - 52 * Math.cos(th / 2) - 6, YC - 52 * Math.sin(th / 2) + fh * 0.3, 'c', fh, INKC);
    else lab('$\\theta$', XF - 46, YC + fh * 1.25, 'c', fh, INKC);
    // inside: bounce between the walls until the right edge; leak at every hit when α ≤ α_r
    const t1 = rad(s.theta1);
    let x = XF, y = YC, dy = 1, alphaI = 255, hits = 0;
    if (s.theta1 < 1e-9) { rayLine(XF, YC, XE, YC, 255, 3); return 0; }
    while (x < XE && alphaI > 12) {
      const yw = dy > 0 ? y2 : y1, xw = x + Math.abs(yw - y) / Math.tan(t1);
      if (xw >= XE) { rayLine(x, y, XE, y + dy * (XE - x) * Math.tan(t1), alphaI, 3); break; }
      rayLine(x, y, xw, yw, alphaI, 3);
      hits++;
      if (hits === 1) angleAt(xw, yw, dy, s, fh);
      if (!s.tir) {                                                // refracted out into the medium
        const b = Math.asin(Math.min(1, N1 * Math.sin(rad(s.alpha)) / s.n2));
        const yo = dy > 0 ? YB : YT, len = Math.abs(yo - yw) / Math.cos(b);
        let xo = xw + len * Math.sin(b), yo2 = yo;
        if (xo > XE) { xo = XE; yo2 = yw + dy * (XE - xw) / Math.tan(b); }
        rayLine(xw, yw, xo, yo2, alphaI * 0.9, 2.5);
        alphaI *= 0.5;
      }
      x = xw; y = yw; dy = -dy;
    }
    return hits;
  }

  function angleAt(xw, yw, dy, s, fh) {
    // the wall's normal (dashed) and the arc from the normal into the core to the incoming ray
    dashed(xw, yw - dy * 50, xw, yw + dy * 34);
    const up = dy > 0 ? -Math.PI / 2 : Math.PI / 2, back = dy > 0 ? Math.PI + rad(s.theta1) : Math.PI - rad(s.theta1);
    const a1 = Math.min(up, back), a2 = Math.max(up, back);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(1.5);
    if (dy > 0) p.arc(xw, yw, 52, 52, back - 2 * Math.PI, up); else p.arc(xw, yw, 52, 52, a1, a2);
    const bis = (up + (dy > 0 ? back - 2 * Math.PI : back)) / 2;
    lab('$\\alpha$', xw + 42 * Math.cos(bis), yw + 42 * Math.sin(bis) + fh * 0.3, 'c', fh, INKC);
  }

  // --- the legend under the block: the core's and the medium's refractive indices ---
  function legend(s, fh) {
    const t = (s.n2 - 1) / 0.47, med = AIR.map((v, i) => v + (CLADMAX[i] - v) * t);
    const ya = YB + 14 + fh * 0.9, yb = ya + fh * 1.9, sw = fh * 1.3;
    p.stroke(...INKC); p.strokeWeight(1.5);
    p.fill(...CORE); p.rect(16, ya - fh * 0.75, sw, fh * 0.9, 2);
    p.fill(...med); p.rect(16, yb - fh * 0.75, sw, fh * 0.9, 2);
    lab(`$\\text{${__('ydin')}},\\ n_1 = ${tx(N1, 2)}$`, 24 + sw, ya, 'l', fh, INKC);
    lab(`$\\text{${__('aine')}},\\ n_2 = ${tx(s.n2, 2)}$`, 24 + sw, yb, 'l', fh, INKC);
  }

  function rayLine(x1, y1, x2, y2, a, w) { p.stroke(...RAYC, a); p.strokeWeight(w); p.line(x1, y1, x2, y2); }
  function dashed(x1, y1, x2, y2) {
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(x1, y1, x2, y2); p.drawingContext.setLineDash([]);
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
