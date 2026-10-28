VERDICT: PASS
CONTENT-HASH: edd01c91e24f237e

## Blocking

## Polish
- tests/sims/fy3-9.json (readout isobaarinen −50 °C assertion) — the note still says "minus sign U+2212", but the assertion now matches TeX `-50`, which KaTeX typesets as a true minus. The check is equivalent; only the note is stale — reword the note to "TeX minus".
- content/FY3/fy3-9/sim.js:1316–1318 — `fi()` is now unused, and a stray duplicate comment "three significant figures" trails `tx` — delete both.
- content/FY3/fy3-9/inquiry.json (virhe, correct option) — `≈ 250 kPa` (252,5) is right to two significant figures from 0,50 l / 0,20 l. Fine as is; optionally write `≈ 2,5·10² kPa` to make the precision explicit.

## Checked
- All 12 exercise answers recomputed independently. Each agrees with answers.py and exercises.json within tolerance. L2-03 uses a least-squares fit through the origin, giving 2009 kPa·ml (2,0 J); pV runs 1980–2030 kPa·ml, as solutions.md says. L3-02 handles gauge vs. absolute pressure correctly (202 kPa; 216 kPa if the reading is wrongly put into the formula).
- Worked example (1,036 l, +30 %), siirto (1,07 l; mistake 2,10 l), check-2 (120 kPa; mistakes 108 and 0,12), exit ticket (160 kPa, 308/280 = 1,1) and misconception (1,035 → 1,04 l): all correct, and every one is solved symbolically before the numbers go in.
- inquiry: pred-1 (200 kPa, pV = 5,00 J), pred-2 (60,2 ml, V/T = 0,1706 ml/K) and pred-3 (curve 200/100/50 kPa) have the right options marked correct. The γ question gives 1/293 K = 3,41·10⁻³ 1/K. In ruisku, pV = 5040 except at 30 ml (5430, +7,7 %), and heating is the correct reason. All the feedback physics is sound.
- Experiments: exp-1 locks mode and Tc and varies Vml; simState gives p in Pa and the constant in J. exp-2 locks mode and varies Tc; the adapter supplies T, Vgas and VperT. Each setup isolates the parameter it varies.
- The simulation implements pV/T = const in all three modes, and the SI conversion of `constant` is correct. Axis maxima cover the slider ranges: 144 kPa ≤ 160 and 72 ml ≤ 80. The theory curves and the dashed lines to the origin are correct. `calc` and pred-3 say the values come from the law, not from measurement.
- The LaTeX migration lost no physics check. tests/sims/fy3-9.json has 72 assertions before and 72 after. Each changed assertion reads the same values (40,0 | 0,0250 | 125,0 | 293,15 | 5000; 38,1; 0,1706; 76,1; 144,3; 0,3411; the axis scales) through simText. Only the label strings were reworded, e.g. "lämpötila vakio". The numeric simState checks are unchanged.
- The figures are to scale: boyle-graphs (pV = 2000 kPa·ml, line ends at (0,12; 240)), absolute-zero (253–373 K points on lines through 0 K), micro-boyle (gas heights 2 : 1, hit marks 4 → 8).
- Facts: cabin pressure about 78 kPa; at 300 bar air has Z ≈ 1,1; for a 0,5 m² lid the force is about 7 kN.
- Scope: Boyle's law and the isobaric and isochoric changes belong to "kaasujen tilanmuutokset" and to the Boyle experiment. L3-01 uses ρgh from fy3-4.
