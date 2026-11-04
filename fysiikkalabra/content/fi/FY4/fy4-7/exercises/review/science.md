VERDICT: PASS
CONTENT-HASH: 6068178bcd61558b

## Blocking

## Polish
- exercises.json:223 (L2-07) — "Kärryn liike-energia mitattiin … massa unohtui" gives no way E_k could be measured without the mass (in this chapter E_k comes from ½mv² or mgh, both need m) — say how it was determined (e.g. from the braking force and stopping distance measured with a force sensor) or present it as a simulation's output.
- exercises.json:290 (L3-04) — a tennis ball keeps about 53–58 % of its height per bounce (ITF drop test); the data's 73 % is a livelier ball — change to "kumipallo/koripallo" or scale the heights (e.g. 1,50 → 0,84 → 0,47 …).
- exercises.json:74–79 (L1-07) — inverse of L1-04 with a kJ conversion and a rearrangement, which answers.py's own header counts as level 2; kind "reasoning" does not fit a one-formula calculation — keep at level 1 but give the energy in joules, or relabel kind.
- solutions.md:285 (L3-05 c) — the segment losses 284, 363, 354, 596 J are not monotonic in speed, and the path lengths along the slope are not given — add "jos osuudet ovat yhtä pitkiä" and say the trend is only rough.
- Set vs plan (docs/exercise-bank/FY4.md) — L3-04 and L3-05 have the same a–d structure (losses + zero-level part d); the plan's energy-bar-chart figure task (level 2) is missing — update the plan or vary one task.

## Checked
- All 18 numeric answers recomputed independently (one script): json, answers.py and own model agree within tolerance (L2-07 least-squares slope 0,259 → 0,52 kg; L3-04 0,614 J; L3-05 1597 J).
- L2-05 table matches free fall from 1,80 m (h, v within 0,01); E_mek 1,001–1,021 J, mean 1,009 J, spread 1,2 % as stated.
- L2-06: h = −1,5 m, E_p = −1030 J, E_mek = −470 J; student's 1590 J reproduced; scope disclaimer ("määritelmän mukainen") covers buoyancy/water drag.
- L3-04 ratios 0,727/0,734/0,712/0,737, mean 0,728; d) zero-level shift cancels (−0,615 J vs 0,614 J rounding).
- L3-05: E_mek table, conservation check v₅ = 17,8 m/s, loss 19 %, zero level at point 1 gives −1543 J and same difference.
- MC L1-06, L1-08: exactly one correct option, every feedback right; E_k ≥ 0 and E_p < 0 below zero level as in the lesson.
- Scope: only E_k, E_p = mgh, E_mek, zero level; losses named as internal energy (guardrail: friction creates no energy).
- Levels 8/7/5; solutions complete, symbolic first, rounding justified.
