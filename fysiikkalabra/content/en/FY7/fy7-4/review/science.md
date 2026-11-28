VERDICT: PASS
CONTENT-HASH: 0ea0e18f925c92b3

## Blocking

## Polish
- lesson.md:211 — the pre-2019 ampere definition leaves out its conditions: the same current in both wires, infinitely long straight wires with negligible cross-section, in a vacuum. Without them a student can read it as true for any two wires (B). Fix: "…when the same current in two very long parallel wires $1\,\text{m}$ apart in a vacuum gives a force of…".
- lesson.md:160 — "transformed into internal energy of the coil and the magnet": the Joule heating is mainly in the voice coil. Following the guardrail wording, say it becomes internal energy, mainly of the coil, which is transferred to the surroundings as heat.
- assets/sims/fy7/fy7-4/sim.js:880–883 — in the top view the α arc is measured from a dashed line that points right, which is against the field arrows (N on the right, B to the left). The force is right because sin(180° − α) = sin α. Still, a student who reads "angle between the current and the field" literally sees the supplement. Drawing the reference line to the left (along $\overline{B}$) would match the formula section's figure.
- lessons/FY7/fy7-4/lesson-answers.py:718 — the comment "wire east–west" does not match the check-2 task, which names no direction. The numbers are right.

## Checked
- One script recomputed every number of the worked example (l = 4.90 m, F = 6.98 N → 7.0 N, about 71 times the 10 g weight), pysähdy (0.25 N), retrieval (10 → 5.0 µT), siirto (B₁ = 2.0 mT, about 40 × the Earth's field, F = 0.60 N, about 61 g; mistakes 0.0060, 3.77, 0.30 N), check-2 (0.20 N; 0.346, 0.40), virhe (0.15 N vs cos 0.26 N) and exit ticket 1 (0.30 N). All agree with the text and lesson-answers.py.
- Sim readings at magnet A, l = 5.0 cm (rounded as the sim rounds): 247.75, 242.85, 246.52 (3 A and 30°), 247.42 (60°). Changes are 2.45, 1.22 and 2.12 g, so B = 0.0240 N : (0.30 A·m) = 0.080 T. The predictions' feedback and the conclusion's model answer match.
- Cross-product directions in every figure: swing (force left), motor (cross side down, dot side up, anticlockwise), speaker (both gap halves toward the cone), angle (force into the page), wires (same direction attract), exit ticket 2 (east × north = up).
- sim.js: F = IlB sin α, positive is up for I > 0 with B to the left, the magnet is pushed down and m = m₀ + F/g. The leads' forces are horizontal. The dot/cross symbols and the side-view current symbol are right. simState gives `lukema`.
- koe-1 and koe-2 lock alpha/magneetti/l and I/magneetti/l. The initial values exist as slider steps and select values ('5'). The 3, 6, 30 and 60 settings can be reached.
- Exactly one correct option in each of ennuste-suunta, ennuste-2, kertaus, virhe and check-1. Each distractor's feedback is correct.
- Motor: the forces are radial when the loop is perpendicular to the field, the commutator reverses the current every half turn, and the loop oscillates without a commutator. Loudspeaker: the radial field is needed because the net force on a closed coil in a uniform field is zero.
- Scope: the force on a wire and between two wires, the motor and the loudspeaker are within the fy7-4 slot. μ₀ is given in Vs/(Am). No self-induction.
