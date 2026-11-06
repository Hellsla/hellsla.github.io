VERDICT: PASS
CONTENT-HASH: 58b13b3e6286c0a5

Round 1 (new task fy7-5-L1-09, ordering; rest of set PASS before)

## Blocking
(none)

## Polish
- exercises.json:92 — five situations each needing a calculation is heavy for level 1 ("one formula or one step"); it reads like level 2. Cut to four situations (drop B or E) or state that the situation is a Level 2 task in the bank plan; do not change ids. Without B the mistakes "forgetting N" and "flux size" are still caught.
- exercises.json:98 — "yhden kierroksen vuo tarkoittaa käämin yhden kierroksen läpi kulkevaa magneettivuota" is circular; write "Vuo on aina yhden kierroksen läpi kulkeva vuo."
- solutions.md:196 — the long closing paragraph mixes three explanations; put each wrong-order cause on its own line.
- Tilanne D has no coil; the stem "joissa voi syntyä induktiojännite" fits C poorly (none arises); say "joissa voisi syntyä".

## Checked
- All five values recomputed: A 1,2 V, B 3,0 V, C 0, D 0,60 V, E 2,0 V; order C, D, A, E, B, direction "pienimmästä suurimpaan" stated in the prompt.
- Distractors catch the chapter's warned mistakes: large flux but no change (C), forgetting N (A, B move), N = 1 loop (E) and flux rate vs size.
- Correct order is not obvious from form: the rate (E) and the turns (B) cross, D is the only e = vBl case.
- Within the chapter (induction law, e = vBl); solution complete step by step; units mWb handled.
- Checked from text only (no renders; pedagogy role); inline formulas measured as KaTeX renders at 390 px: e_A 214 px, e_D 227 px, e_E 164 px, all fit.
