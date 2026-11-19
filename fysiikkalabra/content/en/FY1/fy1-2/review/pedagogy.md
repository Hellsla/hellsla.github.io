VERDICT: PASS
CONTENT-HASH: e7465931349db26a

## Blocking
(none)

## Polish
1. inquiry.json `merkitsevat` (optional: true) and `virhe` (optional: true) — significant figures and square-unit conversion are slot goals, but the only core-path item on rounding is check 1, which counts digits. No core task makes the student round a product, and numeric answers are graded by tolerance, which does not enforce figures. Fix: make `merkitsevat` core (and keep `virhe` optional only if the exercises cover square units). Its numbers (Neptune, 30.1 AU) also repeat the worked example; use another planet.
2. inquiry.json `ennuste-1`, `ennuste-2`, `koe-1`, `check-c2` — the lesson's evidence is almost all "t = s/c, time proportional to distance", tested four times. The experiments read a calculator the student could run by hand, and nothing investigated prefixes or conversion itself. Fix: drop one prediction (core path allows 1-2) and let one experiment ask the student to convert first, then compare with the readout. Retitle "Prediction 2: a probe farther away": its prompt has no probe.
3. inquiry.json `voyager-malli` question — the correct option is much longer and hedged ("may differ slightly…"), so it is guessable by length. Its feedback also adds the Earth-versus-Sun JPL comparison, too heavy for a 17-year-old. Fix: equalise the option lengths and move the comparison into a short source note. The brief gives 119,7 AU at the heliopause crossing, the lesson 119.0 AU (Burlaga); confirm which is intended.
4. lesson.md "Significant figures" — about 150 words in two paragraphs, over the 120-word limit, mixing counting, the trailing-zero ambiguity, the whole-number convention and the multiplication rule. "Whole number ending in zeros … is exact" is wider than the house rule (trailing zeros of a rated value are significant, and context decides). Fix: split into two subsections and narrow the convention to "a time span or count the task sets". In "A unit for every scale", femtometre appears without having been introduced; add it to the prefix figure or the text.
5. Exercises and sim wording — "Answer in the unit AU/a": "a" for year was never introduced, so write "AU per year" or define it. The sim capture (#2) shows English text with decimal commas and a 19.11.2026 date next to a 11/19/2026 field, and two near-identical closed boxes ("Assumptions of the model and explanation" and "Assumptions of the model"). Fix: use the English formats and remove the duplicate box.

## Checked
- Opening question is not answered before the prediction; the hook, the conclusion's model answer and the three-unit table fit together.
- Prerequisite retrieval (powers of ten) matches fy1-1 and gives repairing feedback.
- Prediction and experiment values (142.2 AU, 19.7 h, 33.4/334/3340 s) match the model; the feedback names the evidence.
- Worked example: seven stages, symbolic first, units cancelled, reasonableness check; stage text is short.
- `virhe` (square kilometre) targets the real misconception, and each option repairs a distinct mistake.
- The `siirto` hints are progressive and its mistake values (484000000, 3236) are plausible; the solution has all seven parts.
- Exit ticket tests quantity versus unit and prefix conversion, the core idea.
- Figures (hero, quantity, prefixes, conversion) sit right after their paragraphs and are legible at 390 px.
- Checks cover concept, calculation and explanation with criteria.
- Options carry no letter or position references, and no speaker is right most of the time.
