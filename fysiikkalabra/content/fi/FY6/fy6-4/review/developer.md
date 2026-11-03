VERDICT: DONE
Round 1 (fix).
- assets/sims/fy6/fy6-4/sim.js: dot speed v = 600·I·k with one shared k = min(1, 0.6/I_main), so branch dots always add up to the main wire; node dots only at the two real junctions; narrow parallel layout moves the branch start (xa 236 to 290) so "U = …" clears the wire; narrow series R2 and U2 moved left off the right wire. Tests unchanged, all pass; 390 px captures checked (koe-2, sim).
- lessons/FY6/fy6-4/sim-spec.md: dropped the 360 px/s cap remark.
- lessons/FY6/fy6-4/figures.py (+ regenerated lesson.md figures): parallel figure has nodes only at the junctions, I2 arrow above its wire like I1.
- lesson.md: causal order in Sarjaankytkentä; Sekakytkentä is now a five-step list (R23, R, I, U1 and U23, branch currents).
- inquiry.json: siirto mandatory, "Kuvan lukeminen", 0,6 A feedback covers both causes (only the parallel part, or 1/R not inverted); ennuste-2 "ihanteelliseen" and the correct option a plain claim; koe-2 starts at R2 = 100 Ω with intro adjusted; koe-1/koe-2 `values` make the Alkutila line and table R1, R2 maths; johtopaatos prompt asks for model values and assumptions.
