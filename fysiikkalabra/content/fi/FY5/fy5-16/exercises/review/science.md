VERDICT: PASS
CONTENT-HASH: 2323b719e4b31e3d

## Blocking

## Polish
- exercises/exercises.json:240 — fy5-16-L2-07: the brief's lesson text (Kaava, Esimerkki, Tiivistelmä) and the other tasks do not print 103 dB, 1,3 h or 7,5 min. But a plain-text search shows the strings "103\,\text{dB}" (6 hits) and "7{,}5\,\text{min}" (2 hits) in fy5-16/inquiry.json, which this role may not open. If the inquiry already works out 103 dB → 7,5 min, b) can be read off there — change to a level that neither the lesson nor the inquiry uses. For example, 109 dB gives n = 8: the student gets 8 h : 8 = 1,0 h and the correct value is 8 h / 2⁸ ≈ 1,9 min. Check it first, though: "109" occurs twice in lesson.md. Update the solution and answers.py to match. If the hit is a different calculation, no change is needed.

## Checked
- L2-07 recomputed: n = (103 − 85)/3 = 6; t_sall = 8 h / 64 = 0,125 h = 7,5 min; the student's 8 h : 6 = 1,33 h ≈ 1,3 h = 80 min. answers.py t_allowed(103)·60 = 7,5, answer 7.5 min with tolerance 0.02 matches. The halving chain 8 h → … → 7,5 min has six steps.
- L2-07 a): the error (dividing by n instead of 2ⁿ) is named correctly. The Järkevyys holds: 80 min / 7,5 min ≈ 10,7, so "yli kymmenkertainen" is right, and under t₀/n each extra step really shortens the time less (by 8 h/(n(n+1))). "opiskelija" is used throughout the task and the solution.
- 103 dB, 1,3 h and 7,5 min occur in no other task or solution in the set. The old duplicate (100 dB → 15 min from the Esimerkki and L3-05) is gone.
- Round-2 Polish done: L2-07 moved to 103 dB, the Järkevyys reworded into a real check, and docs/exercise-bank/FY5.md:100 now says "sallittu altistusaika jaettu luvulla n eikä luvulla 2ⁿ".
- The rest is unchanged since round 2. Recomputed in one script: L1-01 2,0 h; L1-02 73; L1-03 82; L1-04 83; L1-07 27; L2-01 4,0 h; L2-02 150 %; L2-03 16 m; L2-04 0,90 s; L2-05 60,3 %; L2-06 11,8 dB; L3-01 125 %; L3-02 46 dB; L3-04 5,26 dB; L3-05 1,59 h. All match answers.py and exercises.json.
- The known eq-chain collapse on main is not counted as a finding.
