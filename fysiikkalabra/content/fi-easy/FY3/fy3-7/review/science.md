VERDICT: PASS
CONTENT-HASH: fe8bebd525a0b695

## Blocking
- none

## Polish
- lesson.md heating-curve figure — the plateaus are not to scale (melting 36 px against 120 px for warming water 0→100 °C; to scale it would be about 96 px, and boiling about 647 px), and only the aria-label says so. A sighted reader sees melting as needing far less energy than warming the water, when the text says it is about the same (0→80 °C). — Put a visible "ei mittakaavassa" note in the figure or under it, or draw the melting plateau about 0,8 times the length of the water segment.
- inquiry.json simulaatio `model` — "Siksi vesi kiehuu 100 °C:ssa" comes after the sentence about the picture's scale, so "Siksi" seems to follow from the scale and not from the constant 101 kPa. — Move the scale sentence after the boiling sentence.
- inquiry.json pred-1 correct option "vesi kiehuu pois puolessa ajassa": in the simulation the steam stays under the piston, so nothing boils away. This is a fair simplification (C), and "kesto" is defined in the prompt. — Optional: "kaikki vesi höyrystyy puolessa ajassa".
- sim.js line 867 code comment "breaks the bonds between particles": the student never sees it, but it uses the wording the guardrail replaces. — Optional: "changes the interactions between particles".

## Checked
- One script recomputed every number from the task data with my own formulas, and all agree: r/s = 6,77, r/(c·100 K) = 5,39, s/c = 80 K, worked example r = 2 343 750 J/kg (+3,7 %, Δm 133 g), pr-lampo 210/2,1/419 kJ, the plateau lengths 1130/565/83,5/167 s, virhe 66,8 kJ, siirto 188 W with mistakes 27,8 and 11 300, check-2 0,597 kg with mistakes 0,677 and 4,04 plus its check 0,54 kg, check-3 2524 J against 264 J (≈ 9,6×).
- Worked example: Q_kuum = Q_h → Pt = rΔm → r = Pt/Δm, solved symbolically first; the loss direction (r comes out too large) and the significant figures are justified.
- Changes of state: the guardrail mechanism wording is used, "molecules stay intact" is said everywhere, and "pure substance, constant pressure" appears in the theory, formula section, summary, contribution, goals and misconception.
- pΔV is about 7,5 % of r: "pieni osa" is correct. The 1700× volume is right.
- Phase diagram: the melting curve's negative slope, the triple point below 100 °C, and the mountain point at lower p and lower T are all correct.
- Heating curve slopes: ice/water 2,0 and steam/water 2,0 match c ratios of 2,0 and 2,1.
- sim.js stateAt and stages implement Q = cmΔT, sm and rm with the table values. The piston model and its limits (open pot, rigid vessel) are stated. simState gives tMelt and tBoil. exp-1 locks m and varies P; exp-2 locks P and varies m. The initial values lie on the slider steps.
- Every choice item has exactly one correct option, and each distractor's feedback says correctly why it is wrong. In pred-3 Bea is the only correct speaker, and the feedback says the simulation is built on her model.
- The model answers (johtopaatos, check-3) and the exit ticket match the theory.
- The hash is unchanged from start to end.
