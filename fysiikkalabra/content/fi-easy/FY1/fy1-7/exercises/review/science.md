VERDICT: PASS
CONTENT-HASH: b2d6a4985ac2c285

## Blocking
- none

## Polish
- content/fi-easy/FY1/fy1-7/exercises/solutions.md (fy1-7-L2-09, Mallivastaus d) — "Saturnus ... vain noin puolet sen tiheydestä": 687/1638 = 0,42, so "alle puolet" would be closer. This is the same wording as the passed Finnish version, so it is not blocking.

## Checked
- Delta: the two added tasks fy1-7-L2-09 (NASA Planetary Fact Sheet) and fy1-7-L2-10 (PhET Density), their solutions, and the answers.py lines. Each one matches the Finnish version that passed science (same answers 5493 and 2700 kg/m³, same unit and tolerance 0,02).
- L2-09, my own recomputation: ρ = 6m/(πd³) gives Earth 5493 kg/m³ (−0,4 % from NASA's 5514) and Saturn 619 kg/m³ (−9,8 % from 687). answers.py gives 5493,29, which matches the key.
- L2-09 oblateness: the explanation is right. Using the equatorial diameter overestimates the volume by about the flattening: about 10 % for Saturn (f ≈ 0,098) and 0,34 % for Earth (f ≈ 1/298). That accounts for most of Earth's 0,4 % difference. The hint (rotation period about 11 h) fits.
- L2-09 table: all eight planets' m, d and ρ match the fact sheet. b) and d) are right: there are two groups, Mercurius is almost as dense as Earth, Neptune is the densest giant, Jupiter is about 4,2 times less dense than Earth, and Mercury is denser than Mars. The "no lines between points" reasoning and the reasonableness checks (crust about 3000 kg/m³, Saturn below water) are sound.
- L2-10, my own recomputation: m/V = 2,703; 2,703; 2,703; 2,698; 2,699 kg/l. The fit through the origin gives 2699,7 kg/m³, consistent with the key 2700. The volumes equal m/2,70 rounded to 0,01 l. The prediction 2,70 · 9,26 l = 25,0 kg matches the simulation's 25,00 kg.
- L2-10 physics: a line through the origin is justified by m = ρV. Reading Volume from the panel rather than from the water level is correctly reasoned for floating and sinking bodies. The unit conversion kg/l → kg/m³ is right. Glass and aluminium sharing 2,70 kg/l in PhET makes d) a valid argument, and hollow bodies or mixtures are also noted.
- Symbolic-first, the conversions and the significant-figure reasons (3 s.f. from the mass 5,97·10²⁴ kg and from the volume readings) are present in both solutions. Notation is ρ, m, V, as in the lesson.
- Scope: density, a linear model, graphs and data, all within FY1's central contents. No later-course physics.
- The hash is the same at the start and at the end.
