VERDICT: PASS
CONTENT-HASH: 1e51956df59067b8

## Blocking

## Polish
- solutions.md (L2-02), exercises.json (L2-02, L3-01) — The tasks use "noste" for buoyancy, while the lesson's worked-example figure labels wing lift $\overline{F}_\text{noste}$ (see the lesson report). No change is needed here if the lesson renames its lift symbol.

## Checked
- All 12 answers recomputed independently: 18 N, 850 N, 90 N, 240 N, 6,38 → 6,4 N, 13 N, 65 N, 833,9 → 830 N, 8,94 → 8,9 kN, 0,27 kN upward, 0,60 N, 1,9 N. answers.py agrees, and each answer is within its tolerance.
- The physics models are right. First-law equilibria and third-law pairs are kept apart in every solution. In L2-01 the force passes along a chain of pairs to the table. In L3-02 the magnetic pair acts without contact. In L3-03 the scale reads the force on its hook.
- Force diagrams described in the solutions are correct: the chosen body is a rectangle, $\overline{G}$ is drawn from the centre, $\overline{N}$ and $\overline{T}$ from the contact or attachment surface, and a pushing force ends at the body. Reaction forces on other bodies are excluded and named, as in L1-03 and L1-05. Velocity is not drawn as a force (L2-03, L3-01).
- Directions are right: drag points up while the balloon and the parachutist move down, and the book pulls the Earth upward.
- Every solution states the positive direction, writes the equation symbolically before substituting, and gives units. Rounding follows the limiting datum. Each reasonableness check is a real check: the tug-of-war is won by ground friction, and the lift's cable tension is the same at rest as at constant speed.
- The varied L2-02 (weight and buoyancy as distractors) and the L3-01 wording (size checked, direction asked in words) are consistent with the answers.
