VERDICT: PASS
CONTENT-HASH: ca2d81baf5a67f35
Round: 3
Mode: delta

Round 2. Delta review of the round-1 Polish fixes (HEAD~2..HEAD~1) on the 20-task set; focus on the 8 new tasks.

## Blocking
- none

## Polish
- exercises/exercises.json:75 (L1-07) — v = P/F with kN and kW is a rearrangement plus conversion, level 2 by this set's own answers.py comment (carried from round 1). — Acceptable at level 1; or give W and N.
- docs/exercise-bank/FY3.md:15 — Taso 1 still lists "työn merkki", which no task asks. — Drop it from the plan or add a sign item later.
- exercises/exercises.json:298 (L3-05) — "graph" was dropped from `kind`, but a) asks for a fitted line through the origin and the solution has a "Kuvaajan lukeminen" step. — Keep "graph", or call the step a table reading.

## Checked
- L3-05 b): reason is now the lesson's own statement (constant speed → lifting force equals weight, as in the W = mgh derivation); no Newton's-law argument left, so the set stays within FY3.
- L3-05 d) recomputed: least-squares slope through origin 0,815 m/s, P = 3598 W → 3,6 kW; P·8,0 s = 28,78 kJ vs mgh = 4414,5 N · 6,5 m = 28,69 kJ, difference 0,3 % as stated ("alle prosentin").
- L2-05: sig-fig reason now cites Δs = 1,0 m and 6,0 N; aligned trapezoid sum 17,6 + 16,15 + 13,05 + 8,5 = 55,3 J → 55 J.
- L3-04: "häviöittä" added to the energy statement; W = 0,500 J, h = 25,48 cm → 25 cm.
- L2-06 aligned block: mean 8,1 s, h = 3,06 m, W = 1861,2 J, P = 229,8 W; unchanged results.
- L2-07: new model answer names the error (mass 40 used as a force) and gives W = mgh ≈ 590 J (588,6 J).
- L1-06, L1-08: options reordered/reworded only; exactly one correct option, `answer` matches it, distractors still wrong with right feedback; L1-08 note that 500 kg and the height do not affect the comparison is correct.
- Plan lines 16-17 updated: kinetic energy and the oblique pull left out as FY4, P = Fv lift task named.
- Hash checked at start and end: unchanged.

## Checked in round 3
- Delta (HEAD): split aligned rows in solutions.md re-derived against the previous rows. Each "... \\ &= result" is the old row cut at its last "="; all numbers, units, symbols and values identical (mechanical check: old and new rows equal once \\, & and = are removed), and the results still follow from the inputs. No physics or answer changed.
