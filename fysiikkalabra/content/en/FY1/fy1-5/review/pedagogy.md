VERDICT: FAIL
CONTENT-HASH: 4c6ae5f3a16b7571

## Blocking
- exit-ticket.json:3 — the only exit question is a unit conversion plus s = vt from the zero point (90 km/h, 20 min); it does not test the lesson's core idea (the position is proportional to time only when s0 = 0; the slope of the (t, s) graph is the speed). A student can pass it and still hold the doubling misconception — replace it with an item on the core idea, for example: "A trolley starts at 4 m and moves at 3 m/s. At 1 s it is at 7 m. Is it at 14 m at 2 s? Justify." (model answer: no, 10 m; only the distance 3 m doubles).

## Polish
- lesson.md:195-205 (worked example, Reasonableness) — one stage holds the estimate, the JPL comparison, the Earth-vs-Sun distance caveat and the model-precision verdict; this is more than one step and beyond FY1's goal (linear model). Keep the estimate in the stage; move the JPL comparison into a short closed box or into the optional explain task.
- lesson.md:178 — the unit-conversion stage writes `15.341 · (1/149 597 870.7) AU : (1/86 400 day)`, which a 17-year-old cannot follow. Write `v = 15.341 km/s · 86 400 s/day ÷ 149 597 870.7 km/AU = 0.0088602 AU/day`. Stage "Rearranged formula" (l.171) rearranges nothing; say "no rearranging is needed, s is already alone".
- inquiry.json (kertaus, l.245-253) — the recap uses the (s, t) axes with slope Δt:Δs, the inverse of the speed students will meet next; use a (t, s) graph so the retrieval matches the lesson. Option 3 of `virhe` (l.500) "Triple the time also triples the speed" is a strawman; rewrite as a plausible slip.
- inquiry.json:271-278 / koe-1 — experiment 1 only recomputes s = vt; its result is the formula, not an emergent result. Acceptable here, but the opening question ("what do you need to calculate Voyager's distance, what do you assume") is answered only in the optional `pohdi`; make the answer to the Miksi question explicit in the worked example or make `pohdi` non-optional. Voyager also appears in the hook, example, optional explain and Level 3, so repetition is high.
- Glossary: uniform motion, speed, position, distance and direct proportionality are still missing from glossary.json (0 hits); add them with definitions. Finnish text not in the packet; case after number+unit not judged.

## Checked
- Learning path follows fy1-4; slot goals (graphical and linear model, s = vt) covered.
- Predictions precede evidence; prediction 2 targets the real misconception; wrong-option feedback repairs it.
- Experiments lock s0 and v, vary t, min 3; sim at 390 px readable, controls labelled, nothing clipped (capture #29).
- Option correctness not concentrated in one speaker or place.
- Figures follow their paragraphs; captions explain; no paragraph over 120 words.
- Transfer task has three progressive hints and mistake feedback for 1092 and 270; solutions follow the seven steps.
- Common misconception section matches prediction 2 and the check items.
- Exercises not judged here.
