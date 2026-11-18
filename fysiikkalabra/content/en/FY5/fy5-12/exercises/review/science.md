VERDICT: PASS
CONTENT-HASH: c1008c5486383ca4

## Blocking

## Polish
- none.

## Checked
- Word diff of the whole delta (removed vs added text, whitespace-normalised): the only changed word is "heat" -> "internal energy" in the energy-claim model answer (solutions.md:177); everything else is paragraph splits with no changed word, number or formula.
- The new sentence is physically right and follows the guardrail: heat is an energy transfer, not a form energy turns into; "does not turn into internal energy on nodal lines" states the correct mechanism (no dissipation caused by interference, energy redistributed to constructive points, source power unchanged).
- The English now matches the Finnish ("ei muutu solmuviivoilla sisäenergiaksi").
- No numbers or answers changed, so answers.py and the earlier recomputations (L2-10: lambda = 0.80 m, destructive 0.40 m and 1.20 m) stand.
- Hash unchanged at start and end of the review.
