VERDICT: PASS
CONTENT-HASH: da441494f5b9baaf

## Blocking

## Polish
- exercises/solutions.md:115 (L3-03) — "travels through space and almost the whole atmosphere at the speed of light, steadily" reads awkwardly; "travels at a constant speed, the speed of light, through space and almost all of the atmosphere".

## Checked
- All 12 answers recomputed in one script with my own formulas (c = fλ, λ_max T = b, s = ct/2) and agree with exercises.json to 1e-4: 3.1915 m, 12.2449 cm, 9.4397 µm, 9993 K, 563.91 THz, 4.0075 µm, 2415 K, 4.8264 µm, 5796 K, 1.0633 mm, 89.1 °C, 384000 km.
- Every number, unit, tolerance and the figure id are identical to the passed Finnish set; the en task texts keep each black-body assumption and the asked unit.
- Solutions: principle, symbolic solution before substitution, conversions (°C → K, nm/µm/mm, THz), rounding reasons and reasonableness checks translated faithfully.
- L2-02 figure: peak of the 2415 K curve on the 1.2 µm gridline (height ≈ 1.06 MW/(m²·µm)); the English description gives the same information without the answer.
- L3-01: 1.063 mm falls in the microwave band 1 mm–1 m as the lesson's table states.
- Note (tooling, not a finding): the packet's "Exercise brief" block is empty for en (the extractor looks for the Finnish section names); I judged against the en lesson's Formula, Worked example, Misconception and Summary.
