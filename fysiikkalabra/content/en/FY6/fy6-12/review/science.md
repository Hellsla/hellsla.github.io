VERDICT: PASS
CONTENT-HASH: cc28d887684ce5bf

## Blocking
(none)

## Polish
- lesson.md:559 — "these radiate the energy as light": only part of the collision energy becomes light. Say "radiate part of it as light".
- lesson.md:630 — "So $1\,\text{keV} = 1000\,\text{eV}$" does not follow from the line before. Write "and".
- sim.js bars comment — says "E_p green", but the bar is drawn in ink. This is a code comment only.

## Checked
- One script recomputed every number from the task text with my own formulas and matched lesson-answers.py: E = 5000 V/m, F/G = 4.9·10¹⁰, worked example 4.806·10⁻¹⁶ J and 3.248·10⁷ m/s, crossing times 161.6/323.2/646.3 ns, speeds 309/13 262/220 km/s (ratio 43), transfer 42.0 km/s and its mistakes, check 2 300 eV, exit −50 eV, aurora 4.2·10⁷ m/s.
- Classical ½mv² is justified: at 3 keV the relativistic v/c is 0.1079 vs 0.1083, and the sim stays at or below 6.3 % of c.
- Gravity neglect is stated with the right magnitudes (at least 4.9·10⁹ in the sim's weakest field).
- Sign logic is the same in the theory, the energy bars, the error task, check 1, the predictions, the summary and the exit ticket: E_p = qV, the electron moves toward the higher potential, and E_p decreases.
- The formula section names the right law (V = E_p/q with E_p = qV under it). The zero points are stated, and the vx-graph and equipotential figure are to scale.
- Photo captions are correct: the cloud–ground potential difference, internal energy transferred as heat, a negative cloud base, the plasma ball's drive.
- Each choice item has exactly one correct option, and the distractor feedback names the right mechanism.
- Each experiment isolates its varied parameter. simState carries E, tns, EkeV, EpeV and vkms, and the adapter's reset matches.
- sim.js integrates exactly at constant acceleration and gets E_k from v, not from |q|U, so the result emerges. The electron is shown 40× slower, as the howto says.
- Scope is FY6 central content.
