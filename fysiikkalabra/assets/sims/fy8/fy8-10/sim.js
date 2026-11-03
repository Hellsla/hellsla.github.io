// fy8-10 Massavaje ja ytimen sidosenergia: a balance and the binding-energy-per-nucleon graph.
// The student picks a nuclide. On the balance, the left pan holds its Z hydrogen atoms and N neutrons apart, the right
// pan the atom itself; the beam tips towards the heavier, separate nucleons (the tilt is exaggerated: it grows with
// Δm / (Z m_H + N m_n), at most about 8°). The mass defect Δm = Z m_H + N m_n − m_atom, E_B = Δm c² with
// 1 u = 931,5 MeV/c² and E_B / A are computed from the atomic masses of AME2020 (rounded to six decimals in u, the same
// table as lessons/FY8/fy8-10/lesson-answers.py). Each nuclide visited adds its point to the graph; one button shows
// every point of the table, another clears the graph. Nothing is animated, so there is no speed control.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const M_H = 1.007825, M_N = 1.008665, U_MEV = 931.5;
  // [key, symbol, Z, A, atomic mass in u] (AME2020, six decimals)
  const NUC = [['H2', 'H', 1, 2, 2.014102], ['H3', 'H', 1, 3, 3.016049], ['He3', 'He', 2, 3, 3.016029], ['He4', 'He', 2, 4, 4.002603],
    ['Li6', 'Li', 3, 6, 6.015123], ['Li7', 'Li', 3, 7, 7.016003], ['Be9', 'Be', 4, 9, 9.012183], ['B11', 'B', 5, 11, 11.009305],
    ['C12', 'C', 6, 12, 12.000000], ['N14', 'N', 7, 14, 14.003074], ['O16', 'O', 8, 16, 15.994915], ['Ne20', 'Ne', 10, 20, 19.992440],
    ['Mg24', 'Mg', 12, 24, 23.985042], ['Si28', 'Si', 14, 28, 27.976927], ['S32', 'S', 16, 32, 31.972071], ['Ca40', 'Ca', 20, 40, 39.962591],
    ['Fe56', 'Fe', 26, 56, 55.934936], ['Ni62', 'Ni', 28, 62, 61.928345], ['Cu63', 'Cu', 29, 63, 62.929598], ['Zn64', 'Zn', 30, 64, 63.929142],
    ['Kr84', 'Kr', 36, 84, 83.911498], ['Zr90', 'Zr', 40, 90, 89.904698], ['Ag107', 'Ag', 47, 107, 106.905092], ['Sn120', 'Sn', 50, 120, 119.902202],
    ['Ba138', 'Ba', 56, 138, 137.905247], ['W184', 'W', 74, 184, 183.950933], ['Au197', 'Au', 79, 197, 196.966570], ['Pb208', 'Pb', 82, 208, 207.976652],
    ['Bi209', 'Bi', 83, 209, 208.980399], ['Th232', 'Th', 90, 232, 232.038056], ['U235', 'U', 92, 235, 235.043928], ['U238', 'U', 92, 238, 238.050787]];
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], RULEC = [201, 194, 178], PROT = [201, 42, 42],
        NEUT = [196, 204, 212], METAL = [138, 150, 163], IRONC = [108, 117, 125], ALU = [196, 204, 212], HEATC = [232, 89, 12],
        HEATL = [255, 192, 120], GOODL = [178, 242, 187];
  const WIDE = { H: 400, cx: 150, cy: 122, half: 105, drop: 112, panW: 44, base: 345, s: 1, gx0: 350, gy0: 330, gx1: 552, gy1: 78, dmY: 30 };
  const NARROW = { H: 840, cx: 300, cy: 150, half: 190, drop: 160, panW: 82, base: 470, s: 1.8, gx0: 112, gy0: 770, gx1: 520, gy1: 530, dmY: 40 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let sel, btnAll, btnClear, readout, showAll = false;
  const visited = new Set();

  const calc = (i) => {
    const [key, sym, Z, A, m] = NUC[i], N = A - Z, msum = Z * M_H + N * M_N;
    const dm = Math.round((msum - m) * 1e6) / 1e6, EB = dm * U_MEV;
    return { i, key, sym, Z, N, A, m, msum, dm, EB, EBA: EB / A };
  };
  const fmt = (v, d) => v.toFixed(d).replace('.', '{,}');
  const nuc = (S) => '{}^{' + S.A + '}_{' + S.Z + '}\\text{' + S.sym + '}';

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnAll = p.createButton(__('nayta_kaikki')).parent(controls);
    btnAll.elt.addEventListener('click', () => { showAll = !showAll; btnAll.html(__(showAll ? 'piilota_muut' : 'nayta_kaikki')); p.redraw(); });
    const ls = p.createElement('label').parent(controls); p.createSpan(__('ydin')).parent(ls); sel = p.createSelect().parent(ls);
    NUC.forEach(([key, sym, Z, A]) => sel.option(__('el_' + sym) + '-' + A, key));
    sel.selected('He4');
    btnClear = p.createButton(__('tyhjenna')).parent(controls);
    btnClear.elt.addEventListener('click', () => { visited.clear(); p.redraw(); });
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { ydin: { input: sel.elt, unit: '' } },
      reset: () => { sel.selected('He4'); showAll = false; btnAll.html(__('nayta_kaikki')); visited.clear(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const idx = Math.max(0, NUC.findIndex((r) => r[0] === sel.value()));
    const S = calc(idx);
    visited.add(idx);
    const tilt = Math.min(0.15, 14 * S.dm / S.msum);
    readout.html(__('lukemat', { nuk: nuc(S), nimi: __('el_' + S.sym), A: S.A, Z: S.Z, N: S.N, m: fmt(S.m, 6), msum: fmt(S.msum, 6),
      dm: fmt(S.dm, 6), EB: fmt(S.EB, S.EB >= 100 ? 1 : S.EB >= 10 ? 2 : 3), EBA: fmt(S.EBA, 3) }));
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 13; G = narrow ? NARROW : WIDE;
    window.simState = { ydin: S.key, Z: S.Z, N: S.N, A: S.A, m: S.m, msum: Math.round(S.msum * 1e6) / 1e6, dm: S.dm,
      EB: Math.round(S.EB * 100) / 100, EBA: Math.round(S.EBA * 1000) / 1000, tilt, visited: visited.size, all: showAll ? 1 : 0, labels: null };
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    balance(S, tilt); graph(S);
    window.simState.labels = labels;
  };

  // --- the balance: separate nucleons on the left pan, the atom's nucleus on the right ---
  function balance(S, tilt) {
    const s = G.s, c = Math.cos(tilt), sn = Math.sin(tilt);
    const L = { x: G.cx - G.half * c, y: G.cy + G.half * sn }, R = { x: G.cx + G.half * c, y: G.cy - G.half * sn };
    // foot and post
    p.stroke(...INKC); p.strokeWeight(2 * s); p.fill(...METAL);
    p.quad(G.cx - 46 * s, G.base, G.cx + 46 * s, G.base, G.cx + 30 * s, G.base - 18 * s, G.cx - 30 * s, G.base - 18 * s);
    p.fill(...ALU); p.rect(G.cx - 7 * s, G.cy, 14 * s, G.base - 18 * s - G.cy, 3 * s);
    // beam and pivot
    p.stroke(...INKC); p.strokeWeight(2 * s); p.fill(...IRONC);
    const dx = 5 * s * sn, dy = 5 * s * c;
    p.quad(L.x - dx, L.y - dy, R.x - dx, R.y - dy, R.x + dx, R.y + dy, L.x + dx, L.y + dy);
    p.fill(...METAL); p.circle(G.cx, G.cy, 16 * s);
    // the pointer swings with the beam
    p.stroke(...PROT); p.strokeWeight(3 * s); p.line(G.cx, G.cy + 8 * s, G.cx - 70 * s * Math.sin(tilt), G.cy + 70 * s * Math.cos(tilt));
    for (const E of [L, R]) {
      const py = E.y + G.drop;
      p.stroke(...INKC); p.strokeWeight(1.5 * s);
      p.line(E.x, E.y + 4 * s, E.x - G.panW, py); p.line(E.x, E.y + 4 * s, E.x + G.panW, py);
      p.fill(...ALU); p.strokeWeight(2 * s); p.arc(E.x, py, 2 * G.panW + 10 * s, 26 * s, 0, Math.PI, p.CHORD);
      p.fill(...INKC); p.noStroke(); p.circle(E.x, E.y + 4 * s, 6 * s);
    }
    pile(S, L.x, L.y + G.drop - 1 * s);
    nucleus(S, R.x, R.y + G.drop - 1 * s);
    lab('$\\Delta m = ' + fmt(S.dm, 6) + '\\,\\text{u}$', G.cx, G.dmY, 'c', PROT);
    const yL = L.y + G.drop + 13 * s + 1.1 * fh, yR = R.y + G.drop + 13 * s + 1.1 * fh;
    lab('$' + fmt(S.msum, 6) + '\\,\\text{u}$', L.x, yL, 'c', INKC);
    lab(__('lab_osat'), L.x, yL + 1.35 * fh, 'c', MUTEDC);
    lab('$' + fmt(S.m, 6) + '\\,\\text{u}$', R.x, yR, 'c', INKC);
    lab(__('lab_atomi'), R.x, yR + 1.35 * fh, 'c', MUTEDC);
  }

  // Z red and N grey balls apart, in rows from the pan upwards
  function pile(S, x, ybot) {
    const A = S.A, cols = Math.max(2, Math.ceil(Math.sqrt(1.6 * A))), gap = A <= 4 ? 1.7 : 1.25;
    const r = Math.min(8 * G.s, (1.7 * G.panW) / (cols * 2 * gap));
    const rows = Math.ceil(A / cols);
    let k = 0, pr = 0;
    p.stroke(...INKC); p.strokeWeight(Math.max(0.6, 0.12 * r));
    for (let row = 0; row < rows; row++) {
      const n = Math.min(cols, A - row * cols), w = (n - 1) * 2 * r * gap;
      for (let j = 0; j < n; j++, k++) {
        const isP = Math.floor((k + 1) * S.Z / A) > pr; if (isP) pr++;
        p.fill(...(isP ? PROT : NEUT));
        p.circle(x - w / 2 + j * 2 * r * gap, ybot - r - row * 2 * r * gap, 2 * r);
      }
    }
  }

  // the nucleus: A balls packed tightly (sunflower), Z of them red
  function nucleus(S, x, ybot) {
    const A = S.A, gold = Math.PI * (3 - Math.sqrt(5));
    const r = Math.min(8 * G.s, (0.9 * G.panW) / (1.05 * Math.sqrt(A) + 0.6));
    const R = 1.05 * r * Math.sqrt(A) + r, cy = ybot - R;
    const isP = new Array(A).fill(false); let pr = 0;
    for (let k = 0; k < A; k++) { if (Math.floor((k + 1) * S.Z / A) > pr) { isP[k] = true; pr++; } }
    p.noStroke(); p.fill(...HEATL); p.circle(x, cy, 2 * R + 10 * G.s);
    p.fill(255); p.circle(x, cy, 2 * R + 2 * G.s);
    p.stroke(...INKC); p.strokeWeight(Math.max(0.6, 0.12 * r));
    for (let i = A - 1; i >= 0; i--) {
      const rr = 1.05 * r * Math.sqrt(i + 0.5);
      p.fill(...(isP[i] ? PROT : NEUT)); p.circle(x + rr * Math.cos(i * gold), cy + rr * Math.sin(i * gold), 2 * r);
    }
  }

  // --- the graph: E_B / A against A, the visited nuclides, the current one ringed ---
  const GX = (A) => G.gx0 + A / 250 * (G.gx1 - G.gx0), GY = (v) => G.gy0 - v / 10 * (G.gy0 - G.gy1);
  function graph(S) {
    p.stroke(...GRID); p.strokeWeight(1 * sk);
    for (let A = 50; A <= 250; A += 50) p.line(GX(A), G.gy0, GX(A), G.gy1);
    for (let v = 2; v <= 10; v += 2) p.line(G.gx0, GY(v), G.gx1, GY(v));
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    p.line(G.gx0, G.gy0, G.gx1 + 14 * sk, G.gy0); p.line(G.gx0, G.gy0, G.gx0, G.gy1 - 14 * sk);
    p.noStroke(); p.fill(...INKC);
    p.triangle(G.gx1 + 22 * sk, G.gy0, G.gx1 + 12 * sk, G.gy0 - 5 * sk, G.gx1 + 12 * sk, G.gy0 + 5 * sk);
    p.triangle(G.gx0, G.gy1 - 22 * sk, G.gx0 - 5 * sk, G.gy1 - 12 * sk, G.gx0 + 5 * sk, G.gy1 - 12 * sk);
    p.stroke(...INKC); p.strokeWeight(1.5 * sk);
    for (let A = 50; A <= 250; A += 50) { p.line(GX(A), G.gy0, GX(A), G.gy0 + 5 * sk); lab('$' + A + '$', GX(A), G.gy0 + 6 * sk + fh, 'c', MUTEDC); }
    for (let v = 2; v <= 10; v += 2) { p.stroke(...INKC); p.line(G.gx0 - 5 * sk, GY(v), G.gx0, GY(v)); lab('$' + v + '$', G.gx0 - 8 * sk, GY(v) + 0.36 * fh, 'r', MUTEDC); }
    lab('$0$', G.gx0 - 8 * sk, G.gy0 + 6 * sk + fh, 'r', MUTEDC);
    lab('$A$', G.gx1 + 26 * sk, G.gy0 + 0.36 * fh, 'l', INKC);
    lab(__('lab_akseli'), G.gx0 + 12 * sk, G.gy1 - 12 * sk, 'l', INKC);
    for (let i = 0; i < NUC.length; i++) {
      const T = calc(i), x = GX(T.A), y = GY(T.EBA);
      if (visited.has(i)) { p.fill(...HEATC); p.stroke(255); p.strokeWeight(1.5 * sk); p.circle(x, y, 9 * sk); }
      else if (showAll) { p.noFill(); p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.circle(x, y, 8 * sk); }
    }
    const x = GX(S.A), y = GY(S.EBA);
    p.noFill(); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(x, y, 18 * sk);
    const right = S.A < 200;
    lab('$' + nuc(S) + '$', right ? x + 12 * sk : x - 12 * sk, y + (S.EBA < 4 ? -14 * sk : 1.25 * fh + 8 * sk), right ? 'l' : 'r', INKC);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    const size = fh;
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * size), G.H - 0.3 * size);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
});
