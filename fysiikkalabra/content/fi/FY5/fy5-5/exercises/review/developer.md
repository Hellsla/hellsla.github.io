VERDICT: DONE

Round 2, exercises (fi, en, fi-easy; numbers unchanged, answers.py untouched).
- Visual Major: Sijoitus chains of L1-02, L1-03, L1-04, L2-03, L3-03 re-broken in 5d style (aligned, breaks before `\cdot`, an `=` row each; L2-03 as three short blocks with joten/ja). Also L2-02 Sijoitus (known clipped) and the three inline Järkevyys formulas that clipped (L2-03, L3-05, L2-09: each chain lifted to its own aligned block, with the quantity symbol G, a_n', F_0 on its first row). Checked at 352, 360, 390 and 1280 px: nothing of the exercises clips. Deleted 13 fy5-5 rows (fi, en, fi-easy) from docs/clipped-formulas.tsv.
- Not fixed (lesson text, not the exercises): two known rows stay in the tsv: the Etsi virhe prompt in inquiry.json (`g = \gamma ... = 6,674...`, clipped at 352, 360, 390) and the lesson's worked-example row `= 6,674 \cdot 10^{-11}\,\tfrac{...}` (9 px at 352 only). Both are pure re-breaks for a lesson round.
- Science Polish L2-08: the feedback of the reason "Kaikki kappaleet putoavat…" (exercises.json) and the model answer (solutions.md) now say it with forces: A is pulled only by B and B only by A, the force is equal on both, the larger mass of A accelerates less. No field strength; task not marked.
- Not done: the level 3 count question (pedagogy Polish, not listed).
Checks: check_solutions ok, lint 0 errors, answers.py runs, check_i18n ok for fy5-5.
