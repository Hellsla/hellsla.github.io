// fy4-3 Vuorovaikutus ja voima: a hand pushes a 10 kg box along a 0,50 m run-up until it moves at v0, lets go, and the box
// slides on a chosen surface. Model: during the push the box speeds up evenly (a_p = v0² / (2 · 0,50 m)), so the hand's
// force is F = m·a_p + F_μ (computed for the picture only); after the release nothing pushes the box: on its force diagram
// remain the weight G = mg, the floor's normal force N = G and the constant sliding friction F_μ backwards (matto 40 N,
// puulattia 20 N, jää 10 N, kitkaton 0 N), so the box slows down evenly (F_μ / m) until it stops, or with no friction keeps
// its speed until the end of the 12 m lane. When the box rests, no friction acts. The result of a run (sliding distance s,
// sliding time t and the speed at the end) appears in simState once the run has ended.
// Top: the situation picture (tilannekuva) with the velocity as a thin blue arrow above the box, never a force. Bottom
// left: the (t, v) graph of the run. Bottom right: the box's force diagram (voimakuvio), the box a plain rectangle, every
// force a red arrow from its point of application drawn to one scale (a push ends at the box's rear side; friction starts
// at the rear bottom corner); no point-particle diagram (Finnish upper secondary). Every canvas text goes through lab(),
// which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, M = 10, RUNUP = 0.5, LANE = 12, S = 0.7;            // m/s², kg, m, m, px per newton in the diagram
  const FRICTION = { matto: 40, puu: 20, jaa: 10, kitkaton: 0 };     // N, model values of the sliding friction
  const FLOOR = 132, X0 = 46, PXM = 42;                               // situation: floor level, x = −0,5 m at X0, px per metre
  const GR = { x0: 56, y0: 362, x1: 300, y1: 224, tmax: 6, vmax: 3.5 }; // the (t, v) graph's plot area and ranges
  const D = { x: 482, y: 300, w: 72, h: 44 };                         // force diagram: the box (centre, size)
  const RED = [201, 42, 42], BLUE = [25, 113, 194], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  let btn, selPinta, slV0, lV0, selSpeed, readout;
  let x, v, t, tRel, phase, running, trace, result, labels = [];

  const X = (xm) => X0 + (xm + RUNUP) * PXM;
  const params = () => ({ pinta: selPinta.value(), v0: Number(slV0.value()), Fmu: FRICTION[selPinta.value()] });
  const restart = () => { x = -RUNUP; v = 0; t = 0; tRel = 0; phase = 'valmis'; running = false; trace = [[0, 0]]; result = null; };

  // the box's motion over a simulated time step (exact for constant acceleration within a phase)
  function advance(dt) {
    const P = params();
    while (dt > 1e-9 && phase !== 'loppu') {
      if (phase === 'valmis') phase = 'tyonto';
      if (phase === 'tyonto') {
        const a = P.v0 * P.v0 / (2 * RUNUP), tLeft = (P.v0 - v) / a, h = Math.min(dt, tLeft);
        x += v * h + a * h * h / 2; v += a * h; t += h; dt -= h;
        if (h >= tLeft - 1e-12) { v = P.v0; x = 0; phase = 'liuku'; }
      } else {
        const dec = P.Fmu / M, tStop = dec > 0 ? v / dec : Infinity, tEnd = v > 0 ? solveEnd(v, dec) : Infinity;
        const h = Math.min(dt, tStop, tEnd);
        x += v * h - dec * h * h / 2; v = Math.max(0, v - dec * h); t += h; tRel += h; dt -= h;
        if (h >= tStop - 1e-12 && tStop <= tEnd) { v = 0; finish(); }
        else if (h >= tEnd - 1e-12) { x = LANE; finish(); }
      }
      trace.push([t, v]);
    }
  }
  function solveEnd(v0, dec) {                                        // time to reach the lane's end, if the box gets there
    const d = LANE - x;
    if (dec === 0) return d / v0;
    const disc = v0 * v0 - 2 * dec * d;
    return disc < 0 ? Infinity : (v0 - Math.sqrt(disc)) / dec;
  }
  function finish() { phase = 'loppu'; running = false; result = { s: x, tl: tRel, vl: v }; }

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (phase === 'loppu') restart(); running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lp = p.createElement('label').parent(controls); p.createSpan(__('pinta')).parent(lp); selPinta = p.createSelect().parent(lp);
    for (const k of ['matto', 'puu', 'jaa', 'kitkaton']) selPinta.option(__(k), k);
    selPinta.selected('puu');
    const l1 = p.createElement('label').parent(controls); lV0 = p.createSpan('').parent(l1); slV0 = p.createSlider(1, 3, 2, 0.5).parent(l1);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    for (const e of [selPinta.elt, slV0.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { pinta: { input: selPinta.elt, unit: '' }, v0: { input: slV0.elt, unit: 'm/s' } },
      reset: () => { selPinta.selected('puu'); slV0.value(2); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    if (running) advance(Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()));
    const P = params(), G = M * g;
    const pushing = phase === 'tyonto', sliding = phase === 'liuku' && v > 0;
    const F = pushing ? M * P.v0 * P.v0 / (2 * RUNUP) + P.Fmu : 0;   // the hand's force during the push
    const Fmu = (pushing || sliding) ? P.Fmu : 0;                       // sliding friction while the box moves
    const sumFx = F - Fmu;
    lV0.html(__('lahtonopeus', { v: tx(P.v0, 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { F: tx(F, 0), Fmu: tx(Fmu, 0), sx: tx(sumFx, 0), G: tx(G, 1), N: tx(G, 1),
      v: tx(v, 2), s: tx(Math.max(0, x), 2), t: tx(tRel, 2) }));
    window.simState = { pinta: P.pinta, v0: P.v0, m: M, F, Fmu, sumFx, G, N: G, v, x, t, tRel, phase, running,
      s: result ? result.s : null, tl: result ? result.tl : null, vl: result ? result.vl : null, labels: null };
    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    p.background(250);
    situation(P, fh, k, pushing);
    graph(fh, k);
    diagram(F, Fmu, G, fh);
    window.simState.labels = labels;
  };

  // --- the situation picture: wall, the chosen floor with metre marks, the box, the hand, the velocity above the box ---
  function situation(P, fh, k, pushing) {
    backdrop(P.pinta);
    floor(P.pinta);
    p.stroke(...INKC); p.strokeWeight(2); p.line(0, FLOOR, 600, FLOOR);
    for (let m = 0; m <= LANE; m++) {
      p.stroke(...MUTEDC); p.strokeWeight(1.5); p.line(X(m), FLOOR + 22, X(m), FLOOR + 28);
      if (m % (k > 1.5 ? 4 : 2) === 0) lab(m === LANE ? `$${m}\\,\\text{m}$` : `$${m}$`, X(m), FLOOR + 26 + fh * 0.95, m === LANE ? 'r' : 'c', fh, MUTEDC);
    }
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.line(X(0), FLOOR + 25, X(LANE), FLOOR + 25);
    // the box: a wooden crate, its centre at x
    const bw = 40, bh = 30, bx = X(Math.min(x, LANE)) - bw / 2, by = FLOOR - bh;
    grect(bx, by, bw, bh, [[233, 201, 138], [217, 178, 106]], false, 2);
    p.stroke(169, 122, 53); p.strokeWeight(1.5); p.line(bx + 3, by + bh / 2, bx + bw - 3, by + bh / 2);
    p.line(bx + 3, by + 3, bx + bw - 3, by + bh - 3);
    // the hand: pushes the rear of the box during the run-up, then stays at the release point
    const hx = pushing || phase === 'valmis' ? bx : X(0) - bw / 2;
    p.stroke(25, 113, 194, 110); p.strokeWeight(12); p.line(0, FLOOR - 16, hx - 9, FLOOR - 14);
    p.noStroke(); p.fill(241, 223, 181); p.stroke(...INKC); p.strokeWeight(1.5); p.circle(hx - 6, FLOOR - 14, 14);
    // the velocity: beside (above) the box, thin, blue, open head; not a force
    if (v > 0.02) {
      const len = 12 + v * 18, cx = bx + bw / 2, yv = by - 22;
      p.stroke(...BLUE); p.strokeWeight(2.5); p.line(cx - len / 2, yv, cx + len / 2, yv);
      p.line(cx + len / 2, yv, cx + len / 2 - 8, yv - 5); p.line(cx + len / 2, yv, cx + len / 2 - 8, yv + 5);
      lab('$\\overline{v}$', Math.min(cx + len / 2 + 6, 590 - fh), yv + fh * 0.36, 'l', fh, BLUE);
    }
    lab(__('tilannekuva'), 10, 20, 'l', fh, INKC);
  }
  // the surroundings: a room for the mat and the wooden floor, a rink for the ice, an empty grid for the thought experiment
  function backdrop(kind) {
    if (kind === 'jaa') {
      grect(0, 0, 600, FLOOR, [[208, 230, 251], [238, 245, 249]], false, 0);
      for (let i = 0; i < 6; i++) { p.noStroke(); p.fill(255, 255, 255, 140); p.ellipse(60 + i * 100, 30, 70, 14); }
      grect(0, 26, 600, 36, [[255, 255, 255], [238, 245, 249]], false, 0);   // the boards on the far side of the rink
      p.stroke(...INKC); p.strokeWeight(2); p.line(0, 26, 600, 26); p.line(0, 62, 600, 62);
      const cols = [[25, 113, 194], [201, 42, 42], [43, 138, 62], [232, 89, 12]];
      for (let i = 0; i < 8; i++) { p.noStroke(); p.fill(...cols[i % 4]); p.rect(12 + i * 75, 32, 56, 24, 3); p.fill(255, 255, 255, 210); p.rect(20 + i * 75, 40, 30, 6); }
      grect(0, 62, 600, FLOOR - 62, [[248, 251, 253], [208, 230, 251]], false, 0);   // the ice between the boards and the lane
      p.stroke(165, 216, 255); p.strokeWeight(2); for (let xx = 40; xx < 600; xx += 110) p.line(xx, 80, xx + 40, 80);
    } else if (kind === 'kitkaton') {
      grect(0, 0, 600, FLOOR, [[246, 241, 230], [255, 255, 255]], false, 0);
      p.stroke(227, 220, 203); p.strokeWeight(1);
      for (let xx = 0; xx <= 600; xx += 30) p.line(xx, 0, xx, FLOOR);
      for (let yy = FLOOR; yy >= 0; yy -= 30) p.line(0, yy, 600, yy);
    } else {
      grect(0, 0, 600, FLOOR, [[241, 223, 181], [233, 201, 138]], false, 0);
      for (const wx of [150, 420]) {                                   // two windows with sky and a cloud
        grect(wx, 22, 96, 66, [[165, 216, 255], [238, 245, 249]], false, 3);
        p.noStroke(); p.fill(255); p.ellipse(wx + 34, 48, 34, 14); p.ellipse(wx + 48, 44, 26, 14);
        p.noFill(); p.stroke(...INKC); p.strokeWeight(2); p.rect(wx, 22, 96, 66, 3); p.line(wx + 48, 22, wx + 48, 88); p.line(wx, 55, wx + 96, 55);
        p.fill(201, 194, 178); p.rect(wx - 6, 88, 108, 6, 2);
      }
      p.noStroke(); p.fill(255); p.rect(0, FLOOR - 10, 600, 10); p.stroke(...INKC); p.strokeWeight(1.5); p.line(0, FLOOR - 10, 600, FLOOR - 10);
    }
  }
  function floor(kind) {
    const y = FLOOR, h = 14;
    if (kind === 'matto') {
      grect(X(-RUNUP) - 30, y, 600, h, [[184, 98, 45], [150, 70, 35]], false, 0);
      p.stroke(242, 166, 156, 150); p.strokeWeight(1); for (let xx = 0; xx < 600; xx += 6) p.line(xx, y + 2, xx + 3, y + h - 2);
    } else if (kind === 'puu') {
      grect(0, y, 600, h, [[241, 223, 181], [217, 178, 106]], false, 0);
      p.stroke(169, 122, 53, 160); p.strokeWeight(1); for (let xx = 18; xx < 600; xx += 64) p.line(xx, y, xx, y + h);
    } else if (kind === 'jaa') {
      grect(0, y, 600, h, [[238, 245, 249], [165, 216, 255]], false, 0);
      p.stroke(255, 255, 255, 200); p.strokeWeight(2); for (let xx = 30; xx < 600; xx += 90) p.line(xx, y + 4, xx + 26, y + 4);
    } else {
      grect(0, y, 600, h, [[255, 255, 255], [227, 220, 203]], false, 0);
      p.stroke(...MUTEDC); p.strokeWeight(1); p.drawingContext.setLineDash([4, 4]); p.line(0, y + h, 600, y + h); p.drawingContext.setLineDash([]);
    }
  }

  // --- the (t, v) graph of the run so far ---
  function graph(fh, k) {
    p.noStroke(); p.fill(255); p.rect(0, 180, 336, 220);
    p.stroke(220); p.strokeWeight(1); p.line(0, 180, 600, 180); p.line(336, 180, 336, 400);
    const TX = (tt) => GR.x0 + tt / GR.tmax * (GR.x1 - GR.x0), VY = (vv) => GR.y0 - vv / GR.vmax * (GR.y0 - GR.y1);
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let i = 1; i <= GR.tmax; i++) p.line(TX(i), GR.y0, TX(i), GR.y1);
    for (let j = 1; j <= 3; j++) p.line(GR.x0, VY(j), GR.x1, VY(j));
    p.stroke(...INKC); p.strokeWeight(2); p.line(GR.x0, GR.y0, GR.x1 + 14, GR.y0); p.line(GR.x0, GR.y0, GR.x0, GR.y1 - 14);
    p.noStroke(); p.fill(...INKC);
    p.triangle(GR.x1 + 20, GR.y0, GR.x1 + 10, GR.y0 - 4, GR.x1 + 10, GR.y0 + 4);
    p.triangle(GR.x0, GR.y1 - 20, GR.x0 - 4, GR.y1 - 10, GR.x0 + 4, GR.y1 - 10);
    for (let i = 1; i <= GR.tmax; i++) if (k <= 1.5 || i % 2 === 0) lab(`$${i}$`, TX(i), GR.y0 + 6 + fh, 'c', fh, MUTEDC);
    for (let j = 1; j <= 3; j++) lab(`$${j}$`, GR.x0 - 6, VY(j) + fh * 0.36, 'r', fh, MUTEDC);
    lab('$0$', GR.x0 - 6, GR.y0 + 6 + fh * 0.6, 'r', fh, MUTEDC);
    lab('$v\\ (\\text{m/s})$', GR.x0 + 8, GR.y1 - 14, 'l', fh, INKC);
    lab('$t\\ (\\text{s})$', GR.x1 + 24, GR.y0 - fh * 0.9, 'r', fh, INKC);
    p.noFill(); p.stroke(...BLUE); p.strokeWeight(3); p.beginShape();
    for (const [tt, vv] of trace) { if (tt > GR.tmax) break; p.vertex(TX(tt), VY(vv)); }
    p.endShape();
    if (t <= GR.tmax) { p.noStroke(); p.fill(...BLUE); p.circle(TX(t), VY(v), 9); }
  }

  // --- the force diagram: the box a plain rectangle; G from the centre, N from the bottom face, the push ending at the
  //     rear side, friction from the rear bottom corner; one scale for every setting ---
  function diagram(F, Fmu, G, fh) {
    lab(__('voimakuvio'), 348, 214, 'l', fh, INKC);
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2); p.rect(D.x - D.w / 2, D.y - D.h / 2, D.w, D.h);
    const left = D.x - D.w / 2, bottom = D.y + D.h / 2;
    arrow([D.x, D.y], [0, -G], '$\\overline{G}$', [16, 4], fh, 'l');
    arrow([D.x - 18, bottom], [0, G], '$\\overline{N}$', [-14, -4], fh, 'r');
    if (F > 0) {
      const tail = [left - F * S, D.y - 8];
      arrow(tail, [F, 0], '$\\overline{F}$', [F * S / 2, -14], fh, 'c', true);
    }
    if (Fmu > 0) arrow([left, bottom], [-Fmu, 0], '$\\overline{F}_\\mu$', [0, 0], fh, 'c', false, true);
  }
  // an arrow from `at` along vec (newtons, y up), at least 12 px long so that a small force still shows; the label at
  // the tip plus off (or at its middle for a push, under it for friction)
  function arrow(at, vec, name, off, fh, align, mid, below) {
    let L = Math.hypot(vec[0], vec[1]) * S; if (L < 0.5) return; L = Math.max(L, 12);
    const ux = vec[0] / Math.hypot(vec[0], vec[1]), uy = -vec[1] / Math.hypot(vec[0], vec[1]);
    const x2 = at[0] + ux * L, y2 = at[1] + uy * L, a = Math.atan2(uy, ux), H = Math.min(11, L * 0.6);
    p.stroke(...RED); p.strokeWeight(3.5); p.line(at[0], at[1], x2 - H * 0.8 * ux, y2 - H * 0.8 * uy);
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.42), y2 - H * Math.sin(a - 0.42), x2 - H * Math.cos(a + 0.42), y2 - H * Math.sin(a + 0.42));
    if (mid) lab(name, at[0] + off[0], at[1] + off[1], 'c', fh, RED);
    else if (below) lab(name, (at[0] + x2) / 2, y2 + fh * 1.5, 'c', fh, RED);
    else lab(name, x2 + off[0], y2 + off[1] + (uy > 0 ? fh * 0.9 : 0), align, fh, RED);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || INKC)); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const gr = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => gr.addColorStop(i / (stops.length - 1), `rgb(${s.map((q) => Math.min(255, Math.round(q))).join(',')})`));
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
