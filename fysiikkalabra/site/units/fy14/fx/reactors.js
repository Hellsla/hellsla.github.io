/* Tokamak or stellarator? (data-fx="reactors"): two cut-away drawings of a magnetic-confinement ring, seen obliquely
   from above, drawn here as a small 3D scene (flat-shaded surfaces sorted by depth, original work, not copied from
   any picture): the tokamak with its D-shaped toroidal field coils, central solenoid, poloidal field coils, plasma
   ring and plasma current; the stellarator with twisted, non-planar modular coils (as in Wendelstein 7-X) round a
   twisted plasma whose cross-section changes from bean-shaped to triangular. The front of the ring is cut away to
   show the cross-section.
   - "Tokamak" / "Stellarator" buttons choose the drawing; checkboxes show or hide the layers: coils, the toroidal
     part of the magnetic field, its poloidal part, the resulting helical field line and the plasma current (tokamak
     only). Each layer has its own colour and its own line pattern (the legend names them), never colour alone. The
     twist of the field lines is drawn stronger than in a real machine so that it can be seen.
   - Step cards (Previous / Next, or a step's number) explain in plain English: the toroidal field, why it alone
     cannot confine a plasma (curvature and gradient drifts separate ions and electrons, an electric field forms and
     the plasma drifts outward), how the twist is made, pulsed and steady operation (inductive and non-inductive
     current drive), disruptions and the difficulty of 3D coils. "Show this in the drawing" sets the layers for the step.
   - A side-by-side comparison table, short checks (choices with feedback for every option, kept in localStorage)
     and a "Which design would you choose and why?" note with sentence starters.
   Facts: W7-X (50 non-planar and 20 planar superconducting coils, five field periods, first plasma 10 December 2015,
   8 minutes and 1.3 GJ on 15 February 2023, a triple-product record for long pulses on 22 May 2025) from ipp.mpg.de
   and Wikipedia; ITER coils from iter.org (checked 2026-11-01).
   Data on the element: {checks?: true|false (default true), start?: "tokamak"|"stellarator", note?: true|false}. */
window.FX.reactors = (el, d, A) => {
  const { h, md, store, typeset } = A;
  const COL = { B: '#2b8a3e', Bdeep: '#1b6e30', I: '#7048e8', E: '#364fc7', plasma: '#e64980' };
  const VW = 640, VH = 470, SC = 182, CX = 320, CY = 238;
  const EL = 22 * Math.PI / 180, ce = Math.cos(EL), se = Math.sin(EL);
  const cam = [0, -ce, se];
  const add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]], sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
  const mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k], dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const norm = (a) => { const l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; };
  const LIGHT = norm([-0.5, -0.65, 0.75]), HALF = norm(add(LIGHT, cam));
  const proj = (p) => [CX + SC * p[0], CY - SC * (p[1] * se + p[2] * ce), p[1] * ce - p[2] * se];
  const f1 = (v) => Math.round(v * 10) / 10;
  const hex = (s) => [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16));
  const shade = (base, n, o = {}) => {
    const l = Math.max(0, dot(n, LIGHT)), s = Math.pow(Math.max(0, dot(n, HALF)), o.pw || 28) * (o.sp == null ? 0.3 : o.sp);
    const k = (o.amb == null ? 0.48 : o.amb) + (o.dif == null ? 0.6 : o.dif) * l;
    return 'rgb(' + base.map((v) => Math.round(Math.min(255, v * k + 255 * s))).join(',') + ')';
  };
  const DEG = Math.PI / 180, CUT_A = -15 * DEG, CUT_B = 260 * DEG;   // the ring is drawn from CUT_A to CUT_B; the front-right wedge is cut away
  const inCut = (phi) => { let p = ((phi / DEG) % 360 + 360) % 360; return p > 260 && p < 345; };

  /* ---------- geometry of the two machines (R0 = 1) ---------- */
  const TOK = { a: 0.32, k: 1.7, dl: 0.35 };
  const tokSec = (t, s) => [1 + s * TOK.a * Math.cos(t + TOK.dl * Math.sin(t)), s * TOK.k * TOK.a * Math.sin(t)];
  const N = 5, ST = { a1: 0.11, a2: 0.245, dx: 0.06 };
  const stAxis = (phi) => { const ps = phi - CUT_A; return [1 + ST.dx * Math.cos(N * ps), ST.dx * 0.8 * Math.sin(N * ps)]; };
  const stLocal = (phi, t, grow) => {   // (u along R, v along z) relative to the axis
    const ps = phi - CUT_A, al = N * ps / 2, cb = (1 + Math.cos(N * ps)) / 2, ct = 1 - cb;
    const a1 = ST.a1 + grow, a2 = ST.a2 + grow;
    const e1 = a1 * Math.cos(t), e2 = a2 * Math.sin(t);
    let u = e1 * Math.cos(al) - e2 * Math.sin(al), v = e1 * Math.sin(al) + e2 * Math.cos(al);
    if (!grow) {
      let ang = Math.atan2(v, u), r = Math.hypot(u, v);
      r *= 1 + 0.2 * ct * Math.cos(3 * ang);
      u = r * Math.cos(ang); v = r * Math.sin(ang);
      ang = Math.atan2(v, u); let w = ang - Math.PI; w = Math.atan2(Math.sin(w), Math.cos(w));
      u += 0.075 * cb * Math.exp(-(w * w) / 0.3);   // the inner side pushed in: a bean
    }
    return [u, v];
  };
  const torus = (phi, R, z) => [R * Math.cos(phi), R * Math.sin(phi), z];
  const SURF = {
    tokamak: (phi, t, s) => { const [R, z] = tokSec(t, s); return torus(phi, R, z); },
    stellarator: (phi, t, s) => { const [Ra, za] = stAxis(phi), [u, v] = stLocal(phi, t, 0); return torus(phi, Ra + s * u, za + s * v); },
  };
  const AXIS = { tokamak: (phi) => torus(phi, 1, 0), stellarator: (phi) => { const [R, z] = stAxis(phi); return torus(phi, R, z); } };

  /* ---------- the scene: primitives sorted by depth ---------- */
  function scene(kind) {
    const P = [], surf = SURF[kind], axis = AXIS[kind];
    const push = (z, s) => P.push([z, s]);
    const pts = (a) => a.map((p) => f1(p[0]) + ' ' + f1(p[1])).join('L');
    const poly = (q3, cls, base, n, o) => {
      if (dot(n, cam) <= 0.002) return;
      const q = q3.map(proj), z = q.reduce((s, p) => s + p[2], 0) / q.length, c = shade(base, n, o);
      push(z, `<path class="${cls}" d="M${pts(q)}Z" fill="${c}" stroke="${c}" stroke-width=".7" stroke-linejoin="round"/>`);
    };
    // a tube of rectangular section along a curve; ref(i) is a point the tube's "n" side faces away from
    const tube = (C, ref, w, t, cls, base, closed, o) => {
      const n = C.length, rings = [];
      for (let i = 0; i < n; i++) {
        const a = C[closed ? (i - 1 + n) % n : Math.max(0, i - 1)], b = C[closed ? (i + 1) % n : Math.min(n - 1, i + 1)];
        const T = norm(sub(b, a)), r = sub(C[i], ref(i)), nn = norm(sub(r, mul(T, dot(r, T)))), bb = cross(T, nn);
        rings.push([[1, 1], [1, -1], [-1, -1], [-1, 1]].map(([p, q]) => add(C[i], add(mul(nn, w * p), mul(bb, t * q)))));
      }
      const m = closed ? n : n - 1;
      for (let i = 0; i < m; i++) {
        const A0 = rings[i], A1 = rings[(i + 1) % n], c = mul(add(C[i], C[(i + 1) % n]), 0.5);
        for (let k = 0; k < 4; k++) {
          const q = [A0[k], A0[(k + 1) % 4], A1[(k + 1) % 4], A1[k]];
          const mid = mul(add(add(q[0], q[1]), add(q[2], q[3])), 0.25);
          poly(q, cls, base, norm(sub(mid, c)), o);
        }
      }
      if (!closed) [[0, 1], [n - 1, -1]].forEach(([i, sg]) => {
        const T = norm(sub(C[Math.min(n - 1, i + 1)], C[Math.max(0, i - 1)]));
        poly(rings[i], cls, base, mul(T, -sg), o);
      });
    };
    const line = (L, cls, col, wd, o = {}) => {   // a polyline on or near the surface, split into short pieces
      const pr = L.map(proj), bias = o.bias == null ? 0.07 : o.bias, every = o.dash || 0;
      for (let i = 0; i < pr.length - 1; i++) {
        if (every && Math.floor(i / every) % 2) continue;
        const z = (pr[i][2] + pr[i + 1][2]) / 2 - bias;
        push(z, `<path class="${cls}" d="M${f1(pr[i][0])} ${f1(pr[i][1])}L${f1(pr[i + 1][0])} ${f1(pr[i + 1][1])}" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" fill="none"/>`);
      }
      (o.arrows || []).forEach((i) => {
        const a = pr[Math.max(0, i - 1)], b = pr[Math.min(pr.length - 1, i + 1)], p = pr[i];
        let dx = b[0] - a[0], dy = b[1] - a[1]; const l = Math.hypot(dx, dy) || 1; dx /= l; dy /= l;
        if (o.rev) { dx = -dx; dy = -dy; }
        const s = o.head || 8, tip = [p[0] + dx * s, p[1] + dy * s], l1 = [p[0] - dx * s * 0.6 - dy * s * 0.62, p[1] - dy * s * 0.6 + dx * s * 0.62], l2 = [p[0] - dx * s * 0.6 + dy * s * 0.62, p[1] - dy * s * 0.6 - dx * s * 0.62];
        push(p[2] - bias - 0.002, `<path class="${cls}" d="M${f1(tip[0])} ${f1(tip[1])}L${f1(l1[0])} ${f1(l1[1])}L${f1(l2[0])} ${f1(l2[1])}Z" fill="${col}" stroke="#fff" stroke-width=".8"/>`);
      });
    };
    const span = (n) => Array.from({ length: n + 1 }, (_, i) => CUT_A + (CUT_B - CUT_A) * i / n);

    // plasma surface
    const pink = hex('#f48fb1'), NP = kind === 'tokamak' ? 84 : 120, NT = kind === 'tokamak' ? 36 : 44;
    const phis = span(NP), ths = Array.from({ length: NT + 1 }, (_, j) => 2 * Math.PI * j / NT);
    const G = phis.map((ph) => ths.map((t) => surf(ph, t, 1)));
    for (let i = 0; i < NP; i++) for (let j = 0; j < NT; j++) {
      const q = [G[i][j], G[i + 1][j], G[i + 1][j + 1], G[i][j + 1]];
      let n = norm(cross(sub(q[2], q[0]), sub(q[3], q[1])));
      const mid = mul(add(add(q[0], q[1]), add(q[2], q[3])), 0.25);
      if (dot(n, sub(mid, axis((phis[i] + phis[i + 1]) / 2))) < 0) n = mul(n, -1);
      poly(q, 'L-plasma', pink, n, { amb: 0.62, dif: 0.45, sp: 0.18, pw: 16 });
    }
    // the cut faces: cross-sections with nested flux surfaces
    [[CUT_A, -1], [CUT_B, 1]].forEach(([ph, sg]) => {
      const nrm = mul([-Math.sin(ph), Math.cos(ph), 0], sg);
      if (dot(nrm, cam) <= 0.02) return;
      const ring = (s) => ths.map((t) => proj(kind === 'tokamak' ? surf(ph, t, s) : (() => { const [Ra, za] = stAxis(ph), [u, v] = stLocal(ph, t, 0); return torus(ph, Ra + s * u, za + s * v); })()));
      const out = ring(1), z = Math.min(...out.map((p) => p[2])) - 0.004, c0 = proj(axis(ph));
      let s = `<g class="rx-cap"><path class="L-plasma" d="M${pts(out)}Z" fill="url(#rx-cap-${kind})" stroke="#c2255c" stroke-width="1.2"/>`;
      [0.72, 0.45, 0.2].forEach((k) => { s += `<path class="L-plasma" d="M${pts(ring(k))}Z" fill="none" stroke="#fff" stroke-opacity=".75" stroke-width="1"/>`; });
      if (sg < 0) {
        // poloidal field drawn as arrowed rings on the face, plasma current coming out of it (tokamak)
        [0.86, 0.55].forEach((k) => {
          const r = ring(k); s += `<path class="L-bp" d="M${pts(r)}Z" fill="none" stroke="${COL.B}" stroke-width="1.8" stroke-dasharray="6 4"/>`;
          [Math.round(NT * 0.08), Math.round(NT * 0.58)].forEach((j) => {
            const a = r[j], b = r[j + 1], dx = b[0] - a[0], dy = b[1] - a[1], l = Math.hypot(dx, dy) || 1, ux = dx / l, uy = dy / l, m = 6;
            s += `<path class="L-bp" d="M${f1(a[0] + ux * m)} ${f1(a[1] + uy * m)}L${f1(a[0] - ux * m * 0.6 - uy * m * 0.7)} ${f1(a[1] - uy * m * 0.6 + ux * m * 0.7)}L${f1(a[0] - ux * m * 0.6 + uy * m * 0.7)} ${f1(a[1] - uy * m * 0.6 - ux * m * 0.7)}Z" fill="${COL.B}"/>`;
          });
        });
        if (kind === 'tokamak') s += `<g class="L-cur"><circle cx="${f1(c0[0])}" cy="${f1(c0[1])}" r="9" fill="#fff" stroke="${COL.I}" stroke-width="2.2"/><circle cx="${f1(c0[0])}" cy="${f1(c0[1])}" r="3" fill="${COL.I}"/></g>`;
      }
      push(z, s + '</g>');
    });

    // coils
    const copper = hex('#c8763f'), steel = hex('#8fa3b5'), bronze = hex('#a86a32'), stc = hex('#c98a4b');
    if (kind === 'tokamak') {
      for (let k = 0; k < 18; k++) {
        const ph = (-5 + 20 * k) * DEG; if (inCut(ph)) continue;
        const C = Array.from({ length: 64 }, (_, i) => { const t = 2 * Math.PI * i / 64; return torus(ph, 1.0 + 0.47 * Math.cos(t + 0.4 * Math.sin(t)), 0.8 * Math.sin(t)); });
        tube(C, () => torus(ph, 1.0, 0), 0.045, 0.028, 'L-coils', copper, true);
      }
      [[0.6, 0.98, 0.04, 0.035], [1.32, 0.86, 0.03, 0.03], [1.66, 0.36, 0.032, 0.036], [1.66, -0.3, 0.032, 0.036], [1.32, -0.86, 0.03, 0.03], [0.64, -1.0, 0.045, 0.04]].forEach(([R, z, w, t]) => {
        const ph = span(Math.round(110 * R)), C = ph.map((p) => torus(p, R, z));
        tube(C, (i) => [0, 0, z], w, t, 'L-coils', steel, false);
      });
      // central solenoid: six modules on a cylinder
      const rc = 0.33, nm = 6, zt = 0.78, gap = 0, hm = (2 * zt - gap * (nm - 1)) / nm, NS = 48;
      for (let m = 0; m < nm; m++) {
        const z0 = -zt + m * (hm + gap), z1 = z0 + hm;
        for (let i = 0; i < NS; i++) {
          const a0 = 2 * Math.PI * i / NS, a1 = 2 * Math.PI * (i + 1) / NS, am = (a0 + a1) / 2;
          poly([[rc * Math.cos(a0), rc * Math.sin(a0), z0], [rc * Math.cos(a1), rc * Math.sin(a1), z0], [rc * Math.cos(a1), rc * Math.sin(a1), z1], [rc * Math.cos(a0), rc * Math.sin(a0), z1]], 'L-coils', bronze, [Math.cos(am), Math.sin(am), 0]);
        }
      }
      for (let m = 1; m < nm; m++) {   // dark joints between the modules
        const z0 = -zt + m * hm - 0.006, z1 = z0 + 0.012, r2 = rc + 0.003;
        for (let i = 0; i < NS; i++) {
          const a0 = 2 * Math.PI * i / NS, a1 = 2 * Math.PI * (i + 1) / NS, am = (a0 + a1) / 2;
          poly([[r2 * Math.cos(a0), r2 * Math.sin(a0), z0], [r2 * Math.cos(a1), r2 * Math.sin(a1), z0], [r2 * Math.cos(a1), r2 * Math.sin(a1), z1], [r2 * Math.cos(a0), r2 * Math.sin(a0), z1]], 'L-coils', [70, 42, 20], [Math.cos(am), Math.sin(am), 0], { sp: 0 });
        }
      }
      poly(Array.from({ length: NS }, (_, i) => [rc * Math.cos(2 * Math.PI * i / NS), rc * Math.sin(2 * Math.PI * i / NS), zt]), 'L-coils', bronze, [0, 0, 1]);
    } else {
      const NC = 40;
      for (let k = 0; k < NC; k++) {
        const ph0 = CUT_A + 2 * Math.PI * (k + 0.5) / NC; if (inCut(ph0)) continue;
        const beta = 2 * Math.PI * ((k % 8) / 8), amp = 0.07 + 0.025 * Math.cos(beta);
        const C = Array.from({ length: 72 }, (_, i) => {
          const t = 2 * Math.PI * i / 72, ph = ph0 + amp * Math.sin(t + beta) + 0.025 * Math.sin(2 * t + beta);
          const [Ra, za] = stAxis(ph), [u, v] = stLocal(ph, t, 0.11);
          return torus(ph, Ra + u, za + v);
        });
        tube(C, (i) => { const t = 2 * Math.PI * i / 72, ph = ph0 + amp * Math.sin(t + beta); return AXIS.stellarator(ph); }, 0.03, 0.022, 'L-coils', stc, true);
      }
    }

    // field lines (on a surface just outside the plasma)
    const S = 1.1, NL = 260, ls = span(NL);
    const atAngle = (ph, g, s) => {   // the surface point seen from the axis at the geometric angle g (stellarator)
      let best = 0, bd = 9;
      for (let j = 0; j < 360; j++) { const t = 2 * Math.PI * j / 360, [u, v] = stLocal(ph, t, 0); let dd = Math.atan2(v, u) - g; dd = Math.abs(Math.atan2(Math.sin(dd), Math.cos(dd))); if (dd < bd) { bd = dd; best = t; } }
      return SURF.stellarator(ph, best, s);
    };
    const tor = kind === 'tokamak' ? [40, 165, -55] : [30, 160, -60];
    tor.forEach((g) => {
      const L = ls.map((ph) => kind === 'tokamak' ? surf(ph, g * DEG, S) : atAngle(ph, g * DEG, S));
      line(L, 'L-bt', COL.B, 1.8, { arrows: [40, 110, 180, 240], head: 7 });
    });
    [35, 95, 150, 205, 245].forEach((pd) => {
      const ph = pd * DEG, L = Array.from({ length: 61 }, (_, j) => surf(ph, 2 * Math.PI * j / 60, S + 0.03));
      line(L, 'L-bp', COL.B, 1.8, { dash: 2, arrows: [6, 36], head: 7 });
    });
    const twist = kind === 'tokamak' ? 4.2 : 0.35;
    const H = ls.map((ph) => surf(ph, 0.6 + twist * (ph - CUT_A), S + 0.02));
    line(H, 'L-helix', COL.Bdeep, 3.2, { arrows: [30, 80, 130, 180, 230], head: 9, bias: 0.08 });
    if (kind === 'tokamak') {
      const L = ls.map((ph) => surf(ph, 95 * DEG, S + 0.05));
      line(L, 'L-cur', COL.I, 2.6, { dash: 0, arrows: [25, 95, 165, 235], head: 9, rev: true, bias: 0.09 });
    }

    P.sort((a, b) => b[0] - a[0]);
    return P.map((p) => p[1]).join('');
  }

  const defs = () => `<defs>
    <radialGradient id="rx-cap-tokamak" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#fff3bf"/><stop offset=".35" stop-color="#ffc9c9"/><stop offset=".75" stop-color="#f783ac"/><stop offset="1" stop-color="#e64980"/></radialGradient>
    <radialGradient id="rx-cap-stellarator" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#fff3bf"/><stop offset=".35" stop-color="#ffc9c9"/><stop offset=".75" stop-color="#f783ac"/><stop offset="1" stop-color="#e64980"/></radialGradient>
    <radialGradient id="rx-floor" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#000" stop-opacity=".16"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>`;

  /* ---------- labels (HTML over the drawing, so that they stay readable on a phone) ---------- */
  const LABELS = {
    tokamak: [
      { n: 1, text: 'Toroidal field coil', layer: 'coils', at: () => torus(-5 * DEG, 1.0 + 0.47 * Math.cos(1.0 + 0.4 * Math.sin(1.0)), 0.8 * Math.sin(1.0)), x: 0.83, y: 0.08 },
      { n: 2, text: 'Central solenoid', layer: 'coils', at: () => [0, -0.36, 0.55], x: 0.06, y: 0.08 },
      { n: 3, text: 'Poloidal field coil', layer: 'coils', at: () => torus(185 * DEG, 1.66, 0.36), x: 0.04, y: 0.5 },
      { n: 4, text: 'Plasma (cut open)', layer: null, at: () => SURF.tokamak(CUT_A, -0.9, 0.7), x: 0.86, y: 0.86 },
    ],
    stellarator: [
      { n: 1, text: 'Non-planar coil', layer: 'coils', at: () => { const ph = CUT_A + 2 * Math.PI * 0.5 / 40, [Ra, za] = stAxis(ph), [u, v] = stLocal(ph, 1.2, 0.11); return torus(ph, Ra + u, za + v); }, x: 0.84, y: 0.1 },
      { n: 2, text: 'Bean-shaped cross-section', layer: null, at: () => SURF.stellarator(CUT_A, -1.2, 0.6), x: 0.82, y: 0.84 },
      { n: 3, text: 'Twisted plasma ring', layer: null, at: () => SURF.stellarator(100 * DEG, Math.PI, 1), x: 0.08, y: 0.1 },
    ],
  };

  /* ---------- texts ---------- */
  const VIEWS = {
    tokamak: { name: 'Tokamak', aria: 'A tokamak cut open at the front: a ring of pink plasma inside 18 D-shaped toroidal field coils, with a tall central solenoid in the middle and six horizontal poloidal field coils around the ring.',
      cap: 'A **tokamak**. D-shaped coils make the field that goes round the ring. The central solenoid induces a large current in the plasma, and that current makes the poloidal field that twists the field lines.' },
    stellarator: { name: 'Stellarator', aria: 'A stellarator cut open at the front: a twisted plasma ring with a bean-shaped cross-section, surrounded by many twisted, non-planar coils.',
      cap: 'A **stellarator**. The twisted, non-planar coils (Wendelstein 7-X has 50 of them, and 20 planar coils) make the twisted field themselves. There is no large current in the plasma. The drawing shows fewer coils than W7-X.' },
  };
  const LAYERS = [
    { id: 'coils', label: 'Coils', on: true },
    { id: 'bt', label: 'Toroidal part of the field $\\overline{B}_\\text{t}$', on: false, swatch: [COL.B, 2, ''] },
    { id: 'bp', label: 'Poloidal part of the field $\\overline{B}_\\text{p}$', on: false, swatch: [COL.B, 2, '5 4'] },
    { id: 'helix', label: 'Resulting helical field line $\\overline{B}$', on: true, swatch: [COL.Bdeep, 3.5, ''] },
    { id: 'cur', label: 'Plasma current $I_\\text{p}$', on: true, swatch: [COL.I, 3, ''], only: 'tokamak' },
  ];
  const STEPS = [
    { t: 'A field that goes round the ring', view: 'tokamak', layers: ['coils', 'bt'],
      x: 'Charged particles in a plasma spiral around magnetic field lines. They move easily **along** a field line but hardly **across** it. Coils around a ring make a field $\\overline{B}_\\text{t}$ that goes round and round the ring (the **toroidal** direction). The field lines have no ends, so particles cannot run out at the ends.' },
    { t: 'Why that field alone is not enough', view: 'tokamak', layers: ['bt'], fig: 'drift',
      x: 'On the inner side of the ring the coils are closer together, so $\\overline{B}$ is **stronger inside and weaker outside**, and the field lines are curved. Because of this, the particles drift slowly across the field: the ions one way (here up), the electrons the other way (down). The charges separate, and an electric field $\\overline{E}$ forms between them. Together, $\\overline{E}$ and $\\overline{B}$ push the **whole plasma outward**, into the wall. A purely toroidal field cannot confine a plasma.' },
    { t: 'The cure: twist the field lines', view: 'tokamak', layers: ['coils', 'bt', 'bp', 'helix', 'cur'],
      x: 'If every field line also goes round the short way (the **poloidal** direction), a particle spends time on the top and on the bottom, on the inside and on the outside. Charges can then flow back along the twisted field lines, so the charge separation and the outward drift do not build up. **Tokamak:** a large current $I_\\text{p}$ flows in the plasma itself, and its magnetic field $\\overline{B}_\\text{p}$ adds the twist. **Stellarator:** the shape of the coils twists the field; no large plasma current is needed.' },
    { t: 'Pulsed or steady?', view: 'tokamak', layers: ['coils', 'cur'],
      x: 'In a tokamak the central solenoid works like the primary winding of a transformer, and the plasma ring is the secondary. A **changing** current in the solenoid induces $I_\\text{p}$. The solenoid current cannot keep changing for ever, so **inductive drive alone is limited in time**: the tokamak runs in pulses. But the current can also be driven **without induction**: by beams of fast neutral atoms, by radio-frequency waves (for example lower hybrid or electron cyclotron current drive), and by the **bootstrap current** that the plasma drives itself through its own pressure gradient. With these, long pulses are possible, perhaps even steady operation. A stellarator needs no plasma current, so it can run **steadily** by design: W7-X kept a plasma for eight minutes in 2023 and aims at 30 minutes.' },
    { t: 'Risks and difficulties', view: 'stellarator', layers: ['coils', 'helix'],
      x: '**Tokamak:** in a **disruption** the plasma suddenly loses its confinement, and its large current dies away in a very short time. This puts strong forces and heat loads on the wall and the vessel, so a reactor must avoid or soften disruptions. **Stellarator:** with no large plasma current there are no disruptions of that kind. But the **3D coils** are hard to design and must be built and placed very precisely: in W7-X, 20 of the 50 non-planar coils had insulation faults that took years to fix. Older stellarators also confined the plasma **worse** than tokamaks. Optimised designs like W7-X, computed on supercomputers, changed this: in May 2025 W7-X set a record for long pulses that is on a par with tokamak results.' },
  ];
  const TABLE = [
    ['How the twist is made', 'By a large current in the plasma (its poloidal field)', 'By the shape of the coils'],
    ['Large current in the plasma', 'Yes (in ITER, millions of amperes)', 'No'],
    ['Coils', 'Planar D-shaped coils, central solenoid, ring coils', 'Twisted, non-planar 3D coils'],
    ['Operation', 'Pulsed with inductive drive; long pulses with non-inductive current drive', 'Steady by design'],
    ['Disruptions', 'A real risk that must be avoided or softened', 'None of that kind'],
    ['Main difficulty', 'Keeping the current and the plasma stable', 'Designing and building the 3D coils precisely'],
    ['Confinement so far', 'The best results for decades', 'Worse until optimised designs such as W7-X'],
    ['Examples', 'JET (UK, closed 2023), JT-60SA (Japan), ITER (France, being built)', 'Wendelstein 7-X (Germany), LHD (Japan)'],
  ];
  const CHECKS = [
    { q: 'Why can a magnetic field that only goes round the ring not hold a plasma?', o: [
      ['The field is too weak to stop the particles.', false, 'Even a very strong purely toroidal field fails. The problem is the drift caused by the curvature and the weaker field on the outside.'],
      ['Ions and electrons drift apart, an electric field forms and the plasma drifts outward.', true, 'Right: curvature and the gradient of $\\overline{B}$ separate the charges, and $\\overline{E}$ and $\\overline{B}$ together push the plasma out.'],
      ['The particles run out at the ends of the field lines.', false, 'In a ring the field lines have no ends; that is why a ring is used.'] ] },
    { q: 'In a tokamak, what makes the poloidal field that twists the field lines?', o: [
      ['The current in the plasma.', true, 'Right: the plasma current $I_\\text{p}$ is surrounded by its own magnetic field $\\overline{B}_\\text{p}$.'],
      ['The toroidal field coils.', false, 'They make the toroidal field, the part that goes round the ring.'],
      ['The vacuum vessel.', false, 'The vessel holds the vacuum; it does not make the twist.'] ] },
    { q: 'Which statement about how long a tokamak can run is correct?', o: [
      ['It can only make short pulses, because its current must come from the central solenoid.', false, 'Not quite: the solenoid alone gives limited pulses, but beams, radio-frequency waves and the bootstrap current can drive the current without induction.'],
      ['Inductive drive alone is limited in time, but non-inductive current drive allows long pulses.', true, 'Right: neutral beams, waves such as lower hybrid or electron cyclotron current drive, and the bootstrap current can keep the current going.'],
      ['It needs no current in the plasma, so it can run for ever.', false, 'That describes a stellarator. A tokamak needs its plasma current for the twist.'] ] },
    { q: 'What is the main engineering challenge of a stellarator?', o: [
      ['Disruptions of its large plasma current.', false, 'A stellarator has no large plasma current, so it has no disruptions of that kind.'],
      ['Complex 3D coils that must be designed and built very precisely.', true, 'Right: the twist is built into the coils, so their shape and position must be exact.'],
      ['The central solenoid wears out.', false, 'A stellarator does not need a central solenoid.'] ] },
  ];

  /* ---------- build the component ---------- */
  const idp = el.id + '-';
  const saved = store.get(el.id) || {};
  let view = saved.view || d.start || 'tokamak';
  const layerOn = {}; LAYERS.forEach((l) => { layerOn[l.id] = saved.layers && saved.layers[l.id] != null ? saved.layers[l.id] : l.on; });
  const save = () => { saved.view = view; saved.layers = layerOn; store.set(el.id, saved); };

  const root = h('div', { class: 'rx' });
  const viewBar = h('div', { class: 'fx-steps rx-views', role: 'group', 'aria-label': 'Choose the machine' });
  const btns = {};
  ['tokamak', 'stellarator'].forEach((k) => { btns[k] = h('button', { type: 'button', class: 'fx-step', 'aria-pressed': 'false', onclick: () => setView(k) }, VIEWS[k].name); viewBar.append(btns[k]); });
  const svgs = {}, figBox = h('div', { class: 'rx-fig' }), labBox = h('div', { class: 'rx-labs', 'aria-hidden': 'true' });
  const key = h('ol', { class: 'rx-key' });
  const caption = h('p', { class: 'rx-cap', 'aria-live': 'polite' });
  figBox.append(labBox);
  const checks = h('fieldset', { class: 'rx-layers' }, h('legend', {}, 'Show in the drawing'));
  const boxes = {};
  LAYERS.forEach((l) => {
    const cb = h('input', { type: 'checkbox', id: idp + 'L-' + l.id });
    cb.checked = layerOn[l.id];
    cb.addEventListener('change', () => { layerOn[l.id] = cb.checked; apply(); save(); });
    const sw = l.swatch ? h('span', { class: 'rx-sw', 'aria-hidden': 'true', html: `<svg viewBox="0 0 36 12" width="36" height="12"><path d="M2 6H34" stroke="${l.swatch[0]}" stroke-width="${l.swatch[1]}" stroke-linecap="round" ${l.swatch[2] ? `stroke-dasharray="${l.swatch[2]}"` : ''}/><path d="M28 2L34 6L28 10Z" fill="${l.swatch[0]}"/></svg>` })
      : h('span', { class: 'rx-sw rx-sw-coil', 'aria-hidden': 'true' });
    const note = l.only ? h('span', { class: 'rx-only', id: idp + 'only-' + l.id }) : null;
    boxes[l.id] = { cb, note };
    checks.append(h('label', { class: 'fx-check rx-check', for: idp + 'L-' + l.id }, cb, sw, h('span', { html: md(l.label) }), note));
  });
  checks.append(h('p', { class: 'fx-note' }, 'The twist of the field lines is drawn much stronger than in a real machine, so that you can see it. The plasma itself is pink.'));

  function build(k) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', `0 0 ${VW} ${VH}`); svg.setAttribute('role', 'img'); svg.setAttribute('class', 'rx-svg');
    svg.setAttribute('aria-label', VIEWS[k].aria);
    const floorY = CY + SC * 1.2 * ce * 0.82;
    let leaders = '';
    LABELS[k].forEach((L) => {
      const p = proj(L.at()), lx = L.x * VW, ly = L.y * VH;
      leaders += `<g class="rx-leader${L.layer ? ' L-' + L.layer : ''}"><path d="M${f1(lx)} ${f1(ly)}L${f1(p[0])} ${f1(p[1])}" stroke="#14171e" stroke-width="1" fill="none"/><circle cx="${f1(p[0])}" cy="${f1(p[1])}" r="2.6" fill="#14171e" stroke="#fff" stroke-width="1"/></g>`;
    });
    svg.innerHTML = defs() + `<ellipse cx="${CX}" cy="${f1(floorY)}" rx="${SC * 1.75}" ry="${f1(SC * 1.75 * se)}" fill="url(#rx-floor)"/>` + scene(k) + leaders;
    return svg;
  }
  function apply() {
    const svg = svgs[view];
    LAYERS.forEach((l) => {
      const ok = !l.only || l.only === view;
      boxes[l.id].cb.disabled = !ok;
      if (boxes[l.id].note) boxes[l.id].note.textContent = ok ? '' : ' (a stellarator has no large plasma current)';
      svg.classList.toggle('off-' + l.id, !layerOn[l.id] || !ok);
    });
    labBox.querySelectorAll('.rx-lab').forEach((s) => { s.hidden = !!(s.dataset.layer && !layerOn[s.dataset.layer]); });
    key.querySelectorAll('li').forEach((s) => { s.hidden = !!(s.dataset.layer && !layerOn[s.dataset.layer]); });
    const shown = LAYERS.filter((l) => layerOn[l.id] && (!l.only || l.only === view)).map((l) => l.label.replace(/\s*\$.*\$/, '').toLowerCase());
    svg.setAttribute('aria-label', VIEWS[view].aria + ' Shown: plasma' + (shown.length ? ', ' + shown.join(', ') : '') + '.');
  }
  function setView(k) {
    view = k;
    Object.entries(btns).forEach(([n, b]) => b.setAttribute('aria-pressed', String(n === k)));
    if (!svgs[k]) svgs[k] = build(k);
    figBox.querySelectorAll('svg.rx-svg').forEach((s) => s.remove());
    figBox.prepend(svgs[k]);
    labBox.replaceChildren(...LABELS[k].map((L) => h('span', { class: 'rx-lab', 'data-layer': L.layer || false, 'data-side': L.x > 0.5 ? 'r' : 'l', style: `left:${(L.x * 100).toFixed(1)}%;top:${(L.y * 100).toFixed(1)}%` }, h('b', {}, String(L.n)), h('span', { class: 'rx-lab-t' }, L.text))));
    key.replaceChildren(...LABELS[k].map((L) => h('li', { 'data-layer': L.layer || false }, L.text)));
    caption.innerHTML = md(VIEWS[k].cap);
    apply(); save();
  }

  // the drift figure for step 2 (a cross-section of the ring; the machine's axis is on the left)
  const driftFig = () => {
    let s = '<svg viewBox="0 0 340 230" role="img" aria-label="Cross-section of a plasma ring in a purely toroidal field that points into the page. The field is stronger on the inner side, near the axis on the left. Ions gather at the top, electrons at the bottom, an electric field points down between them, and the whole plasma drifts outward to the right." class="rx-drift">';
    s += '<defs><marker id="' + idp + 'ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker></defs>';
    s += '<path d="M18 12V218" stroke="#6b7480" stroke-width="1.5" stroke-dasharray="6 5"/>';
    s += '<circle cx="165" cy="118" r="78" fill="#fde2ec" stroke="#e64980" stroke-width="2"/>';
    for (let i = 0; i < 6; i++) for (let j = 0; j < 4; j++) {
      const x = 62 + i * 42, y = 40 + j * 54, r = 9.5 - i * 1.15;
      s += `<g stroke="${COL.B}" stroke-width="1.8" fill="#fff"><circle cx="${x}" cy="${y}" r="${r.toFixed(1)}"/><path d="M${(x - r * 0.62).toFixed(1)} ${(y - r * 0.62).toFixed(1)}L${(x + r * 0.62).toFixed(1)} ${(y + r * 0.62).toFixed(1)}M${(x + r * 0.62).toFixed(1)} ${(y - r * 0.62).toFixed(1)}L${(x - r * 0.62).toFixed(1)} ${(y + r * 0.62).toFixed(1)}"/></g>`;
    }
    [[128, 58], [152, 50], [178, 50], [202, 58]].forEach(([x, y]) => { s += `<g><circle cx="${x}" cy="${y}" r="8" fill="#fff" stroke="#14171e" stroke-width="1.6"/><path d="M${x - 4.5} ${y}H${x + 4.5}M${x} ${y - 4.5}V${y + 4.5}" stroke="#14171e" stroke-width="1.8"/></g>`; });
    [[128, 178], [152, 186], [178, 186], [202, 178]].forEach(([x, y]) => { s += `<g><circle cx="${x}" cy="${y}" r="8" fill="#14171e"/><path d="M${x - 4.5} ${y}H${x + 4.5}" stroke="#fff" stroke-width="1.8"/></g>`; });
    s += `<path d="M110 72V40" stroke="#14171e" stroke-width="1.6" marker-end="url(#${idp}ah)"/><path d="M110 164V196" stroke="#14171e" stroke-width="1.6" marker-end="url(#${idp}ah)"/>`;
    s += `<path d="M165 72V160" stroke="${COL.E}" stroke-width="3" marker-end="url(#${idp}ah)"/>`;
    s += `<path d="M250 118H322" stroke="#14171e" stroke-width="4" marker-end="url(#${idp}ah)"/>`;
    return s + '</svg>';
  };
  const driftLabels = [['$\\overline{E}$', 0.51, 0.45, 'l']];
  const driftKey = ['The ring\'s axis is on the left (dashed line). $\\overline{B}$ points into the page (⊗): the symbols are **larger where the field is stronger**, near the axis.',
    'Ions (⊕, top) drift up; electrons (⊖, bottom) drift down.', 'The separated charges make an electric field $\\overline{E}$ (blue arrow, down).', '$\\overline{E}$ and $\\overline{B}$ together move the whole plasma **outward** (black arrow).'];

  // steps
  let step = 0;
  const stepNums = h('div', { class: 'fx-steps', role: 'group', 'aria-label': 'Steps' });
  const card = h('section', { class: 'rx-card', 'aria-live': 'polite', tabindex: '-1' });
  const prev = h('button', { type: 'button', class: 'fx-btn fx-quiet', onclick: () => goStep(step - 1) }, '← Previous');
  const next = h('button', { type: 'button', class: 'fx-btn', onclick: () => goStep(step + 1) }, 'Next →');
  STEPS.forEach((s, i) => stepNums.append(h('button', { type: 'button', class: 'fx-step', 'aria-pressed': 'false', 'aria-label': `Step ${i + 1}: ${s.t}`, onclick: () => goStep(i) }, String(i + 1))));
  function goStep(i, quiet) {
    step = Math.max(0, Math.min(STEPS.length - 1, i));
    const s = STEPS[step];
    stepNums.querySelectorAll('button').forEach((b, k) => b.setAttribute('aria-pressed', String(k === step)));
    const showBtn = h('button', { type: 'button', class: 'fx-btn fx-quiet fx-small', onclick: () => {
      LAYERS.forEach((l) => { layerOn[l.id] = s.layers.includes(l.id); boxes[l.id].cb.checked = layerOn[l.id]; });
      setView(s.view); figBox.scrollIntoView({ block: 'nearest', behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    } }, 'Show this in the drawing');
    const kids = [h('p', { class: 'rx-card-n' }, `Step ${step + 1} of ${STEPS.length}`), h('h4', {}, s.t), h('p', { html: md(s.x) })];
    if (s.fig === 'drift') {
      const fb = h('div', { class: 'rx-fig rx-fig-drift', html: driftFig() });
      fb.append(h('div', { class: 'rx-labs rx-labs-drift', 'aria-hidden': 'true' }, ...driftLabels.map(([t, x, y, side]) => h('span', { class: 'rx-dl', 'data-side': side, style: `left:${x * 100}%;top:${y * 100}%`, html: md(t) }))));
      kids.push(fb, h('ul', { class: 'rx-drift-key' }, driftKey.map((t) => h('li', { html: md(t) }))));
    }
    kids.push(h('p', { class: 'fx-actions' }, showBtn));
    card.replaceChildren(...kids);
    prev.disabled = step === 0; next.disabled = step === STEPS.length - 1;
    typeset(card);
    if (!quiet) card.focus({ preventScroll: true });
  }

  // comparison table
  const table = h('div', { class: 'fx-table-wrap' }, h('h4', { class: 'rx-h', id: idp + 'tab' }, 'Tokamak and stellarator side by side'), h('table', { class: 'rx-table', 'aria-labelledby': idp + 'tab' },
    h('thead', {}, h('tr', {}, h('th', { scope: 'col' }, ''), h('th', { scope: 'col' }, 'Tokamak'), h('th', { scope: 'col' }, 'Stellarator'))),
    h('tbody', {}, TABLE.map(([a, b, c]) => h('tr', {}, h('th', { scope: 'row' }, a), h('td', { 'data-h': 'Tokamak' }, b), h('td', { 'data-h': 'Stellarator' }, c))))));

  // checks
  const answers = saved.checks || {};
  const checkBox = h('div', { class: 'rx-checks' }, h('h4', {}, 'Check your understanding'));
  CHECKS.forEach((c, qi) => {
    const out = h('output', { 'aria-live': 'polite' });
    const group = h('div', { class: 'rx-opts', role: 'group', 'aria-label': c.q });
    const pick = (oi, quiet) => {
      const [, ok, fb] = c.o[oi];
      group.querySelectorAll('button').forEach((b, k) => { b.setAttribute('aria-pressed', String(k === oi)); b.dataset.state = k === oi ? (ok ? 'ok' : 'no') : ''; });
      out.dataset.state = ok ? 'ok' : 'no'; out.innerHTML = (ok ? '' : 'Not this one. ') + md(fb);
      if (!quiet) { answers[qi] = oi; saved.checks = answers; store.set(el.id, saved); }
      typeset(out);
    };
    c.o.forEach(([t], oi) => group.append(h('button', { type: 'button', class: 'rx-opt', 'aria-pressed': 'false', onclick: () => pick(oi) }, h('span', { class: 'rx-opt-l', 'aria-hidden': 'true' }, 'ABC'[oi]), h('span', { html: md(t) }))));
    checkBox.append(h('div', { class: 'rx-q' }, h('p', { class: 'rx-q-t' }, `${qi + 1}. `, h('span', { html: md(c.q) })), group, out));
    if (answers[qi] != null && c.o[answers[qi]]) setTimeout(() => pick(answers[qi], true), 0);
  });

  const note = h('aside', { class: 'wordbank rx-note' }, h('h4', {}, 'Which design would you choose and why?'),
    h('p', {}, 'Imagine you lead a team that will build a fusion power plant. Write three or four sentences. Use the sentence starters:'),
    h('ul', {}, ['I would choose a … because …', 'One advantage of the … is that …', 'On the other hand, …', 'The biggest problem to solve would be …'].map((t) => h('li', {}, t))));

  root.append(viewBar, figBox, key, caption, checks,
    h('h4', { class: 'rx-h' }, 'How magnetic confinement works, step by step'), stepNums, card, h('p', { class: 'fx-actions rx-nav' }, prev, next),
    table, ...(d.checks === false ? [] : [checkBox]), ...(d.note === false ? [] : [note]));
  el.append(root);
  setView(view);
  goStep(0, true);
};
