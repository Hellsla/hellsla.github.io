// fy2-2 Energian suuruusluokat: an energy ladder in joules, one power of ten at a time.
// Model: every object has an energy E = m · 10^k J (real, rounded values; each with a source or an "estimate" label).
// The view is a window of five powers of ten, centred at 10^L J; a rung is drawn at each power of ten with its prefix
// (kJ, MJ, GJ, TJ ...). The picture is a vertical logarithmic scale: equal steps are equal factors of ten.
// A filled dot = value from a source, table or calculation; a ring = an estimate. The selected object (Kohde) has a band.
// Labels of near-equal energies are pushed apart with a short leader line. Every canvas text goes through lab().
new p5((p) => {
  const OBJ = [
    ['foton', 3.6, -19, 'lahde'],
    ['sydan', 1.0, 0, 'arvio'],
    ['omena', 1.0, 0, 'arvio'],
    ['luoti', 1.5, 2, 'lahde'],
    ['tikku', 1.0, 3, 'arvio'],
    ['paristo', 1.4, 4, 'lahde'],
    ['puhelin', 5.4, 4, 'arvio'],
    ['banaani', 4.5, 5, 'arvio'],
    ['suklaa', 4.4, 6, 'arvio'],
    ['ruoka', 1.0, 7, 'arvio'],
    ['bensiini', 3.2, 7, 'lahde'],
    ['kaasu', 5.1, 8, 'lahde'],
    ['salama', 1.0, 9, 'arvio'],
    ['tankki', 1.6, 9, 'lahde'],
    ['tnt', 4.2, 9, 'lahde'],
    ['lento', 2, 12, 'arvio'],
    ['uraani', 8.2, 13, 'lahde'],
    ['ol3', 1.4, 14, 'lahde'],
    ['sahkopaiva', 7.9, 14, 'lahde'],
    ['tankkeri', 4.2, 15, 'arvio'],
    ['aurinko_s', 1.7, 17, 'lahde'],
    ['sahkovuosi', 2.9, 17, 'lahde'],
    ['suomi', 1.3, 18, 'lahde'],
    ['jaristys', 2.0, 18, 'arvio'],
    ['ihmiskunta', 6.2, 20, 'lahde'],
    ['aurinko_h', 6.2, 20, 'lahde'],
    ['asteroidi', 4, 23, 'arvio'],
    ['aurinko', 3.8, 26, 'lahde']
  ];
  const PRE = { 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y' };
  const LMIN = -19, LMAX = 26.6, HALF = 2.5;
  const SX = 222, Y0 = 205, PD = 70;                         // ladder spine x, y of the view centre, pixels per power of ten
  const COL = { dot: [232, 89, 12], rail: [31, 41, 51], band: [255, 232, 204], z0: [246, 241, 230], z1: [252, 249, 241] };
  let btnUp, btnDown, slL, sL, selK, readout, k = 1, labels = [];

  const lg = (o) => Math.log10(o[1]) + o[2];                 // log10 of the energy in J
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');     // Finnish decimal comma inside LaTeX
  const num = (x) => (Math.abs(x - Math.round(x)) < 1e-9 ? String(Math.round(x)) : tx(x, 1));
  const curL = () => Number(slL.value());
  const setL = (v) => slL.value(Math.max(LMIN, Math.min(LMAX, Math.round(v * 10) / 10)));
  const objOf = (id) => OBJ.find((o) => o[0] === id);
  const byName = (nm) => OBJ.find((o) => __('n_' + o[0]) === nm) || OBJ[0];
  // a name as TeX without space characters, so that the label is one word for the page's text count: words joined by \;
  const nameTex = (o) => __('n_' + o[0]).split(' ').map((w) => `\\text{${w}}`).join('\\kern0.3em');
  // E = m · 10^k J written as mantissa and power, and with the prefix that makes the number 1…999
  const powTex = (o) => (o[2] === 0 ? `${tx(o[1], 1)}\\kern0.17em\\text{J}` : `${tx(o[1], 1)}\\cdot10^{${o[2]}}\\kern0.17em\\text{J}`);
  const prefTex = (o) => {
    if (o[2] < 3) return null;
    const pk = Math.floor(o[2] / 3) * 3, v = o[1] * Math.pow(10, o[2] - pk), r = Math.round(v * 10) / 10;
    return `${num(r)}\\kern0.17em\\text{${PRE[pk]}J}`;
  };
  const rungTex = (kk) => {
    if (kk < 3) return `10^{${kk}}\\kern0.17em\\text{J}`;
    const pk = Math.floor(kk / 3) * 3;
    return `10^{${kk}}\\kern0.17em\\text{J}=${Math.pow(10, kk - pk)}\\kern0.17em\\text{${PRE[pk]}J}`;
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnUp = p.createButton(__('ylos')).parent(controls);
    btnDown = p.createButton(__('alas')).parent(controls);
    const ls = p.createElement('label').parent(controls); sL = p.createSpan('').parent(ls); slL = p.createSlider(LMIN, LMAX, 7, 0.1).parent(ls);
    const lk = p.createElement('label').parent(controls); p.createSpan(__('kohde')).parent(lk); selK = p.createSelect().parent(lk);
    for (const o of OBJ) selK.option(__('n_' + o[0]), __('n_' + o[0]));
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    selK.selected(__('n_bensiini')); setL(lg(objOf('bensiini')));
    btnUp.mousePressed(() => setL(Math.round(curL()) + 1));
    btnDown.mousePressed(() => setL(Math.round(curL()) - 1));
    const jump = () => setL(lg(byName(selK.value())));
    selK.elt.addEventListener('change', jump);
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset these parameters
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { kohde: { input: selK.elt, unit: '' }, L: { input: slL.elt, unit: '' } },
      reset: () => { selK.selected(__('n_bensiini')); setL(lg(objOf('bensiini'))); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const L = curL(), fo = byName(selK.value()), kf = lg(fo);
    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const ts = (x) => Math.round(x * k), fh = ts(11), row = Math.round(fh * 1.65);
    labels = [];
    const Y = (v) => Y0 - (v - L) * PD;
    sL.html(__('keskikohta', { e: num(L) }));
    const vis = OBJ.filter((o) => Math.abs(lg(o) - L) <= HALF + 0.05);
    const ys = vis.map((o) => Y(lg(o)));
    const E = fo[1] * Math.pow(10, fo[2]), typ = fo[3] === 'lahde' ? __('t_lahde') : __('t_arvio');
    const pt = prefTex(fo), dir = kf > L + HALF + 0.05 ? __('yla') : kf < L - HALF - 0.05 ? __('ala') : '';
    readout.html(__('valittu', { nimi: __('n_' + fo[0]), arvo: powTex(fo) + (pt ? ` = ${pt}` : ''), tyyppi: typ, lahde: __('s_' + fo[0]) }) +
      (dir ? __('ulkona', { suunta: dir }) : ''));
    window.simState = { L, kohde: selK.value(), k: kf, E_J: E, E_MJ: E / 1e6, tyyppi: fo[3] === 'lahde' ? 1 : 0, nakyvat: vis.length, labels: null };

    p.background(250);
    // zones between powers of ten that are multiples of three: one prefix each
    for (let z = Math.floor((L - HALF) / 3) - 1; z <= Math.ceil((L + HALF) / 3) + 1; z++) {
      const ya = Math.max(24, Math.min(386, Y(3 * z + 3))), yb = Math.max(24, Math.min(386, Y(3 * z)));
      if (yb > ya) { p.noStroke(); p.fill(...(((z % 2) + 2) % 2 ? COL.z1 : COL.z0)); p.rect(0, ya, 600, yb - ya); }
    }
    // the ladder: two rails and a rung at each power of ten
    p.stroke(...COL.rail); p.strokeWeight(3); p.line(SX - 7, 24, SX - 7, 386); p.line(SX + 7, 24, SX + 7, 386);
    for (let kk = Math.ceil(L - HALF - 0.05); kk <= Math.floor(L + HALF + 0.05); kk++) {
      const y = Y(kk); if (y < 28 || y > 382 || kk > 26) continue;
      p.stroke(...COL.rail); p.strokeWeight(kk % 3 === 0 ? 3 : 1.8); p.line(SX - 7, y, SX + 7, y);
      lab(`$${rungTex(kk)}$`, SX - 16, y + 0.25 * fh, 'r', fh);
    }
    // labels: pushed apart from the top, then back from the bottom, so none overlaps
    const ord = vis.map((o, i) => i).sort((a, b) => ys[a] - ys[b]), ly = {};
    const top = 24 + row / 2, bot = 386 - row / 2;
    ord.forEach((i, j) => { ly[i] = Math.max(ys[i], j ? ly[ord[j - 1]] + row : top); });
    for (let j = ord.length - 1; j >= 0; j--) { const i = ord[j]; ly[i] = Math.min(ly[i], j < ord.length - 1 ? ly[ord[j + 1]] - row : bot); }
    ord.forEach((i) => {
      const o = vis[i], isF = o[0] === fo[0], x = SX + 38;
      const s = `$${nameTex(o)}\\kern0.6em${powTex(o)}$`;
      p.textSize(fh);
      const w = p.textWidth(s);
      if (isF) { p.noStroke(); p.fill(...COL.band); p.rect(SX + 22, ly[i] - row / 2 + 1, x - SX - 22 + w + 10, row - 2, 6); }
      p.stroke(120); p.strokeWeight(1.2); p.line(SX + 7, ys[i], SX + 24, ly[i]); p.line(SX + 24, ly[i], SX + 32, ly[i]);
      p.stroke(...COL.rail); p.strokeWeight(isF ? 3 : 2);
      if (o[3] === 'lahde') p.fill(...COL.dot); else p.fill(255);
      p.stroke(...COL.dot); p.circle(SX, ys[i], isF ? 17 : 13);
      lab(s, x, ly[i] + 0.25 * fh, 'l', fh);
    });
    window.simState.labels = labels;
  };

  // every canvas text: its ink box pushed to simState.labels (canvas coordinates)
  function lab(s, x, y, align, size, col) {
    p.noStroke(); p.textStyle(p.NORMAL); p.textAlign(p.LEFT, p.BASELINE); p.textSize(size);
    const w = p.textWidth(s), x0 = align === 'r' ? x - w : align === 'c' ? x - w / 2 : x;
    p.fill(...(col || [35, 35, 35])); p.text(s, x0, y);
    labels.push({ s, x0, y0: y - 0.75 * size, x1: x0 + w, y1: y + 0.25 * size });
  }
  });
