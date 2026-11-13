VERDICT: PASS
CONTENT-HASH: 077bbc73147433b4
SCOPE: delta added-exercise from de998fe1e15345d2 base 81db4a6fd727

## Blocking
- none

## Polish
- solutions.md fy1-8-L1-10 — the rounding up to 1,4 km is correctly argued (a minimum distance); one could add that 0,2 s has only one significant figure, which is why the result is a design estimate rather than a 3-s.f. answer — optional sentence.

## Checked
- fy1-8-L1-10: relative uncertainty Δt/t ≤ ε_max gives t ≥ Δt/ε_max = 4,0 s, then s = v t for sound at constant speed; solved in symbols first.
- Terms follow the guardrails: "ajanoton epävarmuus" and "suhteellinen epävarmuus", hand timing about 0,2 s as in docs/physics-guardrails.md.
- MAFY speed of sound in air at 20 °C, 343,4 m/s, is right.
- Recomputed independently: 343,4 · 4,0 = 1373,6 m = 1,3736 km; answers.py and exercises.json agree; unit km as asked.
- 1,4 km and 1,37 km both within the 4 % tolerance; rounding up keeps the 5 % limit met.
- Back-check 0,2 s / 4,0 s = 5 % is a real check. Same numbers, answer, unit and tolerance as the Finnish original.
