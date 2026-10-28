VERDICT: PASS
CONTENT-HASH: 78a3de66670c03ad

Round 3, full: main (physics audit) merged with the sim LaTeX pass; vs main only pred-3's reveal (after theory, min 1) and exp-1's intro ("Testaa ennuste 1") changed in inquiry.json.

## Blocking

## Polish
- content/fi/FY3/fy3-8/inquiry.json pred-3 (Aino feedback) — still cites the sim's own assumption ("mikromalli olettaa … ja silti hila laajenee") as if it were evidence; the spacing is set from the formula — lean on the theory now that pred-3 is revealed after it ("Teoriatiivistelmän mikromallissa hiukkaset pysyvät samankokoisina; kasvaa vain niiden keskimääräinen etäisyys").
- content/fi/FY3/fy3-8/lesson.md figure "particles" — amplitude arrows symmetric about each particle while the paragraph above explains the asymmetry — a longer outward than inward arrow on the warm row, or "keskimääräinen etäisyys kasvaa" in the caption.
- lessons/FY3/fy3-8/sim.js readout — axis range renders "−20–30 mm" (en dash after a negative number) — write "−20 mm … 30 mm".
- content/fi/FY3/fy3-8/inquiry.json johtopaatos model — "6,0 mm" beside "12,0 mm" and the feedbacks' "6,00 mm" — use 6,00 mm.
- lessons/FY3/fy3-8/sim.js — `fi` unused — delete it.

## Checked
- One script recomputed every number: example 0,0864 m ≈ 86 mm, 0,072 %, estimate 60 mm; pred-1/pred-2 6,00 / 12,0 mm, 0,0600 %; olomuodot 0,36 / 2,1 / 11 / 34 cm³; virhe 27,9 vs 1,84 mm (×15, 0,7 %); siirto 44 mm, mistakes 0,044 and 110, with glass 42,9 mm, γ ratio ≈ 41; check-2 α = 23 (both columns), mistakes 46 and 15,3; air/steel ≈ 94; exit ticket 21 mm. All match.
- Definitions and mechanism: vibration grows, mean spacing grows through the asymmetric interaction, particles keep their size; temperature in prior matches the guardrail (gas: mean kinetic energy).
- Conditions stated where used: ΔL formula for solids up to about 100 K, liquid γ only near 20 °C, gas γ at constant pressure, γ ≈ 3α for small changes (guardrail met).
- pred-3 revealed after theory, whose Ydinajatus gives the asymmetry argument; Bea alone correct, Cem/Aino/Daniel feedback right.
- exp-1 tests only pred-1: locks material, L₀, varies T, measures dT, dL (in simState); exp-2 locks material, T, varies L₀, measures dL, rel (in simState).
- Sim: ΔL = αL₀ΔT from 20 °C, amplitude ∝ √T (K), ×100 exaggeration stated on canvas, max real change 0,23 % < 0,3 % in howto; model box says it shows *that*, not *why*. KaTeX canvas labels and readout render correctly (1280 and 390 px captures), values agree with the feedback.
- Water 0–4 °C anomaly, hole grows, bridge comb joint closes in summer (hook and hero), check-1/check-c2 single correct options.
- Scope inside FY3 "lämpölaajeneminen"; hash identical at start and end.
