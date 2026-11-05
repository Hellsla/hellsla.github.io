VERDICT: PASS
CONTENT-HASH: d62b2b53d0757222

## Blocking

## Polish

## Checked
- Round-3 Polish resolved: L2-07 now uses 109 dB, so it no longer repeats the inquiry's 103 dB → 7,5 min. The coordinator confirmed that the inquiry has no 109, 1,875 or 1,9, and that the "109" hits in lesson.md are SVG path coordinates. In the exercise set, 109 dB occurs only in L2-07 (task and solution).
- L2-07 recomputed: n = (109 − 85)/3 = 8; t_sall = 480 min / 256 = 1,875 min ≈ 1,9 min. The student's answer is 8 h : 8 = 1,0 h = 60 min exactly, so the earlier mismatch between 1,3 h and 80 min is gone.
- answers.py round(t_allowed(109)·60, 1) = 1,9; exercises.json has 1.9 min with tolerance 0.02. An unrounded 1,875 is off by 1,3 % and is still accepted. Two significant figures fit the data.
- Solution: the unknown is solved symbolically before substitution, the conversion 8 h = 480 min is right, and 2⁸ = 256 is right. a) names the error correctly: dividing by n instead of 2ⁿ.
- Round-5 wording: Vastaus a) "jaetaan kahdella kahdeksan kertaa eli kaikkiaan luvulla 256" is right (2⁸ = 256). In the Järkevyys, 60 min / 1,875 min = 32 is exact; three halvings take 8 h to 1 h and five more take 60 min to 60/32 = 1,875 min, eight in all. Under t₀/n each extra step really shortens the time less. The inquiry's 7,5 min is no longer printed even as an intermediate value.
- "opiskelija" is used throughout; the task text and the solution agree (24 dB, 8 steps, 1,0 h).
- The rest of the set is unchanged since round 3: the other 15 numeric answers recomputed in round 3 still match answers.py and exercises.json.
- The known eq-chain collapse on main is not counted as a finding.
