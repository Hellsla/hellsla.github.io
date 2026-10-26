VERDICT: PASS
CONTENT-HASH: 89861521952abfbd

## Blocking
(none) Round-2 blocker fixed: inquiry.json exp-1 intro now has "tulon $pV$ jouleina" and the unit relation in maths; git diff shows no other lesson change.

## Polish
- Simulation canvas (text in the canvas), DOM readout ("T = 20 °C", "Vakio pV = ...", "V 0…100 ml") and the table under the canvas (V, 1/V, p, T, pV headers in monospace) stay plain interface text per NOTES.md §1; the experiment table headers do render V, p, pV, θ, T as maths. Revisit when the teacher decides.
- fy3-9-fig-5: the "−273 °C" label sits on the bottom edge of the viewBox; add margin.
- Gauge scale numbers "100" and "200" are overlapped by the needle at 390 px; enlarge the dial or drop one label.
- solutions.md L2-01: the real-gas remark (about 1,8 m³) contradicts the answer 2,0 m³ asked under "oleta, että Boylen laki pätee"; move to a separate "Huomio" line.
- inquiry.json "ruisku": the student is told to compute a pV column but has nowhere to enter it; it is a mental check only. Say so, or accept as is.

## Checked
- Round-1 blockers fixed: symbols in inquiry.json (pairs, 1/V, p₁V₁, θ), exercises.json and exit-ticket.json are maths; the Alkutila line and exp-2 table headers render symbols as maths (1280 px capture).
- Simulation speed control ("Nopeus"): clear label, note states it changes only pace, not p, V or T; the 390 px layout is not cramped.
- Learning path: hook, retrieval, three predictions each refutable by exp-1 or exp-2 (reveal after min 2/3), wrong-option feedback repairs the misconception, no answer given before commitment.
- Slot goals met: Boylen laki experimentally, p = vakio·1/V graphically, new column 1/V, noisy-data item with a real cause (heating).
- Figures 2-5 legible in captures, each beside its paragraph; worked example in five stages, symbolic first.
- Exercises: three levels, none repeats the example; check-3 has model answer and criteria; exit ticket tests the core idea; workload one lesson; Finnish reads well.
- Phone captures at 390 px: nothing clipped; lab at 1280 px puts the simulation beside the experiments.
