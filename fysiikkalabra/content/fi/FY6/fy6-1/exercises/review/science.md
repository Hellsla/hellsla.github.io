VERDICT: PASS
CONTENT-HASH: d7608b5687ea2b2b
SCOPE: delta added-exercise from 3eef2a9fd86daae1 base 8f23aa7ae3bd

## Blocking

## Polish

## Checked
- Hash d7608b5687ea2b2b at start and end; delta: only fy6-1-L2-08 judged.
- Physics: energy delivered to the battery E = UQ with U = 4,0 V constant (stated in the task), Q the area under the (t, I) graph; the lesson's U = E/Q and Q = It, graph area as in the earlier L2-04.
- Figure generator: 0,50 A from 0 to 40 s, linear to 0 at 100 s, zero to 120 s; ticks at 20 s and 0,1 A make every value readable; the alt text gives the same values and not the charge or the energy.
- Recomputed independently: Q = 0,50 A · 40 s + ½ · 0,50 A · 60 s = 20 C + 15 C = 35 C; E = 4,0 V · 35 C = 140 J; answers.py gives 140, tolerance 2 % fits two significant figures.
- Solution complete: principle and why area, symbolic Q = I₀t₁ + ½I₀t₂ before numbers, no conversions needed (stated), rounding to 2 sf from U and the read currents, a real upper-bound check (200 J at constant 0,50 A).
