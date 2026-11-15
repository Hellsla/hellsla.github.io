VERDICT: PASS
CONTENT-HASH: 8e426d6c8acacf91

## Blocking
(none)

## Polish
- inquiry.json `hook` — the hook says Faraday saw that "liikkuva magneetti tuotti" before the student has predicted; it names half the answer to the question that follows (movement matters). Keep the history but end at "magneetti käämin vieressä ei tuottanut virtaa"; let Ennusta 1 and the sim show what moving does.
- inquiry.json `koe-1` — the intro asks the student to compute e·Δt for every row, but the table has columns only for e, Δt and e inside; the product (the lesson's key insight, and a criterion in `johtopaatos`) has no column. Add an optional computed column, or say "laske omalla paperilla".
- inquiry.json `koe-1`/`koe-2` — `min: 2` lets a student record 0,10 and 0,05 m/s only, so Ennuste 2 (doubling) is not tested. Name the two rows the prediction needs in the intro (it says "ainakin"), or require them.
- lesson.md "Kaava: Induktiolaki" — the paragraph also gives e(t) = −N dΦ/dt, a derivative notation the course's students may not have; one sentence "tangentin kulmakerroin" already carries it. Consider moving the d-notation to a clause marked as extra.
- Sim shows negative e (−20 mV) before the sign is explained; the model note says Lenz comes later, which is enough, but Ennuste feedback could add "merkki selitetään myöhemmin".

## Checked
- Path: prerequisites (magnetic force on a moving charge, field of a coil) are retrieved, then predictions, sim, two controlled experiments, explanation `after` both, theory, staged seven-step example; covers all four slot goals, no self-induction, Lenz deferred to the next chapter.
- Both predictions can be argued from the hook and can be refuted: the sim reports e inside the field, e on entry and Δt, so each wrong option is contradicted by a model value (feedback names the evidence and repairs the misconception "field itself gives voltage" / "motion alone gives voltage").
- Variable control: B and N locked in Koe 1, v and B locked in Koe 2; the e·Δt invariance is a real emergent result, not a restated formula.
- Simulation (captures 390 and 1280): picture, two graphs, one legend line, controls and readout visible; the model text sits behind Käyttöohje/Mallin oletukset/Laskennan selitys; readable on a phone.
- Figures (hero, Faraday, flux, graph, rod, scene): recognisable, uncluttered, labelled, colour paired with ×/arrows/signs; rod figure forces and polarity are consistent; the graph matches the sim defaults; descriptions give a non-sighted reader the same data.
- Theory figures come after the experiments, so they do not disclose the prediction answers.
- Worked example: seven stages, units conversion, 2 s.f. justified, reasonableness check; not repeated in the exercises.
- Etsi virhe has a real, common mistake (cm² → m²), each distractor's feedback repairs; transfer task has three progressive hints and slip-based mistakes; check 1 distractors are misconception-based; explain criteria are observable.
- Exit ticket tests the core idea (suuri vuo ≠ suuri jännite). Finnish reads well; glossary terms are used consistently. Workload fits one lesson.
