VERDICT: PASS
CONTENT-HASH: 5bf5cc74045e4797

## Blocking

## Polish
- content/fi/FY4/fy4-1/exercises/solutions.md:206 (L3-04) — "kaksi merkitsevää numeroa kuten mittanauhan arvoissa": the tape values 2,00 m and 1,60 m have three figures; the limit is the fitted slope v_ohj ≈ 0,64 m/s — write "kaksi merkitsevää numeroa kuten sovituksesta luetussa nopeudessa 0,64 m/s".
- content/fi/FY4/fy4-1/exercises/solutions.md:152 (L2-05) — the line is said to pass near (5,0 s; 3,54 m), but the least-squares line gives 3,52 m (x₀ 0,488 m, v 0,605 m/s). The answer 0,61 m/s holds either way; to be safe, read (5,0 s; 3,52 m) and keep v ≈ 0,61 m/s.
- solutions.md L2-05 Vastaus — "kaksi merkitsevää numeroa, koska taulukon paikat ovat kahden desimaalin tarkkuudella" does not explain why there are two figures. Say that reading the line limits it to about ±0,01 m/s.
- exercises.json fy4-1-L2-06 — the plan (docs/exercise-bank/FY4.md) asks for a two-body (t,x) graph *figure*, but the task gives a table. The task is good as it is; either note the deviation in the plan or add the figure later.
- exercises.json fy4-1-L1-06, option 4 ("taaksepäin ajassa") — this distractor is implausible and tests nothing. A better one would be "kappale on origon negatiivisella puolella", which mixes up the sign of the position with the direction of motion.

## Checked
- All 20 answers recomputed in one script with my own fits: L2-05 0,605 → 0,61 m/s; L2-06 vA 1,50, vB −1,79, t 5,78 s → 5,8 s; L2-07 −1,5 m/s; L3-04 v_ohj 0,642, k 1,25, v 0,803 → 0,80 m/s, t(6,0 m) 6,99 s; L3-05 vR 9,88 m/s, x0 203,2 m, t 54,1 s, x 738 m → 740 m. The tolerances (2–4 %) cover how the line is read.
- L3-04 physics: a metre stick nearer the camera makes the program's scale too small, so every length is too short. This agrees with the tape reading 1,60 m. The systematic and random error are described correctly (guardrail: repeating does not remove the systematic error), and the extrapolation is given as 40 % beyond the data with its conditions stated.
- L3-05: the extrapolation of 14 s past the data is stated and its assumption named. The sensitivity check (+0,2 m/s gives ≈ 3 % longer) is right (3,4 %).
- L2-06: "faster" is judged by speed (|vB| > |vA|). The guardrail rule that a higher line does not mean "ahead" is not broken.
- MC L1-06..08: exactly one option is correct, every distractor is really wrong and its feedback says why.
- Scope: everything stays inside uniform 1-D motion, the fit and the scale error. No new task uses a vector symbol, so the \overline rule does not apply. No figures with arrows.
- Each solution is symbolic first and has a real check. No duplicate of L1-01..L3-03. The levels fit (data tasks at level 2; modelling and error at level 3).
- Plan +3/+3/+2 met; 8/7/5 = 20.
- The hash was identical at the start and the end.
