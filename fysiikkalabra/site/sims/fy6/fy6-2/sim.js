// fy6-2 Mittaukset virtapiirissä: a series circuit of a battery (1–3 cells of 1,5 V, ideal), a lamp (constant 15 Ω) and
// a resistor (30 Ω), and a digital multimeter whose probes the student puts into the circuit. The meter is either in
// series (in one of two gaps of the top wire) or across the lamp, the resistor or the battery; its selector sets the
// function and range: voltage 2 V / 20 V (internal resistance 10 MΩ) or current 200 mA (1,0 Ω) / 10 A (0,010 Ω).
// The circuit is solved with these resistances, so a voltmeter in series makes the current practically zero (the
// lamp goes out, the meter shows about the battery voltage) and an ammeter across a component short-circuits it;
// a current above the range blows the meter's fuse (the meter then leaves the circuit and reads 0). The 3½-digit
// display shows the reading rounded to the range's resolution, or OL above the range. Conventional current arrows in
// their own colour. Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9.
new p5((p) => {
  const INKC = [31, 41, 51], MUTEDC = [107, 116, 128], RULEC = [201, 194, 178], LCDC = [227, 220, 203], BODY = [196, 204, 212], HILITE = [255, 192, 120],
        FACE = [108, 117, 125], EDGE = [138, 150, 163], LEADR = [201, 42, 42], CURR = [112, 72, 232], GLOW = [255, 192, 120],
        GLOWD = [232, 89, 12], WHITE = [255, 255, 255], RESC = [241, 223, 181];
  const RL = 15, RR = 30, RV = 10e6, CELL = 1.5;
  const RANGE = {      // function, the meter's own resistance (Ω), the largest value the display shows, resolution, unit
    V2: { mode: 'V', R: RV, max: 1.999, res: 0.001, unit: 'V', dec: 3, name: '2\\,\\text{V}' },
    V20: { mode: 'V', R: RV, max: 19.99, res: 0.01, unit: 'V', dec: 2, name: '20\\,\\text{V}' },
    mA200: { mode: 'A', R: 1.0, max: 0.1999, res: 0.0001, unit: 'mA', dec: 1, k: 1000, name: '200\\,\\text{mA}' },
    A10: { mode: 'A', R: 0.01, max: 9.99, res: 0.01, unit: 'A', dec: 2, k: 1, name: '10\\,\\text{A}' },
  };
  const DIAL = ['V2', 'V20', 'mA200', 'A10'];
  // circuit geometry in circuit units (wide layout = canvas pixels); nodes where the probes can touch
  const TOP = 96, BOT = 300, LEFT = 48, RIGHT = 340, LAMPX = 176, LAMPR = 20, RES = [148, 248], BATX = 194;
  const GAP1 = [84, 124], GAP2 = [236, 276];
  const PTS = { sarja1: [[GAP1[0], TOP], [GAP1[1], TOP]], sarja2: [[GAP2[0], TOP], [GAP2[1], TOP]],
                lamppu: [[144, TOP], [208, TOP]], vastus: [[RIGHT, RES[0] - 16], [RIGHT, RES[1] + 16]], paristo: [[150, BOT], [238, BOT]] };
  // the leads run in lanes round the circuit: right of it (circuit x), above it (circuit y) and between the circuit and
  // the jacks (canvas y); index 0 is the black lead's lane, 1 the red one's
  const LANE_R = [368, 384], LANE_T = [56, 36];
  const WIDE = { H: 400, s: 1, ox: 0, oy: 0, body: [404, 20, 176, 360], lcd: [418, 36, 148, 84], dial: [492, 222, 34, 58],
                 ang: [-70, -25, 25, 70], jacks: [[436, 330], [492, 330], [548, 330]], jackLab: 358, laneB: [380, 392] };
  const NARROW = { H: 800, s: 1.5, ox: 6, oy: -40, body: [20, 528, 560, 262], lcd: [40, 606, 270, 128], dial: [450, 690, 46, 84],
                   ang: [-75, -30, 30, 75], jacks: [[90, 556], [190, 556], [290, 556]], jackLab: 586, laneB: [517, 505] };
  let G = WIDE, sk = 1, fh = 13, labels = [];
  let selN, selPos, selRange, readout;

  const X = (x) => G.ox + G.s * x, Y = (y) => G.oy + G.s * y, S = (d) => G.s * d;

  // the circuit with the meter of resistance Rm at pos (null: no meter); returns lamp, resistor and meter values
  function solve(U0, pos, Rm) {
    const par = (a, b) => a * b / (a + b);
    if (Rm === null) {
      const series = pos === 'sarja1' || pos === 'sarja2';
      const I = series ? 0 : U0 / (RL + RR);                       // a meter that left a gap open breaks the loop
      return { IL: I, IR: I, Im: 0, Um: series ? U0 : 0 };
    }
    if (pos === 'sarja1' || pos === 'sarja2') { const I = U0 / (RL + RR + Rm); return { IL: I, IR: I, Im: I, Um: I * Rm }; }
    if (pos === 'paristo') { const I = U0 / (RL + RR); return { IL: I, IR: I, Im: U0 / Rm, Um: U0 }; }
    if (pos === 'lamppu') { const Rp = par(RL, Rm), I = U0 / (Rp + RR), Up = I * Rp; return { IL: Up / RL, IR: I, Im: Up / Rm, Um: Up }; }
    const Rp = par(RR, Rm), I = U0 / (Rp + RL), Up = I * Rp;           // across the resistor
    return { IL: I, IR: Up / RR, Im: Up / Rm, Um: Up };
  }

  function state() {
    const N = Number(selN.value()), pos = selPos.value(), key = selRange.value(), R = RANGE[key], U0 = N * CELL;
    let c = solve(U0, pos, R.R), fuse = false;
    if (R.mode === 'A' && c.Im > R.max) { fuse = true; c = solve(U0, pos, null); }   // the fuse blows: the meter is open
    const raw = R.mode === 'V' ? c.Um : c.Im;
    const ol = !fuse && raw > R.max + R.res / 2;
    const shown = fuse ? 0 : Math.round(raw / R.res) * R.res;           // the display's last digit
    const PL = c.IL * c.IL * RL, Pnom = Math.pow(3 * CELL / (RL + RR), 2) * RL;
    const reading = fuse ? 'sulake' : ol ? 'OL' : Number((R.mode === 'A' ? shown * R.k : shown).toFixed(R.dec));
    return { N, U0, pos, key, R, ...c, fuse, ol, raw, reading, PL, bright: Math.min(1, Math.sqrt(PL / Pnom)), on: PL >= 0.004 };
  }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); p.createSpan(__('kytkenta')).parent(l1); selPos = p.createSelect().parent(l1);
    for (const k of ['sarja1', 'sarja2', 'lamppu', 'vastus', 'paristo']) selPos.option(__('pos_' + k), k);
    selPos.selected('sarja1');
    const l2 = p.createElement('label').parent(controls); p.createSpan(__('valitsin')).parent(l2); selRange = p.createSelect().parent(l2);
    for (const k of DIAL) selRange.option(__('alue_' + k), k);
    selRange.selected('mA200');
    const l3 = p.createElement('label').parent(controls); p.createSpan(__('paristoja')).parent(l3); selN = p.createSelect().parent(l3);
    for (const k of ['1', '2', '3']) selN.option(__('n' + k), k);
    selN.selected('3');
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { kytkenta: { input: selPos.elt, unit: '' }, alue: { input: selRange.elt, unit: '' }, N: { input: selN.elt, unit: '' } },
      reset: () => { selPos.selected('sarja1'); selRange.selected('mA200'); selN.selected('3'); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const st = state(), R = st.R;
    const unitTex = '\\,\\text{' + R.unit + '}', q = R.mode === 'V' ? 'U' : 'I';
    const val = st.fuse ? __('lukema_sulake') : st.ol ? __('lukema_ol')
      : __('lukema', { q: q, v: tx(typeof st.reading === 'number' ? st.reading : 0, R.dec) + unitTex });
    readout.html(__('lukemat', { alue: R.name, lukema: val, lamppu: st.on ? __('palaa') : __('ei_pala') }));
    window.simState = { N: st.N, U0: st.U0, kytkenta: st.pos, alue: st.key, mode: R.mode, IL: st.IL, IR: st.IR, Im: st.Im, Um: st.Um,
      UL: st.IL * RL, UR: st.IR * RR, fuse: st.fuse, ol: st.ol, reading: st.reading, PL: st.PL, lamppu: st.on ? 'palaa' : 'ei',
      ImA: R.mode === 'A' ? (typeof st.reading === 'number' ? Number((st.reading * (R.unit === 'A' ? 1000 : 1)).toFixed(1)) : st.reading) : '–', UV: R.mode === 'V' ? st.reading : '–', labels: null };
    const cw = document.getElementById('sim-root').clientWidth || 600;
    const narrow = cw < 500, k = Math.max(1, 600 / cw);
    G = narrow ? NARROW : WIDE;
    sk = narrow ? Math.min(k, 1.5) : 1;
    fh = narrow ? Math.round(14 * k) : 13;
    if (p.__H !== G.H) { p.__H = G.H; p.resizeCanvas(600, G.H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(255);
    grect(0, 0, 600, G.H, [[246, 241, 230], [255, 255, 255]]);
    circuit(st);
    meter(st);
    leads(st);
    window.simState.labels = labels;
  };

  // --- the circuit: battery on the bottom wire, lamp on the top wire, resistor on the right side ---
  function circuit(st) {
    const series = st.pos === 'sarja1' || st.pos === 'sarja2', gap = series ? (st.pos === 'sarja1' ? GAP1 : GAP2) : null;
    p.stroke(...INKC); p.strokeWeight(3 * sk); p.noFill();
    const bw = 18 * st.N, bx0 = BATX - bw / 2, bx1 = BATX + bw / 2;
    // wires: the loop, broken at the gap the meter is in and at the components
    const seg = (x1, y1, x2, y2) => p.line(X(x1), Y(y1), X(x2), Y(y2));
    seg(LEFT, BOT, bx0, BOT); seg(bx1, BOT, RIGHT, BOT); seg(LEFT, TOP, LEFT, BOT); seg(RIGHT, TOP, RIGHT, RES[0]); seg(RIGHT, RES[1], RIGHT, BOT);
    const topCuts = [[LAMPX - LAMPR, LAMPX + LAMPR]].concat(gap ? [gap] : []).sort((a, b) => a[0] - b[0]);
    let x = LEFT;
    for (const [a, b] of topCuts) { seg(x, TOP, a, TOP); x = b; }
    seg(x, TOP, RIGHT, TOP);
    if (gap) for (const gx of gap) { p.fill(...WHITE); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(X(gx), Y(TOP), S(9)); }
    // battery: N cells, long thin plate +, short thick plate −; the + side on the left
    for (let i = 0; i < st.N; i++) {
      const cx = bx0 + 18 * i;
      p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.line(X(cx + 4), Y(BOT - 22), X(cx + 4), Y(BOT + 22));
      p.strokeWeight(6 * sk); p.line(X(cx + 13), Y(BOT - 11), X(cx + 13), Y(BOT + 11));
      if (i < st.N - 1) { p.strokeWeight(3 * sk); p.line(X(cx + 13), Y(BOT), X(cx + 22), Y(BOT)); }
    }
    lab('$+$', X(bx0 - 6), Y(BOT - 30), 'r', INKC);
    lab('$-$', X(bx1 + 6), Y(BOT - 30), 'l', INKC);
    lab('$' + tx(st.U0, 1) + '\\,\\text{V}$', X(BATX), Y(BOT + 50), 'c', INKC);
    // lamp: a circle with a cross, its glow follows its power
    if (st.bright > 0.02) {
      const c = p.drawingContext, gr = c.createRadialGradient(X(LAMPX), Y(TOP), 0, X(LAMPX), Y(TOP), S(20 + 34 * st.bright));
      gr.addColorStop(0, `rgba(${GLOW.join(',')},${0.95 * st.bright})`); gr.addColorStop(1, `rgba(${GLOW.join(',')},0)`);
      c.save(); c.fillStyle = gr; c.beginPath(); c.arc(X(LAMPX), Y(TOP), S(20 + 34 * st.bright), 0, 2 * Math.PI); c.fill(); c.restore();
    }
    p.fill(st.on ? [255, 236, 200] : WHITE); p.stroke(...INKC); p.strokeWeight(3 * sk); p.circle(X(LAMPX), Y(TOP), S(2 * LAMPR));
    const d = LAMPR * 0.7;
    p.stroke(...(st.on ? GLOWD : INKC)); p.strokeWeight(2.5 * sk);
    p.line(X(LAMPX - d), Y(TOP - d), X(LAMPX + d), Y(TOP + d)); p.line(X(LAMPX - d), Y(TOP + d), X(LAMPX + d), Y(TOP - d));
    lab(__('lamppu'), X(LAMPX), Y(TOP + 46), 'c', INKC);
    // resistor: a rectangle
    p.fill(...RESC); p.stroke(...INKC); p.strokeWeight(3 * sk); p.rect(X(RIGHT - 12), Y(RES[0]), S(24), S(RES[1] - RES[0]));
    lab(__('vastus'), X(RIGHT - 24), Y((RES[0] + RES[1]) / 2 + 5), 'r', INKC);
    // conventional current arrows from + to −, in their own colour, where a current flows
    const arrowUp = (ax, ay, dx, dy) => {
      const L = 16, w = 7;
      p.noStroke(); p.fill(...CURR);
      p.triangle(X(ax + dx * L), Y(ay + dy * L), X(ax - dy * w), Y(ay + dx * w), X(ax + dy * w), Y(ay - dx * w));
      p.stroke(...CURR); p.strokeWeight(3 * sk); p.line(X(ax - dx * 14), Y(ay - dy * 14), X(ax), Y(ay));
    };
    if (st.IR > 1e-3) {
      arrowUp(LEFT, 210, 0, -1);
      arrowUp(292, BOT, -1, 0);
      lab('$I$', X(LEFT + 14), Y(212), 'l', CURR);
    }
  }

  // --- the multimeter: display, selector dial, jacks ---
  function meter(st) {
    const [bx, by, bw, bh] = G.body, [lx, ly, lw, lh] = G.lcd, [dx, dy, dr, drl] = G.dial, R = st.R;
    p.fill(...BODY); p.stroke(...INKC); p.strokeWeight(3 * sk); p.rect(bx, by, bw, bh, 18 * sk);
    p.fill(...FACE); p.noStroke(); p.rect(bx + 8 * sk, by + 8 * sk, bw - 16 * sk, bh - 16 * sk, 12 * sk);
    p.fill(...LCDC); p.stroke(...INKC); p.strokeWeight(2 * sk); p.rect(lx, ly, lw, lh, 6 * sk);
    const big = Math.round(fh * 2.1), digits = st.fuse ? tx(0, R.dec) : st.ol ? '' : tx(st.reading, R.dec);
    if (st.ol) lab(__('ol'), lx + lw * 0.5, ly + lh * 0.52, 'c', INKC, big);
    else {
      lab('$' + digits + '$', lx + lw - fh * 3.2, ly + lh * 0.52, 'r', INKC, big);
      lab('$\\text{' + R.unit + '}$', lx + lw - fh * 2.8, ly + lh * 0.52, 'l', INKC);
    }
    if (st.fuse) lab(__('sulake'), lx + lw / 2, ly + lh - 0.5 * fh, 'c', LEADR);
    // the selector: a knob whose pointer shows the chosen range, the ranges round its top
    p.fill(...EDGE); p.stroke(...INKC); p.strokeWeight(2.5 * sk); p.circle(dx, dy, 2 * dr);
    p.fill(...INKC); p.noStroke(); p.circle(dx, dy, dr * 0.9);
    DIAL.forEach((key, i) => {
      const a = G.ang[i] * Math.PI / 180, on = key === st.key;
      p.stroke(...WHITE); p.strokeWeight(2 * sk);
      p.line(dx + (dr + 3 * sk) * Math.sin(a), dy - (dr + 3 * sk) * Math.cos(a), dx + (dr + 10 * sk) * Math.sin(a), dy - (dr + 10 * sk) * Math.cos(a));
      const rl = Math.abs(G.ang[i]) > 50 ? drl * 1.08 : drl;
      lab('$' + RANGE[key].name + '$', dx + rl * Math.sin(a), dy - rl * Math.cos(a) + 0.35 * fh, 'c', on ? HILITE : WHITE);
      if (on) { p.stroke(...WHITE); p.strokeWeight(5 * sk); p.line(dx, dy, dx + (dr - 4 * sk) * Math.sin(a), dy - (dr - 4 * sk) * Math.cos(a)); }
    });
    // jacks: COM (black lead), V mA and 10 A (red lead)
    const names = [__('com'), __('vma'), __('a10')];
    G.jacks.forEach(([jx, jy], i) => {
      p.fill(...INKC); p.stroke(i === 0 ? WHITE : LEADR); p.strokeWeight(3 * sk); p.circle(jx, jy, 18 * sk);
      lab(names[i], jx, G.jackLab + 0.35 * fh, 'c', WHITE);
    });
  }

  // --- the leads: red from V mA (or 10 A on that range) and black from COM, along their lanes to the probe points ---
  function leads(st) {
    const [pa, pb] = PTS[st.pos], red = G.jacks[st.key === 'A10' ? 2 : 1], black = G.jacks[0];
    const lead = (j, pt, k, col) => {
      const px = X(pt[0]), py = Y(pt[1]), yb = G.laneB[k], xr = X(LANE_R[k]);
      let pts;
      if (pt[1] === BOT) pts = [[j[0], j[1]], [j[0], yb], [px, yb], [px, py]];
      else if (pt[0] === RIGHT) pts = [[j[0], j[1]], [j[0], yb], [xr, yb], [xr, py], [px, py]];
      else pts = [[j[0], j[1]], [j[0], yb], [xr, yb], [xr, Y(LANE_T[k])], [px, Y(LANE_T[k])], [px, py]];
      p.noFill(); p.stroke(...col); p.strokeWeight(3.5 * sk); rounded(pts, 12 * sk);
      p.noStroke(); p.fill(...col); p.circle(px, py, 11 * sk);
      p.fill(...WHITE); p.circle(px, py, 4 * sk);
    };
    lead(black, pb, 0, INKC);
    lead(red, pa, 1, LEADR);
  }
  // a polyline with rounded corners (a lead lying on the bench)
  function rounded(pts, r) {
    p.beginShape(); p.vertex(...pts[0]);
    for (let i = 1; i < pts.length - 1; i++) {
      const [x0, y0] = pts[i - 1], [x1, y1] = pts[i], [x2, y2] = pts[i + 1];
      const d1 = Math.hypot(x1 - x0, y1 - y0) || 1, d2 = Math.hypot(x2 - x1, y2 - y1) || 1, q = Math.min(r, d1 / 2, d2 / 2);
      p.vertex(x1 - (x1 - x0) / d1 * q, y1 - (y1 - y0) / d1 * q);
      p.quadraticVertex(x1, y1, x1 + (x2 - x1) / d2 * q, y1 + (y2 - y1) / d2 * q);
    }
    p.vertex(...pts[pts.length - 1]); p.endShape();
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, col, size) {
    const z = size || fh;
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(z);
    const w = p.textWidth(s), xa = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    const x0 = Math.min(Math.max(xa, 2), 600 - w - 2);
    y = Math.min(Math.max(y, 0.8 * z), G.H - 0.3 * z);
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * z, x1: x0 + w, y1: y + 0.25 * z });
  }
  function grect(x, y, w, h, stops) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, x, y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.join(',')})`));
    c.fillStyle = gr; c.fillRect(x, y, w, h); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
