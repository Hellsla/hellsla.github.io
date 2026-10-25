VERDICT: PASS
CONTENT-HASH: c24638cc28c6310a

The lesson delivers its three goals. The hook question is answered at lesson.md:33. The particle model explains the plateaus. The worked example is the open-calorimeter measurement, and the sim's rm/P readout is the same relation, so theory, sim and example tell one story. At 769 words the length matches the FY3 siblings (703–1125); `_gold/lesson.md` is still a placeholder. The weak spot is practice: no exercise or exit-ticket item checks the measurement or the particle model, while L2-04, L3-02 and L3-03 all practise the same point, that boiling takes most of the energy. Nothing blocks publication.

## Blocking

## Polish
- exercises.json:95–102 — L3-03 repeats the conclusion of L3-02 and L2-04, and no exercise practises measuring r — replace it with a measurement task that does not copy the example, e.g. scale readings at two heater powers so heat loss cancels: r = (P₁ − P₂)/(Δm₁/Δt − Δm₂/Δt). Update answers.py first.
- exit-ticket.json:2–5 — Q1 is L1-01 with other numbers (and the same 0,50 kg / 167 kJ as L1-05) — replace it with a particle-model check ("Miksi lämpötila ei nouse jään sulaessa? Selitä hiukkasmallilla.").
- lesson.md:68 — "Kuumentimen energia siirtyy kokonaan veteen" is stated as fact, but line 72 then blames losses for the error — write "Oletetaan, että …".
- lesson.md:37 — faasikaavio (a glossary term and a summary bullet) gets one sentence, no figure and no further use — add a small schematic SVG, or cut the summary bullet.
- exercises.json:72, 82, 90 — L2-04, L3-01 and L3-02 need c(water) = 4190 J/(kg·K), which neither the task nor the lesson gives, while c(ice) is given in L2-02 and L3-03 — state it in lesson.md:35 or in the tasks.

## Checked
- lint clean; answers.py output matches exercises.json
- meta goals = curriculum.json; within MAOL FY3 scope
- 5/4/3 exercises; none repeats the worked example (L2-01 solves for t)
- Ratios in text: r/s ≈ 6,8, r/(c·100 K) ≈ 5,4, s/c ≈ 80 K
- Example 300 kJ / 0,128 kg = 2,34 MJ/kg; direction of the loss error correct
- sim.js matches sim-spec.md; the Q = Pt readout links the (t,T) chart to the (Q,T) curve
- SVG plateau lengths 40 : 280 px match s : r
- Hook question answered in theory and in exit ticket Q2
