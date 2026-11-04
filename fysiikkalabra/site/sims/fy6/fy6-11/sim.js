// fy6-11 Homogeeninen sähkökenttä: two parallel metal plates (length 20 cm) connected to a high-voltage source U at the
// distance d, and a small charged ball q held by a force sensor at the place (x, h). The field is not set by a formula:
// each plate is split into 40 strips of constant surface charge, the strip charges are solved so that the plates are
// conductors at the potentials +U/2 and -U/2 (2D strip potentials, Gaussian elimination), and the field anywhere is the
// sum of the strips' exact fields (lessons/FY6/fy6-11/lesson-answers.py computes the same model). Between the plates, away
// from the ends, the field is uniform and U/d emerges; at the ends it bends and weakens, and outside the gap it is
// small. The readout shows only the sensor's force F = |q E| and its direction; E itself is not displayed, so the
// student computes E = F : q. Field lines (traced along E, their number proportional to the field between the
// plates) or field vectors (length proportional to E) are drawn in green, the force on the ball as a red arrow
// (0,3 px per µN; 2300 px per metre). Static picture, so no speed control. Every canvas text goes through lab(), which pushes its box to
// simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const L = 0.20, N = 40, SC = 2300, CX = 300, CY = 205;           // plate length (m), strips per plate, px per m, centre
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], FIELD = [43, 138, 62], FORCE = [201, 42, 42];
  const POSL = [242, 166, 156], NEGL = [208, 230, 251], METAL = [196, 204, 212], EDGE = [138, 150, 163];
  let slU, slD, slQ, slX, slH, selField, lU, lD, lQ, lX, lH, readout;
  let fs = 13, sk = 1, labels = [];
  const cache = {};

  // ---- the model: strip charges of two conductor plates (per volt), then the field anywhere ----
  function Fp(u, y) {                       // integral of ln r over a strip, the strip's potential up to a constant
    const r2 = u * u + y * y;
    let v = (r2 > 0 ? 0.5 * u * Math.log(r2) : 0) - u;
    if (y !== 0) v += y * Math.atan(u / y);
    return v;
  }
  function build(d) {
    const w = L / N, S = [];
    for (const yp of [d / 2, -d / 2]) for (let j = 0; j < N; j++) S.push([-L / 2 + j * w, -L / 2 + (j + 1) * w, yp]);
    const n = S.length, M = [], r = [];
    for (let i = 0; i < n; i++) {
      const cx = (S[i][0] + S[i][1]) / 2, row = [];
      for (const [a, b, y] of S) row.push(-(Fp(b - cx, S[i][2] - y) - Fp(a - cx, S[i][2] - y)));
      M.push(row); r.push(S[i][2] > 0 ? 0.5 : -0.5);
    }
    for (let c = 0; c < n; c++) {             // Gaussian elimination with partial pivoting
      let pv = c;
      for (let k = c + 1; k < n; k++) if (Math.abs(M[k][c]) > Math.abs(M[pv][c])) pv = k;
      [M[c], M[pv]] = [M[pv], M[c]]; [r[c], r[pv]] = [r[pv], r[c]];
      for (let k = c + 1; k < n; k++) {
        const f = M[k][c] / M[c][c];
        if (f) { for (let m = c; m < n; m++) M[k][m] -= f * M[c][m]; r[k] -= f * r[c]; }
      }
    }
    const s = new Array(n).fill(0);
    for (let k = n - 1; k >= 0; k--) { let t = r[k]; for (let m = k + 1; m < n; m++) t -= M[k][m] * s[m]; s[k] = t / M[k][k]; }
    return { S, s };
  }
  function model(d) { const k = d.toFixed(3); if (!cache[k]) cache[k] = Object.assign(build(d), { lines: {}, vecs: null }); return cache[k]; }
  function E1(m, x, y) {                    // the field per volt of plate voltage (1/m) at (x, y), y from the midline
    let ex = 0, ey = 0;
    for (let j = 0; j < m.S.length; j++) {
      const [a, b, yp] = m.S[j], sj = m.s[j];
      let yy = y - yp; if (Math.abs(yy) < 1e-12) yy = 1e-12;
      ex += sj * 0.5 * Math.log(((x - a) ** 2 + yy * yy) / ((x - b) ** 2 + yy * yy));
      ey += sj * (Math.atan((b - x) / yy) - Math.atan((a - x) / yy));
    }
    return [ex, ey];
  }
  // field lines from the inner face of the + plate, traced along E (midpoint steps of 0,5 mm) to the - plate or the edge
  function lines(m, d, count) {
    if (m.lines[count]) return m.lines[count];
    const out = [], ds = 0.0005;
    for (let i = 0; i < count; i++) {
      let x = -L / 2 + (i + 0.5) * L / count, y = d / 2 - 1e-4;
      const pts = [[x, y]];
      for (let k = 0; k < 1600; k++) {
        let [ex, ey] = E1(m, x, y), e = Math.hypot(ex, ey); if (e < 1e-9) break;
        const xm = x + ex / e * ds / 2, ym = y + ey / e * ds / 2;
        [ex, ey] = E1(m, xm, ym); e = Math.hypot(ex, ey); if (e < 1e-9) break;
        x += ex / e * ds; y += ey / e * ds;
        if (Math.abs(x) > 0.13 || Math.abs(y) > 0.088) { pts.push([x, y]); break; }
        if (y <= -d / 2 && Math.abs(x) <= L / 2 + 0.002) { pts.push([x, -d / 2]); break; }
        if (k % 2 === 1) pts.push([x, y]);
      }
      out.push(pts);
    }
    return (m.lines[count] = out);
  }
  function vectors(m, d) {
    if (m.vecs) return m.vecs;
    const out = [], rows = [d / 4, 0, -d / 4, d / 2 + 0.02, -d / 2 - 0.02, d / 2 + 0.05, -d / 2 - 0.05].filter((y) => Math.abs(y) < 0.078);
    for (const y of rows) for (let x = -0.12; x <= 0.1201; x += 0.02) { const [ex, ey] = E1(m, x, y); out.push([x, y, ex, ey]); }
    return (m.vecs = out);
  }

  const params = () => {
    const d = Number(slD.value()) / 100;
    let h = Number(slH.value());
    if (h > d * 100 - 0.5) { h = d * 100 - 0.5; slH.value(h); }
    return { U: Number(slU.value()), d, q: Number(slQ.value()), x: Number(slX.value()), h, field: selField.value() };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const mk = (min, max, v, st) => { const l = p.createElement('label').parent(controls), s = p.createSpan('').parent(l); return [s, p.createSlider(min, max, v, st).parent(l)]; };
    [lU, slU] = mk(0, 3, 2, 0.5);
    [lD, slD] = mk(2, 6, 4, 1);
    [lQ, slQ] = mk(-3, 3, 2, 1);
    [lX, slX] = mk(-12, 12, 0, 1);
    [lH, slH] = mk(0.5, 5.5, 2, 0.5);
    const lf = p.createElement('label').parent(controls); p.createSpan(__('kentta')).parent(lf); selField = p.createSelect().parent(lf);
    selField.option(__('viivat'), 'viivat'); selField.option(__('vektorit'), 'vektorit'); selField.option(__('piilossa'), 'piilossa'); selField.selected('viivat');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { U: { input: slU.elt, unit: 'kV' }, d: { input: slD.elt, unit: 'cm' }, q: { input: slQ.elt, unit: 'nC' },
        x: { input: slX.elt, unit: 'cm' }, h: { input: slH.elt, unit: 'cm' }, kentta: { input: selField.elt } },
      reset: () => { slU.value(2); slD.value(4); slQ.value(2); slX.value(0); slH.value(2); selField.selected('viivat'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = params(), m = model(P.d);
    const [ex1, ey1] = E1(m, P.x / 100, P.h / 100 - P.d / 2);
    const Ex = P.U * 1000 * ex1, Ey = P.U * 1000 * ey1, E = Math.hypot(Ex, Ey);
    const Fx = P.q * 1e-9 * Ex * 1e6, Fy = P.q * 1e-9 * Ey * 1e6, F = Math.hypot(Fx, Fy);   // µN
    const dir = F < 1e-9 ? 'dir_ei' : Math.abs(Fx) < 0.05 * F ? (Fy < 0 ? 'dir_alas' : 'dir_ylos') : (Fy < 0 ? 'dir_vino_alas' : 'dir_vino_ylos');
    lU.html(__('u_lbl', { u: tx(P.U, 1) })); lD.html(__('d_lbl', { d: tx(P.d * 100, 1) }));
    lQ.html(__('q_lbl', { q: (P.q > 0 ? '+' : '') + tx(P.q, 1) })); lX.html(__('x_lbl', { x: tx(P.x, 0) })); lH.html(__('h_lbl', { h: tx(P.h, 1) }));
    readout.html(__('lukema', { f: tx(F, F >= 100 ? 0 : F >= 10 ? 1 : 2), dir: __(dir) }));
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const k = Math.max(1, 600 / cw);
    sk = cw < 500 ? k : 1;
    fs = cw < 500 ? Math.round(14 * k) : 14;
    window.simState = { U: P.U, d: P.d * 100, q: P.q, x: P.x, h: P.h, kentta: P.field, E, Ex, Ey, Eud: P.U * 1000 / P.d,
      F, Fx, Fy, suunta: dir, nlines: 0, narrow: cw < 500, labels: null };
    labels = [];
    p.background(255);
    scene(P, m, Fx, Fy, F);
    window.simState.labels = labels;
  };

  const PX = (x) => CX + x * SC, PY = (y) => CY - y * SC;
  function head(x, y, ux, uy, s, col) {     // a filled arrowhead with its tip at (x, y) pointing along (ux, uy)
    p.noStroke(); p.fill(...col);
    p.triangle(x, y, x - ux * s - uy * s * 0.5, y - uy * s + ux * s * 0.5, x - ux * s + uy * s * 0.5, y - uy * s - ux * s * 0.5);
  }
  function scene(P, m, Fx, Fy, F) {
    const top = PY(P.d / 2), bot = PY(-P.d / 2), x0 = PX(-L / 2), x1 = PX(L / 2);
    // wires to the source terminals
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(CX, top - 10, CX, 40); p.line(CX, bot + 10, CX, 370);
    for (const y of [40, 370]) { p.fill(255); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(CX, y, 12 * sk); }
    lab('$+$', CX + 14 * sk, 40 + fs * 0.35, 'l');
    lab('$-$', CX + 14 * sk, 370 + fs * 0.35, 'l');
    lab(__('c_u', { u: tx(P.U, 1) }), 590, 34 + fs * 0.35, 'r');
    lab(__('c_d', { d: tx(P.d * 100, 1) }), 590, 34 + fs * 1.65, 'r');
    // the field, drawn under the plates
    const Eud = P.U * 1000 / P.d;
    if (P.field === 'viivat' && P.U > 0) {
      const count = Math.max(1, Math.round(Eud / 5000)), Ls = lines(m, P.d, count);
      window.simState.nlines = count;
      p.noFill(); p.stroke(...FIELD); p.strokeWeight(1.6 * sk);
      for (const pts of Ls) {
        p.beginShape(); for (const [x, y] of pts) p.vertex(PX(x), PY(y)); p.endShape();
        const i = Math.floor(pts.length / 2);
        if (pts.length > 3) {
          const [xa, ya] = pts[i - 1], [xb, yb] = pts[i + 1], dx = PX(xb) - PX(xa), dy = PY(yb) - PY(ya), l = Math.hypot(dx, dy) || 1;
          head(PX(pts[i][0]) + dx / l * 5 * sk, PY(pts[i][1]) + dy / l * 5 * sk, dx / l, dy / l, 9 * sk, FIELD);
          p.noFill(); p.stroke(...FIELD); p.strokeWeight(1.6 * sk);
        }
      }
    } else if (P.field === 'vektorit' && P.U > 0) {
      for (const [x, y, ex, ey] of vectors(m, P.d)) {
        const e = Math.hypot(ex, ey) * P.U * 1000, len = e / 150000 * 26 * sk;
        if (len < 2) { p.noStroke(); p.fill(...FIELD); p.circle(PX(x), PY(y), 3 * sk); continue; }
        const ux = ex / Math.hypot(ex, ey), uy = -ey / Math.hypot(ex, ey), xa = PX(x) - ux * len / 2, ya = PY(y) - uy * len / 2;
        p.stroke(...FIELD); p.strokeWeight(2 * sk); p.line(xa, ya, xa + ux * (len - 5 * sk), ya + uy * (len - 5 * sk));
        head(xa + ux * len, ya + uy * len, ux, uy, Math.min(8 * sk, len * 0.6), FIELD);
      }
    }
    // the plates: metal with their charge, the number of signs grows with U : d (the plates' surface charge)
    for (const [y, sign] of [[top - 10, 1], [bot, -1]]) {
      p.stroke(...EDGE); p.strokeWeight(1.5 * sk); p.fill(...METAL); p.rect(x0, y, x1 - x0, 10, 2);
      const nq = Math.min(30, Math.round(Eud / 5000));
      p.stroke(...INKC); p.strokeWeight(1.8);
      for (let i = 0; i < nq && P.U > 0; i++) {
        const xc = x0 + (i + 0.5) * (x1 - x0) / nq, yc = y + 5;
        p.line(xc - 3, yc, xc + 3, yc); if (sign > 0) p.line(xc, yc - 3, xc, yc + 3);
      }
    }
    // the ball on the force sensor and the force on it
    const bx = PX(P.x / 100), by = PY(P.h / 100 - P.d / 2), r = 9 * sk;
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    p.fill(...(P.q > 0 ? POSL : P.q < 0 ? NEGL : [255, 255, 255])); p.circle(bx, by, 2 * r);
    p.strokeWeight(2 * sk);
    if (P.q !== 0) { p.line(bx - r * 0.5, by, bx + r * 0.5, by); if (P.q > 0) p.line(bx, by - r * 0.5, bx, by + r * 0.5); }
    if (F > 0.5) {
      const len = Math.min(140, 0.3 * F), ux = Fx / F, uy = -Fy / F;
      const xa = bx + ux * r, ya = by + uy * r, xt = bx + ux * (r + len), yt = by + uy * (r + len);
      p.stroke(...FORCE); p.strokeWeight(3.5 * sk); p.line(xa, ya, xt - ux * 10 * sk, yt - uy * 10 * sk);
      head(xt, yt, ux, uy, 14 * sk, FORCE);
      const side = P.x <= 0 ? 1 : -1, xm = (xa + xt) / 2 + side * (12 * sk + 6), ym = (ya + yt) / 2;
      lab('$\\overline{F}$', xm, ym + fs * 0.35, side > 0 ? 'l' : 'r', FORCE);
    }
  }

  // every canvas text: its box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fs);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fs), 400 - 0.3 * fs);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * fs, x1: x0 + w, y1: y + 0.25 * fs });
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
