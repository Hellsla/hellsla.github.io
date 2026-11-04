// fy8-8 Atomiydin ja radioaktiivinen hajoaminen: the uranium-238 series on a nuclide chart (N across, Z up).
// The chain's nuclides and their decay modes are data (NNDC NuDat 3, the main branch of each step): 8 alpha and
// 6 beta-minus decays lead from U-238 to the stable Pb-206. The slider picks the step k (0–14); "Hajoa" moves one step
// on and animates the emission (alpha: 2 p + 2 n leave; beta-minus: an electron and an antineutrino leave). The chart
// shows the path so far, arrows in the decay's colour, and the stable nuclides of the region as green cells. The
// state is evaluated at once from the slider; the animation only shows it, and the speed select changes its pace.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  // [Z, A, mode]: mode 1 alpha, 2 beta-minus, 0 stable (NNDC NuDat 3)
  const CHAIN = [[92, 238, 1], [90, 234, 2], [91, 234, 2], [92, 234, 1], [90, 230, 1], [88, 226, 1], [86, 222, 1], [84, 218, 1],
                 [82, 214, 2], [83, 214, 2], [84, 214, 1], [82, 210, 2], [83, 210, 2], [84, 210, 1], [82, 206, 0]];
  const SYM = { 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np' };
  const STABLE = [[81, 122], [82, 122], [81, 124], [82, 124], [82, 125], [82, 126], [83, 126]];   // Tl-203, Pb-204, Tl-205, Pb-206, Pb-207, Pb-208, Bi-209 as [Z, N]
  const ZMIN = 81, ZMAX = 93, NMIN = 122, NMAX = 147;
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], PAPERC = [246, 241, 230], PROT = [201, 42, 42],
        NEUT = [196, 204, 212], ALPHAC = [112, 72, 232], BETAC = [25, 113, 194], GOODC = [43, 138, 62], GOODL = [178, 242, 187],
        PATHC = [255, 192, 120], HEATC = [232, 89, 12];
  const WIDE = { H: 400, x0: 66, x1: 440, y0: 30, y1: 330, cx: 527, cy: 214, r: 3.9, symY: 104, nTickY: 352, every: 2 };
  const NARROW = { H: 980, x0: 100, x1: 570, y0: 56, y1: 446, cx: 300, cy: 760, r: 4.6, symY: 590, nTickY: 482, every: 2 };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let slK, selSpeed, btnGo, btnReset, lK, readout, anim = null;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnGo = p.createButton(__('hajoa')).parent(controls); btnGo.elt.addEventListener('click', go);
    const lk = p.createElement('label').parent(controls); lK = p.createSpan('').parent(lk); slK = p.createSlider(0, 14, 0, 1).parent(lk);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    btnReset = p.createButton(__('alkuun')).parent(controls); btnReset.elt.addEventListener('click', () => { slK.value(0); anim = null; });
    p.createP(__('selite')).parent('sim-root').class('note');
    for (const ev of ['input', 'change']) slK.elt.addEventListener(ev, () => { anim = null; });
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { k: { input: slK.elt, unit: '' } },
      reset: () => { slK.value(0); anim = null; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function go() {
    const k = Number(slK.value());
    if (k >= CHAIN.length - 1) return;
    slK.value(k + 1);
    anim = { from: k, t: 0 };
  }

  function state() {
    const k = Number(slK.value()), [Z, A, mode] = CHAIN[k];
    const prev = k > 0 ? CHAIN[k - 1] : null;
    return { k, Z, A, N: A - Z, mode, prevMode: prev ? prev[2] : -1, dZ: prev ? Z - prev[0] : 0, dA: prev ? A - prev[1] : 0 };
  }

  const nuc = (Z, A) => '{}^{' + A + '}_{' + Z + '}\\text{' + SYM[Z] + '}';
  const modeName = (m) => __(m === 1 ? 'alfa' : m === 2 ? 'beeta' : 'pysyva');

  p.draw = () => {
    const S = state();
    const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value());
    if (anim) { anim.t += dt / 1.6; if (anim.t >= 1) anim = null; }
    btnGo.elt.disabled = S.k >= CHAIN.length - 1;
    lK.html(__('vaihe', { k: String(S.k) }));
    let html = __('lukemat', { nuk: nuc(S.Z, S.A), nimi: __('el_' + SYM[S.Z]), A: S.A, Z: S.Z, N: S.N, tapa: modeName(S.mode) });
    if (S.k > 0) {
      const [pZ, pA, pm] = CHAIN[S.k - 1];
      html += '<br>' + __(pm === 1 ? 'yhtalo_alfa' : 'yhtalo_beeta', { emo: nuc(pZ, pA), tytar: nuc(S.Z, S.A) });
    }
    readout.html(html);
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, kk = Math.max(1, 600 / cw);
    sk = narrow ? kk : 1; fh = narrow ? Math.round(14 * kk) : 13; G = narrow ? NARROW : WIDE;
    window.simState = { k: S.k, Z: S.Z, N: S.N, A: S.A, mode: S.mode, prevMode: S.prevMode, dZ: S.dZ, dA: S.dA,
                        anim: anim ? anim.t : -1, labels: null };
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    chart(S); nucleusPanel(S);
    window.simState.labels = labels;
  };

  // --- the nuclide chart: N across, Z up; cells, the stable ones green, the path so far with arrows ---
  const cwid = () => (G.x1 - G.x0) / (NMAX - NMIN + 1), chgt = () => (G.y1 - G.y0) / (ZMAX - ZMIN + 1);
  const CX = (N) => G.x0 + (N - NMIN + 0.5) * cwid(), CY = (Z) => G.y1 - (Z - ZMIN + 0.5) * chgt();
  function chart(S) {
    const w = cwid(), h = chgt();
    p.noStroke(); p.fill(...PAPERC); p.rect(G.x0, G.y0, G.x1 - G.x0, G.y1 - G.y0);
    p.stroke(...GRID); p.strokeWeight(1 * sk);
    for (let N = NMIN; N <= NMAX + 1; N++) p.line(G.x0 + (N - NMIN) * w, G.y0, G.x0 + (N - NMIN) * w, G.y1);
    for (let Z = ZMIN; Z <= ZMAX + 1; Z++) p.line(G.x0, G.y1 - (Z - ZMIN) * h, G.x1, G.y1 - (Z - ZMIN) * h);
    for (const [Z, N] of STABLE) { p.fill(...GOODL); p.stroke(...GOODC); p.strokeWeight(1.5 * sk); p.rect(CX(N) - w / 2 + 1, CY(Z) - h / 2 + 1, w - 2, h - 2); }
    // visited cells
    const shownTo = anim ? anim.from : S.k;
    for (let i = 0; i <= shownTo; i++) {
      const [Z, A] = CHAIN[i], N = A - Z;
      p.fill(...(i === CHAIN.length - 1 ? GOODC : PATHC)); p.stroke(...INKC); p.strokeWeight(1.2 * sk);
      p.rect(CX(N) - w / 2 + 1.5 * sk, CY(Z) - h / 2 + 1.5 * sk, w - 3 * sk, h - 3 * sk, 2 * sk);
    }
    // arrows of the decays so far; the newest grows during the animation
    for (let i = 0; i < S.k; i++) {
      const [Z1, A1, m] = CHAIN[i], [Z2, A2] = CHAIN[i + 1];
      const u = anim && i === anim.from ? ease(anim.t) : (anim && i > anim.from ? 0 : 1);
      if (u <= 0) continue;
      arrow(CX(A1 - Z1), CY(Z1), CX(A2 - Z2), CY(Z2), m === 1 ? ALPHAC : BETAC, u);
    }
    // the current cell, outlined
    const [Zc, Ac] = CHAIN[anim ? anim.from : S.k];
    p.noFill(); p.stroke(...HEATC); p.strokeWeight(3 * sk); p.rect(CX(Ac - Zc) - w / 2 - 1, CY(Zc) - h / 2 - 1, w + 2, h + 2, 3 * sk);
    // axes: Z rows with element symbols on the left, N ticks below
    for (let Z = ZMIN; Z <= ZMAX; Z++) if (Z % G.every === 0) lab('$' + Z + '\\ \\text{' + SYM[Z] + '}$', G.x0 - 6 * sk, CY(Z) + 0.36 * fh, 'r', INKC);
    p.stroke(...INKC); p.strokeWeight(2 * sk);
    for (let N = 124; N <= 144; N += 4) { p.line(CX(N), G.y1, CX(N), G.y1 + 6 * sk); lab('$' + N + '$', CX(N), G.nTickY + 0.36 * fh, 'c', MUTEDC); }
    lab('$N$', G.x1 + 6 * sk, G.nTickY + 0.36 * fh, 'l', INKC);
    lab('$Z$', G.x0 - 6 * sk, G.y0 - 8 * sk, 'r', INKC);
  }

  // --- the nucleus: Z protons and N neutrons; during the animation the emitted particles fly out ---
  function nucleusPanel(S) {
    const from = anim ? CHAIN[anim.from] : null;
    const Z = from ? from[0] : S.Z, A = from ? from[1] : S.A;
    const showZ = anim && anim.t > 0.15 ? S.Z : Z, showA = anim && anim.t > 0.15 ? S.A : A;
    drawNucleus(G.cx, G.cy, showZ, showA - showZ, G.r * sk);
    lab('$' + nuc(S.Z, S.A) + '$', G.cx, G.symY, 'c', INKC, 1.6);
    if (anim && anim.t > 0.15) {
      const u = ease((anim.t - 0.15) / 0.85), R0 = 1.02 * G.r * sk * Math.sqrt(A) + 4 * sk, d = R0 + u * 90 * sk, a = -0.75;
      const x = G.cx + d * Math.cos(a), y = G.cy + d * Math.sin(a);
      if (from[2] === 1) {
        const s = G.r * sk * 1.25;
        [[-1, -1, PROT], [1, -1, NEUT], [-1, 1, NEUT], [1, 1, PROT]].forEach(([i, j, col]) => { p.fill(...col); p.stroke(...INKC); p.strokeWeight(1.2 * sk); p.circle(x + i * s, y + j * s, 2.4 * G.r * sk); });
      } else {
        p.fill(...BETAC); p.stroke(255); p.strokeWeight(2 * sk); p.circle(x, y, 10 * sk);
        const b = 0.6, xb = G.cx + d * Math.cos(b), yb = G.cy + d * Math.sin(b);
        p.fill(255); p.stroke(...MUTEDC); p.strokeWeight(1.8 * sk); p.circle(xb, yb, 8 * sk);
      }
    }
  }

  function drawNucleus(cx, cy, Z, N, r) {
    const A = Z + N, g = Math.PI * (3 - Math.sqrt(5));
    const kinds = []; for (let i = 0; i < A; i++) kinds.push(i);
    kinds.sort((a, b) => rnd(a) - rnd(b));
    const isP = new Array(A).fill(false); for (let i = 0; i < Z; i++) isP[kinds[i]] = true;
    p.stroke(...INKC); p.strokeWeight(0.9 * sk);
    for (let i = A - 1; i >= 0; i--) {
      const rr = 1.02 * r * Math.sqrt(i + 0.5);
      p.fill(...(isP[i] ? PROT : NEUT)); p.circle(cx + rr * Math.cos(i * g), cy + rr * Math.sin(i * g), 2 * r);
    }
  }
  const rnd = (k) => { const v = Math.sin(k * 12.9898 + 78.233) * 43758.5453; return v - Math.floor(v); };
  const ease = (t) => t * t * (3 - 2 * t);

  function arrow(x1, y1, x2, y2, col, u) {
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L, sh = 4 * sk;
    const xa = x1 + ux * sh, ya = y1 + uy * sh, xe = x1 + (x2 - x1) * u - ux * sh, ye = y1 + (y2 - y1) * u - uy * sh;
    const head = 7 * sk;
    p.stroke(...col); p.strokeWeight(2.5 * sk); p.line(xa, ya, xe - ux * head * 0.8, ye - uy * head * 0.8);
    p.noStroke(); p.fill(...col);
    p.triangle(xe, ye, xe - ux * head - uy * head * 0.55, ye - uy * head + ux * head * 0.55, xe - ux * head + uy * head * 0.55, ye - uy * head - ux * head * 0.55);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col, scale) {
    const size = fh * (scale || 1);
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * size), G.H - 0.3 * size);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
});
