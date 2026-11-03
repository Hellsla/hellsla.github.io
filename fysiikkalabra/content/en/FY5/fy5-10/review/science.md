VERDICT: PASS
CONTENT-HASH: cc19a9584475020b

## Blocking

## Polish
- lesson.md, inquiry.json, solutions — "the fundamental equation of wave motion" is a calque of *aaltoliikkeen perusyhtälö*; English textbooks say "the wave equation" or "wave speed equation". Not wrong, and used consistently in every file, so left as is.

## Checked
- Translation review of the English lesson against the Finnish chapter *Mekaaninen aaltoliike* (three PASS reviews): lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json, sim labels `sims.fy5-10` in lang/en.json.
- Every number in lesson.md, inquiry.json and exit-ticket.json matches the Finnish with a decimal point (script comparison: no number added or lost); formulas, conditions ("small amplitude", "in the same medium", frequency kept at a boundary, model assumptions and `calc` of the sim) identical in meaning.
- Physics terms: transverse/longitudinal wave, compression/rarefaction, crest/trough, period, frequency, amplitude, wavelength, medium, displacement, equilibrium position; snapshot = (x, y) graph, graph of one point = (t, y) graph. Energy-not-matter, thermal motion of gas molecules, speed set by the medium and frequency by the source all kept.
- Every prediction keeps its correct option and every feedback its physics; experiment set-ups (initial, locked, vary) unchanged; fixed Finnish left in the experiment strings (`names.aalto` "aalto", `values.aalto.poik` "poikittainen", koe-3 tension "suuri"/"pieni") to wave/transverse/high/low; "What is conserved?" → "What stays the same?" (frequency is not a conserved quantity in the physics sense).
- Worked example: seven stages, symbolic first, 0.80 m with two significant figures.
