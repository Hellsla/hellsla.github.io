VERDICT: PASS
CONTENT-HASH: 1c8be0fc88c80344
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- s2 c Järkevyys: 485 kW − 175 kW − 233 kW = 77 kW from the rounded powers; the added sentence gives 77,6 kW unrounded, which is what answers.py now computes (`fy9-kaasut-s2-waste` = 77,6; 0,64 · 0,25 · 485,1 kW). 77,6/485,1 = 16 %, so the row's conclusion holds.
- s5 common mistake: with 311 kPa instead of the rise 210 kPa the amount of substance is too large and the molar mass is 210/311 = 0,68 of the right one; "moolimassaksi tulee noin kaksi kolmasosaa oikeasta" now names the right quantity.
- s7 e: 10 °C + 11 K = 21 °C; now the same as c's Järkevyys ("palaa mereen noin 21 °C:n lämpöisenä") and the task's sea temperature. No 20 °C left in s7.
- s7 c part text: asks for a symbolic expression from the heat per unit time and the volume per second without naming Q = cmΔT; the solution and the equation criterion derive ΔT = P_2 t/(cρV) from exactly those; ΔT = 2,7e9 W / 2,388e8 W/K = 11,3 K unchanged.
- `python scripts/practice.py check units/fy9-kaasut`: OK (7 tasks, 110 points). Hash equal at start and end.
