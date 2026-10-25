VERDICT: PASS
CONTENT-HASH: 4373e217df79ecae

## Blocking
(none)

## Polish
1. exercises.json:25 — L1-03 relative tolerance 0,001 accepts 600,4…601,6 mm, so a halved ΔL (600,5) passes; 600,0 is correctly rejected. — Tighten to 0.0005 (600,7…601,3 mm).
2. lesson.md:21 — "Nesteiden ja kaasujen … samalla tavalla" gives no condition for gases; only the table says "vakiopaineessa". — Add "kaasuilla, kun paine pysyy vakiona".
3. solutions.md:63 — L2-03 condition is correct but unexplained: each rail end moves ΔL/2, and a gap gets ΔL/2 from both neighbours. — Add this; "raon täytyy olla riittävän leveä" wrongly suggests 7,2 mm is a design error.
4. lesson.md:37 — water's γ varies strongly with T (≈0 at 4 °C, ≈0,30 · 10⁻³ 1/K at 30 °C); L1-04 true change ≈0,90 l vs 0,84 l. — Optionally note "taulukon arvo on 20 °C:ssa".

## Checked
- Lint clean; hash identical at start and end.
- Micro model (lesson.md:6): anharmonic potential stated correctly and simply; particles do not grow.
- α and γ tables match handbook values at 20 °C; air 3,4 · 10⁻³ 1/K = 1/293 K at constant pressure.
- γ ≈ 3α for solids only; validity limit stated.
- Water anomaly, 4 °C density maximum, freezing from the top, ice floats because water expands on freezing (lesson.md:12, 67; exit ticket 3): correct.
- Worked example 0,0864 m, 0,07 %: correct; blocked-expansion force only qualitative.
- answers.py: right formula, sign and unit conversion in every line.
- Hand-recomputed L1-03, L2-03, L3-03. L3-03: a cavity expands like the solid filling it, so the solid-steel can is correct.
- solutions.md reasoning sound (shrink fit, bimetal bends toward steel).
- sim.js:59–63 implements ΔL = αL₀ΔT exactly; amplitude ∝ √T.

## Python output
```
answers.py: {"L1-01": 2.88, "L1-02": -51.75, "L1-03": 601.02, "L1-04": 0.84, "L1-05": 0.3375, "L2-01": 52.083, "L2-02": 3.024, "L2-03": 36.0, "L2-04": 23.0, "L3-01": 120.0, "L3-02": 20.0, "L3-03": 457.0}
L1-03 window 600.399..601.601; 600.0 err 0.00166; 600.5 err 0.00083
L2-03 rail dL at 36 C = 7.2 mm = gap
L3-03 petrol 475.0, can 18.0 (exact 18.005), overflow 457.0
```
