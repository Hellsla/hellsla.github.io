VERDICT: PASS
CONTENT-HASH: 66c250ebde3dc328
Mode: delta (round 1; the diff since 5318e9526d309a04)

## Blocking
- none

## Polish
- content/en/FY8/fy8-7/inquiry.json:403 — the prompt now says the energy difference "stays in the fibre as internal energy" and then asks "how much heat is produced in the fibre per second"; hints (410), mistake feedback (419) and the solution's Asked, Principle, Reasonableness (422) keep "heat produced" — for one wording everywhere, ask e.g. "by how much does the internal energy of the fibre grow per second at least" (level C as it stands: no wrong picture, the quantity asked is unambiguous).

## Checked
- The diff is two wording changes ("as heat" -> "as internal energy"; "the beam and heat" -> "the beam and the internal energy of the fibre"); both agree with the guardrail "a body has internal energy, not heat".
- No number, symbol, unit, answer, tolerance, hint or mistake value changed.
- Recomputed the task from its text: P_heat = P_L(lambda_L/lambda_p - 1) = 1000 W * (1070/976 - 1) = 96.31 W; answer 96.3 W, shown 96 W (two figures from 1.0 kW) inside the 2 % tolerance.
- Mistake values: 1000(1 - 976/1070) = 87.9 W and pump power 1096.3 W, as the feedback says.
- Reasonableness check: photon energies 1.270 eV and 1.159 eV, difference 9.6 % of the laser photon's energy, consistent with "about a tenth of the beam power".
- Energy balance and the "at least" condition (one laser photon per pump photon) still stated in prompt and solution; the model's limit (real fibres give more heating) still said.
- lesson.md: teacher-approved figures only, not judged (category teacher-figure).
- Hash identical at the start and the end.
