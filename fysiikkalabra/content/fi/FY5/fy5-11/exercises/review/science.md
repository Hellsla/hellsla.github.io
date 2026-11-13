VERDICT: FAIL
CONTENT-HASH: 65fac7034d08e8df
SCOPE: delta added-exercise from 19c4b1112a3292c3 base 81db4a6fd727

## Blocking
- exercises.json:240, solutions.md:254 (L2-09) — A: the magnitude is impossible. Water waves with λ = 8,0 cm cannot have f = 7,0 Hz. The gravity–capillary relation ω² = (gk + σk³/ρ)·tanh(kh) gives at most f = 4,5 Hz (v = 36 cm/s) even in deep water, and shallow water is slower. The claim "0,56 m/s on aaltoaltaan aalloille tavallinen" is false: ripple-tank waves move at about 0,2–0,35 m/s, as L1-03 and L2-06 show. — Fix: f = 4,0 Hz, which gives v = 32 cm/s (consistent with a depth of about 1,3 cm). Update the answer (32), answers.py and the reasonableness check.
- exercises.json:252, solutions.md:265 (L2-10) — A: the causality is wrong. "veden syvyys ja siis aallon nopeus pysyvät samoina" and "nopeus riippuu … veden syvyydestä, ei taajuudesta" contradict the prerequisite chapter, which says that the speed of water surface waves can depend on wavelength (dispersion). A ripple tank is dispersive. — Fix: state the speed as an assumption, as L2-08 does: "Oletetaan, että aallon nopeus pysyy samana myös uudella taajuudella." The solution then uses that assumption.

## Polish
- L2-10 is the same reasoning as L1-07 (f doubled → λ halved → b/λ doubled → weaker diffraction). The figure reading is what is new, so this is acceptable.
- In the figure, the fronts behind the gap are full semicircles at b/λ = 1,5. That is a fair simplification (C), but it makes the spreading look stronger than it is.

## Checked
- The hash was the same at the start and at the end. Only L2-09 and L2-10 were judged.
- Recomputed from figures.py: fronts at gridlines 1 and 5 give λ = 4 · 2,0 cm = 8,0 cm, and the wall blocks at rows 0–1 and 7–8 give b = 6 · 2,0 cm = 12 cm. The arcs behind the gap are spaced 4 squares apart, the same λ. Then v = 56 cm/s and b/λ' = 12/4,0 = 3,0, which equal answers.py.
- The description gives the same gridline positions as the drawing and marks neither λ nor b. L2-09 needs only λ, and L2-10 also needs b, so neither gives the other away.
- Sig figs: both answers have 2 (7,0 Hz and 2,0 cm per square), and the 2 % tolerance fits.
- The diffraction criterion and $v = f\lambda$ are in the brief's scope (fy5-10 and fy5-11).
