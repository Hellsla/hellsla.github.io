VERDICT: PASS
CONTENT-HASH: 78c57d65fbb8f279

## Delta review (2026-11-04)
Only change since round 3 (`git diff HEAD`, the only modified file under content/en/units/fy9-sahkokentta and nothing under lessons/units/fy9-sahkokentta): sovella/tasks.json s1 b) rubric `calculation` detail, where the long inline $q = 0.080\,\text{m}\cdot\sqrt{\dfrac{4.93\cdot10^{-4}\,\text{N}}{8.988\cdot10^{9}\,\ldots}}$ is split into $F_\text{s} = 4.93\cdot10^{-4}\,\text{N}$ and $k = 8.988\cdot10^{9}\,\text{N·m}^2/\text{C}^2$, so $q = 0.080\,\text{m}\cdot\sqrt{F_\text{s}/k} \approx 1.87\cdot10^{-8}\,\text{C}$. It mirrors the fi source line exactly (check_i18n en: 0 errors). Recomputed: 0.080·sqrt(4.93e-4/8.988e9) = 1.874·10⁻⁸ C, n = q/e = 1.17·10¹¹ ≈ 1.2·10¹¹; same values, units and model as before. practice.py check: en 6 tasks, 95 points. No new findings.

Science review, round 3, of the en translation of fy9-sahkokentta (source content/fi/units/fy9-sahkokentta/, passed). 2026-11-04.

Since round 2 only the figure translation changed: scripts/figlib.translate() now covers \textbf{}, and the en figures were regenerated. The only change in the figure SVGs is the four concept-map branch headings (now "charge and force", "field and potential", "capacitor", "components and safety"); no number, formula or answer changed. check_i18n.py: en 0 errors; units.py check: 77 units ok; practice.py check: en fy9-sahkokentta 6 tasks, 95 points. The round-1/2 recomputations (7264 km/s, 35.95 µN, 6.008 pN, 1690 V, 3.865 h, 112.6 mJ, s1–s6) still apply. Figures checked at 390 and 1280 px: values and units match the source (e.g. spark figure U ≈ 9 kV, Q ≈ 0.9 µC, W ≈ 4 mJ; plates 0–200 V; s3-lin k ≈ 354 pF·mm, intercept 22 pF).

## Blocking
None.

## Polish
1. inquiry.json activities[7] solution, Conversions: `$\sqrt{1\,\text{J} : 1\,\text{kg}}$` keeps the Finnish colon for division; "/" would be usual in English. It is a formula compared with the source by check_i18n; no action required.
2. $F_\text{s}$ keeps the Finnish subscript because formulas must match the source; acceptable.
