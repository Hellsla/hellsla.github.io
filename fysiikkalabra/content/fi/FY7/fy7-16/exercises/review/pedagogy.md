VERDICT: PASS
CONTENT-HASH: 17151a3c70a4f503

Scope: new task fy7-16-L2-08 (suuruusluokka, YO type 5).

## Blocking
(none)

## Polish
- exercises.json (choices) — option values are 12 us, 1,2 ms, 12 ms, 12 s: the last gap is a factor 1000, outside the "10-100 apart" rule in docs/exercise-types.md; replace 12 s by 120 ms (and a matching unit-slip feedback).
- exercises.json (12 s feedback) — "valon nopeudeksi on otettu 300 000" is hard to reach since the task gives c in m/s; use a slip a student can make with the given data.

## Checked
- Calculation verified: v = 2,04 x 10^8 m/s, s = 2,4 x 10^6 m, t = 11,8 ms; each wrong value follows from a named unit slip.
- Forgetting n (8 ms) or the return trip (6 ms) lands near 12 ms, so the order of magnitude is robust; no distractor depends on that.
- Correct option is not the longest or only hedged one; digits "12" repeat in three options, which hides it.
- Within fy7-12 (t = ns/c) and earlier units; everyday context (ping).
- Widest display chain 174 px, inline 187 px (render).
