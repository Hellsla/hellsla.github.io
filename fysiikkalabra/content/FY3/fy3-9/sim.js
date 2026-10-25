// fy3-9 Kaasujen tilanmuutokset: a fixed amount of ideal gas in a cylinder with a piston.
// Physics: for a fixed amount of gas pV/T stays constant. The initial state is V₀ = 50 ml, p₀ = 100 kPa, T₀ = 293,15 K, so
//   isoterminen (T = T₀):  p = p₀V₀/V        → pV = p₀V₀ (Boylen laki), and p is proportional to 1/V
//   isobaarinen (p = p₀):  V = V₀ T/T₀       → V/T = V₀/T₀
//   isokoorinen (V = V₀):  p = p₀ T/T₀       → p/T = p₀/T₀
// The pressure comes from these formulas, not from counting hits. The micro model only illustrates them: 40 particles
// (start positions from a fixed seed) move with a speed ∝ √T, the mean speed of gas particles at the kelvin temperature T,
// and bounce off the walls and the moving piston. A smaller volume means more hits per second, a higher T faster hits.
// The chart axes start from zero, so a proportionality is a line through the origin. The readout and table are DOM text.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const V0 = 50, P0 = 100, T0 = 293.15, TC0 = 20, MAX_ROWS = 10, N = 40, SEED = 9;   // ml, kPa, K, °C
  const CYL = { l: 40, r: 140, bot: 330, top: 60, w: 6, px: 2.5 };     // gas region (px), wall, px per ml
  const GA = { x: 225, y: 250, r: 34, max: 300 };                       // pressure gauge, full scale 300 kPa
  const CH = { x0: 345, x1: 575, y0: 320, y1: 50 };                     // chart area (axes at x0 and y0)
  const AX = {                                                          // axis maximum, tick step, name
    isoterminen: { x: [100, 20, 'V (ml)'], y: [300, 50, 'p (kPa)'] },
    kaanteinen: { x: [0.05, 0.01, '1/V (1/ml)'], y: [300, 50, 'p (kPa)'] },
    isobaarinen: { x: [500, 100, 'T (K)'], y: [80, 20, 'V (ml)'] },
    isokoorinen: { x: [500, 100, 'T (K)'], y: [160, 40, 'p (kPa)'] } };
  const CONST = {                                                       // name, unit, value from (V ml, p kPa, T K), decimals
    isoterminen: ['pV', 'kPa·ml', (V, pp) => pp * V, 0],
    isobaarinen: ['V/T', 'ml/K', (V, pp, T) => V / T, 4],
    isokoorinen: ['p/T', 'kPa/K', (V, pp, T) => pp / T, 4] };
  let sel, sV, lV, sT, lT, chk, lChk, readout, table, mode = 'isoterminen', rows = [], parts = [], full = false;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  const button = (parent, text, fn) => { const b = p.createButton(text).parent(parent); b.elt.addEventListener('click', fn); return b; };
  // seeded PRNG (mulberry32), so the particles start the same way every time
  const mulberry32 = (a) => () => {
    a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const reset = () => {                                                 // back to the initial state, table cleared
    mode = sel.value(); rows = []; full = false;
    sV.value(V0); sT.value(TC0); chk.elt.checked = false;
    const rnd = mulberry32(SEED), yTop = CYL.bot - V0 * CYL.px;
    parts = Array.from({ length: N }, () => {
      const a = 2 * Math.PI * rnd();
      return { x: CYL.l + 5 + rnd() * (CYL.r - CYL.l - 10), y: yTop + 5 + rnd() * (CYL.bot - yTop - 10), dx: Math.cos(a), dy: Math.sin(a) };
    });
  };
  // current state from the mode and the slider (V in ml, p in kPa, T in K)
  const state = () => {
    if (mode === 'isoterminen') { const V = Number(sV.value()); return [V, P0 * V0 / V, T0]; }   // pV = p₀V₀
    const T = Number(sT.value()) + 273.15;
    if (mode === 'isobaarinen') return [V0 * T / T0, P0, T];             // V/T = V₀/T₀
    return [V0, P0 * T / T0, T];                                          // p/T = p₀/T₀
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    table = p.createDiv('').parent('sim-root').class('sim-table');
    const btns = p.createDiv('').parent(controls).style('display', 'flex').style('flex-wrap', 'wrap').style('gap', '.5rem');
    button(btns, 'Tallenna mittaus', () => {
      if (rows.length >= MAX_ROWS) { full = true; return; }
      const [V, pp, T] = state(); rows.push({ V: V * 1e-6, p: pp * 1000, T });   // SI units
    });
    button(btns, 'Tyhjennä', () => { rows = []; full = false; });
    const ls = p.createElement('label').parent(controls);
    p.createSpan('Tilanmuutos').parent(ls);
    sel = p.createSelect().parent(ls);
    sel.option('isoterminen (T vakio)', 'isoterminen'); sel.option('isobaarinen (p vakio)', 'isobaarinen');
    sel.option('isokoorinen (V vakio)', 'isokoorinen');
    sel.elt.addEventListener('change', reset);
    [sV, lV] = slider(controls, 20, 100, V0, 1);                          // tilavuus V (ml)
    [sT, lT] = slider(controls, -50, 150, TC0, 1);                        // lämpötila T (°C)
    lChk = p.createElement('label').parent(controls).style('flex-direction', 'row').style('align-items', 'center').style('gap', '.5rem').style('min-height', '40px');
    chk = p.createElement('input').attribute('type', 'checkbox').parent(lChk).style('width', '22px').style('height', '22px');
    p.createSpan('Piirrä p 1/V:n funktiona').parent(lChk);
    p.createP('Paine lasketaan yhtälöstä pV/T = vakio. Hiukkasten nopeus on verrannollinen √T:hen, kun T on kelvineinä. ' +
              'Kuvaajan ohut viiva on teoria, katkoviiva jatkaa suoraa origoon, pisteet ovat tallennetut mittaukset ja punainen piste on nykyinen tila.')
      .parent('sim-root').class('note');
    reset();
    p.textFont('Arial');
  };

  p.draw = () => {
    if (sel.value() !== mode) reset();                                    // mode changed without a change event
    const iso = mode === 'isoterminen', inv = iso && chk.elt.checked;
    lV.elt.parentElement.style.display = iso ? '' : 'none'; lT.elt.parentElement.style.display = iso ? 'none' : ''; lChk.elt.style.display = iso ? '' : 'none';
    const [V, pk, T] = state();
    const [cName, cUnit, cFn, cDec] = CONST[mode], c = cFn(V, pk, T);
    const ax = AX[inv ? 'kaanteinen' : mode];
    const speed = 120 * Math.sqrt(T / T0);                                // px/s, ∝ √T
    const dt = Math.min(p.deltaTime, 100) / 1000;
    const yP = CYL.bot - V * CYL.px;                                      // piston bottom
    for (const q of parts) {                                              // straight lines, elastic bounces
      q.x += q.dx * speed * dt; q.y += q.dy * speed * dt;
      if (q.x < CYL.l + 4) { q.x = CYL.l + 4; q.dx = Math.abs(q.dx); }
      if (q.x > CYL.r - 4) { q.x = CYL.r - 4; q.dx = -Math.abs(q.dx); }
      if (q.y > CYL.bot - 4) { q.y = CYL.bot - 4; q.dy = -Math.abs(q.dy); }
      if (q.y < yP + 4) { q.y = yP + 4; q.dy = Math.abs(q.dy); }
    }

    lV.html(`Tilavuus V = ${V} ml`);
    lT.html(`Lämpötila T = ${fi(T - 273.15, 0)} °C = ${fi(T, 2)} K`);
    const cText = iso ? `pV = ${fi(pk, 1)} kPa · ${fi(V, 1)} ml` : mode === 'isobaarinen' ? `V/T = ${fi(V, 1)} ml / ${fi(T, 2)} K` : `p/T = ${fi(pk, 1)} kPa / ${fi(T, 2)} K`;
    readout.html(`Tilanmuutos: <strong>${mode}</strong> (${iso ? 'lämpötila' : mode === 'isobaarinen' ? 'paine' : 'tilavuus'} on vakio)` +
                 `<br>Paine p = <strong>${fi(pk, 1)} kPa</strong>, tilavuus V = <strong>${fi(V, 1)} ml</strong>, ` +
                 `lämpötila T = ${fi(T - 273.15, 0)} °C = <strong>${fi(T, 2)} K</strong>` +
                 `<br>Vakio ${cText} = <strong>${fi(c, cDec)} ${cUnit}</strong>` +
                 `<br>Kuvaajan akselit: ${ax.x[2].split(' ')[0]} 0…${fi(ax.x[0], inv ? 2 : 0)} ${ax.x[2].split(' ')[1].slice(1, -1)}, ` +
                 `${ax.y[2].split(' ')[0]} 0…${ax.y[0]} ${ax.y[2].split(' ')[1].slice(1, -1)}. ` +
                 `Taulukossa ${rows.length}/${MAX_ROWS} mittausta${full ? ', taulukko on täynnä' : ''}.`);
    const td = '<td style="padding:.4rem .25rem">', th = '<th style="padding:.4rem .25rem;letter-spacing:0">';   // narrow cells, five columns fit a phone
    let h = `<table><thead><tr>${th}V<br>(ml)</th>${th}1/V<br>(1/ml)</th>${th}p<br>(kPa)</th>${th}T<br>(K)</th>${th}${cName}<br>(${cUnit})</th></tr></thead><tbody>`;
    for (const r of rows) {
      const Vm = r.V * 1e6, pr = r.p / 1000;
      h += `<tr>${td}${fi(Vm, 1)}</td>${td}${fs(1 / Vm)}</td>${td}${fi(pr, 1)}</td>${td}${fi(r.T, 2)}</td>${td}${fi(cFn(Vm, pr, r.T), cDec)}</td></tr>`;
    }
    if (!rows.length) h += '<tr><td colspan="5" style="padding:.4rem .25rem">Ei mittauksia. Paina ”Tallenna mittaus”.</td></tr>';
    h += '</tbody></table>';
    if (table.elt.innerHTML !== h) table.elt.innerHTML = h;
    window.simState = { mode, V: V * 1e-6, p: pk * 1000, T, constant: c * (iso ? 1e-3 : mode === 'isobaarinen' ? 1e-6 : 1e3),
                        rows: rows.map((r) => ({ ...r })), plotInv: inv, speed, nParticles: parts.length,
                        inside: parts.every((q) => q.x >= CYL.l && q.x <= CYL.r && q.y >= yP && q.y <= CYL.bot) ? 1 : 0,
                        xMax: ax.x[0], yMax: ax.y[0] };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);
    const col = tempColor(T);

    // cylinder, gas and piston (rod to the top edge)
    p.noStroke(); p.fill(col.levels[0], col.levels[1], col.levels[2], 40); p.rect(CYL.l, yP, CYL.r - CYL.l, CYL.bot - yP);
    p.fill(120); p.rect(CYL.l - CYL.w, CYL.top, CYL.w, CYL.bot - CYL.top + CYL.w); p.rect(CYL.r, CYL.top, CYL.w, CYL.bot - CYL.top + CYL.w);
    p.rect(CYL.l - CYL.w, CYL.bot, CYL.r - CYL.l + 2 * CYL.w, CYL.w);
    p.fill(80); p.rect(CYL.l + 1, yP - 14, CYL.r - CYL.l - 2, 14, 2); p.rect((CYL.l + CYL.r) / 2 - 4, 14, 8, yP - 28);
    p.rect((CYL.l + CYL.r) / 2 - 22, 8, 44, 8, 3);
    p.fill(col); p.stroke(255); p.strokeWeight(1);
    for (const q of parts) p.circle(q.x, q.y, 8);

    // pressure gauge on a pipe from the bottom of the cylinder, needle 0…300 kPa over 270°
    p.stroke(120); p.strokeWeight(5); p.noFill(); p.line(CYL.r + CYL.w, CYL.bot - 12, GA.x, CYL.bot - 12); p.line(GA.x, CYL.bot - 12, GA.x, GA.y + GA.r);
    p.stroke(60); p.strokeWeight(2); p.fill(255); p.circle(GA.x, GA.y, 2 * GA.r);
    for (let v = 0; v <= GA.max; v += 50) {
      const a = p.radians(135 + 270 * v / GA.max);
      p.line(GA.x + (GA.r - 8) * Math.cos(a), GA.y + (GA.r - 8) * Math.sin(a), GA.x + (GA.r - 2) * Math.cos(a), GA.y + (GA.r - 2) * Math.sin(a));
    }
    const an = p.radians(135 + 270 * Math.min(pk, GA.max) / GA.max);
    p.stroke(200, 50, 40); p.strokeWeight(3); p.line(GA.x, GA.y, GA.x + (GA.r - 9) * Math.cos(an), GA.y + (GA.r - 9) * Math.sin(an));
    p.noStroke(); p.fill(40); p.circle(GA.x, GA.y, 7);
    p.textAlign(p.CENTER); p.textSize(ts(13)); p.text(`${fi(pk, 1)} kPa`, GA.x, GA.y - GA.r - 8);
    p.text(`V = ${fi(V, 1)} ml`, (CYL.l + CYL.r) / 2, CYL.bot + 4 + ts(13));
    p.fill(col); p.text(`T = ${fi(T, 0)} K`, GA.x, 40 + ts(13));

    // chart from zero: grid, axes, tick labels (every second one on a narrow screen)
    const X = (v) => CH.x0 + (CH.x1 - CH.x0) * v / ax.x[0], Y = (v) => CH.y0 - (CH.y0 - CH.y1) * v / ax.y[0];
    const nx = Math.round(ax.x[0] / ax.x[1]), ny = Math.round(ax.y[0] / ax.y[1]), every = k > 1.5 ? 2 : 1;
    p.stroke(225); p.strokeWeight(1);
    for (let i = 1; i <= nx; i++) p.line(X(i * ax.x[1]), CH.y0, X(i * ax.x[1]), CH.y1);
    for (let j = 1; j <= ny; j++) p.line(CH.x0, Y(j * ax.y[1]), CH.x1, Y(j * ax.y[1]));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1 + 5, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    p.noStroke(); p.fill(60); p.textSize(ts(11)); p.textAlign(p.RIGHT);
    for (let j = 0; j <= ny; j += every) p.text(`${j * ax.y[1]}`, CH.x0 - 6, Y(j * ax.y[1]) + ts(4));
    p.textAlign(p.CENTER);
    for (let i = every; i <= nx; i += every) p.text(fi(i * ax.x[1], inv ? 2 : 0), X(i * ax.x[1]), CH.y0 + ts(16));
    p.textSize(ts(12)); p.textAlign(p.RIGHT); p.text(ax.x[2], CH.x1, CH.y0 - 8);   // lower right of the plot is always empty
    p.textAlign(p.LEFT); p.text(ax.y[2], CH.x0 + 6, CH.y1 - 10);

    // theory: the state along the whole slider range; a dashed line continues a proportionality to the origin
    const pt = (Vm, pp, TT) => inv ? [X(1 / Vm), Y(pp)] : iso ? [X(Vm), Y(pp)] : [X(TT), Y(mode === 'isobaarinen' ? Vm : pp)];
    const curve = [];
    for (let i = 0; i <= 80; i++) {
      if (iso) { const Vm = 20 + i; curve.push(pt(Vm, P0 * V0 / Vm, T0)); }
      else { const TT = 223.15 + 2.5 * i; curve.push(pt(mode === 'isobaarinen' ? V0 * TT / T0 : V0, mode === 'isobaarinen' ? P0 : P0 * TT / T0, TT)); }
    }
    p.noFill(); p.stroke(60, 90, 150); p.strokeWeight(1.5);
    p.beginShape(); for (const [x, y] of curve) p.vertex(x, y); p.endShape();
    if (!iso || inv) {
      const e = inv ? curve[curve.length - 1] : curve[0];                // end nearest the origin
      p.drawingContext.setLineDash([5, 5]); p.line(CH.x0, CH.y0, e[0], e[1]); p.drawingContext.setLineDash([]);
    }
    p.noStroke(); p.fill(60, 90, 150);
    for (const r of rows) { const [x, y] = pt(r.V * 1e6, r.p / 1000, r.T); p.circle(x, y, 9); }
    const [cx, cy] = pt(V, pk, T);
    p.stroke(255); p.strokeWeight(2); p.fill(200, 50, 40); p.circle(cx, cy, 13);
  };

  // −50 °C blue, 150 °C red
  function tempColor(T) { return p.lerpColor(p.color(40, 100, 210), p.color(215, 50, 40), (T - 223.15) / 200); }
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                   // Finnish decimal comma and minus sign
  const fs = (x) => x.toPrecision(3).replace('.', ',');                                      // three significant figures
});
