// fy2-1 Energialajit ja energian säilyminen: a skateboarder in a half-pipe, with the energy in joules stacked by form.
// Model: a 50 kg skateboarder (a point on the track) is released from rest at height h0 on a parabolic half-pipe (rims 3,0 m high, 9,0 m apart).
// Gravity acts along the track; the optional friction is a constant force mu m g along the track against the motion (mu = 0 / 0,04 / 0,10).
// Potential energy E_p comes from the height, kinetic energy E_k from the speed; the thermal energy E_lämpö is what the friction force has
// done in total along the path travelled so far. The three are added up from their own values (nothing is subtracted from a total), so the
// constant sum is a result of the motion. The motion is computed once for the chosen h0 and friction (RK4, step 2 ms, 16 s) and played back in
// simulated time (time · speed), so the speed select changes only the pace and the "Hetki t" slider scrubs the same run.
// Colour carries meaning: blue = potential, orange = kinetic, red (hatched) = thermal energy, in the scene, the bar, the chart and the legend.
// Every canvas text goes through lab(), which pushes its ink box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  const g = 9.81, M = 50, HR = 3.0, LR = 4.5, A = 2 * HR / (LR * LR), DT = 0.002, T = 16, N = Math.round(T / DT);
  const MU = [0, 0.04, 0.10];
  const COL = { p: [25, 113, 194], k: [255, 192, 120], th: [201, 42, 42], ink: [31, 41, 51], muted: [107, 116, 128] };
  const SC = { x: 6, y: 6, w: 376, h: 252 }, SX = (xm) => 194 + 38 * xm, SY = (hm) => 212 - 38 * hm;      // scene panel, pixels per metre 38
  const BR = { x: 388, y: 6, w: 206, h: 252, ax: 444, y0: 226, per: 170 / 1500, bx: 452, bw: 36 };           // energy panel: axis, bar, 0…1500 J
  const CH = { x: 6, y: 266, w: 588, h: 128, x0: 60, x1: 490, y0: 360, per: 64 / 1500 };                    // chart panel: t 0…16 s, E 0…1500 J
  let btn, slT, slH, selK, selSp, readout, k = 1, labels = [];
  let tau = 0, tmax = 0, running = false, face = 1, run = null, runKey = '';

  // --- the physics: the whole run for a start height and a friction level ---
  const slope = (x) => A * x;
  function accel(x, u, sg, mu) {                                  // u = dx/dt; equation of motion of a bead on y = h(x) with friction mu m g
    const hp = slope(x), w = 1 + hp * hp;
    return -(g * hp + hp * A * u * u + mu * g * sg * Math.sqrt(w)) / w;
  }
  function compute(h0, mu) {
    const X = new Float64Array(N + 1), U = new Float64Array(N + 1), E = new Float64Array(N + 1);
    let x = -LR * Math.sqrt(h0 / HR), u = 0, eth = 0, stuck = false;
    X[0] = x; U[0] = u; E[0] = eth;
    for (let i = 1; i <= N; i++) {
      if (!stuck) {
        let sg = u > 0 ? 1 : u < 0 ? -1 : 0;
        if (sg === 0) {
          const hp = slope(x), sn = hp / Math.sqrt(1 + hp * hp);
          if (Math.abs(sn) <= mu) stuck = true; else sg = sn > 0 ? -1 : 1;     // at rest: friction holds, or the motion starts downhill
        }
        if (!stuck) {
          const f = (xx, uu) => [uu, accel(xx, uu, sg, mu)];
          const k1 = f(x, u), k2 = f(x + DT / 2 * k1[0], u + DT / 2 * k1[1]), k3 = f(x + DT / 2 * k2[0], u + DT / 2 * k2[1]), k4 = f(x + DT * k3[0], u + DT * k3[1]);
          const xn = x + DT / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]);
          let un = u + DT / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]);
          if (u !== 0 && un * u < 0) { const hp = slope(xn); if (Math.abs(hp / Math.sqrt(1 + hp * hp)) <= mu) un = 0; }   // friction cannot reverse the motion by itself
          const v0 = Math.abs(u) * Math.sqrt(1 + slope(x) ** 2), v1 = Math.abs(un) * Math.sqrt(1 + slope(xn) ** 2);
          eth += mu * M * g * (v0 + v1) / 2 * DT;                    // the work of the friction force along the path = thermal energy
          x = xn; u = un;
        }
      }
      X[i] = x; U[i] = stuck ? 0 : u; E[i] = eth;
    }
    return { X, U, E, e0: M * g * h0 };
  }
  function ensureRun() {
    const h0 = Number(slH.value()), kk = Number(selK.value()), key = h0 + '|' + kk;
    if (key !== runKey) { run = compute(h0, MU[kk]); runKey = key; }
    return run;
  }
  const at = (i) => {
    const x = run.X[i], u = run.U[i], h = HR * x * x / (LR * LR), v = Math.abs(u) * Math.sqrt(1 + slope(x) ** 2);
    return { x, u, h, v, Ep: M * g * h, Ek: 0.5 * M * v * v, Eth: run.E[i] };
  };
  const idx = (t) => Math.max(0, Math.min(N, Math.round(t / DT)));
  function whole(a) {                                              // whole joules that add up to the whole-joule total (largest remainder)
    const tot = Math.round(a[0] + a[1] + a[2]), fl = a.map(Math.floor);
    let rest = tot - fl[0] - fl[1] - fl[2];
    a.map((v, i) => [v - fl[i], i]).sort((u, v) => v[0] - u[0]).forEach(([, i]) => { if (rest > 0) { fl[i]++; rest--; } });
    return fl;
  }
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');            // Finnish decimal comma inside LaTeX
  const tj = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '\\,');   // 1471 -> 1\,471

  const restart = () => { tau = 0; tmax = 0; running = false; slT.value(0); face = 1; };
  const toTime = (t) => { tau = Math.min(T, Math.max(0, Number(t))); tmax = Math.max(tmax, tau); };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btn = p.createButton(__('aloita')).parent(controls);
    btn.elt.addEventListener('click', () => {
      if (running) { running = false; return; }
      if (tau >= T) { tau = 0; tmax = 0; }                          // replay from the start
      running = true;
    });
    const bR = p.createButton(__('alusta')).parent(controls); bR.elt.addEventListener('click', restart);
    const lt = p.createElement('label').parent(controls); const sT = p.createSpan('').parent(lt); slT = p.createSlider(0, T, 0, 0.5).parent(lt);
    const lh = p.createElement('label').parent(controls); const sH = p.createSpan('').parent(lh); slH = p.createSlider(1, 3, 2, 0.5).parent(lh);
    const lk = p.createElement('label').parent(controls); p.createSpan(__('kitka')).parent(lk); selK = p.createSelect().parent(lk);
    selK.option(__('kitka_ei'), '0'); selK.option(__('kitka_pieni'), '1'); selK.option(__('kitka_suuri'), '2');
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(lv); selSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                           // pace only: time advances by dt · speed
    slT.elt.addEventListener('input', () => { running = false; toTime(slT.value()); });
    slT.elt.addEventListener('change', () => { running = false; toTime(slT.value()); });
    for (const e of [slH.elt, selK.elt]) { const f = () => { restart(); }; e.addEventListener('input', f); e.addEventListener('change', f); }
    lt.sp = sT; lh.sp = sH;
    p.createP(__('huomautus')).parent('sim-root').class('note');
    p.textFont('Arial');
    ensureRun(); restart();
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { t: { input: slT.elt, unit: 's' }, h0: { input: slH.elt, unit: 'm' }, kitka: { input: selK.elt, unit: '' } },
      reset: () => { selK.selected('0'); slH.value(2); selSp.selected('1'); restart(); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
    p.labelBoxes = { sT, sH };
  };

  p.draw = () => {
    ensureRun();
    const sp = Number(selSp.value()), kk = Number(selK.value()), h0 = Number(slH.value());
    if (running) { toTime(tau + Math.min(p.deltaTime, 100) / 1000 * sp); slT.value(tau); if (tau >= T) running = false; }
    const s = at(idx(tau)), parts = whole([s.Ep, s.Ek, s.Eth]), Etot = parts[0] + parts[1] + parts[2];
    if (Math.abs(s.u) > 0.05) face = s.u > 0 ? 1 : -1;
    p.labelBoxes.sT.html(__('hetki', { t: tx(tau, 1) })); p.labelBoxes.sH.html(__('alkukorkeus', { h: tx(h0, 1) }));
    const bt = running ? __('tauko') : __('aloita'); if (btn.elt.textContent !== bt) btn.elt.textContent = bt;
    readout.html(__('rivi_1', { t: tx(tau, 1), h: tx(s.h, 2), v: tx(s.v, 1) }) + __('rivi_2', { ep: tj(parts[0]), ek: tj(parts[1]), el: tj(parts[2]) }) + __('rivi_3', { e: tj(Etot) }));
    window.simState = { t: tau, h0, kitka: kk, h: s.h, v: s.v, Ep: parts[0], Ek: parts[1], Eth: parts[2], Ekok: Etot, Emek: parts[0] + parts[1], running, speed: sp, tmax, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(11 * k);
    labels = [];
    p.background(250);
    scene(s, h0, kk, Etot, fh);
    bars(parts, Etot, fh);
    chart(fh);
    window.simState.labels = labels;
  };

  // --- the scene: sky, half-pipe that warms with the thermal energy, the skateboarder ---
  function scene(s, h0, kk, Etot, fh) {
    const c = p.drawingContext, frac = Math.min(1, s.Eth / Math.max(1, run.e0));
    c.save(); c.beginPath(); c.roundRect(SC.x, SC.y, SC.w, SC.h, 8); c.clip();
    const sky = c.createLinearGradient(0, SC.y, 0, SC.y + SC.h); sky.addColorStop(0, '#cfe6fa'); sky.addColorStop(0.7, '#f4f9fd'); sky.addColorStop(1, '#f6f1e6');
    c.fillStyle = sky; c.fillRect(SC.x, SC.y, SC.w, SC.h);
    p.noStroke(); p.fill(255, 255, 255, 190);
    for (const [cx, cy, r] of [[78, 44, 17], [100, 38, 21], [124, 46, 15], [292, 30, 14], [312, 25, 19], [334, 32, 13]]) p.ellipse(cx, cy, r * 2.2, r * 1.2);
    // the wall under the half-pipe: concrete with seams, tinted red as thermal energy builds up
    c.beginPath(); c.moveTo(SX(-LR) - 14, SY(HR)); c.lineTo(SX(-LR), SY(HR));
    for (let i = 0; i <= 90; i++) { const xm = -LR + i * 2 * LR / 90; c.lineTo(SX(xm), SY(HR * xm * xm / (LR * LR))); }
    c.lineTo(SX(LR), SY(HR)); c.lineTo(SX(LR) + 14, SY(HR)); c.lineTo(SX(LR) + 14, SC.y + SC.h); c.lineTo(SX(-LR) - 14, SC.y + SC.h); c.closePath();
    const wall = c.createLinearGradient(0, SY(HR), 0, SC.y + SC.h); wall.addColorStop(0, '#c4ccd4'); wall.addColorStop(1, '#8a96a3');
    c.fillStyle = wall; c.fill(); c.fillStyle = `rgba(201,42,42,${(0.30 * frac).toFixed(3)})`; c.fill();
    c.save(); c.clip(); c.strokeStyle = 'rgba(31,41,51,0.12)'; c.lineWidth = 1;
    for (let xs = SX(-LR) - 14; xs < SX(LR) + 16; xs += 38) { c.beginPath(); c.moveTo(xs, SY(HR)); c.lineTo(xs, SC.y + SC.h); c.stroke(); }
    c.restore();
    // the riding surface: grey, glowing red as the thermal energy grows
    c.beginPath(); for (let i = 0; i <= 90; i++) { const xm = -LR + i * 2 * LR / 90; (i ? c.lineTo.bind(c) : c.moveTo.bind(c))(SX(xm), SY(HR * xm * xm / (LR * LR))); }
    c.strokeStyle = `rgb(${Math.round(70 + 131 * frac)},${Math.round(78 - 36 * frac)},${Math.round(88 - 46 * frac)})`; c.lineWidth = 5; c.lineJoin = 'round'; c.stroke();
    c.strokeStyle = '#1f2933'; c.lineWidth = 3; c.beginPath(); c.moveTo(SX(-LR) - 14, SY(HR)); c.lineTo(SX(-LR), SY(HR)); c.moveTo(SX(LR), SY(HR)); c.lineTo(SX(LR) + 14, SY(HR)); c.stroke();
    // levels: the start height (dashed) and the zero level of the potential energy
    p.stroke(...COL.muted); p.strokeWeight(1.5); c.setLineDash([7, 6]);
    p.line(SX(-LR) - 12, SY(h0), SX(LR) + 12, SY(h0)); p.line(SX(-LR) - 12, SY(0), SX(LR) + 12, SY(0)); c.setLineDash([]);
    c.restore();
    lab(__('h0_nimi', { h: tx(h0, 1) }), SX(0), SY(h0) - 6, 'c', fh, COL.muted);
    lab(__('nollataso'), SX(0), SY(0) + 14 + fh, 'c', fh, COL.ink);
    // the skateboarder
    const px = SX(s.x), py = SY(s.h);
    p.stroke(...COL.muted); p.strokeWeight(1.5); c.setLineDash([3, 5]); p.line(px, py - 4, px, SY(0)); c.setLineDash([]);
    if (kk > 0 && s.v > 0.3) {                                      // friction at work: a warm glow under the board
      const gl = c.createRadialGradient(px, py, 1, px, py, 22), a = Math.min(0.85, 0.25 + s.v * 0.1);
      gl.addColorStop(0, `rgba(255,192,120,${a})`); gl.addColorStop(0.5, `rgba(232,89,12,${a * 0.6})`); gl.addColorStop(1, 'rgba(201,42,42,0)');
      c.fillStyle = gl; c.beginPath(); c.arc(px, py, 22, 0, 2 * Math.PI); c.fill();
    }
    skater(px, py, -Math.atan(slope(s.x)), face);
  }
  function skater(cx, cy, ang, dir) {
    p.push(); p.translate(cx, cy); p.rotate(ang); p.scale(dir, 1);
    const ln = (x1, y1, x2, y2, w, col) => { p.stroke(...col); p.strokeWeight(w); p.strokeCap(p.ROUND); p.line(x1, y1, x2, y2); };
    p.noStroke(); p.fill(31, 41, 51); p.circle(-10, -3.4, 6.4); p.circle(10, -3.4, 6.4);                // wheels
    p.fill(217, 178, 106); p.stroke(138, 95, 34); p.strokeWeight(1.2); p.rect(-17, -9, 34, 4.2, 2.1);    // board
    ln(-8, -9.5, -4, -19, 4.2, [47, 59, 74]); ln(-4, -19, 1, -28, 4.2, [47, 59, 74]);                      // back leg
    ln(9, -9.5, 7, -19, 4.2, [47, 59, 74]); ln(7, -19, 1, -28, 4.2, [47, 59, 74]);                         // front leg
    ln(1, -28, 4, -44, 7, [11, 114, 133]);                                                                 // torso
    ln(4, -41, -6, -34, 3, [233, 201, 138]); ln(4, -41, 14, -36, 3, [233, 201, 138]);                      // arms
    p.noStroke(); p.fill(233, 201, 138); p.circle(6, -51, 12.5); p.fill(31, 41, 51); p.arc(6, -52, 13, 13, Math.PI, 2 * Math.PI);   // head and cap
    p.pop();
  }

  // --- the energy bar: potential, kinetic and thermal energy stacked on a joule scale ---
  function bars(parts, Etot, fh) {
    const c = p.drawingContext;
    c.save(); c.beginPath(); c.roundRect(BR.x, BR.y, BR.w, BR.h, 8); c.clip(); p.noStroke(); p.fill(255); p.rect(BR.x, BR.y, BR.w, BR.h); c.restore();
    p.stroke(228); p.strokeWeight(1);
    for (const e of [500, 1000, 1500]) p.line(BR.ax, BR.y0 - e * BR.per, BR.bx + BR.bw + 8, BR.y0 - e * BR.per);
    // segments from the bottom: thermal (hatched), kinetic, potential
    let y = BR.y0;
    const seg = (e, col, hatch) => {
      const hh = e * BR.per; if (hh <= 0) return;
      p.noStroke(); p.fill(...col); p.rect(BR.bx, y - hh, BR.bw, hh);
      if (hatch) { c.save(); c.beginPath(); c.rect(BR.bx, y - hh, BR.bw, hh); c.clip(); c.strokeStyle = 'rgba(255,255,255,0.55)'; c.lineWidth = 2;
        for (let d = -hh; d < BR.bw + hh; d += 7) { c.beginPath(); c.moveTo(BR.bx + d, y); c.lineTo(BR.bx + d + hh, y - hh); c.stroke(); } c.restore(); }
      p.noFill(); p.stroke(...COL.ink); p.strokeWeight(1.5); p.rect(BR.bx, y - hh, BR.bw, hh);
      y -= hh;
    };
    seg(parts[2], COL.th, true); seg(parts[1], COL.k, false); seg(parts[0], COL.p, false);
    // the total: a dashed level that never moves while the run goes on
    p.stroke(...COL.ink); p.strokeWeight(1.5); c.setLineDash([6, 5]); p.line(BR.ax, BR.y0 - Etot * BR.per, BR.bx + BR.bw + 8, BR.y0 - Etot * BR.per); c.setLineDash([]);
    // axis with arrowhead, ticks and numbers
    p.stroke(60); p.strokeWeight(1.8); p.line(BR.ax, BR.y0, BR.ax, BR.y0 - 1500 * BR.per - 8);
    p.noStroke(); p.fill(60); p.triangle(BR.ax, BR.y0 - 1500 * BR.per - 16, BR.ax - 4.5, BR.y0 - 1500 * BR.per - 7, BR.ax + 4.5, BR.y0 - 1500 * BR.per - 7);
    for (const e of [0, 500, 1000, 1500]) {
      p.stroke(60); p.strokeWeight(1.5); p.line(BR.ax - 5, BR.y0 - e * BR.per, BR.ax, BR.y0 - e * BR.per);
      lab(`$${tj(e)}$`, BR.ax - 8, BR.y0 - e * BR.per + fh * 0.36, 'r', fh);
    }
    lab(__('akseli_e'), BR.ax, BR.y + 4 + fh, 'c', fh);
    // legend, top to bottom as the segments are stacked
    const rows = [[COL.p, __('e_p'), 70], [COL.k, __('e_k'), 110], [COL.th, __('e_lampo'), 150]];
    for (const [col, s, ly] of rows) {
      p.stroke(...COL.ink); p.strokeWeight(1.5); p.fill(...col); p.rect(BR.bx + BR.bw + 12, ly - 6, 12, 12);
      lab(s, BR.bx + BR.bw + 30, ly + fh * 0.36, 'l', fh, COL.ink);
    }
    lab(__('kokonais', { e: tj(Etot) }), BR.ax + 10, BR.y0 + 10 + fh, 'l', fh, COL.ink);
  }

  // --- the chart: the three energies against time, drawn for the times visited so far; the top stays level ---
  function chart(fh) {
    const c = p.drawingContext, X = (t) => CH.x0 + t / T * (CH.x1 - CH.x0), Y = (e) => CH.y0 - e * CH.per;
    c.save(); c.beginPath(); c.roundRect(CH.x, CH.y, CH.w, CH.h, 8); c.clip(); p.noStroke(); p.fill(255); p.rect(CH.x, CH.y, CH.w, CH.h); c.restore();
    p.stroke(228); p.strokeWeight(1);
    for (const t of [4, 8, 12, 16]) p.line(X(t), CH.y0, X(t), Y(1500));
    for (const e of [500, 1000, 1500]) p.line(CH.x0, Y(e), CH.x1, Y(e));
    const last = idx(tmax), step = 25, pts = [];
    for (let i = 0; i < last; i += step) pts.push(i); pts.push(last);
    const band = (lo, hi, col) => {
      if (pts.length < 2) return;
      p.noStroke(); p.fill(...col, 235); p.beginShape();
      pts.forEach((i) => { const q = at(i); p.vertex(X(i * DT), Y(hi(q))); });
      for (let j = pts.length - 1; j >= 0; j--) { const q = at(pts[j]); p.vertex(X(pts[j] * DT), Y(lo(q))); }
      p.endShape(p.CLOSE);
    };
    band(() => 0, (q) => q.Eth, COL.th); band((q) => q.Eth, (q) => q.Eth + q.Ek, COL.k); band((q) => q.Eth + q.Ek, (q) => q.Eth + q.Ek + q.Ep, COL.p);
    // the total: a dashed level across the whole time axis
    p.stroke(...COL.ink); p.strokeWeight(1.5); c.setLineDash([6, 5]); p.line(CH.x0, Y(run.e0), CH.x1, Y(run.e0)); c.setLineDash([]);
    // the present moment
    p.stroke(90); p.strokeWeight(1.2); c.setLineDash([4, 4]); p.line(X(tau), CH.y0, X(tau), Y(1500)); c.setLineDash([]);
    const q = at(idx(tau)); p.fill(255); p.stroke(...COL.ink); p.strokeWeight(2); p.circle(X(tau), Y(q.Eth + q.Ek + q.Ep), 9);
    // axes
    p.stroke(60); p.strokeWeight(1.8); p.noFill(); p.line(CH.x0, CH.y0, CH.x1 + 10, CH.y0); p.line(CH.x0, CH.y0, CH.x0, Y(1500) - 10);
    p.noStroke(); p.fill(60);
    p.triangle(CH.x1 + 18, CH.y0, CH.x1 + 9, CH.y0 - 4.5, CH.x1 + 9, CH.y0 + 4.5); p.triangle(CH.x0, Y(1500) - 18, CH.x0 - 4.5, Y(1500) - 9, CH.x0 + 4.5, Y(1500) - 9);
    for (const t of [0, 4, 8, 12, 16]) { p.stroke(60); p.strokeWeight(1.5); p.line(X(t), CH.y0, X(t), CH.y0 + 5); lab(`$${t}$`, X(t), CH.y0 + 6 + fh, 'c', fh); }
    for (const e of [0, 1000]) { p.stroke(60); p.strokeWeight(1.5); p.line(CH.x0 - 5, Y(e), CH.x0, Y(e)); lab(`$${tj(e)}$`, CH.x0 - 8, Y(e) + fh * 0.36, 'r', fh); }
    lab(__('akseli_t'), CH.x1 + 22, CH.y0 + fh * 0.36, 'l', fh);
    lab(__('akseli_e'), CH.x0 + 12, Y(1500) - 14, 'l', fh);
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
});
