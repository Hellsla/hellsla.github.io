VERDICT: PASS
CONTENT-HASH: 7bb6d77c69feb453

## Blocking

## Polish
- solutions.md:253 (L2-10 Part c) — "the same particles produce northern lights" is a simplification (C): the ground disturbance comes from currents in the upper atmosphere that strengthen when particles precipitate — "the particles that rush into the upper atmosphere at the same time produce northern lights" would be exact (same remark as on the Finnish set).
- solutions.md:256 (L2-10 Reasonableness) — "changes in a minute by at most $36\,\text{nT}$" holds because R sums absolute changes of the three components; one clause could say so.

## Checked
- Delta round 1: only fy7-2-L2-10 (FY7-A5) judged; hash identical at start and end.
- Recomputed from the task text with my own formulas: $r = mv/(|q|B) = 83.55\,\text{m} \to 84\,\text{m}$ (two figures from 4.0 and 50; tolerance 2 % covers it), $r/R_\text{E} = 1.3 \cdot 10^{-5}$, hundredfold weaker field 8.4 km, $810/1350 = 0.60\,\text{nT/s}$, 36 nT per minute = 0.072 % of 50 000 nT. answers.py agrees.
- English against Finnish by script: answer 84, unit m, tolerance 0.02, kind, the eight table rows and every number of the task text and the solution are the same (the only extra number is "24 hours" for "vuorokausi").
- Example table: lower threshold 200 exceeded 20–0 (five hours), upper 400 exceeded 21–23 (three), maximum 810 at 22. Marked invented.
- Both source pages fetched 16 Nov 2026 (HTTP 200). The aurora page has the chart title "Magneettinen aktiivisuus kuluneen vuorokauden aikana", station-specific thresholds, the link to the guide and the review of 16.11. 9.23 (quiet weekend, solar wind strengthening Monday and Tuesday). The guide has: R describes the speed of field variations; divide by 1350 for nT/s; both thresholds about 50 % (faint; bright or extensive); statistical link, never a sure sign, short exceedances without auroras, several consecutive bars a better sign; cloudiness not included; probability grows northwards; auroral zone a ring round the magnetic pole, Lapland in it; solar wind a particle stream that produces auroras, 300–400 km/s. Every claim the English task and solution attribute to the source is there; the solution's own additions are marked as its own.
- Physics of b): force perpendicular to $\overline{v}$ and $\overline{B}$, no work, motion along the field unaffected, helical path; uniform-field assumption and the magnetosphere simplification stated.
- Scope: charged particle in a magnetic field (FY7).
