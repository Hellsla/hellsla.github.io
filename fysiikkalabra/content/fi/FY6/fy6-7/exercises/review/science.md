VERDICT: PASS
CONTENT-HASH: 0725c3201eb7ad5e

## Blocking

## Polish
- solutions.md:180 — L2-07 Kuvaajan lukeminen: "Se kulkee pisteen (48 h; 1,64 kWh) kohdalle" is true of the fitted line only to about 0,1 % (my least-squares slope through the origin gives 1,639 kWh there). You could write "kulkee lähes pisteen kautta", so it is not read as joining raw points.
- solutions.md:245 — L1-10: the sentence "Vastaus kelpaa, kun se on noin ±4 % sisällä" is about the checker, not the physics. You could drop it.

## Checked
- Hash 0725c3201eb7ad5e at the start and at the end.
- I recomputed all 20 numeric answers in one script with my own formulas (E = Pt, E = UIt, P = U²/R, K = aE + K_perus, meter differences, payback H/(aΔE), least-squares fit through the origin). All agree with answers.py and exercises.json. My fit gives 299,1 kWh for L2-07 against the key's 299,3 kWh, inside its 5 % tolerance.
- The round-1 blocking items are fixed. L2-02 (:69) now reads $4{,}8 \cdot 10^{2}\,\text{kJ}$. L2-05 (:154, :156) reads $7{,}3 \cdot 10^{2}\,\text{kWh}$ and names the limiting data correctly: 90 W, 60 W and the times; 110 W, 800 W and 1200 W have more figures. L2-07 (:184, :186) reads $3{,}0 \cdot 10^{2}\,\text{kWh}$.
- P7 (a): 230 V is treated as three figures (L1-03 5,22 A, L3-03 4,99 kWh).
- P7 (b): no other final answer with two figures is written with a trailing zero. 40 W, 60 W and 20 snt-type data count as two figures; 350 kWh, 320 kWh and 489 € count as three.
- P7 (c): no maximum or minimum is rounded in this set.
- Every tolerance lets an answer rounded to the data's figures pass (worst case L1-10: 11 MJ against 10,8 MJ is 1,9 % inside 4 %).
- Figures: washer gives 0,80 kWh and dryer 2,5 kWh, so 0,45 €. Both have the stated grid steps, and their descriptions match the drawn data without giving the energy.
- L1-06 and L1-09 each have exactly one correct option. Each distractor's number comes from the error its feedback names (÷3600, minutes as hours, W as kW, W·min).
- L3-04: the saving is 6,0 kWh · 15,5 snt/kWh = 0,93 €, and the mean price is 14,08 snt/kWh. L3-05: payback 12,96 a and a 77 € gain. The waste-heat point is right physics.
- Scope (power, kWh, the bill) and notation (E, P, t, a, K_perus) match the brief.
