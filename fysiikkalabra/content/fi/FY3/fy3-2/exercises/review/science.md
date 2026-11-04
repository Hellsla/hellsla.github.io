VERDICT: PASS
CONTENT-HASH: 24fb5d210fa3c9a2

Full review of the 20-task set; focus on the 8 new tasks (L1-06..08, L2-05..07, L3-04..05).

## Blocking
- none

## Polish
- exercises/exercises.json:302 (L3-05 b) and solutions.md:194 — the model answer justifies "nostovoima = paino" by "voimien summa on nolla", which is Newton's first law (FY4 per the scope note). — Accept the lesson's own statement ("tasaisella nopeudella nostovoima on yhtä suuri kuin paino") as the reason, or say the sum-of-forces argument comes in FY4.
- exercises/solutions.md:152 (L2-05, Vastaus) — the sig-fig reason ("kolme numeroa mutta viimeinen epävarma") is not a rule; the limiting data are $\Delta s = 1{,}0\,\text{m}$ and $6{,}0\,\text{N}$. — Cite those.
- exercises/solutions.md:178 (L3-04, Periaate) — "Energia säilyy: jousen venyttämiseen tehty työ voidaan käyttää nostamiseen" needs its condition. — Add "häviöittä" (the task itself only asks for an equal amount of work).
- exercises/exercises.json:75 (L1-07) — v = P/F with kN and kW conversions is a rearrangement plus conversion, level-2 by this set's own answers.py comment. — Acceptable at level 1; or give W and N.
- docs/exercise-bank/FY3.md:15,17 — plan items "työn merkki" (L1), "liike-energian muutos" (L2) and "kulman unohtaminen vinossa vedossa" (L3) are not in the set; the last two are FY4 (E_k, cos α), so leaving them out is right. — Update the plan lines.

## Checked
- All six new numeric answers recomputed independently (own models, least-squares fits through origin): L1-07 1,5 m/s; L2-05 55,3 J; L2-06 229,8 W; L2-07 588,6 J; L3-04 F/s = 1,001 N/cm, W = 0,500 J, h = 25,5 cm; L3-05 v = 0,815 m/s, P = 3,60 kW, Pt = mgh = 53,0 kJ. All inside tolerance; answers.py lines right.
- L2-05 bounds 24–72 J valid (F decreases monotonically); L3-04 trapezoid sum from origin 0,500 J as stated.
- L2-06: time range 7,8–8,4 s → 222–239 W as stated; assumption "only lifting the weight" stated in task; mean reduces random error (guardrail wording).
- Origin lines justified physically in L3-04 (free length) and L3-05 (time from start of lift); slope from fitted line, not raw neighbours.
- L1-06, L1-08: exactly one correct option, every distractor really wrong with correct feedback.
- L2-07 error task: mass used as force, correct W = mgh = 590 J; no duplicate of existing tasks; all in FY3 scope.
