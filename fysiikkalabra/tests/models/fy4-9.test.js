// Physics tests of the fy4-9 model (assets/sims/fy4/fy4-9/model.js), run by scripts/test_models.py with node. Every
// mass, initial speed, bumper and collision type the sim offers, not only the defaults.
const M = require('../../assets/sims/fy4/fy4-9/model.js');
const { check, near } = require('./_assert.js');

for (const m of [0.5, 1, 2]) for (const v1 of [0.5, 1, 1.5, 2]) for (const b of ['kova', 'keski', 'pehmea']) for (const ty of ['pysahtyy', 'kimpoaa']) {
  const s = M.run(m, v1, b, ty), id = `m=${m} v1=${v1} ${b} ${ty}`;
  const dp = m * s.v2 - m * v1;
  check(`${id}: the run ends with a measured collision`, s.done && s.imp !== null && s.v2 !== null);
  near(`${id}: I_x = Δp_x`, s.imp, dp, 0.002);
  check(`${id}: the bumper's force and impulse point to the left (negative)`, s.imp < 0 && s.curve.every(([, F]) => F <= 0));
  near(`${id}: the largest force is v1 √(k m)`, -s.Fmin, M.peak(m, v1, b), 0.01);
  check(`${id}: the curve starts and ends on the time axis`, s.curve[0][1] === 0 && s.curve[s.curve.length - 1][1] === 0);
  if (ty === 'pysahtyy') {
    near(`${id}: the cart stops`, s.v2, 0, 1e-9);
    const x = s.x; for (let i = 0; i < 2000; i++) M.step(s, 1e-4);
    check(`${id}: the stopped cart stays where it is, no force after the stop`, s.x === x && s.v === 0 && M.Fx(s) === 0);
    near(`${id}: the crushed bumper absorbed the kinetic energy ½ m v1²`, M.energy(s).Eb, 0.5 * m * v1 * v1, 0.01);
    near(`${id}: Δp_x = −m v1`, dp, -m * v1, 0.002);
    const iMin = s.curve.reduce((b, c, i) => c[1] < s.curve[b][1] ? i : b, 0), tMid = s.curve[iMin][0];
    check(`${id}: a whole pulse: the force is largest half-way and falls smoothly to zero as the cart stops`,
          Math.abs(tMid - s.kesto / 2) < 0.03 * s.kesto && s.curve[s.curve.length - 2][1] > 0.1 * s.Fmin);
  } else {
    check(`${id}: the cart bounces back (v2 < 0)`, s.v2 < 0);
    near(`${id}: the ideal spring keeps the kinetic energy: |v2| = v1`, -s.v2, v1, 0.002);
    near(`${id}: Δp_x = −2 m v1`, dp, -2 * m * v1, 0.002);
  }
}
// during a spring collision the cart's kinetic energy and the spring's energy add up to the same total at every step
for (const b of ['kova', 'pehmea']) {
  const s = M.create(1, 2, b, 'kimpoaa'); let worst = 0, sawSpring = false;
  while (!s.done) { M.step(s, 1e-4); const E = M.energy(s); worst = Math.max(worst, Math.abs(E.Ek + E.Eb - 2)); if (E.Eb > 0.5) sawSpring = true; }
  check(`kimpoaa ${b}: E_k + ½ k c² stays 2,00 J during the collision (worst ${worst.toExponential(1)} J)`, worst < 2e-3 && sawSpring);
}
// the sign of the force at every moment: while the cart is pressed in, F_x < 0 and the arrow points left
{ const s = M.create(1, 2, 'keski', 'kimpoaa'); let ok = true;
  while (!s.done) { M.step(s, 1e-4); if (s.contact && !(M.Fx(s) <= 0)) ok = false; if (s.ended && M.Fx(s) !== 0) ok = false; }
  check('F_x ≤ 0 during contact and 0 after it', ok); }
// a harder bumper: the same impulse in a shorter time with a larger force
{ const a = M.run(1, 2, 'kova', 'pysahtyy'), c = M.run(1, 2, 'pehmea', 'pysahtyy');
  check('a harder bumper: same impulse, shorter time, larger force', Math.abs(a.imp - c.imp) < 0.005 && a.kesto < c.kesto && -a.Fmin > -c.Fmin); }
require('./_assert.js').done();
