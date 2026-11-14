VERDICT: PASS
CONTENT-HASH: edc1028be1632df7
SCOPE: delta added-exercise from 7c99e4251271e391 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- solutions.md fy6-4-L2-09 Vastaus — "500 mA, kaksi merkitsevää numeroa" is ambiguous as written; "0,50 A = 500 mA" (already in Sijoitus) or $5{,}0 \cdot 10^{2}\,\text{mA}$ shows the two figures.

## Checked
- fy6-4-L2-09 recomputed: R = 30 Ω · 45 Ω : 75 Ω = 18 Ω, I = 9,0 V : 18 Ω = 0,50 A = 500 mA; matches answers.py and exercises.json (unit mA, tolerance 0,02).
- Topology of fy6-4/task-parallel traced in figures.py: R1 (top wire) and R2 (middle wire) both join node (xL, T) to node (xR, M), so they are in parallel across the battery; values 9,0 V, 30 Ω, 45 Ω shown, no currents; alt text gives the same.
- Ideal battery and wire resistance neglected stated in the task, as in the brief's example.
- Solution complete: parallel reasoning, symbolic R and I, conversion to mA, branch-current check 0,30 A + 0,20 A and R < smaller resistor.
- Does not repeat the worked example (different values, asks the same quantity at level 2 with a figure to read: acceptable).
- Content hash checked at start and end.
