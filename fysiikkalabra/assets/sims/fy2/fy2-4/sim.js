// fy2-4 Hyötysuhde: one device drawn as an energy-flow (Sankey) arrow split into useful power and losses.
// Model: the device has a constant efficiency eta (a typical, rounded value per device type, not a measurement of one
// particular device). Of the power P_o taken in, P_a = eta P_o is useful and P_h = P_o − P_a ends up mostly as heat;
// over a time t the energies are E = P t, so E_a / E_o = P_a / P_o = eta. The arrow's thickness is drawn to scale:
// the input arrow is always 100 px thick, the useful arrow eta · 100 px and the loss arrow (1 − eta) · 100 px.
// Colour carries meaning: warm grey = energy taken in, green = useful, orange = losses (heat); the same in the picture,
// the readout and the legend line. The stripes moving along the arrows show the direction of the flow only; the speed
// select changes the pace of that motion and nothing else. Every canvas text goes through lab(), which pushes its ink
// box to simState.labels. p5.js 1.9 instance mode.
new p5((p) => {
  // typical efficiencies (rounded), slider range of the input power in W, form of the input and of the useful energy
  const DEV = {
    lamppu:   { eta: 0.05, lo: 10,    hi: 100,    step: 5,    def: 60,    inn: 'sahko',    out: 'valo',   loss: 'lampo' },
    ledi:     { eta: 0.30, lo: 2,     hi: 40,     step: 1,    def: 10,    inn: 'sahko',    out: 'valo',   loss: 'lampo' },
    keitin:   { eta: 0.90, lo: 500,   hi: 3000,   step: 100,  def: 2000,  inn: 'sahko',    out: 'vesi',   loss: 'lampo' },
    moottori: { eta: 0.90, lo: 100,   hi: 5000,   step: 100,  def: 1000,  inn: 'sahko',    out: 'liike',  loss: 'lampo' },
    auto:     { eta: 0.25, lo: 10000, hi: 100000, step: 5000, def: 60000, inn: 'bensiini', out: 'liike',  loss: 'lampo' },
    paneeli:  { eta: 0.20, lo: 100,   hi: 2000,   step: 100,  def: 1000,  inn: 'valo',     out: 'sahko',  loss: 'lampo_ym' },
  };
  const ORDER = ['lamppu', 'ledi', 'keitin', 'moottori', 'auto', 'paneeli'];
  const T_DEF = 10;
  const COL = { inA: [227, 220, 203], inB: [201, 194, 178], okA: [178, 242, 187], okB: [43, 138, 62], lossA: [255, 192, 120], lossB: [232, 89, 12], ink: [31, 41, 51] };
  const H = 100, XI = 24, XB0 = 170, XB1 = 270, XEND = 540, XTIP = 574, YT = 105, YL = 250;   // geometry (canvas units)
  let selDev, slPo, slT, selSp, lPo, lT, readout, k = 1, labels = [], phase = 0;

  // --- the physics: the split of the power and of the energy over the time t ---
  const split = (dev, Po, t) => {
    const Pa = dev.eta * Po, Ph = Po - Pa, Eo = Po * t;
    return { Pa, Ph, Eo, Ea: dev.eta * Eo, Eh: Eo - dev.eta * Eo };
  };

  const setRange = (dev) => {
    slPo.elt.min = dev.lo; slPo.elt.max = dev.hi; slPo.elt.step = dev.step; slPo.value(dev.def);
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const ld = p.createElement('label').parent(controls); p.createSpan(__('laite')).parent(ld); selDev = p.createSelect().parent(ld);
    for (const key of ORDER) selDev.option(__('laite_' + key), key);
    const lp = p.createElement('label').parent(controls); lPo = p.createSpan('').parent(lp); slPo = p.createSlider(0, 1, 0, 1).parent(lp);
    const lt = p.createElement('label').parent(controls); lT = p.createSpan('').parent(lt); slT = p.createSlider(1, 600, T_DEF, 1).parent(lt);
    const ls = p.createElement('label').parent(controls); p.createSpan(__('nopeus')).parent(ls); selSp = p.createSelect().parent(ls);
    for (const [txt, v] of [[__('hidas'), 0.5], [__('normaali'), 1], [__('nopea'), 2]]) selSp.option(txt, v);
    selSp.selected('1');                                                  // pace of the flow stripes only
    for (const e of [selDev.elt]) { const f = () => setRange(DEV[selDev.value()]); e.addEventListener('input', f); e.addEventListener('change', f); }
    p.createP(__('nuolet')).parent('sim-root').class('note');
    p.textFont('Arial');
    setRange(DEV.lamppu);
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { laite: { input: selDev.elt, unit: '' }, Po: { input: slPo.elt, unit: 'W' }, t: { input: slT.elt, unit: 's' } },
      reset: () => { selDev.selected('lamppu'); selSp.selected('1'); setRange(DEV.lamppu); slT.value(T_DEF); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const key = selDev.value(), dev = DEV[key], speed = Number(selSp.value());
    const Po = Number(slPo.value()), t = Number(slT.value()), r = split(dev, Po, t);
    phase = (phase + Math.min(p.deltaTime, 100) / 1000 * speed * 60) % 36;
    lPo.html(__('otettu_teho', { P: fP(Po) }));
    lT.html(__('aika', { t: sig(t) }));
    readout.html(__('hyotysuhde', { eta: sig(dev.eta * 100) }) +
      '<br>' + __('tehot', { po: fP(Po), pa: fP(r.Pa), ph: fP(r.Ph) }) +
      '<br>' + __('energiat', { t: sig(t), eo: fE(r.Eo), ea: fE(r.Ea), eh: fE(r.Eh) }));
    window.simState = { laite: key, Po, t, eta: dev.eta, Pa: r.Pa, Ph: r.Ph, Eo: r.Eo, Ea: r.Ea, Eh: r.Eh,
      etaP: r.Pa / Po * 100, etaE: r.Ea / r.Eo * 100, nopeus: speed, labels: null };

    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(13 * k);
    labels = [];
    p.background(250);
    picture(dev, key, Po, r, fh);
    window.simState.labels = labels;
  };

  // --- the picture: three arrows to scale, the device between them, labels ---
  function picture(dev, key, Po, r, fh) {
    const c = p.drawingContext, Ta = H * dev.eta, Th = H - Ta;
    const ok = `M${XB1},${YT} L${XEND},${YT} L${XEND},${YT - 9} L${XTIP},${YT + Ta / 2} L${XEND},${YT + Ta + 9} L${XEND},${YT + Ta} L${XB1},${YT + Ta} Z`;
    const loss = `M${XB1},${YT + Ta} C${XB1 + 70},${YT + Ta} ${XB1 + 70},${YL} ${XB1 + 140},${YL} L${XEND},${YL} L${XEND},${YL - 9} L${XTIP},${YL + Th / 2} ` +
                 `L${XEND},${YL + Th + 9} L${XEND},${YL + Th} L${XB1 + 140},${YL + Th} C${XB1 + 70},${YL + Th} ${XB1 + 70},${YT + H} ${XB1},${YT + H} Z`;
    const inn = `M${XI},${YT} L${XB0 - 22},${YT} L${XB0 - 22},${YT - 9} L${XB0},${YT + H / 2} L${XB0 - 22},${YT + H + 9} L${XB0 - 22},${YT + H} L${XI},${YT + H} Z`;
    arrowFill(inn, XI, XB0, COL.inA, COL.inB);
    arrowFill(ok, XB1, XTIP, COL.okA, COL.okB);
    arrowFill(loss, XB1, XTIP, COL.lossA, COL.lossB);
    // the stripes that show the direction of the flow, clipped to the three arrows
    const all = new Path2D(); for (const d of [inn, ok, loss]) all.addPath(new Path2D(d));
    c.save(); c.clip(all); p.noStroke(); p.fill(255, 255, 255, 80);
    for (let x = -36 + phase; x < 620; x += 36) p.rect(x, 0, 10, 400);
    c.restore();
    for (const d of [inn, ok, loss]) { c.save(); c.strokeStyle = 'rgba(31,41,51,0.55)'; c.lineWidth = 1.5; c.lineJoin = 'round'; c.stroke(new Path2D(d)); c.restore(); }

    // the device: a box with its picture
    p.fill(255); p.stroke(...COL.ink); p.strokeWeight(2); p.rect(XB0, 85, XB1 - XB0, 140, 10);
    icon(key, 220, 155);

    // labels: name, input, useful, losses, efficiency
    lab(`$\\text{${__('laite_' + key)}}$`, 220, 38, 'c', fh);
    lab(`$P_\\text{o} = ${fP(Po)}$`, XI, 90, 'l', fh);
    lab(`$\\text{${__('sisaan_' + dev.inn)}}$`, XI, YT + H + 26, 'l', fh);
    lab(`$P_\\text{a} = ${fP(r.Pa)}\\ (\\text{${__('ulos_' + dev.out)}})$`, 395, YT - 17, 'c', fh, COL.okB);
    lab(`$P_\\text{h} = ${fP(r.Ph)}\\ (\\text{${__(dev.loss)}})$`, 395, YL + Th + 34, 'c', fh, [190, 66, 8]);
    lab(`$\\eta = ${sig(dev.eta * 100)}\\,\\%$`, 220, 274, 'c', fh);
  }

  // a filled arrow outline with a horizontal gradient and no stroke yet (the stroke is drawn after the stripes)
  function arrowFill(d, x0, x1, a, b) {
    const c = p.drawingContext; c.save();
    const g = c.createLinearGradient(x0, 0, x1, 0);
    g.addColorStop(0, `rgb(${a.join(',')})`); g.addColorStop(1, `rgb(${b.join(',')})`);
    c.fillStyle = g; c.fill(new Path2D(d)); c.restore();
  }

  // --- the six device pictures (about 70 px, centred on cx, cy) ---
  function icon(key, cx, cy) {
    p.strokeJoin(p.ROUND);
    if (key === 'lamppu' || key === 'ledi') {
      p.stroke(...COL.ink); p.strokeWeight(2); p.fill(238, 245, 249); p.circle(cx, cy - 12, 52);
      if (key === 'lamppu') {                                           // glowing filament
        p.noFill(); p.stroke(232, 89, 12); p.strokeWeight(2.5);
        p.beginShape(); for (let i = 0; i <= 6; i++) p.vertex(cx - 12 + i * 4, cy - 14 + (i % 2 ? 7 : -7)); p.endShape();
      } else {                                                          // three LED chips
        p.stroke(...COL.ink); p.strokeWeight(1.5); p.fill(255, 224, 130);
        for (const dx of [-14, 0, 14]) p.rect(cx + dx - 5, cy - 20, 10, 12, 2);
      }
      p.stroke(...COL.ink); p.strokeWeight(2); p.fill(196, 204, 212); p.rect(cx - 13, cy + 14, 26, 22, 3);
      p.strokeWeight(1.5); p.line(cx - 13, cy + 22, cx + 13, cy + 22); p.line(cx - 13, cy + 29, cx + 13, cy + 29);
    } else if (key === 'keitin') {                                      // kettle with a spout and a handle
      p.stroke(...COL.ink); p.strokeWeight(2); p.fill(196, 204, 212);
      p.quad(cx - 22, cy + 26, cx + 22, cy + 26, cx + 17, cy - 22, cx - 17, cy - 22);
      p.triangle(cx - 22, cy - 14, cx - 36, cy - 24, cx - 20, cy - 4);
      p.noFill(); p.strokeWeight(3); p.arc(cx + 20, cy + 2, 26, 36, -p.HALF_PI, p.HALF_PI);
      p.fill(169, 209, 240); p.strokeWeight(1.5); p.rect(cx - 12, cy - 30, 24, 8, 3);
    } else if (key === 'moottori') {                                    // electric motor: housing, shaft, a turning mark
      p.stroke(...COL.ink); p.strokeWeight(2); p.fill(196, 204, 212); p.rect(cx + 20, cy - 4, 22, 8);
      p.fill(108, 117, 125); p.rect(cx - 36, cy - 24, 56, 48, 6);
      p.fill(184, 98, 45); p.strokeWeight(1.5); for (const dy of [-14, -4, 6]) p.rect(cx - 30, cy + dy, 44, 6, 2);
      const a = phase / 36 * p.TWO_PI; p.stroke(255); p.strokeWeight(2); p.line(cx + 31, cy, cx + 31 + 3 * Math.cos(a), cy + 3 * Math.sin(a));
    } else if (key === 'auto') {                                        // engine block with three cylinders
      p.stroke(...COL.ink); p.strokeWeight(2); p.fill(108, 117, 125); p.rect(cx - 34, cy - 6, 68, 32, 4);
      p.fill(196, 204, 212); for (const dx of [-24, -6, 12]) { p.rect(cx + dx, cy - 26, 14, 22, 2); }
      p.fill(232, 89, 12); p.strokeWeight(1.5); for (const dx of [-24, -6, 12]) p.rect(cx + dx + 2, cy - 12, 10, 8, 1);
    } else {                                                            // solar panel on a stand
      p.stroke(...COL.ink); p.strokeWeight(2); p.fill(28, 95, 168);
      p.quad(cx - 30, cy + 14, cx + 30, cy + 14, cx + 40, cy - 22, cx - 20, cy - 22);
      p.stroke(255); p.strokeWeight(1.2);
      for (let i = 1; i < 4; i++) p.line(cx - 30 + i * 15, cy + 14, cx - 20 + i * 15, cy - 22);
      p.line(cx - 25, cy - 4, cx + 35, cy - 4);
      p.stroke(...COL.ink); p.strokeWeight(2.5); p.line(cx, cy + 14, cx, cy + 30); p.line(cx - 14, cy + 30, cx + 14, cy + 30);
    }
  }

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }

  // numbers inside LaTeX: three significant figures, decimal comma as {,}; powers and energies with a fitting unit
  const sig = (x) => String(parseFloat(Number(x).toPrecision(3))).replace('.', '{,}');
  const fP = (w) => (w >= 1000 ? `${sig(w / 1000)}\\,\\text{kW}` : `${sig(w)}\\,\\text{W}`);
  const fE = (j) => (j >= 1e6 ? `${sig(j / 1e6)}\\,\\text{MJ}` : j >= 1000 ? `${sig(j / 1000)}\\,\\text{kJ}` : `${sig(j)}\\,\\text{J}`);
});
