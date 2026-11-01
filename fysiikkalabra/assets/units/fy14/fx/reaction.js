/* Fusion reaction and energy scales (data-fx="reaction"), with the facts from the data file named by data-src
   (units/fy14/data/nuclides.json: AME2020 masses, CODATA 2018 constants, "energy_scales").
   (a) "reaction": D + T → He-4 + n in six steps (Step back / Next step / Play): the nuclei approach, the Coulomb
       barrier (electric force, red #c92a2a) slows them, they fuse into helium-5, it breaks into an alpha particle and a
       neutron and the products fly apart. Velocity arrows are blue (#1971c2) and their lengths are proportional to the
       speeds (centre-of-mass frame, $m v$ equal and opposite). Every step has one sentence; the last shows how the
       energy is shared: with equal momenta $E_\text{k} = p^2 / (2m)$, so the neutron gets $m_\alpha / (m_\alpha + m_\text{n})$
       of $Q$, computed from the nuclear masses (atomic mass minus the electrons). With prefers-reduced-motion the
       steps change without animation and there is no Play button.
   (b) "scales": a bar chart on a logarithmic axis of the energy released per kilogram of fuel or per reaction
       (burning methane and coal, U-235 fission, D–T fusion), with each value's calculation and source.
   Every label is KaTeX laid over the SVG in HTML. Options: {part?: "reaction" | "scales" | "both" (default "both"),
   question?: text shown as a question box under the part(s), scales_mode?: "kg" | "reaction"}. */
window.FX.reaction = (el, d, A) => {
  const { h, md, typeset } = A;
  const NS = 'http://www.w3.org/2000/svg';
  const S = (tag, attrs) => { const e = document.createElementNS(NS, tag); Object.entries(attrs || {}).forEach(([k, v]) => e.setAttribute(k, v)); return e; };
  const root = h('div', { class: 'fx-rx' });
  el.append(root);
  A.data(el.getAttribute('data-src')).then(build).catch((e) => root.append(h('p', { class: 'fx-note' }, 'The data could not be loaded (' + e + ').')));
  const p3 = (v) => { const e = Math.floor(Math.log10(Math.abs(v))); const m = v / 10 ** e; return m.toFixed(2) + ' \\cdot 10^{' + e + '}'; };
  const g3 = (v) => (v >= 100 ? v.toFixed(0) : v >= 10 ? v.toFixed(1) : v.toFixed(2));

  function build(data) {
    const part = d.part || 'both', idp = el.id + '-';
    if (part !== 'scales') reaction(data);
    if (part !== 'reaction') scales(data);
    if (d.question) root.append(h('div', { class: 'fx-question' }, h('p', { class: 'fx-question-h' }, 'Think'), h('p', { html: md(d.question) })));
    root.append(h('p', { class: 'fx-note', html: `Masses: AME2020; constants: CODATA 2018 (checked ${data.checked}).` }));
    typeset(root);

    function reaction(data) {
      const by = Object.fromEntries(data.nuclides.map((x) => [x.id, x])), C = data.constants;
      const me = C.m_e_u, mD = by['H-2'].mass_u - me, mT = by['H-3'].mass_u - me, mA = by['He-4'].mass_u - 2 * me, mN = C.m_n_u;
      const dm = by['H-2'].mass_u + by['H-3'].mass_u - by['He-4'].mass_u - by.n.mass_u, Q = dm * C.u_MeV;
      const Q3 = Number(Q.toFixed(1)), share = mA / (mA + mN), En = share * Q3, Ea = Q3 - Number(En.toFixed(1));
      const ratio = mA / mN;
      const W = 560, H = 240, Y = 122, R = 11, CX = 280;
      const P = 'p', Nn = 'n';
      const SHAPES = {
        D: [[P, -9.5, 0], [Nn, 9.5, 0]],
        T: [[Nn, -10, 6.5], [Nn, 10, 6.5], [P, 0, -9]],
        C: [[Nn, -10, 10], [P, 10, 10], [Nn, 0, -1], [P, -10, -10], [Nn, 10, -10]],
        He: [[Nn, -9.5, 9.5], [P, 9.5, 9.5], [P, -9.5, -9.5], [Nn, 9.5, -9.5]],
        N: [[Nn, 0, 0]],
      };
      const TEX = { D: '^{2}_{1}\\text{H}', T: '^{3}_{1}\\text{H}', C: '^{5}_{2}\\text{He}', He: '^{4}_{2}\\text{He}', N: '^{1}_{0}\\text{n}' };
      const vD = 80, vT = vD * (mD / mT), vN = 150, vA = vN / ratio;
      const STEPS = [
        { b: { D: [80, 1], T: [480, 1] }, v: { D: vD, T: -vT },
          t: 'A deuterium nucleus (1 proton, 1 neutron) and a tritium nucleus (1 proton, 2 neutrons) move towards each other; the blue arrows are their velocities $\\overline{v}$.' },
        { b: { D: [206, 1], T: [354, 1] }, v: { D: vD / 2, T: -vT / 2 }, F: { D: -44, T: 44 }, barrier: true,
          t: 'Both nuclei are positive, so the electric force $\\overline{F}$ (red) pushes them apart and slows them down: this repulsion is the **Coulomb barrier**, and only very fast nuclei in a plasma of over 100 million kelvin get close enough (helped by quantum tunnelling).' },
        { b: { C: [CX, 1] },
          t: 'At a distance of about $10^{-15}\\ \\text{m}$ the strong nuclear force, which attracts all nucleons, wins and the nuclei fuse into one very short-lived nucleus, helium-5.' },
        { b: { He: [CX - 18, 1], N: [CX + 28, 1] }, burst: true,
          t: `Helium-5 breaks up at once into a helium-4 nucleus (an alpha particle) and a neutron, which together have less mass than the fuel: $\\Delta m = ${dm.toFixed(4)}\\ \\text{u}$, so $Q = ${Q3}\\ \\text{MeV}$ is released.` },
        { b: { He: [236, 1], N: [356, 1] }, v: { He: -vA, N: vN },
          t: 'The products fly apart in opposite directions; the total momentum stays zero, so $m_\\alpha v_\\alpha = m_\\text{n} v_\\text{n}$, and the neutron, about four times lighter, moves about four times faster.' },
        { b: { He: [236, 1], N: [356, 1] }, v: { He: -vA, N: vN }, share: true,
          t: `With equal momenta $p$, the kinetic energy $E_\\text{k} = \\dfrac{p^2}{2m}$ is larger for the lighter particle: the neutron carries $${En.toFixed(1)}\\ \\text{MeV}$ (about $80\\ \\%$) and the alpha particle $${Ea.toFixed(1)}\\ \\text{MeV}$.` },
      ];
      const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const svg = S('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img', class: 'fx-rx-svg' });
      const defs = S('defs');
      [['p', '#ff8a80', '#c92a2a', '#7f1d1d'], ['n', '#e9ecef', '#9aa1a9', '#4b5259']].forEach(([k, a, b, c]) => {
        const g = S('radialGradient', { id: idp + 'g' + k, cx: '35%', cy: '32%', r: '70%' });
        g.append(S('stop', { offset: '0%', 'stop-color': a }), S('stop', { offset: '55%', 'stop-color': b }), S('stop', { offset: '100%', 'stop-color': c }));
        defs.append(g);
      });
      svg.append(defs);
      const scene = S('g'); svg.append(scene);
      const labs = h('div', { class: 'fx-labs', 'aria-hidden': 'true' });
      const plot = h('div', { class: 'fx-plot fx-rx-plot' }, svg, labs);
      const text = h('p', { class: 'fx-rx-text', 'aria-live': 'polite' });
      const count = h('span', { class: 'fx-rx-count' });
      const back = h('button', { type: 'button', class: 'fx-btn fx-quiet' }, 'Step back');
      const next = h('button', { type: 'button', class: 'fx-btn' }, 'Next step');
      const play = h('button', { type: 'button', class: 'fx-btn fx-quiet', hidden: reduce }, 'Play');
      const bar = h('div', { class: 'fx-rx-share', hidden: true, role: 'img',
        'aria-label': `Energy shared: neutron ${En.toFixed(1)} MeV, ${(share * 100).toFixed(1)} percent; alpha particle ${Ea.toFixed(1)} MeV.` },
        h('div', { class: 'fx-rx-share-bar' }, h('div', { class: 'fx-rx-share-n', style: `width:${(share * 100).toFixed(1)}%` }), h('div', { class: 'fx-rx-share-a', style: `width:${(100 - share * 100).toFixed(1)}%` })),
        h('p', { class: 'fx-rx-share-key', html: `<span><span class="fx-swatch fx-rx-sw-n"></span> neutron $${En.toFixed(1)}\\ \\text{MeV}$ $(${(share * 100).toFixed(1)}\\ \\%)$</span> <span><span class="fx-swatch fx-rx-sw-a"></span> alpha particle $${Ea.toFixed(1)}\\ \\text{MeV}$ $(${(100 - share * 100).toFixed(1)}\\ \\%)$</span>` }));
      const why = h('details', { class: 'fx-rx-why' }, h('summary', {}, 'Why does the neutron get about 80 % of the energy?'),
        h('ol', { class: 'fx-be-steps' },
          h('li', { html: `Before the reaction the total momentum is (almost) zero, so after it $p_\\alpha = p_\\text{n} = p$ in opposite directions.` }),
          h('li', { html: `Kinetic energy $E_\\text{k} = \\dfrac{1}{2} m v^2 = \\dfrac{p^2}{2m}$, so $\\dfrac{E_\\text{n}}{E_\\alpha} = \\dfrac{m_\\alpha}{m_\\text{n}} = \\dfrac{${mA.toFixed(4)}\\ \\text{u}}{${mN.toFixed(4)}\\ \\text{u}} = ${ratio.toFixed(2)}$.` }),
          h('li', { html: `Nuclear masses: $m_\\alpha = m(^{4}\\text{He}) - 2 m_\\text{e} = ${by['He-4'].mass_u.toFixed(6)}\\ \\text{u} - 2 \\cdot ${me.toFixed(6)}\\ \\text{u} = ${mA.toFixed(6)}\\ \\text{u}$, $m_\\text{n} = ${mN.toFixed(6)}\\ \\text{u}$.` }),
          h('li', { html: `$E_\\text{n} = \\dfrac{m_\\alpha}{m_\\alpha + m_\\text{n}} \\cdot Q = ${share.toFixed(3)} \\cdot ${Q3}\\ \\text{MeV} = ${En.toFixed(1)}\\ \\text{MeV}$, and $E_\\alpha = Q - E_\\text{n} = ${Q3}\\ \\text{MeV} - ${En.toFixed(1)}\\ \\text{MeV} = ${Ea.toFixed(1)}\\ \\text{MeV}$.` }),
          h('li', { html: `Here $Q = \\Delta m \\cdot 931.494\\ \\text{MeV/u} = ${dm.toFixed(6)}\\ \\text{u} \\cdot 931.494\\ \\text{MeV/u} = ${Q.toFixed(2)}\\ \\text{MeV}$ from the atomic masses of $^{2}\\text{H}$, $^{3}\\text{H}$, $^{4}\\text{He}$ and the neutron (AME2020).` })),
        h('p', { class: 'fx-note' }, 'A neutron has no charge, so the magnetic field cannot hold it: it leaves the plasma and carries most of the energy to the wall, where it heats the blanket and breeds tritium. The alpha particle stays in the plasma and keeps it hot.'));
      const legend = h('p', { class: 'fx-note fx-rx-legend', html: '<span><span class="fx-key fx-key-v" aria-hidden="true"></span> velocity $\\overline{v}$ (length proportional to speed)</span> <span><span class="fx-key fx-key-f" aria-hidden="true"></span> electric force $\\overline{F}$</span> <span><span class="fx-iso-dot fx-iso-p" aria-hidden="true">+</span> proton</span> <span><span class="fx-iso-dot fx-iso-n" aria-hidden="true"></span> neutron</span>' });
      root.append(h('h4', { class: 'fx-rx-h' }, 'The D–T fusion reaction, step by step'),
        h('p', { class: 'fx-rx-eq', html: `$$\\begin{aligned} {}^{2}_{1}\\text{H} + {}^{3}_{1}\\text{H} \\to\\ &{}^{4}_{2}\\text{He}\\ (${Ea.toFixed(1)}\\ \\text{MeV}) \\\\ +\\ &{}^{1}_{0}\\text{n}\\ (${En.toFixed(1)}\\ \\text{MeV}) \\end{aligned}$$` }),
        plot, legend, h('div', { class: 'fx-actions fx-rx-ctl' }, back, next, play, count), text, bar, why);

      let step = 0, anim = null, timer = null;
      const nucleus = (key, x, op) => {
        const g = S('g', { opacity: op });
        SHAPES[key].slice().forEach(([k, dx, dy]) => {
          g.append(S('circle', { cx: (x + dx).toFixed(1), cy: (Y + dy).toFixed(1), r: R, fill: `url(#${idp}g${k})`, stroke: k === P ? '#7f1d1d' : '#4b5259', 'stroke-width': 0.8 }));
          if (k === P) g.append(S('path', { d: `M${(x + dx - 4.6).toFixed(1)} ${(Y + dy).toFixed(1)}h9.2M${(x + dx).toFixed(1)} ${(Y + dy - 4.6).toFixed(1)}v9.2`, stroke: '#fff', 'stroke-width': 1.8, 'stroke-linecap': 'round' }));
        });
        return g;
      };
      const arrow = (x1, y, len, col) => {
        const g = S('g'); const s = Math.sign(len), L = Math.abs(len); if (L < 2) return g;
        const x2 = x1 + len;
        g.append(S('line', { x1, y1: y, x2: x2 - s * 10, y2: y, stroke: col, 'stroke-width': 4, 'stroke-linecap': 'round' }));
        g.append(S('path', { d: `M${x2} ${y}l${-s * 14} -7v14Z`, fill: col }));
        return g;
      };
      const lab = (x, y, tex, cls) => labs.append(h('span', { class: 'fx-lab ' + (cls || ''), style: `left:${(x / W) * 100}%;top:${(y / H) * 100}%`, html: tex }));
      const render = (st, from, t) => {
        while (scene.firstChild) scene.firstChild.remove(); labs.replaceChildren();
        const keys = new Set([...Object.keys(st.b), ...(from ? Object.keys(from.b) : [])]);
        const pos = {};
        keys.forEach((k) => {
          const a = from && from.b[k], b = st.b[k];
          let x, o;
          if (a && b) { x = a[0] + (b[0] - a[0]) * t; o = 1; }
          else if (b) { x = b[0]; o = from ? t : 1; }
          else { x = a[0]; o = 1 - t; }
          if (from && !a && b && (k === 'C')) x = b[0];
          if (from && a && !b && (k === 'D' || k === 'T')) x = a[0] + (CX - a[0]) * t;
          if (from && !a && b && (k === 'He' || k === 'N')) x = CX + (b[0] - CX) * t;
          pos[k] = x; if (o > 0.02) scene.append(nucleus(k, x, o.toFixed(2)));
        });
        if (from && t < 1) return;
        if (st.burst) {
          const star = S('path', { d: Array.from({ length: 16 }, (_, i) => { const r = i % 2 ? 26 : 58, a = (i * Math.PI) / 8; return (i ? 'L' : 'M') + (CX + 5 + r * Math.cos(a)).toFixed(1) + ' ' + (Y + r * Math.sin(a)).toFixed(1); }).join('') + 'Z', fill: '#ffe066', stroke: '#f08c00', 'stroke-width': 1.5, opacity: 0.85 });
          scene.insertBefore(star, scene.firstChild);
          lab(CX + 5, Y - 76, `$Q = ${Q3}\\ \\text{MeV}$`, 'fx-lab-strong');
        }
        if (st.barrier) {
          scene.insertBefore(S('rect', { x: CX - 34, y: Y - 70, width: 68, height: 140, rx: 8, fill: '#ffe3e3', stroke: '#c92a2a', 'stroke-dasharray': '6 4' }), scene.firstChild);
          lab(CX, Y - 86, '$\\text{Coulomb barrier}$', 'fx-lab-f');
        }
        Object.entries(st.v || {}).forEach(([k, v]) => {
          const x0 = pos[k] + Math.sign(v) * (k === 'N' ? 14 : 24);
          scene.append(arrow(x0, Y - 34, v, '#1971c2'));
          lab(x0 + v / 2, Y - 52, k === 'N' ? '$\\overline{v}_\\text{n}$' : k === 'He' ? '$\\overline{v}_\\alpha$' : '$\\overline{v}$', 'fx-lab-v');
        });
        Object.entries(st.F || {}).forEach(([k, F]) => {
          const x0 = pos[k] + Math.sign(F) * 24;
          scene.append(arrow(x0, Y + 34, F, '#c92a2a'));
          lab(x0 + F / 2, Y + 54, '$\\overline{F}$', 'fx-lab-f');
        });
        Object.entries(st.b).forEach(([k, [x]]) => lab(pos[k] != null ? pos[k] : x, Y + (st.F ? 82 : 52), `$${TEX[k]}$`));
        typeset(labs);
      };
      const plain = (t) => t.replace(/\*\*/g, '').replace(/\$([^$]*)\$/g, (m, x) => x.replace(/\\dfrac\{([^}]*)\}\{([^}]*)\}/g, '$1 / ($2)').replace(/\\overline\{(\w)\}/g, '$1').replace(/\\text\{([^}]*)\}/g, '$1')
        .replace(/\\Delta /g, 'delta ').replace(/\\alpha/g, 'alpha').replace(/\\cdot 10\^\{(-?\d+)\}/g, ' times 10 to the power $1').replace(/10\^\{(-?\d+)\}/g, '10 to the power $1').replace(/\^2/g, ' squared').replace(/\\ /g, ' ').replace(/[\\{}_^]/g, ''));
      const show = (i, animate) => {
        const prev = step; step = Math.max(0, Math.min(STEPS.length - 1, i));
        const st = STEPS[step];
        text.innerHTML = md(st.t); count.textContent = `Step ${step + 1} of ${STEPS.length}`;
        back.disabled = step === 0; next.disabled = step === STEPS.length - 1;
        bar.hidden = !st.share;
        svg.setAttribute('aria-label', `Step ${step + 1} of ${STEPS.length}: ` + plain(st.t));
        typeset(text); typeset(bar);
        if (anim) cancelAnimationFrame(anim);
        if (!animate || reduce || step !== prev + 1) { render(st); return; }
        const from = STEPS[prev], t0 = performance.now(), dur = 900;
        const tick = (now) => { const t = Math.min(1, (now - t0) / dur), e = t < 0.5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2; render(st, from, e); if (t < 1) anim = requestAnimationFrame(tick); else { anim = null; render(st); } };
        anim = requestAnimationFrame(tick);
      };
      const stop = () => { clearTimeout(timer); timer = null; play.textContent = 'Play'; play.setAttribute('aria-pressed', 'false'); };
      back.addEventListener('click', () => { stop(); show(step - 1, false); });
      next.addEventListener('click', () => { stop(); show(step + 1, true); });
      play.addEventListener('click', () => {
        if (timer) { stop(); return; }
        play.textContent = 'Pause'; play.setAttribute('aria-pressed', 'true');
        if (step === STEPS.length - 1) show(0, false);
        const go = () => { if (step >= STEPS.length - 1) { stop(); return; } show(step + 1, true); timer = setTimeout(go, 3400); };
        timer = setTimeout(go, 600);
      });
      show(0, false);
    }

    function scales(data) {
      const E = data.energy_scales, items = E.items;
      const nb = Object.fromEntries(data.nuclides.map((x) => [x.id, x])), mU = nb['U-235'].mass_u, mF = nb['H-2'].mass_u + nb['H-3'].mass_u;
      let mode = d.scales_mode === 'reaction' ? 'reaction' : 'kg';
      const btns = [['kg', 'Per kilogram of fuel'], ['reaction', 'Per reaction or molecule']].map(([k, t]) => h('button', { type: 'button', class: 'fx-step', 'data-mode': k, 'aria-pressed': String(k === mode) }, t));
      const chart = h('div', { class: 'fx-sc', role: 'img' });
      const say = h('p', { class: 'fx-sc-say', 'aria-live': 'polite' });
      const how = h('details', { class: 'fx-rx-why' }, h('summary', {}, 'Where the numbers come from'),
        h('ul', { class: 'fx-sc-src' }, items.map((it) => h('li', {}, h('strong', {}, it.label + ': '), h('span', { html: it.how }), h('span', { class: 'fx-note fx-sc-cite' }, ' Source: ' + it.source)))));
      root.append(h('h4', { class: 'fx-rx-h' }, 'Energy scales: chemical and nuclear fuels'),
        h('div', { class: 'fx-steps', role: 'group', 'aria-label': 'Compare' }, btns), chart, say, how);
      const fmtE = (it) => {
        if (mode === 'kg') return `$${p3(it.per_kg_J)}\\ \\text{J/kg}$`;
        const v = it.per_reaction_eV; return v >= 1e6 ? `$${g3(v / 1e6)}\\ \\text{MeV}$` : `$${g3(v)}\\ \\text{eV}$`;
      };
      const draw = () => {
        const val = (it) => (mode === 'kg' ? it.per_kg_J : it.per_reaction_eV);
        const rows = items.filter((it) => val(it));
        const lo = Math.floor(Math.log10(Math.min(...rows.map(val)))) - 1, hi = Math.ceil(Math.log10(Math.max(...rows.map(val))) + 0.15), every = hi - lo > 6 ? 2 : 1;
        const pos = (v) => ((Math.log10(v) - lo) / (hi - lo)) * 100;
        const ticks = []; for (let e = lo; e <= hi; e += every) ticks.push(h('span', { class: 'fx-sc-tick', style: `left:${pos(10 ** e)}%`, html: `$10^{${e}}$` }));
        const grid = []; for (let e = lo; e <= hi; e++) grid.push(h('span', { class: 'fx-sc-grid', style: `left:${pos(10 ** e)}%` }));
        chart.replaceChildren(
          ...rows.map((it) => h('div', { class: 'fx-sc-row' },
            h('span', { class: 'fx-sc-lab' }, it.label, h('span', { class: 'fx-sc-kind' }, it.kind === 'nuclear' ? ' nuclear' : ' chemical')),
            h('span', { class: 'fx-sc-track' }, ...grid.map((g) => g.cloneNode()), h('span', { class: 'fx-sc-bar fx-sc-' + it.kind, style: `width:${pos(val(it)).toFixed(2)}%` })),
            h('span', { class: 'fx-sc-val', html: fmtE(it) }))),
          h('div', { class: 'fx-sc-row fx-sc-axisrow' }, h('span', {}), h('span', { class: 'fx-sc-axis' }, ticks), h('span', {})),
          h('p', { class: 'fx-sc-unit', html: mode === 'kg' ? 'Energy per kilogram of fuel in $\\text{J/kg}$ (logarithmic axis: each step is ten times more)' : 'Energy per reaction or per molecule in $\\text{eV}$ (logarithmic axis: each step is ten times more)' }));
        chart.setAttribute('aria-label', 'Bar chart on a logarithmic axis. ' + rows.map((it) => it.label + ': ' + (mode === 'kg' ? it.per_kg_J.toExponential(2) + ' joules per kilogram' : it.per_reaction_eV.toExponential(2) + ' electronvolts')).join('; ') + '.');
        const by = Object.fromEntries(items.map((it) => [it.id, it]));
        say.innerHTML = mode === 'kg'
          ? `Per kilogram, D–T fusion releases about $${p3(by.dt.per_kg_J / by.methane.per_kg_J)}$ times as much energy as burning methane, and about $${g3(by.dt.per_kg_J / by.fission.per_kg_J)}$ times as much as the fission of uranium-235.`
          : `One fission ($${g3(by.fission.per_reaction_eV / 1e6)}\\ \\text{MeV}$) releases more than one D–T reaction ($${g3(by.dt.per_reaction_eV / 1e6)}\\ \\text{MeV}$), but a uranium-235 nucleus is about $${g3(mU / mF)}$ times heavier than the fuel of one fusion reaction, so per kilogram fusion wins. Both are millions of times more than a chemical reaction.`;
        typeset(chart); typeset(say);
      };
      btns.forEach((b) => b.addEventListener('click', () => { mode = b.dataset.mode; btns.forEach((x) => x.setAttribute('aria-pressed', String(x === b))); draw(); }));
      draw();
    }
  }
};
