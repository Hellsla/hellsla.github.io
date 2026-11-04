VERDICT: PASS
CONTENT-HASH: f11d7c4f7347aaa8
Round 2.

## Blocking

## Polish
- solutions.md:185 (L3-04 c) — "Kalvo on siis tummempi kuin yksikään väri paksummassa kohdassa" is not quite true: at 450 nm the weakened wavelengths 661,5 and 441 nm also reflect 2,0 %, the same as the thin film — fix: "Kalvo on siis kokonaisuutena tummempi kuin paksumpi kohta, jossa heijastus vaihtelee värin mukaan 2,0 %:sta 5,7 %:iin."
- solutions.md:185 — the full two-surface formula gives 5,7 % at the maximum (5,8 % without the multiple-reflection denominator); "noin 5,7 %" is better.
- L2-05 — the model goes through the origin (n = 1,333 that way, 1,315 with a free fit); both are accepted (carried over).
- L3-05 — the air wedge is not in the plan (pedagogy; carried over).

## Checked
- Round-1 Blocking L2-07 resolved: glass n = 1,52 is stated. I recomputed the table with the Airy formula for a quarter-wave MgF₂ layer at 540 nm (d = 97,83 nm): 1,84/1,48/1,31/1,26/1,30/1,39/1,50/1,64 %, which is exactly the table. The solution's ratios of 1,46 and 1,30 are right, and the minimum of 1,26 % matches the lesson's 1,3 %.
- Round-1 Blocking L3-04 b) resolved: "heijastuu ensimmäistä kertaa heikoimmin (heikentävä interferenssi)". d' = 360,0 nm. R at the minimum = 2,0 % = bare water, as c) says; the amplitudes are 0,190 and 0,050.
- L3-04 c "tummalta ja lähes värittömältä" (round-1 Polish) done.
- L3-05 is now given to two significant figures, limited by L = 80 mm (round-1 Polish). LSQ: slope 1,896 mm, intercept 0,054 mm (the solution says that point is the line's intercept, not a measurement), D = 12,42 µm.
- Every new answer recomputed: 96,94 nm; 1,5; 1,315; 443,3 nm; 97,83 nm; 360,0 nm; 12,42 µm. All agree with exercises.json and answers.py.
- The stated good ranges (1,26–1,37; 11,9–12,9 µm) fall inside the box's acceptance (data-step 0,1 → 1,215–1,415; data-step 1 → 11,4–13,4).
- L1-06 reordered: one correct option, it matches `answer`, and the feedback is right.
- Hash the same at start and end.
