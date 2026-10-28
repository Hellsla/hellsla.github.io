// fy2-2 Energian suuruusluokat: an energy ladder in joules, one power of ten at a time.
// Model: every object has an energy E = m · 10^k J (real, rounded values; each with a source or an "estimate" label).
// The view is a window of about 2,4 powers of ten, centred at 10^L J; a rung is drawn at each power of ten and named with its
// prefix (10 MJ, 100 MJ, 1 GJ ...). The picture is a vertical logarithmic scale: equal steps are equal factors of ten.
// The view moves by the Kohde select (to the object) and by the two buttons (one power of ten); there is no free slider.
// A filled dot = value from a source, table or calculation; a ring = an estimate. The selected object (Kohde) has a band and
// its energy under its name, as a power of ten and with a prefix. Labels of near-equal energies are pushed apart with a short
// leader line. Text is large (17 px on the page at every width), so few objects share one view. Every canvas text goes through lab().
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
  const LMIN = -19, LMAX = 26.6, HALF = 1.2;
  const Y0 = 205, PD = 150;                                  // y of the view centre, pixels per power of ten
  const COL = { dot: [232, 89, 12], rail: [31, 41, 51], band: [255, 232, 204], z0: [246, 241, 230], z1: [252, 249, 241] };
  let btnUp, btnDown, selK, readout, L = 7.5, k = 1, labels = [];

  const lg = (o) => Math.log10(o[1]) + o[2];                 // log10 of the energy in J
  const tx = (x, d) => x.toFixed(d).replace('.', '{,}');     // Finnish decimal comma inside LaTeX
  const num = (x) => (Math.abs(x - Math.round(x)) < 1e-9 ? String(Math.round(x)) : tx(x, 1));
  const setL = (v) => { L = Math.max(LMIN, Math.min(LMAX, Math.round(v * 10) / 10)); };
  const objOf = (id) => OBJ.find((o) => o[0] === id);
  const byName = (nm) => OBJ.find((o) => __('n_' + o[0]) === nm) || OBJ[0];
  // a name as TeX without space characters, so that the label is one word for the page's text count
  // objects with a number and a unit in their name have a TeX name t_<id> (lang/fi.json); the select keeps the plain name
  const texOf = (o) => { const t = __('t_' + o[0]); return t && t !== 't_' + o[0] ? t : null; };
  const nameTex = (o) => texOf(o) || __('n_' + o[0]).split(' ').map((w) => `\\text{${w}}`).join('\\kern0.3em');
  // E = m · 10^k J written as mantissa and power, and with the prefix that makes the number 1…999
  const powTex = (o) => (o[2] === 0 ? `${tx(o[1], 1)}\\kern0.17em\\text{J}` : `${tx(o[1], 1)}\\cdot10^{${o[2]}}\\kern0.17em\\text{J}`);
  const prefTex = (o) => {
    if (o[2] < 3) return null;
    const pk = Math.floor(o[2] / 3) * 3, v = o[1] * Math.pow(10, o[2] - pk), r = Math.round(v * 10) / 10;
    return `${num(r)}\\kern0.17em\\text{${PRE[pk]}J}`;
  };
  // a rung named with its prefix (1 kJ, 10 MJ, 100 GJ); below 1 kJ in joules, below 1 J as a power of ten
  const rungTex = (kk) => {
    if (kk < 0) return `10^{${kk}}\\kern0.17em\\text{J}`;
    if (kk < 3) return `${Math.pow(10, kk)}\\kern0.17em\\text{J}`;
    const pk = Math.floor(kk / 3) * 3;
    return `${Math.pow(10, kk - pk)}\\kern0.17em\\text{${PRE[pk]}J}`;
  };

  p.setup = () => {
    p.createCanvas(600, 400).parent('sim-root');
    const controls = p.createDiv('').parent('sim-root').class('controls');
    readout = p.createDiv('').parent('sim-root').class('readout');
    btnUp = p.createButton(__('ylos')).parent(controls);
    btnDown = p.createButton(__('alas')).parent(controls);
    const lk = p.createElement('label').parent(controls); p.createSpan(__('kohde')).parent(lk); selK = p.createSelect().parent(lk);
    for (const o of OBJ) selK.option(__('n_' + o[0]), __('n_' + o[0]));
    p.createP(__('selite')).parent('sim-root').class('note');
    p.textFont('Arial');
    selK.selected(__('n_bensiini')); setL(lg(objOf('bensiini')));
    btnUp.mousePressed(() => { setL(Math.round(L) + 1); p.redraw(); });
    btnDown.mousePressed(() => { setL(Math.round(L) - 1); p.redraw(); });
    const jump = () => { setL(lg(byName(selK.value()))); p.redraw(); };
    selK.elt.addEventListener('change', jump);
    selK.elt.addEventListener('input', jump);
    // adapter for guided investigations (sim-embed.js): the page may set, lock and reset the object
    if (window.defineSimAdapter) window.defineSimAdapter({
      params: { kohde: { input: selK.elt, unit: '' } },
      reset: () => { selK.selected(__('n_bensiini')); setL(lg(objOf('bensiini'))); },
      step: () => p.redraw(), pause: () => p.noLoop(), resume: () => p.loop(),
    });
  };

  p.draw = () => {
    const fo = byName(selK.value()), kf = lg(fo);
    k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));
    const fh = Math.round(17 * k), row = Math.round(fh * 1.5), row2 = Math.round(fh * 2.7);
    const SX = Math.round(34 + 3.4 * fh);                    // ladder spine x: room for the rung names on its left
    labels = [];
    const Y = (v) => Y0 - (v - L) * PD;
    const vis = OBJ.filter((o) => Math.abs(lg(o) - L) <= HALF + 0.05);
    const ys = vis.map((o) => Y(lg(o)));
    const E = fo[1] * Math.pow(10, fo[2]);
    const pt = prefTex(fo), dir = kf > L + HALF + 0.05 ? __('yla') : kf < L - HALF - 0.05 ? __('ala') : '';
    readout.html(__('valittu', { nimi: texOf(fo) ? `$${texOf(fo)}$` : __('n_' + fo[0]), arvo: powTex(fo) + (pt ? ` = ${pt}` : ''), lahde: __('s_' + fo[0]) }) +
      (dir ? __('ulkona', { suunta: dir }) : ''));
    window.simState = { L, kohde: selK.value(), k: kf, E_J: E, E_MJ: E / 1e6, E_EJ: E / 1e18, tyyppi: fo[3] === 'lahde' ? 1 : 0, nakyvat: vis.length, labels: null };

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
      lab(`$${rungTex(kk)}$`, SX - 16, y + 0.3 * fh, 'r', fh, kk % 3 === 0 ? null : [90, 98, 108]);
    }
    // labels: one line per object, two for the selected one (its energy under the name); pushed apart from the top, then back
    const hs = vis.map((o) => (o[0] === fo[0] ? row2 : row));
    const ord = vis.map((o, i) => i).sort((a, b) => ys[a] - ys[b]), ly = {};
    ord.forEach((i, j) => { const q = ord[j - 1]; ly[i] = Math.max(ys[i], j ? ly[q] + (hs[q] + hs[i]) / 2 : 24 + hs[i] / 2); });
    for (let j = ord.length - 1; j >= 0; j--) {
      const i = ord[j], q = ord[j + 1];
      ly[i] = Math.min(ly[i], j < ord.length - 1 ? ly[q] - (hs[q] + hs[i]) / 2 : 386 - hs[i] / 2);
    }
    ord.forEach((i) => {
      const o = vis[i], isF = o[0] === fo[0], x = SX + 38;
      const s = `$${nameTex(o)}$`, v = `$${powTex(o)}${pt ? ` = ${pt}` : ''}$`;
      p.textSize(fh);
      const w = isF ? Math.max(p.textWidth(s), p.textWidth(v)) : 0;
      if (isF) { p.noStroke(); p.fill(...COL.band); p.rect(SX + 22, ly[i] - hs[i] / 2 + 2, x - SX - 22 + w + 10, hs[i] - 4, 6); }
      p.stroke(120); p.strokeWeight(1.2); p.line(SX + 7, ys[i], SX + 24, ly[i]); p.line(SX + 24, ly[i], SX + 32, ly[i]);
      p.strokeWeight(isF ? 3 : 2);
      if (o[3] === 'lahde') p.fill(...COL.dot); else p.fill(255);
      p.stroke(...COL.dot); p.circle(SX, ys[i], isF ? 19 : 15);
      if (isF) { lab(s, x, ly[i] - 0.4 * fh, 'l', fh); lab(v, x, ly[i] + 0.85 * fh, 'l', fh, [70, 70, 70]); }
      else lab(s, x, ly[i] + 0.3 * fh, 'l', fh);
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
