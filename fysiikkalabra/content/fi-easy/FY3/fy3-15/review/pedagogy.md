VERDICT: PASS
CONTENT-HASH: 9bccab069f2e3300

## Blocking

(none)

## Polish

- inquiry.json pred-2 Bea feedback — "yhteistuotannolla ei voitettaisi mitään" is wrong Finnish — "ei voitettaisiin mitään".
- inquiry.json check-1, check-c2, tyypit — the correct option is the longest and most detailed in each, so length gives it away. Shorten it or lengthen the distractors.
- inquiry.json tyypit/ketju (Tutki) — kattila, savukaasu, muuntaja, höyrykierto and lauhdutin are met in Tutki before the Teoria stage. This is the Selkeä suomi version, where a hard word is explained the first time. Add a one-line gloss for höyrykierto and muuntaja in the ketju text, or in the pred-1 prompt.
- lesson.md Sankey figure — the label "lauhdutin 248 MW" covers the whole steam cycle (turbine and condenser). The aria-label says so, but the visible label could read "turbiini ja lauhdutin".
- inquiry.json kaukolampo-tarve (optional) — it needs linear interpolation. That is fine as an optional task, but the hints should say earlier that the 0,75 is a fraction of the way between the end states.

## Checked

- Path: prerequisites (η = W/Q₁, Q₁ = W + Q₂) are retrieved first, optionally. The hook question, "where does the most energy go and could it be used?", is answered only after the student commits in Ennusta and uses the tables. The reflect task returns to it.
- Predictions: both can be refuted by the Tutki tables. Pred-1 is refuted by the 248 MW computed in ketju. Pred-2 is refuted by the 232 and 120 MW table. Each wrong option's feedback repairs its misconception and appears only after commitment. The speakers are shuffled and the right one is not the first.
- No simulation, and sim-spec.md justifies that. The table work is something the student acts on, not just reads. Workload is one lesson, because the extra tasks (kaukolampo-tarve, etsi virhe, siirto, check-3) are optional.
- Theory figures (Sankey, stacked area, bars; captures 390 px) are legible and to scale, with colour never alone, and sit in the Teoria stage after Tutki, so they do not leak the answers.
- Example: seven stages, one step each, symbolic before numeric, with a check (balance, order of magnitude, typical η).
- Etsi virhe, siirto and the numeric checks have mistake-based feedback (average, sum, P₂ versus loss, only electricity subtracted). The exit ticket tests the core idea (η as a product).
- Checks: two concept choices with misconception distractors, one calculation, one explain with observable criteria and a model answer. Check-3 criteria match its question.
- Finnish: terms (hyötysuhde, lauhdevoimalaitos, yhteistuotanto, hukkalämpö, kaukolämpö) match the glossary. Units are in LaTeX.
- Not judged: the exercise set, which is reviewed apart. The figure-task rules do not apply, because no task has a "figure" key.
