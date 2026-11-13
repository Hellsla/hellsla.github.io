VERDICT: PASS
CONTENT-HASH: cf2465df9ace3a5d
SCOPE: delta added-exercise from 5161df0334c5195f base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-7/exercises/solutions.md (fy6-7-L1-10, Vastaus) — "Vastaus kelpaa, kun se on noin ±4 % sisällä" is page mechanics, not part of a model solution; drop it.
- content/fi/FY6/fy6-7/exercises/solutions.md (fy6-7-L2-08, Vastaus) — "arvot luetaan 0,4 kW:n ja 0,25 h:n ruudukkoviivoilta" is not quite true for the cooling stage: 0,2 kW lies halfway between the 0 and 0,4 kW lines. Say so ("0,2 kW puolivälissä ruutua"); the result is insensitive to it (0,25 kW would give 0,4545 €, inside tolerance).

## Checked
- Hash cf2465df9ace3a5d at start and end; delta: only fy6-7-L1-10 and fy6-7-L2-08 judged.
- L1-10: E = Pt at constant power; 1,5 kW · 2,0 h = 3,0 kWh; 3,0 · 3,6 MJ = 10,8 MJ. The MAFY factor 1 kWh = 3,6·10⁶ J is the VERIFIED fy6-7 row of docs/mafy-arvot.tsv (Yksikkömuunnoksia), as the hint says; it is exact, so the rounded 11 MJ (1,9 % off) passes tolerance 4 %. answers.py agrees.
- L2-08 figure generator: 2,4 kW (0–0,5 h), 1,2 kW (0,5–1,5 h), 0,2 kW (1,5–2,0 h), then 0; gridlines 0,4 kW and 0,25 h; alt text gives the same values and no energy or cost.
- L2-08 recomputed: E = 1,2 + 1,2 + 0,10 = 2,5 kWh; K = 0,18 €/kWh · 2,5 kWh = 0,45 €; answers.py agrees; unit €, tolerance 3 % fit. 2,5 kWh per programme is realistic for a vented tumble dryer.
- Both solutions: principle and why (constant power per stage), symbolic E and K = aE before numbers (the lesson's K = aE + K_perus with no fixed fees for one appliance, as in its example), conversions, rounding reason, a real check (mean power 1,25 kW; 3 · 4 MJ upper estimate).
- Notation E, P, t, a, K as in the lesson.
