VERDICT: PASS
CONTENT-HASH: 51ef54c541fe6381

Science review, round 3, of the en translation of fy9-sahkokentta (source content/fi/units/fy9-sahkokentta/, passed). 2026-11-04.

Since round 2 only the figure translation changed: scripts/figlib.translate() now covers \textbf{}, and the en figures were regenerated. The only change in the figure SVGs is the four concept-map branch headings (now "charge and force", "field and potential", "capacitor", "components and safety"); no number, formula or answer changed. check_i18n.py: en 0 errors; units.py check: 77 units ok; practice.py check: en fy9-sahkokentta 6 tasks, 95 points. The round-1/2 recomputations (7264 km/s, 35.95 µN, 6.008 pN, 1690 V, 3.865 h, 112.6 mJ, s1–s6) still apply. Figures checked at 390 and 1280 px: values and units match the source (e.g. spark figure U ≈ 9 kV, Q ≈ 0.9 µC, W ≈ 4 mJ; plates 0–200 V; s3-lin k ≈ 354 pF·mm, intercept 22 pF).

## Blocking
None.

## Polish
1. inquiry.json activities[7] solution, Conversions: `$\sqrt{1\,\text{J} : 1\,\text{kg}}$` keeps the Finnish colon for division; "/" would be usual in English. It is a formula compared with the source by check_i18n; no action required.
2. $F_\text{s}$ keeps the Finnish subscript because formulas must match the source; acceptable.
