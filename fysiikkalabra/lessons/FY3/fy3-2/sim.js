// fy3-2 Työ ja energia: a box pulled along a horizontal floor by a constant force along the motion.
// Physics: W = F s (force along the displacement), P = W / t.
// Work is also the area under the (s,F) graph; the right-hand plot fills that area as the box moves.
// The numeric readout (W, P, work so far) is plain DOM text, so it stays readable on a phone;
// the canvas only draws the picture, and its text is scaled up when the canvas is shrunk by CSS.
// Speed control: the box advances by simulated time (real frame time)·speed, so "Nopeus" changes only the pace;
// W, P and the work done at a given fraction of s are the same at every speed.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const FLOOR_Y = 250, FLOOR_END = 346, X0 = 40, BOX = 40, PX_PER_M = 13;   // 20 m + box fits left of x = 346
  const G = { x: 380, y: 70, w: 200, h: 180 };                              // (s,F) graph box
  let sF, sS, sT, lF, lS, lT, btn, sSp, readout;
  let u = 0;                                                  // fraction of s covered so far, 0…1
  let running = false;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sF, lF] = slider(controls, 0, 100, 60, 1);      // voima F (N)
    [sS, lS] = slider(controls, 1, 20, 10, 0.5);     // matka s (m)
    [sT, lT] = slider(controls, 1, 20, 5, 0.5);      // aika t (s)
    btn = p.createButton(__('veda')).parent(controls);
    btn.mousePressed(() => { u = 0; running = true; });
    const lv = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(lv); sSp = p.createSelect().parent(lv);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) sSp.option(txt, v);
    sSp.selected('1');                                         // pace only: the box covers s in the simulated time t
    p.textFont('Arial');
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset the three sliders
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { F: { input: sF.elt, unit: 'N' }, s: { input: sS.elt, unit: 'm' }, t: { input: sT.elt, unit: 's' } },
      reset: () => { sF.value(60); sS.value(10); sT.value(5); u = 0; running = false; },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const F = sF.value(), s = sS.value(), t = sT.value();
    const W = F * s;                       // work over the whole distance
    const P = W / t;                       // average power
    const speed = Number(sSp.value());
    if (running) { u += Math.min(p.deltaTime, 100) / 1000 * speed / t; if (u >= 1) { u = 1; running = false; } }
    const Wdone = W * u;                   // constant force: work grows linearly with distance

    lF.html(__(`voima`, {f: F})); lS.html(__(`matka`, {s: tx(s, 1)})); lT.html(__(`aika`, {t: tx(t, 1)}));
    readout.html(__(`fs_p_t`, {w: tj(W), p: tx(P, 1)}) +
                 __(`tehty_tyo_tahan`, {wdone: tj(Wdone), u: tx(u * t, 1)}));
    window.simState = { F, s, t, W, P, u, Wdone, running, tElapsed: u * t, speed };

    // The canvas is scaled down by CSS on narrow screens; enlarge canvas text so it stays near 11 px or more.
    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (n) => Math.round(n * k);

    p.background(250);
    // floor with a metre scale
    p.stroke(60); p.strokeWeight(2); p.line(0, FLOOR_Y, FLOOR_END, FLOOR_Y);
    p.strokeWeight(1); p.textSize(ts(11)); p.textAlign(p.CENTER);
    for (let m = 0; m <= 20; m += 5) { const x = X0 + m * PX_PER_M; p.stroke(150); p.line(x, FLOOR_Y, x, FLOOR_Y + 5); p.noStroke(); p.fill(90); p.text(`$${m}\\,\\text{m}$`, x, FLOOR_Y + 5 + ts(13)); }
    const xEnd = X0 + s * PX_PER_M;
    p.stroke(26, 77, 46); p.drawingContext.setLineDash([4, 4]); p.line(xEnd, FLOOR_Y - 90, xEnd, FLOOR_Y); p.drawingContext.setLineDash([]);

    // box and force arrow (100 N = 50 px, so the tip stays left of the graph even at s = 20 m)
    const bx = X0 + u * s * PX_PER_M, by = FLOOR_Y - BOX;
    p.noStroke(); p.fill(200, 120, 60); p.rect(bx - BOX / 2, by, BOX, BOX, 4);
    const ax = bx + BOX / 2, ay = by + BOX / 2, tipX = ax + F * 0.5;
    if (F > 0) { arrow(ax, ay, tipX, ay, p.color(200, 40, 40)); p.noStroke(); p.fill(200, 40, 40); p.textAlign(p.LEFT); p.textSize(ts(13)); p.text(`$F = ${F}\\,\\text{N}$`, ax + 6, ay - 12); }

    // (s,F) graph: the work done so far is the shaded area under the constant force
    p.stroke(60); p.strokeWeight(2); p.noFill();
    p.line(G.x, G.y + G.h, G.x + G.w, G.y + G.h); p.line(G.x, G.y + G.h, G.x, G.y);
    const yF = G.y + G.h - (F / 100) * (G.h - 20), xS = G.x + (s / 20) * (G.w - 20);
    p.noStroke(); p.fill(26, 77, 46, 90); if (F > 0) p.rect(G.x, yF, (xS - G.x) * u, G.y + G.h - yF);
    p.stroke(26, 77, 46); p.strokeWeight(3); if (F > 0) p.line(G.x, yF, xS, yF);
    p.strokeWeight(1); p.stroke(150); p.drawingContext.setLineDash([4, 4]); p.line(xS, yF, xS, G.y + G.h); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(90); p.textSize(ts(12)); p.textAlign(p.CENTER);
    p.text('$s\\ (\\text{m})$', G.x + G.w - 10, G.y + G.h + ts(30)); p.text(`$${tx(s, 1)}$`, xS, G.y + G.h + ts(15));
    p.textAlign(p.RIGHT); p.text('$F\\ (\\text{N})$', G.x + ts(20), G.y - 8); p.text(`$${F}$`, G.x - 6, yF + 4);
    p.textAlign(p.RIGHT); p.fill(26, 77, 46); p.textSize(ts(13)); p.text(__('pinta_ala'), G.x + G.w + 10, Math.max(G.y - 8 - ts(14), ts(13) + 6));   // clear of the canvas top on a phone

    // progress bar: filled fraction of the total work
    const barX = 20, barY = 330, barW = 560, barH = 16;
    p.noFill(); p.stroke(120); p.strokeWeight(1); p.rect(barX, barY, barW, barH, 4);
    p.noStroke(); p.fill(26, 77, 46); if (W > 0) p.rect(barX, barY, barW * u, barH, 4);
    p.fill(90); p.textSize(ts(12)); p.textAlign(p.LEFT); p.text('$0\\,\\text{J}$', barX, barY + barH + ts(14)); p.textAlign(p.RIGHT); p.text(`$${tj(W)}\\,\\text{J}$`, barX + barW, barY + barH + ts(14));
  };

  function arrow(x1, y1, x2, y2, col) {
    p.stroke(col); p.strokeWeight(3); p.line(x1, y1, x2, y2);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 10;
    p.fill(col); p.noStroke();
    p.triangle(x2, y2, x2 - L * Math.cos(a - 0.4), y2 - L * Math.sin(a - 0.4), x2 - L * Math.cos(a + 0.4), y2 - L * Math.sin(a + 0.4));
  }
  const fi = (x, d) => x.toFixed(d).replace('.', ',');         // Finnish decimal comma
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');       // the same inside LaTeX
  const fj = (x) => fi(x, Number.isInteger(x) ? 0 : 1);
  const tj = (x) => tx(x, Number.isInteger(x) ? 0 : 1);        // joules: show a half joule when s has a .5 step
});
