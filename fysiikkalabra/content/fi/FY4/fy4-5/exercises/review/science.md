VERDICT: PASS
CONTENT-HASH: 548a782b3164dea2

## Blocking

## Polish
- exercises.json:111 (L3-03) — the key is still 0.061, while the solution concludes 0,06 N. It is within tolerance; 0.06 would match.
- solutions.md:69 (L1-05) — the step "Voimakuvio" shows only T and its components. Rename it, for example to "Kuvio: köyden voima ja komponentit", so it is not taught as a complete force diagram.
- solutions.md `pinta` diagrams — the surface is hatched inside the voimakuvio, but the lesson says surfaces are not drawn. This comes from the tool, not from this set.
- solutions.md:78 (L1-05) — the significant-figure reason "eikä 250 N ole sitä tarkempi" is still shaky (carried over).

## Checked
- Round-1 fix: L3-03 now gives "0,061 N ≈ 0,06 N" and justifies it by decimals in a difference. Correct.
- One script recomputed all twelve answers: 14,715 / 15 / 4,905 / 637,65 / 191,5 / 51,96 / 660,6 / 0,598 / 1,0 / 581,7 / 1,9 / 0,06076. All agree with answers.py and exercises.json.
- Models: the wall's static friction is mg; a lift slowing on the way up has a pointing down, so N < G; the curling stone has no forward force; the ceiling's N points down; the L2-04 pulls add as vectors.
- I rendered all 11 voimakuvio blocks. They use one linear scale, except L1-03 and L3-02, whose separate horizontal scale the rule allows and whose text alternatives say so. Every sum is visible (F = N, F_μ = G; F_noste = G + N), and no force is under 15 %.
- Directions are right: the wall's N points away from the wall; the L2-03 push ends on the body; v and a are drawn off the body; there are no third-law pairs; components are dashed.
- The figures ruutu, malli-pulkka and malli-hissi agree with their tasks.
- Each solution goes diagram, axes, symbolic answer, numbers, then a real reasonableness check. Everything is within FY4's scope.
- "FAIL sims" does not reproduce. The hash was the same at start and end.
