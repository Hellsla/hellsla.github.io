VERDICT: PASS
CONTENT-HASH: a3a64a7608c7dd0a

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking

## Polish
- solutions.md fy3-5-L2-03 — "800 J = 0,8 kJ … yksi merkitsevä numero" while the answer is 800 J; "0,8 kJ (sadan joulen tarkkuudella)" says the same more cleanly.
- fy3-5-L1-05 — the escaping air also gains kinetic energy (the jet). This is fine at this level (C), but "kun ilma on pysähtynyt" would make ΔU = Q + W exact.

## Checked
- Round-1 B, exercises.json fy3-5-L3-01: the task now says "ja ilmaa voi pitää ideaalikaasuna". This matches the solution's reasoning (constant T and an ideal gas give ΔU = 0, so Q = −W = −18 J) and the wording of L3-03. Resolved.
- The answer (−18 J), the unit, the tolerance and answers.py are unchanged and still correct. The added clause is grammatical.
- The diff touches no other exercise. All twelve answers were recomputed in the full review at the previous hash: 570 J, −8,4 kJ, 250 J, −500 J, −70 J, −15 J, 160 kJ, 800 J, 40 s, −18 J, 1,7 m, 310 J.
