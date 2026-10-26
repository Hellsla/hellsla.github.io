// fy3-9 Kaasujen tilanmuutokset: a fixed amount of ideal gas in a cylinder with a piston.
// Physics: for a fixed amount of gas pV/T stays constant. The initial state is V₀ = 50 ml, p₀ = 100 kPa, T₀ = 293,15 K, so
//   isoterminen (T = T₀):  p = p₀V₀/V        → pV = p₀V₀ (Boylen laki), and p is proportional to 1/V
//   isobaarinen (p = p₀):  V = V₀ T/T₀       → V/T = V₀/T₀   (a weight on a free piston keeps p constant)
//   isokoorinen (V = V₀):  p = p₀ T/T₀       → p/T = p₀/T₀   (the piston is locked)
// The pressure comes from these formulas, not from counting hits. The micro model only illustrates them: 40 particles
// (start positions from a fixed seed) move with a speed ∝ √T, the mean speed of gas particles at the kelvin temperature T,
// and bounce off the walls and the moving piston; every bounce flashes. The flash rate per wall length is ∝ √T/V and the
// flash size ∝ speed, so "how often × how hard" grows with p = (const)·T/V in every mode.
// The chart axes start from zero, so a proportionality is a line through the origin. The readout and table are DOM text.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const V0 = 50, P0 = 100, T0 = 293.15, TC0 = 20, MAX_ROWS = 10, N = 40, SEED = 9;   // ml, kPa, K, °C
  const CYL = { l: 24, r: 124, bot: 330, top: 60, w: 8, px: 2.5 };      // gas region (px), wall, px per ml
  const GA = { x: 215, y: 318, r: 46, max: 300 };                       // pressure gauge, full scale 300 kPa
  const TH = { x: 270, y0: 192, y1: 72 };                               // thermometer: −50 °C at y0, 150 °C at y1
  const CH = { x0: 345, x1: 575, y0: 320, y1: 50 };                     // chart area (axes at x0 and y0)
  const AX = {                                                          // axis maximum, tick step, name
    isoterminen: { x: [100, 20, 'V (ml)'], y: [300, 50, 'p (kPa)'] }, kaanteinen: { x: [0.05, 0.01, '1/V (1/ml)'], y: [300, 50, 'p (kPa)'] },
    isobaarinen: { x: [500, 100, 'T (K)'], y: [80, 20, 'V (ml)'] }, isokoorinen: { x: [500, 100, 'T (K)'], y: [160, 40, 'p (kPa)'] } };
  const CONST = { isoterminen: ['pV', 'kPa·ml', (V, pp) => pp * V, 0],   // name, unit, value from (V ml, p kPa, T K), decimals
    isobaarinen: ['V/T', 'ml/K', (V, pp, T) => V / T, 4], isokoorinen: ['p/T', 'kPa/K', (V, pp, T) => pp / T, 4] };
  const COLD = [40, 105, 215], ROOM = [150, 140, 180], HOT = [240, 120, 25];   // −50 °C, 20 °C, 150 °C
  let sel, sV, lV, sT, lT, chk, lChk, readout, table, mode = 'isoterminen', rows = [], parts = [], flashes = [], hits = 0, full = false;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent), span = p.createSpan('').parent(label);
    return [p.createSlider(min, max, val, step).parent(label), span];
  };
  const button = (parent, text, fn) => { const b = p.createButton(text).parent(parent); b.elt.addEventListener('click', fn); return b; };
  // seeded PRNG (mulberry32), so the particles start the same way every time
  const mulberry32 = (a) => () => {
    a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const reset = () => {                                                 // back to the initial state, table cleared
    mode = sel.value(); rows = []; full = false; flashes = [];
    sV.value(V0); sT.value(TC0); chk.elt.checked = false;
    const rnd = mulberry32(SEED), yTop = CYL.bot - V0 * CYL.px;
    parts = Array.from({ length: N }, (_, a) => (a = 2 * Math.PI * rnd(),
      { x: CYL.l + 5 + rnd() * (CYL.r - CYL.l - 10), y: yTop + 5 + rnd() * (CYL.bot - yTop - 10), dx: Math.cos(a), dy: Math.sin(a) }));
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
    p.createP('Paine lasketaan yhtälöstä pV/T = vakio. Hiukkasten nopeus on verrannollinen √T:hen, kun T on kelvineinä. ' +
              'Kaasun väri kertoo lämpötilan (sininen kylmä, oranssi lämmin; väriasteikko on lämpömittarin vieressä). ' +
              'Välähdykset ovat hiukkasten törmäyksiä seiniin: mitä tiheämmin ja kovemmin ne osuvat, sitä suurempi paine on. ' +
              'Isobaarisessa muutoksessa punnus pitää paineen vakiona, isokoorisessa mäntä on lukittu. ' +
              'Kuvaajan haalea viiva on teoria, katkoviiva jatkaa suoraa origoon, siniset pisteet ovat tallennetut mittaukset ja punainen piste on nykyinen tila.')
      .parent('sim-root').class('note');
    table = p.createDiv('').parent('sim-root').class('sim-table');
    const btns = p.createDiv('').parent(controls).style('display', 'flex').style('flex-wrap', 'wrap').style('gap', '.5rem');
    button(btns, 'Tallenna mittaus', () => {
      if (rows.length >= MAX_ROWS) { full = true; return; }
      const [V, pp, T] = state(); rows.push({ V: V * 1e-6, p: pp * 1000, T });   // SI units
    });
    button(btns, 'Tyhjennä', () => { rows = []; full = false; });
    const ls = p.createElement('label').parent(controls);
    p.createSpan('Tilanmuutos').parent(ls); sel = p.createSelect().parent(ls);
    sel.option('isoterminen (T vakio)', 'isoterminen'); sel.option('isobaarinen (p vakio)', 'isobaarinen');
    sel.option('isokoorinen (V vakio)', 'isokoorinen'); sel.elt.addEventListener('change', reset);
    [sV, lV] = slider(controls, 20, 100, V0, 1);                          // tilavuus V (ml)
    [sT, lT] = slider(controls, -50, 150, TC0, 1);                        // lämpötila T (°C)
    lChk = p.createElement('label').parent(controls).style('flex-direction', 'row').style('align-items', 'center').style('gap', '.5rem').style('min-height', '40px');
    chk = p.createElement('input').attribute('type', 'checkbox').parent(lChk).style('width', '22px').style('height', '22px');
    p.createSpan('Piirrä p 1/V:n funktiona').parent(lChk);
    reset(); p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { mode: { input: sel.elt, unit: '' }, Vml: { input: sV.elt, unit: 'ml' }, Tc: { input: sT.elt, unit: '°C' } },
      get: () => ({ ...window.simState, Vml: Number(sV.value()), Tc: Number(sT.value()),   // slider readings beside the SI values of simState
                     Vgas: window.simState.V * 1e6, VperT: window.simState.V * 1e6 / window.simState.T }),   // gas volume (ml) and V/T (ml/K) for the tables
      reset: () => { sel.selected('isoterminen'); reset(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    if (sel.value() !== mode) reset();                                    // mode changed without a change event
    const iso = mode === 'isoterminen', inv = iso && chk.elt.checked;
    lV.elt.parentElement.style.display = iso ? '' : 'none'; lT.elt.parentElement.style.display = iso ? 'none' : ''; lChk.elt.style.display = iso ? '' : 'none';
    const [V, pk, T] = state();
    const [cName, cUnit, cFn, cDec] = CONST[mode], c = cFn(V, pk, T);
    const ax = AX[inv ? 'kaanteinen' : mode], dt = Math.min(p.deltaTime, 100) / 1000;
    const speed = 120 * Math.sqrt(T / T0);                                // px/s, ∝ √T
    const yP = CYL.bot - V * CYL.px;                                      // piston bottom
    const needle = Math.min(pk, GA.max);                                  // gauge needle value (kPa), full scale 300 kPa
    const hit = (x, y) => { hits++; if (flashes.length < 80) flashes.push({ x, y, age: 0 }); };
    for (const q of parts) {                                              // straight lines, elastic bounces
      q.x += q.dx * speed * dt; q.y += q.dy * speed * dt;
      if (q.x < CYL.l + 4) { q.x = CYL.l + 4; if (q.dx < 0) hit(CYL.l, q.y); q.dx = Math.abs(q.dx); }
      if (q.x > CYL.r - 4) { q.x = CYL.r - 4; if (q.dx > 0) hit(CYL.r, q.y); q.dx = -Math.abs(q.dx); }
      if (q.y > CYL.bot - 4) { q.y = CYL.bot - 4; if (q.dy > 0) hit(q.x, CYL.bot); q.dy = -Math.abs(q.dy); }
      if (q.y < yP + 4) { q.y = yP + 4; if (q.dy < 0) hit(q.x, yP); q.dy = Math.abs(q.dy); }
    }
    flashes = flashes.filter((f) => (f.age += dt) < 0.25);

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
    for (const r of rows) { const Vm = r.V * 1e6, pr = r.p / 1000;
      h += `<tr>${td}${fi(Vm, 1)}</td>${td}${fs(1 / Vm)}</td>${td}${fi(pr, 1)}</td>${td}${fi(r.T, 2)}</td>${td}${fi(cFn(Vm, pr, r.T), cDec)}</td></tr>`; }
    if (!rows.length) h += '<tr><td colspan="5" style="padding:.4rem .25rem">Ei mittauksia. Paina ”Tallenna mittaus”.</td></tr>';
    h += '</tbody></table>'; if (table.elt.innerHTML !== h) table.elt.innerHTML = h;
    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k), labels = [];
    const lab = (s, x, y, align) => {                                     // draw a text label and remember its box for the sweep
      p.textAlign(align); p.text(s, x, y);
      const w = p.textWidth(s), x0 = align === p.RIGHT ? x - w : align === p.CENTER ? x - w / 2 : x;
      labels.push({ s, x0, y0: y - p.textAscent(), x1: x0 + w, y1: y + p.textDescent() });
    };
    const col = tempRGB(T), mid = (CYL.l + CYL.r) / 2, piece = iso ? 'kahva' : mode === 'isobaarinen' ? 'punnus' : 'lukittu';
    p.background(250);
    // gas: tinted by temperature, slightly denser colour at the bottom
    paint(grad(0, yP, 0, CYL.bot, [[0, rgba(col, 0.18)], [1, rgba(col, 0.38)]]), (g) => g.rect(CYL.l, yP, CYL.r - CYL.l, CYL.bot - yP));
    // particles: a motion trail (length ∝ speed, kept inside the gas), then a small shaded sphere
    const L = speed * 0.09, cx = (x) => Math.min(CYL.r - 2, Math.max(CYL.l + 2, x)), cy = (y) => Math.min(CYL.bot - 2, Math.max(yP + 2, y));
    for (const q of parts) for (let j = 0; j < 3; j++) {
      p.stroke(col[0], col[1], col[2], 110 - 35 * j); p.strokeWeight(5 - 1.3 * j);
      p.line(cx(q.x - q.dx * L * j / 3), cy(q.y - q.dy * L * j / 3), cx(q.x - q.dx * L * (j + 1) / 3), cy(q.y - q.dy * L * (j + 1) / 3));
    }
    p.noStroke();
    for (const q of parts) { p.fill(col[0] * 0.55, col[1] * 0.55, col[2] * 0.55); p.circle(q.x, q.y, 9);
      p.fill(col[0], col[1], col[2]); p.circle(q.x - 0.7, q.y - 0.7, 7); p.fill(255, 255, 255, 200); p.circle(q.x - 1.8, q.y - 1.8, 2.8); }
    // metal cylinder (cut open): shaded walls and bottom with a highlight stripe
    for (const x of [CYL.l - CYL.w, CYL.r]) paint(metal(x, 0, x + CYL.w, 0), (g) => g.rect(x, CYL.top, CYL.w, CYL.bot - CYL.top + CYL.w));
    paint(grad(0, CYL.bot, 0, CYL.bot + CYL.w, [[0, '#c9ced4'], [1, '#5f656c']]), (g) => g.rect(CYL.l - CYL.w, CYL.bot, CYL.r - CYL.l + 2 * CYL.w, CYL.w));
    // piston with seal rings; isoterminen: rod and handle, isobaarinen: a weight, isokoorinen: locking pins
    paint(grad(0, yP - 14, 0, yP, [[0, '#9aa1a8'], [0.4, '#e2e5e9'], [1, '#6a7078']]), (g) => g.rect(CYL.l, yP - 14, CYL.r - CYL.l, 14));
    p.fill(40, 44, 50); p.rect(CYL.l, yP - 10, CYL.r - CYL.l, 2); p.rect(CYL.l, yP - 5, CYL.r - CYL.l, 2);
    if (piece === 'kahva') {
      paint(metal(mid - 4, 0, mid + 4, 0), (g) => g.rect(mid - 4, 16, 8, yP - 30));
      paint(grad(0, 6, 0, 18, [[0, '#4a4f56'], [0.4, '#8b929a'], [1, '#33373c']]), (g) => g.roundRect(mid - 26, 6, 52, 11, 5));
    } else if (piece === 'punnus') {
      paint(grad(mid - 40, 0, mid + 40, 0, [[0, '#3a3e44'], [0.3, '#7c838b'], [1, '#2c3035']]), (g) => g.roundRect(mid - 40, yP - 50, 80, 36, 4));
      p.fill(70, 75, 82); p.rect(mid - 8, yP - 58, 16, 9, 3);
      p.textSize(ts(10)); p.fill(255); lab('punnus', mid, yP - 27, p.CENTER);
    } else for (const x of [CYL.l - CYL.w - 10, CYL.r - 8]) {          // pins through both walls lock the piston
      paint(metal(0, yP - 27, 0, yP - 17), (g) => g.roundRect(x, yP - 27, 26, 10, 2)); p.fill(30); p.circle(x + (x < mid ? 5 : 21), yP - 22, 5);
    }
    for (const f of flashes) { const a = 1 - f.age / 0.25; p.fill(255, 245, 190, 230 * a); p.circle(f.x, f.y, (6 + 6 * (1 - a)) * speed / 120); }   // wall hits, size ∝ speed
    if (!iso) {                                                           // heater / cooler plate under the cylinder
      const g = p.drawingContext; g.shadowColor = rgba(col, 0.9); g.shadowBlur = 6 + 14 * Math.abs(T - T0) / 130;
      paint(grad(0, CYL.bot + 9, 0, CYL.bot + 17, [[0, rgba(col, 1)], [1, rgba(col.map((v) => v * 0.6), 1)]]), (gg) => gg.roundRect(CYL.l - 10, CYL.bot + 9, CYL.r - CYL.l + 20, 8, 3));
      g.shadowBlur = 0;
    }
    // pressure gauge on a pipe from the bottom of the gas, needle 0…300 kPa over 270°
    paint(metal(0, CYL.bot - 16, 0, CYL.bot - 8), (g) => g.rect(CYL.r + CYL.w, CYL.bot - 16, GA.x - GA.r - CYL.r, 8));
    paint(grad(GA.x - GA.r, GA.y - GA.r, GA.x + GA.r, GA.y + GA.r, [[0, '#eef0f2'], [0.5, '#8d949c'], [1, '#41464c']]), (g) => g.arc(GA.x, GA.y, GA.r, 0, 7));
    paint(grad(GA.x, GA.y - GA.r, GA.x, GA.y + GA.r, [[0, '#ffffff'], [1, '#dfe3e7']]), (g) => g.arc(GA.x, GA.y, GA.r - 5, 0, 7));
    const ang = (v) => p.radians(135 + 270 * v / GA.max), rim = GA.r - 7, ray = (v, r0, r1) => p.line(GA.x + r0 * Math.cos(ang(v)), GA.y + r0 * Math.sin(ang(v)), GA.x + r1 * Math.cos(ang(v)), GA.y + r1 * Math.sin(ang(v)));
    p.stroke(60);
    for (let v = 0; v <= GA.max; v += 10) { p.strokeWeight(v % 50 ? 1 : 2); ray(v, rim - (v % 50 ? 4 : 8), rim); }
    p.noStroke(); p.fill(50); p.textSize(ts(9));
    for (const v of k > 1.5 ? [] : [0, 100, 200, 300]) lab(`${v}`, GA.x + 22 * Math.cos(ang(v)), GA.y + 22 * Math.sin(ang(v)) + ts(3), p.CENTER);
    lab('kPa', GA.x, GA.y + (k > 1.5 ? -14 : 41), p.CENTER);   // below the hub when 100 and 200 are printed; 41 keeps a 5 px gap to "0" and "300" in wider fonts
    p.stroke(200, 50, 40); p.strokeWeight(3); ray(needle, -6, rim - 6);  // needle
    p.noStroke(); p.fill(40); p.circle(GA.x, GA.y, 8); p.fill(255, 255, 255, 120); p.circle(GA.x - 1, GA.y - 1, 3);
    // thermometer: glass tube, liquid up to T, a colour strip that is the legend of the gas colour, scale in °C
    const yT = (tc) => TH.y0 - (TH.y0 - TH.y1) * (tc + 50) / 200;
    p.stroke(150); p.strokeWeight(1); p.fill(255); p.rect(TH.x - 5, TH.y1 - 10, 10, TH.y0 - TH.y1 + 16, 5); p.circle(TH.x, TH.y0 + 13, 20);
    p.noStroke(); p.fill(col[0], col[1], col[2]); p.circle(TH.x, TH.y0 + 13, 14); p.rect(TH.x - 2.5, yT(T - 273.15), 5, TH.y0 + 13 - yT(T - 273.15));
    p.fill(255, 255, 255, 170); p.circle(TH.x - 3, TH.y0 + 10, 4);
    paint(grad(0, TH.y0, 0, TH.y1, [[0, rgba(COLD, 1)], [0.35, rgba(ROOM, 1)], [1, rgba(HOT, 1)]]), (g) => g.rect(TH.x + 8, TH.y1, 6, TH.y0 - TH.y1));
    p.stroke(90); p.strokeWeight(1);
    for (let tc = -50; tc <= 150; tc += 25) p.line(TH.x - 9, yT(tc), TH.x - (tc % 50 ? 6 : 3), yT(tc));
    p.noStroke(); p.fill(60); p.textSize(ts(9));
    for (let tc = -50; tc <= 150; tc += k > 1.5 ? 100 : 50) lab(`${fi(tc, 0)} °C`, TH.x - 12, yT(tc) + ts(3), p.RIGHT);

    p.fill(40); p.textSize(ts(13));
    lab(`${fi(pk, 1)} kPa`, GA.x, GA.y - GA.r - 8, p.CENTER); const vs = `V = ${fi(V, 1)} ml`;
    lab(vs, Math.max(mid, p.textWidth(vs) / 2 + 3), CYL.bot + 22 + ts(13), p.CENTER);   // kept inside the left edge on a phone
    p.fill(col[0] * 0.8, col[1] * 0.8, col[2] * 0.8); lab(`T = ${fi(T, 0)} K`, 222, 20 + ts(13), p.CENTER);
    // chart from zero: panel, grid, axes with arrows, tick labels (every second one on a narrow screen)
    const X = (v) => CH.x0 + (CH.x1 - CH.x0) * v / ax.x[0], Y = (v) => CH.y0 - (CH.y0 - CH.y1) * v / ax.y[0];
    const nx = Math.round(ax.x[0] / ax.x[1]), ny = Math.round(ax.y[0] / ax.y[1]), every = k > 1.5 ? 2 : 1;
    p.noStroke(); p.fill(255); p.rect(CH.x0, CH.y1, CH.x1 - CH.x0, CH.y0 - CH.y1);
    p.strokeWeight(1);                                                    // minor (half-step) and major gridlines
    for (let i = 1; i <= 2 * nx; i++) { p.stroke(i % 2 ? 240 : 215); p.line(X(i * ax.x[1] / 2), CH.y0, X(i * ax.x[1] / 2), CH.y1); }
    for (let j = 1; j <= 2 * ny; j++) { p.stroke(j % 2 ? 240 : 215); p.line(CH.x0, Y(j * ax.y[1] / 2), CH.x1, Y(j * ax.y[1] / 2)); }
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1 + 8, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 8);
    p.noStroke(); p.fill(60); p.triangle(CH.x1 + 14, CH.y0, CH.x1 + 6, CH.y0 - 4, CH.x1 + 6, CH.y0 + 4); p.triangle(CH.x0, CH.y1 - 14, CH.x0 - 4, CH.y1 - 6, CH.x0 + 4, CH.y1 - 6);
    p.textSize(ts(11));
    for (let j = 0; j <= ny; j += every) lab(`${j * ax.y[1]}`, CH.x0 - 6, Y(j * ax.y[1]) + ts(4), p.RIGHT);
    for (let i = every; i <= nx; i += every) lab(fi(i * ax.x[1], inv ? 2 : 0), X(i * ax.x[1]), CH.y0 + ts(16), p.CENTER);
    p.textSize(ts(12)); lab(ax.x[2], CH.x1, CH.y0 - 8, p.RIGHT); lab(ax.y[2], CH.x0 + 10, CH.y1 - 10, p.LEFT);   // lower right of the plot is always empty
    // theory (faint): the state along the whole slider range; a dashed line continues a proportionality to the origin
    const pt = (Vm, pp, TT) => inv ? [X(1 / Vm), Y(pp)] : iso ? [X(Vm), Y(pp)] : [X(TT), Y(mode === 'isobaarinen' ? Vm : pp)];
    const curve = Array.from({ length: 81 }, (_, i) => { const Vm = 20 + i, TT = 223.15 + 2.5 * i;
      return iso ? pt(Vm, P0 * V0 / Vm, T0) : pt(mode === 'isobaarinen' ? V0 * TT / T0 : V0, mode === 'isobaarinen' ? P0 : P0 * TT / T0, TT); });
    p.noFill(); p.stroke(60, 90, 150, 110); p.strokeWeight(2.5);
    p.beginShape(); for (const [x, y] of curve) p.vertex(x, y); p.endShape();
    if (!iso || inv) {
      const e = inv ? curve[curve.length - 1] : curve[0];                // end nearest the origin
      p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 5]); p.line(CH.x0, CH.y0, e[0], e[1]); p.drawingContext.setLineDash([]);
    }
    p.stroke(255); p.strokeWeight(1.5); p.fill(60, 90, 150);
    for (const r of rows) { const [x, y] = pt(r.V * 1e6, r.p / 1000, r.T); p.circle(x, y, 10); }
    const [qx, qy] = pt(V, pk, T);                                        // current state: guides to both axes and a halo
    p.stroke(200, 50, 40, 120); p.strokeWeight(1); p.drawingContext.setLineDash([3, 4]);
    p.line(qx, qy, qx, CH.y0); p.line(qx, qy, CH.x0, qy); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(200, 50, 40, 45); p.circle(qx, qy, 28);
    p.stroke(255); p.strokeWeight(2); p.fill(200, 50, 40); p.circle(qx, qy, 13);
    window.simState = { mode, V: V * 1e-6, p: pk * 1000, T, constant: c * (iso ? 1e-3 : mode === 'isobaarinen' ? 1e-6 : 1e3),
                        rows: rows.map((r) => ({ ...r })), plotInv: inv, speed, nParticles: parts.length,
                        inside: parts.every((q) => q.x >= CYL.l && q.x <= CYL.r && q.y >= yP && q.y <= CYL.bot) ? 1 : 0,
                        xMax: ax.x[0], yMax: ax.y[0], pistonY: yP, needleKPa: needle,
                        gasRGB: col, piece, hits, flashes: flashes.length, thermoY: yT(T - 273.15), labels, k };
  };

  // gas colour: −50 °C blue, 20 °C (room) greyish violet, 150 °C orange
  const tempRGB = (T) => { const u = Math.min(1, Math.max(0, (T - 223.15) / 200)), [a, b, f] = u < 0.35 ? [COLD, ROOM, u / 0.35] : [ROOM, HOT, (u - 0.35) / 0.65];
    return a.map((v, i) => Math.round(v + (b[i] - v) * f)); };
  const rgba = (c, a) => `rgba(${c.map(Math.round).join(',')},${a})`;
  const grad = (x0, y0, x1, y1, stops) => { const g = p.drawingContext.createLinearGradient(x0, y0, x1, y1); for (const [o, s] of stops) g.addColorStop(o, s); return g; };
  const metal = (x0, y0, x1, y1) => grad(x0, y0, x1, y1, [[0, '#5f656c'], [0.3, '#dde1e5'], [0.55, '#a9afb6'], [1, '#575d64']]);   // shaded metal bar
  // fill a path with a canvas gradient, then give p5 its own fill style back (p5 caches it)
  const paint = (style, path) => { const g = p.drawingContext, prev = g.fillStyle; g.fillStyle = style; g.beginPath(); path(g); g.fill(); g.fillStyle = prev; };
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                   // Finnish decimal comma and minus sign
  const fs = (x) => x.toPrecision(3).replace('.', ',');                                      // three significant figures
});
