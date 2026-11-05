VERDICT: PASS
CONTENT-HASH: 78c57d65fbb8f279

## Delta review (2026-11-04)
Only change since round 3 (`git diff HEAD`, the only modified file under content/en/units/fy9-sahkokentta and nothing under lessons/units/fy9-sahkokentta): sovella/tasks.json s1 b) rubric `calculation` detail, where the long inline $q = 0.080\,\text{m}\cdot\sqrt{\dfrac{4.93\cdot10^{-4}\,\text{N}}{8.988\cdot10^{9}\,\ldots}}$ is split into $F_\text{s} = 4.93\cdot10^{-4}\,\text{N}$ and $k = 8.988\cdot10^{9}\,\text{N·m}^2/\text{C}^2$, so $q = 0.080\,\text{m}\cdot\sqrt{F_\text{s}/k} \approx 1.87\cdot10^{-8}\,\text{C}$. It mirrors the fi source line exactly (check_i18n en: 0 errors). The criterion still asks for substituted values with units and a correct calculation; 1 point unchanged, task total 95 points (practice.py check). Naming $F_\text{s}$ and $k$ first reads more clearly for a student marking their own work. No new findings.

Pedagogy review, round 3, of the en translation of fy9-sahkokentta. 2026-11-04.

No Blocking findings in rounds 1–2 in this role. Structure unchanged from the source: 6 diagnostic choices, 1 interpret, theory, 4 choice + 4 numeric Apply items with hints, mistakes and solutions, 3 Check items, a 2-question exit ticket, 6 tasks (95 points). The concept map the student reads in the Theory summary now has English branch headings (charge and force, field and potential, capacitor, components and safety), so the summary is fully readable in English. Nothing regressed.

## Blocking
None.

## Polish
1. Coordinates in s3 c) criteria[0] and solutions.md s3 still use the Finnish semicolon "(0.20; 93)"; formulas must match the source for check_i18n, so no action required.
