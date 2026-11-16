VERDICT: PASS
CONTENT-HASH: 9ff2b23aaedfa400

## Blocking

## Polish
- exercises.json:66 (L1-06, "nelinkertaistuu" option feedback) — "Energia … nelinkertaistuu … Siksi $C$ on kaavassa vakio" reverses the causality: the energy quadrupling does not make C constant — write "Kaavassa $C$ on vakio; vain $U^2$ muuttuu."
- exercises.json:362 (L3-03) — the area is unique only for the thinnest allowed dielectric (any thicker d with a larger A also meets the conditions); the solution assumes the minimum d — add "kun eriste on niin ohut kuin varmuusraja sallii" to the task.
- exercises.json:354 (L3-02) — "varaus siirtyy kondensaattoriin lisää" says the capacitor gains net charge, against the lesson's misconception box (net charge zero) — write "levyille siirtyy lisää varausta $\pm\Delta Q$" (the solution's "Erotuksen tuo lähde" likewise).

## Checked
- All 18 numeric answers recomputed in one script with my own formulas (C = Q/U, C = ε0εrA/d, U_max = E_max d, W = ½CU², origin-fit slopes for L2-05 and L3-04, the L3-05 ratio 6,89); all agree with answers.py and exercises.json.
- Shown answers against the page check (answers_shown step): e.g. L1-08 "1,4·10² mJ" gives step 10, so 140 is accepted; L1-04 220 pF, L3-03 220 cm², L2-05 3,3–3,5 mJ (tol 0,04) are all accepted.
- Significant figures follow P7(b): 120 pF / 500 V give 3 figures (L3-01), 10 F, 200 J and 1000 µF are not the limiting data.
- Connected vs disconnected source (L1-07, L3-01, L3-02): Q or U kept constant correctly; the energy rise in L3-01 is said to be work done pulling the plates apart.
- L1-09 and L2-07: the half-of-QU rule uses a constant-voltage source; the lost half goes to internal energy, as in the lesson.
- L2-06 data match an RC charge with τ ≈ 2,0 s; the option feedback values (3,5; 2,0; 0,5; 0,3 V per s) are right; exactly one option is correct.
- Figures ex-qu (60 µC at 12 V on the gridlines) and ex-qu2 (120 µC; 8 V) give the values the tasks need, their descriptions carry the same values, and neither shows the answer.
- L1-10 polyethylene εr = 2,3 (MAFY) with tolerance 5 %; L3-05 table values match the lesson table.
- Defibrillator L3-04: 150 µF, 1,8 kV, 243 J, 18 s are realistic; the safety reasoning is correct.
- Scope: no capacitor connections and no exponential function, as the course notes require.
