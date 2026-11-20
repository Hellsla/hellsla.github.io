VERDICT: PASS
CONTENT-HASH: 1c475d117a3c45bd

## Blocking
(none)

## Polish
- inquiry.json pred-3 feedback (Aino, Bea, Cem) — "Teoriatiivistelmä" / "Teoriatiivistelmässä" names a stage the page calls *Teoria* (CLAUDE.md "Lesson page" 5) — write "luvun Teoria-osassa" or just "teoriassa".
- inquiry.json check-c2 vs pred-3 — the same situation (narrow tube vs wide basin, same height) is asked twice with only the numbers changed, so the check tests recall of the prediction's answer, not transfer — change the check to a different vessel (e.g. a slanted or bulging vessel with equal depth, or two depths in one vessel) or make it optional.
- sim (Tutki, 390 and 1280 px captures) — the readout already prints ρgh and p, and the line "Jokainen syvyysmetri lisää painetta ρg · 1 m verran" shows the slope before the student reads it from data in exp-1's numeric question; sim-spec.md says ρg is not printed. Remove that line, or keep it only behind Laskennan selitys. As the brief warns, the sim computes the formula it predicts; the model note and conclusion do say "mallin arvot", which is enough for this slot.
- lesson.md "Mistä paine syntyy?" — about 150 words in one paragraph carrying the microscopic cause, the derivation and the independence of container shape; split after "...ja jäljelle jää ρgh." so the derivation and the conclusion are separate ideas.

## Checked
- Path: hook (ear pressure) → weight retrieval (optional) → predictions → sim/experiment → theory → example → exercises → checks; the dam question is answered in "Ilmanpaine ja ylipaine" only after the student has committed.
- Slot goals met: p = F/A, ρgh, line with constant term p₀ (graph slope and intercept read in exp-1, check-2), force perpendicular so scalar; no FY4 content.
- Predictions can be refuted by exp-1 (2 measurements, the 1.3-fold total vs 2-fold overpressure); wrong-option feedback names the evidence and repairs the confusion of total pressure with overpressure.
- Variable control is correct: exp-1 locks ρ, varies h; exp-2 the reverse (optional).
- Worked example has seven stages, one step each, symbolic before numeric, window force with the room's air pressure explained.
- Etsi virhe (depth measured from the surface) and the mercury barometer transfer task have hints and real common-mistake feedback.
- Checks: concept distractors are misconception-based; the explain criteria are observable and match the question (eardrum, overpressure, F = Δp·A).
- Exit ticket tests the core idea (p = F/A; ρgh plus p₀).
- Finnish and units read correctly; the approved formula-row name is not a finding.
- Phone captures (390 px) legible; wide layout puts sim beside the experiments.
