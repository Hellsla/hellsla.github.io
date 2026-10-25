// fy3-11 Kaasun tekemä työ ja lämpövoimakone: an energy-flow (Sankey) diagram of a heat engine or a heat pump.
// Physics (powers, i.e. energy per second; values in MW or kW, the mode's unit):
//   heat engine: the fuel power Pin enters; the useful power (electricity or mechanical work) is Puse = ηPin,
//     district heat (CHP only) Pheat = hPin with η + h ≤ 95 %, and the rest leaves as waste heat Pwaste = Pin − Puse − Pheat.
//     Energy is conserved: Pin = Puse + Pheat + Pwaste. Total efficiency ηtot = (Puse + Pheat)/Pin = η + h.
//   heat pump: electric power Pel in, heat delivered inside Pout = cop·Pel (cop = lämpökerroin), heat taken from the
//     outdoor air Pambient = Pout − Pel, so Pel + Pambient = Pout: the pump moves heat, it does not create energy.
// Drawing: arrow width ∝ power; the total (Pin, or Pout for the pump) gets the full width W, so the diagram always fills
// its area, and the header key prints the scale. Colours: hot fuel red, electricity/work yellow, useful heat orange-red,
// waste and outdoor heat cool blue. Each label sits beside its arrow end in a slot at least as tall as the label, so thin
// flows keep readable labels. eta, etaTotal in percent. p5.js 1.9 instance mode, 600×400 canvas inside #sim-root.
// Exposes window.simState every frame and window.simDebug with the ink box of every canvas text (overlap checks).
new p5((p) => {
  const CAP = 95;                                                      // CHP: electricity + district heat ≤ 95 % of fuel
  const XA = 140, XI = 152, BX0 = 196, BX1 = 336, XC = 384, XH = 396, YB = 394, GAP = 8;   // x stations of the diagram (px)
  const COL = { fuel: [200, 60, 35], el: [238, 186, 20], dh: [240, 125, 40], waste: [110, 160, 205], amb: [80, 170, 230], inside: [220, 75, 50] };
  const MODES = {
    lauhdevoimalaitos: { unit: 'MW', P: [100, 2000, 10, 1000], eta: 40, use: 'sähkö' },
    yhteistuotanto: { text: 'yhteistuotantovoimalaitos', unit: 'MW', P: [100, 2000, 10, 1000], eta: 30, heat: 55, use: 'sähkö' },
    automoottori: { unit: 'kW', P: [10, 200, 1, 60], eta: 30, use: 'mekaaninen työ' },
    ilmalämpöpumppu: { unit: 'kW', P: [0.5, 5, 0.1, 1], cop: 3 } };
  let sel, sP, lP, sE, lE, sH, lH, sC, lC, readout, mode = '', last = 'eta', t = 0, k = 1, boxes = {};

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent), span = p.createSpan('').parent(label);
    return [p.createSlider(min, max, val, step).parent(label), span];
  };
  const preset = () => {                                               // a new situation gets its typical values
    mode = sel.value(); last = 'eta';
    const m = MODES[mode], [a, b, st, v] = m.P; sP.elt.min = a; sP.elt.max = b; sP.elt.step = st; sP.value(v);
    if (m.eta) sE.value(m.eta); sH.value(m.heat || 0); if (m.cop) sC.value(m.cop);
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const ls = p.createElement('label').parent(controls); p.createSpan('Tilanne').parent(ls); sel = p.createSelect().parent(ls);
    for (const [v, m] of Object.entries(MODES)) sel.option(m.text || v, v);
    sel.elt.addEventListener('change', preset);
    [sP, lP] = slider(controls, 100, 2000, 1000, 10); [sE, lE] = slider(controls, 10, 60, 40, 1);   // input power, η (%)
    [sH, lH] = slider(controls, 0, 65, 55, 1); [sC, lC] = slider(controls, 1.5, 5, 3, 0.1);          // district heat share (%), cop
    sE.elt.addEventListener('input', () => { last = 'eta'; }); sH.elt.addEventListener('input', () => { last = 'heat'; });   // CHP cap moves the other one
    p.createP('Nuolen leveys on verrannollinen tehoon. Kokonaisteho täyttää aina koko kaavion, joten asteikko vaihtuu; ' +
              'se näkyy kankaan ylälaidassa. Yhteistuotannossa sähkön ja kaukolämmön osuus on yhteensä enintään 95 %.')
      .parent('sim-root').class('note');
    preset(); p.textFont('Arial');
  };

  p.draw = () => {
    if (sel.value() !== mode) preset();
    const m = MODES[mode], u = m.unit, pump = !!m.cop, chp = mode === 'yhteistuotanto';
    t += Math.min(p.deltaTime, 100) / 1000;
    for (const [l, on] of [[lE, !pump], [lH, chp], [lC, pump]]) l.elt.parentElement.style.display = on ? '' : 'none';
    const P = Number(sP.value()), cop = Number(sC.value());
    let eta = Number(sE.value()), h = chp ? Number(sH.value()) : 0;
    if (chp && eta + h > CAP) { if (last === 'heat') { eta = CAP - h; sE.value(eta); } else { h = CAP - eta; sH.value(h); } }
    const n = (x) => `${fs(x)} ${u}`, pc = (x) => `${x} %`;
    let S, ins, outs, lines;
    if (pump) {
      const Pout = cop * P, Pamb = Pout - P;                           // heat inside = cop · electricity, the rest from outdoor air
      S = { Pin: null, eta: null, heatShare: null, Puse: null, Pheat: null, Pwaste: null, etaTotal: null, Pel: P, cop, Pout, Pambient: Pamb, sumIn: P + Pamb, sumOut: Pout };
      ins = [['sähkö', P, COL.el], ['ulkoilman lämpö', Pamb, COL.amb]]; outs = [['lämpö sisälle', Pout, COL.inside]];
      lP.html(`Sähköteho = ${fi(P, 1)} kW`); lC.html(`Lämpökerroin = ${fi(cop, 1)}`);
      lines = [`Sähköteho ${n(P)}, lämpökerroin ${fi(cop, 1)}`,
        `Lämpö sisälle = lämpökerroin · sähköteho = ${fi(cop, 1)} · ${n(P)} = <strong>${n(Pout)}</strong>`,
        `Lämpö ulkoilmasta = ${n(Pout)} − ${n(P)} = <strong>${n(Pamb)}</strong>`,
        `Energia säilyy: sisään ${n(P)} + ${n(Pamb)} = ${n(P + Pamb)} = ulos ${n(Pout)}`,
        'Lämpöpumppu siirtää lämpöä kylmästä ulkoilmasta lämpimään sisätilaan. Se ei luo energiaa: sisälle luovutettu lämpö on ulkoilmasta otetun lämmön ja sähkön summa.'];
    } else {
      const Puse = eta / 100 * P, Pheat = h / 100 * P, Pwaste = P - Puse - Pheat;   // energy conserved: the rest is waste heat
      S = { Pin: P, eta, heatShare: h, Puse, Pheat, Pwaste, etaTotal: eta + h, Pel: null, cop: null, Pout: null, Pambient: null, sumIn: P, sumOut: Puse + Pheat + Pwaste };
      ins = [['polttoaine', P, COL.fuel]];
      outs = [[m.use, Puse, COL.el], ...(chp ? [['kaukolämpö', Pheat, COL.dh]] : []), ['hukkalämpö', Pwaste, COL.waste]];
      lP.html(`Polttoaineen teho = ${fi(P, 0)} ${u}`); lE.html(`${chp ? 'Sähkön osuus, hyötysuhde' : 'Hyötysuhde'} η = ${pc(eta)}`);
      lH.html(`Kaukolämmön osuus = ${pc(h)}`);
      lines = [`Polttoaineen teho ${n(P)}`,
        `${m.use[0].toUpperCase() + m.use.slice(1)} ${n(Puse)}${chp ? `, kaukolämpö ${n(Pheat)}` : ''}, hukkalämpö ympäristöön ${n(Pwaste)}`,
        `Energia säilyy: sisään ${n(P)} = ulos ${outs.map((f) => n(f[1])).join(' + ')} = ${n(S.sumOut)}`,
        chp ? `Sähkön hyötysuhde ${pc(eta)}, kokonaishyötysuhde (${n(Puse)} + ${n(Pheat)}) / ${n(P)} = <strong>${pc(eta + h)}</strong>`
          : `Hyötysuhde η = ${n(Puse)} / ${n(P)} = <strong>${pc(eta)}</strong>`];
    }

    // layout: header (scale key + legend, wrapped into rows), then the widest W for which every slot fits
    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (x) => Math.round(x * k), total = S.sumIn, fh = ts(11), rowH = Math.max(30, Math.round(fh * 1.6));
    const v = nice(total / 8), keyT = `${fv(v)} ${u}`, legend = [...ins, ...outs];
    boxes = {}; p.textSize(fh); p.textStyle(p.NORMAL);
    let hx = 8, row = 0;
    const pos = [['key', p.textWidth('Asteikko:') + 22 + p.textWidth(keyT)], ...legend.map((f) => [f, fh + 6 + p.textWidth(f[0])])]
      .map(([it, w]) => { if (hx + w > 592 && hx > 8) { hx = 8; row++; } const r = [it, hx, row]; hx += w + ts(14); return r; });
    const YT = 10 + (row + 1) * rowH, fz = ts(13), LI = ins.map((f) => lab(f, XA - 12, fz)), LO = outs.map((f) => lab(f, 160, fz));
    const need = (fl, L, w) => fl.reduce((s, f, i) => s + Math.max(f[1] / total * w, L[i].h), 0) + GAP * (fl.length - 1);
    let W = 210; while (W > 60 && Math.max(need(ins, LI, W), need(outs, LO, W), W + 24) > YB - YT) W -= 2;
    const sc = W / total, yc = (YT + YB) / 2;
    const slots = (fl, L) => {                                         // label slots stacked around the centre line
      const hs = fl.map((f, i) => Math.max(f[1] * sc, L[i].h)), T = hs.reduce((a, b) => a + b, 0) + GAP * (fl.length - 1);
      let y = Math.max(YT, Math.min(YB - T, yc - T / 2)), yb = yc - W / 2;
      return fl.map((f, i) => { const w = f[1] * sc, o = { w, top: y + (hs[i] - w) / 2, mid: y + hs[i] / 2, box: yb }; y += hs[i] + GAP; yb += w; return o; });
    };
    const SI = slots(ins, LI), SO = slots(outs, LO), y0 = yc - W / 2 - 12, y1 = yc + W / 2 + 12;

    // background: outdoors cool, indoors warm for the heat pump
    p.background(250); p.noStroke();
    if (pump) { p.fill(226, 239, 250); p.rect(0, 0, BX0 + 84, 400); p.fill(253, 238, 225); p.rect(BX0 + 84, 0, 600, 400); }
    ins.forEach((f, i) => { band(f[2], [[XA, SI[i].top], [XI, SI[i].top], [BX0, SI[i].box]], SI[i].w, false);
      label(`in${i}`, LI[i], XA - 8, SI[i].mid, 'r'); });
    outs.forEach((f, i) => { const end = band(f[2], [[BX1, SO[i].box], [XC, SO[i].top], [XH, SO[i].top]], SO[i].w, true);
      label(`out${i}`, LO[i], end + 8, SO[i].mid, 'l'); });
    if (pump) heatPump(BX0, y0, BX1, y1); else if (mode === 'automoottori') engine(BX0, y0, BX1, y1); else plant(BX0, y0, BX1, y1, chp);

    // header: scale key (a bar as wide as v) and the colour legend
    for (const [it, x, r] of pos) {
      const cy = 4 + rowH * (r + 0.5), by = cy + fh * 0.36;
      if (it !== 'key') { p.fill(it[2]); p.stroke(80); p.strokeWeight(1); p.rect(x, cy - fh / 2, fh, fh, 2); say(`leg-${it[0]}`, it[0], fh, x + fh + 6, by, 'l'); continue; }
      say('key', 'Asteikko:', fh, x, by, 'l');
      const bx = boxes.key[1] + 8; p.fill(90); p.noStroke(); p.rect(bx, cy - v * sc / 2, 6, v * sc); say('keyValue', keyT, fh, bx + 14, by, 'l');
    }
    lines.push(`Asteikko: nuolen leveys on verrannollinen tehoon, kokonaisteho ${n(total)} on koko kaavion levyinen ja avainpalkki on ${fv(v)} ${u}.`);
    readout.html(lines.join('<br>'));
    window.simState = { mode, unit: u, ...S, scale: sc, scaleKey: v, bandTotal: W, labels: [...LI, ...LO].map((L) => L.lines.join(' ')) };
    window.simDebug = { boxes, k, W, YT };
  };

  // one flow: a ribbon of width w through the key points [x, top] (smooth steps between them), moving chevrons on it,
  // an arrowhead at the end of an output; returns the x where the arrow ends. A zero flow is a thin dashed line.
  function band(col, keys, w, head) {
    const top = (x) => { for (let i = 1; i < keys.length; i++) if (x <= keys[i][0] || i === keys.length - 1) {
      const [xa, ya] = keys[i - 1], [xb, yb] = keys[i], s = Math.min(1, Math.max(0, (x - xa) / (xb - xa)));
      return ya + (yb - ya) * s * s * (3 - 2 * s); } };
    const xa = keys[0][0], xb = keys[keys.length - 1][0], xs = [];
    for (let x = xa; x < xb; x += 3) xs.push(x); xs.push(xb);
    if (w < 0.8) { p.noFill(); p.stroke(col); p.strokeWeight(1.5); p.drawingContext.setLineDash([4, 4]);
      p.beginShape(); xs.forEach((x) => p.vertex(x, top(x))); p.endShape(); p.drawingContext.setLineDash([]); return xb + 4; }
    const hl = Math.min(30, 10 + w / 5), e = Math.min(8, 3 + w / 10), yt = top(xb);
    p.fill(col); p.stroke(col.map((c) => c * 0.7)); p.strokeWeight(1);
    p.beginShape(); xs.forEach((x) => p.vertex(x, top(x)));
    if (head) { p.vertex(xb, yt - e); p.vertex(xb + hl, yt + w / 2); p.vertex(xb, yt + w + e); }
    [...xs].reverse().forEach((x) => p.vertex(x, top(x) + w)); p.endShape(p.CLOSE);
    if (w >= 4) {                                                       // chevrons drift in the direction of the flow
      const c = Math.min(9, w / 2); p.noStroke(); p.fill(255, 255, 255, 95);
      for (let x = xa + ((t * 40) % 28); x + 6 + c < xb; x += 28) {
        const a = top(x), b = top(x + c), mm = (a + b) / 2;
        p.quad(x, a + 1, x + 5, a + 1, x + 5 + c, mm + w / 2, x + c, mm + w / 2); p.quad(x + c, mm + w / 2, x + 5 + c, mm + w / 2, x + 5, a + w - 1, x, a + w - 1);
      }
    }
    return head ? xb + hl : xb;
  }
  // a label: name (wrapped to maxW, the font shrinks if one word does not fit) and the value in bold on its own line
  function lab([name, P], maxW, size) {
    for (const unit = MODES[mode].unit; ; size--) {
      p.textSize(size); p.textStyle(p.NORMAL); const lines = [];
      for (const wd of name.split(' ')) { const tt = lines.length ? `${lines[lines.length - 1]} ${wd}` : wd;
        if (lines.length && p.textWidth(tt) <= maxW) lines[lines.length - 1] = tt; else lines.push(wd); }
      const ok = lines.every((s) => p.textWidth(s) <= maxW); p.textStyle(p.BOLD);
      const val = `${fs(P)} ${unit}`, fit = ok && p.textWidth(val) <= maxW; p.textStyle(p.NORMAL); lines.push(val);
      if (fit || size <= 9) return { lines, size, h: (lines.length - 1) * Math.round(size * 1.2) + 1.25 * size };
    }
  }
  function label(name, L, x, mid, align) {
    let y = mid - L.h / 2 + L.size;
    L.lines.forEach((s, i) => { say(`${name}-${i}`, s, L.size, x, y, align, i === L.lines.length - 1); y += Math.round(L.size * 1.2); });
  }
  // text with a halo, its ink box recorded in boxes[name]
  function say(name, s, size, x, y, align, bold) {
    p.textSize(size); p.textStyle(bold ? p.BOLD : p.NORMAL); p.textAlign(p.LEFT, p.BASELINE);
    const mt = p.drawingContext.measureText(s), lx = align === 'r' ? x - mt.width : x;
    p.stroke(255, 255, 255, 200); p.strokeWeight(3 * k); p.strokeJoin(p.ROUND); p.fill(35);
    p.text(s, lx, y); p.noStroke(); p.text(s, lx, y); p.textStyle(p.NORMAL);
    boxes[name] = [lx - mt.actualBoundingBoxLeft, lx + mt.actualBoundingBoxRight, y - mt.actualBoundingBoxAscent, y + mt.actualBoundingBoxDescent];
  }
  // gradient fill (raw canvas, inside save/restore so p5's own fill state is untouched) with a thin outline
  function grad(stops, xa, ya, xb, yb, path) {
    const c = p.drawingContext; c.save(); const g = c.createLinearGradient(xa, ya, xb, yb);
    stops.forEach((s, i) => g.addColorStop(i / (stops.length - 1), `rgba(${s.length === 3 ? [...s, 1] : s})`));
    c.fillStyle = g; c.strokeStyle = 'rgba(0,0,0,0.35)'; c.lineWidth = 1; c.beginPath(); path(c); c.fill(); c.stroke(); c.restore();
  }
  const grect = (x, y, w, h, stops, horiz, r = 4) => grad(stops, x, y, horiz ? x + w : x, horiz ? y : y + h, (c) => c.roundRect(x, y, w, h, r));
  const METAL = [[95, 98, 108], [175, 180, 190], [95, 98, 108]];

  // power plant: boiler with flames → steam pipe → turbine → generator; turbine exhaust → condenser cooled by sea water
  function plant(x0, y0, x1, y1, chp) {
    const h = y1 - y0, bx = x0 + 2, by = y0 + 0.1 * h, ty = y0 + 0.2 * h, cy = y0 + 0.52 * h;
    p.noFill(); p.strokeWeight(5); p.stroke(205, 205, 212);
    p.beginShape(); p.vertex(bx + 25, by); p.vertex(bx + 25, y0 + 3); p.vertex(x0 + 66, y0 + 3); p.vertex(x0 + 66, ty); p.endShape();
    p.line(x0 + 90, ty, x0 + 90, cy); p.stroke(70, 130, 200); p.line(x0 + 62, y1 - 12, bx + 50, y1 - 12);   // exhaust steam down, feed water back
    grect(bx, by, 50, y1 - by - 2, METAL, true);
    grect(bx + 6, y1 - 0.38 * h, 38, 0.38 * h - 8, [[40, 15, 10], [110, 35, 15]]);
    for (let i = 0; i < 3; i++) {                                       // flames flicker (deterministic)
      const fx = bx + 13 + 12 * i, base = y1 - 10, fl = 0.28 * h * (0.75 + 0.25 * Math.sin(9 * t + 2.1 * i));
      grad([[255, 245, 160], [255, 150, 30], [210, 40, 20, 0.6]], 0, base, 0, base - fl, (c) => { c.moveTo(fx - 6, base);
        c.bezierCurveTo(fx - 7, base - fl * 0.5, fx, base - fl * 0.6, fx, base - fl); c.bezierCurveTo(fx, base - fl * 0.6, fx + 7, base - fl * 0.5, fx + 6, base); });
    }
    grad(METAL, 0, ty - 0.17 * h, 0, ty + 0.17 * h, (c) => { c.moveTo(x0 + 60, ty - 0.08 * h); c.lineTo(x0 + 98, ty - 0.16 * h); c.lineTo(x0 + 98, ty + 0.16 * h); c.lineTo(x0 + 60, ty + 0.08 * h); c.closePath(); });
    p.stroke(60, 60, 70, 150); p.strokeWeight(1.5);                     // turbine blades sweep by
    for (let j = 0; j < 4; j++) { const xx = x0 + 61 + ((t * 50 + 9.5 * j) % 36), hh = 0.08 * h + (xx - x0 - 60) / 38 * 0.08 * h; p.line(xx, ty - hh + 2, xx, ty + hh - 2); }
    p.stroke(80); p.strokeWeight(4); p.line(x0 + 98, ty, x0 + 104, ty); grect(x0 + 104, ty - 0.13 * h, x1 - x0 - 106, 0.26 * h, [[170, 130, 30], [245, 210, 90], [170, 130, 30]]);
    const gx = x0 + 104 + (x1 - x0 - 106) / 2, s = 0.1 * h; p.fill(255, 250, 220); p.stroke(120, 90, 0); p.strokeWeight(1);   // lightning bolt
    p.beginShape(); for (const [a, b] of [[0.2, -1], [-0.5, 0.15], [0, 0.15], [-0.2, 1], [0.5, -0.15], [0, -0.15]]) p.vertex(gx + a * s, ty + b * s); p.endShape(p.CLOSE);
    grect(x0 + 58, cy, x1 - x0 - 60, y1 - cy - 2, [[150, 155, 165], [110, 115, 125]]);
    const sy = chp ? cy + 0.45 * (y1 - cy) : cy + 8;                    // CHP: upper part heats district-heating water
    if (chp) grect(x0 + 62, cy + 4, x1 - x0 - 68, sy - cy - 8, [[250, 170, 90], [225, 105, 40]]);
    grect(x0 + 62, sy, x1 - x0 - 68, y1 - sy - 6, [[120, 190, 235], [30, 90, 170]]);
    p.noFill(); p.stroke(255, 255, 255, 170); p.strokeWeight(1.5);       // sea water flowing through
    for (let r = 0; r < 3; r++) { const wy = sy + (r + 1) * (y1 - sy - 6) / 4; p.beginShape();
      for (let x = x0 + 64; x <= x1 - 8; x += 3) p.vertex(x, wy + 2 * Math.sin((x - x0) / 7 - 4 * t)); p.endShape(); }
  }
  // car engine: three cylinders with pistons, flywheel (work), exhaust pipe with hot gas puffs (waste heat)
  function engine(x0, y0, x1, y1) {
    const h = y1 - y0, ex = x0 + 18, ew = x1 - x0 - 58, et = y0 + 0.24 * h, eb = y1 - 0.16 * h, fy = y0 + 0.18 * h, fr = Math.min(20, 0.11 * h);
    p.stroke(150, 60, 30); p.strokeWeight(3); p.line(x0, (y0 + y1) / 2, ex, (y0 + y1) / 2);    // fuel line
    p.stroke(90); p.strokeWeight(5); p.line(ex + ew, eb - 0.12 * h, x1, eb - 0.12 * h);          // exhaust pipe
    p.stroke(60); p.strokeWeight(2); p.line(ex + ew - 6, fy, x1 - 20, fy);                       // belt to the flywheel
    grect(ex, et, ew, eb - et, [[120, 124, 132], [80, 84, 92]], true, 6);
    const cw = (ew - 16) / 3, ch = (eb - et) * 0.62;
    for (let i = 0; i < 3; i++) {
      const cx = ex + 4 + i * (cw + 4), ph = Math.sin(8 * t + 2.1 * i), py = et + 6 + (ch - 22) * (0.5 + 0.5 * ph);
      p.noStroke(); p.fill(35); p.rect(cx, et + 4, cw, ch, 2);
      p.fill(255, 140, 30, 230 * Math.max(0, -ph)); p.rect(cx + 1, et + 5, cw - 2, py - et - 5);    // combustion near the top
      grect(cx + 1, py, cw - 2, 14, METAL, true, 2);
      p.stroke(200); p.strokeWeight(3); p.line(cx + cw / 2, py + 14, cx + cw / 2, eb - 8);
    }
    p.stroke(200); p.strokeWeight(4); p.line(ex + 4, eb - 8, ex + ew - 4, eb - 8); grad([[200, 200, 210], [90, 92, 100]], x1 - 20 - fr, fy - fr, x1 - 20 + fr, fy + fr, (c) => c.arc(x1 - 20, fy, fr, 0, 2 * Math.PI));
    p.stroke(50); p.strokeWeight(2); for (let j = 0; j < 3; j++) { const a = 5 * t + j * 2.094; p.line(x1 - 20, fy, x1 - 20 + fr * Math.cos(a), fy + fr * Math.sin(a)); }
    p.noStroke(); for (let j = 0; j < 3; j++) { const s = ((t * 0.8 + j / 3) % 1); p.fill(160, 150, 145, 160 * (1 - s)); p.circle(x1 - 30 + 30 * s, eb - 0.12 * h - 8 * s, 6 + 12 * s); }
  }
  // air-source heat pump: outdoor unit with a fan, refrigerant pipes through the wall, indoor unit releasing warm air
  function heatPump(x0, y0, x1, y1) {
    const h = y1 - y0, xw = x0 + 84, ut = y0 + 0.22 * h, ub = y1 - 0.12 * h, ix = x1 - 24;
    p.strokeWeight(4); p.stroke(215, 70, 50); p.line(x0 + 60, ut + 8, ix, ut + 8); p.stroke(60, 120, 210); p.line(x0 + 60, ut + 18, ix, ut + 18);
    grect(xw, 4, 10, 392, [[170, 95, 70], [205, 130, 100], [170, 95, 70]], true, 1);          // house wall
    grect(x0, ut, 72, ub - ut, [[240, 242, 246], [190, 195, 205]], false, 5);
    const fx = x0 + 36, fyc = (ut + ub) / 2, fr = Math.min(30, (ub - ut) / 2 - 6);
    p.fill(70, 75, 85); p.noStroke(); p.circle(fx, fyc, 2 * fr);
    p.fill(170, 205, 230); for (let j = 0; j < 3; j++) { p.push(); p.translate(fx, fyc); p.rotate(6 * t + j * 2.094); p.ellipse(fr * 0.5, 0, fr * 0.9, fr * 0.38); p.pop(); }
    p.noFill(); p.stroke(220); p.strokeWeight(1.5); p.circle(fx, fyc, 2 * fr); p.circle(fx, fyc, fr);
    grect(ix, y0 + 4, 22, h - 8, [[255, 255, 255], [225, 220, 215]], true, 4);
    p.noFill(); p.stroke(225, 90, 50, 150); p.strokeWeight(1.5);         // warm air rising beside the indoor unit
    for (let j = 0; j < 2; j++) { p.beginShape(); for (let y = y1 - 6; y > y0 + 6; y -= 3) p.vertex(ix - 8 - 8 * j + 3 * Math.sin(y / 9 + 4 * t + j), y); p.endShape(); }
  }
  const nice = (x) => { const e = 10 ** Math.floor(Math.log10(x)); return [5, 2.5, 2, 1].map((c) => c * e).find((c) => c <= x * (1 + 1e-9)); };
  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');                    // Finnish decimal comma and minus sign
  const fs = (x) => (Math.abs(x) < 1e-9 ? '0' : fi(x, Math.max(0, 2 - Math.floor(Math.log10(Math.abs(x)) + 1e-9))));   // 3 significant figures
  const fv = (x) => String(+x.toPrecision(3)).replace('.', ',');                             // scale key value
});
