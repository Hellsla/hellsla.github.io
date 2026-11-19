VERDICT: PASS
CONTENT-HASH: 40c234e16b882e67

## Blocking
(none)

## Polish
1. inquiry.json `koe-1`/`ennuste-1` — Prediction 1 is about the shape of the graph, but the experiment evidence is a table of s and the quotient s : t. The intro's "Also look at how the graph is drawn" asks for no action, and the sim's slope triangle (Δs : Δt = v) is never used by a task before the theory. Fix: add one step to koe-1/koe-2 ("at t = 6 s read the slope triangle and compare it with v") or a question line tying the constant s : t to the line through the origin.
2. exit-ticket.json item 2 — uses x and x₀ while the whole lesson uses s and s₀. Fix: "The position is $s = s_0 + vt = ...$".
3. lesson.md "Formula: Uniform motion" last sentence, and the sim `model` text — "velocity" appears undefined in FY1 where only speed is taught. Fix: "so the speed is taken as positive" or drop the clause.
4. lesson.md Worked example, "Unit conversions" stage — the single chain `15.341 · 1/149 597 870.7 AU : (1/86 400 day)` is hard for a first-year student to follow. Fix: two lines: 15.341 km/s · 86 400 s/day = 1 325 462 km/day, then ÷ 149 597 870.7 km/AU = 0.0088602 AU/day. The "Reasonableness" stage also holds four paragraphs (the JPL comparison and the Earth-orbit note); move the comparison to its own paragraph block after the stages, or trim.
5. Workload: Etsi virhe (`virhe`) and the transfer task (`siirto`) are not optional although the core-path rule makes them optional, and Pohdi/kertaus/tarkistus-3 are. With 2 predictions, 2 experiments, 3 mandatory checks, 20 exercises and the exit ticket, the lesson is heavy. Fix: mark `virhe` optional, since check-c2 and tarkistus-1 already test the same misconception, or keep `siirto` and drop `virhe`.

## Checked
- Learning path: prerequisites (line fitting, slope, intercept from fy1-4) are enough. The hero "Why" and hook question are answered by the model and the worked example, with no answer shown before the student commits.
- Slot goals (graphical and linear model, direct proportionality s = vt) are covered. Forces, acceleration and vectors are not introduced.
- Predictions come before the evidence. Option feedback repairs the misconceptions: s doubles with t when s0 ≠ 0, and horizontal line means speed. Reveal is gated on koe-1/koe-2 with min 3. The "model values" wording is consistent.
- Worked example arithmetic verified: 2922 days, 0.0088602 AU/day, 25.89 AU, 144.9 AU, and the February 2026 model value 142.6 AU (2659 days). Seven stages, one step each; the reasonableness check is sound.
- virhe (5 + 18 = 23 m), siirto (390 m; mistakes 1092 and 270) and tarkistus-2 (s0 = 4.0 m) are correct. Hints are progressive and the solutions follow the seven-step pattern.
- Exit ticket tests the core idea (unit conversion; distance doubles, position does not) and neither repeats the worked example.
- Figures sit beside the paragraphs they explain; captions and aria-labels are informative. The photo caption honestly says it does not show uniform motion.
- Terminology position vs distance is consistent in the lesson text, and the Common misconception section is precise.
- Exercises were not judged (reviewed separately). Phone captures were not opened; the packet lists no layout problems.
