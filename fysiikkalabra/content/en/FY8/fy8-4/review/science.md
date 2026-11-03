VERDICT: PASS
CONTENT-HASH: 6d3ece49d7b0afcf

## Blocking

## Polish
- inquiry.json:activities[5–6] values `reitti/ei` = "not measured", while the sim's select shows "no" (sim-390 screenshot) — the same state under two names; harmless — optionally align the label with the sim.

## Checked
- Line-aligned comparison with content/fi (lesson.md 1139 lines, inquiry.json, exit-ticket.json): every number and every formula identical after the decimal-comma → point change; the only numeric differences are SVG label x-coordinates for the English label widths.
- Every non-text value in inquiry.json and exit-ticket.json (correct flags, numeric answers, tolerances, mistake values, initial/locked/vary, measure keys) identical to the Finnish source.
- Theory sections (double slit, probability, duality, four models, p = E/c = h/λ, Compton hf = hf' + E_k with vector momentum, N/t = P/hf) translated faithfully, no condition lost (no rest mass, "in a vacuum", "almost free electron", "on average less than one photon").
- Worked example recomputed: hf = 3.138e-19 J, N/t = 3.187e5 1/s, d = 940.8 m, 1.2 m : 940.8 m = 0.0013; rounding reasons kept.
- Compton table recomputed with Δλ = h/(m_e c)(1 − cos θ): 0.0718, 0.0735, 0.0752, 0.0760 nm.
- tarkistus-2 794.9 eV, mistake 516 700 eV (hc/Δλ), siirto 290.5 µN, absorbing case 145.3 µN, no-area 9.08 µN, virhe 1.27e-36 vs 1.27e-27 kg·m/s: all recomputed and match.
- Predictions: exactly one correct option each, distractor feedback physics unchanged (43/1000 vs 3/1000, path measurement removes interference).
- Sim howto/model/calc texts match the source (I(x) formula, s = 2.0 mm, a = 10 mm, dark fringes at ±1.0, ±3.0 mm); sim UI is localised (decimal point, English button names agree with howto).
- Number words: "thousands of trillions" (3e15) and "a billionth" (factor 1e9) are correct short-scale renderings.
