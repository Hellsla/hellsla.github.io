// fy4-10 model (no drawing): two gliders on a level 2,0 m air track; friction and air resistance are neglected and the
// weight and the track's normal force cancel, so the only horizontal forces are the ones the gliders exert on each other.
// Glider 1 starts at x = 0,40 m, glider 2 at x = 1,20 m (centres; each glider is L = 0,20 m long, its end bumpers
// included). In contact (overlap d = L − (x2 − x1) > 0) the bumpers push the gliders apart with equal and opposite forces,
// F on glider 2 and −F on glider 1 (Newton's third law), F = max(0, k d + c (v1 − v2)), k = 300 N/m:
//   kimmoisa  spring bumpers, c = 0: the spring holds E_p = ½ k d² during the collision and gives it all back.
//   kimmoton  a soft bumper, c = 3,0 N·s/m: the damper turns kinetic energy into internal energy E_sis at the rate
//             c (v1 − v2)²; the gliders separate afterwards.
//   tarra     velcro on a soft bumper, critical damping c = 2√(k μ), μ = m1 m2/(m1 + m2): when the relative velocity
//             reaches zero the velcro holds, the gliders move on together at the same velocity, and the bumper stays
//             compressed for good, so its E_p becomes internal energy at that moment (it can no longer push them apart).
//   rajahdys  the gliders at rest at the middle of the track with a spring compressed by 4,0 cm between them
//             (E_p = ½ k d² = 0,24 J), released at t = 0.
// When F would be negative (the damper would pull), the bumpers lose contact with the force: the bumper's spring then
// relaxes on its own and its energy goes to internal energy, never to the gliders. So in every case
// E_k + E_p + E_sis is the energy at the start, and the tests check that the numerical solution keeps it so.
// RK4 steps (0,2 ms in the sim). Momenta and energies are computed from the state: the conservation of the
// total momentum is a result of the equal and opposite forces, not an input. The "after" values are taken when the
// contact ends (or when the gliders stick). Used by sim.js (window.FY410Model) and tests/models/fy4-10.test.js.
(function (root) {
  const L = 0.20, K = 300, C_IN = 3.0, D0 = 0.04, TRACK = 2.0, TMAX = 12, BUMP = 0.035;   // BUMP: each glider's bumper length (m)

  const damp = (s) => s.typ === 'kimmoton' ? C_IN : s.typ === 'tarra' ? 2 * Math.sqrt(K * s.m1 * s.m2 / (s.m1 + s.m2)) : 0;
  const overlap = (s, a1 = s.x1, a2 = s.x2) => Math.max(0, L - (a2 - a1));
  function force(s, a1, a2, u1, u2) { const d = L - (a2 - a1); return d <= 0 ? 0 : Math.max(0, K * d + damp(s) * (u1 - u2)); }
  const Ep = (s) => s.stuck ? 0 : 0.5 * K * overlap(s) ** 2;                      // the energy the bumpers hold now (J)

  function create(typ, m1, m2, v1, v2) {
    const s = { typ, m1, m2, v1: typ === 'rajahdys' ? 0 : v1, v2: typ === 'rajahdys' ? 0 : v2, t: 0, contact: false, stuck: false,
                after: null, done: false, Esis: 0 };
    if (typ === 'rajahdys') { s.x1 = 1 - (L - D0) / 2; s.x2 = 1 + (L - D0) / 2; } else { s.x1 = 0.40; s.x2 = 1.20; }
    s.w1 = s.v1; s.w2 = s.v2; s.F = force(s, s.x1, s.x2, s.w1, s.w2);
    s.E0 = energies(s).Ek + Ep(s); s.P0 = momentum(s);
    return s;
  }
  const momentum = (s) => s.m1 * s.w1 + s.m2 * s.w2;
  function energies(s) {
    const Ek1 = 0.5 * s.m1 * s.w1 ** 2, Ek2 = 0.5 * s.m2 * s.w2 ** 2;
    return { Ek1, Ek2, Ek: Ek1 + Ek2, Ep: s.stuck ? 0 : 0.5 * K * overlap(s) ** 2, Esis: s.Esis };
  }

  // the rates of change of (x1, x2, w1, w2, E_sis): Newton's second and third law, and the internal energy the bumpers
  // produce: the damper's power c (v1 − v2)² while they push, or the relaxing spring's power when they do not (F = 0 < k d)
  function rates(s, x1, x2, w1, w2) {
    const d = L - (x2 - x1), F = force(s, x1, x2, w1, w2), vr = w1 - w2;
    const dE = d <= 0 ? 0 : F > 0 ? damp(s) * vr * vr : -K * d * vr;
    return [w1, w2, -F / s.m1, F / s.m2, dE];
  }
  function step(s, dt) {                                                          // RK4: equal and opposite forces keep m1 v1 + m2 v2 exactly
    if (s.done) return;
    s.t += dt;
    if (s.stuck) { s.x1 += s.w1 * dt; s.x2 += s.w2 * dt; return endCheck(s); }
    const y = [s.x1, s.x2, s.w1, s.w2, s.Esis], add = (a, k, h) => a.map((v, i) => v + h * k[i]);
    const f = (q) => rates(s, q[0], q[1], q[2], q[3]);
    const k1 = f(y), k2 = f(add(y, k1, dt / 2)), k3 = f(add(y, k2, dt / 2)), k4 = f(add(y, k3, dt));
    [s.x1, s.x2, s.w1, s.w2, s.Esis] = y.map((v, i) => v + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]));
    s.F = force(s, s.x1, s.x2, s.w1, s.w2);
    const d = L - (s.x2 - s.x1);
    if (d > 0) s.contact = true;
    if (s.typ === 'tarra' && s.contact && s.w1 - s.w2 <= 0) {                      // the velcro holds: one common velocity
      const V = momentum(s) / (s.m1 + s.m2), Ek = energies(s).Ek, Epn = 0.5 * K * Math.max(0, d) ** 2;
      s.w1 = s.w2 = V; s.stuck = true; s.F = 0;
      s.Esis += Epn + (Ek - energies(s).Ek);                                       // the bumper stays crushed; the tiny snap too
      s.after = { u1: V, u2: V };
    } else if (s.contact && s.after === null && d <= 0) s.after = { u1: s.w1, u2: s.w2 };
    endCheck(s);
  }
  function endCheck(s) { if (s.x1 - L / 2 <= 0 || s.x2 + L / 2 >= TRACK || s.t >= TMAX) s.done = true; }

  // the largest values a run can reach, for the drawing scales (an elastic outcome bounds the collisions)
  function bounds(typ, m1, m2, v1, v2) {
    if (typ === 'rajahdys') { v1 = 0; v2 = 0; }
    const ue1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2), ue2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2);
    const mu = m1 * m2 / (m1 + m2), E0 = 0.5 * m1 * v1 * v1 + 0.5 * m2 * v2 * v2 + (typ === 'rajahdys' ? 0.5 * K * D0 * D0 : 0);
    const pr = Math.sqrt(2 * 0.5 * K * D0 * D0 * mu);                              // each glider's momentum after the explosion
    const P = Math.max(0.05, Math.abs(m1 * v1), Math.abs(m2 * v2), Math.abs(m1 * v1 + m2 * v2), Math.abs(m1 * ue1), Math.abs(m2 * ue2), typ === 'rajahdys' ? pr : 0);
    const V = Math.max(0.05, Math.abs(v1), Math.abs(v2), Math.abs(ue1), Math.abs(ue2), typ === 'rajahdys' ? pr / Math.min(m1, m2) : 0);
    const Fmax = typ === 'rajahdys' ? K * D0 : Math.abs(v1 - v2) * Math.sqrt(K * mu) + damp({ typ, m1, m2 }) * Math.abs(v1 - v2);
    return { E: Math.max(0.01, E0), P, V, F: Math.max(0.5, Fmax) };
  }
  function run(typ, m1, m2, v1, v2, dt = 2e-4, watch) {                          // a whole run, for the tests
    const s = create(typ, m1, m2, v1, v2); while (!s.done) { step(s, dt); if (watch) watch(s); } return s;
  }

  const api = { L, K, D0, TRACK, BUMP, create, step, energies, momentum, bounds, run, overlap };
  root.FY410Model = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
