VERDICT: PASS
CONTENT-HASH: 2ced2c581f51c659
SCOPE: delta added-exercise from 21165e7fa5250d9b base b5600a63ddae

## Blocking

## Polish
- content/fi/FY5/fy5-12/exercises/exercises.json:305 (L2-10) — "valitse aaltolajiksi ääni (kaiuttimen kuva) ja käynnistä molemmat lähteet niiden vihreistä painikkeista": the source notes confirm the Interference screen (the second of four), the choice water/sound/light and two in-phase sources. They do not confirm the speaker icon or one green button on each source. Check these details in the simulation, or write only "valitse aaltolajiksi ääni ja käynnistä lähteet".
- content/fi/FY5/fy5-12/exercises/exercises.json:305 (L2-10) — the answer 0.4 has one significant figure, but the solution says 0,40 m with two, as λ = 0,80 m has. Store 0.40.

## Checked
- The hash was the same at the start and at the end. I judged only the added exercise L2-10.
- Recomputed: the smallest positive constructive Δs is λ = 0,80 m (n = 1, because n = 0 gives zero), and the smallest destructive Δs is λ/2 = 0,40 m (n = 0). The line in answers.py computes the same.
- The notation follows the brief: Δs = |s₁ − s₂|, nλ, (n + ½)λ, v = fλ. The solution solves in symbols first and justifies n = 1 against n = 0.
- In a), the central line is constructive, the nodal lines are flat grey, and the pattern is symmetric. This agrees with the brief's "Kuvion viivat" and with the sound view's pressure shading.
- In b), raising f shortens λ (v is fixed by the medium), so the lines move closer together and there are more of them. The central line stays constructive. This is right.
- d) names reflections, many frequencies, sources that are not point sources and unequal amplitudes, so the cancellation is not complete. This matches the lesson ("ei käytännössä katoa kokonaan"), and nothing claims full silence.
- The remark that the points exist only when the source separation is larger than Δs agrees with the triangle argument in the brief.
- The answer in the box (0,40 m) is computed from the task's own λ, not from the simulation, so it does not depend on the source.
- The other source statements (free, in the browser, a Finnish version, four screens) are supported by the fetched notes.
