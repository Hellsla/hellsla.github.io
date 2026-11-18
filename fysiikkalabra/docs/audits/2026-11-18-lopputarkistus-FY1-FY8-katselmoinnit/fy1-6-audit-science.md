VERDICT: PASS
CONTENT-HASH: 2b496ad3e6b080b1

## Blocking

## Polish
- inquiry.json:116 (simulation `model`): the box names only wind and spin as neglected. The sim (sim.js `KDRAG`) also leaves out buoyancy and uses a fixed drag coefficient of 0,47 and an air density of 1,2 kg/m³. Buoyancy changes v(4 s) of the 0,1 kg ball from 10,5 to 10,2 m/s. Fix: add "ja ilman noste" (or nothing, since buoyancy is outside FY1's scope). Severity Minor, kind C/B.
- inquiry.json:339 (`data` solution, Vastaus): "Mittauspisteet poikkeavat suorasta noin 0,1 m/s". The real residuals from the line g = 9,81 m/s² are at most 0,04 m/s, and 0,1 m/s is the data's resolution. Fix: "Mittaustarkkuus on 0,1 m/s, joten …". The conclusion of about 0,2 m/s² still stands. Severity Minor.
- lesson.md:525 (same-fall aria-label): "Katkoviiva kulkee molempien nuolten kärkien kautta" is not quite true. Both arrows start at the ball's edge, so the 1 kg ball's tip lies 8 px above the dashed line at t = 1 s and at t = 2 s. The ball centres and arrow lengths are equal, as they should be. Fix: draw the line through the centres, or match the tips. Severity Minor.
- glossary.json, putoamiskiihtyvyys (in the packet, not a lesson file): "kuinka monta newtonia yhden kilogramman massan paino on" brings in force. The FY1 scope note leaves force to FY2. Severity Minor, for the glossary owner.
- lesson.md:693 (Järkevyys): the "53 km/h city speed" remark is not a check. The interpolation sentence before it is the real check and is enough. Severity Minor (style).

## Checked
- One script recomputed every number: exp-1 9,81 (9,8); data slope 9,8 (least squares through the origin 9,78); siirto 3,7 → 11,1 m/s; check-2 3,058 s; example 14,715 m/s and 52,97 km/h; exit 4,86, 29,4 and 6,06; kertaus 1,08. Every mistake value (1,82, 0,93, 2,7, 19,6, 29,4, 22,2, 11,0, 0,327) matches the error its feedback names. lesson-answers.py agrees.
- The Moon hammer is realistic: 1,4 m in 1,31 s at 1,62 m/s².
- sim.js: vacuum v = gt; in air v = v_T tanh(gt/v_T) with K = ½ρC_dA. In exp-3, 0,1 kg → 10,5 m/s and 10 kg → 37,5 m/s, the same as the explain model answer. Every fall stays under 80 m and 40 m/s. simState gives vA and vB.
- Each experiment's setup isolates its varied parameter: equal-size balls, the environment locked, t or mB varied, slider steps reach the suggested values.
- The free-fall figure is to scale as claimed: positions 4,9/19,6/44,1 m at 8,6 px/m, arrows ∝ v. The vt-graph points and its slope of 9,81 are right. The data-figure points lie on its grid.
- Every prediction, check and Etsi virhe has exactly one correct option, and the distractor feedback is right.
- The conditions are stated where the laws are used: no air resistance, starting from rest, Δv = gΔt only for downward motion.
- Theory, summary, misconception box, model answers and exit ticket agree; air, not mass as such, causes the difference.
- Significant figures are justified throughout (1,5 s → two; 108 km/h → three).
- The lesson stays inside FY1 scope: a linear model and no forces.

## Scores
- 1 Physics and mathematical correctness: 5. Every number reproduces, the conditions are stated, and the figures are to scale. Only Minor findings.
- 6 Experimental reasoning (physics): 4. Variables are controlled and the simulated data is labelled. The sim's model assumptions are not all stated, and the residual statement in the data solution is loose.

Severities: all five findings Minor; no Critical or Major.
