// fy4-9 model (no drawing): a cart of mass m runs to the right (+x) at v1 on a level track and hits a bumper at the wall.
// Friction and air resistance are neglected and the weight and the normal force cancel, so the only horizontal force is
// the bumper's. While the bumper is pressed in by c it pushes the cart to the left: F_x = −k c (k: hard 1600, medium 400,
// soft 100 N/m). Every force, impulse and momentum here is an x-component with its sign (+x to the right).
//   pysahtyy  a crushable bumper (perfectly plastic): it does not spring back, so it pushes only while the cart still moves
//             into it; when the cart stops, the force ends and the cart stays at rest against the crushed bumper. The
//             cart's kinetic energy has gone into the bumper's permanent deformation and internal energy. (A real
//             crushable bumper unloads quickly but not instantly; the model makes that unloading time zero.)
//   kimpoaa   an ideal spring bumper: it is pressed in, slows the cart, turns it back and springs back; the cart leaves it
//             at −v1, so its kinetic energy before and after is the same (the spring's energy ½ k c² holds it meanwhile).
// Newton's second law is integrated with RK4 steps (0,1 ms in the sim). The force is recorded into a (t, F_x) curve from
// the first contact, the impulse I_x is the signed area between the curve and the time axis, and Δp_x = m v2 − m v1 comes
// from the velocities, so I_x = Δp_x is a result of the model, not an input. Used by sim.js (window.FY49Model) and by
// tests/models/fy4-9.test.js (node), so the picture and the tests run the same physics.
(function (root) {
  const K = { kova: 1600, keski: 400, pehmea: 100 }, XS = 0.30, XB = 1.18;   // stiffness (N/m); cart front at start, bumper's free end (m)

  function create(m, v1, bumper, type) {
    return { m, v1, b: bumper, k: K[bumper], ty: type, x: XS, v: v1, t: 0, contact: false, ended: false, done: false, crush: 0,
             tc: 0, area: 0, Fprev: 0, Fmin: 0, curve: [], kesto: null, imp: null, v2: null, Ep: 0 };
  }
  const comp = (s, x) => Math.max((x === undefined ? s.x : x) - XB, 0);           // how far the cart presses the bumper in (m)
  // the bumper's force on the cart, x-component (N): to the left, so never positive
  const Fx = (s) => (s.ty === 'pysahtyy' && s.ended) ? 0 : -s.k * comp(s);

  function step(s, dt) {
    if (s.done) return;
    const acc = (xx) => (s.ty === 'pysahtyy' && s.ended) ? 0 : -s.k * comp(s, xx) / s.m;
    const x = s.x, v = s.v;
    const k1x = v, k1v = acc(x), k2x = v + dt / 2 * k1v, k2v = acc(x + dt / 2 * k1x);
    const k3x = v + dt / 2 * k2v, k3v = acc(x + dt / 2 * k2x), k4x = v + dt * k3v, k4v = acc(x + dt * k3x);
    const xn = x + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x), vn = v + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
    s.t += dt;
    if (!s.contact && !s.ended && xn > XB) {                                       // the first contact inside this step, at its fraction f
      const f = (XB - x) / (xn - x), Fn = -s.k * (xn - XB);
      s.contact = true; s.tc = (1 - f) * dt; s.area = Fn / 2 * s.tc; s.Fprev = Fn; s.Fmin = Fn; s.curve = [[0, 0], [s.tc, Fn]];
      s.x = xn; s.v = vn; return;
    }
    if (s.contact) {
      if (s.ty === 'pysahtyy' && vn <= 0) {                                         // the crushable bumper: the cart stops and stays
        const f = v / (v - vn), xs = x + f * (xn - x), Fs = -s.k * (xs - XB);
        s.area += (s.Fprev + Fs) / 2 * f * dt; s.tc += f * dt; s.Fmin = Math.min(s.Fmin, Fs); s.curve.push([s.tc, Fs], [s.tc, 0]);
        s.x = xs; s.v = 0; s.crush = xs - XB; finish(s, 0); s.done = true; return;
      }
      if (s.ty === 'kimpoaa' && xn <= XB && vn < 0) {                               // the spring bumper: the cart leaves it
        const f = (x - XB) / (x - xn); s.area += s.Fprev / 2 * f * dt; s.tc += f * dt; s.curve.push([s.tc, 0]);
        finish(s, v + f * (vn - v)); s.x = xn; s.v = vn; return;
      }
      const Fn = -s.k * comp(s, xn); s.area += (s.Fprev + Fn) / 2 * dt; s.Fprev = Fn; s.Fmin = Math.min(s.Fmin, Fn); s.tc += dt;
      if (s.curve.length === 0 || s.tc - s.curve[s.curve.length - 1][0] >= 0.001) s.curve.push([s.tc, Fn]);
    }
    s.x = xn; s.v = vn;
    if (s.ended && s.ty === 'kimpoaa' && s.x <= XS) { s.x = XS; s.done = true; }
  }
  function finish(s, vEnd) { s.contact = false; s.ended = true; s.kesto = s.tc; s.imp = s.area; s.v2 = vEnd; }

  // the largest force this run reaches (both bumpers: ½ m v1² = ½ k c², F = k c): the graph's scale before the run starts
  const peak = (m, v1, bumper) => v1 * Math.sqrt(K[bumper] * m);
  // the energies (J): the cart's kinetic energy and the energy the bumper holds now (spring) or has absorbed (crushable)
  function energy(s) {
    const Ek = 0.5 * s.m * s.v * s.v, c = s.ty === 'pysahtyy' && s.ended ? s.crush : comp(s), Eb = 0.5 * s.k * c * c;
    return { Ek, Eb };
  }
  function run(m, v1, bumper, type, dt = 1e-4, tmax = 5) {                       // a whole run, for the tests
    const s = create(m, v1, bumper, type); while (!s.done && s.t < tmax) step(s, dt); return s;
  }

  const api = { K, XS, XB, create, step, Fx, peak, energy, run };
  root.FY49Model = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
