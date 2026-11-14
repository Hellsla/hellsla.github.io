VERDICT: PASS
CONTENT-HASH: 8bb9e0e9ca841849
Mode: delta

## Blocking
- none

## Polish
- Earlier polish items (L3-02 "force and time at their greatest", L2-05 v_k vs avg, L2-07 rounding reason) still open; not part of this diff.

## Checked
- Hash at start and end identical (8bb9e0e9ca841849).
- Diff, exercises.json L1-03: the ball is now thrown vertically upwards and spiked when momentarily at rest at the top. A vertical throw is indeed at rest at its highest point, so v_0 = 0 is now justified by the situation instead of asserted (a ball on a general arc would keep its horizontal velocity at the top).
- Solution L1-03 still agrees: v_0 = 0, I = mv = 0.27 kg · 18 m/s = 4.86 N·s -> 4.9 N·s; weight neglected during the spike as the task states; answer, unit, tolerance unchanged.
