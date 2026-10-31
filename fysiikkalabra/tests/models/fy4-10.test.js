// Physics tests of the fy4-10 model (assets/sims/fy4/fy4-10/model.js), run by scripts/test_models.py with node: every
// collision type with every mass the sim offers and a spread of initial velocities (not only the defaults).
const M = require('../../assets/sims/fy4/fy4-10/model.js');
const { check, near, done } = require('./_assert.js');
const masses = [0.2, 0.4, 0.6], v1s = [0.1, 0.3, 0.6, 1.0], v2s = [-1.0, -0.4, 0, 0.05];

for (const typ of ['kimmoisa', 'kimmoton', 'tarra', 'rajahdys']) for (const m1 of masses) for (const m2 of masses)
  for (const v1 of typ === 'rajahdys' ? [0] : v1s) for (const v2 of typ === 'rajahdys' ? [0] : v2s) {
    if (typ !== 'rajahdys' && v1 - v2 < 0.2) continue;                             // glider 1 must catch up with glider 2 before 12 s
    const id = `${typ} m1=${m1} m2=${m2} v1=${v1} v2=${v2}`;
    let pWorst = 0, eWorst = 0, negE = false, dMax = 0, gap = Infinity, sawEp = 0, ekMin = Infinity, forcesOk = true;
    const s = M.run(typ, m1, m2, v1, v2, 2e-4, (q) => {
      const E = M.energies(q);
      pWorst = Math.max(pWorst, Math.abs(M.momentum(q) - q.P0));
      eWorst = Math.max(eWorst, Math.abs(E.Ek + E.Ep + E.Esis - q.E0));
      if (E.Ek < -1e-12 || E.Ep < -1e-12 || E.Esis < -1e-9) negE = true;
      dMax = Math.max(dMax, M.overlap(q)); gap = Math.min(gap, q.x2 - q.x1); sawEp = Math.max(sawEp, E.Ep); ekMin = Math.min(ekMin, E.Ek);
      if (q.F < 0) forcesOk = false;                                                // the bumpers only push
    });
    const P0 = s.P0, E0 = s.E0, Eend = M.energies(s);
    check(`${id}: the collision happened and ended`, s.after !== null);
    near(`${id}: total momentum before = after`, s.m1 * s.after.u1 + s.m2 * s.after.u2, P0, 1e-6);
    check(`${id}: total momentum is the same at every step (worst ${pWorst.toExponential(1)})`, pWorst < 1e-9);
    check(`${id}: E_k + E_p + E_sis stays the starting energy at every step (worst ${eWorst.toExponential(1)} J)`, eWorst < 0.002 * Math.max(E0, 0.01));
    check(`${id}: no energy is negative`, !negE);
    check(`${id}: the gliders never pass through each other: the bumpers squeeze less than their length`, dMax < 2 * M.BUMP && gap > M.L - 2 * M.BUMP);
    check(`${id}: the gliders stay on the track`, s.x1 - M.L / 2 >= -0.01 && s.x2 + M.L / 2 <= M.TRACK + 0.01);
    check(`${id}: the bumper forces only push (equal and opposite by construction)`, forcesOk);
    const Ek0 = 0.5 * m1 * v1 * v1 + 0.5 * m2 * v2 * v2, Ek1 = 0.5 * s.m1 * s.after.u1 ** 2 + 0.5 * s.m2 * s.after.u2 ** 2;
    if (typ === 'kimmoisa') {
      near(`${id}: kinetic energy before = after`, Ek1, Ek0, 0.002);
      check(`${id}: during the collision E_k dips and the spring holds the difference (E_p > 0)`, sawEp > 0 && ekMin < Ek0 - 0.5 * sawEp);
      near(`${id}: no internal energy`, Eend.Esis, 0, 1e-4);
      near(`${id}: v1' from the elastic formula`, s.after.u1, ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2), 0.01);
    }
    if (typ === 'kimmoton') {
      check(`${id}: part of E_k becomes internal energy`, Eend.Esis > 0.02 * Ek0 && Ek1 < Ek0);
      near(`${id}: what E_k lost is E_sis`, Ek0 - Ek1, Eend.Esis, 0.002);
      check(`${id}: the gliders separate after the collision`, s.after.u2 > s.after.u1);
    }
    if (typ === 'tarra') {
      check(`${id}: the gliders stick together`, s.stuck);
      check(`${id}: exactly the same final velocity`, s.after.u1 === s.after.u2 && s.w1 === s.w2);
      near(`${id}: common velocity = total momentum / total mass`, s.after.u1, (m1 * v1 + m2 * v2) / (m1 + m2), 1e-6);
      near(`${id}: kinetic energy lost = ½ μ v_rel²`, Ek0 - Ek1, 0.5 * (m1 * m2 / (m1 + m2)) * (v1 - v2) ** 2, 0.002);
      near(`${id}: the lost kinetic energy is internal energy`, Eend.Esis, Ek0 - Ek1, 0.002);
      check(`${id}: they stay together to the end`, Math.abs(s.x2 - s.x1 - (M.L - M.overlap(s))) < 1e-9 && s.w1 === s.w2);
    }
    if (typ === 'rajahdys') {
      near(`${id}: the spring starts with ½ k d² = 0,24 J`, E0, 0.24, 1e-9);
      near(`${id}: total momentum stays zero`, M.momentum(s), 0, 1e-9);
      near(`${id}: equal and opposite momenta`, s.m1 * s.after.u1, -s.m2 * s.after.u2, 1e-6);
      check(`${id}: the gliders move apart in opposite directions`, s.after.u1 < 0 && s.after.u2 > 0);
      near(`${id}: the spring's 0,24 J became kinetic energy`, Ek1, 0.24, 0.002);
    }
  }
// scales: what a run shows never exceeds the bounds the sim draws with
for (const typ of ['kimmoisa', 'kimmoton', 'tarra', 'rajahdys']) for (const [m1, m2, v1, v2] of [[0.2, 0.6, 1, -1], [0.6, 0.2, 1, -1], [0.4, 0.4, 0.6, 0]]) {
  const B = M.bounds(typ, m1, m2, v1, v2); let ok = true;
  M.run(typ, m1, m2, v1, v2, 2e-4, (q) => { const E = M.energies(q);
    if (Math.abs(q.m1 * q.w1) > B.P * 1.001 || Math.abs(q.m2 * q.w2) > B.P * 1.001 || Math.abs(q.w1) > B.V * 1.001 || Math.abs(q.w2) > B.V * 1.001
        || E.Ek + E.Ep + E.Esis > B.E * 1.01 || q.F > B.F * 1.01) ok = false; });
  check(`${typ} ${m1}/${m2}: momentum, velocity, energy and force stay inside the drawing scales`, ok);
}
done();
