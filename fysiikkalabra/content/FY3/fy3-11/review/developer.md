VERDICT: DONE

Seven teacher-listed items only. Exercises, answers, solutions and sim physics unchanged.

lesson.md
- Ydinajatus: the "fy3-2" reference is replaced by "voima kertaa matka: W = Fs = pAs". The heat-engine paragraph is split after "…yhteensä.". New heat-pump SVG figure (600×300, aria-label) after the heat-pump paragraph: arrows W and Q_ulko (widths 1 : 2) merge into Q_sisälle, with LaTeX labels.
- Figure 1: the T₁, T₂, Q₁, Q₂ and W boxes are enlarged (font-size 32 px), so they render at about 16 px at 360 px. Box texts shifted left.
- Kaava: one sentence contrasts the work done by the gas (pΔV) with W in ΔU = Q + W (fy3-5, work on the gas). Added Q_sisälle = Q_ulko + W and ε = Q_sisälle/W, with symbols named.

sim.js
- automoottori: efficiency slider max is 45 %; the other modes reset it to 60 %.
- Readout: four short lines in every mode (≤ 266 of 294 px at 360 px).

tests/sims/fy3-11.json
- Readout assertions now match the new text. The car conservation case uses 44 % instead of 58 %. Added two range assertions: 10–45 % for the car, and 10–60 % again after switching back.
