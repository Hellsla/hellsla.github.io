VERDICT: PASS
CONTENT-HASH: 7de4344ab38e2aaf
Mode: delta

## Blocking
- none

## Polish
- Earlier polish items (L2-07 rounding reason, L3-03 v_k clash) still open; not part of this diff.

## Checked
- Hash at start and end identical (7de4344ab38e2aaf).
- Diff, exercises.json L1-03: "Pallo heitetään pystysuoraan ylöspäin ... hetkellisesti levossa lentoratansa ylimmässä kohdassa". A vertical throw is at rest at its top, so v_0 = 0 now follows from the situation; same meaning as the Finnish and English sets.
- Solution L1-03 consistent: v_0 = 0, I = mv = 4.86 N·s -> 4,9 N·s; weight neglected during the spike as stated; answer, unit, tolerance unchanged.
