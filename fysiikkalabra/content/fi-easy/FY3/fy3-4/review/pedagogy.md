VERDICT: PASS
CONTENT-HASH: 377023ae1fb31127

## Blocking
(none)

## Polish
- inquiry.json check-c2 — it repeats pred-3 (same narrow tube and wide basin, same three options, 1,0 m instead of 2,0 m), so it tests recall of the theory, not transfer — change the situation (e.g. a vessel that widens upward, or a tilted tube; the pressure depends on vertical depth).
- inquiry.json pred-1, pred-2 — wrong-option feedback says "Mittauksesi näyttävät", but the correct option and the sim's own text say "mallin arvot". The house rule is that sim numbers are model values; also exp-1 and the explain prompt say "mittaustesi" — use "mallin arvojen" or "lukemiesi" throughout, so that criterion 4 of johtopäätös is coherent.
- sim, visible line "Jokainen syvyysmetri lisää painetta ρg · 1 m verran" — it is open under the sim before exp-1 asks for the increase per metre, so it names the quantity the student is to read from their data. Move it into Laskennan selitys (the number stays hidden, so this is only half a disclosure).
- inquiry.json hook — "Padon muuria ja tärykalvoasi kuormittaa sama asia: yläpuolella oleva vesi" gives the cause before the prediction. Ask what the load comes from, or drop the sentence.
- lesson.md "Tee pullon kylkeen reikiä usealle korkeudelle." — an imperative for something the student does not do; write "Jos pullon kylkeen tekisi reikiä usealle korkeudelle, alimmasta suihkuaisi vesi voimakkaimmin".

## Checked
- Learning path: prerequisites (G = mg, state variable pressure) are retrieved; the opening dam question is answered in "Ilmanpaine ja ylipaine"; scope matches the slot (p = p₀ + ρgh, constant term, force as a scalar because it is perpendicular to the surface).
- Prediction 1 can be refuted by exp-1 (a doubling of the total pressure is visible in the table); exp-1 locks ρ, varies h; the numeric task reads the slope from the student's data, with mistake feedback.
- Pred-3 has no experiment, but the theory derivation and the feedback address the misconception (the area cancels); wrong-option feedback repairs it. Speakers are not always right.
- Workload: the core path is 2 predictions plus 1 experiment, 1 explain, the example and the exercises; the extras are marked optional.
- The worked example is staged in seven steps, with the principle, the conversion, a reasonableness check and the diver comment. The figure captures (390 px) are legible.
- Simulation at 390 and 1280 px: picture, controls and readout are clear, and the explanations are behind Käyttöohje, Mallin oletukset and Laskennan selitys. The 1280 px layout has the sim beside the experiments.
- Exit ticket: the pin item tests p = F/A; the second item tests ρgh against the total pressure. Both are solved with a model answer.
- Finnish: the glossary terms are used, the case after number+unit is correct, and "hydrostaattinen paine :: p = p₀ + ρgh" is the approved exception and is not reported.
- The exercises are not in this packet and were not judged. The content hash is the same at the end of the review.
