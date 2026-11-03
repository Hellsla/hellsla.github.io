// fy6-6 Sähköteho ja vastuksen lämpeneminen: an ideal source U (no internal resistance) feeds two resistors R1 and R2,
// in series or in parallel, ideal wires. Series: I = U / (R1 + R2), U1 = R1 I, U2 = R2 I; parallel: U1 = U2 = U,
// I1 = U / R1, I2 = U / R2, I = I1 + I2. Each resistor's power P = U_k I_k (= R I^2 = U^2 / R) and the source's P = U I.
// Each resistor is a heating coil in its own beaker of 0,10 kg water (c = 4190 J/(kg K)) starting at 20,0 C; heat
// losses are neglected, so while the clock runs T_k rises by P_k dt / (c m). The run stops at 80 C. The speed select
// changes only the pace (simulated seconds per real second); every value is per simulated time.
// Wires are drawn with violet conventional-current arrowheads (#7048e8), the coils glow with their power, an orange
// bar under each beaker is its power to scale (0-72 W), the thermometers and the water's tint show the temperature.
// Every canvas text goes through lab(), which pushes its box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], CURC = [112, 72, 232], GLASSC = [238, 245, 249],
        WATERL = [169, 209, 240], HOTC = [201, 42, 42], HOTL = [242, 166, 156], HEATL = [255, 192, 120], HEATC = [232, 89, 12],
        ALU = [196, 204, 212], METAL = [138, 150, 163], RULEL = [227, 220, 203], RULEC = [201, 194, 178];
  const C_W = 4190, M_W = 0.10, T0 = 20, TMAX = 80, PMAX = 72;
  const WIDE = { H: 400, S: 60, B: [270, 450], MX: 360, RX: 585, bw: 64, bar: 80 },
        NARROW = { H: 660, S: 40, B: [170, 450], MX: 310, RX: 585, bw: 62, bar: 125 };
  let G = WIDE, fh = 13, sk = 1, narrow = false, labels = [];
  let slU, slR1, slR2, selK, selV, btn, lU, lR1, lR2, readout;
  let t = 0, T1 = T0, T2 = T0, running = false;

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', toggle);
    const b2 = p.createButton(__('nollaa')).parent(controls);
    b2.elt.addEventListener('click', clear);
    const mk = (min, max, v, st) => { const l = p.createElement('label').parent(controls); const s = p.createSpan('').parent(l); return [s, p.createSlider(min, max, v, st).parent(l)]; };
    [lU, slU] = mk(1, 12, 12, 0.5);
    [lR1, slR1] = mk(2, 20, 4, 1);
    [lR2, slR2] = mk(2, 20, 8, 1);
    const l4 = p.createElement('label').parent(controls); p.createSpan(__('kytkenta')).parent(l4); selK = p.createSelect().parent(l4);
    selK.option(__('sarja'), 'sarja'); selK.option(__('rinnan'), 'rinnan'); selK.selected('sarja');
    const l5 = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(l5); selV = p.createSelect().parent(l5);
    selV.option(__('hidas'), '5'); selV.option(__('normaali'), '15'); selV.option(__('nopea'), '60'); selV.selected('15');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { U: { input: slU.elt, unit: 'V' }, R1: { input: slR1.elt, unit: 'Ω' }, R2: { input: slR2.elt, unit: 'Ω' },
                kytkenta: { input: selK.elt, unit: '' } },
      reset: () => { slU.value(12); slR1.value(4); slR2.value(8); selK.selected('sarja'); clear(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  function toggle() {
    if (!running && Math.max(T1, T2) >= TMAX - 1e-9) clear();
    running = !running; btn.html(running ? __('pysayta') : __('kaynnista'));
  }
  function clear() { running = false; t = 0; T1 = T0; T2 = T0; if (btn) btn.html(__('kaynnista')); }

  function solve() {
    const U = Number(slU.value()), R1 = Number(slR1.value()), R2 = Number(slR2.value()), k = selK.value();
    let I, I1, I2, U1, U2;
    if (k === 'sarja') { I = U / (R1 + R2); I1 = I; I2 = I; U1 = R1 * I; U2 = R2 * I; }
    else { I1 = U / R1; I2 = U / R2; I = I1 + I2; U1 = U; U2 = U; }
    return { U, R1, R2, k, Rkok: U / I, I, I1, I2, U1, U2, P1: U1 * I1, P2: U2 * I2, P: U * I };
  }

  p.draw = () => {
    const S = solve();
    if (running) {
      const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selV.value());      // simulated seconds this frame
      let d1 = S.P1 * dt / (C_W * M_W), d2 = S.P2 * dt / (C_W * M_W), f = 1;
      const need = Math.max((T1 + d1 - TMAX) / (d1 || 1), (T2 + d2 - TMAX) / (d2 || 1));
      if (need > 0) { f = Math.max(0, 1 - need); running = false; btn.html(__('kaynnista')); }   // stop exactly at 80 C
      T1 += d1 * f; T2 += d2 * f; t += dt * f;
    }
    lU.html(__('jannite', { U: tx(S.U, 1) }));
    lR1.html(__('vastus', { n: '1', R: String(S.R1) }));
    lR2.html(__('vastus', { n: '2', R: String(S.R2) }));
    readout.html(__('lukemat', { I: tx(S.I, 2), I1: tx(S.I1, 2), I2: tx(S.I2, 2), U1: tx(S.U1, 2), U2: tx(S.U2, 2),
                                 P1: tx(S.P1, 2), P2: tx(S.P2, 2), P: tx(S.P, 2), t: tx(t, 0), T1: tx(T1, 1), T2: tx(T2, 1),
                               }));
    window.simState = { U: S.U, R1: S.R1, R2: S.R2, kytkenta: S.k, Rkok: S.Rkok, I: S.I, I1: S.I1, I2: S.I2, U1: S.U1, U2: S.U2,
                        P1: S.P1, P2: S.P2, P: S.P, Psum: S.P1 + S.P2, t, T1, T2, dT1: T1 - T0, dT2: T2 - T0, running,
                        speed: Number(selV.value()), labels: null };
    const cw = (p.canvas && p.canvas.parentElement && p.canvas.parentElement.clientWidth) || document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500; const k = Math.min(2.4, Math.max(1, 600 / cw));
    sk = narrow ? k : 1; fh = narrow ? Math.round(14 * k) : 13; G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.H, [[246, 241, 230], [255, 255, 255]]);
    scene(S);
    window.simState.labels = labels;
  };

  // --- layout: rows from the top, the beakers take the height that is left ----------------------------------------
  function layout() {
    const L = {};
    L.yTop = fh + 6;
    L.yW1 = L.yTop + 0.5 * fh + 22 * sk;          // the + wire
    L.yW2 = L.yW1 + 18 * sk;                       // the wire between the inner terminals
    L.yTerm = L.yW2 + 18 * sk;                     // binding posts
    L.bTop = L.yTerm + 16 * sk;
    const below = (bH) => {                         // rows under the beakers
      const bBot = L.bTop + bH, yR = bBot + 0.9 * fh + 10, yP = yR + 1.35 * fh, yBar = yP + 0.45 * fh + 8, barH = 10 * sk;
      const yT = yBar + barH + 0.9 * fh + 8;
      return { bBot, yR, yP, yBar, barH, yT, yBot: yT + 0.5 * fh + 16 * sk };
    };
    const bH = Math.max(140, Math.min(260, G.H - 24 - below(0).yBot));
    Object.assign(L, below(bH));
    L.water = L.bTop + 24;
    L.mid = (L.yW1 + L.yBot) / 2;
    return L;
  }

  function scene(S) {
    const L = layout(), [B1, B2] = G.B, w = G.bw, a1 = B1 - 36, b1 = B1 + 36, b2 = B2 - 36, a2 = B2 + 36, Sx = G.S;
    const plusY = L.mid - 8 * sk, minusY = L.mid + 8 * sk;
    // wires (behind the beakers' rims)
    if (S.k === 'sarja') {
      wire([[Sx, plusY], [Sx, L.yW1], [a1, L.yW1], [a1, L.yTerm]]);
      wire([[b1, L.yTerm], [b1, L.yW2], [b2, L.yW2], [b2, L.yTerm]]);
      wire([[a2, L.yTerm], [a2, L.yW1], [G.RX, L.yW1], [G.RX, L.yBot], [Sx, L.yBot], [Sx, minusY]]);
      head(Sx, (L.yW1 + plusY) / 2, 'u'); head((Sx + a1) / 2, L.yW1, 'r'); head(G.MX, L.yW2, 'r');
      head(G.RX, L.mid, 'd'); head((Sx + G.RX) / 2, L.yBot, 'l');
    } else {
      wire([[Sx, plusY], [Sx, L.yW1], [a2, L.yW1], [a2, L.yTerm]]);
      wire([[a1, L.yW1], [a1, L.yTerm]]);
      wire([[b1, L.yTerm], [b1, L.yW2], [b2, L.yW2], [b2, L.yTerm]]);
      wire([[G.MX, L.yW2], [G.MX, L.yBot], [Sx, L.yBot], [Sx, minusY]]);
      dot(a1, L.yW1); dot(G.MX, L.yW2);
      head(Sx, (L.yW1 + plusY) / 2, 'u'); head((Sx + a1) / 2, L.yW1, 'r'); head(G.MX, L.yW1, 'r');
      head((b1 + G.MX) / 2, L.yW2, 'r'); head((G.MX + b2) / 2, L.yW2, 'l');
      head(G.MX, (L.yW2 + L.yBot) / 2, 'd'); head((Sx + G.MX) / 2, L.yBot, 'l');
    }
    // source: long thin plate +, short thick plate -
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.line(Sx - 20, plusY, Sx + 20, plusY);
    p.strokeWeight(7 * sk); p.line(Sx - 10, minusY, Sx + 10, minusY);
    lab('$+$', Sx + 22 + 0.3 * fh, plusY - 0.25 * fh, 'c'); lab('$-$', Sx + 22 + 0.3 * fh, minusY + 0.95 * fh, 'c');
    lab('$U = ' + tx(S.U, 1) + '\\,\\text{V}$', 12, L.yTop, 'l');
    lab('$t = ' + tx(t, 0) + '\\,\\text{s}$', 588, L.yTop, 'r');
    // beakers
    beaker(1, B1, a1, b1, S.P1, T1, S.R1, L, w);
    beaker(2, B2, b2, a2, S.P2, T2, S.R2, L, w);
  }

  function beaker(n, B, xl, xr, P, T, R, L, w) {
    const x0 = B - w, x1 = B + w, glowT = Math.min(1, P / 36);
    // water, tinted warmer with the temperature
    const ht = Math.max(0, Math.min(1, (T - T0) / (TMAX - T0)));
    p.noStroke(); p.fill(...mix(WATERL, HOTL, ht), 230);
    p.rect(x0 + 2, L.water, 2 * w - 4, L.bBot - L.water - 2, 0, 0, 12, 12);
    p.stroke(255, 255, 255, 160); p.strokeWeight(2 * sk); p.line(x0 + 8, L.water + 1, x1 - 8, L.water + 1);
    // the coil's leads from the posts down into the water, the coil at the bottom glowing with its power
    const yc = L.bBot - 30;
    p.noFill(); p.stroke(...METAL); p.strokeWeight(3 * sk);
    p.line(xl, L.yTerm, xl, yc); p.line(xr, L.yTerm, xr, yc);
    if (glowT > 0.02) { p.noStroke(); p.fill(...HEATL, 140 * glowT); p.ellipse(B, yc, (xr - xl) + 40, 50); }
    p.stroke(...mix(ALU, HEATC, glowT)); p.strokeWeight(3.5 * sk);
    const loops = 6, lw = (xr - xl) / loops;
    for (let i = 0; i < loops; i++) p.ellipse(xl + (i + 0.5) * lw, yc, lw + 4, 24);
    // thermometer dipped in the middle, its red column on a 0-100 C scale
    const tt = L.bTop - 10, tb = L.water + (yc - L.water) * 0.55, tw = 6 * sk;
    p.fill(255); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(B - tw, tt, 2 * tw, tb - tt, tw);
    p.fill(...HOTC); p.circle(B, tb, 4.2 * tw);
    const top = tb - (tb - tt - tw) * T / 100;
    p.noStroke(); p.rect(B - tw / 2, top, tw, tb - top);
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk);
    for (let c = 20; c <= 80; c += 20) { const y = tb - (tb - tt - tw) * c / 100; p.line(B + tw, y, B + tw + 5 * sk, y); }
    // glass
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3 * sk);
    p.beginShape(); p.vertex(x0 - 6, L.bTop); p.vertex(x0, L.bTop + 6); p.vertex(x0, L.bBot - 12);
    p.quadraticVertex(x0, L.bBot, x0 + 12, L.bBot); p.vertex(x1 - 12, L.bBot); p.quadraticVertex(x1, L.bBot, x1, L.bBot - 12);
    p.vertex(x1, L.bTop + 6); p.vertex(x1 + 6, L.bTop); p.endShape();
    p.noStroke(); p.fill(...GLASSC, 90); p.rect(x0 + 4, L.bTop + 8, 8, L.bBot - L.bTop - 20, 4);
    dot(xl, L.yTerm); dot(xr, L.yTerm);
    // labels: resistance, power and its bar to scale, temperature
    lab('$R_' + n + ' = ' + String(R) + '\\,\\Omega$', B, L.yR, 'c');
    lab('$P_' + n + ' = ' + tx(P, 1) + '\\,\\text{W}$', B, L.yP, 'c', HEATC);
    const bx = B - G.bar, bwid = 2 * G.bar;
    p.fill(255); p.stroke(...RULEC); p.strokeWeight(1.5); p.rect(bx, L.yBar, bwid, L.barH, 3);
    p.noStroke(); p.fill(...HEATC); p.rect(bx, L.yBar, bwid * Math.min(1, P / PMAX), L.barH, 3);
    lab('$T_' + n + ' = ' + tx(T, 1) + '\\,{}^\\circ\\text{C}$', B, L.yT, 'c', HOTC);
  }

  function wire(pts) {
    p.noFill(); p.stroke(...INKC); p.strokeWeight(3 * sk); p.strokeJoin(p.ROUND);
    p.beginShape(); for (const [x, y] of pts) p.vertex(x, y); p.endShape();
  }
  function dot(x, y) { p.noStroke(); p.fill(...INKC); p.circle(x, y, 9 * sk); }
  function head(x, y, d) {
    const s = 7 * sk; p.noStroke(); p.fill(...CURC);
    if (d === 'r') p.triangle(x + s, y, x - s, y - 0.8 * s, x - s, y + 0.8 * s);
    else if (d === 'l') p.triangle(x - s, y, x + s, y - 0.8 * s, x + s, y + 0.8 * s);
    else if (d === 'u') p.triangle(x, y - s, x - 0.8 * s, y + s, x + 0.8 * s, y + s);
    else p.triangle(x, y + s, x - 0.8 * s, y - s, x + 0.8 * s, y - s);
  }
  const mix = (a, b, t) => a.map((c, i) => c + (b[i] - c) * t);

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
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
});
