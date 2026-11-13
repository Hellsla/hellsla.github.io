VERDICT: PASS
CONTENT-HASH: 4b72cccf4ef872c5
SCOPE: delta added-exercise from 5161df0334c5195f base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-7/exercises/solutions.md (fy6-7-L1-10, Vastaus) — "Vastaus kelpaa, kun se on noin ±4 % sisällä" is page mechanics, not part of a model solution; drop it.
- content/fi/FY6/fy6-7/exercises/solutions.md (fy6-7-L2-08, Vastaus) — "arvot luetaan 0,4 kW:n ja 0,25 h:n ruudukkoviivoilta" is not quite true for the cooling stage: 0,2 kW lies halfway between gridlines. Say so; the result is insensitive to it.

## Checked
- Hash 4b72cccf4ef872c5 at start and end; delta round 2: only fy6-7-L1-10 and fy6-7-L2-08 judged.
- L1-10: E = Pt at constant power; 1,5 kW · 2,0 h = 3,0 kWh = 10,8 MJ with the exact MAFY factor 1 kWh = 3,6 MJ; rounded 11 MJ is 1,9 % off, inside 4 %. answers.py agrees.
- L2-08 figure: 2,4 kW (0–0,5 h), 1,2 kW (0,5–1,5 h), 0,2 kW (1,5–2,0 h); alt text gives the same, no energy or cost.
- L2-08 recomputed: E = 1,2 + 1,2 + 0,10 = 2,5 kWh; K = 0,18 €/kWh · 2,5 kWh = 0,45 €; answers.py agrees; tolerance 3 % fits; 2,5 kWh per programme is realistic.
- Both solutions: principle with its reason, symbolic E and K = aE before numbers, conversions, rounding reason, real checks; notation as in the lesson.
