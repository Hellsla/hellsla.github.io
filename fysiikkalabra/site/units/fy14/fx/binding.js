/* Binding Energy Explorer (data-fx="binding"): binding energy per nucleon $B/A$ against the mass number $A$ for the
   nuclides of the data file named by data-src (units/fy14/data/nuclides.json, AME2020). Filled circles are stable
   nuclides, hollow ones radioactive; a smooth guide line (monotone cubic, no overshoot) joins the stable and the
   long-lived natural ones; the region of $^{56}\text{Fe}$ and $^{62}\text{Ni}$ is shaded as the peak. Every label on
   the graph is KaTeX in HTML laid over the SVG (no SVG text), so all symbols are typeset as in the text.
   - Select a nuclide from the list or click its point: the panel gives its notation, $B/A$, $B = A \cdot (B/A)$ and
     stability. "Whole curve" / "Light nuclei" switch the range of $A$.
   - Compare a reaction: masses before and after, the mass difference $\Delta m$ and $Q = \Delta m \cdot 931.494\ \text{MeV/u}$ step by
     step (atomic masses: the electrons cancel because charge is conserved), the same $Q$ again from binding energies,
     and arrows on the curve from the fuel to the products: fusion climbs from the left, fission from the right.
   Options in the element's JSON: {highlight?: [nuclide ids labelled on the curve], reactions?: [reaction ids from
   the data file, default all], reaction?: id chosen at start, select?: nuclide id chosen at start,
   question?: text shown as a question box under the graph}. */
window.FX.binding = (el, d, A) => {
  const { h, md, typeset } = A;
  const NS = 'http://www.w3.org/2000/svg';
  const S = (tag, attrs) => { const e = document.createElementNS(NS, tag); Object.entries(attrs || {}).forEach(([k, v]) => e.setAttribute(k, v)); return e; };
  const root = h('div', { class: 'fx-be' });
  el.append(root);
  A.data(el.getAttribute('data-src')).then(build).catch((e) => root.append(h('p', { class: 'fx-note' }, 'The nuclide data could not be loaded (' + e + ').')));

  function build(data) {
    const C = data.constants, uMeV = C.u_MeV;
    const all = data.nuclides.filter((x) => x.id !== 'p');
    const byId = Object.fromEntries(data.nuclides.map((x) => [x.id, x]));
    const pts = all.filter((x) => x.A > 1).sort((a, b) => a.A - b.A || a.Z - b.Z);
    const reactions = data.reactions.filter((r) => !d.reactions || d.reactions.includes(r.id));
    const idp = el.id + '-';
    const W = 640, H = 400, X0 = 64, X1 = 620, Y0 = 34, Y1 = 344, BMAX = 10;
    const VIEWS = { all: { a0: 0, a1: 250, step: 50, label: 'Whole curve' }, light: { a0: 0, a1: 24, step: 4, label: 'Light nuclei ($A \\le 24$)' } };
    let view = 'all', sel = d.select && byId[d.select] ? d.select : null, rx = null;
    const hl = d.highlight || ['H-2', 'He-4', 'Fe-56', 'U-235'];
    const LIGHT = ['H-1', 'H-2', 'H-3', 'He-3', 'He-4', 'Li-6', 'Be-9', 'C-12', 'O-16', 'Ne-20', 'Mg-24'];
    const tex = (x) => x.id === 'n' ? '$\\text{n}$' : `$^{${x.A}}\\text{${x.symbol}}$`;
    const texFull = (x) => x.id === 'n' ? '{}^{1}_{0}\\text{n}' : `{}^{${x.A}}_{${x.Z}}\\text{${x.symbol}}`;
    const f = (v, n) => v.toFixed(n);
    const sig = (v) => (Math.abs(v) >= 100 ? v.toFixed(0) : Math.abs(v) >= 10 ? v.toFixed(1) : v.toFixed(2));

    const svg = S('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img', class: 'fx-be-svg' });
    const labs = h('div', { class: 'fx-labs', 'aria-hidden': 'true' });
    const plot = h('div', { class: 'fx-plot' }, svg, labs);
    const viewBtns = Object.entries(VIEWS).map(([k, v]) => h('button', { type: 'button', class: 'fx-step', 'aria-pressed': String(k === view), 'data-view': k, html: v.label }));
    const pick = h('select', { id: idp + 'nuc' }, h('option', { value: '' }, 'Choose a nuclide…'),
      ...all.slice().sort((a, b) => a.A - b.A || a.Z - b.Z).map((x) => h('option', { value: x.id }, x.name)));
    const rsel = h('select', { id: idp + 'rx' }, h('option', { value: '' }, 'No reaction'), ...reactions.map((r) => h('option', { value: r.id }, r.label)));
    const info = h('div', { class: 'fx-be-info', 'aria-live': 'polite' });
    const calc = h('div', { class: 'fx-be-calc', 'aria-live': 'polite' });
    const caption = h('p', { class: 'fx-note fx-be-cap', html: 'Binding energy per nucleon $B/A$ against mass number $A$ (AME2020). ● stable, ○ radioactive; the line joins the stable and long-lived nuclides. The shaded band is the peak: $^{62}\\text{Ni}$ ($8.79\\ \\text{MeV}$) and $^{56}\\text{Fe}$ are the most tightly bound nuclei. Nuclei to the left can release energy by fusion, nuclei far to the right by fission.' });
    root.append(
      h('div', { class: 'fx-be-bar' },
        h('div', { class: 'fx-steps', role: 'group', 'aria-label': 'Range of the graph' }, viewBtns),
        h('div', { class: 'fx-field' }, h('label', { for: idp + 'nuc' }, 'Nuclide'), pick),
        h('div', { class: 'fx-field fx-field-wide' }, h('label', { for: idp + 'rx' }, 'Compare a reaction'), rsel)),
      h('figure', { class: 'fx-be-fig' }, plot, h('figcaption', {}, caption)), info, calc,
      ...(d.question ? [h('div', { class: 'fx-question' }, h('p', { class: 'fx-question-h' }, 'Think'), h('p', { html: md(d.question) }))] : []),
      h('p', { class: 'fx-note', html: `Masses and binding energies: AME2020; $1\\ \\text{u} = ${uMeV.toFixed(6)}\\ \\text{MeV}/c^2$ (CODATA 2018). Checked ${A.date(data.checked)}.` }));

    const xs = (a) => X0 + ((a - VIEWS[view].a0) / (VIEWS[view].a1 - VIEWS[view].a0)) * (X1 - X0);
    const ys = (b) => Y1 - (b / BMAX) * (Y1 - Y0);
    const lab = (x, y, html, cls) => labs.append(h('span', { class: 'fx-lab ' + (cls || ''), style: `left:${(x / W) * 100}%;top:${(y / H) * 100}%`, html }));

    // monotone cubic (Fritsch–Carlson) through points [[x,y]] sorted by x
    const smooth = (P) => {
      const n = P.length; if (n < 2) return '';
      const dx = [], m = [], t = [];
      for (let i = 0; i < n - 1; i++) { dx[i] = P[i + 1][0] - P[i][0]; m[i] = (P[i + 1][1] - P[i][1]) / dx[i]; }
      t[0] = m[0]; t[n - 1] = m[n - 2];
      for (let i = 1; i < n - 1; i++) t[i] = m[i - 1] * m[i] <= 0 ? 0 : (3 * (dx[i - 1] + dx[i])) / ((2 * dx[i] + dx[i - 1]) / m[i - 1] + (dx[i] + 2 * dx[i - 1]) / m[i]);
      let s = `M${f(P[0][0], 1)} ${f(P[0][1], 1)}`;
      for (let i = 0; i < n - 1; i++) s += `C${f(P[i][0] + dx[i] / 3, 1)} ${f(P[i][1] + (t[i] * dx[i]) / 3, 1)} ${f(P[i + 1][0] - dx[i] / 3, 1)} ${f(P[i + 1][1] - (t[i + 1] * dx[i]) / 3, 1)} ${f(P[i + 1][0], 1)} ${f(P[i + 1][1], 1)}`;
      return s;
    };
    const arrow = (x1, y1, x2, y2, col, dash) => {
      const g = S('g', { class: 'fx-be-arrow' });
      const len = Math.hypot(x2 - x1, y2 - y1); if (len < 4) return g;
      const ux = (x2 - x1) / len, uy = (y2 - y1) / len, hx = x2 - ux * 7, hy = y2 - uy * 7;
      g.append(S('line', { x1: f(x1 + ux * 7, 1), y1: f(y1 + uy * 7, 1), x2: f(hx - ux * 6, 1), y2: f(hy - uy * 6, 1), stroke: col, 'stroke-width': 3, 'stroke-linecap': 'round', 'stroke-dasharray': dash || 'none' }));
      g.append(S('path', { d: `M${f(hx, 1)} ${f(hy, 1)} l${f(-ux * 12 - uy * 6, 1)} ${f(-uy * 12 + ux * 6, 1)} l${f(uy * 12, 1)} ${f(-ux * 12, 1)}Z`, fill: col }));
      return g;
    };

    function draw() {
      while (svg.firstChild) svg.firstChild.remove(); labs.replaceChildren();
      const V = VIEWS[view];
      svg.append(S('rect', { x: X0, y: Y0, width: X1 - X0, height: Y1 - Y0, fill: '#fffdf8', stroke: 'none' }));
      if (view === 'all') {
        svg.append(S('rect', { x: xs(52), y: Y0, width: xs(66) - xs(52), height: Y1 - Y0, fill: '#efeadd' }));
        lab(xs(59), ys(0.55), '$\\text{peak}$', 'fx-lab-muted');
      }
      for (let b = 0; b <= BMAX; b++) {
        svg.append(S('line', { x1: X0, x2: X1, y1: ys(b), y2: ys(b), stroke: b ? '#eee8d9' : '#1f2933', 'stroke-width': b ? 1 : 1.5 }));
        lab(X0 - 10, ys(b), `$${b}$`, 'fx-lab-end');
      }
      for (let a = V.a0; a <= V.a1; a += V.step) {
        svg.append(S('line', { x1: xs(a), x2: xs(a), y1: Y1, y2: Y1 + 6, stroke: '#1f2933', 'stroke-width': 1.5 }));
        lab(xs(a), Y1 + 18, `$${a}$`);
      }
      svg.append(S('line', { x1: X0, x2: X0, y1: Y0, y2: Y1, stroke: '#1f2933', 'stroke-width': 1.5 }));
      lab(X0 - 4, 12, '$B/A\\ (\\text{MeV})$', 'fx-lab-start');
      lab((X0 + X1) / 2, H - 12, '$\\text{mass number}\\ A$');
      // the guide line through the stable and long-lived nuclides (largest B/A for each A)
      const best = {};
      pts.filter((x) => x.stable || x.long_lived).forEach((x) => { if (!best[x.A] || best[x.A].be_per_A_MeV < x.be_per_A_MeV) best[x.A] = x; });
      const guide = Object.values(best).sort((a, b) => a.A - b.A).filter((x) => x.A <= V.a1 + V.step).map((x) => [xs(x.A), ys(x.be_per_A_MeV)]);
      const clip = S('clipPath', { id: idp + 'clip' }); clip.append(S('rect', { x: X0, y: Y0 - 10, width: X1 - X0 + 8, height: Y1 - Y0 + 10 }));
      svg.append(clip);
      const gl = S('g', { 'clip-path': `url(#${idp}clip)` }); svg.append(gl);
      gl.append(S('path', { d: smooth(guide), fill: 'none', stroke: '#8a96a3', 'stroke-width': 2 }));
      // reaction arrows: from each fuel nucleus to each product (neutrons have no binding energy and are left out)
      const R = rx && reactions.find((r) => r.id === rx);
      if (R) {
        const col = R.kind === 'fission' ? '#7048e8' : '#1a4d2e';
        const from = [...new Set(R.before)].map((i) => byId[i]).filter((x) => x.A > 1), to = [...new Set(R.after)].map((i) => byId[i]).filter((x) => x.A > 1);
        from.forEach((a) => to.forEach((b) => gl.append(arrow(xs(a.A), ys(a.be_per_A_MeV), xs(b.A), ys(b.be_per_A_MeV), col, R.kind === 'fission' ? '8 5' : null))));
      }
      if (view === 'all' && !R) {   // the two general directions, under the curve
        gl.append(arrow(xs(8), ys(4.6), xs(46), ys(7.7), '#1a4d2e')); lab(xs(30), ys(5.2), '$\\text{fusion}$', 'fx-lab-fus');
        gl.append(arrow(xs(240), ys(6.6), xs(150), ys(7.6), '#7048e8', '8 5')); lab(xs(205), ys(6.45), '$\\text{fission}$', 'fx-lab-fis');
      }
      const shown = pts.filter((x) => x.A >= V.a0 && x.A <= V.a1);
      const labelled = new Set(view === 'light' ? LIGHT : hl);
      if (sel) labelled.add(sel);
      if (R) [...R.before, ...R.after].forEach((i) => labelled.add(i));
      shown.forEach((x) => {
        const cx = xs(x.A), cy = ys(x.be_per_A_MeV), on = sel === x.id;
        const g = S('g', { class: 'fx-be-pt' + (on ? ' is-on' : ''), 'data-id': x.id });
        if (on) g.append(S('circle', { cx, cy, r: 11, fill: 'none', stroke: '#14171e', 'stroke-width': 2.5 }));
        const filled = x.stable;
        g.append(S('circle', { cx, cy, r: 5.5, fill: filled ? '#1f2933' : '#fff', stroke: '#1f2933', 'stroke-width': 2 }));
        g.append(S('circle', { cx, cy, r: 13, fill: 'transparent', stroke: 'none' }));
        const t = S('title'); t.textContent = `${x.name}: ${x.be_per_A_MeV.toFixed(2)} MeV per nucleon`; g.append(t);
        g.addEventListener('click', () => choose(x.id));
        svg.append(g);
      });
      placeLabels(shown, labelled, R);
      const R2 = R ? ` Arrows show the reaction ${R.label}.` : '';
      svg.setAttribute('aria-label', `Graph of binding energy per nucleon against mass number from A = ${V.a0} to ${V.a1}. The values rise steeply from hydrogen to a peak of about 8.8 MeV near iron-56 and nickel-62, then fall slowly to about 7.6 MeV for uranium.` + (sel ? ` Selected: ${byId[sel].name}.` : '') + R2);
      typeset(labs);
    }

    // Labels of the points: measured after KaTeX has drawn them, then put in the first free place round the point
    // (above, beside, below, a little farther), never over another label, a point, the axis titles or outside the plot.
    function placeLabels(shown, labelled, R) {
      typeset(labs);
      const pr = labs.getBoundingClientRect(), k = pr.width / W;
      if (!k) return;
      const rel = (e) => { const r = e.getBoundingClientRect(); return [(r.left - pr.left) / k, (r.top - pr.top) / k, (r.right - pr.left) / k, (r.bottom - pr.top) / k]; };
      const obst = [...labs.children].map(rel);
      shown.forEach((x) => { const cx = xs(x.A), cy = ys(x.be_per_A_MeV), r = x.id === sel ? 13 : 7; obst.push([cx - r, cy - r, cx + r, cy + r]); });
      const must = new Set([sel, ...(R ? [...R.before, ...R.after] : []), ...hl].filter(Boolean));
      const prio = [sel, ...(R ? [...R.before, ...R.after] : []), ...hl, ...(view === 'light' ? LIGHT : [])].filter((id, i, a) => id && a.indexOf(id) === i && labelled.has(id));
      const area = (b) => obst.reduce((t, o) => t + Math.max(0, Math.min(b[2], o[2]) - Math.max(b[0], o[0])) * Math.max(0, Math.min(b[3], o[3]) - Math.max(b[1], o[1])), 0);
      const free = (b) => area(b) < 3;
      const inside = (b) => b[0] >= X0 + 2 && b[2] <= W - 2 && b[1] >= 2 && b[3] <= Y1 - 2;
      prio.map((id) => shown.find((x) => x.id === id)).filter(Boolean).forEach((x) => {
        const span = h('span', { class: 'fx-lab fx-lab-abs', html: tex(x) });
        labs.append(span); typeset(span);
        const m = rel(span), w = m[2] - m[0] + 3, hh = m[3] - m[1] - 2 / k;
        const cx = xs(x.A), cy = ys(x.be_per_A_MeV), g = x.id === sel ? 14 : 8;
        const lower = shown.some((o) => o.A === x.A && o.be_per_A_MeV > x.be_per_A_MeV);
        const ring = (r) => {
          const q = r * 0.7;
          const up = [[cx + q, cy - q - hh], [cx - w / 2, cy - r - hh], [cx - q - w, cy - q - hh]], mid = [[cx + r, cy - hh / 2], [cx - r - w, cy - hh / 2]], down = [[cx + q, cy + q], [cx - w / 2, cy + r], [cx - q - w, cy + q]];
          return lower ? [...down, ...mid, ...up] : [...up, ...mid, ...down];
        };
        const cands = [g, g + 10, g + 22, g + 36, g + 54].flatMap(ring).map(([x0, y0]) => [x0, y0, x0 + w, y0 + hh]).filter(inside);
        let best = cands.find(free);
        if (!best && must.has(x.id) && cands.length) best = cands.reduce((a, b) => (area(b) < area(a) ? b : a));
        if (!best) { span.remove(); return; }
        span.style.left = ((best[0] + 1.5) / W) * 100 + '%'; span.style.top = ((best[1] - 1 / k) / H) * 100 + '%';
        // a thin leader line when the label had to move away from its point
        const nx = Math.max(best[0], Math.min(cx, best[2])), ny = Math.max(best[1], Math.min(cy, best[3])), dist = Math.hypot(nx - cx, ny - cy);
        if (dist > g + 6) svg.append(S('line', { x1: f(cx + ((nx - cx) / dist) * (g - 2), 1), y1: f(cy + ((ny - cy) / dist) * (g - 2), 1), x2: f(nx, 1), y2: f(ny, 1), stroke: '#6b7480', 'stroke-width': 1 }));
        obst.push(best);
      });
    }

    function showInfo() {
      if (!sel) { info.replaceChildren(h('p', { class: 'fx-note' }, 'Choose a nuclide from the list or click a point on the graph.')); return; }
      const x = byId[sel], B = x.A * x.be_per_A_MeV;
      info.replaceChildren(h('h4', { html: `${tex(x)} — ${x.name}` }),
        h('p', { html: x.A > 1 ? `$Z = ${x.Z}$, $N = ${x.N}$, $A = ${x.A}$. Binding energy per nucleon $B/A = ${x.be_per_A_MeV.toFixed(3)}\\ \\text{MeV}$, so the whole nucleus has $B = A \\cdot (B/A) = ${x.A} \\cdot ${x.be_per_A_MeV.toFixed(3)}\\ \\text{MeV} = ${sig(B)}\\ \\text{MeV}$.`
          : `A single nucleon: there is nothing to bind, so $B = 0$.` }),
        h('p', { html: `Atomic mass $m = ${x.mass_u.toFixed(6)}\\ \\text{u}$. ` + (x.stable ? '✓ Stable.' : `Radioactive, half-life ${x.half_life}.`) + (x.note ? ' ' + md(x.note) : '') }));
      typeset(info);
    }

    function showCalc() {
      const R = rx && reactions.find((r) => r.id === rx);
      if (!R) { calc.replaceChildren(); return; }
      const side = (ids) => {
        const cnt = {}; ids.forEach((i) => (cnt[i] = (cnt[i] || 0) + 1));
        return Object.entries(cnt).map(([i, c]) => (c > 1 ? c + '\\,' : '') + texFull(byId[i])).join(' + ');
      };
      const sum = (ids) => ids.reduce((s, i) => s + byId[i].mass_u, 0);
      const narrow = calc.getBoundingClientRect().width < 520;   // a phone: one term per line, so no equation needs a sideways scroll
      const terms = (ids) => { const cnt = {}; ids.forEach((i) => (cnt[i] = (cnt[i] || 0) + 1)); return Object.entries(cnt).map(([i, c]) => (c > 1 ? c + ' \\cdot ' : '') + byId[i].mass_u.toFixed(6) + '\\ \\text{u}').join(narrow ? ' \\\\ &\\quad + ' : ' + '); };
      const mb = sum(R.before), ma = sum(R.after), dm = mb - ma, Q = dm * uMeV;
      const Bsum = (ids) => ids.reduce((s, i) => s + byId[i].A * byId[i].be_per_A_MeV, 0);
      const Bb = Bsum(R.before), Ba = Bsum(R.after);
      const rows = (ids) => { const cnt = {}; ids.forEach((i) => (cnt[i] = (cnt[i] || 0) + 1)); return Object.entries(cnt).map(([i, c]) => h('tr', {}, h('td', { html: '$' + (c > 1 ? c + ' \\cdot ' : '') + texFull(byId[i]) + '$' }), h('td', { html: byId[i].name }), h('td', { class: 'num', html: `$${byId[i].mass_u.toFixed(6)}$` }))); };
      const tbl = (cap, ids, tot) => h('table', { class: 'fx-be-tbl' }, h('caption', {}, cap), h('thead', {}, h('tr', {}, h('th', {}, 'Particle'), h('th', {}, 'Name'), h('th', { class: 'num', html: 'Mass ($\\text{u}$)' }))),
        h('tbody', {}, rows(ids), h('tr', { class: 'fx-be-total' }, h('td', { colspan: 2 }, 'Total'), h('td', { class: 'num', html: `$${tot.toFixed(6)}$` }))));
      const fis = R.kind === 'fission';
      calc.replaceChildren(
        h('h4', {}, R.label),
        h('p', { class: 'fx-be-eq', html: `$$${side(R.before)} \\to ${side(R.after)}$$` }),
        h('div', { class: 'fx-be-tbls' }, tbl('Before', R.before, mb), tbl('After', R.after, ma)),
        h('ol', { class: 'fx-be-steps' },
          h('li', { html: `Mass before the reaction: $$\\begin{aligned} m_\\text{before} &= ${terms(R.before)} \\\\ &= ${mb.toFixed(6)}\\ \\text{u} \\end{aligned}$$` }),
          h('li', { html: `Mass after the reaction: $$\\begin{aligned} m_\\text{after} &= ${terms(R.after)} \\\\ &= ${ma.toFixed(6)}\\ \\text{u} \\end{aligned}$$` }),
          h('li', { html: `Mass difference: $$\\begin{aligned} \\Delta m &= m_\\text{before} - m_\\text{after} \\\\ &= ${dm.toFixed(6)}\\ \\text{u} \\end{aligned}$$` }),
          h('li', { html: `Energy released: $$\\begin{aligned} Q &= \\Delta m \\cdot 931.494\\ \\text{MeV/u} \\\\ &= ${dm.toFixed(6)}\\ \\text{u} ${narrow ? '\\\\ &\\quad' : ''} \\cdot 931.494\\ \\text{MeV/u} \\\\ &= ${sig(Q)}\\ \\text{MeV} \\end{aligned}$$` })),
        h('p', { html: `Check with binding energies: $$\\begin{aligned} Q &= B_\\text{after} - B_\\text{before} \\\\ &= ${sig(Ba)}\\ \\text{MeV} - ${sig(Bb)}\\ \\text{MeV} \\\\ &= ${sig(Ba - Bb)}\\ \\text{MeV} \\end{aligned}$$ The products are more tightly bound, so they have less mass, and the difference leaves as kinetic energy.` }),
        h('p', { class: 'fx-note', html: 'These are atomic masses (electrons included). The electrons cancel because the charge is the same before and after.'
          + (fis ? ` This particular split releases $${sig(Q)}\\ \\text{MeV}$ at once. The fragments are radioactive, and their later decays bring the total to about $200\\ \\text{MeV}$ per fission.` : '') }));
      typeset(calc);
    }

    function choose(id) { sel = id || null; pick.value = sel || ''; draw(); showInfo(); }
    function setView(v) { view = v; viewBtns.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.view === v))); draw(); }
    viewBtns.forEach((b) => b.addEventListener('click', () => setView(b.dataset.view)));
    pick.addEventListener('change', () => { const x = byId[pick.value]; if (x && view === 'light' && x.A > VIEWS.light.a1) setView('all'); choose(pick.value); });
    rsel.addEventListener('change', () => {
      rx = rsel.value || null; const R = rx && reactions.find((r) => r.id === rx);
      if (R) view = R.kind === 'fission' ? 'all' : 'light';
      viewBtns.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.view === view)));
      draw(); showCalc();
    });
    let lastW = 0;
    if (window.ResizeObserver) new ResizeObserver(() => { const cw = Math.round(svg.getBoundingClientRect().width); if (cw && Math.abs(cw - lastW) > 4) { lastW = cw; draw(); showCalc(); } }).observe(plot);
    if (d.reaction && reactions.find((r) => r.id === d.reaction)) { rsel.value = d.reaction; rsel.dispatchEvent(new Event('change')); }
    else draw();
    pick.value = sel || ''; showInfo();
    typeset(root);
  }
};
