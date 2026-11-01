// Physics tests of the FY14 magnetic model (assets/sims/fy14/magnetic/model.js), run by scripts/test_models.py with node.
// Every particle, speeds and fields across the sim's sliders, both field directions, with and without E, every pitch angle.
const M = require('../../assets/sims/fy14/magnetic/model.js');
const { check, near, done } = require('./_assert.js');
const rel = (name, got, want, tol) => check(`${name}: got ${got}, expected ${want}`, Math.abs(got - want) <= tol * Math.abs(want));
const e = 1.602176634e-19;
rel('proton r at 2.00e6 m/s, 1 T', M.radius(M.PARTICLES.p.m, e, 2e6, 1), 0.0208794, 1e-5);
rel('proton T at 1 T', M.period(M.PARTICLES.p.m, e, 1), 6.55945e-8, 1e-5);
rel('electron f at 1 T', M.frequency(M.PARTICLES.e.m, -e, 1), 2.79925e10, 1e-5);
for (const k of Object.keys(M.PARTICLES)) for (const v of [1e5, 5.05e6, 1e7]) for (const B of [0.1, 2.5, 5]) for (const dir of [-1, 1]) for (const E of [0, 2e5]) {
  const P = M.PARTICLES[k], id = `${k} v=${v} B=${B} dir=${dir} E=${E}`, T = M.period(P.m, P.q, B);
  // Boris integration of m dv/dt = q (E + v × B) against the exact solution over one period
  let x = 0, y = 0, vx = v, vy = 0; const n = 4000, h = T / n, Bz = dir * B;
  for (let i = 0; i < n; i++) {
    const qh = P.q * h / (2 * P.m), ax = vx, ay = vy + qh * E, t = qh * Bz, s = 2 * t / (1 + t * t);
    const px = ax + ay * t, py = ay - ax * t, nx = ax + py * s, ny = ay - px * s;
    vx = nx; vy = ny + qh * E; x += vx * h; y += vy * h;
  }
  const g = M.uniform(P.m, P.q, v, B, dir, E, T), rr = M.radius(P.m, P.q, v, B);
  check(`${id}: exact solution matches Boris after one period`, Math.hypot(g.x - x, g.y - y) < 2e-3 * (rr + Math.abs(E / B) * T));
  check(`${id}: drift over one period is (E/B) T along E × B`, Math.abs(g.x - E / Bz * T) <= 1e-9 * (rr + Math.abs(E / Bz * T)) && Math.abs(g.y) <= 1e-9 * rr);
  check(`${id}: |v| constant without E`, E || Math.abs(Math.hypot(g.vx, g.vy) - v) < 1e-6 * v);
  if (!E) { const q = M.uniform(P.m, P.q, v, B, dir, 0, T / 4);   // quarter turn: clockwise for q B_z > 0
    check(`${id}: sense of rotation`, Math.sign(q.vy) === -Math.sign(P.q * Bz)); }
}
// mirror: reflected exactly when sin²θ ≥ 1/Rm, and μ conserved along the way
for (const k of Object.keys(M.PARTICLES)) for (let th = 5; th <= 85; th += 5) {
  const P = M.PARTICLES[k], v = 2e6, B0 = 1, L = 125 * M.radius(P.m, P.q, v, B0) / 30, s = M.createAlong(P.m, P.q, v, th, B0, L, true);
  const wmax = M.omega(P.m, P.q, 4 * B0), h = Math.min(0.1 / wmax, 0.004 * L / v);
  const mu0 = M.alongState(s).mu; let muErr = 0;
  for (let i = 0; i < 4000 && !s.escaped && s.refl < 3; i++) { M.stepAlong(s, 20 * h, h); const q = M.alongState(s); muErr = Math.max(muErr, Math.abs(M.mu(P.m, q.vperp, q.B) - mu0) / mu0); }
  const trapped = M.mirrorTrapped(th, M.RM);
  if (Math.abs(Math.sin(th * Math.PI / 180) ** 2 - 0.25) > 0.02) check(`${k} θ=${th}: ${trapped ? 'reflected' : 'escapes'}`, trapped ? s.refl >= 2 && !s.escaped : s.escaped && s.refl === 0);
  check(`${k} θ=${th}: μ conserved`, muErr < 1e-9);
  const q = M.alongState(s); near(`${k} θ=${th}: kinetic energy conserved`, s.vpar ** 2 + q.vperp ** 2, v * v, 0.01);
}
near('loss cone of Rm = 4 is 30°', M.lossConeDeg(4), 30, 1e-9);
done();
