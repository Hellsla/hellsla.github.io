// fy5-14 Äänen ominaisuudet: the Doppler effect from the geometry of wavefronts. A loudspeaker sends a tone of frequency
// f0; wavefront k leaves the source at the time t_k = k/f0 from the source's position x_s(t_k) and spreads at v = 340 m/s
// relative to the still air. Listener A is to the right of the source, listener B to the left. Case "lähde liikkuu":
// the source moves right at u (towards A, away from B); case "kuulijat liikkuvat": the source is at rest and both
// listeners move left at u (A towards the source, B away from it). The heard frequency is never computed from a Doppler
// formula: the sim solves, for two successive wavefronts, the time each reaches the listener x_o(t) = x_o0 + v_o t
// (A: x_o(t) − x_s(t_k) = v (t − t_k); B: x_s(t_k) − x_o(t) = v (t − t_k)) and takes one over the interval. The wavelength
// on each side is the spacing of successive fronts at one instant. The picture runs in slow motion (1/400 of real time
// at normaali); the frequencies do not depend on it. Below, a frequency line shows f_B, f0 and f_A. Every canvas text
// goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const V = 340, SC = 100, SLOW = 1 / 400;                           // sound speed (m/s), px per metre, slow motion
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], GRID = [227, 220, 203], RULEC = [201, 194, 178], VEL = [25, 113, 194],
        HEATC = [232, 89, 12], IRONC = [108, 117, 125], ALU = [196, 204, 212], EDGE = [138, 150, 163], SANDL = [241, 223, 181],
        SAND = [217, 178, 106], GRAINC = [169, 122, 53];
  // wide 600 x 400: picture above, frequency line below; narrow (sim-root < 500 px) 600 x 600 with larger labels
  const WIDE = { H: 400, picH: 262, yg: 226, rows: [30, 66, 100, 132], fy: [292, 318, 344], ay: 366, tky: 386, ax0: 80, ax1: 520, ticks: [0, 500, 1000, 1500] };
  const NARROW = { H: 600, picH: 410, yg: 360, rows: [46, 104, 160, 214], fy: [446, 490, 534], ay: 560, tky: 586, ax0: 104, ax1: 440, ticks: [0, 500, 1000] };
  const START = { lahde: { xs: 1.5, xA: 5.6, xB: 0.4 }, kuulija: { xs: 3.2, xA: 5.6, xB: 2.5 } };
  let G = WIDE, narrow = false, sk = 1, fh = 13, labels = [];
  let selMode, slF, slU, lF, lU, selSpeed, readout;
  let ts = 0, runKey = '';

  const params = () => ({ tila: selMode.value(), f0: Number(slF.value()), u: Number(slU.value()) });
  // the motion of the case: source x_s(t) = xs + vs t, listeners x(t) = x0 + vo t (metres, seconds)
  const motion = (P) => {
    const s = START[P.tila];
    return P.tila === 'lahde' ? { xs: s.xs, vs: P.u, xA: s.xA, xB: s.xB, vo: 0 } : { xs: s.xs, vs: 0, xA: s.xA, xB: s.xB, vo: -P.u };
  };
  // the time wavefront emitted at te reaches listener A (side +1, to the right) or B (side −1)
  const arrival = (M, te, side) => {
    const xe = M.xs + M.vs * te;
    return side > 0 ? (M.xA - xe + V * te) / (V - M.vo) : (xe - M.xB + V * te) / (V + M.vo);
  };
  // heard frequency: one over the interval between two successive arrivals; wavelength: spacing of fronts at one instant
  const heard = (M, f0, side) => 1 / (arrival(M, 1 / f0, side) - arrival(M, 0, side));
  const spacing = (M, f0, side) => {
    const t = 0.02, front = (te) => M.xs + M.vs * te + side * V * (t - te);
    return Math.abs(front(0) - front(1 / f0));
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l0 = p.createElement('label').parent(controls); p.createSpan(__('tilanne')).parent(l0); selMode = p.createSelect().parent(l0);
    selMode.option(__('lahde'), 'lahde'); selMode.option(__('kuulija'), 'kuulija'); selMode.selected('lahde');
    const l1 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l1); slF = p.createSlider(200, 800, 400, 10).parent(l1);
    const l2 = p.createElement('label').parent(controls); lU = p.createSpan('').parent(l2); slU = p.createSlider(0, 150, 0, 2).parent(l2);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { tila: { input: selMode.elt, unit: '' }, f0: { input: slF.elt, unit: 'Hz' }, u: { input: slU.elt, unit: 'm/s' } },
      reset: () => { selMode.selected('lahde'); slF.value(400); slU.value(0); ts = 0; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = params(), M = motion(P);
    const key = `${P.tila}|${P.f0}|${P.u}`;
    if (key !== runKey) { runKey = key; ts = 0; }
    ts += Math.min(p.deltaTime, 100) / 1000 * SLOW * Number(selSpeed.value());
    // start again before the source reaches A (lähde) or A reaches the source (kuulijat)
    const xsNow = M.xs + M.vs * ts, xANow = M.xA + M.vo * ts, xBNow = M.xB + M.vo * ts;
    if ((P.tila === 'lahde' && xsNow > 4.0) || (P.tila === 'kuulija' && xANow < 4.1)) ts = 0;
    const fA = heard(M, P.f0, 1), fB = heard(M, P.f0, -1), lamA = spacing(M, P.f0, 1), lamB = spacing(M, P.f0, -1);
    lF.html(__('taajuus', { f: String(P.f0) }));
    lU.html(P.tila === 'lahde' ? __('nopeus_s', { u: String(P.u) }) : __('nopeus_h', { u: String(P.u) }));
    readout.html(__('lukemat', { fA: tx(fA, 1), lA: tx(lamA, 3), fB: tx(fB, 1), lB: tx(lamB, 3) }));
    window.simState = { tila: P.tila, f0: P.f0, u: P.u, v: V, fA, fB, lamA, lamB, t: ts, labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    narrow = cw < 500;
    const k = Math.max(1, 600 / cw);
    sk = narrow ? k : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    G = narrow ? NARROW : WIDE;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    scene(P, M, fA, fB);
    p.stroke(220); p.strokeWeight(1); p.line(0, G.picH, 600, G.picH);
    freqLine(P.f0, fA, fB);
    window.simState.labels = labels;
  };

  const PX = (x) => x * SC;

  function scene(P, M, fA, fB) {
    const { yg, picH, rows } = G, ysp = yg - 40 * sk;
    grect(0, 0, 600, yg, [[246, 241, 230], [255, 255, 255]]);
    p.noStroke(); p.fill(...GRID); p.rect(0, yg, 600, picH - yg);
    p.stroke(...RULEC); p.strokeWeight(2); p.line(0, yg, 600, yg);
    // wavefronts: every front emitted within the last 800 px of travel, centred where the source was
    const c = p.drawingContext; c.save(); c.beginPath(); c.rect(0, 0, 600, picH); c.clip();
    const kMax = Math.floor(ts * P.f0), kMin = Math.ceil((ts - 8.5 / V) * P.f0);
    p.noFill();
    for (let kk = kMin; kk <= kMax; kk++) {
      const te = kk / P.f0, r = PX(V * (ts - te)), xe = PX(M.xs + M.vs * te);
      p.stroke(...MUTEDC, 200 * Math.max(0.15, 1 - r / 900)); p.strokeWeight(2 * sk);
      p.circle(xe, ysp, 2 * r);
    }
    c.restore();
    const xs = PX(M.xs + M.vs * ts), xA = PX(M.xA + M.vo * ts), xB = PX(M.xB + M.vo * ts);
    source(xs, ysp, P.tila === 'kuulija');
    listener(xA, ts, M, 1, P.tila === 'kuulija');
    listener(xB, ts, M, -1, P.tila === 'kuulija');
    // labels: values on the top row, the source's frequency, velocity arrows, names
    lab(__('lbl_fA', { f: tx(fA, 0) }), 596, rows[0], 'r');
    lab(__('lbl_fB', { f: tx(fB, 0) }), 4, rows[0], 'l');
    lab(__('lbl_f0', { f: String(P.f0) }), xs, rows[1], 'c');
    const len = 0.45 * P.u * sk;
    if (P.u > 0 && P.tila === 'lahde') {
      arrow(xs, rows[2] - 0.35 * fh, xs + len); lab('$\\overline{v}_\\text{s}$', xs + len + 6 * sk, rows[2], 'l', VEL);
    } else if (P.u > 0) {
      for (const x of [xA, xB]) { arrow(x, rows[2] - 0.35 * fh, x - len); lab('$\\overline{v}_\\text{h}$', x - len - 6 * sk, rows[2], 'r', VEL); }
    }
    lab(__('lbl_A'), xA, rows[3], 'c');
    lab(__('lbl_B'), xB, rows[3], 'c');
  }

  function source(x, ysp, still) {   // a loudspeaker on a wheeled cart
    const { yg } = G, s = sk;
    p.stroke(...INKC); p.strokeWeight(2 * s); p.fill(...IRONC); p.rect(x - 22 * s, yg - 28 * s, 44 * s, 18 * s, 3 * s);
    p.fill(...ALU); p.circle(x - 13 * s, yg - 7 * s, 13 * s); p.circle(x + 13 * s, yg - 7 * s, 13 * s);
    p.fill(...INKC); p.noStroke(); p.rect(x - 9 * s, ysp - 10 * s, 10 * s, 20 * s, 2);
    p.fill(...EDGE); p.stroke(...INKC); p.strokeWeight(2 * s);
    p.quad(x + 1 * s, ysp - 10 * s, x + 13 * s, ysp - 20 * s, x + 13 * s, ysp + 20 * s, x + 1 * s, ysp + 10 * s);
    p.stroke(...INKC); p.strokeWeight(2.5 * s); p.line(x - 4 * s, ysp + 10 * s, x - 4 * s, yg - 28 * s);
    if (still) { p.noStroke(); p.fill(...SAND); p.rect(x - 26 * s, yg - 3 * s, 52 * s, 5 * s, 2); }
  }

  function listener(x, t, M, side, onCart) {   // a person; the ear ring glows when a wavefront arrives
    const { yg } = G, s = sk;
    const foot = onCart ? yg - 16 * s : yg;
    if (onCart) {
      p.stroke(...INKC); p.strokeWeight(2 * s); p.fill(...SAND); p.rect(x - 20 * s, yg - 16 * s, 40 * s, 9 * s, 2);
      p.fill(...ALU); p.circle(x - 11 * s, yg - 5 * s, 10 * s); p.circle(x + 11 * s, yg - 5 * s, 10 * s);
    }
    p.stroke(...INKC); p.strokeWeight(3 * s);
    p.line(x, foot - 22 * s, x - 7 * s, foot); p.line(x, foot - 22 * s, x + 7 * s, foot);
    p.fill(...IRONC); p.strokeWeight(2 * s); p.rect(x - 8 * s, foot - 46 * s, 16 * s, 26 * s, 5 * s);
    p.fill(...SANDL); p.circle(x, foot - 55 * s, 16 * s);
    // the most recent arrival: te of the last front that has reached the listener
    const f0 = Number(slF.value());
    let te = side > 0 ? ((V - M.vo) * t - (M.xA - M.xs)) / (V - M.vs) : ((V + M.vo) * t - (M.xs - M.xB)) / (V + M.vs);
    te = Math.floor(te * f0) / f0;
    const age = (t - arrival(M, te, side)) / SLOW;                        // seconds of display time since it arrived
    const glow = Math.max(0, 1 - age / 0.35);
    const ex = x - side * 7 * s, ey = foot - 55 * s;
    p.noFill(); p.stroke(...HEATC, 60 + 195 * glow); p.strokeWeight((1.5 + 2.5 * glow) * s); p.circle(ex, ey, (8 + 10 * glow) * s);
    p.noStroke(); p.fill(...GRAINC); p.circle(ex, ey, 4 * s);
  }

  function arrow(x0, y, x1) {
    const d = Math.sign(x1 - x0), h = 10 * sk;
    if (Math.abs(x1 - x0) < h + 2) return;
    p.stroke(...VEL); p.strokeWeight(3 * sk); p.line(x0, y, x1 - d * h, y);
    p.noStroke(); p.fill(...VEL); p.triangle(x1, y, x1 - d * h, y - 0.5 * h, x1 - d * h, y + 0.5 * h);
  }

  // the frequency line: f_A, f_0 and f_B as points on one axis
  function freqLine(f0, fA, fB) {
    const { ax0, ax1, ay, tky, fy } = G, X = (f) => ax0 + Math.min(f, 1500) / 1500 * (ax1 - ax0);
    p.stroke(...GRID); p.strokeWeight(1.5);
    for (let f = 250; f <= 1500; f += 250) p.line(X(f), ay, X(f), fy[0] - 12 * sk);
    p.stroke(...MUTEDC); p.strokeWeight(1.5 * sk); p.drawingContext.setLineDash([5 * sk, 5 * sk]);
    p.line(X(f0), fy[0] - 12 * sk, X(f0), ay); p.drawingContext.setLineDash([]);
    p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(ax0, ay, ax1 + 16 * sk, ay);
    p.noStroke(); p.fill(...INKC); p.triangle(ax1 + 28 * sk, ay, ax1 + 14 * sk, ay - 6 * sk, ax1 + 14 * sk, ay + 6 * sk);
    for (const f of G.ticks) {
      p.stroke(...INKC); p.strokeWeight(2 * sk); p.line(X(f), ay, X(f), ay + 6 * sk);
      lab('$' + f + '$', X(f), tky, 'c');
    }
    lab('$f\\,(\\text{Hz})$', 596, tky, 'r');
    const pts = [[__('lbl_rowA'), fA, fy[0], HEATC], [__('lbl_row0'), f0, fy[1], INKC], [__('lbl_rowB'), fB, fy[2], HEATC]];
    for (const [name, f, y, col] of pts) {
      p.stroke(...RULEC); p.strokeWeight(1.2 * sk); p.line(ax0, y, ax1, y);
      p.fill(...col); p.stroke(255); p.strokeWeight(2 * sk); p.circle(X(f), y, 13 * sk);
      lab(name, 10, y + 0.36 * fh, 'l');
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(fh);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * fh), G.H - 0.3 * fh);
    p.noStroke(); p.fill(250, 247, 240, 235); p.rect(x0 - 3, y - 0.85 * fh, w + 6, 1.2 * fh, 3);   // paper backing: arcs never cross a label
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
