// fy4-4 Newtonin toinen laki: a laboratory cart on a level track, pulled by a string from a winch at either end with a constant
// force F (a force-controlled winch), with mass blocks on the cart. Model: friction and air resistance are neglected, so the
// weight G = mg and the track's normal force N cancel and the net force is the pull: ΣF_x = ±F. The cart starts at rest or moving
// to the right at 1,5 m/s; the run lasts 1,0 s or until the cart nears an end of the 2,0 m track. The velocity is sampled
// every 0,05 s of simulated time into a (t, v_x) graph, and the acceleration a_x is the slope of the line fitted to the samples
// (shown when the run ends), so the student reads a from the motion and compares it with ΣF and m.
// Top left: the situation picture (tilannekuva) with the velocity (blue) and the acceleration (orange) beside the cart, never
// forces. Right: the cart's force diagram (voimakuvio), a plain rectangle with every force from its point of application, all
// to one scale (11 px per newton), so the pull is short beside the weight, as it is. Bottom: the (t, v_x) graph.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, S = 11;                                                   // m/s², px per newton in the force diagram
  const X0 = 20, PX = 182, TOP = 150;                                      // track: x = 0 m at px 20, 182 px per metre, its top at y 150
  const V0 = 1.5, TMAX = 1.0, DT = 0.05;                                   // initial speed when moving (m/s), run length (s), sampling (s)
  const D = { x: 506, y: 205, w: 64, h: 40 };                              // force diagram: the cart as a rectangle
  const GR = { x0: 58, x1: 380, y0: 294, k: 16 };                          // graph: t = 0 and t = 1 s, v = 0 and px per m/s
  const RED = [201, 42, 42], BLUE = [25, 113, 194], ORANGE = [232, 89, 12], INKC = [31, 41, 51], MUTEDC = [107, 116, 128];
  let btn, slF, lF, selM, selAlku, selSuunta, selSpeed, readout;
  let t = 0, running = false, done = false, samples = [], aMeas = null, tEnd = TMAX, labels = [];

  const model = () => {
    const F = Number(slF.value()), m = Number(selM.value()), dir = selSuunta.value() === 'vasen' ? -1 : 1;
    const v0 = selAlku.value() === 'vauhdissa' ? V0 : 0, Fx = dir * F, a = Fx / m;
    const x0 = v0 === 0 && dir < 0 ? 1.8 : 0.2;
    return { F, m, dir, v0, Fx, a, x0, G: m * g };
  };
  const pos = (M, tt) => M.x0 + M.v0 * tt + 0.5 * M.a * tt * tt;
  const vel = (M, tt) => M.v0 + M.a * tt;
  const findEnd = (M) => {                                                 // the run stops at 1,0 s or 0,1 m from an end
    for (let tt = 0; tt <= TMAX; tt += 0.0005) { const x = pos(M, tt); if (x >= 1.9 || x <= 0.1) return Math.max(tt, DT * 2); }
    return TMAX;
  };
  const restart = () => { const M = model(); t = 0; running = false; done = false; aMeas = null; tEnd = findEnd(M); samples = [[0, M.v0]]; };
  const fit = (pts) => {                                                   // least-squares slope of v against t
    const n = pts.length, mt = pts.reduce((s, q) => s + q[0], 0) / n, mv = pts.reduce((s, q) => s + q[1], 0) / n;
    let num = 0, den = 0; for (const [a, b] of pts) { num += (a - mt) * (b - mv); den += (a - mt) * (a - mt); }
    return den ? num / den : 0;
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { if (done) { restart(); running = true; } else running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const l1 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l1); slF = p.createSlider(0, 3, 1, 0.5).parent(l1);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of ['0.5', '1', '1.5']) selM.option(Number(m).toFixed(m === '0.5' ? 2 : 1).replace('.', DECP) + ' kg', m);
    selM.selected('1');
    const la = p.createElement('label').parent(controls); p.createSpan(__('alku')).parent(la); selAlku = p.createSelect().parent(la);
    selAlku.option(__('levosta'), 'levosta'); selAlku.option(__('vauhdissa'), 'vauhdissa');
    const ld = p.createElement('label').parent(controls); p.createSpan(__('suunta')).parent(ld); selSuunta = p.createSelect().parent(ld);
    selSuunta.option(__('oikea'), 'oikea'); selSuunta.option(__('vasen'), 'vasen');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.2'); selSpeed.option(__('normaali'), '0.4'); selSpeed.option(__('nopea'), '1'); selSpeed.selected('0.4');
    for (const e of [slF.elt, selM.elt, selAlku.elt, selSuunta.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { F: { input: slF.elt, unit: 'N' }, m: { input: selM.elt, unit: 'kg' }, alku: { input: selAlku.elt, unit: '' }, suunta: { input: selSuunta.elt, unit: '' } },
      reset: () => { slF.value(1); selM.selected('1'); selAlku.selected('levosta'); selSuunta.selected('oikea'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const M = model();
    if (running) {
      t = Math.min(t + Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()), tEnd);
      while (samples.length && samples[samples.length - 1][0] + DT <= t + 1e-9) { const ts = samples[samples.length - 1][0] + DT; samples.push([ts, vel(M, ts)]); }
      if (t >= tEnd - 1e-9) {
        if (tEnd - samples[samples.length - 1][0] > 1e-6) samples.push([tEnd, vel(M, tEnd)]);
        running = false; done = true; aMeas = fit(samples);
      }
    }
    const x = pos(M, t), v = vel(M, t);
    lF.html(__('voima', { F: tx(M.F, 1) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { Fx: tx(M.Fx, 1), m: tx(M.m, M.m < 1 ? 2 : 1), G: tx(M.G, 1), sx: tx(M.Fx, 1), t: tx(t, 2), x: tx(x, 2), v: tx(v, 2),
                                 a: aMeas === null ? '\\ldots' : tx(aMeas, 2) }));
    window.simState = { F: M.F, m: M.m, alku: selAlku.value(), suunta: selSuunta.value(), Fx: M.Fx, G: M.G, N: M.G, sumFx: M.Fx, sumFy: 0,
                        aModel: M.a, t, x, v, a: aMeas, running, done, labels: null };
    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    p.background(250);
    situation(M, x, v, fh);
    diagram(M, fh);
    graph(M, fh, k);
    window.simState.labels = labels;
  };

  // --- the situation picture: the lab wall, the track on the bench with its scale, the winches, the cart, v and a beside it ---
  function situation(M, x, v, fh) {
    grect(0, 0, 406, TOP, [[240, 244, 248], [225, 232, 240]], 0);
    grect(0, TOP, 406, 46, [[233, 201, 138], [217, 178, 106]], 0);
    p.noStroke(); p.fill(196, 204, 212); p.rect(X0, TOP, 2 * PX, 7);       // the aluminium track
    p.stroke(138, 150, 163); p.strokeWeight(1.5); p.line(X0, TOP + 3.5, X0 + 2 * PX, TOP + 3.5);
    p.stroke(...INKC); p.strokeWeight(1);                                  // the scale on the bench edge: 0,1 m ticks
    for (let i = 0; i <= 20; i++) { const xx = X0 + i * PX / 10; p.line(xx, TOP + 9, xx, TOP + (i % 5 ? 14 : 20)); }
    for (const [s, xm] of [['$0$', 0], ['$1{,}0\\,\\text{m}$', 1], ['$2{,}0$', 2]]) lab(s, X0 + xm * PX, TOP + 38, 'c', fh, INKC);
    for (const [wx, on] of [[3, M.dir < 0], [388, M.dir > 0]]) {           // the winches; the pulling one has a lit lamp
      grect(wx, TOP - 30, 15, 34, [[134, 142, 150], [96, 104, 112]], 3);
      p.noStroke(); p.fill(on && M.F > 0 ? 43 : 160, on && M.F > 0 ? 138 : 160, on && M.F > 0 ? 62 : 160); p.circle(wx + 7.5, TOP - 22, 6);
      p.fill(70); p.circle(wx + 7.5, TOP - 9, 9);
    }
    const cx = X0 + PX * x, top = TOP - 26;
    if (M.F > 0) {                                                          // the string from the cart to the pulling winch
      p.stroke(120, 90, 50); p.strokeWeight(1.5);
      if (M.dir > 0) p.line(cx + 18, top + 8, 395, TOP - 9); else p.line(cx - 18, top + 8, 10, TOP - 9);
    }
    grect(cx - 18, top, 36, 17, [[120, 160, 200], [60, 100, 150]], 3);
    p.noStroke(); p.fill(31, 41, 51); p.circle(cx - 10, TOP - 5, 10); p.circle(cx + 10, TOP - 5, 10);
    p.fill(196, 204, 212); p.circle(cx - 10, TOP - 5, 4); p.circle(cx + 10, TOP - 5, 4);
    const nb = Math.round((M.m - 0.5) / 0.25);                              // mass blocks of 0,25 kg on a 0,50 kg cart
    for (let i = 0; i < nb; i++) grect(cx - 15 + (i % 2) * 16, top - 10 - Math.floor(i / 2) * 10, 14, 9, [[160, 166, 172], [100, 106, 112]], 1);
    motion(cx, 86, v, 18, BLUE, '$\\overline{v}$', fh);
    if (t > 0) motion(cx, 58, M.a, 12, ORANGE, '$\\overline{a}$', fh);
    lab(__('tilannekuva'), 10, 22, 'l', fh, INKC);
    lab(`$t = ${tx(t, 2)}\\,\\text{s}$`, 398, 22, 'r', fh, INKC);
  }
  function motion(x0, y, val, scale, col, name, fh) {                      // a thin arrow with an open head beside the cart
    if (Math.abs(val) < 0.02) return;
    const dir = Math.sign(val), room = dir > 0 ? 398 - x0 : x0 - 6;
    const L = dir * Math.max(10, Math.min(Math.abs(val) * scale, room)), x2 = x0 + L;
    p.stroke(...col); p.strokeWeight(2.5); p.line(x0, y, x2, y);
    p.line(x2, y, x2 - dir * 8, y - 5); p.line(x2, y, x2 - dir * 8, y + 5);
    p.textSize(fh); const w = p.textWidth(name);
    if (dir > 0 ? x2 + 6 + w < 400 : x2 - 6 - w > 0) lab(name, x2 + dir * 6, y + fh * 0.36, dir > 0 ? 'l' : 'r', fh, col);
    else lab(name, x0 - dir * 6, y + fh * 0.36, dir > 0 ? 'r' : 'l', fh, col);
  }

  // --- the force diagram: the cart as a plain rectangle; G from the centre, N from the bottom face beside it, the pull from the side ---
  function diagram(M, fh) {
    p.noStroke(); p.fill(255); p.rect(406, 0, 194, 400);
    p.stroke(220); p.strokeWeight(1); p.line(406, 0, 406, 400);
    lab(__('voimakuvio'), 414, 22, 'l', fh, INKC);
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2); p.rect(D.x - D.w / 2, D.y - D.h / 2, D.w, D.h);
    arrow([D.x, D.y], [0, -M.G], '$\\overline{G}$', fh, [0, 18]);
    arrow([D.x - 14, D.y + D.h / 2], [0, M.G], '$\\overline{N}$', fh, [0, -14]);
    if (M.F > 0) arrow([D.x + M.dir * D.w / 2, D.y - 4], [M.Fx, 0], '$\\overline{F}$', fh, [M.dir * 16, 0]);
  }
  function arrow(at, vec, name, fh, off) {
    const x2 = at[0] + vec[0] * S, y2 = at[1] - vec[1] * S, L = Math.hypot(x2 - at[0], y2 - at[1]);
    if (L < 1) return;
    const a = Math.atan2(y2 - at[1], x2 - at[0]), H = Math.min(11, L * 0.7);
    p.stroke(...RED); p.strokeWeight(3.5); p.line(at[0], at[1], x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
    lab(name, x2 + off[0], y2 + off[1] + fh * 0.36, 'c', fh, RED);
  }

  // --- the (t, v_x) graph: the samples so far as blue points; when the run ends, the fitted line (orange) and its slope a_x ---
  function graph(M, fh, k) {
    const X = (tt) => GR.x0 + tt * (GR.x1 - GR.x0), Y = (vv) => GR.y0 - vv * GR.k;
    p.noStroke(); p.fill(255); p.rect(0, 196, 406, 204);
    p.stroke(227, 220, 203); p.strokeWeight(1);
    for (let i = 1; i <= 10; i++) p.line(X(i / 10), Y(5), X(i / 10), Y(-5));
    for (let j = -5; j <= 5; j++) if (j) p.line(X(0), Y(j), X(1), Y(j));
    p.stroke(...INKC); p.strokeWeight(2);
    p.line(X(0), Y(0), X(1) + 12, Y(0)); p.line(X(0), Y(-5), X(0), Y(5) - 12);
    p.noStroke(); p.fill(...INKC);
    p.triangle(X(1) + 18, Y(0), X(1) + 9, Y(0) - 4, X(1) + 9, Y(0) + 4); p.triangle(X(0), Y(5) - 18, X(0) - 4, Y(5) - 9, X(0) + 4, Y(5) - 9);
    const vt = k > 1.5 ? [-4, 0, 4] : [-4, -2, 0, 2, 4];
    for (const j of vt) lab(`$${tx(j, 0)}$`, X(0) - 6, Y(j) + fh * 0.36, 'r', fh, MUTEDC);
    const tt = k > 1.5 ? [0.5, 1] : [0.2, 0.4, 0.6, 0.8, 1];
    for (const s of tt) lab(`$${tx(s, 1)}$`, X(s), 394, 'c', fh, MUTEDC);
    lab('$v_x\\ (\\text{m/s})$', X(0) + 8, 212, 'l', fh, INKC);
    lab('$t\\ (\\text{s})$', 398, Y(0) - 10, 'r', fh, INKC);
    if (done && samples.length > 1) {
      const t1 = samples[samples.length - 1][0], v0 = samples.reduce((s, q) => s + q[1], 0) / samples.length - aMeas * samples.reduce((s, q) => s + q[0], 0) / samples.length;
      p.stroke(...ORANGE); p.strokeWeight(2.5); p.line(X(0), Y(v0), X(t1), Y(v0 + aMeas * t1));
      lab(`$a_x = ${tx(aMeas, 2)}\\,\\text{m/s}^2$`, 398, 214, 'r', fh, ORANGE);
    }
    p.noStroke(); p.fill(...BLUE);
    for (const [a, b] of samples) if (a <= t + 1e-9) p.circle(X(a), Y(b), 7);
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
    c.fillStyle = gr; c.strokeStyle = r ? 'rgba(0,0,0,0.35)' : 'rgba(0,0,0,0)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  // a number in LaTeX with the page language's decimal sign (lang "format.decimal": {,} in Finnish, . in English)
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const DECP = DEC === '.' ? '.' : ',';
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
