VERDICT: PASS
CONTENT-HASH: 84089ae446eb257f
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- s2 c: added sentence "pyöristämättömillä arvoilla se on 77,6 kW" recomputed: 0,64 · 0,25 · 485,1 kW = 77,6 kW; the row above (485 - 175 - 233 = 77 kW) stays right for the rounded terms; 16 % holds for both. New answers.py key `fy9-kaasut-s2-waste` = (P0 - Pe - Ph)/1e3 is the same quantity.
- s5 common mistakes: "moolimassaksi tulee noin kaksi kolmasosaa oikeasta" is now the right quantity (n becomes 1,5-fold, M = m/n 0,68-fold).
- s7 e: "noin 21 °C" = 10 °C (given sea temperature) + 11,3 K = 21,3 °C; agrees with c.
- s7 c text: the derivation is now asked "symbolein" from the heat transferred per unit time (lämpöteho) and the volume flowing per second; the equation criterion (P2 t = c rho V dT) and the solution answer exactly that; dT = 2,7e9 W / (4190 · 1000 · 57 W/K) = 11,31 K, answer value unchanged.
- `practice.py check` OK (7 tasks, 110 points).
