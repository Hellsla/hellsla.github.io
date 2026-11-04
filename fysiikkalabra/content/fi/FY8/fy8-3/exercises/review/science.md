VERDICT: PASS
CONTENT-HASH: 858f921815ead802
Round: 2

## Blocking

## Polish
- exercises.json:82 (L1-08) — the new transition 2 → 4 (2,55 eV, 486 nm) is the same line as L1-03 (486 nm → 2,55 eV). The physics is right and the Järkevyys even uses it as a cross-check, but the two level-1 tasks give the same number. — Optionally use 3 → 5 (0,967 eV), or keep it and name the link to L1-03.
- exercises.json L1-08 `kind: ["data"]` — the task has no data table, so "data" does not fit the task. — Use `["calc"]` or the kind the schema uses for a one-formula calculation, or drop it.
- solutions.md:187 (L3-04, first bullet) — "(ylätaso kokonaisluku)" reads as if the condition held. — Write "(ylätason $n_\text{y}$ olisi oltava kokonaisluku)".

## Checked
- Round 1 had no blockers. All five round-1 polish items are applied: L3-05 names the filtered 4 → 1 line (97,3 nm); L2-05 reads its slope from (0,0300; 723,3 THz) and (0,1100; 460,2 THz) inside the data range and calls the intercept an extrapolation; L2-07 now uses 5 → 1 and says the r ∝ n² claim may hold in Bohr's model; the L3-04 a) text no longer gives away m = 3; L2-06 says "perustilasta ylemmän tason erotusta".
- Recomputed with my own formulas: L1-08 E₄ − E₂ = 2,55 eV ✓. L2-07 E₅ − E₁ = 13,056 eV → 13,1 eV, and 95,0 nm ✓; the pupil's 25 · 13,6 = 340 eV is wrong for the stated reasons. L2-05 least-squares slope −3288,8 THz → 13,60 eV, and the line passes through 723,3 and 460,2 THz at the stated points ✓. L3-04 365,3 THz ✓. L3-05 97,25 nm ✓.
- L1-06 reordered: one correct option (4 → 1, 12,75 eV, 97,3 nm). Each distractor is wrong and its feedback numbers are right (5 → 4 gives 0,306 eV ≈ 4052 nm; 3 → 2 gives 1,89 eV and 656 nm; 2 → 1 gives 10,2 eV).
- L2-07 and L1-08 no longer duplicate each other (both were 12,1 eV in round 1).
- The L3-04 solution's new bullet list renders cleanly at 1280 px (capture taken after the fix commit).
- Levels 8/7/5, notation and constants as in the brief.
- Hash 858f921815ead802 is the same at the start and the end.
