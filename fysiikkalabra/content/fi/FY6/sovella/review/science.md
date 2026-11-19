VERDICT: PASS
CONTENT-HASH: 78dc8c2332232d74

## Blocking

## Polish
- lessons/FY6/sovella/answers.py — the new drift rate $0{,}005\,\text{V/min}$ (s1 d solution) is the one solution number answers.py does not compute — add `"fy6-s1-d-drift": 0.03 / 6`.
- solutions.md fy6-s3 c **Kysytty** still says "on paljon pienempi kuin b-kohdan tulos"; harmless behind the button, but it could follow the new task wording ("poikkeaa").

## Checked
- One script recomputed every number from the task data: s1 fit (−1,194 V/A, 4,598 V, max residual 0,020 V), E 4,60 V, R_s 1,2 Ω, I 0,50 A, P 2,0 W, share 13 %, scatter 0,08 Ω, drift 0,06 Ω; s2 2,5 A, 16,7 W (30 W balance), 1,76 A/10,6 V/18,7 W/2,5 W, 4,29 A/8,6 V/15 W; s3 1,8e-7 N, mg 2,2 %, E/E_b 0,10, 13,4 m/s, 5,0e-9 J/14 %/3,1e-8 J, 3,2e-9 N (1,8 %, 0,82 mg); s4 14,85 J, 6,86 J/46 % vs 27 %, 26,4 A, 6,9 kW, 0,30 A. All agree with tasks.json and answers.py.
- s1 drift: definition (slow change of U with time at unchanged current) is right and matches the task text; rate 0,03 V over six ~1 min readings ≈ 0,005 V/min is consistent, and the worst-case last point ~0,03 V low → slope ≤ 0,06 Ω follows from it.
- s1 idealisation: model $U = E - R_\text{s} I$ assumes E and R_s constant; discharge lowers E (steeper line, R_s high), warming usually lowers R_s (direction uncertain) — correct, and the error_sources detail now states it.
- s2 b without "todellisuudessa": still asks the power at the real lamp voltage; answer 16,7 W and rubric (loop rule, 10,0 V) unchanged and consistent.
- s3 b "Kerro oletuksesi": only the no-drag, no-weight energy model is computable from the data, so the expected 13 m/s is unique; the new rubric clause asks for exactly that assumption; a) already justifies dropping weight.
- s3 c "poikkeaa" no longer gives away the direction; criteria (drag, 14 %, energy to air, b as upper limit) still match.
- s4 b reworded: the relative-voltage comparison (27 %) is now asked, and the reasonableness criterion asks exactly that; no answer revealed.
- Energy wording: "ilman sisäenergia kasvaa ja siirtyy lämpönä" follows P1; scope inside FY6; points per part sum to the criteria.
