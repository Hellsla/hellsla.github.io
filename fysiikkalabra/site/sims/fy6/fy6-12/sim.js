// fy6-12 Potentiaalienergia ja potentiaali sähkökentässä: a charged particle (proton q = +e, electron q = -e or alpha
// particle q = +2e) is released at rest at its plate in the homogeneous field between two parallel plates, the upper
// plate positive at potential U, the lower one negative at 0 V (the zero point). E = U / d, F = q E, a = F / m; the
// motion is integrated step by step with the constant acceleration (exact for a constant force) until the particle
// reaches the other plate. Readings: E, F, t, v, E_k = m v^2 / 2 and E_p = q V with V = E x (x from the negative plate);
// E_k + E_p stays constant, and at the far plate E_k = |q| U whatever the gap d. Gravity is left out.
// Animation: simulated time advances dt · speed · scale; the electron is shown 40 times more slowed down than the
// proton and the alpha particle, so each crossing takes a few seconds on screen (the readout gives the real t).
// Colours: field lines and E green, equipotential lines dashed grey, force red, velocity blue (FY4), potentials and E_p ink, E_k orange. Every canvas text
// goes through lab(), which pushes its box to simState.labels. Phone: the energy bars stack under the plates.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], FORCEC = [201, 42, 42], VELC = [25, 113, 194],
        FIELDC = [43, 138, 62], EQC = [134, 142, 150], KINC = [232, 89, 12], ALU = [196, 204, 212], POSL = [242, 166, 156], NEGL = [208, 230, 251];
  const E0 = 1.602e-19;
  const PART = { p: { q: 1, m: 1.673e-27, scale: 1e-7 }, e: { q: -1, m: 9.109e-31, scale: 2.5e-9 }, a: { q: 2, m: 6.645e-27, scale: 1e-7 } };
  const WIDE = { H: 400, px0: 92, px1: 330, pxc: 212, cy: 200, cmpx: 30, arrows: [122, 160, 266, 302], sep: 396,
                 bars: [455, 545], bw: 64, zero: 232, bs: 150, names: 40, lblx: 84 };
  const NARROW = { H: 970, px0: 150, px1: 470, pxc: 310, cy: 290, cmpx: 46, arrows: [168, 448], sep: 0, sepy: 570,
                   bars: [195, 405], bw: 130, zero: 830, bs: 150, names: 600, lblx: 140 };
  let G = WIDE, sk = 1, fh = 13, narrow = false, labels = [];
  let slU, slD, selP, selS, lU, lD, btn, readout;
  let st = null;                       // the run: t (s), y (m travelled), v (m/s), running, arrived, trail

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('paasta')).parent(controls);
    btn.elt.addEventListener('click', () => { if (!st.running) { if (st.arrived) restart(); st.running = true; } });
    p.createButton(__('alkuun')).parent(controls).elt.addEventListener('click', () => restart());
    const mk = (min, max, v, step) => { const l = p.createElement('label').parent(controls); const s = p.createSpan('').parent(l); return [s, p.createSlider(min, max, v, step).parent(l)]; };
    [lU, slU] = mk(100, 1000, 500, 50);
    [lD, slD] = mk(2, 10, 5, 0.5);
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('hiukkanen')).parent(l3); selP = p.createSelect().parent(l3);
    selP.option(__('protoni'), 'p'); selP.option(__('elektroni'), 'e'); selP.option(__('alfa'), 'a'); selP.selected('p');
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l4); selS = p.createSelect().parent(l4);
    selS.option(__('hidas'), '0.25'); selS.option(__('normaali'), '1'); selS.option(__('nopea'), '4'); selS.selected('1');
    for (const el of [slU, slD, selP]) for (const ev of ['input', 'change']) el.elt.addEventListener(ev, restart);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { U: { input: slU.elt, unit: 'V' }, d: { input: slD.elt, unit: 'cm' }, hiukkanen: { input: selP.elt, unit: '' } },
      reset: () => { slU.value(500); slD.value(5); selP.selected('p'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function restart() { st = { t: 0, y: 0, v: 0, running: false, arrived: false, trail: [], next: 1 }; }

  function model() {
    const U = Number(slU.value()), dcm = Number(slD.value()), d = dcm / 100, key = selP.value(), P = PART[key];
    const q = P.q * E0, E = U / d, F = Math.abs(q) * E, a = F / P.m, tc = Math.sqrt(2 * d / a);
    return { U, dcm, d, key, P, q, E, F, a, tc };
  }

  function advance(M) {
    if (!st.running || st.arrived) return;
    let dt = Math.min(p.deltaTime, 100) / 1000 * Number(selS.value()) * M.P.scale;   // simulated seconds this frame
    while (dt > 0 && !st.arrived) {
      const tk = st.next * M.tc / 10;                       // the next strobe time: ten equal steps of the crossing time
      const h = Math.min(dt, Math.max(tk - st.t, 0));
      const yNew = st.y + st.v * h + 0.5 * M.a * h * h;
      if (yNew >= M.d) {                                   // arrival inside this step: the exact time to the plate
        const s = M.d - st.y, tau = (-st.v + Math.sqrt(st.v * st.v + 2 * M.a * s)) / M.a;
        st.t += tau; st.v += M.a * tau; st.y = M.d; st.arrived = true; st.running = false; break;
      }
      st.y = yNew; st.v += M.a * h; st.t += h; dt -= h;
      if (st.t >= tk - 1e-18) { st.trail.push(st.y); st.next += 1; }
    }
  }

  p.draw = () => {
    const M = model();
    advance(M);
    const xneg = M.q > 0 ? M.d - st.y : st.y;              // distance from the negative plate (positive particles start at +)
    const V = M.E * xneg, Ep = M.q * V, Ek = 0.5 * M.P.m * st.v * st.v;
    const EpeV = Ep / E0, EkeV = Ek / E0;
    lU.html(__('jannite', { U: String(M.U) }));
    lD.html(__('vali', { d: tx(M.dcm, 1) }));
    btn.elt.disabled = st.running;
    readout.html(__('lukemat', { E: grp(M.E), F: sci(M.F, 3), t: tx(st.t * 1e9, st.t * 1e9 < 10 ? 2 : 1), v: grp4(st.v / 1000),
                                 Ek: tx(EkeV, 0), EkJ: sci(Ek, 3), Ep: tx(EpeV, 0), sum: tx(EkeV + EpeV, 0) }));
    window.simState = { U: M.U, dcm: M.dcm, d: M.dcm, dm: M.d, particle: M.key, hiukkanen: M.key, q: M.q, m: M.P.m, E: M.E, F: M.F, a: M.a, tc: M.tc,
                        t: st.t, tns: st.t * 1e9, y: st.y, x: xneg, V, v: st.v, vkms: st.v / 1000, Ek, EkeV, Ep, EpeV,
                        sumeV: EkeV + EpeV, running: st.running, arrived: st.arrived, labels: null };
    const cw = (p.canvas && p.canvas.parentElement && p.canvas.parentElement.clientWidth) || document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500; const k = Math.min(2.4, Math.max(1, 600 / cw));
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); return; }
    labels = [];
    p.background(255);
    const picH = narrow ? G.sepy : G.H;
    grect(0, 0, narrow ? 600 : G.sep, picH, [[246, 241, 230], [255, 255, 255]]);
    plates(M, xneg);
    if (narrow) { p.stroke(...RULEC); p.strokeWeight(1.5); p.line(0, G.sepy, 600, G.sepy); }
    else { p.stroke(...RULEC); p.strokeWeight(1.5); p.line(G.sep, 12, G.sep, G.H - 12); }
    bars(M, EpeV, EkeV);
    window.simState.labels = labels;
  };

  // --- the plates, the field, the particle ------------------------------------------------------------------------
  function plates(M, xneg) {
    const gap = M.dcm * G.cmpx, top = G.cy - gap / 2, bot = G.cy + gap / 2, { px0, px1, pxc } = G;
    // equipotential lines: as many inner lines as the labels have room for (4, 1 or none)
    const n = [4, 1, 0].find((c) => gap / (c + 1) >= 1.7 * fh);
    for (let i = 1; i <= n; i++) {
      const y = bot - i * gap / (n + 1), v = M.U * i / (n + 1);
      p.stroke(...EQC); p.strokeWeight(2 * sk); p.drawingContext.setLineDash([8 * sk, 6 * sk]);
      p.line(px0, y, px1, y); p.drawingContext.setLineDash([]);
      lab('$' + tx(v, 0) + '\\,\\text{V}$', G.lblx, y + 0.36 * fh, 'r', INKC);
    }
    lab('$' + String(M.U) + '\\,\\text{V}$', G.lblx, top + 0.36 * fh, 'r', INKC);
    lab('$0\\,\\text{V}$', G.lblx, bot + 0.36 * fh, 'r', INKC);
    // field lines: green arrows from the + plate to the - plate
    for (const x of G.arrows) arrow(x, top + 9 * sk, x, bot - 9 * sk, FIELDC, 2.5 * sk, 12 * sk);
    lab('$\\overline{E}$', G.arrows[0] + 8 * sk, top + gap * 0.5 / (n + 1) + 0.36 * fh, 'l', FIELDC, true);
    // the plates
    for (const [y, plus] of [[top, true], [bot, false]]) {
      p.fill(...ALU); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.rect(px0, y - 6 * sk, px1 - px0, 12 * sk, 2);
      p.strokeWeight(2 * sk);
      for (let x = px0 + 20 * sk; x < px1 - 10 * sk; x += 40 * sk) { p.line(x - 4 * sk, y, x + 4 * sk, y); if (plus) p.line(x, y - 4 * sk, x, y + 4 * sk); }
    }
    // the gap
    const bx = px1 + 22 * sk;
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(bx, top, bx, bot); p.line(bx - 6 * sk, top, bx + 6 * sk, top); p.line(bx - 6 * sk, bot, bx + 6 * sk, bot);
    lab('$d$', bx + 10 * sk, G.cy + 0.36 * fh, 'l');
    // the particle: its strobe trail, then itself
    const r = (M.key === 'a' ? 12 : M.key === 'p' ? 10 : 7) * sk, ypx = (xn) => bot - 6 * sk - r - xn / M.d * (gap - 12 * sk - 2 * r);   // the particle's surface touches the plates
    p.noStroke(); p.fill(...MUTEDC, 110);
    for (const y of st.trail) p.circle(pxc, ypx(M.q > 0 ? M.d - y : y), 6 * sk);
    const py = ypx(xneg);
    p.fill(...(M.q > 0 ? POSL : VELC)); p.stroke(...INKC); p.strokeWeight(2 * sk); p.circle(pxc, py, 2 * r);
    p.stroke(...(M.q > 0 ? INKC : [255, 255, 255])); p.strokeWeight(2 * sk); p.line(pxc - r * 0.5, py, pxc + r * 0.5, py); if (M.q > 0) p.line(pxc, py - r * 0.5, pxc, py + r * 0.5);
    const dir = M.q > 0 ? 1 : -1;                            // down for a positive particle, up for the electron
    const picH = narrow ? G.sepy : G.H, clampY = (y) => Math.min(Math.max(y, 10), picH - 10);
    const fe = clampY(py + dir * Math.min(44 * sk, gap * 0.42));
    arrow(pxc - 15 * sk, py, pxc - 15 * sk, fe, FORCEC, 3 * sk, 11 * sk);
    lab('$\\overline{F}$', pxc - 22 * sk, (py + fe) / 2 + 0.36 * fh, 'r', FORCEC, true);
    const vEnd = Math.sqrt(2 * M.a * M.d);
    if (st.v > 0) {
      const vl = Math.max(st.v / vEnd * 70 * sk, 12 * sk), ye = clampY(py + dir * vl);
      arrow(pxc + 15 * sk, py, pxc + 15 * sk, ye, VELC, 3 * sk, 11 * sk);
      lab('$\\overline{v}$', pxc + 22 * sk, (py + ye) / 2 + 0.36 * fh, 'l', VELC, true);
    }
  }

  // --- energy bars in eV: E_p green, E_k orange; full scale 2|q|U/e of an alpha particle -------------------------
  function bars(M, EpeV, EkeV) {
    const full = 2 * M.U, { zero, bs, bw } = G, s = bs / full;
    const x0 = narrow ? 60 : G.sep + 14, x1 = narrow ? 540 : 590;
    p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(x0, zero, x1, zero);
    for (const [cx, val, col, name] of [[G.bars[0], EpeV, INKC, '$E_\\text{p}$'], [G.bars[1], EkeV, KINC, '$E_\\text{k}$']]) {
      lab(name, cx, G.names + 0.36 * fh, 'c', INKC);
      const h = val * s;
      p.fill(...col); p.stroke(...INKC); p.strokeWeight(2 * sk);
      if (Math.abs(h) >= 1) p.rect(cx - bw / 2, Math.min(zero, zero - h), bw, Math.abs(h));
      const yl = h >= 0 ? zero - h - 0.55 * fh : zero - h + 1.15 * fh;
      lab('$' + tx(val, 0) + '\\,\\text{eV}$', cx, yl, 'c', INKC);
    }
  }

  function arrow(x1, y1, x2, y2, col, w, head) {
    const L = Math.hypot(x2 - x1, y2 - y1); if (L < 1) return;
    const ux = (x2 - x1) / L, uy = (y2 - y1) / L, hh = Math.min(head, L * 0.6), bx = x2 - ux * hh, by = y2 - uy * hh, hw = hh * 0.5;
    p.stroke(...col); p.strokeWeight(w); p.line(x1, y1, bx, by);
    p.noStroke(); p.fill(...col); p.triangle(x2, y2, bx - uy * hw, by + ux * hw, bx + uy * hw, by - ux * hw);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col, bg) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    if (bg) { p.noStroke(); p.fill(255, 255, 255, 225); p.rect(x0 - 3, y - 0.85 * fh, w + 6, 1.15 * fh, 3); }
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
  const grp = (x) => { const s = String(Math.round(x)); return s.length > 4 ? s.replace(/\B(?=(\d{3})+(?!\d))/g, '\\,') : s; };
  const grp4 = (x) => (x >= 1000 ? grp(Number(x.toPrecision(4))) : tx(x, x >= 100 ? 1 : x >= 10 ? 2 : 3));
  const sci = (x, sig) => {
    if (x === 0) return '0';
    const ex = Math.floor(Math.log10(Math.abs(x))), m = x / Math.pow(10, ex);
    return tx(m, sig - 1) + ' \\cdot 10^{' + ex + '}';
  };
});
