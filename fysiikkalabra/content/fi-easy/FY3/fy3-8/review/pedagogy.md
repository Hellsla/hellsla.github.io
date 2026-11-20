VERDICT: PASS
CONTENT-HASH: 10c4c512e2a5ece4

## Blocking
(none)

## Polish
- inquiry.json exp-1/exp-2, sim — the model draws Δl straight from Δl = αl₀ΔT and prints that formula under the canvas, so both experiments confirm the program's arithmetic (the model box says so honestly). Material, the third thing Δl depends on, is never varied in an experiment: learn goal 2 ("tutkimaan kokeilla, mistä pituuden muutos riippuu") is met only for ΔT and l₀. Add an optional run that varies only the material at fixed l₀ and ΔT, and let the student read α from the graph lines.
- inquiry.json pred-1 and pred-2 — both correct options are the bare word "Kaksinkertainen.", so a student can guess the pattern without reasoning; vary the form (e.g. ask for the ratio in mm for given α) and keep the justification box.
- inquiry.json olomuodot — the correct option says weaker interactions make gases expand most, but the table's gas value is a constant-pressure result the student cannot tie to interactions; the option is the longest. Ask the science reviewer whether the wording is safe; the pedagogy fix is a question on what the table shows (order of magnitude by state) plus the micro-model for solids only.
- lesson.md Kaava — the γ paragraph holds about 150 words (γ ≈ 3α derivation, validity range, water's variable γ); split into two paragraphs.
- inquiry.json siirto — the prompt carries three assumptions in one long sentence and mixes cm³ and mm²; fine as an optional transfer, but state the assumptions as a short list.

## Checked
- Path: prior (ΔT in K) → hook (bridge joint) → three predictions → sim with a controlled experiment (T only) and an optional one (l₀ only) → interpret table by state of matter → theory → 7-stage example → checks. The opening question is answered.
- Micro-model: particles stay the same size; the asymmetry of the interaction explains why the mean distance grows (pred-3 feedback repairs Aino, Cem and Daniel separately).
- pred-3 revealed only after theory (min 1) is honest, since the sim cannot show the asymmetry.
- Example: seven stages, symbolic first, safe-side rounding to 87 mm, order-of-magnitude check. Mistake values (0,044; 110; 46; 15,3) are real slips; check-2 reads α from a table and verifies it with a second column.
- Exit ticket and check-1 (water below 4 °C) test the core ideas; check-2 on the hole repairs the "metal fills the hole" idea.
- Sim at 390 px: controls and readout fit; text sits behind Käyttöohje/Mallin oletukset.
- Finnish: glossary terms, case after number+unit correct. Workload one lesson.
