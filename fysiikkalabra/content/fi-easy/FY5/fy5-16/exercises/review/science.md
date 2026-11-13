VERDICT: FAIL
CONTENT-HASH: 18ea4ac4cccb0ca2

## Blocking
- content/fi-easy/FY5/fy5-16/exercises/solutions.md:246 and :257 — B: "alueella, jossa kuulo vaurioituu" says any exposure at 90 or 105 dB damages hearing; it holds only for long enough exposure, which is what the task computes. The passed Finnish says "kuulovaurion vaara -alue", and the figure says "pitkä altistus ... vaurioittaa kuuloa" — write "alueella, jossa on kuulovaurion vaara" (or "jossa pitkä altistus vaurioittaa kuuloa") in both lines.

## Polish
- none.

## Checked
- Delta round 1, fi-easy: added fy5-16-L1-09 and L2-09 only.
- Compared by script with the passed Finnish set: answer, unit, tolerance, figure identical; same numbers in text and solution; only the wording above differs in meaning.
- Recomputed: t = 8 h / 2^((L − 85 dB)/3 dB): 90 dB -> 2,52 h; 105 dB -> 480 min / 101,6 = 4,72 min. answers.py agrees; tolerance 2 % covers 2,5 h and 4,7 min.
- Figure fy5-16/scale-tehtava: levels written at the markers (90, 105 dB) match the tasks; description matches.
- Equal-energy 3 dB rule and rounding to two figures justified as in the Finnish; reasonableness checks (between 88 and 91 dB; 1/100 of 480 min) correct.
- Hash same at start and end.
