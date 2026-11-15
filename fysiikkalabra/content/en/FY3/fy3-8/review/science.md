VERDICT: PASS
CONTENT-HASH: 97a72241efc3f371

## Blocking
- none

## Polish
- inquiry.json check-3 model — "about a hundred times" (3.4·10⁻³ / 3.6·10⁻⁵ ≈ 94): fine as an order of magnitude; "nearly a hundred times" would be exact.
- inquiry.json siirto reasonableness — "≈ 4 mm per kelvin … order of the scale of an ordinary thermometer": ordinary lab thermometers are nearer 1 mm/K; "same order of magnitude" holds, consider a softer wording.
- sim.js readout — decimal comma (10,0000 m) on the English page; language/visual, not physics.

## Checked
- Full review (changed line with a number/formula, proofreading round 1): hash equal at start and end.
- Mechanism: stronger vibration plus the asymmetric interaction (repulsion steep, attraction weakening gradually) raises the mean spacing; particles keep their size. Cem's symmetric-vibration distractor and its feedback are physically right; the model box states that the sim sets the spacing from the formula and does not show the asymmetry.
- Model conditions: l = l₀(1 + αΔT), ΔV = γV₀ΔT, γ ≈ 3α for small changes; valid for about 100 K for solids; liquid γ only near 20 °C; gases at constant pressure — matches the guardrails.
- Water anomaly (densest at about 4 °C, lake freezes from the surface, ice floats because water expands on freezing) — consistent in theory, misconception and check-1.
- Table values α (12, 23, 17, 9, 3.3) and γ (0.21, 1.1, 0.95, 3.4 ·10⁻³ 1/K at 20 °C) are standard.
- Recomputed in one script: pred-1 6.00/12.0 mm; pred-2 0.0600 %; olomuodot 0.36/2.1/11/34 cm³; worked example 86.4 mm and 0.072 %; virhe 1.8 mm vs 28 mm (×15, 0.7 %); siirto 44 mm, mistakes 0.044 and 110, glass ratio 41, corrected 43 mm; check-2 23·10⁻⁶ 1/K, mistakes 46 and 15.3; exit 21 mm; sim howto "< 0.3 %" (max 0.23 %).
- Worked example: ΔT as a difference (60 K), formula symbolic, 2 s.f. justified by α and ΔT, rough-estimate check real.
- Simulation: ΔL = αL₀(T − 20 °C), L = L₀ + ΔL, rel = αΔT, ×100 exaggeration labelled; chart lines match (aluminium at 10 m: +23/−13.8 mm); simState carries dT, dL, rel.
- Experiments: exp-1 locks material and L₀, varies T; exp-2 locks material and T, varies L₀ — each isolates its parameter, ranges reach the suggested values.
- Assessment: one correct option in every choice item; hole-expands item and shrink-fit statement correct.
