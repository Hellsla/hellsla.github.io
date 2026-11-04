VERDICT: PASS
CONTENT-HASH: 379dfaed9bef0431

## Blocking

## Polish
- solutions.md:196 vs exercises.json:265 (L3-05) — Vastaus says 1720 MW, but `answer` and answers.py give 1716. This is within tolerance; make them match ("1716 MW ≈ 1720 MW").
- solutions.md:197 (L3-05) — the leftover 84 MW is about the size of the data spread (ΔT 10,6–10,9 K, ≈ ±25 MW), and the generator and transformer losses are only about 15–20 MW. Add "osin mittausepävarmuutta; ydinvoimalassa ei ole savukaasuja".
- solutions.md:191 — the header "Kuvaajan lukeminen" sits over a table. Use "Taulukon lukeminen".
- exercises.json:75, 86 (L1-07, L1-08) — `kind: reasoning` on one-formula tasks. L1-07 repeats the calculation of L1-02 and fy3-11-L1-03; consider asking for P_h instead.
- exercises.json:246 (L3-04) — close to fy3-11-L3-01 (CHP vs separate production). The boiler top-up step makes it acceptable; note the overlap in the plan.

## Checked
- New answers recomputed independently: L1-07 34,0 %; L1-08 12,0 GWh; L2-05 90,0 % (η_s 35/32/30, η_kok 84,6/88,4/90,0); L2-06 1560 MW; L2-07 36,6 %; L3-04 131,9 MW; L3-05 1715,6 MW. All agree with answers.py.
- L1-06 MC: one correct option. The distractors and their feedback are right.
- L2-05 c): a cold year means more heat and less electricity, so η_s falls and η_kok rises. The data agree, and the solution keeps "sähkö ja lämpö eivät ole yhtä arvokkaita".
- L2-06 c): the weakest η has the smallest P_h. This is argued correctly.
- L2-07: the product rule is derived from the chain, and the 230 % sum is called impossible.
- L3-04: η_kok = 0,88, the boiler top-up and the source of the saving are correct.
- L3-05: P_L < P_h, and the d) answer follows the brief.
- Scope: inside the fy3-15 brief, with no Carnot.
- Plan coverage complete. Levels fit.
