VERDICT: PASS
CONTENT-HASH: 5b1dbbf676a79d5e

## Blocking

## Polish
- lesson.md "A wave is a travelling disturbance" paragraph (about 190 words) and "The speed depends on the medium..." (about 200 words) exceed the ~120-word rule and mix several ideas (ideal model, gas thermal motion, water waves; non-dispersive rope/air, dispersion, tsunami). Split them, and consider moving the water-wave, dispersion and tsunami asides out of the core text (beyond the FY5 clarification, which names only v = fλ and the two wave types).
- inquiry.json koe-2/koe-3: the readout already shows v and λ for the chosen settings, so the experiments partly confirm the sim's own formula. The ruler check of λ in koe-2 is what makes it empirical; say so in the intro ("measure λ with the ruler first, then compare with the readout").
- inquiry.json "ennuste-1" option 4 feedback refers to "the experiment with the spring". It is shown only after koe-1, which is fine, but the prediction's own prompt never mentions longitudinal waves. Add one clause to the prompt so the reopened prediction reads naturally.
- inquiry.json "virhe": the prompt says "the frequency is 2.0 Hz" as given, yet option 3 suggests reading frequency from the graph. The item works, but the statement should say where the student got 2.0 Hz (e.g. "from the same graph") so the error is clearly only the reading of 0.50.
- The pulse (Source menu) is not used in any experiment or check, although theory introduces it. Optional: one line in koe-1 asking to try the pulse.

## Checked
- Hash taken with --lang en; unchanged at start and end.
- Path: prior (period, frequency, amplitude) is retrieved by kertaus; the Miksi/hook question is answered in the conclusion and reflection; slot goals (origin and propagation, transverse/longitudinal, v = fλ) covered, reflection correctly deferred to the next chapter.
- Predictions are committed before evidence and each can be refuted; every wrong option's feedback names the misconception and the model value that refutes it. Prediction 2 was checked against the sim's two speeds.
- Experiments lock the right variables, vary one at a time and measure what the conclusion needs. The explain criteria are observable and match the prompt.
- Tarkista: concept checks use real misconception distractors (frequency/speed/wavelength at a boundary; transverse/longitudinal; molecule travelling). Task 2 uses figure fy5-10/valokuva: it is needed to answer, legible at 390 px, its description gives the crest positions without marking λ, and the theory figure "graphs" is a different wave.
- Worked example: seven stages, one step each; the symbolic form comes before the substitution; the example differs from the transfer task.
- Phone captures: simulation at 390 px has a readable canvas, controls and readout, with text behind the three boxes; the types figure is legible.
- Exit ticket tests the core idea (energy not matter; λ at a changed f).
- Not judged: exercises (reviewed apart).
