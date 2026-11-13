VERDICT: PASS
CONTENT-HASH: 07b8fc3a7879dabc
SCOPE: delta added-exercise from fba7000b59694eb4 base c52e6381769f

## Blocking

## Polish
- exercises/solutions.md (fy3-9-L2-09, Vastaus) — the reason given for "kolme merkitsevää numeroa kuten luetussa paineessa $120\,\text{kPa}$" is weak. The value is read exactly at a grid crossing, so "Kuvaajan lukeminen on arvio" does not explain the ±2 %, which is simply the default acceptance. Optional: name $100\,{}^\circ\text{C}$ and the exact crossing as the reason.
- exercises/exercises.json (fy3-9-L2-09) — the four points are exactly proportional, which is fine for an "esimerkkiaineisto". If the text ever calls them measured, add the guardrail sentence that real points lie only *yleensä* near the line.

## Checked
- Figure generator: points $(T, 0{,}4T)$ at 200, 250, 300 and 350 K, all on crossings of the 50 K / 20 kPa grid; the description lists the same points and gives no $p/T$ and no answer.
- Recomputed from every point: $p_2 = p_1 T_2/T_1 = 149{,}26\,\text{kPa}$ (149,2 kPa with 273 K), which matches answers.py; tolerance 0,02 (146,0–152,0 kPa) accepts all of them.
- Law and conditions: isochoric change with constant $V$ and $n$, stated in the task (closed rigid vessel), with kelvin temperatures; thin air near room temperature, so $p \propto T$ holds. The values are within FY3 (kaasujen tilanmuutokset).
- Solution complete: given/asked, principle with reason, symbolic $p_2 = p_1 T_2/T_1$ before numbers, °C → K conversion, substitution with units, rounding, real checks (ratio 1,24; above the 350 K point).
- Notation matches the brief ($T = \theta + 273{,}15\,\text{K}$, $p_1/T_1 = p_2/T_2$).
- Rest of the set unchanged since PASS; hash same at start and end.
