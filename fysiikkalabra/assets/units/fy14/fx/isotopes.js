/* Isotope Builder (data-fx="isotopes"): the student sets the number of protons Z and neutrons N (a slider and − / +
   buttons for each, all keyboard operable) and sees the nucleus drawn as packed protons (red, marked +) and neutrons
   (grey), the element's name and symbol, the nuclear notation $^{A}_{Z}\text{X}$, the mass number $A = Z + N$ and
   whether the nuclide is known: stable, radioactive with its half-life (NUBASE2020), unbound, or "not in our table —
   probably very unstable". Chips list every known isotope of the element and set it with one press.
   The facts come from the data file named by the element's data-src (units/fy14/data/nuclides.json: "elements",
   "chart" keyed "Z-N" with "stable" or a half-life text, and "nuclides" for the course's own table).
   Options in the element's JSON: {zmax?: highest Z on the slider (default 20, at most 92), start?: [z, n],
   intro?: text, tasks?: [{text, z, n, hint?: text shown after a wrong check, done?: text shown when right}]}.
   Each task has its own "Check" button; feedback says right or wrong in words and with ✓ / ✗, and explains what is
   still wrong (the element or the isotope). The current nucleus and solved tasks are kept in localStorage. */
window.FX.isotopes = (el, d, A) => {
  const { h, md, store, typeset } = A;
  const NS = 'http://www.w3.org/2000/svg';
  const S = (tag, attrs) => { const e = document.createElementNS(NS, tag); Object.entries(attrs || {}).forEach(([k, v]) => e.setAttribute(k, v)); return e; };
  const root = h('div', { class: 'fx-iso' });
  el.append(root);
  A.data(el.getAttribute('data-src')).then(build).catch((e) => root.append(h('p', { class: 'fx-note' }, 'The nuclide data could not be loaded (' + e + ').')));

  function build(data) {
    const zmax = Math.min(92, Math.max(2, d.zmax || 20));
    const nmax = zmax <= 20 ? Math.max(30, Math.ceil(zmax * 1.6)) : Math.ceil(zmax * 1.65);
    const els = data.elements, chart = data.chart;
    const byZN = {}; data.nuclides.forEach((x) => { if (x.id !== 'p') byZN[x.Z + '-' + x.N] = x; });
    const saved = store.get(el.id) || {};
    let Z = (saved.z != null ? saved.z : (d.start || [2, 2])[0]), N = (saved.n != null ? saved.n : (d.start || [2, 2])[1]);
    Z = Math.min(zmax, Math.max(0, Z)); N = Math.min(nmax, Math.max(0, N));
    const solved = saved.solved || {};
    const idp = el.id + '-';

    const ctl = (key, label, max) => {
      const range = h('input', { type: 'range', id: idp + key, min: 0, max, step: 1, 'aria-describedby': idp + key + '-out' });
      const out = h('output', { id: idp + key + '-out', for: idp + key, class: 'fx-iso-num' });
      const minus = h('button', { type: 'button', class: 'fx-move', 'aria-label': 'One ' + (key === 'z' ? 'proton' : 'neutron') + ' fewer' }, '−');
      const plus = h('button', { type: 'button', class: 'fx-move', 'aria-label': 'One ' + (key === 'z' ? 'proton' : 'neutron') + ' more' }, '+');
      const row = h('div', { class: 'fx-iso-ctl' }, h('label', { for: idp + key, html: label }), h('div', { class: 'fx-iso-row' }, minus, range, plus, out));
      return { range, out, minus, plus, row };
    };
    const cz = ctl('z', '<span class="fx-iso-dot fx-iso-p" aria-hidden="true">+</span> Protons $Z$', zmax);
    const cn = ctl('n', '<span class="fx-iso-dot fx-iso-n" aria-hidden="true"></span> Neutrons $N$', nmax);
    const svg = S('svg', { viewBox: '0 0 200 200', role: 'img', class: 'fx-iso-svg' });
    const defs = S('defs');
    [['p', '#ff8a80', '#c92a2a', '#7f1d1d'], ['n', '#e9ecef', '#9aa1a9', '#4b5259']].forEach(([k, a, b, c]) => {
      const g = S('radialGradient', { id: idp + 'g' + k, cx: '35%', cy: '32%', r: '70%' });
      g.append(S('stop', { offset: '0%', 'stop-color': a }), S('stop', { offset: '55%', 'stop-color': b }), S('stop', { offset: '100%', 'stop-color': c }));
      defs.append(g);
    });
    svg.append(defs);
    const g = S('g'); svg.append(g);
    const notation = h('p', { class: 'fx-iso-notation', 'aria-live': 'polite' });
    const nameP = h('p', { class: 'fx-iso-name' });
    const massP = h('p', { class: 'fx-iso-mass' });
    const status = h('p', { class: 'fx-iso-status', 'aria-live': 'polite' });
    const chipsH = h('p', { class: 'fx-iso-chips-h' });
    const chips = h('div', { class: 'fx-iso-chips', role: 'group' });
    const legend = h('p', { class: 'fx-note fx-iso-legend', html: '<span class="fx-iso-dot fx-iso-p" aria-hidden="true">+</span> proton (red, marked +) &nbsp; <span class="fx-iso-dot fx-iso-n" aria-hidden="true"></span> neutron (grey). The drawing is a picture of the counts, not of real positions: a nucleus has no sharp surface.' });

    root.append(...(d.intro ? [h('p', { class: 'fx-prompt', html: md(d.intro) })] : []),
      h('div', { class: 'fx-iso-ctls' }, cz.row, cn.row),
      h('div', { class: 'fx-iso-main' }, h('div', { class: 'fx-iso-pic' }, svg), h('div', { class: 'fx-iso-info' }, notation, nameP)), massP, status,
      legend, chipsH, chips);

    let tasksBox = null; const taskRows = [];
    if (d.tasks && d.tasks.length) {
      tasksBox = h('ol', { class: 'fx-iso-tasks' });
      d.tasks.forEach((t, i) => {
        const out = h('output', { 'aria-live': 'polite' });
        const btn = h('button', { type: 'button', class: 'fx-btn fx-small' }, 'Check');
        const li = h('li', { class: 'fx-iso-task' }, h('p', { html: md(t.text) }), h('div', { class: 'fx-actions' }, btn), out);
        btn.addEventListener('click', () => {
          const zOk = Z === t.z, nOk = N === t.n;
          let msg;
          if (zOk && nOk) { msg = 'Right. ' + md(t.done || `This is ${nameOf(t.z, t.n)}.`); solved[i] = true; save(); }
          else if (!zOk) msg = 'Not yet. Your nucleus is not the right element: the number of protons $Z$ decides the element.' + (t.hint ? ' ' + md(t.hint) : '');
          else msg = 'Not yet. The element is right, but it is not the right isotope: change the number of neutrons $N$.' + (t.hint ? ' ' + md(t.hint) : '');
          out.dataset.state = zOk && nOk ? 'ok' : 'no'; li.dataset.state = out.dataset.state; out.innerHTML = msg; typeset(out);
        });
        if (solved[i]) { li.dataset.state = 'ok'; out.dataset.state = 'ok'; out.innerHTML = 'Right. You solved this one earlier.'; }
        taskRows.push(li); tasksBox.append(li);
      });
      root.append(h('h4', { class: 'fx-iso-tasks-h' }, 'Challenges'), tasksBox);
    }
    root.append(h('p', { class: 'fx-note', html: `Data: masses AME2020, half-lives NUBASE2020 (checked ${A.date(data.checked)}).` }));

    function save() { store.set(el.id, { z: Z, n: N, solved }); }
    function el0(z) { return els[z] || { symbol: '?', name: 'unknown' }; }
    function nameOf(z, n) { return z === 0 ? (n === 1 ? 'a free neutron' : n + ' neutrons') : el0(z).name.toLowerCase() + '-' + (z + n); }
    function tex(z, n) { return z === 0 && n === 1 ? '$^{1}_{0}\\text{n}$' : `$^{${z + n}}_{${z}}\\text{${el0(z).symbol}}$`; }

    function draw() {
      const Anum = Z + N;
      while (g.firstChild) g.firstChild.remove();
      if (Anum === 0) { svg.setAttribute('aria-label', 'No nucleons yet.'); return; }
      const outer = Math.min(94, 27 * Math.cbrt(Anum));
      const k = outer / (Math.sqrt(Anum) * 1.0 + 1);
      const golden = Math.PI * (3 - Math.sqrt(5));
      const pts = [];
      for (let i = 0; i < Anum; i++) {
        const r = Anum === 1 ? 0 : Math.sqrt(i + 0.5) * k * 1.0;
        pts.push([100 + r * Math.cos(i * golden), 100 + r * Math.sin(i * golden)]);
      }
      for (let i = Anum - 1; i >= 0; i--) {
        const isP = Math.floor(((i + 1) * Z) / Anum) > Math.floor((i * Z) / Anum);
        const [x, y] = pts[i];
        g.append(S('circle', { cx: x.toFixed(2), cy: y.toFixed(2), r: (k * 1.02).toFixed(2), fill: `url(#${idp}g${isP ? 'p' : 'n'})`, stroke: isP ? '#7f1d1d' : '#4b5259', 'stroke-width': Math.max(0.4, k * 0.06).toFixed(2) }));
        if (isP && k >= 4.5) {
          const s = k * 0.42, w = Math.max(0.8, k * 0.16);
          g.append(S('path', { d: `M${(x - s).toFixed(2)} ${y.toFixed(2)}h${(2 * s).toFixed(2)}M${x.toFixed(2)} ${(y - s).toFixed(2)}v${(2 * s).toFixed(2)}`, stroke: '#fff', 'stroke-width': w.toFixed(2), 'stroke-linecap': 'round' }));
        }
      }
      svg.setAttribute('aria-label', `A nucleus drawn as ${Z} red proton${Z === 1 ? '' : 's'} and ${N} grey neutron${N === 1 ? '' : 's'} packed together.`);
    }

    function stableNs(z) { return Object.entries(chart).filter(([key, v]) => key.split('-')[0] === String(z) && v === 'stable').map(([key]) => Number(key.split('-')[1])); }

    function update() {
      cz.range.value = Z; cn.range.value = N; cz.out.textContent = String(Z); cn.out.textContent = String(N);
      cz.minus.disabled = Z <= 0; cz.plus.disabled = Z >= zmax; cn.minus.disabled = N <= 0; cn.plus.disabled = N >= nmax;
      const Anum = Z + N, key = Z + '-' + N, e = el0(Z);
      draw();
      if (Anum === 0) {
        notation.innerHTML = '—'; nameP.textContent = 'Add protons or neutrons to build a nucleus.'; massP.innerHTML = 'Mass number: $A = 0$';
        status.dataset.state = 'hint'; status.textContent = 'Nothing to show yet.';
      } else {
        notation.innerHTML = Z === 0 && N !== 1 ? '—' : tex(Z, N);
        nameP.innerHTML = Z === 0 ? (N === 1 ? 'A free <strong>neutron</strong> (no protons: not an element)' : 'Only neutrons: this is not an element.')
          : `Element: <strong>${e.name.toLowerCase()}</strong> (symbol ${'$\\text{' + e.symbol + '}$'}), because ${'$'}{Z = ${Z}}${'$'}`;
        massP.innerHTML = `Mass number: ${'$'}{A = Z + N = ${Z} + ${N} = ${Anum}}${'$'}`;
        const v = chart[key], own = byZN[key];
        if (v === 'stable') {
          status.dataset.state = 'ok';
          status.innerHTML = `<strong>Stable.</strong> ${cap(nameOf(Z, N))} is a known nuclide: no decay has ever been observed.` + (own && own.note ? ' ' + md(own.note) : '');
        } else if (v && /^unbound/.test(v)) {
          status.dataset.state = 'no';
          status.innerHTML = `<strong>Unbound.</strong> ${cap(nameOf(Z, N))} has been seen only as a resonance: it falls apart at once.`;
        } else if (v) {
          status.dataset.state = 'rad';
          status.innerHTML = `<strong>Radioactive.</strong> ${cap(nameOf(Z, N))} is known; its half-life is ${v}.` + (own && own.note ? ' ' + md(own.note) : '') + valley(Z, N);
        } else {
          status.dataset.state = 'no';
          status.innerHTML = '<strong>Not in our table.</strong> This combination is probably very unstable: it falls apart almost at once, or nobody has made it yet.' + valley(Z, N);
        }
      }
      // chips: the known isotopes of this element
      const isoNs = Object.keys(chart).filter((kk) => kk.split('-')[0] === String(Z)).map((kk) => Number(kk.split('-')[1])).filter((n) => !/^unbound/.test(chart[Z + '-' + n])).sort((a, b) => a - b);
      chips.replaceChildren(...isoNs.map((n) => {
        const st = chart[Z + '-' + n] === 'stable';
        const b = h('button', { type: 'button', class: 'fx-iso-chip' + (st ? ' is-stable' : ''), 'aria-pressed': String(n === N),
          'aria-label': `${nameOf(Z, n)}, ${st ? 'stable' : 'radioactive'}`, html: (st ? '<span aria-hidden="true">✓ </span>' : '') + tex(Z, n) });
        b.addEventListener('click', () => { N = n; changed(); });
        return b;
      }));
      chips.setAttribute('aria-label', 'Isotopes of this element');
      chipsH.innerHTML = Z === 0 ? 'Only the single free neutron is a known particle here.' : isoNs.length
        ? `Known isotopes of ${e.name.toLowerCase()} (${isoNs.length}; ✓ = stable, the others are radioactive). Press one to build it:` : 'No known isotopes in our table.';
      typeset(root);
    }
    function valley(z, n) {
      if (z === 0) return '';
      const s = stableNs(z); if (!s.length) return z > 82 ? ' Every element after lead is radioactive: no isotope of it is stable.' : '';
      if (n > Math.max(...s)) return ` It has more neutrons than any stable isotope of ${el0(z).name.toLowerCase()}: such nuclei usually turn a neutron into a proton ($\\beta^-$ decay).`;
      if (n < Math.min(...s)) return ` It has fewer neutrons than any stable isotope of ${el0(z).name.toLowerCase()}: such nuclei usually turn a proton into a neutron ($\\beta^+$ decay) or lose a proton.`;
      return '';
    }
    function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
    function changed() { save(); update(); }
    cz.range.addEventListener('input', () => { Z = Number(cz.range.value); changed(); });
    cn.range.addEventListener('input', () => { N = Number(cn.range.value); changed(); });
    cz.minus.addEventListener('click', () => { Z = Math.max(0, Z - 1); changed(); });
    cz.plus.addEventListener('click', () => { Z = Math.min(zmax, Z + 1); changed(); });
    cn.minus.addEventListener('click', () => { N = Math.max(0, N - 1); changed(); });
    cn.plus.addEventListener('click', () => { N = Math.min(nmax, N + 1); changed(); });
    update();
  }
};
