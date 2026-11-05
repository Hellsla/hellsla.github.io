VERDICT: PASS
CONTENT-HASH: abd49d96b1b5b3bc

## Blocking

## Polish
- exercises.json L1-08 — the transition 2 → 4 (2,55 eV, 486 nm) is the same line as L1-03 (486 nm → 2,55 eV), so two level-1 tasks give the same number (physics right). — Optionally use 3 → 5 (0,967 eV), or keep it and name the link to L1-03.
- exercises.json L1-08 `kind: ["data"]` — the task has no data table. — Use the kind the schema uses for a one-formula calculation, or drop it.
- solutions.md:187 (L3-04, first bullet) — "(ylätaso kokonaisluku)" reads as if the condition held. — Write "(ylätason $n_\text{y}$ olisi oltava kokonaisluku)".
- solutions.md L3-05 — the Substitution is one long paragraph (same in fi). — Optionally split it into steps.

## Checked
- Only change since the passed version: commit 41862d574 (answers.py, numpy.polyfit → `_polyfit1`); exercises.json and solutions.md are unchanged (git diff e8ad9bdb8..HEAD).
- `_polyfit1` is the ordinary least-squares line (slope Σ(x−x̄)(y−ȳ)/Σ(x−x̄)², intercept ȳ − k x̄); no numpy import is left, and answers.py runs with numpy blocked.
- Old (numpy) and new answers.py outputs compared in one script: all 19 numeric answers identical (max difference 0).
- Independent recomputation (own formulas; L2-05 via the normal equations): slope −3288,75 THz → E_ion = 13,60 eV; intercept 822,0 THz = 3,40 eV = 13,6 eV/4; the fitted line passes through 723,3 THz and 460,2 THz at 0,0300 and 0,1100, as the solution says ✓.
- All other answers recomputed and agree with exercises.json within tolerance: L1-01..08, L2-01..07, L3-01..05 (e.g. L1-07 121,6 nm, L2-07 13,06 eV, L3-04 365,3 THz, L3-05 97,25 nm).
- answer, unit, tolerance and correct flags identical in fi, en and fi-easy.
- check_solutions.py fy8-3: 0 missing or incomplete; answers_shown.py: every shown answer agrees; lint_lesson.py: 0 errors (only word-count and palette warnings).
- Hash abd49d96b1b5b3bc at the start and the end.
