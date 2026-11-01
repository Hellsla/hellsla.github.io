/* ITER component explorer (data-fx="iter"): an original cut-away cross-section of the ITER tokamak, drawn here from
   ITER's published dimensions (plasma major radius 6.2 m, vacuum vessel 19.4 m wide and 11.4 m tall, cryostat 28 m
   inside diameter and about 30 m tall, coil counts), approximately to scale; coil positions and shapes are simplified.
   The machine's axis is in the middle; both halves are drawn, with diagnostics in the ports on the left and heating
   and a cryopump in the ports on the right.
   - Every part is a hotspot: a focusable SVG button (Enter or Space) with a numbered marker, and the same part is a
     button in the list under the drawing. Selecting one shows its panel: what it does, a key number (LaTeX), why it
     is hard, its sources and the date they were checked.
   - mode "quiz": the student is asked to find parts by description (a round of `count` parts, default 6, in a seeded
     order); feedback in words with ✓/✗, the part's panel after a right answer, a score at the end.
   - Below (explore mode, unless about: false): what Q means (bars to scale), the 2024 baseline schedule, the Members
     and the site.
   The facts live in the data file named by the element's data-src (units/fy14/data/iter.json): parts[] {id, name,
   does, number, number_note?, hard, find, hint, sources[]}, q, schedule, members, site, checked.
   Data on the element: {mode?: "explore"|"quiz", count?: number of quiz questions, about?: true|false}. */
window.FX.iter = (el, d, A) => {
  const { h, md, typeset, shuffle, store } = A;
  const src = el.getAttribute('data-src');
  const root = h('div', { class: 'ip' }); el.append(root);
  A.data(src).then(build).catch((e) => root.append(h('p', { class: 'fx-note' }, 'The ITER data could not be loaded (' + e + '). Open the page from the web site.')));

  /* ---------- geometry in metres (R to the right, Z up) ---------- */
  const K = 19.5, OX = 320, OY = 18 * K, VW = 640, VH = 32 * K;
  const P = (R, Z) => [OX + R * K, OY - Z * K];
  const f = (v) => Math.round(v * 1000) / 1000;
  const path = (pts, close = true) => 'M' + pts.map((p) => f(p[0]) + ' ' + f(p[1])).join('L') + (close ? 'Z' : '');
  const area = (pts) => pts.reduce((s, p, i) => { const q = pts[(i + 1) % pts.length]; return s + p[0] * q[1] - q[0] * p[1]; }, 0) / 2;
  const ccw = (pts) => (area(pts) < 0 ? pts.slice().reverse() : pts);
  const offset = (pts, dd) => pts.map((p, i) => {   // outward for a counter-clockwise outline
    const a = pts[(i - 1 + pts.length) % pts.length], b = pts[(i + 1) % pts.length];
    const tx = b[0] - a[0], tz = b[1] - a[1], l = Math.hypot(tx, tz) || 1;
    return [p[0] + dd * tz / l, p[1] - dd * tx / l];
  });
  const miller = (Rc, Am, Zc, ku, kl, dl, n) => Array.from({ length: n }, (_, i) => {
    const t = 2 * Math.PI * i / n, s = Math.sin(t);
    return [Rc + Am * Math.cos(t + dl * s), Zc + (s >= 0 ? ku : kl) * Am * s];
  });
  const bez = (p0, p1, p2, p3, n) => Array.from({ length: n }, (_, i) => {
    const t = i / n, u = 1 - t;
    return [0, 1].map((k) => u * u * u * p0[k] + 3 * u * u * t * p1[k] + 3 * u * t * t * p2[k] + t * t * t * p3[k]);
  });
  const spline = (W, n) => {   // a closed Catmull-Rom spline through the waypoints
    const out = [];
    for (let i = 0; i < W.length; i++) {
      const p0 = W[(i - 1 + W.length) % W.length], p1 = W[i], p2 = W[(i + 1) % W.length], p3 = W[(i + 2) % W.length];
      for (let j = 0; j < n; j++) {
        const t = j / n, t2 = t * t, t3 = t2 * t;
        out.push([0, 1].map((k) => 0.5 * (2 * p1[k] + (-p0[k] + p2[k]) * t + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2 + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3)));
      }
    }
    return out;
  };

  const VVo = miller(6.375, 3.275, 0.4, 1.6, 1.85, 0.42, 240);   // vacuum vessel, outer surface
  const VVi = offset(VVo, -0.6), FW = offset(VVo, -1.05), VVm1 = offset(VVo, -0.07), VVm2 = offset(VVo, -0.53);
  const TSv = offset(VVo, 0.2);
  // the blanket covers the wall except at the bottom, where the divertor sits
  const gap = FW.map((p) => p[1] < -2.55);
  const i0 = gap.findIndex((g, i) => g && !gap[(i - 1 + gap.length) % gap.length]);   // first index of the bottom gap
  const i1 = gap.findIndex((g, i) => !g && gap[(i - 1 + gap.length) % gap.length]);   // first index after it
  const ring = (arr, a, b) => { const out = []; for (let i = a; ; i = (i + 1) % arr.length) { out.push(arr[i]); if (i === b) break; } return out; };
  const blankOut = ring(VVi, i1, (i0 - 1 + VVi.length) % VVi.length), blankIn = ring(FW, i1, (i0 - 1 + FW.length) % FW.length);
  const fwOut = FW[(i0 - 1 + FW.length) % FW.length], fwIn = FW[i1];   // where the blanket ends (inboard / outboard ends of the gap)
  const A0 = fwOut[0] < fwIn[0] ? fwOut : fwIn, B0 = fwOut[0] < fwIn[0] ? fwIn : fwOut;   // A0 inboard end, B0 outboard end
  const floor = ring(VVi, (i0 - 1 + VVi.length) % VVi.length, i1);   // the vessel floor under the divertor
  const floorIO = floor[0][0] < floor[floor.length - 1][0] ? floor : floor.slice().reverse();
  const X = [5.24, -3.35];
  const divTop = [A0, [4.35, -3.3], [4.5, -4.2], [4.78, -4.32], [4.88, -3.95], [5.25, -3.78], [5.62, -3.95], [5.72, -4.42], [6.0, -4.6], [6.45, -3.75], [6.75, -3.2], B0];
  const divBody = divTop.concat(floorIO.slice().reverse());
  const plasma = [];
  for (let i = 0; i <= 60; i++) { const t = Math.PI * i / 60, s = Math.sin(t); plasma.push([6.2 + 2 * Math.cos(t + 0.45 * s), 0.5 + 3.5 * s]); }
  plasma.push(...bez([4.2, 0.5], [4.2, -1.2], [4.44, -2.55], X, 24), ...bez(X, [6.14, -2.45], [8.2, -1.4], [8.2, 0.5], 30));
  const flux = [0.72, 0.45, 0.2].map((k) => miller(6.45, 1.95 * k, 0.65, 1.62, 1.62, 0.3 * k, 90));
  const TFo = ccw(spline([[2.15, 4.8], [2.6, 6.3], [3.6, 6.85], [5.0, 7.05], [6.5, 6.9], [7.9, 6.0], [9.4, 4.6], [10.6, 2.6], [11.1, 0.5], [10.7, -1.8], [9.7, -3.9], [8.3, -5.6], [6.6, -6.55], [5.0, -6.75], [3.5, -6.45], [2.55, -5.7], [2.15, -4.6], [2.15, -2], [2.15, 0], [2.15, 2.5]], 8));
  const TFi = offset(TFo, -0.82);
  const PF = [[3.94, 7.57, 0.97, 0.98], [8.29, 6.54, 0.64, 0.7], [11.99, 3.28, 0.7, 0.96], [11.96, -2.23, 0.64, 0.97], [8.39, -6.73, 0.82, 0.97], [4.33, -7.47, 1.55, 1.11]];
  const rect = (R, Z, w, hh) => [[R - w / 2, Z - hh / 2], [R + w / 2, Z - hh / 2], [R + w / 2, Z + hh / 2], [R - w / 2, Z + hh / 2]];
  const cryo = 'M0 -12.4L14.3 -12.4L14.3 13C14.3 15.8 8 17.6 0 17.6L0 17.3C7.8 17.3 14 15.6 14 13L14 -11.2L0 -11.2Z';
  const cryoTS = 'M0 -10.75L13.55 -10.75L13.55 12.95C13.55 15.15 7.6 16.75 0 16.85';
  const upPort = [[5.9, 5.1], [7.6, 4.85], [7.6, 16.9], [5.9, 17.3]];
  const eqPort = [[9.45, -0.6], [15.2, -0.6], [15.2, 1.8], [9.45, 1.8]];
  const loPort = [[7.9, -4.7], [14.6, -6.5], [14.6, -7.8], [6.7, -5.5]];
  const rot = (cx, cz, w, hh, ang) => [[-1, -1], [1, -1], [1, 1], [-1, 1]].map(([a, b]) => { const x = a * w / 2, z = b * hh / 2, c = Math.cos(ang), s = Math.sin(ang); return [cx + x * c - z * s, cz + x * s + z * c]; });
  const pumpAng = Math.atan2(-1.8, 6.7), pump = rot(11.3, -6.22, 2.6, 1.9, pumpAng);

  /* ---------- the drawing, part by part (both halves unless a part says otherwise) ---------- */
  const both = (s) => s + `<g transform="scale(-1,1)">${s}</g>`;
  const NS = 'vector-effect="non-scaling-stroke"';
  const DRAW = {
    cryostat: () => both(`<path d="M0 -11.2L14 -11.2L14 13C14 15.6 7.8 17.3 0 17.3Z" fill="#f3f5f8"/><path class="ip-hl" d="${cryo}" fill="#dfe4ea" stroke="#5c6b7a" stroke-width="1.2" ${NS}/>`),
    shield: () => both(`<path class="ip-hit" d="${path(TSv)}" fill="none" stroke="transparent" stroke-width="12" ${NS}/><path class="ip-hit" d="${cryoTS}" fill="none" stroke="transparent" stroke-width="12" ${NS}/><path class="ip-hl" d="${path(TSv)}" fill="none" stroke="#7d93a8" stroke-width="2.6" stroke-dasharray="7 2" ${NS}/><path class="ip-hl" d="${cryoTS}" fill="none" stroke="#7d93a8" stroke-width="2.6" stroke-dasharray="7 2" ${NS}/>`),
    tf: () => both(`<path class="ip-hl" d="${path(TFo)}${path(TFi)}" fill="#efc9a6" fill-rule="evenodd" stroke="#a5561f" stroke-width="1.2" ${NS}/><path d="${path(offset(TFo, -0.41))}" fill="none" stroke="#c8763f" stroke-width=".8" stroke-dasharray="3 3" ${NS}/>`),
    pf: () => both(PF.map(([R, Z, w, hh]) => `<path class="ip-hl" d="${path(rect(R, Z, w, hh))}" fill="#a9bccd" stroke="#3f5366" stroke-width="1.2" ${NS}/><path d="${path(rect(R, Z, w * 0.6, hh * 0.6))}" fill="none" stroke="#6d8296" stroke-width=".7" ${NS}/>`).join('')),
    cs: () => both(Array.from({ length: 6 }, (_, m) => { const hm = (13 - 5 * 0.06) / 6, z0 = -6 + m * (hm + 0.06); return `<path class="ip-hl" d="${path(rect(1.69, z0 + hm / 2, 0.78, hm))}" fill="#b07a45" stroke="#6b3f17" stroke-width="1.1" ${NS}/>`; }).join('')),
    ports: () => both(`<path class="ip-hl" d="${path(upPort)}" fill="#f3f5f7" stroke="#6b7a88" stroke-width="1.1" ${NS}/><path class="ip-hl" d="${path(eqPort)}" fill="#f3f5f7" stroke="#6b7a88" stroke-width="1.1" ${NS}/><path class="ip-hl" d="${path(loPort)}" fill="#f3f5f7" stroke="#6b7a88" stroke-width="1.1" ${NS}/>`
      + `<path d="${path(rect(15.05, 0.6, 0.3, 2.9))}" fill="#c9d1d9" stroke="#6b7a88" stroke-width="1" ${NS}/><path d="${path(rect(6.75, 17.15, 2.1, 0.3))}" fill="#c9d1d9" stroke="#6b7a88" stroke-width="1" ${NS}/><path d="${path(rot(14.45, -7.15, 0.3, 1.6, pumpAng))}" fill="#c9d1d9" stroke="#6b7a88" stroke-width="1" ${NS}/>`),
    vessel: () => both(`<path class="ip-hl" d="${path(VVo)}${path(VVi)}" fill="#8e9baa" fill-rule="evenodd" stroke="#3d4955" stroke-width="1.2" ${NS}/><path d="${path(VVm1)}${path(VVm2)}" fill="#cfe3f2" fill-rule="evenodd" stroke="none"/>`
      + Array.from({ length: 24 }, (_, k) => { const i = Math.round(k * VVo.length / 24); return `<path d="${path([VVm1[i], VVm2[i]], false)}" stroke="#8e9baa" stroke-width=".8" ${NS}/>`; }).join('')),
    blanket: () => {
      let s = `<path class="ip-hl" d="${path(blankOut.concat(blankIn.slice().reverse()))}" fill="#d8c79f" stroke="#7a6a45" stroke-width="1" ${NS}/><path d="${path(blankIn, false)}" fill="none" stroke="#3b3f45" stroke-width="2.4" ${NS}/>`;
      for (let i = 0; i < blankIn.length; i += 11) s += `<path d="${path([blankIn[i], blankOut[i]], false)}" stroke="#7a6a45" stroke-width=".9" ${NS}/>`;
      return both(s);
    },
    divertor: () => both(`<path class="ip-hl" d="${path(divBody)}" fill="#c3cbd3" stroke="#4a5562" stroke-width="1" ${NS}/><path d="${path([[4.35, -3.3], [4.5, -4.2]], false)}M5.72 -4.42L6 -4.6L6.45 -3.75M4.88 -3.95L5.25 -3.78L5.62 -3.95" fill="none" stroke="#2f343a" stroke-width="3.2" stroke-linecap="round" ${NS}/>`),
    plasma: () => both(`<path class="ip-hl" d="${path(plasma)}" fill="url(#ip-plasma)" stroke="#c2255c" stroke-width="1.4" ${NS}/>` + flux.map((q) => `<path d="${path(q)}" fill="none" stroke="#fff" stroke-opacity=".8" stroke-width=".9" ${NS}/>`).join('')
      + `<path d="M${X[0]} ${X[1]}L4.45 -3.95M${X[0]} ${X[1]}L5.9 -4.35M${X[0]} ${X[1]}L4.95 -3.05M${X[0]} ${X[1]}L5.55 -3.05" fill="none" stroke="#c2255c" stroke-width="1.2" stroke-dasharray="4 3" ${NS}/>`),
    heating: () => `<path class="ip-hl" d="${path(rect(10.25, 0.6, 2.0, 2.1))}" fill="#ffd8bf" stroke="#b5400a" stroke-width="1.2" ${NS}/>`
      + [9.45, 9.75, 10.05].map((r) => `<path d="M${r} -0.25V1.45" stroke="#b5400a" stroke-width="2.2" ${NS}/>`).join('')
      + `<path class="ip-hl" d="${path(rect(6.75, 6.9, 1.4, 2.6))}" fill="#ffd8bf" stroke="#b5400a" stroke-width="1.2" ${NS}/><path d="M6.4 8.1L7.05 5.75M6.75 16.9V8.4" stroke="#b5400a" stroke-width="1.6" stroke-dasharray="5 3" ${NS}/>`
      + `<path d="M16.2 0.6H11.4" stroke="#b5400a" stroke-width="3" stroke-dasharray="8 4" ${NS}/><path d="M11.3 0.6L11.95 1.0L11.95 0.2Z" fill="#b5400a"/>`,
    diagnostics: () => `<path class="ip-hl" d="${path(rect(-10.25, 0.6, 2.0, 2.1))}" fill="#c5efe9" stroke="#0b7285" stroke-width="1.2" ${NS}/>`
      + [[-10.9, 1.1], [-10.9, 0.1], [-9.9, 1.1], [-9.9, 0.1]].map(([r, z]) => `<path d="${path(rect(r, z, 0.7, 0.7))}" fill="#fff" stroke="#0b7285" stroke-width=".9" ${NS}/>`).join('')
      + `<path class="ip-hl" d="${path(rect(-6.75, 6.9, 1.4, 2.6))}" fill="#c5efe9" stroke="#0b7285" stroke-width="1.2" ${NS}/>`
      + `<path d="M-9.3 0.9L-6.4 2.6M-9.3 0.6L-5.5 0.4M-9.3 0.3L-6.8 -1.9M-6.75 5.6L-6.2 2.3M-6.75 5.6L-5.0 1.0" fill="none" stroke="#0b7285" stroke-width="1.3" stroke-dasharray="4 3" ${NS}/>`,
    cryopumps: () => `<path class="ip-hl" d="${path(pump)}" fill="#d0ebff" stroke="#1864ab" stroke-width="1.2" ${NS}/>` + [-0.8, -0.4, 0, 0.4, 0.8].map((x) => `<path d="${path(rot(11.3 + x * Math.cos(pumpAng), -6.22 + x * Math.sin(pumpAng), 0.06, 1.5, pumpAng))}" fill="#1864ab"/>`).join(''),
  };
  const ORDER = ['cryostat', 'shield', 'tf', 'pf', 'cs', 'ports', 'vessel', 'blanket', 'divertor', 'plasma', 'heating', 'diagnostics', 'cryopumps'];
  const MARK = { plasma: [6.9, 1.6], blanket: [-8.82, 2.2], divertor: [-5.25, -4.6], vessel: [-9.35, -2.4], tf: [10.32, -2.6], pf: [11.99, 3.28], cs: [1.69, 3.6], shield: [13.55, 8.5], cryostat: [-14.15, 8.5], ports: [-13.2, 0.6], heating: [10.25, 0.6], diagnostics: [-10.4, 3.0], cryopumps: [11.3, -6.22] };

  function build(data) {
    const parts = data.parts.filter((p) => DRAW[p.id]);
    const byId = Object.fromEntries(parts.map((p, i) => [p.id, { ...p, n: i + 1 }]));
    const mode = d.mode === 'quiz' ? 'quiz' : 'explore';
    const checked = (() => { try { return new Date(data.checked + 'T12:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); } catch (e) { return data.checked; } })();

    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', `0 0 ${VW} ${VH}`); svg.setAttribute('class', 'ip-svg'); svg.setAttribute('role', 'group');
    svg.setAttribute('aria-label', 'Cross-section of the ITER tokamak with ' + parts.length + ' selectable parts');
    let s = `<title>Cross-section of the ITER tokamak</title><desc>A cut through the whole machine, axis in the middle: the cryostat outside, inside it the D-shaped toroidal field coils, six poloidal field coils, the central solenoid next to the axis, the double-walled vacuum vessel lined with blanket modules, the divertor at the bottom and the D-shaped pink plasma. Ports lead out at the top, the middle and the bottom; diagnostics are drawn on the left, heating and a cryopump on the right.</desc>`;
    s += `<defs><radialGradient id="${el.id}-pl" gradientUnits="userSpaceOnUse" cx="6.45" cy="0.7" r="3.6"><stop offset="0" stop-color="#fff3bf"/><stop offset=".35" stop-color="#ffc9c9"/><stop offset=".8" stop-color="#f783ac"/><stop offset="1" stop-color="#e64980"/></radialGradient></defs>`;
    s += `<g transform="translate(${OX},${OY}) scale(${K},${-K})">`;
    s += `<path d="M0 -11.2V17.3" stroke="#6b7480" stroke-width="1" stroke-dasharray="8 4 2 4" ${NS}/>`;
    ORDER.forEach((id) => {
      const p = byId[id]; const g = DRAW[id]().replace(/url\(#ip-plasma\)/g, `url(#${el.id}-pl)`);
      s += p ? `<g class="ip-part" data-id="${id}" tabindex="0" role="button" aria-pressed="false" aria-label="${p.n}. ${p.name}">${g}</g>` : g;
    });
    s += `<path d="M-14 -13.4H-9" stroke="#14171e" stroke-width="2" ${NS}/><path d="M-14 -13.65V-13.15M-9 -13.65V-13.15" stroke="#14171e" stroke-width="2" ${NS}/></g>`;
    // markers, in viewBox units so that they stay round; each belongs to its part's button
    svg.innerHTML = s;
    parts.forEach((p) => {
      const [R, Z] = MARK[p.id], [x, y] = P(R, Z), g = svg.querySelector(`.ip-part[data-id="${p.id}"]`);
      const m = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      m.setAttribute('class', 'ip-mk'); m.setAttribute('aria-hidden', 'true');
      m.innerHTML = `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="11"/><text x="${x.toFixed(1)}" y="${(y + 0.5).toFixed(1)}">${byId[p.id].n}</text>`;
      svg.append(m); m.addEventListener('click', () => choose(p.id, false));
      g.addEventListener('click', () => choose(p.id, false));
      g.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); choose(p.id, true); } });
      g.addEventListener('focus', () => m.classList.add('focus')); g.addEventListener('blur', () => m.classList.remove('focus'));
      p.mark = m; p.g = g;
    });
    const [sx, sy] = P(-11.5, -13.4);
    const fig = h('div', { class: 'ip-fig' }, svg, h('span', { class: 'ip-scale', style: `left:${(sx / VW * 100).toFixed(1)}%;top:${((sy - 24) / VH * 100).toFixed(1)}%`, html: '$5\\ \\text{m}$' }));

    const list = h('ul', { class: 'ip-list', 'aria-label': 'Parts of ITER' }, parts.map((p) => h('li', { 'data-id': p.id },
      h('button', { type: 'button', 'aria-pressed': 'false', onclick: () => choose(p.id, true) }, h('b', { 'aria-hidden': 'true' }, String(byId[p.id].n)), p.name))));
    const panel = h('div', { class: 'ip-panel', tabindex: '-1', 'aria-live': 'polite' });
    const note = h('p', { class: 'fx-note', html: md(data.drawing_note) });

    const showPanel = (id, focus) => {
      const p = byId[id];
      panel.replaceChildren(h('h4', {}, `${p.n}. ${p.name}`), h('dl', {},
        h('dt', {}, 'What it does'), h('dd', { html: md(p.does) }),
        h('dt', {}, 'Key number'), h('dd', { class: 'ip-num', html: md(p.number) }), ...(p.number_note ? [h('dd', { class: 'fx-note', html: md(p.number_note) })] : []),
        h('dt', {}, 'Why it is hard'), h('dd', { html: md(p.hard) }),
        h('dd', { class: 'ip-src' }, 'Sources: ', ...p.sources.flatMap((x, i) => [i ? ', ' : '', h('a', { href: x.url }, x.title)]), ` (checked ${checked}).`)));
      typeset(panel);
      if (focus) panel.focus({ preventScroll: true });
    };
    const mark = (id) => {
      svg.classList.toggle('has-sel', !!id);
      parts.forEach((p) => { const on = p.id === id; p.g.classList.toggle('sel', on); p.g.setAttribute('aria-pressed', String(on)); p.mark.classList.toggle('sel', on); });
      list.querySelectorAll('li').forEach((li) => li.querySelector('button').setAttribute('aria-pressed', String(li.dataset.id === id)));
      // the selected part's marker on top of the others
      const m = id && byId[id] && parts.find((p) => p.id === id).mark; if (m) svg.append(m);
    };

    // quiz state
    const N = Math.min(parts.length, d.count || 6);
    let qs = [], qi = 0, firstTry = 0, tried = false;
    const qBox = h('div', { class: 'ip-quiz', 'aria-live': 'polite' });
    const qOut = h('output', {});
    const qNext = h('button', { type: 'button', class: 'fx-btn', hidden: true, onclick: () => { qi++; ask(); } }, 'Next part →');
    const startQuiz = () => {
      const seed = el.id + ':' + ((store.get(el.id) || {}).round || 0);
      qs = shuffle(parts.map((p) => p.id), seed).slice(0, N); qi = 0; firstTry = 0;
      list.querySelectorAll('li').forEach((li) => li.removeAttribute('data-state'));
      ask();
    };
    function ask() {
      mark(null); qNext.hidden = true; qOut.textContent = ''; qOut.removeAttribute('data-state'); tried = false;
      if (qi >= qs.length) {
        const st = store.get(el.id) || {}; st.round = (st.round || 0) + 1; store.set(el.id, st);
        qBox.replaceChildren(h('p', { class: 'ip-quiz-q' }, h('strong', {}, `You found ${firstTry} of ${qs.length} parts on the first try.`)),
          h('p', { class: 'fx-actions' }, h('button', { type: 'button', class: 'fx-btn', onclick: startQuiz }, 'Play again with other parts')));
        panel.replaceChildren(h('p', { class: 'fx-note' }, 'Select any part to read about it.'));
        return;
      }
      const p = byId[qs[qi]];
      qBox.replaceChildren(h('p', { class: 'ip-quiz-n' }, `Part ${qi + 1} of ${qs.length}`), h('p', { class: 'ip-quiz-q', html: 'Find ' + md(p.find) + '.' }), qOut, h('p', { class: 'fx-actions' }, qNext));
      panel.replaceChildren(h('p', { class: 'fx-note' }, 'Select a part in the drawing or in the list.'));
    }

    function choose(id, focus) {
      if (mode === 'quiz' && qi < qs.length) {
        const want = byId[qs[qi]];
        if (!qNext.hidden) { mark(id); showPanel(id, false); return; }   // already answered: just browse
        if (id === want.id) {
          if (!tried) firstTry++;
          qOut.dataset.state = 'ok'; qOut.textContent = `Right: that is the ${want.name.toLowerCase()}.`;
          list.querySelector(`li[data-id="${id}"]`).dataset.state = 'ok';
          mark(id); showPanel(id, false); qNext.hidden = false; qNext.textContent = qi === qs.length - 1 ? 'See your score →' : 'Next part →';
          if (focus) qNext.focus();
        } else {
          tried = true; qOut.dataset.state = 'no';
          qOut.innerHTML = `Not this one: that is the ${md(byId[id].name.toLowerCase())}. Hint: ${md(want.hint)}`;
          typeset(qOut);
        }
        return;
      }
      mark(id); showPanel(id, focus);
      try { history.replaceState(null, '', '#iter-' + id); } catch (e) { /* file: pages */ }
    }

    root.append(...(mode === 'quiz' ? [qBox] : []), fig, list, h('div', { class: 'ip-main' }, panel), note);
    if (mode === 'quiz') startQuiz();
    else {
      const want = (location.hash.match(/^#iter-([\w-]+)$/) || [])[1];
      if (want && byId[want]) choose(want, false); else panel.append(h('p', { class: 'fx-note' }, 'Select a part in the drawing or in the list to read what it does.'));
    }
    if (d.about !== false && mode === 'explore') root.append(about(data, checked));
    typeset(root);
  }

  function about(data, checked) {
    const src = (arr) => h('p', { class: 'ip-src' }, 'Sources: ', ...arr.flatMap((x, i) => [i ? ', ' : '', h('a', { href: x.url }, x.title)]), ` (checked ${checked}).`);
    const box = h('div', { class: 'ip-about' });
    const q = data.q;
    if (q) {
      const max = Math.max(q.fusion_mw, q.heating_mw);
      box.append(h('section', { class: 'ip-box' }, h('h4', {}, 'What does Q mean?'), h('p', { class: 'ip-formula', html: md(q.formula) }),
        h('div', { class: 'ip-bars', role: 'img', 'aria-label': `Bars to scale: heating power ${q.heating_mw} MW in, fusion power ${q.fusion_mw} MW out, ten times longer.` },
          h('div', { class: 'ip-bar' }, h('span', { html: md('Heating in, $P_\\text{heating}$') }), h('span', { class: 'ip-bar-in', style: `width:${(q.heating_mw / max * 100).toFixed(1)}%`, html: md(`$${q.heating_mw}\\ \\text{MW}$`) })),
          h('div', { class: 'ip-bar' }, h('span', { html: md('Fusion out, $P_\\text{fusion}$') }), h('span', { class: 'ip-bar-out', style: `width:${(q.fusion_mw / max * 100).toFixed(1)}%`, html: md(`$${q.fusion_mw}\\ \\text{MW}$`) }))),
        h('ul', {}, q.points.map((t) => h('li', { html: md(t) }))), src(q.sources)));
    }
    const sc = data.schedule;
    if (sc) box.append(h('section', { class: 'ip-box' }, h('h4', {}, 'When? The 2024 baseline'), h('p', { html: md(sc.baseline) }),
      h('ol', { class: 'ip-sched' }, sc.items.map((it) => h('li', {}, h('b', {}, String(it.year)), ' ', h('span', { html: md(it.event) })))),
      h('p', { class: 'fx-note', html: md(sc.note) }), src(sc.sources)));
    const mb = data.members, site = data.site;
    if (mb) box.append(h('section', { class: 'ip-box' }, h('h4', {}, 'Who builds ITER, and where?'),
      ...(site ? [h('p', { html: md(site.text) })] : []),
      h('p', {}, 'The seven ITER Members and their shares of the construction costs:'),
      h('ul', {}, mb.list.map((m) => h('li', {}, `${m.name}: ${m.share}`))), h('p', { class: 'fx-note', html: md(mb.share_note) }),
      ...(mb.cooperation && mb.cooperation.length ? [h('p', {}, 'Countries that are not Members have technical cooperation agreements with ITER:'), h('ul', {}, mb.cooperation.map((c) => h('li', {}, `${c.name} (${c.year}): ${c.note}`)))] : []),
      src(mb.sources.concat(site ? site.sources : []))));
    return box;
  }
};
