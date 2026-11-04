// fy7-13 Valon interferenssi ja diffraktio: a laser shines perpendicularly through a grating of N lines per millimetre
// (slider 100–1000) onto a screen at distance L (slider 0,50–2,00 m) that is perpendicular to the beam; the wavelength
// λ (slider 400–700 nm) sets the light's colour. Seen from above, to scale (160 px per metre in both directions): the
// screen is 1,80 m wide (±0,90 m). Model: d = 1 mm : N, maxima where d sin θ = k λ (θ from the beam's direction, the
// central maximum), k = 0, ±1, … while k λ < d; on the screen x = L tan θ. Maxima that would land beyond the screen's
// edge are drawn as faint rays only. The brightness of the higher orders is an illustration, not computed.
// Static: drawn again on every frame, no animation. Every canvas text goes through lab().
new p5((p) => {
  const ROOM = [31, 41, 51], PAPER = [246, 241, 230], MUTEDC = [150, 158, 168], SCREEN = [227, 220, 203];
  const SLIDE = [196, 204, 212], LASER = [108, 117, 125];
  const XG = 128, YC = 200, S = 160, HALF = 0.9;                 // grating, beam axis, px per metre, screen half-width (m)
  const YT = YC - HALF * S, YB = YC + HALF * S;
  let slN, slW, slL, lN, lW, lL, readout, labels = [];

  const deg = (r) => r * 180 / Math.PI;
  const state = () => {
    const N = Number(slN.value()), lambda = Number(slW.value()), L = Number(slL.value());
    const d = 1000 / N;                                           // µm
    const lam = lambda / 1000;                                    // µm
    let kmax = Math.floor(d / lam); if (kmax * lam >= d) kmax -= 1;
    const orders = [];
    for (let k = 0; k <= kmax; k++) {
      const th = Math.asin(k * lam / d), x = L * Math.tan(th);    // x in metres
      orders.push({ k, th, x, on: x <= HALF + 1e-9 });
    }
    const onScreen = orders.reduce((n, o) => n + (o.on ? (o.k === 0 ? 1 : 2) : 0), 0);
    return { N, lambda, L, d, kmax, count: 2 * kmax + 1, onScreen, orders };
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    const l1 = p.createElement('label').parent(controls); lN = p.createSpan('').parent(l1); slN = p.createSlider(100, 1000, 300, 50).parent(l1);
    const l2 = p.createElement('label').parent(controls); lW = p.createSpan('').parent(l2); slW = p.createSlider(400, 700, 650, 1).parent(l2);
    const l3 = p.createElement('label').parent(controls); lL = p.createSpan('').parent(l3); slL = p.createSlider(0.5, 2, 1, 0.05).parent(l3);
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { N: { input: slN.elt, unit: '1/mm' }, lambda: { input: slW.elt, unit: 'nm' }, L: { input: slL.elt, unit: 'm' } },
      reset: () => { slN.value(300); slW.value(650); slL.value(1); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const s = state();
    lN.html(__('N', { n: s.N })); lW.html(__('lambda', { l: s.lambda })); lL.html(__('L', { L: tx(s.L, 2) }));
    const o1 = s.orders[1], o2 = s.orders[2];
    let r = __('r_d', { d: tx(s.d, 3) }) + '<br>' + __('r_1', { t: tx(deg(o1.th), 2), x: tx(o1.x * 100, 1) }) + (o1.on ? '' : __('r_off'));
    r += '<br>' + (o2 ? __('r_2', { t: tx(deg(o2.th), 2), x: tx(o2.x * 100, 1) }) + (o2.on ? '' : __('r_off')) : __('r_2_none'));
    r += '<br>' + __('r_count', { c: s.count, km: s.kmax, s: s.onScreen });
    readout.html(r);
    const cw = document.getElementById('sim-root').clientWidth || 600, k = Math.max(1, 600 / cw);
    const fh = Math.round((k > 1.2 ? 14 : 13) * k), H = k > 1.2 ? 450 : 400;
    if (p.__H !== H) { p.__H = H; p.resizeCanvas(600, H); setTimeout(() => p.redraw(), 0); return; }
    labels = [];
    p.background(...ROOM);
    scene(s, fh);
    window.simState = {
      N: s.N, lambda: s.lambda, L: s.L, d: s.d, kmax: s.kmax, count: s.count, onScreen: s.onScreen,
      theta1: deg(o1.th), x1: o1.x * 100, sin1: Math.sin(o1.th),
      theta2: o2 ? deg(o2.th) : null, x2: o2 ? o2.x * 100 : null, labels,
    };
  };

  function scene(s, fh) {
    const XS = XG + s.L * S, col = wlColour(s.lambda);
    // the screen with its scale (x upward positive, cm)
    p.noStroke(); p.fill(...SCREEN); p.rect(XS, YT, 8, YB - YT);
    p.stroke(...PAPER); p.strokeWeight(1.5);
    for (let c = -90; c <= 90; c += 10) {
      const y = YC - c / 100 * S, long = c % 30 === 0;
      p.line(XS + 8, y, XS + 8 + (long ? 10 : 5), y);
      if (long && (fh < 20 || c % 60 === 0)) lab(`$${c}$`, XS + 24, y + fh * 0.35, 'l', fh, PAPER);
    }
    lab('$x\\ (\\text{cm})$', XS + 24, YT - 14, 'l', fh, PAPER);
    lab(`$\\text{${__('varjostin')}}$`, XS - 6, YT - 14, 'r', fh, PAPER);
    // the laser and its beam up to the grating
    p.stroke(...PAPER); p.strokeWeight(2); p.fill(...LASER); p.rect(24, YC - 11, 66, 22, 4);
    p.noStroke(); p.fill(...col); p.rect(88, YC - 4, 4, 8);
    lab(`$\\text{${__('laser')}}$`, 57, YC + 11 + fh * 1.0, 'c', fh, PAPER);
    beam(92, YC, XG, YC, 255, 3, col);
    // the rays of every order, the spots on the screen
    s.orders.forEach((o) => {
      [1, -1].forEach((sg) => {
        if (o.k === 0 && sg < 0) return;
        const a = o.k === 0 ? 255 : Math.max(90, 220 - 40 * o.k);
        if (o.on) {
          const y = YC - sg * o.x * S;
          beam(XG, YC, XS, y, a, o.k === 0 ? 3 : 2, col);
          spot(XS + 2, y, col, o.k);
        } else {                                                 // beyond the screen: to the canvas's edge, faint
          const yEdge = sg > 0 ? 14 : p.height - 14, len = Math.abs(yEdge - YC) / Math.sin(o.th);
          const xEnd = Math.min(XS, XG + len * Math.cos(o.th));
          beam(XG, YC, xEnd, YC - sg * (xEnd - XG) * Math.tan(o.th), 70, 1.5, col);
        }
      });
    });
    // the grating: a slide in its frame
    p.stroke(...PAPER); p.strokeWeight(2); p.fill(...SLIDE); p.rect(XG - 5, YC - 46, 10, 92, 2);
    p.stroke(...ROOM); p.strokeWeight(1);
    for (let y = YC - 40; y <= YC + 40; y += 4) p.line(XG - 3, y, XG + 3, y);
    lab(`$\\text{${__('hila')}}$`, XG, YC - 54, 'c', fh, PAPER);
    // the angle θ1 from the beam's direction
    const t1 = s.orders[1].th;
    dashed(XG, YC, XS - 2, YC);
    p.noFill(); p.stroke(...PAPER); p.strokeWeight(1.5); p.arc(XG, YC, 120, 120, -t1, 0);
    const rl = 56 + fh, b = Math.max(t1 / 2, 0.2);
    lab('$\\theta_1$', XG + rl * Math.cos(b), YC - rl * Math.sin(b) + fh * 0.35, 'c', fh, PAPER);
    // the distance L under the screen's foot
    const yd = YB + 12;
    p.stroke(...PAPER); p.strokeWeight(1.5); p.line(XG, yd, XS, yd); p.line(XG, yd - 7, XG, yd + 7); p.line(XS, yd - 7, XS, yd + 7);
    arrowHead(XG, yd, -1); arrowHead(XS, yd, 1);
    lab(`$L = ${tx(s.L, 2)}\\,\\text{m}$`, (XG + XS) / 2, yd + fh * 1.25, 'c', fh, PAPER);
  }

  function spot(x, y, col, k) {
    const r = k === 0 ? 7 : Math.max(4, 6 - k);
    p.noStroke();
    for (let i = 4; i >= 1; i--) { p.fill(...col, 40); p.circle(x, y, r * 2 + i * 5); }
    p.fill(...col); p.circle(x, y, r * 2);
    p.fill(255, 255, 255, 170); p.circle(x, y, r * 0.8);
  }
  function arrowHead(x, y, dir) {
    p.noStroke(); p.fill(...PAPER); p.triangle(x, y, x - dir * 9, y - 4.5, x - dir * 9, y + 4.5);
  }
  function beam(x1, y1, x2, y2, a, w, col) { p.stroke(...col, a); p.strokeWeight(w); p.line(x1, y1, x2, y2); }
  function dashed(x1, y1, x2, y2) {
    p.stroke(...MUTEDC); p.strokeWeight(1.5); p.drawingContext.setLineDash([6, 5]); p.line(x1, y1, x2, y2); p.drawingContext.setLineDash([]);
  }
  // the colour of light of wavelength l (nm), an approximation of how it looks (after D. Bruton)
  function wlColour(l) {
    let r = 0, g = 0, b = 0;
    if (l < 440) { r = (440 - l) / 60; b = 1; } else if (l < 490) { g = (l - 440) / 50; b = 1; }
    else if (l < 510) { g = 1; b = (510 - l) / 20; } else if (l < 580) { r = (l - 510) / 70; g = 1; }
    else if (l < 645) { r = 1; g = (645 - l) / 65; } else { r = 1; }
    const f = l < 420 ? 0.55 + 0.45 * (l - 400) / 20 : l > 680 ? 0.55 + 0.45 * (700 - l) / 20 : 1;
    const c = (v) => Math.round(255 * Math.pow(Math.max(0.12, v * f), 0.8));
    return [c(r), c(g), c(b)];
  }

  // every canvas text: drawn and its ink box pushed to simState.labels (canvas coordinates)
  function lab(str, x, y, align, size, col) {
    p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(str), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.noStroke(); p.fill(...(col || PAPER)); p.text(str, x0, y);
    labels.push({ s: str, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  const DEC = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).format.decimal === '.' ? '.' : '{,}'; } catch (e) { return '{,}'; } })();
  const tx = (x, d) => x.toFixed(d).replace(/^-(0(\.0+)?)$/, '$1').replace('.', DEC);
});
