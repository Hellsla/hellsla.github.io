VERDICT: PASS
CONTENT-HASH: 5b3a27971a4efdaf
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A `sovella/tasks.json` s7 c: the prompt names the model ("Johda lämpömäärän yhtälöstä $Q = cm\Delta T$"). An application task should let the student choose it: "Johda lauseke meriveden lämpötilan muutokselle. Tunnet veteen siirtyvän lämpötehon ja sekunnissa virtaavan veden tilavuuden."
- A s7 a–c covers the same plant and nearly the same computations as fy9-moderni-s6 (efficiency of OL3, sea water through the condenser). Different unit and the teacher's order, so no change needed here; the mixer may show both.
- C `sovella/solutions.md` s5 Yleisiä virheitä: "Silloin tulos on noin kaksi kolmasosaa oikeasta" follows "ainemäärä lasketaan", so "tulos" can be read as the amount (which is 1,5-fold). Clearer: "Silloin moolimassa on noin kaksi kolmasosaa oikeasta."

## Checked
- Item 18 hunks: 485 − 175 − 233 = 77 kW; s5 error with 311 kPa instead of 210 kPa gives M · 210/311 = 0,68, "noin kaksi kolmasosaa" is right.
- s7 recomputed: 1600/4300 = 0,372; 2700 MW, 64,8 GWh, 2,333 · 10^14 J; 2,388 · 10^8 W/K, 11,3 K, 47 kJ/kg; 563 K, 283 K, 280 K.
- s7 in full: source read in a, c, d; parts progress read → energy balance → derived flow model with a judged assumption → why Q2 cannot vanish → environment and limits of use; criteria observable, sums 2+3+4+3+3 = 15; FY3 content only; no repeat of s1–s6 (s2 c asks the same idea for an engine, with other data).
- fi-easy against fi: same parts, points, criteria, headings, numbers; no step dropped. Sentences short, terms glossed (nimellisteho, nettosähköteho, yläraja-arvio).
- Rendered s7 at 360 px from the preview, all boxes open: nothing clipped.
