VERDICT: PASS
CONTENT-HASH: 58ca1c36704e1ad3
Mode: full
Round: 1

## Blocking

## Fixed
- exercises.json L3-03 unit "kertaa" -> "times" (Finnish word left in the English set; check_i18n still 0 errors).

## Polish

## Checked
- Scripted comparison of all 20 exercises against the reviewed Finnish: ids, levels, kinds, answers, units (except the translated unit), tolerances, correct flags and every number in texts, choices, feedback and data tables are equal (decimal comma normalised to point).
- Same comparison on solutions.md (193 lines each): all numbers and formulas equal; the only reordering is "Radan 3 ionin" / "path 3" in the L2-05 reasonableness line (text order, not a value).
- New tasks L1-06..08, L2-05..07, L3-04..05: physics reads the same as the Finnish: qvB as centripetal force, B = mv : (qr) = 0.43 mT, T = 2πm : (qB) = 1.8 ns, m : q = rB : v = 1.0e-8 kg/C, d = 2r so m is proportional to d (25.1 u, 25.9 u, 78.9 %), r^2 = 2mU : (qB^2) giving 22.8 u (sodium-23), cyclotron 1.92e7 m/s, 3.07e-13 J, 32 crossings, 16 revolutions, 1.05 us, v : c = 0.064.
- L1-06 and L2-07 choices: only the correct flag is on the same option as in Finnish; each distractor feedback names the misconception correctly.
- No Finnish left in exercises.json or solutions.md (grep for ä, ö and Finnish unit words).
- check_i18n.py en: 0 errors.

## Follow-up (58ca1c36704e1ad3: four solutions.md edits on top of the hash above)
- L1-02 Annettu: ${|q| = e = 1.602 \cdot 10^{-19}\,\text{C}}$ is the right elementary charge, given as a magnitude, so the electron's negative sign is no longer hidden. The outer braces only group.
- L1-02 Kaava: $|q|vB = mv^2/r$, $r = mv/(|q|B)$ is the correct magnitude form, matching the lesson's $|q|$ notation. Recomputed $r = 7.581$ mm → 7.6 mm, unchanged; answers.py and exercises.json untouched.
- L2-03 and L3-02 chapter references (*Uniform electric field*, *Moving in a circle: period and speed*) match the current titles of fy6-11 and fy5-3; the physics is unchanged.
- Polish (not from this diff): exercises.json L1-02 still gives the electron's charge without a sign; match the solution: "charge $1.602…$" → "charge of magnitude $1.602…$".
- Hash at start and end: 58ca1c36704e1ad3.
