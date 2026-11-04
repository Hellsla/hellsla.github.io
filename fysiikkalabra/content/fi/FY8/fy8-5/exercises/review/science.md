VERDICT: PASS
CONTENT-HASH: 60d9e9328cf45092
Round: 3. Re-review: the only change since the PASS is the boxed value moved to the start of the first answer-step line (answers_shown).

## Blocking

## Polish
- solutions.md fy8-5-L1-07 Mallivastaus — "Sumenemisselitys ei kelpaa …" rebuts the fan-blade option that round 2 removed; the new distractor (pilvi osoittaa tarkan paikan, muut pisteet kohinaa) is not addressed. — Replace the sentence with "Pilvi ei osoita yhtä tarkkaa paikkaa, eivätkä muut pisteet ole kohinaa: jokainen piste on yhtä pätevä mittaustulos."
- exercises.json fy8-5-L3-05 — the stem now says "siirtyy perustilasta ylemmälle tilalle" and c) repeats "Siirtymä on 3s → 3p" and then the same transition again. — Drop "Siirtymä on 3s → 3p." from c).
- figure fy8-5/string (L2-06) — carried over: the node-count labels stay in the figure; a) no longer asks for them, so this is now harmless. Optional: remove the labels so that c) still makes the student count nodes.

## Checked
- Round-1 polish applied: L3-05 b) now gives the screening reason; L3-04 calls the end-point slope a check of the fitted 13,62 eV and "kuorille" is fixed; L2-06 b) computes f₁ = 64/1,60 = 40 Hz directly; L3-05 names NIST ASD as source.
- L2-06 rewrite: λ 1,60/0,80/0,533 m, f 40/80/120 Hz; the key 120 Hz is the two-node state; the solution answers a), b), c) in order.
- L1-06, L1-07, L2-07 options reordered: exactly one `correct` each, `answer` equals that option's text, every distractor wrong and its feedback right.
- L2-05 table only changed its decimal sign; 72,25 %, 92,0 %, 0,145 nm unchanged. answers.py unchanged and still equal to the keys.
- Set coherent with the plan in docs/exercise-bank/FY8.md; no duplicates; levels fit. Hash identical at start and end.
- L2-05 answer step now starts "Vastauslaatikkoon $72{,}3\,\%$." It equals 289 : 400 = 72,25 % rounded to 3 s.f., the key 72,25 (tol 0,02) and b); same unit, LaTeX with decimal comma; the line reads well.
