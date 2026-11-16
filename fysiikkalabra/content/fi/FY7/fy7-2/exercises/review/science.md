VERDICT: PASS
CONTENT-HASH: c4a62c74b27e255e

## Blocking

## Polish
- solutions.md:253 (L2-10 Kohta c) — "samat hiukkaset synnyttävät revontulia" is a simplification (C): the ground disturbance comes from currents in the upper atmosphere that strengthen when particles precipitate, not literally from the same particles — "samaan aikaan yläilmakehään syöksyvät hiukkaset synnyttävät revontulia" would be exact.
- solutions.md:244 (L2-10 Järkevyys) — "kenttä muuttuu minuutissa enintään 36 nT" holds because R sums the absolute changes of the three components; one clause could say that R is a mean of absolute changes, so the net change is usually smaller.

## Checked
- Delta round 1: only fy7-2-L2-10 (FY7-A5) judged; hash identical at start and end.
- Recomputed from the task text: $r = mv/(|q|B) = 83{,}55\,\text{m} \to 84\,\text{m}$ (two significant figures from 4,0 and 50; tolerance 2 % covers it), $r/R_\text{M} = 1{,}3 \cdot 10^{-5}$, hundredfold weaker field 8,4 km, $810/1350 = 0{,}60\,\text{nT/s}$, 36 nT per minute = 0,072 % of 50 000 nT. answers.py agrees.
- Example table: lower threshold 200 exceeded 20–0 (five hours), upper 400 exceeded 21–23 (three), maximum 810 at 22; the solution reads it correctly. The table and the thresholds are marked invented in the task, the caption and the solution.
- Source pages fetched 16 Nov 2026 (both HTTP 200). The aurora page has the chart title "Magneettinen aktiivisuus kuluneen vuorokauden aikana", station-specific thresholds, the link to the interpretation guide, and the dated review (16.11. 9.23: quiet weekend, solar wind strengthening Monday and Tuesday). The guide has: R describes the speed of field variations; divide by 1350 for nT/s; lower and upper threshold about 50 % for faint and for bright or wide auroras; statistical link, never a certain sign, short crossings without auroras, several consecutive bars a better sign; cloudiness not included; probability grows northwards; auroral zone a ring round the magnetic pole, Lapland in it; solar wind a particle stream that causes auroras, typical speed 300–400 km/s. Every claim the task and the solution attribute to the source is there; the solution's own additions are marked as its own.
- Physics of b): force perpendicular to $\overline{v}$ and $\overline{B}$, no work, motion along the field unaffected, helical path along field lines; the uniform-field assumption and the simplification (solar wind does not enter the atmosphere directly) are stated.
- Scope: charged particle in a magnetic field (FY7), field of a current (later chapter named); notation as in the brief.
