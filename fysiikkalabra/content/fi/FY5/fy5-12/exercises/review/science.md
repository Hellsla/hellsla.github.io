VERDICT: PASS
CONTENT-HASH: 8a3bb847f1c530b5
SCOPE: delta wording (Työjono 18 oikoluku P1), round 1

## Blocking

## Polish
- content/fi/FY5/fy5-12/exercises/solutions.md (L2-10, Sijoitus and Vastaus) — the earlier Polish still applies: "1,20 m" has three significant figures, but the sentence says the results have two, as λ = 0,80 m has. This is outside the diff. — Write 1,2 m.

## Checked
- The hash was 8a3bb847f1c530b5 at the start and at the end.
- solutions.md:157 (L2-06): "ei muutu solmuviivoilla sisäenergiaksi" is correct physics and fits the guardrail. Heat is energy in transfer, so energy cannot "turn into heat". The claim says interference itself does not dissipate energy. That is true: the energy is redistributed and none is lost at the nodal lines. The rest of the model answer still agrees with the brief's Kaava section.
- Every other hunk only splits a paragraph (L1-03, L1-05, L2-01, L2-04, L2-07, L2-08, L2-10 a and d). No number, symbol or claim changed. The split text reads in the same order and keeps its meaning.
- The deterministic checks (lint, build, latex) are green, so the blank lines inside the fields do not break the rendering.
