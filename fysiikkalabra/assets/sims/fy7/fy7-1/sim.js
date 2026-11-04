// fy7-1 Magneetit, magneettinen dipoli ja magneettikenttä: a bar magnet lies east–west on a table seen from above (north
// up), and a compass stands at the distance r from the magnet's centre in the direction φ (measured from east,
// counterclockwise). Model: the magnet is two magnetic poles ±a apart (a = 4 cm), each with a field ∝ 1/d², scaled so
// that on the axis 10 cm from the centre the magnet's field is B_m = 30,0 µT; far away this is the field of a dipole.
// Earth's field adds its horizontal component B_h = 14 µT to the north (southern Finland), or can be left out. The
// needle turns towards the total horizontal field (damped rotation, simulated time · speed); its settled direction θ
// (degrees from north, + east, − west) is computed from the field. Optional: the magnet's own field lines and a grid
// of small compasses showing the total field. The compass can be dragged. Every canvas text goes through lab().
new p5((p) => {
  const A = 0.04, BH = 14;                                                  // m, pole half-separation; µT, Earth's horizontal field
  const C = 30e-6 / (1 / (0.10 - A) ** 2 - 1 / (0.10 + A) ** 2);           // T·m², so that B_m(10 cm on the axis) = 30,0 µT
  const O = [300, 205], PX = 6.5;                                           // the magnet's centre on the canvas; px per cm
  const INKC = [31, 41, 51], MUTED = [107, 116, 128], GREEN = [43, 138, 62], NPOLE = [242, 166, 156], SPOLE = [208, 230, 251];
  let slR, slP, lR, lP, selM, selE, selSpeed, cbLines, cbGrid, readout, cv;
  let labels = [], psi = 65 * Math.PI / 180, omega = 0, drag = false, lines = null, linesFor = null;

  // the field in µT at a point (x east, y north, metres): the magnet's poles and Earth's horizontal component
  const magnetField = (x, y, s) => {
    let bx = 0, by = 0;
    for (const [px, q] of [[s * A, 1], [-s * A, -1]]) {
      const dx = x - px, dy = y, d = Math.hypot(dx, dy), d3 = Math.max(d, 0.004) ** 3;
      bx += q * C * dx / d3; by += q * C * dy / d3;
    }
    return [bx * 1e6, by * 1e6];
  };
  const model = () => {
    const r = Number(slR.value()), phi = Number(slP.value()), s = selM.value() === 'ita' ? 1 : -1, earth = selE.value() === '1';
    const x = r / 100 * Math.cos(phi * Math.PI / 180), y = r / 100 * Math.sin(phi * Math.PI / 180);
    const [mx, my] = magnetField(x, y, s), bh = earth ? BH : 0, tx_ = mx, ty_ = my + bh;
    const Bm = Math.hypot(mx, my), B = Math.hypot(tx_, ty_);
    let th = Math.atan2(tx_, ty_) * 180 / Math.PI;                         // clockwise from north: + east, − west
    if (th <= -179.95) th = 180;
    return { r, phi, s, earth, Bm, Bh: bh, B, th, bx: tx_, by: ty_ };
  };

  p.setup = () => {
    cv = p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const kick = p.createButton(__('heilauta')).parent(controls);
    kick.elt.addEventListener('click', () => { omega += 7; });
    const l1 = p.createElement('label').parent(controls); lR = p.createSpan('').parent(l1); slR = p.createSlider(10, 24, 10, 1).parent(l1);
    const l2 = p.createElement('label').parent(controls); lP = p.createSpan('').parent(l2); slP = p.createSlider(0, 345, 0, 15).parent(l2);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('magneetti')).parent(lm); selM = p.createSelect().parent(lm);
    selM.option(__('n_ita'), 'ita'); selM.option(__('n_lansi'), 'lansi'); selM.selected('ita');
    const le = p.createElement('label').parent(controls); p.createSpan(__('maa')).parent(le); selE = p.createSelect().parent(le);
    selE.option(__('mukana'), '1'); selE.option(__('pois'), '0'); selE.selected('1');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const lk = p.createElement('label').parent(controls); cbLines = p.createCheckbox('', true).parent(lk); p.createSpan(__('viivat')).parent(lk);
    const lg = p.createElement('label').parent(controls); cbGrid = p.createCheckbox('', false).parent(lg); p.createSpan(__('ruudukko')).parent(lg);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // drag the compass: the pointer sets r and φ (snapped to the sliders' steps)
    cv.elt.style.touchAction = 'pan-y'; cv.elt.style.cursor = 'grab';
    cv.elt.setAttribute('role', 'img'); cv.elt.setAttribute('aria-label', __('kuva_alt'));
    const pt = (e) => { const b = cv.elt.getBoundingClientRect(); return [(e.clientX - b.left) / b.width * 600, (e.clientY - b.top) / b.height * p.height]; };
    cv.elt.addEventListener('pointerdown', (e) => {
      const [x, y] = pt(e), c = compassPx(model());
      if (Math.hypot(x - c[0], y - c[1]) > 34) return;
      drag = true; cv.elt.style.touchAction = 'none';
      try { cv.elt.setPointerCapture(e.pointerId); } catch (err) { /* synthetic events */ }
    });
    cv.elt.addEventListener('pointermove', (e) => {
      if (!drag) return;
      const [x, y] = pt(e), dx = x - O[0], dy = O[1] - y;
      const r = Math.min(24, Math.max(10, Math.round(Math.hypot(dx, dy) / PX)));
      const phi = ((Math.round(Math.atan2(dy, dx) * 180 / Math.PI / 15) * 15) % 360 + 360) % 360;
      slR.value(r); slP.value(phi === 360 ? 0 : phi);
    });
    const up = () => { drag = false; cv.elt.style.touchAction = 'pan-y'; };
    cv.elt.addEventListener('pointerup', up); cv.elt.addEventListener('pointercancel', up);
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { r: { input: slR.elt, unit: 'cm' }, phi: { input: slP.elt, unit: '°' }, magneetti: { input: selM.elt, unit: '' }, maa: { input: selE.elt, unit: '' } },
      reset: () => { slR.value(10); slP.value(0); selM.selected('ita'); selE.selected('1'); cbLines.checked(true); cbGrid.checked(false); omega = 0; psi = model().th * Math.PI / 180; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  const compassPx = (m) => [O[0] + m.r * PX * Math.cos(m.phi * Math.PI / 180), O[1] - m.r * PX * Math.sin(m.phi * Math.PI / 180)];

  p.draw = () => {
    const m = model();
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    // the needle: a damped rotation towards the total field (simulated time · speed, small sub-steps)
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()), N = 20, h = dt / N, th = m.th * Math.PI / 180;
    const stiff = m.B > 0.05 ? 3.5 * Math.min(m.B, 60) : 0;
    for (let i = 0; i < N; i++) { omega += (stiff * Math.sin(th - psi) - 2.5 * omega) * h; psi += omega * h; }
    psi = Math.atan2(Math.sin(psi), Math.cos(psi));
    lR.html(__('etaisyys', { r: String(m.r) })); lP.html(__('suunta', { phi: String(m.phi) }));
    readout.html(__('lukemat', { r: String(m.r), phi: String(m.phi), Bm: tx(m.Bm, 1), Bh: tx(m.Bh, 1), B: tx(m.B, 1), th: tx(m.th, 0) }));
    const fh = Math.round(13 * k), U = Math.max(1, 0.8 * k);
    labels = [];
    table();
    if (cbLines.checked()) fieldLines(m.s, U);
    if (cbGrid.checked()) grid(m, U);
    magnet(m.s, fh, U);
    northArrow(m, fh, U);
    compass(m, U);
    window.simState = { r: m.r, phi: m.phi, magneetti: selM.value(), maa: m.earth ? 1 : 0, Bm: m.Bm, Bh: m.Bh, B: m.B, theta: m.th,
                        neula: psi * 180 / Math.PI, omega, viivat: cbLines.checked(), ruudukko: cbGrid.checked(), labels };
  };

  // --- the table top: light wood with a faint grid ---
  function table() {
    grect(0, 0, 600, p.height, [[246, 241, 230], [233, 226, 210]], 0);
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let x = 20; x < 600; x += 40) p.line(x, 0, x, p.height);
    for (let y = 5; y < p.height; y += 40) p.line(0, y, 600, y);
  }

  // --- the magnet's own field lines (pole model), traced once per orientation from the N pole ---
  function fieldLines(s, U) {
    if (linesFor !== s) {
      lines = [];
      const npx = [O[0] + s * A * 100 * PX, O[1]];
      for (let i = 0; i < 16; i++) {
        const a = (i + 0.5) / 16 * 2 * Math.PI;
        let x = npx[0] + 5 * Math.cos(a), y = npx[1] + 5 * Math.sin(a); const pts = [[x, y]];
        for (let n = 0; n < 900; n++) {
          const [bx, by] = magnetField((x - O[0]) / PX / 100, (O[1] - y) / PX / 100, s), b = Math.hypot(bx, by);
          if (b < 1e-9) break;
          x += 3 * bx / b; y -= 3 * by / b; pts.push([x, y]);
          if (x < -10 || x > 610 || y < -10 || y > 410 || Math.hypot(x - (O[0] - s * A * 100 * PX), y - O[1]) < 5) break;
        }
        lines.push(pts);
        const e = pts[pts.length - 1];                                     // a line that leaves the canvas: its mirror image comes into S
        if (Math.hypot(e[0] - (O[0] - s * A * 100 * PX), e[1] - O[1]) > 8) lines.push(pts.map((q) => [2 * O[0] - q[0], q[1]]).reverse());
      }
      linesFor = s;
    }
    for (const L of lines) {
      p.noFill(); p.stroke(...GREEN, 150); p.strokeWeight(1.6 * U);
      p.beginShape(); for (const q of L) p.vertex(q[0], q[1]); p.endShape();
      const j = Math.min(L.length - 2, Math.max(2, Math.round(L.length * 0.35)));   // an arrowhead along each line, pointing along the field
      if (j > 2) arrowHead(L[j], L[j + 1], 7 * U, [...GREEN, 190]);
    }
  }

  // --- a grid of small compass needles showing the total field's direction ---
  function grid(m, U) {
    const c = compassPx(m);
    for (let gx = 40; gx < 600; gx += 40) for (let gy = 25; gy < p.height; gy += 40) {
      if (Math.abs(gx - O[0]) < 52 && Math.abs(gy - O[1]) < 22) continue;
      if (Math.hypot(gx - c[0], gy - c[1]) < 36 || (gx > 520 && gy < 130)) continue;
      const [bx, by] = magnetField((gx - O[0]) / PX / 100, (O[1] - gy) / PX / 100, m.s), ey = by + m.Bh;
      if (Math.hypot(bx, ey) < 0.05) continue;
      const a = Math.atan2(bx, ey);
      needle(gx, gy, a, 9 * U, 2.4 * U, 1);
    }
  }

  function magnet(s, fh, U) {
    const w = 10 * PX, hgt = 24, x0 = O[0] - w / 2, y0 = O[1] - hgt / 2;
    p.stroke(...INKC); p.strokeWeight(2.4);
    const east = s > 0 ? NPOLE : SPOLE, west = s > 0 ? SPOLE : NPOLE;
    p.fill(...west); p.rect(x0, y0, w / 2, hgt, 4, 0, 0, 4);
    p.fill(...east); p.rect(O[0], y0, w / 2, hgt, 0, 4, 4, 0);
    lab(s > 0 ? __('ps') : __('pn'), O[0] - w / 4, O[1] + fh * 0.36, 'c', fh, INKC);
    lab(s > 0 ? __('pn') : __('ps'), O[0] + w / 4, O[1] + fh * 0.36, 'c', fh, INKC);
  }

  // --- north (map north is up) and Earth's horizontal field when it is on ---
  function northArrow(m, fh, U) {
    const x = 566, y0 = 112, y1 = 46;
    p.stroke(...INKC); p.strokeWeight(2.2 * U); p.line(x, y0, x, y1 + 10);
    arrowHead([x, y1 + 12], [x, y1], 11 * U, INKC);
    lab(__('pohjoinen'), 590, y1 - 6 - fh * 0.3, 'r', fh, INKC);
    if (m.earth) {
      const bx = 542; p.stroke(...GREEN); p.strokeWeight(2.6 * U); p.line(bx, y0, bx, y1 + 22);
      arrowHead([bx, y1 + 24], [bx, y1 + 10], 11 * U, GREEN);
      lab(__('bh'), bx - 8, (y0 + y1) / 2 + 14 + fh * 0.36, 'r', fh, GREEN);
    }
  }

  // --- the compass: a housing with a scale, the needle turning towards the total field ---
  function compass(m, U) {
    const [cx, cy] = compassPx(m), R = 21;
    p.noStroke(); p.fill(31, 41, 51, 40); p.circle(cx + 2, cy + 3, 2 * R + 4);
    p.stroke(...INKC); p.strokeWeight(2.4); p.fill(255); p.circle(cx, cy, 2 * R);
    p.strokeWeight(1.2); p.stroke(...MUTED);
    for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4; p.line(cx + (R - 5) * Math.sin(a), cy - (R - 5) * Math.cos(a), cx + (R - 1.5) * Math.sin(a), cy - (R - 1.5) * Math.cos(a)); }
    needle(cx, cy, psi, R - 4, 5, 2);
    p.noStroke(); p.fill(...INKC); p.circle(cx, cy, 4);
  }

  // a needle at (x, y) along the angle a (clockwise from north): the N half arrow-shaped, the S half blunt
  function needle(x, y, a, len, wid, sw) {
    const ux = Math.sin(a), uy = -Math.cos(a), nx = -uy, ny = ux;
    p.stroke(...INKC); p.strokeWeight(sw * 0.6);
    p.fill(...NPOLE); p.triangle(x + ux * len, y + uy * len, x + nx * wid, y + ny * wid, x - nx * wid, y - ny * wid);
    p.fill(...SPOLE); p.quad(x + nx * wid, y + ny * wid, x - ux * len * 0.8 + nx * wid * 0.5, y - uy * len * 0.8 + ny * wid * 0.5,
                             x - ux * len * 0.8 - nx * wid * 0.5, y - uy * len * 0.8 - ny * wid * 0.5, x - nx * wid, y - ny * wid);
  }

  function arrowHead(a, b, s, col) {
    const an = Math.atan2(b[1] - a[1], b[0] - a[0]);
    p.noStroke(); p.fill(...col);
    p.triangle(b[0] + Math.cos(an) * s * 0.4, b[1] + Math.sin(an) * s * 0.4, b[0] - s * Math.cos(an - 0.45), b[1] - s * Math.sin(an - 0.45), b[0] - s * Math.cos(an + 0.45), b[1] - s * Math.sin(an + 0.45));
  }

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
