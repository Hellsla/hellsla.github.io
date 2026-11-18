VERDICT: PASS
CONTENT-HASH: 7e098a62279429a4
Mode: delta

## Blocking
- none

## Polish
- content/en/FY8/fy8-16/exercises/solutions.md (L3-06 Answer) — "$4.2 \cdot 10^{2}\,\text{Mpc}$, about $416\,\text{Mpc}$" gives two precisions side by side; the two-figure reason (the limit $0.10\,c$) is right, so "about" could be dropped or the 416 kept only as the unrounded intermediate — optional.

## Checked
- Hash at start and end identical (7e098a62279429a4, `--exercises --lang en`).
- Figure `fy8-16/hubble-t`: lesson-answers `t2-H0` = 18000/250 = 72 km/s/Mpc; the line is drawn from the origin to (291.7 Mpc, 21 000 km/s), so it passes through the grid point (250, 18 000) as the tasks and the alt text say. A least-squares fit through the origin of the nine points T2 gives 72.4, so the drawn line is a fair fit. The alt text gives the grid point, so a reader who cannot see the figure has the same data. The figure does not give away either answer.
- L2-09 recomputed independently: z = 15.3/434.0 = 0.03525, v = 10 569 km/s, d = v/H0 = 146.8 Mpc. answers.py gives 146.791, exercises.json 146.8 Mpc, tolerance 2 %; the rounded 147 is 0.1 % off. The bracket check (120 Mpc / 8300 km/s and 160 Mpc / 11 900 km/s are T2 points) is correct.
- L2-09 conditions: z < 0.1, so v = cz is valid and the solution says so. Three significant figures fit Δλ = 15.3 nm.
- L3-06 recomputed independently: 0.10c = 29 980 km/s, d = 416.4 Mpc. answers.py gives 416.389; 420 is 0.9 % off and inside the tolerance.
- L3-06 reasoning: 416/285 ≈ 1.46 ("about 1.5 times"). The top of the figure, 21 000 km/s, is z = 0.070 < 0.10, so v = cz holds for every point. The extrapolation caveat follows the guardrail rule on extrapolation (it says how far and that the points do not show it).
- L3-06 c): "v = cz is an approximation for small z; z = 3 would give 3c" matches L3-05's wording and is correct for this level (C).
- Both solutions solve symbolically before substituting; units cancel correctly (km/s ÷ km/s/Mpc gives Mpc). The notation (z, λ0, H0, Hubble–Lemaître law) is the same as in the other tasks of the set.
- Scope: redshift and Hubble's law belong to "maailmankaikkeuden kehitys"; the data is invented and presented as model data, not as measured.
