// fy3-4 Paine ja hydrostaattinen paine: a pressure gauge sinks into a pool, and a (h, p) chart shows the line.
// Physics: at depth h in a liquid of density ρ the pressure is p = p₀ + ρgh, with p₀ = 101 kPa (air pressure on
// the surface) and g = 9,81 m/s². The term ρgh is the hydrostatic pressure (ylipaine): the weight of the liquid
// column above the gauge divided by its area. The (h, p) graph is a straight line with slope ρg and intercept p₀;
// with "Näytä vain ylipaine" the chart drops the constant term and the line passes through the origin.
// The chart's p axis is scaled to the line shown over 0–20 m at the current density (rounded up to a round
// number) and the scale is printed on the axis. The readout is DOM text; the canvas only draws.
// p5.js 1.9 instance mode, 600×400 canvas inside #sim-root. Exposes window.simState every frame.
new p5((p) => {
  const P0 = 101, G = 9.81, H_MAX = 20;                       // air pressure (kPa), g (m/s²), deepest gauge position (m)
  const TANK = { x: 70, w: 160, top: 70, bottom: 370 };       // pool: 20 m over 300 px
  const CH = { x0: 330, x1: 575, y0: 345, y1: 60 };           // chart area (axes at x0 and y0)
  const LIQUIDS = { 720: 'bensiini', 1000: 'vesi', 1025: 'merivesi', 1240: 'Kuolleenmeren vesi' };
  let sH, lH, sR, lR, cb, readout;

  const slider = (parent, min, max, val, step) => {
    const label = p.createElement('label').parent(parent);
    const span = p.createSpan('').parent(label);
    const s = p.createSlider(min, max, val, step).parent(label);
    return [s, span];
  };
  // round axis maximum: the smallest of 10, 20, 25, 50, 100 kPa steps that needs at most 6 steps
  const niceMax = (v) => { for (const st of [10, 20, 25, 50, 100]) if (Math.ceil(v / st) <= 6) return [Math.ceil(v / st) * st, st]; return [Math.ceil(v / 100) * 100, 100]; };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    [sH, lH] = slider(controls, 0, H_MAX, 10, 0.5);           // syvyys h (m)
    [sR, lR] = slider(controls, 700, 1300, 1000, 5);          // tiheys ρ (kg/m³)
    const lc = p.createElement('label').parent(controls).style('flex-direction', 'row').style('align-items', 'center').style('gap', '.6rem').style('min-height', '40px');
    cb = p.createElement('input').attribute('type', 'checkbox').parent(lc).style('width', '24px').style('height', '24px').style('margin', '0');
    p.createSpan('Näytä vain ylipaine').parent(lc);
    p.createP('Paine kasvaa syvyyden mukana tasaisesti: jokainen metri lisää painetta ρg:n verran. Suoran kulmakerroin riippuu tiheydestä, mutta pinnalla paine on aina ilmanpaine.')
      .parent('sim-root').class('note');
    p.textFont('Arial');
  };

  p.draw = () => {
    const h = Number(sH.value()), rho = Number(sR.value()), overOnly = cb.elt.checked;
    const slope = rho * G / 1000;                              // ρg in kPa per metre
    const pOver = slope * h;                                   // hydrostatic pressure ρgh (kPa)
    const pTotal = P0 + pOver;                                 // total pressure p₀ + ρgh (kPa)
    const ratio = pTotal / P0;                                 // how many times the air pressure
    const base = overOnly ? 0 : P0;                            // constant term of the line shown in the chart
    const [pMax, step] = niceMax(base + slope * H_MAX);        // chart scale: the line at 20 m, rounded up
    const name = LIQUIDS[rho] ? ` (${LIQUIDS[rho]})` : '';
    lH.html(`Syvyys h = ${fi(h, 1)} m`); lR.html(`Tiheys ρ = ${rho} kg/m³${name}`);
    readout.html(`Syvyys h = ${fi(h, 1)} m, tiheys ρ = ${rho} kg/m³` +
                 `<br>Hydrostaattinen paine ρgh = <strong>${fi(pOver, 1)} kPa</strong>` +
                 `<br>Kokonaispaine p = p₀ + ρgh = 101 kPa + ${fi(pOver, 1)} kPa = <strong>${fi(pTotal, 1)} kPa</strong>` +
                 `<br>Kokonaispaine on <strong>${fi(ratio, 2)}</strong> kertaa ilmanpaine.` +
                 `<br>Kuvaajan asteikko 0–${pMax} kPa, kulmakerroin ρg = ${fi(slope, 2)} kPa/m.`);
    window.simState = { h, rho, pOver, pTotal, ratio, overOnly, p0: P0, g: G, slope, chartBase: base, chartValue: base + pOver, pMax };

    const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
    const ts = (n) => Math.round(n * k);
    p.background(250);

    // pool: air above, liquid below (darker for denser liquid), depth scale on the left
    const PXM = (TANK.bottom - TANK.top) / H_MAX, gy = TANK.top + h * PXM, gx = TANK.x + TANK.w / 2;
    p.noStroke(); p.fill(60 - (rho - 700) / 20, 140 - (rho - 700) / 12, 210, 150); p.rect(TANK.x, TANK.top, TANK.w, TANK.bottom - TANK.top);
    p.fill(255, 255, 255, 90); p.rect(gx - 18, TANK.top, 36, gy - TANK.top);           // liquid column above the gauge
    p.stroke(255); p.strokeWeight(1.5); p.drawingContext.setLineDash([5, 4]); p.noFill(); p.rect(gx - 18, TANK.top, 36, gy - TANK.top); p.drawingContext.setLineDash([]);
    p.stroke(60); p.strokeWeight(3); p.line(TANK.x, TANK.top - 30, TANK.x, TANK.bottom); p.line(TANK.x, TANK.bottom, TANK.x + TANK.w, TANK.bottom); p.line(TANK.x + TANK.w, TANK.bottom, TANK.x + TANK.w, TANK.top - 30);
    p.stroke(30, 80, 160); p.strokeWeight(2); p.line(TANK.x, TANK.top, TANK.x + TANK.w, TANK.top);   // surface
    p.noStroke(); p.fill(60); p.textSize(ts(12)); p.textAlign(p.LEFT); p.text('ilma, p₀ = 101 kPa', 12, TANK.top - 40);
    p.textAlign(p.RIGHT); p.textSize(ts(11));
    for (let d = 0; d <= H_MAX; d += 5) { const y = TANK.top + d * PXM; p.stroke(60); p.strokeWeight(1.5); p.line(TANK.x - 6, y, TANK.x, y); p.noStroke(); p.text(`${d} m`, TANK.x - 9, y + ts(4)); }

    // gauge on a cable; arrows from four sides, length grows with the total pressure (pressure acts in every direction)
    p.stroke(80); p.strokeWeight(1.5); p.line(gx, TANK.top - 30, gx, gy - 10);
    const L = 8 + 20 * pTotal / 360;
    p.stroke(200, 40, 40); p.strokeWeight(2.5); p.fill(200, 40, 40);
    for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      const ex = gx + dx * 12, ey = gy + dy * 12, sx = ex + dx * L, sy = ey + dy * L;
      if (sy > TANK.bottom) continue;                          // no arrow through the floor when the gauge rests on it
      p.line(sx, sy, ex + dx * 5, ey + dy * 5);
      p.triangle(ex, ey, ex + dx * 6 - dy * 4, ey + dy * 6 - dx * 4, ex + dx * 6 + dy * 4, ey + dy * 6 + dx * 4);
    }
    p.stroke(40); p.strokeWeight(2); p.fill(240); p.circle(gx, gy, 20);
    // depth bracket on the right of the pool
    const bx = TANK.x + TANK.w + 12;
    p.stroke(60); p.strokeWeight(1.5); p.line(bx, TANK.top, bx, gy); p.line(bx - 4, TANK.top, bx + 4, TANK.top); p.line(bx - 4, gy, bx + 4, gy);
    p.noStroke(); p.fill(60); p.textAlign(p.LEFT); p.textSize(ts(13)); p.text('h', bx + 6, (TANK.top + gy) / 2 + ts(5));

    // (h, p) chart scaled to the line shown; p₀ marked as a dashed line when the constant term is included
    const X = (hh) => CH.x0 + (CH.x1 - CH.x0) * hh / H_MAX, Y = (pp) => CH.y0 - (CH.y0 - CH.y1) * pp / pMax;
    p.stroke(225); p.strokeWeight(1);
    for (let v = step; v <= pMax; v += step) p.line(CH.x0, Y(v), CH.x1, Y(v));
    p.stroke(60); p.strokeWeight(2); p.line(CH.x0, CH.y0, CH.x1, CH.y0); p.line(CH.x0, CH.y0, CH.x0, CH.y1 - 5);
    p.noStroke(); p.fill(60); p.textSize(ts(11)); p.textAlign(p.RIGHT);
    for (let v = 0; v <= pMax; v += step) p.text(`${v}`, CH.x0 - 6, Y(v) + ts(4));
    p.textAlign(p.CENTER);
    for (let d = 0; d <= H_MAX; d += 5) p.text(`${d}`, X(d), CH.y0 + ts(16));
    p.textAlign(p.RIGHT); p.text('h (m)', CH.x1 - 8, CH.y0 - 8);                // a few px left of the h = 20 m guide line
    p.textAlign(p.LEFT); p.textSize(ts(12)); p.text(overOnly ? 'ylipaine ρgh (kPa)' : 'paine p (kPa)', CH.x0 - 26, CH.y1 - ts(14));
    // current gauge reading: its label goes above-left of the rising line, or below-right near h = 0; below-right it
    // never goes under the h axis (its tick labels): the baseline stays above the axis and the label moves right until
    // the rising line clears its top edge
    const px = X(h), py = Y(base + pOver), txt = `${fi(base + pOver, 0)} kPa`;
    const up = h > 4;
    p.textSize(ts(12));
    let lx, ly;
    if (up) { lx = px - 10; ly = Math.max(CH.y1 + ts(12), py - 10); }
    else {
      ly = Math.min(py + ts(16), CH.y0 - 6);
      const rise = (CH.y0 - CH.y1) / pMax * slope / ((CH.x1 - CH.x0) / H_MAX);   // px the line rises per px to the right
      lx = px + Math.max(10, (py - ly + ts(12) + 4) / rise);
    }
    const lw = p.textWidth(txt), box = up ? [lx - lw, lx, ly - ts(12), ly + 3] : [lx, lx + lw, ly - ts(12), ly + 3];
    if (!overOnly) {
      p.stroke(110); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(CH.x0, Y(P0), CH.x1, Y(P0)); p.drawingContext.setLineDash([]);
      // p₀ label on the dashed line, clear of the reading and of the red guide lines: at the right end (below the line,
      // else above it, else one line higher) while the gauge is shallow, at the left end below the line when it is deep
      p.noStroke(); p.fill(90); p.textSize(ts(11));
      const t0 = 'p₀ = 101 kPa', w0 = p.textWidth(t0);
      const spots = h <= 10 ? [[CH.x1 - 4 - w0, Y(P0) + ts(16)], [CH.x1 - 4 - w0, Y(P0) - 6], [CH.x1 - 4 - w0, Y(P0) - 6 - ts(14)]] : [[CH.x0 + 6, Y(P0) + ts(16)]];
      const free = ([x, y]) => x + w0 < box[0] || x > box[1] || y + 3 < box[2] || y - ts(11) > box[3];
      const [x0, y0] = spots.find(free) || spots[spots.length - 1];
      p.textAlign(p.LEFT); p.text(t0, x0, y0);
    }
    p.stroke(30, 80, 160); p.strokeWeight(3); p.line(X(0), Y(base), X(H_MAX), Y(base + slope * H_MAX));
    p.stroke(200, 40, 40); p.strokeWeight(1.5); p.drawingContext.setLineDash([4, 4]); p.line(px, py, px, CH.y0); p.line(CH.x0, py, px, py); p.drawingContext.setLineDash([]);
    p.noStroke(); p.fill(200, 40, 40); p.circle(px, py, 12);
    p.textSize(ts(12)); p.textAlign(up ? p.RIGHT : p.LEFT); p.text(txt, lx, ly);
  };

  const fi = (x, d) => x.toFixed(d).replace('.', ',').replace('-', '−');   // Finnish decimal comma and minus sign
});
