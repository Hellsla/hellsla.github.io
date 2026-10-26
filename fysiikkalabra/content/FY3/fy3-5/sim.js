// fy3-5 Sisäenergia, lämpömäärä ja energian säilyminen: a piston pushed into a gas, and walls that insulate or conduct.
// Physics: N = 40 point particles (mass m = 1) move in a 2D cylinder of length X (the piston position) and height LY and do
// not collide with each other (ideal gas). The piston is a moving wall with velocity w along x (w = −u while pushed in,
// +u while pulled out, 0 at rest). A particle that hits it reflects elastically in the piston's frame: vx' = 2w − vx
// ("kuin pallo mailasta"). Its kinetic energy changes by ½(vx'² − vx²) = (impulse on the piston) · (piston displacement
// per unit time), so the sum of these changes is exactly the work W the piston does on the gas (force × distance).
// The fixed walls (cylinder bottom, top and bottom) reflect specularly. Eristetty: the speed is unchanged, Q = 0.
// Johtava: the wall is at room temperature T0; a particle leaving it has its speed scaled by √(T0/T), where T is the gas
// temperature at that step, so a hot gas loses energy at every wall hit and a cold one gains it (Newton-like cooling,
// no noise). That energy change is the heat Q into the gas (negative when leaving).
// Temperature: T = T0 · E/E0, where E is the total kinetic energy and E0 = N·kT0 the initial one (the seeded speeds are
// rescaled so that Σvx² = Σvy² = N·kT0 exactly). Scale: the model gas has the heat capacity of 0,50 g of air, whose
// internal energy grows 0,50 g · 718 J/(kg·K) = 0,359 J per kelvin, so ΔU = C·(T − T0) and one model energy unit is
// C·T0/E0 joules. W and Q are summed in the same unit, so ΔU = Q + W holds to rounding error: bookkeeping, not a fit.
// Pressure (shown as p/p0) is the kinetic one averaged over both directions, p ∝ E/A, relative to the start; the
// pressure on the piston itself (x direction only) is higher after an insulated push (Lisätietoja says so).
// Piston speeds: hidas 4 px/s (≈ 1/50 of the mean particle speed 213 px/s, nearly the adiabatic limit T → 407 K),
// nopea 60 px/s (≈ 1/3,5): the particles meet the advancing piston at a higher relative speed, the gas pushes back
// harder, and the same stroke takes more work (47,2 J against 40,8 J); ΔT = W/C in both, since Q = 0.
// A push from the untouched initial state (V = 100 %, W = Q = 0) first re-seeds the gas, so every such push gives the
// same numbers whenever it is started. Fixed physics step 1/240 s, seeded PRNG (mulberry32): frame-rate independent.
// Picture: particle colour = speed; a particle that has just hit the moving piston gets a long bright trail and a green
// halo (the speed-up); wall hits on a conducting wall flash red; red arrows through the walls = heat Q, green arrow on the
// rod = work W, and the three bars Q, W, ΔU share one energy axis. Canvas text only labels and values, via lab().
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame, and as test hooks
// window.simAdvance(s), window.simRestart() and window.simMove(dir) (dir −1 push, +1 pull).
new p5((p) => {
  const DT = 1 / 240, N = 40, SEED = 306, T0 = 293.15, C = 0.359;    // step (s), particles, seed, room T (K), J/K of 0,50 g air
  const L0 = 300, LY = 220, XEND = 225, R = 3;                       // full gas length, height, pushed-in length (px), radius
  const BOX = { x: 34, y: 80 }, WT = 8, INS = 12, PW = 10;           // gas region corner, steel wall, insulation, piston
  const VRMS = 240, KT = VRMS * VRMS / 2, E0 = N * KT, FJ = C * T0 / E0;   // v_rms at T0 (px/s), kT/m, E0, J per unit
  const U = { hidas: 4, nopea: 60 };                                 // piston speed (px/s)
  const BAR = { ax: 432, x: [462, 516, 570], w: 32, y0: 72, y1: 318 };   // energy axis, bar centres, bar area
  const COL_W = [40, 150, 80], COL_Q = [205, 45, 60], COL_U = [125, 70, 190];
  const SLOW = [60, 130, 255], MID = [245, 215, 80], FAST = [255, 120, 30], VMAX = 480;
  const TAIL = 0.05, BOOST = 0.35, HN = 128, FL = 36;                // trail (s), speed-up shown (s), flashes, flash life (steps)
  const mix = (a, b, f) => a.map((x, i) => Math.round(x + (b[i] - x) * f));
  const PAL = Array.from({ length: 32 }, (_, i) => i < 16 ? mix(SLOW, MID, i / 15.5) : mix(MID, FAST, (i - 16) / 15));
  const fx = new Float32Array(HN), fy = new Float32Array(HN), fk = new Int8Array(HN), fn = new Int32Array(HN);   // flash ring
  let rnd, parts = [], X = L0, move = 0, Wm = 0, Qm = 0, E = E0, acc = 0, nStep = 0, fi0 = 0, qRate = 0, tSim = 0;
  let selPush, selWall, selAnim, speed = 1, readout, top = 50, tStep = 25;

  const mulberry32 = (a) => () => {
    a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const restart = () => {                                            // the same gas every time: seeded, exactly at T0
    rnd = mulberry32(SEED); parts = [];
    for (let i = 0; i < N; i++) {
      const x = rnd() * L0, y = rnd() * LY, th = 2 * Math.PI * rnd(), s = Math.sqrt(-2 * Math.log(1 - rnd()) * KT);
      parts.push({ x, y, vx: s * Math.cos(th), vy: s * Math.sin(th), boost: -1 });
    }
    let sx = 0, sy = 0; for (const q of parts) { sx += q.vx * q.vx; sy += q.vy * q.vy; }
    const ax = Math.sqrt(E0 / sx), ay = Math.sqrt(E0 / sy);          // Σvx² = Σvy² = N·kT0, so E = E0
    for (const q of parts) { q.vx *= ax; q.vy *= ay; }
    X = L0; move = 0; Wm = 0; Qm = 0; E = E0; acc = 0; nStep = 0; qRate = 0; tSim = 0; fn.fill(-FL);
  };
  const flash = (x, y, kind) => { fx[fi0] = x; fy[fi0] = y; fk[fi0] = kind; fn[fi0] = nStep; fi0 = (fi0 + 1) % HN; };
  const bounce = (vx, w) => 2 * w - vx;                              // elastic reflection off a wall moving at w
  const push = () => {                                               // from the untouched start: the same seeded gas every time
    if (X === L0 && Wm === 0 && Math.abs(Qm * FJ) < 1e-6) restart();
    if (X > XEND) move = -1;
  };
  // one fixed step: piston motion, free flight, piston hits (work), fixed-wall hits (heat if conducting)
  const step = () => {
    const u = U[selPush.value()] || U.hidas, cond = selWall.value() === 'johtava';
    let w = 0;
    if (move < 0) { w = -u; X -= u * DT; if (X <= XEND) { X = XEND; move = 0; } }
    else if (move > 0) { w = u; X += u * DT; if (X >= L0) { X = L0; move = 0; } }
    const g = cond ? Math.sqrt(E0 / E) : 1;                          // speed factor at a conducting wall: T → T0
    let dW = 0, dQ = 0;
    const wall = (q) => { if (!cond) return; const e = (q.vx * q.vx + q.vy * q.vy) / 2; q.vx *= g; q.vy *= g; dQ += e * (g * g - 1);
      if (g < 0.995 || g > 1.005) flash(BOX.x + Math.min(Math.max(q.x, 0), X), BOX.y + Math.min(Math.max(q.y, 0), LY), 1); };
    for (const q of parts) {
      q.x += q.vx * DT; q.y += q.vy * DT;
      if (q.x < 0) { q.x = -q.x; q.vx = -q.vx; wall(q); }
      else if (q.x > X) {
        if (q.vx > w) { const e = q.vx * q.vx / 2; q.vx = bounce(q.vx, w); dW += q.vx * q.vx / 2 - e;
          if (w !== 0) { q.boost = tSim; flash(BOX.x + X, BOX.y + q.y, 0); } }
        q.x = Math.min(X, 2 * X - q.x);
      }
      if (q.y < 0) { q.y = -q.y; q.vy = -q.vy; wall(q); }
      else if (q.y > LY) { q.y = 2 * LY - q.y; q.vy = -q.vy; wall(q); }
    }
    Wm += dW; Qm += dQ; E += dW + dQ; nStep++; tSim += DT;
    qRate += (dQ * FJ / DT - qRate) * DT / 0.5;                      // heat flow (J/s), smoothed over about 0,5 s
  };
  const advance = (sec) => { acc += sec / DT; const n = Math.floor(acc + 1e-6); acc -= n; for (let i = 0; i < n; i++) step(); };
  const update = () => {
    let e = 0; for (const q of parts) e += (q.vx * q.vx + q.vy * q.vy) / 2;
    E = e;                                                           // re-sum: no drift of the running total
    const T = T0 * E / E0, W = Wm * FJ, Q = Qm * FJ, dU = (E - E0) * FJ;
    window.simState = Object.assign(window.simState && window.simState.labels ? { labels: window.simState.labels } : {}, {
      W, Q, dU, sum: Q + W, T, dT: T - T0, V: 100 * X / L0, p: (E / E0) / (X / L0), push: selPush.value(), wall: selWall.value(),
      u: U[selPush.value()], moving: move, done: move === 0 && X === XEND, t: tSim, qRate, speed, N });
    return window.simState;
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    const button = (text, fn) => { const b = p.createButton(text).parent(controls); b.elt.addEventListener('click', fn); return b; };
    button('Työnnä mäntää', push);
    button('Vedä ulos', () => { if (X < L0) move = 1; });
    button('Alkuun', () => { restart(); update(); });
    const select = (id, name, opts, val) => {
      const box = p.createDiv('').parent(controls).style('display', 'flex').style('flex-direction', 'column')
        .style('flex', '1 1 9rem').style('font-size', '.9rem');
      p.createSpan(name).parent(box).id(id);
      const s = p.createSelect().parent(box).style('min-height', '40px').attribute('aria-labelledby', id);
      for (const [t, v] of opts) s.option(t, v);
      s.selected(val); return s;
    };
    selPush = select('fy3-5-push', 'Männän nopeus', [['hidas', 'hidas'], ['nopea', 'nopea']], 'hidas');
    selWall = select('fy3-5-wall', 'Seinät', [['eristetty', 'eristetty'], ['johtava', 'johtava']], 'eristetty');
    selAnim = select('fy3-5-speed', 'Animaatio', [['hidas (0,5×)', '0.5'], ['normaali (1×)', '1'], ['nopea (3×)', '3']], '1');
    selAnim.changed(() => { speed = Number(selAnim.value()); });
    readout = p.createDiv('').parent('sim-root').class('readout');
    const det = p.createElement('details').parent('sim-root').class('note');
    p.createElement('summary', 'Lisätietoja').parent(det);
    p.createP('Malli: 40 hiukkasta liikkuu tasossa eivätkä törmää toisiinsa. Mäntään osuva hiukkanen kimpoaa kuin pallo mailasta: ' +
              'jos mäntä liikkuu sitä vastaan nopeudella u, hiukkasen nopeus männän suunnassa kasvaa 2u:n verran. Männän työ W on ' +
              'hiukkasten näin saama liike-energia, ja se on sama kuin männän voima kertaa matka. Ulos vedettäessä hiukkaset kimpoavat ' +
              'männästä hitaampina, ja W on negatiivinen.').parent(det);
    p.createP('Hidas mäntä liikkuu noin 50 kertaa hitaammin kuin hiukkaset keskimäärin, nopea vain noin 3,5 kertaa hitaammin. ' +
              'Nopeaan mäntään hiukkaset osuvat suuremmalla suhteellisella nopeudella, joten kaasu vastustaa sitä suuremmalla ' +
              'voimalla, ja samalla työntömatkalla työ on hieman suurempi. Eristetyssä sylinterissä koko työ jää kaasuun ' +
              '(ΔU = W), joten lämpötila nousee täsmälleen työn verran enemmän. Oikeassa pumpussa mäntä on paljon hitaampi kuin ' +
              'molekyylit (noin 500 m/s), joten siellä ero syntyy lähinnä siitä, ehtiikö lämpö siirtyä pois.').parent(det);
    p.createP('Eristetty seinä ei muuta hiukkasen nopeutta, joten Q = 0. Johtava seinä on huoneen lämpötilassa 293 K: siihen osuva ' +
              'hiukkanen kimpoaa hitaampana, jos kaasu on huonetta lämpimämpää, ja nopeampana, jos kaasu on kylmempää. Näin siirtynyt ' +
              'energia on lämpömäärä Q.').parent(det);
    p.createP('Luvut ovat mallin arvoja. Mallin kaasu vastaa lämpökapasiteetiltaan 0,50 g:aa ilmaa: sen sisäenergia kasvaa ' +
              '0,359 J jokaista kelviniä kohden. Oikea 0,50 g ilmaa lämpenisi samassa eristetyssä puristuksessa vain noin 36 K, ' +
              'ja työ olisi noin 13 J; johtavassa sylinterissä työ olisi noin 12 J. Malli liioittelee lämpenemistä kahdesta syystä: ' +
              'hiukkaset liikkuvat tasossa eivätkä avaruudessa, ja vain mäntä muuttaa niiden männän suuntaista liikettä, koska ' +
              'hiukkaset eivät törmää toisiinsa.').parent(det);
    p.createP('Malli on täysin toistettava: työntö alkutilasta alkaa aina samasta kaasun tilasta, joten samat valinnat antavat ' +
              'samat lukemat. Paine p/p₀ on molempien suuntien keskiarvo, laskettu hiukkasten liike-energiasta ja tilavuudesta. ' +
              'Mäntään kohdistuva paine on hitaan eristetyn työnnön jälkeen suurempi, noin 2,4 · p₀, koska vain männän suuntainen liike ' +
              'nopeutuu. Animaation nopeus muuttaa vain tahtia, ei lukemia.').parent(det);
    window.simAdvance = (s) => { advance(s); return update(); };
    window.simRestart = () => { restart(); update(); };
    window.simMove = (dir) => { if (dir < 0) push(); if (dir > 0 && X < L0) move = 1; return update(); };
    window.simBounce = bounce;
    restart(); update();
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { push: { input: selPush.elt, unit: '' }, wall: { input: selWall.elt, unit: '' } },
      reset: () => { selPush.value('hidas'); selWall.value('eristetty'); restart(); update(); },
      get: () => { const S = window.simState, r = (x, d) => Math.round(x * 10 ** d) / 10 ** d + 0;   // table values as shown
        return Object.assign({}, S, { W: r(S.W, 1), Q: r(S.Q, 1), dU: r(S.dU, 1), T: r(S.T, 0), dT: r(S.dT, 0), p: r(S.p, 2) }); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    advance(Math.min(p.deltaTime, 100) / 1000 * speed);
    const S = update(), { W, Q, dU, T } = S;
    readout.html(`Männän työ kaasuun W = <strong>${fs(W, 1)} J</strong>, lämpö seinien läpi Q = <strong>${fs(Q, 1)} J</strong>` +
      `<br>Sisäenergian muutos ΔU = <strong>${fs(dU, 1)} J</strong>` +
      `<br>Kaasu: T = <strong>${fi(T, 0)} K</strong> (ΔT = ${fs(T - T0, 0)} K), V = ${fi(S.V, 0)} %, paine p = ${fi(S.p, 2)} · p₀`);

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (n) => Math.round(n * k), ctx = p.drawingContext;
    const grad = (x0, y0, x1, y1, stops) => { const g = ctx.createLinearGradient(x0, y0, x1, y1); for (const [o, c] of stops) g.addColorStop(o, c); return g; };
    const rgb = (c, a = 1) => `rgba(${c[0]},${c[1]},${c[2]},${a})`;
    const rect = (x, y, w, h, fill) => { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); };
    const steel = (x, y, w, h, across, cu) => rect(x, y, w, h, grad(x, y, across ? x + w : x, across ? y : y + h,
      cu ? [[0, '#8a4a22'], [0.45, '#e9a36a'], [1, '#7a3e1a']] : [[0, '#79828d'], [0.45, '#dfe3e8'], [1, '#5d6570']]));
    const labels = [];
    const lab = (str, x, y, align = p.LEFT) => {
      p.textAlign(align); p.text(str, x, y);
      const w = p.textWidth(str), x0l = align === p.CENTER ? x - w / 2 : align === p.RIGHT ? x - w : x;
      labels.push({ s: str, x0: x0l, y0: y - p.textAscent(), x1: x0l + w, y1: y + p.textDescent() });
    };
    const arrow = (x0, y0, x1, y1, c, wgt) => {
      const a = Math.atan2(y1 - y0, x1 - x0), h = 4 + 2 * wgt;
      p.stroke(...c); p.strokeWeight(wgt); p.line(x0, y0, x1 - h * 0.8 * Math.cos(a), y1 - h * 0.8 * Math.sin(a)); p.noStroke(); p.fill(...c);
      p.triangle(x1, y1, x1 - h * Math.cos(a - 0.45), y1 - h * Math.sin(a - 0.45), x1 - h * Math.cos(a + 0.45), y1 - h * Math.sin(a + 0.45));
    };
    p.background(250);
    const cond = S.wall === 'johtava';

    // cylinder: gas region tinted by temperature, insulation or copper walls, piston, rod and handle
    const x0 = BOX.x - R, y0 = BOX.y - R, h = LY + 2 * R, xp = BOX.x + X + R, f = Math.max(-1, Math.min(1, (T - T0) / 150));
    const gasTop = f >= 0 ? mix([36, 49, 77], [92, 36, 52], f) : mix([36, 49, 77], [20, 60, 110], -f);
    rect(x0, y0, xp - x0, h, grad(0, y0, 0, y0 + h, [[0, rgb(gasTop)], [1, rgb(mix(gasTop, [10, 14, 24], 0.5))]]));
    rect(xp, y0, BOX.x + L0 + R + PW + 30 - xp, h, grad(0, y0, 0, y0 + h, [[0, '#f1f4f8'], [1, '#dce2ea']]));
    const xr = BOX.x + L0 + R + PW + 30;                             // open end of the cylinder
    if (!cond) {                                                     // insulation jacket with hatching outside the steel
      const jx = x0 - WT - INS, jy = y0 - WT - INS, jw = xr - jx, jh = h + 2 * (WT + INS);
      rect(jx, jy, jw, INS, '#f3e3a6'); rect(jx, y0 + h + WT, jw, INS, '#f3e3a6'); rect(jx, jy, INS, jh, '#f3e3a6');
      p.stroke(205, 180, 100); p.strokeWeight(1);
      for (let x = jx; x < jx + jw; x += 9) { p.line(x, jy + INS, x + INS, jy); p.line(x, y0 + h + WT + INS, x + INS, y0 + h + WT); }
      for (let y = jy + INS; y < jy + jh - INS; y += 9) p.line(jx, y + INS, jx + INS, y);
    }
    steel(x0 - WT, y0 - WT, xr - x0 + WT, WT, false, cond); steel(x0 - WT, y0 + h, xr - x0 + WT, WT, false, cond); steel(x0 - WT, y0, WT, h, true, cond);
    steel(xp, y0, PW, h, true); steel(xp + PW, y0 + h / 2 - 3, xr - xp - PW + 14, 6);
    p.noStroke(); p.fill(55, 62, 72); p.rect(xr + 12, y0 + h / 2 - 13, 10, 26, 3);

    // particles: trail back along the velocity (long and bright just after a piston hit), sphere coloured by speed
    const col = (q) => PAL[Math.min(31, Math.floor(32 * Math.hypot(q.vx, q.vy) / VMAX))];
    for (const q of parts) {
      const hot = q.boost >= 0 && tSim - q.boost < BOOST;
      let t = hot ? 3 * TAIL : TAIL;
      if (q.vx) t = Math.min(t, Math.max(0, q.vx > 0 ? q.x / q.vx : (q.x - X) / q.vx));
      if (q.vy) t = Math.min(t, Math.max(0, q.vy > 0 ? q.y / q.vy : (q.y - LY) / q.vy));
      const c = col(q), x = BOX.x + q.x, y = BOX.y + q.y;
      p.strokeWeight(hot ? 3 : 2); p.stroke(c[0], c[1], c[2], hot ? 230 : 150); p.line(x, y, x - q.vx * t, y - q.vy * t);
      if (hot) { p.noStroke(); p.fill(...COL_W, 110); p.circle(x, y, 15); }
    }
    p.noStroke();
    for (const q of parts) { const c = col(q); p.fill(c[0], c[1], c[2]); p.circle(BOX.x + q.x, BOX.y + q.y, 2 * R + 1); }
    p.fill(255, 255, 255, 190); for (const q of parts) p.circle(BOX.x + q.x - 1, BOX.y + q.y - 1, 2.4);
    for (let i = 0; i < HN; i++) {                                   // flashes: green = piston hit, red = conducting wall hit
      const a = 1 - (nStep - fn[i]) / FL; if (a <= 0 || a > 1) continue;
      p.fill(...(fk[i] ? COL_Q : COL_W), 220 * a); p.circle(fx[i], fy[i], 6 + 6 * a);
    }

    // work arrow on the rod while the piston moves, heat arrows through the walls while heat flows
    p.textSize(ts(16)); p.textStyle(p.BOLD);
    if (move !== 0) {
      const ya = y0 + h / 2 - 34, xa = xp + PW + 14, L = 34;
      if (move < 0) arrow(xa + L, ya, xa, ya, COL_W, 4); else arrow(xa, ya, xa + L, ya, COL_W, 4);
      p.fill(...COL_W); lab('W', xa + L / 2, ya - 10, p.CENTER);
    }
    if (cond && Math.abs(qRate) > 0.2) {
      const L = 8 + 16 * Math.min(1, Math.sqrt(Math.abs(qRate) / 30)), out = qRate < 0, yt = y0 - WT - 4, yb = y0 + h + WT + 4;
      for (const ax of [150, 230, 310]) {
        if (out) { arrow(ax, yt, ax, yt - L, COL_Q, 3); arrow(ax, yb, ax, yb + L, COL_Q, 3); }
        else { arrow(ax, yt - L, ax, yt, COL_Q, 3); arrow(ax, yb + L, ax, yb, COL_Q, 3); }
      }
      if (k <= 1.3) { p.fill(...COL_Q); lab('Q', 330, yt - 6); }
    }
    p.textStyle(p.NORMAL);

    // values and legends around the cylinder
    p.fill(30); p.textSize(ts(17)); const sT = `T = ${fi(T, 0)} K`; lab(sT, x0 - WT, 36); const xT = x0 - WT + p.textWidth('T = 000 K') + 18;
    p.textSize(ts(13)); const yD = y0 + h + WT + INS + 8, yV = yD + 4 + ts(12), xw = xr + 4;
    p.stroke(80); p.strokeWeight(1.2); p.line(x0, yD, xp, yD); p.line(x0, yD - 5, x0, yD + 5); p.line(xp, yD - 5, xp, yD + 5);
    p.noStroke(); p.fill(40); const wl = cond ? 'johtava seinä' : 'eristetty seinä', xwl = xw - p.textWidth(wl);
    lab(wl, xw, yV, p.RIGHT);
    const sV = `V = ${fi(S.V, 0)} %`, hV = p.textWidth(sV) / 2;
    lab(sV, Math.max(x0 + hV, Math.min(xwl - 10 - hV, (x0 + xp) / 2)), yV, p.CENTER);
    const lw = k > 1.5 ? 30 : 44; p.textSize(ts(13));                  // speed legend in the top row, right of T
    lab('hidas', xT, 36); const lx0 = xT + p.textWidth('hidas') + 5;
    rect(lx0, 36 - ts(4) - 4, lw, 8, grad(lx0, 0, lx0 + lw, 0, [[0, rgb(SLOW)], [0.5, rgb(MID)], [1, rgb(FAST)]]));
    p.fill(40); lab('nopea', lx0 + lw + 5, 36);

    // energy bars Q, W, ΔU on one axis, zero in the middle, gridlines at the tick steps
    const v = Math.max(Math.abs(W), Math.abs(Q), Math.abs(dU));
    if (v > 0.98 * top || (v < 0.3 * top && top > 50)) [top, tStep] = scale(v);
    const ym = (BAR.y0 + BAR.y1) / 2, Y = (x) => ym - (BAR.y1 - BAR.y0) / 2 * Math.max(-1.04, Math.min(1.04, x / top));
    p.stroke(228); p.strokeWeight(1);
    for (let j = -2; j <= 2; j++) if (j) p.line(BAR.ax, Y(j * tStep), 592, Y(j * tStep));
    p.stroke(60); p.strokeWeight(2); p.line(BAR.ax, BAR.y0 - 6, BAR.ax, BAR.y1 + 6); p.line(BAR.ax, ym, 592, ym);
    p.noStroke(); p.fill(60); p.textSize(ts(11));
    for (let j = -2; j <= 2; j++) lab(j ? fs(j * tStep, 0) : '0', BAR.ax - 5, Y(j * tStep) + ts(4), p.RIGHT);
    p.textSize(ts(13)); p.fill(40); lab('energia (J)', 592, 40, p.RIGHT);
    const vals = [Q, W, dU], cols = [COL_Q, COL_W, COL_U], names = ['Q', 'W', 'ΔU'], dec = k > 1.3 ? 0 : 1;
    for (let i = 0; i < 3; i++) {
      const bx = BAR.x[i] - BAR.w / 2, yv = Y(vals[i]), c = cols[i], y = Math.min(yv, ym), hb = Math.abs(yv - ym);
      if (hb > 0.5) rect(bx, y, BAR.w, hb, grad(bx, 0, bx + BAR.w, 0, [[0, rgb(c, 0.9)], [0.35, rgb(mix(c, [255, 255, 255], 0.35))], [1, rgb(mix(c, [0, 0, 0], 0.25))]]));
      p.fill(...c); p.textSize(ts(12));
      if (vals[i] >= 0) lab(fs(vals[i], dec), BAR.x[i], yv - 5, p.CENTER); else lab(fs(vals[i], dec), BAR.x[i], yv + 4 + ts(11), p.CENTER);
      p.textSize(ts(15)); p.textStyle(p.BOLD); lab(names[i], BAR.x[i], 352, p.CENTER); p.textStyle(p.NORMAL);
    }
    if (k <= 1.3) { p.fill(40); p.textSize(ts(13)); lab('ΔU = Q + W', BAR.x[1], 390, p.CENTER); }
    window.simState.labels = labels;
  };

  const scale = (v) => {                                             // axis top n·step with n = 2 ticks per side
    for (const st of [10, 25, 50, 100, 250, 500, 1000]) if (2 * st >= 1.08 * v) return [2 * st, st];
    return [5000, 2500];
  };
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                       // decimal comma, minus sign
  const fs = (x, d) => { const s = fi(Math.abs(x) < 0.5 * 10 ** -d ? 0 : x, d); return x >= 0.5 * 10 ** -d ? '+' + s : s; };   // signed
});
