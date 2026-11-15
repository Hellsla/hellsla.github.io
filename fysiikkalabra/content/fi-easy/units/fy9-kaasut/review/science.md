VERDICT: PASS
CONTENT-HASH: 5b3a27971a4efdaf
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: solutions s2, the row 485 kW − 175 kW − 233 kW ≈ 77 kW now agrees with the numbers shown; the unrounded value is 77,6 kW, so "eli 16 %" still holds. A half sentence ("pyöristetyillä arvoilla") would stop a student who computes 78 kW from the unrounded values from doubting it.
- A: s7 c: the net electrical power is used, so the plant's own consumption (about 100 MW) is counted in P2; the answer's "yläraja-arvio" covers it, one clause naming it would make the reason concrete.

## Checked
- Item 18 hunks: s2 rounding row (485 − 175 − 233 = 77); s5 common mistake: with the total pressure 311 kPa instead of the rise 210 kPa, Δn is 311/210 times too large and M is 210/311 = 0,68 of the right value, so "noin kaksi kolmasosaa" is right (the old "kolmasosa" was wrong).
- s7 recomputed with own formulas: η = 1600/4300 = 0,3721; P2 = 2700 MW; Q2 = 64 800 MWh = 64,8 GWh = 2,333e14 J; share 62,8 %; 38,4 GWh + 64,8 GWh = 103,2 GWh = 4300 MW · 24 h; 1600 MW · 8760 h = 14,0 TWh; cρ(V/t) = 2,388e8 W/K; ΔT = 11,31 K; 47,4 kJ/kg; wrong 18,0 K with 4300 MW; 563 K, 283 K, 280/563 = 0,50. All agree with tasks.json, the solution and answers.py.
- s7 physics: efficiency from powers, steady state so P1 = Ps + P2, Q = cmΔT with m = ρV derived in symbols, direction of the estimate, heat engine must reject Q2 (not a loss), low-temperature heat cannot heat a district-heating network by itself. No "muuttuu lämmöksi". Points 2+3+4+3+3 = 15.
- `python scripts/practice.py check units/fy9-kaasut`: OK (7 tasks, 110 points). Hash equal at start and end.
