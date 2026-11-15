VERDICT: PASS
CONTENT-HASH: d1b9b62898b7d7d3
Mode: full, round 1 (hash identical at start and end)

## Blocking
- none

## Polish
- exercises.json:157 (L2-05) — the 435.7 nm line is called violet; L2-09 calls the same mercury line blue and L3-06 uses violet for 405 nm — call it blue.
- solutions.md:321 (L3-06) — "subtracting two nearly equal energies" does not describe 3.06 eV and 2.27 eV; the two figures follow from the reading uncertainty (±2 nm per line, about ±0.02 eV) — give that reason.
- solutions.md:231 (L2-07) — the range 577.0 nm − 404.7 nm is 172.3 nm, written 173 nm — write 172 nm.
- solutions.md:273 (L3-04) — "over 780 nm, that is, infrared", while L2-08 ends the visible range at 720 nm and the lesson at 750 nm — use one limit.
- solutions.md:188 (L1-07) — the model answer requires nuclear charge and electron number, which the lesson does not teach — treat it as an extension, not a requirement.

## Checked
- All 19 numeric answers recomputed in one script with own formulas from the task texts: each agrees with exercises.json, answers.py and its solution's intermediate values; a correctly rounded answer is inside its tolerance.
- L2-07: own least-squares fit k = 12.0095 nm/mm, b = 299.65 nm, residuals at most 0.76 nm, 496.6 nm at 16.4 mm.
- L3-04: a search over level systems finds two that fit the five lines (1.10/2.40/3.90 eV and its mirror); the task's condition selects the first, so 1127 nm is unique.
- L3-05: shares 18.9 %, 22.1 %, 15.1 %; part d) 477 nm.
- L2-08: 496, 413, 282 nm from the ground state, 653 nm from state 2; one option right, each wrong spectrum has the one error its feedback names (figure code read).
- L2-05, L2-06, L3-06: line data agree with real spectra and are marked example data.
- L1-06, L1-08: one correct option, distractors wrong, feedback right.
- Assumptions stated in the tasks (one photon out per photon in, no internal energy, atoms in the ground state, high levels near zero).
- Solutions: symbolic form first, eV–J conversions shown, signs right, rounding by the limiting datum; scope within FY8.
- The packet's exercise brief was empty; check_lesson.py had not been run.
