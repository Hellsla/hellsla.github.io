// fy5-11 Aaltojen heijastuminen ja diffraktio: a rope pulse at a fixed or a free end, and a ripple tank seen from above
// (a straight wall, a gap, an obstacle). One select chooses the situation (tila):
//  kiintea / vapaa: a pulse y = A g(s − s0 − vt) travels along a 5,0 m rope to its end; the end is modelled by an image
//    pulse ∓A g(2L − s − s0 − vt) (fixed end y = 0: inverted; free end ∂y/∂s = 0: not inverted). g is a Gaussian, A = 3,0 cm,
//    v = 2,0 m/s; the run lasts 4,0 s. yh is the reflected pulse's displacement at its centre once it has left the end (t ≥ 3 s).
//  seina: plane wave crests hit a straight wall at the angle alpha from the normal. Huygens: the front reaches two wall points
//    a distance d apart with a path difference d sin(alpha); when it reaches the second, the first one's wavelet has the radius
//    d sin(alpha), and the reflected front is their common tangent, sin(beta) = r1 / d. The crests and the wavelets are drawn.
//  rako / este: the field behind a gap (or an obstacle) of width b is a Huygens sum of point sources λ/8 apart over the gap
//    (2D Kirchhoff: e^{i(kr − π/4)} / sqrt(λ r)· Δy), the obstacle by Babinet (plane wave minus the gap's field).
//    theta is the far-field angle from straight ahead where the gap's amplitude has fallen to half (90° when it never does);
//    AP is the obstacle's amplitude at P, 8,0 cm straight behind it, as a percentage of the free wave.
// The tank is 30 cm × 20 cm, 20 px per cm. Every canvas text goes through lab(), which pushes its ink box to simState.labels.
new p5((p) => {
  const PX = 20, XB = 140, YC = 200, GW = 200, GH = 134, CELL = 3, PERIOD = 1.2;   // tank scale, barrier, field grid, animation period (s)
  const L = 5.0, A = 3.0, S0 = 1.0, V = 2.0, SIG = 0.2, TEND = 4.0, RX0 = 50, RPX = 96, RY = 230, RCM = 18;   // the rope
  const BLUE = [25, 113, 194], GREEN = [43, 138, 62], INKC = [31, 41, 51], MUTEDC = [107, 116, 128], ROPE = [138, 95, 34];
  const ROPE_MODES = ['kiintea', 'vapaa'];
  let btn, selTila, selSpeed, slLam, slA, slB, cbH, lLam, lA, lB, readout, img;
  let t = 0, phase = 0, running = false, fieldKey = '', field = null, theta = 90, AP = 100, yh = null, fh = 13, k = 1, labels = [];

  // --- the physics ---
  const g = (u) => Math.exp(-u * u / (2 * SIG * SIG));
  const ropeY = (s, tt, sgn) => A * (g(s - S0 - V * tt) + sgn * g(2 * L - s - S0 - V * tt));          // cm
  function sources(w, lam) { const N = Math.max(2, Math.ceil(w / (lam / 8))), out = []; for (let j = 0; j < N; j++) out.push(-w / 2 + w * (j + 0.5) / N); return { ys: out, dy: w / N }; }
  function slit(w, lam, x, y) {                                    // complex amplitude of a gap of width w at (x > 0, y), cm
    const { ys, dy } = sources(w, lam), kk = 2 * Math.PI / lam; let re = 0, im = 0;
    for (const yj of ys) { const r = Math.hypot(x, y - yj), a = dy / Math.sqrt(lam * r), ph = kk * r - Math.PI / 4; re += a * Math.cos(ph); im += a * Math.sin(ph); }
    return [re, im];
  }
  function thetaHalf(b, lam) {                                     // far-field half-amplitude angle of the gap, degrees
    const { ys } = sources(b, lam), kk = 2 * Math.PI / lam;
    const amp = (th) => { let re = 0, im = 0; const s = Math.sin(th); for (const y of ys) { re += Math.cos(kk * y * s); im -= Math.sin(kk * y * s); } return Math.hypot(re, im); };
    const A0 = amp(0);
    for (let i = 0; i <= 900; i++) if (amp(i / 10 * Math.PI / 180) < 0.5 * A0) return i / 10;
    return 90;
  }
  function obstacleAP(b, lam) { const D = 8.0, kk = 2 * Math.PI / lam, [re, im] = slit(b, lam, D, 0); return 100 * Math.hypot(Math.cos(kk * D) - re, Math.sin(kk * D) - im); }
  function computeField(tila, lam, b) {                            // complex amplitude on the grid, once per change
    const key = tila + '|' + lam + '|' + b; if (key === fieldKey) return; fieldKey = key;
    const kk = 2 * Math.PI / lam; field = new Float32Array(GW * GH * 2);
    for (let j = 0; j < GH; j++) for (let i = 0; i < GW; i++) {
      const x = ((i + 0.5) * CELL - XB) / PX, y = ((j + 0.5) * CELL - YC) / PX; let re = Math.cos(kk * x), im = Math.sin(kk * x);
      if (x > 0) { const [sr, si] = slit(b, lam, x, y); if (tila === 'rako') { re = sr; im = si; } else { re -= sr; im -= si; } }
      field[2 * (j * GW + i)] = re; field[2 * (j * GW + i) + 1] = im;
    }
  }

  const P = () => ({ tila: selTila.value(), lam: Number(slLam.value()), alpha: Number(slA.value()), b: Number(slB.value()), h: cbH.checked() });
  const isRope = (tila) => ROPE_MODES.includes(tila);
  function newSituation() { t = 0; yh = null; running = !isRope(selTila.value()); }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (isRope(selTila.value()) && t >= TEND - 1e-9) { t = 0; yh = null; }
      running = true;
    });
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('tilanne')).parent(l0); selTila = p.createSelect().parent(l0);
    for (const m of ['kiintea', 'vapaa', 'seina', 'rako', 'este']) selTila.option(__('tila_' + m), m);
    selTila.selected('kiintea');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const l1 = p.createElement('label').parent(controls); lLam = p.createSpan('').parent(l1); slLam = p.createSlider(1, 3, 2, 0.5).parent(l1);
    const l2 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l2); slA = p.createSlider(0, 75, 30, 5).parent(l2);
    const l3 = p.createElement('label').parent(controls); lB = p.createSpan('').parent(l3); slB = p.createSlider(0.5, 8, 4, 0.5).parent(l3);
    cbH = p.createCheckbox(__('huygens'), false).parent(controls);
    selTila.elt.addEventListener('change', newSituation);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    img = p.createImage(GW, GH);
    newSituation();
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tila: { input: selTila.elt, unit: '' }, lam: { input: slLam.elt, unit: 'cm' }, alpha: { input: slA.elt, unit: '°' }, b: { input: slB.elt, unit: 'cm' } },
      reset: () => { selTila.selected('kiintea'); slLam.value(2); slA.value(30); slB.value(4); cbH.checked(false); newSituation(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const S = P(), rope = isRope(S.tila), sgn = S.tila === 'kiintea' ? -1 : 1;
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    if (running) {
      if (rope) { t += dt; if (t >= TEND) { t = TEND; running = false; } }
      else phase = (phase + dt / PERIOD) % 1;
    }
    if (rope && t >= 3.0 - 1e-9) yh = ropeY(2 * L - S0 - V * t, t, sgn);
    const yEnd = ropeY(L, t, sgn);
    // Huygens at the wall: wavelet of the first of two points d apart when the front reaches the second
    const d = 10, r1 = d * Math.sin(S.alpha * Math.PI / 180), beta = Math.asin(Math.min(1, r1 / d)) * 180 / Math.PI;
    const key = S.b + '|' + S.lam;
    if (key !== p.__tk) { p.__tk = key; theta = thetaHalf(S.b, S.lam); AP = obstacleAP(S.b, S.lam); }
    if (!rope && S.tila !== 'seina') computeField(S.tila, S.lam, S.b);
    lLam.html(__('lbl_lam', { l: tx(S.lam, 1) }));
    lA.html(__('lbl_alpha', { a: String(S.alpha) }));
    lB.html(__(S.tila === 'este' ? 'lbl_b_este' : 'lbl_b', { b: tx(S.b, 1) }));
    const bt = running ? __('pysayta') : __('kaynnista');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    const suhde = S.b / S.lam;
    if (rope) readout.html(__(yh === null ? 'lukemat_koysi_odota' : 'lukemat_koysi', { t: tx(t, 1), y0: tx(A, 1), yh: yh === null ? '' : sgnTx(yh, 1), ye: sgnTx(yEnd, 1) }));
    else if (S.tila === 'seina') readout.html(__('lukemat_seina', { a: String(S.alpha), be: tx(beta, 0), pi: tx(90 - beta, 0) }));
    else if (S.tila === 'rako') readout.html(__(theta >= 90 ? 'lukemat_rako_koko' : 'lukemat_rako', { l: tx(S.lam, 1), b: tx(S.b, 1), s: tx(suhde, 2), th: tx(theta, 0) }));
    else readout.html(__('lukemat_este', { l: tx(S.lam, 1), b: tx(S.b, 1), s: tx(suhde, 2), ap: tx(AP, 0) }));
    window.simState = { tila: S.tila, lam: S.lam, alpha: S.alpha, b: S.b, huygens: S.h, t, running, yh, yEnd, beta, pinta: 90 - beta,
      suhde, theta, AP, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    k = Math.max(1, 600 / cw); fh = cw < 500 ? Math.round(14 * k) : 15;
    labels = [];
    p.background(255);
    if (rope) drawRope(S, sgn); else if (S.tila === 'seina') drawWall(S, beta); else drawField(S);
    window.simState.labels = labels;
  };

  // --- the rope seen from the side ---
  function drawRope(S, sgn) {
    grect(0, 0, 600, 400, [[246, 241, 230], [255, 255, 255]]);
    const X = (s) => RX0 + RPX * s, Yy = (y) => RY - RCM * y, xe = X(L);
    dashed(RX0, RY, xe, RY, MUTEDC, 1.5);
    // the left end: a handle
    p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2); p.rect(RX0 - 34, RY - 14, 30, 28, 6);
    // the far end
    if (S.tila === 'kiintea') {
      p.fill(108, 117, 125); p.stroke(...INKC); p.strokeWeight(2.5); p.rect(xe + 6, RY - 120, 34, 240, 3);
      p.stroke(...INKC); p.strokeWeight(1.5); for (let y = RY - 112; y < RY + 120; y += 16) p.line(xe + 12, y + 10, xe + 34, y - 6);
      p.fill(196, 204, 212); p.stroke(...INKC); p.strokeWeight(2); p.circle(xe + 2, RY, 12);
    } else {
      p.noStroke(); p.fill(138, 150, 163); p.rect(xe - 4, 70, 8, 300, 4);
      p.fill(108, 117, 125); p.rect(xe - 26, 366, 52, 12, 3);
      p.noFill(); p.stroke(...INKC); p.strokeWeight(3); p.ellipse(xe, Yy(ropeY(L, t, sgn)), 26, 12);
    }
    // the rope
    p.noFill(); p.stroke(...ROPE); p.strokeWeight(5); p.beginShape();
    for (let i = 0; i <= 250; i++) { const s = L * i / 250; p.vertex(X(s), Yy(ropeY(s, t, sgn))); }
    p.endShape();
    lab(__(S.tila === 'kiintea' ? 'lbl_kiintea' : 'lbl_vapaa'), 594, 392, 'r', INKC);
    // the direction of travel (velocity colour) over the pulse
    const inc = t < (L - S0) / V, sc = inc ? S0 + V * t : 2 * L - S0 - V * t;
    if (Math.abs(sc - L) > 0.45) {
      const xc = X(sc), dir = inc ? 1 : -1, y = 70;
      arrow(xc - dir * 32, y, xc + dir * 32, y, BLUE, 3);
      lab('$v$', xc + dir * 44, y + fh * 0.36, dir > 0 ? 'l' : 'r', BLUE);
    }
  }

  // --- the wall seen from above: incident (blue) and reflected (green) crests, rays, the normal, the angles ---
  function drawWall(S, beta) {
    const yw = 44, O = [300, yw], lam = S.lam * PX, al = S.alpha * Math.PI / 180, be = beta * Math.PI / 180;
    grect(0, yw, 600, 400 - yw, [[208, 230, 251], [238, 245, 249]]);
    const dIn = [Math.sin(al), -Math.cos(al)], dR = [Math.sin(be), Math.cos(be)], sft = phase * lam;
    const c = p.drawingContext; c.save(); c.beginPath(); c.rect(0, yw, 600, 400 - yw); c.clip();
    crests(dIn, O, sft, lam, BLUE);
    crests(dR, O, sft, lam, GREEN);
    if (S.h) {                                                     // Huygens wavelets from points of the wall
      p.noFill(); p.stroke(255); p.strokeWeight(2);
      for (let x = 40; x <= 560; x += 40) {
        const r0 = ((sft - dIn[0] * (x - O[0])) % lam + lam) % lam;
        for (let m = 0; m < 2; m++) p.arc(x, yw, 2 * (r0 + m * lam), 2 * (r0 + m * lam), 0, Math.PI);
        p.noStroke(); p.fill(255); p.circle(x, yw, 6); p.noFill(); p.stroke(255);
      }
    }
    c.restore();
    // the wall
    p.fill(196, 204, 212); p.stroke(...INKC); p.strokeWeight(2.5); p.rect(-4, 14, 608, yw - 14);
    p.stroke(...MUTEDC); p.strokeWeight(1.5); for (let x = 8; x < 600; x += 18) p.line(x, yw - 4, x + 12, 18);
    // the normal and the rays to and from O
    dashed(O[0], yw, O[0], 392, INKC, 2);
    const R = 250, s0 = [O[0] - R * dIn[0], O[1] - R * dIn[1]], e0 = [O[0] + R * dR[0], O[1] + R * dR[1]];
    arrow(s0[0], s0[1], O[0] - 6 * dIn[0], O[1] - 6 * dIn[1], INKC, 3);
    arrow(O[0], O[1], e0[0], e0[1], INKC, 3);
    p.noFill(); p.strokeWeight(3);
    p.stroke(...BLUE); if (al > 0.01) p.arc(O[0], O[1], 120, 120, Math.PI / 2, Math.PI / 2 + al);
    p.stroke(...GREEN); if (be > 0.01) p.arc(O[0], O[1], 136, 136, Math.PI / 2 - be, Math.PI / 2);
    const ma = Math.max(al / 2, 0.3), mb = Math.max(be / 2, 0.3);
    lab('$\\alpha$', O[0] - 100 * Math.sin(ma), O[1] + 100 * Math.cos(ma) + fh * 0.36, 'c', BLUE, true);
    lab('$\\beta$', O[0] + 104 * Math.sin(mb), O[1] + 104 * Math.cos(mb) + fh * 0.36, 'c', GREEN, true);
    lab(__('lbl_normaali'), O[0] + 10, 388, 'l', INKC, true);
    lab(__('lbl_seina'), 594, 12 + 0.8 * fh, 'r', INKC, true);
  }
  function crests(dir, O, sft, lam, col) {
    const perp = [-dir[1], dir[0]];
    p.stroke(...col, 210); p.strokeWeight(2.5); p.noFill();
    for (let n = -40; n <= 40; n++) {
      const cc = sft + n * lam; if (Math.abs(cc) > 760) continue;
      const cx = O[0] + cc * dir[0], cy = O[1] + cc * dir[1];
      p.line(cx - 900 * perp[0], cy - 900 * perp[1], cx + 900 * perp[0], cy + 900 * perp[1]);
    }
  }

  // --- the gap or the obstacle seen from above: the water surface from the Huygens sum ---
  function drawField(S) {
    const cs = Math.cos(2 * Math.PI * phase), sn = Math.sin(2 * Math.PI * phase);
    img.loadPixels();
    for (let q = 0; q < GW * GH; q++) {
      const h = Math.max(-1, Math.min(1, field[2 * q] * cs + field[2 * q + 1] * sn)), u = (h + 1) / 2, o = 4 * q;
      img.pixels[o] = 40 + u * 190; img.pixels[o + 1] = 100 + u * 142; img.pixels[o + 2] = 168 + u * 84; img.pixels[o + 3] = 255;
    }
    img.updatePixels();
    p.image(img, 0, 0, GW * CELL, GH * CELL);
    const half = S.b * PX / 2, lam = S.lam * PX;
    if (S.h && S.tila === 'rako') {                                // wavelets from points of the gap
      const n = Math.min(5, Math.max(1, Math.round(S.b / S.lam) + 1)), r0 = phase * lam;
      p.noFill(); p.stroke(255); p.strokeWeight(2);
      for (let j = 0; j < n; j++) {
        const y = n === 1 ? YC : YC - half + 2 * half * (j + 0.5) / n;
        for (let m = 0; m < 3; m++) p.arc(XB, y, 2 * (r0 + m * lam), 2 * (r0 + m * lam), -Math.PI / 2, Math.PI / 2);
        p.noStroke(); p.fill(255); p.circle(XB, y, 6); p.noFill(); p.stroke(255);
      }
    }
    p.fill(196, 204, 212); p.stroke(...INKC); p.strokeWeight(2.5);
    if (S.tila === 'rako') { p.rect(XB - 6, -4, 12, YC - half + 4); p.rect(XB - 6, YC + half, 12, 404 - YC - half); }
    else p.rect(XB - 6, YC - half, 12, 2 * half);
    // the wave arrives from the left (velocity colour)
    p.noStroke(); p.fill(255, 255, 255, 225); p.rect(12, 358, 118, 30, 5);
    arrow(22, 373, 92, 373, BLUE, 3);
    lab('$v$', 100, 373 + fh * 0.36, 'l', BLUE);
    lab('$b$', XB - 16, YC + fh * 0.36, 'r', INKC, true);
    if (S.tila === 'rako') {
      const th = theta * Math.PI / 180;
      for (const sgn of [-1, 1]) dashed(XB, YC, XB + 460 * Math.cos(th), YC + sgn * 460 * Math.sin(th), INKC, 2);
      const at = theta >= 20 ? th / 2 : th + 0.16, rr = theta >= 20 ? 120 : 150;
      lab('$\\theta$', XB + rr * Math.cos(at), YC - rr * Math.sin(at) + fh * 0.36, 'c', INKC, true);
    } else {
      const xp = XB + 8 * PX;
      p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5); p.circle(xp, YC, 12);
      lab('$P$', xp, YC - 14, 'c', INKC, true);
    }
  }

  // --- helpers ---
  function dashed(x1, y1, x2, y2, col, w) { p.stroke(...col); p.strokeWeight(w); p.drawingContext.setLineDash([7, 6]); p.line(x1, y1, x2, y2); p.drawingContext.setLineDash([]); }
  function arrow(x1, y1, x2, y2, col, w) {
    const a = Math.atan2(y2 - y1, x2 - x1), hl = 14, hw = 6;
    p.stroke(...col); p.strokeWeight(w); p.line(x1, y1, x2 - hl * 0.8 * Math.cos(a), y2 - hl * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...col);
    p.triangle(x2, y2, x2 - hl * Math.cos(a) + hw * Math.sin(a), y2 - hl * Math.sin(a) - hw * Math.cos(a), x2 - hl * Math.cos(a) - hw * Math.sin(a), y2 - hl * Math.sin(a) + hw * Math.cos(a));
  }
  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col, bg) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 6), 600 - w - 6);
    y = Math.min(Math.max(y, 0.8 * fh), 400 - 0.3 * fh);
    if (bg) { p.noStroke(); p.fill(255, 255, 255, 225); p.rect(x0 - 4, y - 0.85 * fh, w + 8, 1.15 * fh, 4); }   // a backing on the water
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fh, x1: x0 + w, y1: y + 0.25 * fh });
  }
  function grect(x, y, w, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, w, h); c.restore();
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
  const sgnTx = (x, d) => { const s = tx(x, d); return Number(s.replace(DEC, '.')) > 0 ? '+' + s : s; };
});
