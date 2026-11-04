VERDICT: FAIL
CONTENT-HASH: 7e12525e7056284a

## Blocking
- exercises.json:247 (L2-07) — A: the answer box holds `1.96` (three figures), but the solution's Vastaus (solutions.md:332) gives $2{,}0\,\text{m/s}^2$ "kaksi merkitsevää numeroa kuten tiedoissa", so the answer and its solution disagree — set `"answer": 2.0`, `"tolerance": 0.02` and `within(..., 2.0, 0.02)` in lessons/FY4/fy4-13/answers.py:48 (|2,0 − 1,962|/1,962 = 1,9 %). Or, if you keep 1.96, make the Vastaus say $1{,}96\,\text{m/s}^2$ and give the reason for three figures.
- solutions.md:310 (L2-06) — A: the rounding reason is false. $a = 2{,}84\,\text{m/s}^2$ and $m_1 = 1{,}20\,\text{kg}$ have three significant figures, not two — give the real reason for two figures: the two equations give 3,41 N and 3,49 N, which differ by about 2 %, so only two figures are reliable. Or answer $3{,}41\,\text{N}$.
- solutions.md:353 (L3-05) — B: the solution writes $T = m_1 a$ and $m_2 g - T = m_2 a$ without naming any force or positive direction, which breaks the force-diagram standard ("never ΣF = ma without first naming the forces and the positive direction") — add a **Voimakuvio:** line before **Kaava:**, as in L2-06, with a `voimakuvio` block for $m_2 = 0{,}200\,\text{kg}$: the cart with $\overline{G}_1$ and $\overline{N}$, $\overline{T}_1$ to the right, positive to the right; the weight with $\overline{G}_2$ down, $\overline{T}_2$ up, positive down.

## Polish
- solutions.md:345 (L3-04) — the Vastaus lists the parts in the order b), a), c). Order them a), b), c) and keep the answer-box note on b).
- exercises.json:284 (L3-04) — "ne ovat kytketty" → "ne on kytketty".
- solutions.md (L3-04) — the task asks for every wagon's force diagram, but the model solution only describes them in words. Add a `voimakuvio` block for the three wagons, as the other solutions have.
- L2-06 — the bank plan line "kärry + punnus -mittaustaulukko → kitkan arvio" is not met: the task assumes a frictionless track. The 2 % gap between the two T values could serve as the friction estimate (about 0,08 N). This is optional.
- solutions.md:287 (L2-05) — "kuten mittaustuloksissa": the data have two or three figures (0,96; 2,02). Say instead that a line fitted by hand gives two figures.

## Checked
- New answers recomputed in one script: L1-07 3,924; L2-05 least-squares k = 19,53 → g = 9,77; L2-06 3,408 and 3,485; L2-07 1,962; L3-04 a = 0,500, 15,03 kN and 21 kN; L3-05 0,920, 0,930, 0,877, 0,907 → 0,909 kg, v = 1,67 m/s. All are inside their tolerances.
- The L1-06 and L1-08 multiple-choice tasks each have exactly one correct option, and every distractor's feedback is right.
- The L2-05 Atwood relation $a = g\,\Delta m/M$ comes from the lesson's equations. The line through the origin has a physical reason, and the residuals are ≤ 0,07 m/s².
- The L2-07 error (dropping $m_2 a$) matches the planned "koko systeemin massa unohdettu".
