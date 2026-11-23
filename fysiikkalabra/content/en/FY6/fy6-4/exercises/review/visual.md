VERDICT: PASS
CONTENT-HASH: cdf30d1f28121f1a
SCOPE: delta numbers from 934ed52fd84979e7 base a2442fe

## Blocking

## Polish
- [Minor] 4-21 solution (L3-3) — the last Formula row still writes $R_1/2$ with a slash inside a fraction — write the nested fraction or a colon.
- [Minor] Formula blocks with fractions in every row (4-21, 4-13) are tight vertically; shared mathlayout row spacing, not a per-lesson fix.

## Checked
- Diff `git diff a2442fe -- content/en/FY6/fy6-4/exercises` read: 11 Formula blocks only, bare $\Sigma U$/$\Sigma I$ labels removed, rows read `X &= ...`.
- Captures (content/en/FY6/fy6-4/review/shots) opened: open-exercises-L3-1280-3 (4-21, longest block: equals signs in one column, nothing clipped) and the earlier L1/L2/L3 open-solution captures (4-1, 4-10, 4-13, L3-6 corrected circuit); layout survived.

## Scores
illustrations n/a · typography 4 · Finnish 4 · accessibility 4
