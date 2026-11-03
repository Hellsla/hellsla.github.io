// fy7-11 Dispersio: prisma ja sateenkaari. A narrow beam of white light hits the left face of a prism (apex angle A,
// isosceles, in air) at the angle of incidence α1. Seven wavelengths from 405 nm to 656 nm are traced with Snell's
// law n1 sin α1 = n2 sin α2 in vector form; the refractive index of each comes from a three-term Cauchy fit
// n = a + b / λ² + c / λ⁴ (λ in µm) through the material's data: crown glass N-BK7 and water (20 °C) through 405, 589
// and 656 nm (the values of the lesson's table, so the red and violet readouts equal the table), flint glass F2
// through 486, 588 and 656 nm. Air is n = 1. The deviation of a colour is δ = α1 + α4 − A (α4 the exit angle).
// When n sin α3 > 1 at the second face the colour cannot leave: its ray is drawn reflected back into the prism and
// simState.ulosP / ulosV say whether red and violet leave. The picture: a darkened room, the glass prism, the white
// beam, the coloured rays added together (they look white where they overlap), the normals and the continued
// incident ray dashed, a white screen at the right. Static: drawn again on every frame, no animation. Every canvas
// text goes through lab() (simState.labels).
new p5((p) => {
  const MAT = {                                                    // Cauchy coefficients a, b (µm²), c (µm⁴)
    kruunu: [1.50411, 0.00446253, -3.09312e-05],
    flint: [1.59582, 0.00791448, 0.000154174],
    vesi: [1.32293, 0.00361273, -3.98464e-05],
  };
  const LAMBDAS = [656.3, 610, 580, 545, 500, 465, 404.7];       // red … violet (nm)
  const RGB = [[255, 40, 30], [255, 120, 0], [235, 220, 0], [40, 215, 60], [0, 190, 210], [40, 90, 255], [150, 50, 255]];
  const INKC = [31, 41, 51], MUTEDC = [150, 158, 168], PAPERC = [246, 241, 230];
  const T = [262, 74], L = 250;                                    // apex and face length (canvas units)
  let slA, slI, sel, lA, lI, readout, labels = [];

  const nOf = (m, lam) => { const [a, b, c] = MAT[m], x = 1 / Math.pow(lam / 1000, 2); return a + b * x + c * x * x; };
  const unit = (x, y) => { const l = Math.hypot(x, y); return [x / l, y / l]; };
  const refract = (d, nrm, eta) => {                               // nrm: unit normal on the incident side
    const ci = -(d[0] * nrm[0] + d[1] * nrm[1]), k = 1 - eta * eta * (1 - ci * ci);
    if (k < 0) return null;
    const f = eta * ci - Math.sqrt(k);
    return unit(eta * d[0] + f * nrm[0], eta * d[1] + f * nrm[1]);
  };
  const reflect = (d, nrm) => { const k = 2 * (d[0] * nrm[0] + d[1] * nrm[1]); return [d[0] - k * nrm[0], d[1] - k * nrm[1]]; };
  const meet = (p0, d, a, b) => {                                  // ray p0 + t d with the segment a–b: [t, s along a–b]
    const ex = b[0] - a[0], ey = b[1] - a[1], den = d[0] * ey - d[1] * ex;
    if (Math.abs(den) < 1e-12) return [Infinity, -1];
    const t = ((a[0] - p0[0]) * ey - (a[1] - p0[1]) * ex) / den, s = ((a[0] - p0[0]) * d[1] - (a[1] - p0[1]) * d[0]) / den;
    return [t, s];
  };
  const toEdge = (p0, d, H) => {                                   // distance along d to the canvas edge
    let t = 1e9;
    if (d[0] > 1e-9) t = Math.min(t, (600 - p0[0]) / d[0]); if (d[0] < -1e-9) t = Math.min(t, -p0[0] / d[0]);
    if (d[1] > 1e-9) t = Math.min(t, (H - p0[1]) / d[1]); if (d[1] < -1e-9) t = Math.min(t, -p0[1] / d[1]);
    return Math.max(0, t);
  };
  const deg = (r) => r * 180 / Math.PI, rad = (d) => d * Math.PI / 180;

  // the geometry and the rays of the current settings
  const model = () => {
    const A = Number(slA.value()), a1 = Number(slI.value()), m = sel.value(), h = rad(A / 2);
    const B1 = [T[0] - L * Math.sin(h), T[1] + L * Math.cos(h)], B2 = [T[0] + L * Math.sin(h), T[1] + L * Math.cos(h)];
    const outL = [-Math.cos(h), -Math.sin(h)], outR = [Math.cos(h), -Math.sin(h)];
    const P = [T[0] + 0.5 * (B1[0] - T[0]), T[1] + 0.5 * (B1[1] - T[1])];
    const th = Math.atan2(-outL[1], -outL[0]) - rad(a1);              // incident direction: the inward normal turned up by α1
    const d0 = [Math.cos(th), Math.sin(th)];
    const rays = LAMBDAS.map((lam, i) => {
      const n = nOf(m, lam), d1 = refract(d0, outL, 1 / n);
      const [tR, sR] = meet(P, d1, T, B2), [tB, sB] = meet(P, d1, B1, B2);
      if (!(sR >= 0 && sR <= 1 && tR > 0) || (tB > 0 && sB >= 0 && sB <= 1 && tB < tR)) {   // reaches the base first
        return { lam, i, n, d1, Q: [P[0] + tB * d1[0], P[1] + tB * d1[1]], out: false, base: true };
      }
      const Q = [P[0] + tR * d1[0], P[1] + tR * d1[1]];
      const d2 = refract(d1, [-outR[0], -outR[1]], n);
      if (!d2) return { lam, i, n, d1, Q, out: false, refl: reflect(d1, outR) };
      const dev = deg(Math.atan2(d0[0] * d2[1] - d0[1] * d2[0], d0[0] * d2[0] + d0[1] * d2[1]));          // turn from d0 to d2
      return { lam, i, n, d1, Q, d2, out: true, dev };
    });
    const red = rays[0], vio = rays[rays.length - 1];
    const dP = red.out ? red.dev : 0, dV = vio.out ? vio.dev : 0;
    return { A, a1, m, B1, B2, P, outL, outR, d0, rays, nP: red.n, nV: vio.n, dP, dV, dd: red.out && vio.out ? dV - dP : 0,
             ulosP: red.out, ulosV: vio.out, ulos: rays.filter((r) => r.out).length };
  };

  p.setup = () => {
    const cv = p.createCanvas(600, 400).parent('sim-root');
    cv.elt.setAttribute('role', 'img'); cv.elt.setAttribute('aria-label', __('kuva_alt'));
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l1); slA = p.createSlider(30, 70, 60, 5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lI = p.createSpan('').parent(l2); slI = p.createSlider(20, 80, 50, 1).parent(l2);
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('aine')).parent(l3); sel = p.createSelect().parent(l3);
    sel.option(__('kruunu'), 'kruunu'); sel.option(__('flint'), 'flint'); sel.option(__('vesi'), 'vesi'); sel.selected('kruunu');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { A: { input: slA.elt, unit: '°' }, a1: { input: slI.elt, unit: '°' }, aine: { input: sel.elt, unit: '' } },
      reset: () => { slA.value(60); slI.value(50); sel.selected('kruunu'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = model(), H = 400;
    lA.html(__('huippu', { A: s.A })); lI.html(__('tulo', { a: s.a1 }));
    readout.html(s.ulosP && s.ulosV
      ? __('lukemat', { np: tx(s.nP, 4), nv: tx(s.nV, 4), dp: tx(s.dP, 1), dv: tx(s.dV, 1), dd: tx(s.dd, 2) })
      : __('lukemat_tir', { np: tx(s.nP, 4), nv: tx(s.nV, 4), k: s.ulos }));
    window.simState = { A: s.A, a1: s.a1, aine: s.m, nP: s.nP, nV: s.nV, dP: s.dP, dV: s.dV, dd: s.dd,
                        ulosP: s.ulosP, ulosV: s.ulosV, ulos: s.ulos, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.min(24, Math.round((k > 1.2 ? 14 : 15) * k));
    labels = [];
    // the darkened room and the screen
    const c = p.drawingContext, gr = c.createLinearGradient(0, 0, 0, H);
    gr.addColorStop(0, 'rgb(31,41,51)'); gr.addColorStop(1, 'rgb(48,58,70)');
    c.fillStyle = gr; c.fillRect(0, 0, 600, H);
    const xs = 584;
    p.noStroke(); p.fill(...PAPERC); p.rect(xs, 16, 10, H - 32, 2);
    // the prism
    p.stroke(196, 204, 212); p.strokeWeight(2.5); p.fill(208, 230, 251, 55);
    p.triangle(T[0], T[1], s.B2[0], s.B2[1], s.B1[0], s.B1[1]);
    // dashed: the normal at the entry point, the normal at the violet (or red) exit point, the continued incident ray
    dashed(() => {
      p.stroke(...MUTEDC); p.strokeWeight(1.5);
      p.line(s.P[0] + s.outL[0] * 70, s.P[1] + s.outL[1] * 70, s.P[0] - s.outL[0] * 60, s.P[1] - s.outL[1] * 60);
      const ex = s.rays.find((r) => r.out) || s.rays[0];
      if (!ex.base) p.line(ex.Q[0] + s.outR[0] * 70, ex.Q[1] + s.outR[1] * 70, ex.Q[0] - s.outR[0] * 60, ex.Q[1] - s.outR[1] * 60);
      const te = Math.min(toEdge(s.P, s.d0, H), 380);
      p.line(s.P[0], s.P[1], s.P[0] + s.d0[0] * te, s.P[1] + s.d0[1] * te);
    });
    // the white beam from the left edge to the entry point
    const back = [-s.d0[0], -s.d0[1]], tb = toEdge(s.P, back, H), S = [s.P[0] + back[0] * tb, s.P[1] + back[1] * tb];
    p.stroke(255); p.strokeWeight(5); p.line(S[0], S[1], s.P[0], s.P[1]);
    // the coloured rays, added together
    p.blendMode(p.ADD);
    for (const r of s.rays) {
      const col = RGB[r.i];
      p.stroke(...col, 230); p.strokeWeight(2.5); p.line(s.P[0], s.P[1], r.Q[0], r.Q[1]);
      if (r.out) {
        const t = toEdge(r.Q, r.d2, H), E = [r.Q[0] + r.d2[0] * t, r.Q[1] + r.d2[1] * t];
        const tsc = r.d2[0] > 1e-9 ? (xs - r.Q[0]) / r.d2[0] : Infinity;
        const end = tsc < t ? [r.Q[0] + r.d2[0] * tsc, r.Q[1] + r.d2[1] * tsc] : E;
        p.strokeWeight(3); p.line(r.Q[0], r.Q[1], end[0], end[1]);
        if (tsc < t && end[1] > 16 && end[1] < H - 16) { p.noStroke(); p.fill(...col); p.rect(xs, end[1] - 3, 10, 6); }
      } else if (r.refl) {
        p.stroke(...col, 120); p.strokeWeight(2); p.line(r.Q[0], r.Q[1], r.Q[0] + r.refl[0] * 60, r.Q[1] + r.refl[1] * 60);
      }
    }
    p.blendMode(p.BLEND);
    // labels: the apex angle above the apex, α1 beside the entry point, the colour scale at the lower left
    lab(`$A = ${s.A}^\\circ$`, T[0], T[1] - 16, 'c', fh, [230, 236, 242]);
    const bis = unit(s.outL[0] + back[0], s.outL[1] + back[1]);   // between the normal and the incoming beam
    p.noFill(); p.stroke(230, 236, 242); p.strokeWeight(1.5);
    const aN = Math.atan2(s.outL[1], s.outL[0]), aB = Math.atan2(back[1], back[0]);
    let a0 = Math.min(aN, aB), a1 = Math.max(aN, aB); if (a1 - a0 > Math.PI) { const t = a0; a0 = a1; a1 = t + 2 * Math.PI; }
    p.arc(s.P[0], s.P[1], 56, 56, a0, a1);
    lab('$\\alpha_1$', s.P[0] + 50 * bis[0], s.P[1] + 50 * bis[1] + fh * 0.35, 'c', fh, [230, 236, 242]);
    const bw = Math.max(160, Math.round(fh * 8.5)), g2 = c.createLinearGradient(16, 0, 16 + bw, 0);
    [[0, '#8c32ff'], [0.25, '#285aff'], [0.45, '#00bed2'], [0.6, '#28d73c'], [0.75, '#ebdc00'], [0.87, '#ff7800'], [1, '#ff281e']]
      .forEach(([o, col]) => g2.addColorStop(o, col));
    c.fillStyle = g2; c.fillRect(16, H - 16 - fh * 1.3 - 12, bw, 10);
    lab('$400\\,\\text{nm}$', 16, H - 16, 'l', fh, [230, 236, 242]);
    lab('$700\\,\\text{nm}$', 16 + bw, H - 16, 'r', fh, [230, 236, 242]);
    window.simState.labels = labels;
  };

  function dashed(fn) { p.drawingContext.setLineDash([6, 5]); fn(); p.drawingContext.setLineDash([]); }

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
