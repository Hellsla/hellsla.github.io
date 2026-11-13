VERDICT: PASS
CONTENT-HASH: 1eceddd9c27ef416

## Blocking
- none

## Polish
- solutions.md (L1-10 Answer line) — the reason for three significant figures (the mean distance is not the exact path) is physical, while the lesson's rule is "as few significant figures as the least precise datum", and both data have four. A student may see a conflict. Fix, optional: add "(the lesson's rule would allow four, but the mean distance is only an approximation)".

## Checked
- exercises.json fy1-2-L1-10: answer 1.28 s equals 3.844e8 / 2.998e8 = 1.2822 rounded to three significant figures; unit s unchanged.
- Tolerance 0.04 (about 3 %) still sits inside the stated 4 % and accepts both 1.28 and the earlier 1.282.
- solutions.md L1-10: substitution shows 1.282 s, then 1.28 s; the km to m conversion is explained before it; the answer line and the 4 % note agree with the JSON.
- The reasonableness check (a little over a second) agrees with 1.28 s.
- answers.py: round(384400e3/2.998e8, 2) gives 1.28, consistent with exercises.json.
- The task text is unchanged: situation, lookup, hint, question last. The rest of the set is unchanged since the earlier pass.
- The packet contained no SCOPE line, so none is written.
