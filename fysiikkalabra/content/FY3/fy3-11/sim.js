// fy3-11 Kaasun tekemä työ ja lämpövoimakone: a cylinder of gas under a weighted piston on a hot plate, and a cycle.
// Model: a monatomic ideal gas, U = (3/2)nRT = (3/2)pV, so every energy follows from p and V alone (1 kPa · 1 l = 1 J).
// The weights hold the pressure at p₁ = 200 kPa while the piston moves; the start volume is V₁ = 1,00 l.
//   Heating at constant pressure (the student chooses the heat Q): W_k = p₁ΔV, ΔU = (3/2)p₁ΔV, Q = ΔU + W_k = (5/2)p₁ΔV,
//     so ΔV = 2Q/(5p₁). The (V, p) graph fills the rectangle p₁ΔV as the piston rises.
//   Return A "samassa paineessa": the weights push the piston back at p₁ while the gas gives its heat to the cold water,
//     Q₂ = (5/2)p₁ΔV = Q, work on the gas p₁ΔV, net work W = 0.
//   Return B "jäähdytä ensin": the piston is latched at V₂ and the upper weight slid onto a high shelf; cold water cools
//     the gas at fixed volume until p = p₂ (heat (3/2)V₂(p₁ − p₂) out); the piston then descends at p₂ (heat (5/2)p₂ΔV out,
//     work p₂ΔV on the gas); at V₁ it is latched, a fresh weight is taken from a low shelf and the hot plate heats the gas
//     at fixed volume back to p₁ (heat (3/2)V₁(p₁ − p₂) in). Net work W = (p₁ − p₂)ΔV = the weight moved from the low
//     shelf to the high one, and Q₁ − Q₂ = W.
// Q₁ is all heat from the hot plate in a cycle, Q₂ all heat to the cold water, W the net work of the gas, η = W/Q₁.
// Every phase runs in simulated time (dt·speed), so the "Nopeus" select changes only the pace. Energies in J, p in kPa,
// V in litres. Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const P1 = 200, V1 = 1.0;                                             // kPa, l (the weights' pressure, start volume)
  const DUR = { lammitys: 4, paluuA: 4, jaahdytys: 2.5, paluuB: 3, lisays: 2.5 };   // phase durations (simulated s)
  const HEAT = ['lammitys', 'lisays'], COOL = ['paluuA', 'jaahdytys', 'paluuB'];
  const CYL = { x0: 74, x1: 164, yb: 316, w: 6, pxl: 50, pist: 10, rod: 104, bpk: 0.16 };   // bore, px per l, block px per kPa
  const G = { x0: 290, x1: 580, y0: 236, y1: 40, vmax: 3.5, pmax: 250 };   // (V, p) graph
  const BAR = { x0: 346, x1: 590, y: [294, 330], h: 20, jmax: 1250 };      // energy bars
  const COL = { Q: [210, 60, 40], dU: [135, 85, 190], Wk: [222, 150, 10], Won: [60, 115, 205], Q2: [50, 150, 215] };
  const N = 28, SEED = 11;
  let sQ, lQ, sP, lP, sel, sV, btn, readout, phase = 'alku', u = 0, queue = [], acc, parts = [], k = 1, labels = [];

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent), span = p.createSpan('').parent(label);
    return [p.createSlider(min, max, val, step).parent(label), span];
  };
  const mulberry32 = (a) => () => {                                     // seeded PRNG: particles start the same way every time
    a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const par = () => {                                                   // settings → the process
    const Q = Number(sQ.value()), p2 = Number(sP.value()), dV = 2 * Q / (5 * P1);
    return { Q, p2, dV, V2: V1 + dV, B: sel.value() === 'jäähdytys ensin' };
  };
  const restart = () => {                                               // back to the start state, nothing transferred yet
    phase = 'alku'; u = 0; queue = []; acc = { Qh: 0, Qc: 0, Wg: 0 };
    const rnd = mulberry32(SEED);
    parts = Array.from({ length: N }, (_, a) => (a = 2 * Math.PI * rnd(), { x: rnd(), y: rnd(), dx: Math.cos(a), dy: Math.sin(a) }));
  };
  // contribution of one phase at progress s ∈ [0, 1]: state (V, p) and heat in, heat out, work by the gas so far
  const phaseAt = (ph, s, P) => {
    const { dV, V2, p2 } = P;
    switch (ph) {
      case 'lammitys': return { V: V1 + s * dV, p: P1, Qh: 2.5 * P1 * s * dV, Qc: 0, Wg: P1 * s * dV };
      case 'paluuA': return { V: V2 - s * dV, p: P1, Qh: 0, Qc: 2.5 * P1 * s * dV, Wg: -P1 * s * dV };
      case 'jaahdytys': return { V: V2, p: P1 - s * (P1 - p2), Qh: 0, Qc: 1.5 * V2 * (P1 - p2) * s, Wg: 0 };
      case 'paluuB': return { V: V2 - s * dV, p: p2, Qh: 0, Qc: 2.5 * p2 * s * dV, Wg: -p2 * s * dV };
      case 'lisays': return { V: V1, p: p2 + s * (P1 - p2), Qh: 1.5 * V1 * (P1 - p2) * s, Qc: 0, Wg: 0 };
      case 'ylhaalla': return { V: V2, p: P1, Qh: 0, Qc: 0, Wg: 0 };
      default: return { V: V1, p: P1, Qh: 0, Qc: 0, Wg: 0 };           // alku, valmis
    }
  };
  const running = () => phase in DUR;
  const advance = (dt, P) => {                                          // simulated time; carries over into the next phase
    while (dt > 0 && running()) {
      const left = (1 - u) * DUR[phase];
      if (dt < left) { u += dt / DUR[phase]; return; }
      dt -= left; const c = phaseAt(phase, 1, P); acc.Qh += c.Qh; acc.Qc += c.Qc; acc.Wg += c.Wg;
      const was = phase; u = 0;
      phase = queue.length ? queue.shift() : (was === 'lammitys' ? 'ylhaalla' : 'valmis');
    }
  };
  const go = () => {                                                    // the main button
    if (running()) return;
    if (phase === 'valmis') restart();
    if (phase === 'alku') { phase = 'lammitys'; u = 0; }
    else if (phase === 'ylhaalla') { const B = par().B; queue = B ? ['paluuB', 'lisays'] : []; phase = B ? 'jaahdytys' : 'paluuA'; u = 0; }
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton('Lämmitä').parent(controls); btn.elt.addEventListener('click', go);
    const bR = p.createButton('Alusta').parent(controls); bR.elt.addEventListener('click', restart);
    [sQ, lQ] = slider(controls, 200, 1000, 500, 50);                     // heat given at constant pressure (J)
    const ls = p.createElement('label').parent(controls); p.createSpan('Männän paluu').parent(ls); sel = p.createSelect().parent(ls);
    sel.option('samassa paineessa', 'sama paine'); sel.option('jäähdytä ensin', 'jäähdytys ensin');
    [sP, lP] = slider(controls, 40, 180, 100, 10);                       // pressure after cooling, B only (kPa)
    for (const e of [sQ.elt, sP.elt, sel.elt]) { e.addEventListener('input', restart); e.addEventListener('change', restart); }
    const lv = p.createElement('label').parent(controls); p.createSpan('Nopeus').parent(lv); sV = p.createSelect().parent(lv);
    for (const [txt, v] of [['hidas', 0.4], ['normaali', 1], ['nopea', 2]]) sV.option(txt, v);
    sV.selected('1');                                                  // pace only; every quantity follows simulated time
    const det = p.createElement('details').parent('sim-root').class('note');   // explanations stay behind "Lisätietoja"
    p.createElement('summary', 'Lisätietoja').parent(det);
    p.createP('Luvut ovat mallin arvoja: sylinterissä on yksiatomista ideaalikaasua, jonka sisäenergian muutos on ' +
      'ΔU = (3/2)nRΔT = (3/2)Δ(pV). Mäntä on kitkaton ja painoton, eikä sen yläpuolella ole ilmaa, joten kaasun paineen ' +
      'aiheuttavat punnukset: 200 kPa kahdella punnuksella, alempi punnus yksin antaa paineen p₂. Kuuman levyn oletetaan ' +
      'olevan aina kaasua kuumempi ja kylmän veden kylmempi. Lämpöä ei karkaa muualle.').parent(det);
    p.createP('Kuvaajan oranssi pinta-ala on kaasun tekemä työ Wₖ = pΔV, sininen pinta-ala työ, joka tehdään kaasuun, ' +
      'kun mäntä palautetaan. Palkeissa sama väri tarkoittaa samaa energiaa. Vaihtoehdossa B ylempi punnus siirretään ' +
      'ylös hyllylle ja alhaalta otetaan uusi: kierroksen nettotyö W on punnuksen nostamiseen kulunut energia. ' +
      'Kun mäntä on lukittu (pienet tapit), tilavuus ei muutu.').parent(det);
    restart(); p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { Qin: { input: sQ.elt, unit: 'J' }, paluu: { input: sel.elt, unit: '' }, p2: { input: sP.elt, unit: 'kPa' } },
      reset: () => { sQ.value(500); sP.value(100); sel.selected('sama paine'); sV.selected('1'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const P = par(), speed = Number(sV.value());
    advance(Math.min(p.deltaTime, 100) / 1000 * speed, P);
    const c = phaseAt(phase, u, P), V = c.V, pr = c.p;
    const Q1 = acc.Qh + c.Qh, Q2 = acc.Qc + c.Qc, W = acc.Wg + c.Wg, done = phase === 'valmis';
    const heated = phase === 'lammitys' ? u : phase === 'alku' ? 0 : 1;  // heating progress
    const dVh = heated * P.dV, Wk = P1 * dVh, dU = 1.5 * P1 * dVh, Qh = 2.5 * P1 * dVh;
    const eta = Q1 > 0 ? 100 * W / Q1 : 0, returning = !['alku', 'lammitys', 'ylhaalla'].includes(phase);

    // controls: labels, hidden p₂ in mode A, main button text
    lQ.html(`Lämpö Q = ${P.Q} J`); lP.html(`Paine jäähdytyksen jälkeen p<sub>2</sub> = ${P.p2} kPa`);
    lP.elt.parentElement.style.display = P.B ? '' : 'none';
    const bt = phase === 'alku' ? 'Lämmitä' : phase === 'ylhaalla' ? 'Palauta mäntä' : phase === 'valmis' ? 'Uusi kierros' : (phase === 'lammitys' ? 'Lämmitetään…' : 'Palautetaan…');
    if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    btn.elt.disabled = running();

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(11);
    labels = [];
    p.background(250);
    cylinder(P, phase, u, V, pr, speed, ts);
    graph(P, phase, u, V, pr, done, ts, fh);
    const area = areas(P, phase, u);
    bars(done, Q1, Q2, W, Qh, dU, Wk, ts);

    // readout: at most four short lines
    const J = (x) => `${Math.round(x)} J`, L = (x) => `${fi(x, 2)} l`;
    const lines = [`Lämmitys: ΔV = ${L(dVh)}, W<sub>k</sub> = pΔV = <strong>${J(Wk)}</strong>`,
      `Q = ${J(Qh)}, ΔU = ${J(dU)}, ΔU + W<sub>k</sub> = <strong>${J(dU + Wk)}</strong>`];
    if (!returning) lines.push(phase === 'ylhaalla' ? 'Mäntä on ylhäällä. Palauta se alas.' : 'Lämmitä kaasua kuumalla levyllä.');
    else {
      lines.push(`Kierros${done ? '' : ' kesken'}: Q<sub>1</sub> = ${J(Q1)}, Q<sub>2</sub> = ${J(Q2)}`);
      lines.push(done ? `W = Q<sub>1</sub> − Q<sub>2</sub> = <strong>${J(W)}</strong>, η = W/Q<sub>1</sub> = <strong>${fi(eta, 0)} %</strong>`
        : `Nettotyö tähän asti W = ${J(W)}`);
    }
    readout.html(lines.join('<br>'));
    window.simState = { paluu: sel.value(), Qin: P.Q, p1: P1, p2: P.p2, V1, V2: P.V2, phase, u, done: done ? 1 : 0, V, p: pr,
      dV: dVh, Q: Qh, dU, Wk, Q1, Q2, W, eta, dUcycle: 1.5 * (pr * V - P1 * V1), areaWk: area.wk, areaNet: area.net, speed, labels };
    window.simDebug = { finish: () => advance(1e6, par()), go, restart };
  };

  // the cylinder: hot plate or cold water below, gas particles, piston with a rod, weights, shelves, latch pins
  function cylinder(P, ph, s, V, pr, speed, ts) {
    const { x0, x1, yb, w, pxl, pist, rod, bpk } = CYL, cx = (x0 + x1) / 2, gt = yb - V * pxl, wallTop = yb - 3.0 * pxl - pist - 4;
    const heat = HEAT.includes(ph), cool = COOL.includes(ph), t = p.millis() / 1000;
    // contact slab
    if (heat) grect(x0 - 14, yb + 2, x1 - x0 + 28, 26, [[255, 200, 80], [220, 60, 30]], false, 3);
    else if (cool) {
      grect(x0 - 14, yb + 2, x1 - x0 + 28, 26, [[150, 205, 240], [40, 110, 190]], false, 3);
      p.noFill(); p.stroke(255, 255, 255, 170); p.strokeWeight(1.5); p.beginShape();
      for (let x = x0 - 10; x <= x1 + 10; x += 3) p.vertex(x, yb + 14 + 2 * Math.sin(x / 6 - 3 * t)); p.endShape();
    } else grect(x0 - 14, yb + 2, x1 - x0 + 28, 26, [[205, 205, 210], [160, 160, 168]], false, 3);
    lab(heat ? 'kuuma levy' : cool ? 'kylmä vesi' : 'eriste', cx, yb + 28 + ts(16), 'c', ts(12));
    // gas: colour from pV (cold blue → warm orange), particles faster when pV is larger
    const f = Math.min(1, Math.max(0, (pr * V - 40) / 560)), gc = mix([90, 140, 225], [245, 130, 40], f);
    p.noStroke(); p.fill(...gc, 70); p.rect(x0, gt, x1 - x0, yb - gt);
    const v = 30 * Math.sqrt(pr * V / 200) * speed * Math.min(p.deltaTime, 100) / 1000;
    p.fill(...gc.map((x) => x * 0.75));
    for (const q of parts) {
      q.x += q.dx * v / (x1 - x0); q.y += q.dy * v / Math.max(20, yb - gt);
      if (q.x < 0 || q.x > 1) { q.dx = -q.dx; q.x = Math.min(1, Math.max(0, q.x)); }
      if (q.y < 0 || q.y > 1) { q.dy = -q.dy; q.y = Math.min(1, Math.max(0, q.y)); }
      p.circle(x0 + 4 + q.x * (x1 - x0 - 8), gt + 4 + q.y * (yb - gt - 8), 5);
    }
    // heat arrows: up into the gas from the plate, down out of the gas into the water
    if (heat || cool) {
      p.stroke(...(heat ? COL.Q : COL.Q2)); p.strokeWeight(3); p.noFill();
      for (let i = 0; i < 3; i++) {
        const ax = x0 + 20 + i * 25, ph2 = (t * 0.8 + i / 3) % 1, ya = heat ? yb - 4 - 26 * ph2 : yb - 30 + 26 * ph2;
        p.line(ax, ya, ax, ya + 14); const tip = heat ? ya : ya + 14, d = heat ? 6 : -6;
        p.line(ax, tip, ax - 4, tip + d); p.line(ax, tip, ax + 4, tip + d);
      }
    }
    // walls
    grect(x0 - w, wallTop, w, yb - wallTop + 2, [[95, 98, 108], [175, 180, 190], [95, 98, 108]], true, 1);
    grect(x1, wallTop, w, yb - wallTop + 2, [[95, 98, 108], [175, 180, 190], [95, 98, 108]], true, 1);
    p.noStroke(); p.fill(95, 98, 108); p.rect(x0 - w, yb, x1 - x0 + 2 * w, 3);
    // piston, rod, platform
    grect(x0, gt - pist, x1 - x0, pist, [[130, 134, 142], [200, 204, 212], [130, 134, 142]], false, 2);
    const plat = gt - pist - rod;
    p.fill(120); p.rect(cx - 4, plat, 8, rod);
    grect(cx - 32, plat - 6, 64, 6, [[90, 90, 96], [150, 150, 158]], false, 1);
    if (['jaahdytys', 'lisays'].includes(ph)) {                          // latch pins hold the piston at fixed volume
      p.fill(40); p.triangle(x0, gt - pist - 6, x0 + 8, gt - pist - 6, x0, gt - pist - 14);
      p.triangle(x1, gt - pist - 6, x1 - 8, gt - pist - 6, x1, gt - pist - 14);
    }
    // weights: lower block (p₂ in B, the whole p₁ in A) and the upper block (p₁ − p₂) that B moves between shelves
    const hLow = (P.B ? P.p2 : P1) * bpk, hUp = (P1 - P.p2) * bpk, bw = 56;
    const yLow = plat - 6 - hLow;
    block(cx, yLow, bw, hLow, [70, 75, 85]);
    if (P.B) {
      const platHi = yb - P.V2 * pxl - pist - rod, yHi = platHi - 6 - hLow - hUp;          // upper block level at the top
      const platLo = yb - V1 * pxl - pist - rod, yLo = platLo - 6 - hLow - hUp;            // fresh block level at the bottom
      const sxR = cx + 84, sxL = cx - 82;
      shelf(sxR, yHi + hUp); shelf(sxL, yLo + hUp);
      const slide = (q) => Math.min(1, q / 0.4);
      const order = ['alku', 'lammitys', 'ylhaalla', 'jaahdytys', 'paluuB', 'lisays', 'valmis'], i = order.indexOf(ph);
      // upper block: on the piston until cooling starts, then slides right onto the high shelf
      if (i <= 2) block(cx, yLow - hUp, bw, hUp, [150, 110, 60]);
      else { const q = ph === 'jaahdytys' ? slide(s) : 1; block(cx + q * (sxR - cx), yHi, bw, hUp, [150, 110, 60]); }
      // fresh block: waits on the low shelf, slides onto the piston when the weight is put back at the bottom
      if (i <= 4) block(sxL, yLo, bw, hUp, [150, 110, 60]);
      else { const q = ph === 'lisays' ? slide(s) : 1; block(sxL + q * (cx - sxL), yLow - hUp, bw, hUp, [150, 110, 60]); }
    }
  }
  function block(x, y, bw, h, c) { if (h < 0.5) return; grect(x - bw / 2, y, bw, h, [c.map((v) => v + 40), c], false, 2); }
  function shelf(x, y) {                                                // a shelf on a post standing on the table
    const px = x < CYL.x0 ? x - 26 : x + 26; p.noStroke(); p.fill(150, 130, 105); p.rect(px - 2, y, 4, CYL.yb + 28 - y);
    p.fill(120, 100, 80); p.rect(x - 32, y, 64, 4);
  }

  // (V, p) graph: gridlines, the path so far, the gas work (orange) and the work on the gas (blue)
  function graph(P, ph, s, V, pr, done, ts, fh) {
    const X = (v) => G.x0 + v / G.vmax * (G.x1 - G.x0), Y = (q) => G.y0 - q / G.pmax * (G.y0 - G.y1);
    p.stroke(225); p.strokeWeight(1);
    for (let v = 0.5; v <= G.vmax + 1e-9; v += 0.5) p.line(X(v), G.y0, X(v), G.y1);
    for (let q = 50; q <= G.pmax; q += 50) p.line(G.x0, Y(q), G.x1, Y(q));
    const rects = geometry(P, ph, s);
    p.noStroke();
    if (rects.wk) { p.fill(...COL.Wk, 120); p.rect(X(V1), Y(P1), X(V1 + rects.wk) - X(V1), Y(0) - Y(P1)); }
    if (rects.on) {                                                     // work on the gas: blue, hatched over the orange it cancels
      const [va, vb, q] = rects.on, xa = X(va), xb = X(vb), ya = Y(q), yb = Y(0);
      p.fill(...COL.Won, 55); p.rect(xa, ya, xb - xa, yb - ya);
      const c = p.drawingContext; c.save(); c.beginPath(); c.rect(xa, ya, xb - xa, yb - ya); c.clip();
      p.stroke(...COL.Won, 200); p.strokeWeight(2); for (let x = xa - (yb - ya); x < xb; x += 9) p.line(x, yb, x + (yb - ya), ya);
      c.restore(); p.noStroke();
    }
    // path: heating line, return lines, isochoric steps
    p.strokeWeight(3); p.noFill();
    const seg = (va, qa, vb, qb, c) => { p.stroke(...c); p.line(X(va), Y(qa), X(vb), Y(qb)); };
    const order = ['alku', 'lammitys', 'ylhaalla', 'paluuA', 'jaahdytys', 'paluuB', 'lisays', 'valmis'];
    const reached = (n) => order.indexOf(ph) >= order.indexOf(n);
    if (reached('lammitys')) seg(V1, P1, ph === 'lammitys' ? V : P.V2, P1, COL.Q);
    if (!P.B && reached('paluuA')) seg(P.V2, P1, ph === 'paluuA' ? V : V1, P1, COL.Q2);
    if (P.B && reached('jaahdytys')) seg(P.V2, P1, P.V2, ph === 'jaahdytys' ? pr : P.p2, COL.Q2);
    if (P.B && reached('paluuB')) seg(P.V2, P.p2, ph === 'paluuB' ? V : V1, P.p2, COL.Q2);
    if (P.B && reached('lisays')) seg(V1, P.p2, V1, ph === 'lisays' ? pr : P1, COL.Q);
    // axes
    p.stroke(60); p.strokeWeight(1.5); p.line(G.x0, G.y0, G.x1 + 6, G.y0); p.line(G.x0, G.y0, G.x0, G.y1 - 6);
    p.fill(60); p.noStroke(); p.triangle(G.x1 + 10, G.y0, G.x1 + 2, G.y0 - 4, G.x1 + 2, G.y0 + 4);
    p.triangle(G.x0, G.y1 - 10, G.x0 - 4, G.y1 - 2, G.x0 + 4, G.y1 - 2);
    for (let v = 0; v <= 3; v++) lab(String(v), X(v), G.y0 + fh + 4, 'c', fh);
    for (let q = (k > 1.5 ? 100 : 50); q <= G.pmax; q += (k > 1.5 ? 100 : 50)) lab(String(q), G.x0 - 6, Y(q) + fh * 0.36, 'r', fh);
    lab('V (l)', 596, G.y0 + fh + 4, 'r', fh);
    lab('p (kPa)', G.x0 - 6 - ts(24), G.y1 - fh * 0.9, 'l', fh);
    // current state
    p.fill(255); p.stroke(30); p.strokeWeight(2); p.circle(X(V), Y(pr), 10);
    // area labels: Wₖ while heating, W (the net work left over) when cycle B is done
    const big = ts(13);
    if (rects.wk && !rects.on && ph !== 'jaahdytys') {
      const xm = (X(V1) + X(V1 + rects.wk)) / 2, wpx = X(V1 + rects.wk) - X(V1);
      if (wpx > ts(30)) labSub([['W', 'k']], xm, Y(P1 / 2) + big * 0.36, 'c', big, COL.Wk.map((x) => x * 0.6));
    }
    if (done && P.B) {
      const hpx = Y(P.p2) - Y(P1), wpx = X(P.V2) - X(V1);
      if (hpx > big * 1.3 && wpx > ts(24)) labSub([['W', '']], (X(V1) + X(P.V2)) / 2, (Y(P1) + Y(P.p2)) / 2 + big * 0.36, 'c', big, COL.Wk.map((x) => x * 0.6));
    }
  }
  // the drawn areas: gas work rectangle (ΔV of the heating so far) and the work done on the gas while returning
  function geometry(P, ph, s) {
    const order = ['alku', 'lammitys', 'ylhaalla', 'paluuA', 'jaahdytys', 'paluuB', 'lisays', 'valmis'], i = order.indexOf(ph);
    const wk = ph === 'alku' ? 0 : ph === 'lammitys' ? s * P.dV : P.dV;
    let on = null;
    if (ph === 'paluuA') on = [P.V2 - s * P.dV, P.V2, P1];
    else if (ph === 'paluuB') on = [P.V2 - s * P.dV, P.V2, P.p2];
    else if (ph === 'valmis' || (P.B && i >= order.indexOf('lisays'))) on = [V1, P.V2, P.B ? P.p2 : P1];
    return { wk, on };
  }
  function areas(P, ph, s) {                                            // in J (kPa · l), from the drawn rectangles
    const r = geometry(P, ph, s), wk = P1 * r.wk, on = r.on ? r.on[2] * (r.on[1] - r.on[0]) : 0;
    return { wk, net: wk - on };
  }

  // energy bars: heating Q against ΔU + Wₖ; when the cycle is done Q₁ against W + Q₂
  function bars(done, Q1, Q2, W, Q, dU, Wk, ts) {
    const sc = (BAR.x1 - BAR.x0) / BAR.jmax, fz = ts(12), [y1, y2] = BAR.y, h = BAR.h;
    const row = (y, segs) => { let x = BAR.x0; for (const [v, c] of segs) { const wv = Math.max(0, v) * sc; p.noStroke(); p.fill(...c); p.rect(x, y, wv, h); x += wv; }
      p.noFill(); p.stroke(150); p.strokeWeight(1); p.rect(BAR.x0, y, BAR.x1 - BAR.x0, h); };
    const dark = (c) => c.map((x) => x * 0.7);
    if (done) {
      row(y1, [[Q1, COL.Q]]); row(y2, [[W, COL.Wk], [Q2, COL.Q2]]);
      labSub([['Q', '1', dark(COL.Q)]], BAR.x0 - 8, y1 + h / 2 + fz * 0.36, 'r', fz);
      labSub([['W', '', dark(COL.Wk)], [' + ', ''], ['Q', '2', dark(COL.Q2)]], BAR.x0 - 8, y2 + h / 2 + fz * 0.36, 'r', fz);
    } else {
      row(y1, [[Q, COL.Q]]); row(y2, [[dU, COL.dU], [Wk, COL.Wk]]);
      labSub([['Q', '', dark(COL.Q)]], BAR.x0 - 8, y1 + h / 2 + fz * 0.36, 'r', fz);
      labSub([['ΔU', '', dark(COL.dU)], [' + ', ''], ['W', 'k', dark(COL.Wk)]], BAR.x0 - 8, y2 + h / 2 + fz * 0.36, 'r', fz);
    }
    lab(done ? 'kierros' : 'lämmitys', BAR.x0, y2 + h + fz + 8, 'l', fz);
  }

  // every canvas text: drawn with a halo, its ink box pushed to simState.labels
  function lab(s, x, y, align, size) { labSub([[s, '']], x, y, align, size); }
  // text made of parts [main, subscript, colour?]; one box for the whole label
  function labSub(partsIn, x, y, align, size, col) {
    const sub = Math.round(size * 0.7), ctx = p.drawingContext;
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE);
    const m = partsIn.map(([a, b]) => { p.textSize(size); const wa = ctx.measureText(a); p.textSize(sub); const wb = b ? ctx.measureText(b) : { width: 0 };
      return { wa: wa.width, wb: wb.width, asc: wa.actualBoundingBoxAscent, desc: wa.actualBoundingBoxDescent }; });
    const total = m.reduce((s2, q) => s2 + q.wa + q.wb, 0);
    let lx = align === 'r' ? x - total : align === 'c' ? x - total / 2 : x;
    const x0 = lx, asc = Math.max(...m.map((q) => q.asc)), desc = Math.max(size * 0.3 * (partsIn.some((q) => q[1]) ? 1 : 0) + sub * 0.25, ...m.map((q) => q.desc));
    partsIn.forEach(([a, b, c], i) => {
      const cc = c || col || [35, 35, 35];
      for (const [txt, sz, dy, dx] of [[a, size, 0, 0], [b, sub, size * 0.3, m[i].wa]]) {
        if (!txt) continue; p.textSize(sz);
        p.stroke(255, 255, 255, 210); p.strokeWeight(3 * k); p.strokeJoin(p.ROUND); p.fill(...cc); p.text(txt, lx + dx, y + dy);
        p.noStroke(); p.text(txt, lx + dx, y + dy);
      }
      lx += m[i].wa + m[i].wb;
    });
    labels.push({ s: partsIn.map((q) => q[0] + q[1]).join(''), x0, y0: y - asc, x1: x0 + total, y1: y + desc });
  }
  // gradient fill (raw canvas, inside save/restore so p5's own fill state is untouched) with a thin outline
  function grect(x, y, w, h, stops, horiz, r = 4) {
    const c = p.drawingContext; c.save(); const g = c.createLinearGradient(x, y, horiz ? x + w : x, horiz ? y : y + h);
    stops.forEach((s, i) => g.addColorStop(i / (stops.length - 1), `rgb(${s.map((v) => Math.min(255, Math.round(v))).join(',')})`));
    c.fillStyle = g; c.strokeStyle = 'rgba(0,0,0,0.35)'; c.lineWidth = 1; c.beginPath(); c.roundRect(x, y, w, h, r); c.fill(); c.stroke(); c.restore();
  }
  const mix = (a, b, f) => a.map((v, i) => v + (b[i] - v) * f);
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');   // Finnish decimal comma and minus sign
});
