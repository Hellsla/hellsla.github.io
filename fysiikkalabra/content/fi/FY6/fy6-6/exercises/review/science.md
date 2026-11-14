VERDICT: PASS
CONTENT-HASH: af0ac97658e02be2
SCOPE: delta added-exercise from 2683349f549333dc base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-6/exercises/solutions.md (fy6-6-L2-09, Järkevyys) — the closing sentence "Energia on myös kuvaajan viivan alle jäävä pinta-ala" is stated but not used; one clause tying it to the three rectangles (360 + 300 + 120 kJ) would make it part of the check.

## Checked
- Hash af0ac97658e02be2 at start and end; delta: only fy6-6-L2-09 judged.
- Law: E = Pt per constant-power step, summed; the lesson's E = Pt, and a resistive hob turns its electrical energy into internal energy as the lesson says.
- Figure generator: steps 2000 W (0–3 min), 1000 W (3–8 min), 500 W (8–12 min) with vertical joins; gridlines every 1 min and 500 W, so every value lies on a gridline; alt text gives the same steps and no energy.
- Recomputed: 2000 W · 180 s + 1000 W · 300 s + 500 W · 240 s = 360 + 300 + 120 kJ = 780 kJ; answers.py agrees; unit kJ, tolerance 2 % fits.
- Magnitudes realistic for a hob plate (0,5–2 kW); mean power 1,08 kW lies between the extremes, a real check.
- Solution complete: reading, principle, symbolic sum before numbers, min → s conversions, substitution with units, rounding reason (values read exactly on gridlines).
