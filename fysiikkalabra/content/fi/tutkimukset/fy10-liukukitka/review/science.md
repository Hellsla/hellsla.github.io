VERDICT: PASS
CONTENT-HASH: 43e1c4e36cbb8f96

## Blocking
None.

## Polish
None.

## Checked (delta 2026-11-15)
- Every changed sentence read in context. investigation.json `why` (fy4-6), the *Teoriaa lyhyesti* paragraph, the force-diagram aria-label in investigation.md and figures.py (they match): "liukukitka $F_\mu = \mu N$" fits the situation. The brake slides on the track, so this is sliding (kinetic) friction. The force opposes the motion, and the vehicle decelerates with $a = \mu g$ on a level track. That agrees with the P8 terms in docs/physics-guardrails.md (Friction).
- Two later edits remove the doubled terms the rename left. Line 48 now reads "...jarrun ja radan välinen liukukitkakerroin epävarmuuksineen". Line 83 now reads "missä $\mu$ on liukukitkakerroin." Both remove only a repeated name, and the physics is unchanged. $\mu$ is still defined once, as dimensionless, with the model's assumption (the brake carries the whole weight) still stated.
- No "liikekitka" or "liikekitkakerroin" is left in investigation.json, investigation.md, teacher.md or figures.py. teacher.md uses only "kitkavoima" and "kitkakerroin", which stay consistent with the new terms.
- The investigation never brings in static friction ("lepokitka" or "lähtökitka"). That is right: the cart slides from the first moment of measurement. So nothing had to be named "täysin kehittynyt lepokitka eli lähtökitka", and nothing contradicts that term.
- The content hash is `43e1c4e36cbb8f96`, checked again at the end.
