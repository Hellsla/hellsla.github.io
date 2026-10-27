VERDICT: FAIL
CONTENT-HASH: 0caa11574237ad86

## Blocking
- solutions.md:70 (L2-02 Järkevyys) — the check is false. At about 4,2 min/km, 1,2 km takes about 5 min, not "hieman yli neljä minuuttia", so the check contradicts the answer it accepts. — Fix: "kilometri kuluu noin 4,2 minuutissa, joten 1,2 km vie noin 1,2 · 4,2 min ≈ 5 min."
- inquiry.json:343 (data, Kuvaajan lukeminen and Vastaus) — the solution reads 19,1 m as exact from a graph with 5 m gridlines and calls Δx = 15,0 m a three-figure value that "rajoittaa vähemmän". The hints themselves say "noin 19 m" and "noin 15 m". What really limits the answer is the reading precision and the scatter (fit slope 1,494 ± 0,029 m/s). — Fix: read about 19 m (Δx ≈ 15 m) and justify two figures by the reading precision and the scatter, not by "10 s on kahdella numerolla".

## Polish
- solutions.md:19 (L1-02) — "koska kärry ei kääntynyt" is not given in the task; write "jos kärry ei käänny".
- solutions.md:39 (L1-04) — 4,0 m is given to 0,1 m, not "metrin tarkkuudella"; 24 m is the datum that limits.
- inquiry.json:332, :343 (data) — the mistake feedback subtracts 4,2 m where the solution uses the line's 4,1 m. The Järkevyys calls 1,5 m/s "kahden sekunnin välinen kasvu", but the increase per 2 s is about 3,0 m.
- inquiry.json:197, :309 (exp-1, exp-3 Vastaus) — the readout shows 10,0 s and 40,0 m. Two figures is a convention for model values, so say that instead.
- solutions.md:52 (L2-01) — "kuljettu matka eli siirtymä Δx": write s = vΔt or say why the two coincide.

## Checked
- One script ran answers.py and my own formulas on all 12 exercises and every inquiry number: all match and are within tolerance.
- Every principle applies and is justified. Solutions are symbolic first, conversions are right, and rounding follows the figures of a difference. The example's 1,7·10² m is right.
- The other checks are real: back-substitutions, the sledge's x₀ = −11 m, check-2 via 4,8 s, L3-01 between 5,0 and 3,3 m/s.
- The figures are to scale: data line 4,10 → 19,10 m, all six points, the jogger graph and graph E. Predictions match sim.js CASES. The experiments lock tapaus and vary t. pos, vel and path are correct. The hash was unchanged at the end.
