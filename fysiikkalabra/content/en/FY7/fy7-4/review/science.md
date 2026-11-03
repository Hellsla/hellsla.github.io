VERDICT: PASS
CONTENT-HASH: e68558154b2428a0

## Blocking

## Polish
- lesson.md:312 — the pre-2019 ampere definition omits its conditions — add "two long, thin parallel wires in vacuum, each carrying the current".
- inquiry.json tarkistus-3 model — "so the coil would not move": in a uniform field the net force on a closed coil is zero but a torque can still turn it — say "nothing would push the coil along its axis", as lesson.md:227 does.
- assets/sims/fy7/fy7-4/sim.js:926 — the length options '2,5 cm' and '5,0 cm' keep the Finnish decimal comma on the English page (shots sim-1280, koe-2), unlike the readout (language only).
- sim.js:1014–1016 — the top view's α arc starts from the dashed line pointing towards N, that is against $\overline{B}$ (correct for the line, sin α = sin(180° − α)); starting the arc from the field direction would match the lesson's angle figure.

## Checked
- Recomputed in one script: worked example l = 4.90 m, F = 6.98 N → 7.0 N, F/weight ≈ 71; sim readings 247.75 / 242.85 / 246.52 g, Δm 2.45, 1.22 (3 A and 30°), 2.12 (60°), 0 (0°); B = 0.0801 T → 0.080 T; magnet B Δm 3.67 g.
- siirto: B₁ = 2.0 mT, F = 0.60 N, repulsion; mistakes 0.0060, 3.77, 0.30 N; ≈ 40 × Earth's field, ≈ 61 g weight. virhe 0.15 vs 0.26 N; tarkistus-2 0.20, mistakes 0.346 and 0.40 N; exit ticket 0.30 N, east × north = up.
- Figure directions checked with the cross product: swing (I into page, B down → F left; rule panel I × B down), motor (forces down/up, anticlockwise), speaker (radial B, both forces towards the cone), angle figure (F into page, B sin α perpendicular to the wire), wires (anticlockwise field for current out of page; parallel attract, antiparallel repel).
- sim.js implements F = I l B sin α with m = m₀ + F/g by Newton's third law; sign of the reading, side-view cross and top-view dot agree with I × B (shot koe-2); simState gives `lukema`; koe-1 varies only I, koe-2 only α.
- Predictions: exactly one correct option each; distractor feedback names the right physics.
- Motor: no torque at the plane perpendicular to B, commutator every half turn; check-1 single correct option, its swinging-about-equilibrium feedback right.
- Loudspeaker: net force zero on a closed coil in a uniform field, radial field gives axial force — theory, figure and tarkistus-3 agree.
- Scope within LOPS FY7; copper "not attracted" is a fair C.
