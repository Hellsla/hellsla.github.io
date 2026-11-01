// FY14 Charged particles and magnetic confinement: the model (no drawing). One charged particle in a static magnetic
// field, non-relativistic (every speed the sim offers is below 0.04 c), no collisions, no radiation, no other particles.
// Masses CODATA 2022, elementary charge exact (SI 2019).
//   Uniform field B along z (perpendicular to the page): the magnetic force q v × B is perpendicular to the velocity, so
//   the speed is constant and the particle moves on a circle of radius r = m v⊥ / (|q| B) with the period
//   T = 2π m / (|q| B), independent of the speed; it turns clockwise for a positive charge when B points out of the page.
//   With an electric field E in the plane (perpendicular to B) the guiding centre drifts at v_d = E × B / B², of size
//   E / B, the same for every charge and mass; in the frame moving at v_d the particle gyrates as without E. The motion
//   is solved exactly (uniform()).
//   Field along x (side view): v∥ = v cos θ along the field, v⊥ = v sin θ around it, so the orbit is a helix. In the
//   magnetic mirror the field grows towards the ends, B(x) = B0 g(x/L) with g = 1 + (Rm − 1)(x/L)² inside the device
//   (|x| ≤ L, B = Rm B0 at the mirror throats) and falling again outside. The magnetic moment μ = m v⊥² / (2B) is
//   conserved (guiding-centre approximation: the field changes little within one gyration) and so is the kinetic
//   energy, so v⊥² = v⊥0² B/B0 and the mirror force F∥ = −μ dB/dx pushes the particle back towards the weak field. It
//   is reflected before the throat if sin²θ0 ≥ B0/Bmax = 1/Rm; smaller pitch angles (the loss cone) escape.
(function (root) {
  const e = 1.602176634e-19;                                        // C, exact
  const PARTICLES = {                                               // CODATA 2022 masses (kg), charges (C)
    p: { m: 1.67262192595e-27, q: e, z: 1 },                       // proton
    d: { m: 3.3435837768e-27, q: e, z: 1 },                        // deuteron
    e: { m: 9.1093837139e-31, q: -e, z: -1 },                      // electron
    a: { m: 6.6446573450e-27, q: 2 * e, z: 2 },                    // alpha particle (helium-4 nucleus)
  };
  const RM = 4;                                                     // mirror ratio Bmax / B0 of the sim's mirror

  const radius = (m, q, vperp, B) => m * Math.abs(vperp) / (Math.abs(q) * B);          // m
  const period = (m, q, B) => 2 * Math.PI * m / (Math.abs(q) * B);                      // s
  const frequency = (m, q, B) => Math.abs(q) * B / (2 * Math.PI * m);                   // Hz
  const omega = (m, q, B) => Math.abs(q) * B / m;                                       // rad/s
  const driftSpeed = (E, B) => E / B;                                                   // m/s
  const mu = (m, vperp, B) => m * vperp * vperp / (2 * B);                              // J/T
  const lossConeDeg = (Rm) => Math.asin(Math.sqrt(1 / Rm)) * 180 / Math.PI;
  // reflected by a mirror of ratio Rm when sin²θ ≥ 1/Rm (θ the pitch angle where B is weakest); θ = 90° stays put
  const mirrorTrapped = (pitchDeg, Rm) => { const s = Math.sin(pitchDeg * Math.PI / 180); return s * s >= 1 / Rm - 1e-12; };

  // Uniform B = (0, 0, dir·B), E = (0, E, 0) (dir +1 out of the page, −1 into it); the particle starts at the origin
  // with velocity (v, 0). Returns position (m) and velocity (m/s) at time t (s), and the drift and gyration data.
  function uniform(m, q, v, B, dir, E, t) {
    const Bz = dir * B, W = -q * Bz / m;                             // signed rotation rate of the velocity (counter-clockwise > 0)
    const vdx = E / Bz, vdy = 0;                                    // E × B / B² = (E Bz, 0) / Bz²
    const ux = v - vdx, uy = -vdy;                                  // velocity in the drifting frame
    const c = Math.cos(W * t), s = Math.sin(W * t);
    const vx = vdx + ux * c - uy * s, vy = vdy + ux * s + uy * c;
    // ρ = (uy, −ux)/W is the position relative to the gyration centre, rotating with the velocity
    const r0x = uy / W, r0y = -ux / W, rx = r0x * c - r0y * s, ry = r0x * s + r0y * c;
    return { x: vdx * t + rx - r0x, y: vdy * t + ry - r0y, vx, vy, cx: vdx * t - r0x, cy: vdy * t - r0y,
             vd: [vdx, vdy], rg: Math.hypot(ux, uy) / Math.abs(W), W };
  }

  // the mirror's field profile B/B0 = g(s), s = x/L, and dg/ds; Rm = 1 is the straight uniform field
  function profile(s, Rm) {
    if (Rm <= 1) return { g: 1, dg: 0 };
    const a = Math.abs(s), sg = s < 0 ? -1 : 1;
    if (a <= 1) return { g: 1 + (Rm - 1) * s * s, dg: 2 * (Rm - 1) * s };
    const u = a - 1, den = 1 + 3 * u * u;                           // outside the throat the field weakens again
    return { g: Rm / den, dg: -sg * Rm * 6 * u / (den * den) };
  }

  // the side view: the guiding centre at x (m) on the axis, half-length L (m) of the device, B0 at its middle
  function createAlong(m, q, v, pitchDeg, B0, L, mirror) {
    const th = pitchDeg * Math.PI / 180;
    return { m, q, v, B0, L, Rm: mirror ? RM : 1, vperp0: v * Math.sin(th), x: 0, vpar: v * Math.cos(th), phi: 0,
             t: 0, refl: 0, escaped: false, xmax: 0 };
  }
  const alongField = (s) => { const P = profile(s.x / s.L, s.Rm); return { B: s.B0 * P.g, dB: s.B0 * P.dg / s.L }; };
  // derived quantities at the particle's position: v⊥ from μ conservation, the gyroradius, the axial mirror force
  function alongState(s) {
    const F = alongField(s), vperp = s.vperp0 * Math.sqrt(F.B / s.B0);
    const muv = mu(s.m, s.vperp0, s.B0);
    return { B: F.B, vperp, r: radius(s.m, s.q, vperp, F.B), Fpar: -muv * F.dB, Fperp: Math.abs(s.q) * vperp * F.B, mu: muv };
  }
  // advances by dt (s) in substeps of at most h (s): velocity Verlet for the guiding centre, the gyrophase with the
  // local cyclotron frequency (negative sense about +x for a positive charge). Escape: beyond 1.12 L.
  function stepAlong(s, dt, h) {
    if (s.escaped) return;
    const n = Math.max(1, Math.ceil(dt / h)), k = dt / n, acc = () => -(s.vperp0 * s.vperp0 / (2 * s.B0)) * alongField(s).dB;
    for (let i = 0; i < n; i++) {
      const a0 = acc(), sg0 = Math.sign(s.vpar);
      s.vpar += 0.5 * a0 * k; s.x += s.vpar * k; s.vpar += 0.5 * acc() * k;
      if (sg0 !== 0 && Math.sign(s.vpar) === -sg0) s.refl++;
      s.phi += -Math.sign(s.q) * omega(s.m, s.q, alongField(s).B) * k;
      s.t += k; s.xmax = Math.max(s.xmax, Math.abs(s.x));
      if (Math.abs(s.x) > 1.12 * s.L) { s.escaped = true; break; }
    }
    // the kinetic energy is conserved: v∥ follows from μ exactly, the Verlet step keeps only the sign and the turning
    const vp2 = s.v * s.v - s.vperp0 * s.vperp0 * profile(s.x / s.L, s.Rm).g;
    if (vp2 > 0 && Math.abs(s.vpar) > 0.05 * s.v) s.vpar = Math.sign(s.vpar) * Math.sqrt(vp2);
  }

  const api = { e, PARTICLES, RM, radius, period, frequency, omega, driftSpeed, mu, lossConeDeg, mirrorTrapped, uniform,
                profile, createAlong, alongState, stepAlong };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.FY14Magnetic = api;
})(typeof window !== 'undefined' ? window : globalThis);
