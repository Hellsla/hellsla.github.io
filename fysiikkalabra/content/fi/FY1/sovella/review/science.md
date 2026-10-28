VERDICT: FAIL
CONTENT-HASH: eaea0b645c267870

## Blocking
- content/fi/FY1/sovella/solutions.md:108–109, :115 and tasks.json:172 — (A, guardrail "Half the range") fy1-s2 b uses half the range "keskiarvon epävarmuuden varovaisena arviona" and reports $(2{,}37 \pm 0{,}08)\,\text{s}$ as the mean's uncertainty; the task text asks for "keskiarvo ja sen epävarmuus". The guardrails say half the range is a simple estimate of the scatter of single results and must never be called the uncertainty of the mean. — Reword the task to "keskiarvo ja arvioi tulosten epävarmuus", and the Periaate/Kysytty to "Vaihteluvälin puolikas on yksinkertainen arvio yksittäisten mittausten hajonnasta; käytetään sitä tässä yksinkertaisena, varovaisena epävarmuusarviona vertailussa". Keep the closing remark on the mean's own uncertainty (from the standard deviation) as the separate, more exact estimate.

## Polish
- solutions.md:115 — the "more exact" check compares the difference 0,03 s with each mean's uncertainty (0,031 s and 0,025 s); the fair comparison is with the uncertainty of the difference, about 0,04 s ("ero on sitä pienempi") — clearer and the conclusion is unchanged.
- fy1-s1 b has no `### Hyväksytään myös`: a slope from a regression line (0,800 m/s with t ≥ 0,4 s, 0,799 m/s with t ≥ 0,6 s) or from other two well-separated points of the line is equally correct; say so, since `graph_read` otherwise reads as one method only.

## Checked
- One Python run recomputed every number: floor speed 0,80 m/s (two line points) and 0,7998/0,7993 m/s (least squares from 0,4 s / 0,6 s), intercept −0,16 m, extrapolation 7,8 m at 10 s; means 2,37 s and 2,40 s, half ranges 0,08 s and 0,07 s, difference 0,03 s; standard errors 0,031 s and 0,025 s, difference uncertainty 0,040 s.
- The ramp data are physically consistent: uniform acceleration ≈ 2,0 m/s² gives 40 mm at 0,2 s and 160 mm and 0,80 m/s at 0,4 s, matching the 16 cm ramp end; the negative intercept is explained correctly.
- Fit guardrails: line fitted only to the floor points, slope read from two distant points on the line, extrapolation beyond 0,4–2,0 s questioned with a physical reason, no line forced through the origin.
- Display digits vs real precision (2,5 mm pixel) handled as the guardrail on resolution and uncertainty asks.
- fy1-s2 physics: same-size solid balls roll down in the same time independent of mass; the corrected data agree; the conclusion says the difference cannot be shown, not that the times are equal, and is limited to the studied conditions.
- First-report shortcomings (changed conditions, single runs, false precision vs hand timing, no uncertainty, overgeneralisation, vague question) are real and their fixes remove them.
- Points add up: 12, 15, 14; every criterion matches what its part asks and the solution shows.
- Data labelled as example data, not measurements; scope inside FY1.
- Hash identical at start and end.
