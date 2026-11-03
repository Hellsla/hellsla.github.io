VERDICT: FAIL
CONTENT-HASH: 065e2c938d949599

## Blocking
- inquiry.json:113 (sim `model`) — A: "Laturissa ei ole diodia, joten liian pieni laturin jännite purkaa kennoa, kunnes se on tyhjä" is wrong for the model and for the physics. The cell discharges only until its source voltage has fallen to the charger's voltage, where the current is zero. It empties completely only if $U_\text{lat} < 3{,}40\,\text{V}$. sim.js `cell()` and lesson-answers.py do this correctly: with 3,6 V from 80 % the level settles near 25 %. — Fix: "…purkaa kennoa, kunnes kennon lähdejännite on laskenut laturin jännitteeseen (alle 3,40 V:n laturi tyhjentää sen)."

## Polish
- inquiry.json:316 — "muuttaisi tulosta vähän": leaving out $R_\text{s}$ gives 4,6 A instead of 4,0 A (+14 %). Say "muuttaisi tulosta noin 15 %" or "vähemmän".
- inquiry.json:348 (siirto, Järkevyys) — "kolmannes energiasta menee hukkaan": the loss is 30 %. Say "lähes kolmannes".

## Checked
- Recomputed every number in one script (own ODE integration of the cell): start 2,2 A; 0,88/0,22/3,40 V drops; 3,62 V terminal; koe-1 1,47/0,99/0,66 A and E 3,76/4,01/4,17 V; koe-2 −0,88/−0,08/0,32/1,12 A at E 4,04 V; koe-3 t_full 2,01/1,37/0,87 h, W_lat 8,8/9,2/10 Wh, η 86/83/76 %; full charge 9,0/7,6 Wh, losses 1,12 + 0,28 Wh, η 84 %.
- Worked example 2,0 A, 3,90 V, the 16,8 A check; virhe 35 A vs 4,0 A; siirto 1,68 with mistakes 2,5/2,40/1,75; check 2 6,0 A (48 A, 7,2 A), 12,9 V both ways; exit ticket 9000 C; 19,25 Wh; 12 : 3,7 = 3,24; 37 vs 45,6 Wh.
- Figures to scale: capacity graph (0,50 A × 4 h), potential graph (40,6 px/V), energy flow widths 90/76/11/3 = 9,0/7,6/1,1/0,3 Wh.
- Current and energy directions in all figures and the sim.
- Voltage law, $I = (U_\text{lat}-E):(R+R_\text{s})$, $U = E \pm R_\text{s} I$ with conditions ($U_\text{lat} > E$, diode); notation $E$ lähdejännite, $R_\text{s}$, energy $W$ stated.
- The energy wording "sisäenergiaksi, joka siirtyy lämpönä" is used. No "muuttuu lämmöksi". The efficiency sentence follows the guardrail.
- The cell is neutral and stores chemical energy, not charge. Capacity is charge, energy is $UQ$ with the nominal voltage.
- Predictions: exactly one option is correct in each, and every distractor's feedback is right with model values. The simplifications are stated (linear E, CC/CV, model values).
- Experiments: each varies one parameter and locks the rest; the simState keys I, E, soc, tFull, Wlat, eta exist.
