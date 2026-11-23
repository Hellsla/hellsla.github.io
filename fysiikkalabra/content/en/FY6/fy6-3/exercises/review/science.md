VERDICT: PASS
CONTENT-HASH: 665b27fbb36f8dfa
SCOPE: delta md-paragraphs,numbers,typography,wording from 2a633435c63ab47d base 5b3ca4f

## Blocking

## Polish
- solutions.md fy6-3-L2-05 Formula (unchanged line) — "the uncertainty $\Delta R \approx (R_\text{max} - R_\text{min}) : 2$" calls half the range an uncertainty; the guardrail wants it named "a simple estimate of the scatter" — say "estimate of the scatter $\Delta R$".
- solutions.md fy6-3-L2-07 and L3-05 Formula — still written as one inline line with "and", while the rest of the set now uses aligned blocks; style only.
- exercises.json fy6-3-L2-08 — the earlier note ("an example measurement … made with the same circuit" reads as measured) still applies.

## Checked
- Diff only: Formula lines rewritten as aligned blocks starting from the definition $R = U : I$ or $R = \rho l : A$ before the solved form; L2-04's block derives $R_2 = 4R_1$ from $V = Al$ constant correctly; L2-06 $\rho = (R : l)\,A$ from both laws; L2-08 slope $1/R$ on (U, I) axes correct.
- Recomputed in one script with my own formulas: 3.3 V, 10 A, 0.375 A, 1.7 mm², 7.96 Ω, 3.2 Ω, ρ = 1.09 µΩ·m (least-squares slope through the origin 5.47 Ω/m), 3.0 A, 0.30 A, ratio 1.98, 4.93 Ω, 600 Ω, 26 Ω, 38.1 %, 40.0 Ω: all agree.
- answers.py and exercises.json unchanged since the version passed.
- Paragraph splits keep every causal step: lamp's resistance rising with temperature, Ohm's law's constant-temperature condition, diode's falling $U : I$, 0 : 0 undefined at the origin, self-heating as an error source.
- Guardrail fit sentence ("usually not exactly on the same line") kept.
- Hash read at start and end: unchanged.
