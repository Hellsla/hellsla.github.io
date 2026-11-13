VERDICT: PASS
CONTENT-HASH: 7a9383fdf3772fc8
Delta review (solution practice, 2026-11-12) of the version passed before.

## Blocking
(none)

## Polish
(none)

## Checked
Earlier Blocking 1 resolved: `sovella/tasks.json` s5 a `units_precision` now awards $\rho \approx 2{,}7 \cdot 10^3\,\text{kg/m}^3$ with the two-figure reason ($V = 70\,\text{cm}^3$) and also accepts 2680 kg/m³, matching the model answer, *Hyväksytään myös* and the answer 2680 ± 2 %. answers.py run: s5-a 2677,1, s5-b 78,0, s6 unchanged (0,4247; 3,779 m/s²; +10,25 %). The fix is the same in fi, fi-easy and en; `units.py check` passes; nothing else changed.
