// fy4-5 Voimakuvio ja voimien yhteisvaikutus: a sled on ice pulled by a rope or pushed by a handle at an angle α, beside
// its force diagram. Model: friction on the ice is neglected; the force F of the rope (pull, up from the horizontal) or of
// the handle (push, down from the horizontal) acts at the angle α; weight G = mg is vertical; the ice's normal force N is
// perpendicular to the ice. Vertically the sled does not accelerate: N = G − F sin α (pull) or N = G + F sin α (push).
// Horizontally ΣF_x = F cos α = m a. F ≤ 150 N and m ≥ 20 kg keep F sin α below G, so the sled never leaves the ice.
// Left: the situation picture (tilannekuva) with the velocity v as a thin blue arrow beside the sled, never a force.
// Right: the force diagram (voimakuvio) drawn to one fixed scale for every setting, so lengths can be compared: solid red
// arrows are forces, dashed ones the components of F (checkbox). The sled is a plain rectangle and every force starts at
// its point of application on it (a push ends there, at the handle); no point-particle diagram (Finnish upper secondary).
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, S = 0.32;                                              // m/s², px per newton in the force diagram
  const GROUND = 262, SLED = { x: 150, w: 92, h: 30 };                   // situation: ice level, sled position and size
  const D = { x: 468, y: 196, w: 74, h: 30 };                            // force diagram: the sled's rectangle (centre, size)
  const RED = [201, 42, 42], BLUE = [25, 113, 194], INKC = [31, 41, 51];
  let btn, slF, slA, lF, lA, selTapa, selM, cbKomp, selSpeed, readout;
  let v = 0, scroll = 0, running = false, labels = [];

  const forces = () => {
    const F = Number(slF.value()), al = Number(slA.value()) * Math.PI / 180, m = Number(selM.value());
    const push = selTapa.value() === 'tyonto';
    const G = m * g, Fx = F * Math.cos(al), Fy = (push ? -1 : 1) * F * Math.sin(al);
    const N = G - Fy;                                                    // vertical: N + F_y − G = 0
    return { F, al, m, push, G, Fx, Fy, N, sumFx: Fx, a: Fx / m };
  };
  const restart = () => { v = 0; scroll = 0; running = false; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('kaynnista')).parent(controls);
    btn.elt.addEventListener('click', () => { running = !running; });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lt = p.createElement('label').parent(controls); p.createSpan(__('tapa')).parent(lt); selTapa = p.createSelect().parent(lt);
    selTapa.option(__('veto'), 'veto'); selTapa.option(__('tyonto'), 'tyonto');
    const l1 = p.createElement('label').parent(controls); lF = p.createSpan('').parent(l1); slF = p.createSlider(0, 150, 100, 10).parent(l1);
    const l2 = p.createElement('label').parent(controls); lA = p.createSpan('').parent(l2); slA = p.createSlider(0, 80, 30, 5).parent(l2);
    const lm = p.createElement('label').parent(controls); p.createSpan(__('massa')).parent(lm); selM = p.createSelect().parent(lm);
    for (const m of [20, 30, 40]) selM.option(`${m} kg`, String(m));
    selM.selected('20');
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSpeed = p.createSelect().parent(ls);
    selSpeed.option(__('hidas'), '0.5'); selSpeed.option(__('normaali'), '1'); selSpeed.option(__('nopea'), '2'); selSpeed.selected('1');
    const lk = p.createElement('label').parent(controls); cbKomp = p.createCheckbox('', false).parent(lk); p.createSpan(__('komponentit')).parent(lk);
    for (const e of [selTapa.elt, selM.elt, slF.elt, slA.elt]) { e.addEventListener('input', () => { v = 0; }); e.addEventListener('change', () => { v = 0; }); }
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { F: { input: slF.elt, unit: 'N' }, alpha: { input: slA.elt, unit: '°' }, m: { input: selM.elt, unit: 'kg' }, tapa: { input: selTapa.elt, unit: '' } },
      reset: () => { slF.value(100); slA.value(30); selM.selected('20'); selTapa.selected('veto'); cbKomp.checked(false); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {   // the speed select scales simulated time, so it changes only the pace
    const f = forces();
    if (running) { const dt = Math.min(p.deltaTime, 100) / 1000 * Number(selSpeed.value()); v = Math.min(v + f.a * dt, 12); scroll = (scroll + v * dt * 40) % 60; }
    lF.html(__('voima', { F: tx(f.F, 0) })); lA.html(__('kulma', { a: tx(f.al * 180 / Math.PI, 0) }));
    const bt = running ? __('tauko') : __('kaynnista'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('lukemat', { G: tx(f.G, 0), N: tx(f.N, 0), Fx: tx(f.Fx, 0), Fy: tx(Math.abs(f.Fy), 0), sx: tx(f.sumFx, 0), a: tx(f.a, 2), v: tx(v, 1) }));
    window.simState = { F: f.F, alpha: f.al * 180 / Math.PI, m: f.m, tapa: selTapa.value(), komponentit: cbKomp.checked(),
                        G: f.G, N: f.N, Fx: f.Fx, Fy: f.Fy, sumFx: f.sumFx, sumFy: f.N + f.Fy - f.G, a: f.a, v, running, labels: null };
    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    p.background(250);
    situation(f, fh);
    diagram(f, fh, k);
    window.simState.labels = labels;
  };

  // --- the situation picture: sky, ice with moving marks, the sled, the rope or handle, the velocity beside the sled ---
  function situation(f, fh) {
    grect(0, 0, 330, GROUND, [[206, 230, 250], [242, 248, 255]], false, 0);
    grect(0, GROUND, 330, 400 - GROUND, [[228, 240, 250], [200, 222, 240]], false, 0);
    p.stroke(120, 150, 180); p.strokeWeight(2); p.line(0, GROUND, 330, GROUND);
    p.stroke(160, 185, 210); p.strokeWeight(1.5);
    for (let x = -scroll; x < 330; x += 60) p.line(x, GROUND + 14, x + 26, GROUND + 14);
    const x0 = SLED.x - SLED.w / 2, y0 = GROUND - SLED.h;
    // runners and box
    p.noFill(); p.stroke(70, 80, 95); p.strokeWeight(3); p.line(x0 - 4, GROUND - 2, x0 + SLED.w, GROUND - 2);
    p.arc(x0 + SLED.w, GROUND - 12, 20, 20, -p.HALF_PI, p.HALF_PI);
    grect(x0 + 4, y0, SLED.w - 8, SLED.h - 6, [[214, 120, 60], [176, 86, 40]], false, 4);
    // rope (pull: from the front, up at α) or handle (push: from behind, down at α into the sled)
    const L = 120, ax = f.push ? x0 + 4 : x0 + SLED.w - 4, ay = y0 + 6;
    const ex = f.push ? ax - L * Math.cos(f.al) : ax + L * Math.cos(f.al), ey = ay - L * Math.sin(f.al);
    p.stroke(f.push ? 90 : 150, f.push ? 90 : 110, f.push ? 100 : 60); p.strokeWeight(f.push ? 5 : 2.5); p.line(ax, ay, ex, ey);
    p.noStroke(); p.fill(70); p.circle(ex, ey, 10);                       // the hand
    // the velocity: beside the sled, thin, blue, open head; not a force
    if (v > 0.02) {
      const len = Math.min(80, 14 + v * 12), yv = y0 - 40;
      p.stroke(...BLUE); p.strokeWeight(2.5); p.line(SLED.x - len / 2, yv, SLED.x + len / 2, yv);
      p.line(SLED.x + len / 2, yv, SLED.x + len / 2 - 9, yv - 5); p.line(SLED.x + len / 2, yv, SLED.x + len / 2 - 9, yv + 5);
      lab('$\\mathbf{v}$', SLED.x + len / 2 + 8, yv + fh * 0.36, 'l', fh, BLUE);
    }
    lab(__('tilannekuva'), 10, 22, 'l', fh, INKC);
    lab(`$v = ${tx(v, 1)}\\,\\text{m/s}$`, 10, 22 + fh * 1.5, 'l', fh, BLUE);
  }

  // --- the force diagram: one scale for every setting; the sled a plain rectangle with the points of application ---
  function diagram(f, fh, k) {
    p.noStroke(); p.fill(255); p.rect(338, 0, 262, 400);
    p.stroke(220); p.strokeWeight(1); p.line(338, 0, 338, 400);
    lab(__('voimakuvio'), 350, 22, 'l', fh, INKC);
    const w = D.w, h = D.h;
    p.fill(246, 241, 230); p.stroke(...INKC); p.strokeWeight(2); p.rect(D.x - w / 2, D.y - h / 2, w, h);
    const pG = [D.x, D.y], pN = [D.x - 14, D.y + h / 2];   // N left of G, clear of the F_y label
    const pF = f.push ? [D.x - w / 2, D.y - h / 2] : [D.x + w / 2, D.y - h / 2];   // the handle's or the rope's corner
    const F = [f.Fx, f.Fy];
    arrow(pG, [0, -f.G], '$\\mathbf{G}$', fh, k);
    arrow(pN, [0, f.N], '$\\mathbf{N}$', fh, k);
    if (f.F > 0) {
      // a pull starts at the rope's corner; a push ends at the handle's corner, so the arrow stays off the sled
      const tail = f.push ? [pF[0] - F[0] * S, pF[1] + F[1] * S] : pF;
      arrow(tail, F, '$\\mathbf{F}$', fh, k, f.push);
      if (cbKomp.checked() && f.al > 0.01) {
        dashed(tail, [F[0], 0], '$\\mathbf{F}_x$', fh, k); dashed(tail, [0, F[1]], '$\\mathbf{F}_y$', fh, k);
      }
    }
  }
  function arrow(at, vec, name, fh, k, atTail) {
    const x2 = at[0] + vec[0] * S, y2 = at[1] - vec[1] * S, L = Math.hypot(x2 - at[0], y2 - at[1]);
    if (L < 1) return;
    const a = Math.atan2(y2 - at[1], x2 - at[0]), H = 12;
    p.stroke(...RED); p.strokeWeight(3.5); p.line(at[0], at[1], x2 - H * 0.8 * Math.cos(a), y2 - H * 0.8 * Math.sin(a));
    p.noStroke(); p.fill(...RED);
    p.triangle(x2, y2, x2 - H * Math.cos(a - 0.4), y2 - H * Math.sin(a - 0.4), x2 - H * Math.cos(a + 0.4), y2 - H * Math.sin(a + 0.4));
    if (atTail) lab(name, at[0] - 16 * Math.cos(a), at[1] - 16 * Math.sin(a) + fh * 0.36, 'c', fh, RED);
    else lab(name, x2 + 16 * Math.cos(a), y2 + 16 * Math.sin(a) + fh * 0.36, 'c', fh, RED);
  }
  function dashed(at, vec, name, fh, k) {
    const x2 = at[0] + vec[0] * S, y2 = at[1] - vec[1] * S, L = Math.hypot(x2 - at[0], y2 - at[1]);
    if (L < 6) return;
    const a = Math.atan2(y2 - at[1], x2 - at[0]);
    p.stroke(...RED, 200); p.strokeWeight(2); p.drawingContext.setLineDash([6, 5]); p.line(at[0], at[1], x2, y2); p.drawingContext.setLineDash([]);
    p.noFill(); p.line(x2, y2, x2 - 10 * Math.cos(a - 0.5), y2 - 10 * Math.sin(a - 0.5)); p.line(x2, y2, x2 - 10 * Math.cos(a + 0.5), y2 - 10 * Math.sin(a + 0.5));
    const off = vec[0] !== 0 ? [0, 16] : [-18, 0];   // F_y labelled on its left, away from the label of F
    lab(name, x2 + off[0] + 10 * Math.cos(a), y2 + off[1] + 10 * Math.sin(a) + fh * 0.36, 'c', fh, RED);
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
