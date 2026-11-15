VERDICT: PASS
CONTENT-HASH: d1b9b62898b7d7d3
Mode: full, round 1 (hash identical at start and end)

## Blocking
- none

## Polish
- exercises.json:157 (L2-05) — the 435.7 nm line is called violet, while L2-09 calls the same mercury line (436 nm) blue and L3-06 uses violet for 405 nm — call it blue in L2-05 too.
- solutions.md:321 (L3-06, Reading the graph and Answer) — "subtracting two nearly equal energies" does not describe 3.06 eV and 2.27 eV; the two figures follow from the reading uncertainty (±2 nm per line gives about ±0.02 eV in the difference) — give that as the reason.
- solutions.md:231 (L2-07, Principle) — the measuring range 577.0 nm − 404.7 nm is 172.3 nm, written as 173 nm — write 172 nm.
- solutions.md:273 (L3-04, Reasonableness) — "over 780 nm, that is, infrared" while L2-08 and the figures end the visible range at 720 nm and the lesson uses 750 nm — use one limit.
- solutions.md:188 (L1-07) — the model answer requires the nuclear charge and the number of electrons as the reason; the task asks for it, but the lesson only says that every element has its own states — accept the answer without it or keep it as an extension, not a requirement.

## Checked
- All 19 numeric answers recomputed in one script with own formulas from the task texts (h = 6.626e-34 J s, c = 2.998e8 m/s, 1 eV = 1.602e-19 J): each agrees with exercises.json, answers.py and the intermediate values of its solution, and a correctly rounded answer is inside its tolerance.
- L2-07: own least-squares fit gives k = 12.0095 nm/mm, b = 299.65 nm, residuals at most 0.76 nm, λ(16.4 mm) = 496.6 nm; two-point interpolation 496.4 nm.
- L3-04: brute-force search over level systems finds exactly two that fit the five lines (1.10/2.40/3.90 eV and its mirror 1.50/2.80/3.90 eV); the task's condition (missing line = lowest excited state to ground) selects the first, so 1127 nm is unique.
- L3-05: shares 18.9 %, 22.1 %, 15.1 %; part d) 477 nm. L2-08: 496, 413, 282 nm from the ground state, 653 nm from state 2; exactly one option is right, and each wrong spectrum carries the one error its feedback names (figure code read).
- L2-05, L2-06, L3-06: line data agree with real spectra (Hg 404.7/435.8/546.1/577.0 nm; Ca II 393.4, Mg 518.4, Na 589.0 nm; Hg 6³P₀ and 6³P₂ 0.794 eV apart) and are marked example data.
- Choice tasks L1-06, L1-08: one correct option, distractors wrong, feedback physically right; "cooler gas than the source" stated.
- Conditions stated in the tasks: one photon out per photon in (L3-05), no internal energy (L3-03), atoms in the ground state (L2-03, L2-08), high levels at about zero energy (L3-01).
- Solutions: symbolic form before substitution, eV–J conversions shown, signs right (L2-06 −0.85 eV), rounding reasons name the limiting datum.
- Scope: only hf = E_u − E_l, c = fλ and given level energies; nothing beyond FY8.
- The packet's exercise brief was empty and it states check_lesson.py had not been run.
