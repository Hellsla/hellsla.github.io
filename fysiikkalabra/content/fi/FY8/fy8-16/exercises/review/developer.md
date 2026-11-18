VERDICT: DONE

Added two figure tasks (kuvatehtävät), both on the safe figure fy8-16/hubble-t (no new figure, no figures.py change), in fi, en and fi-easy.

- lessons/FY8/fy8-16/answers.py: answers for fy8-16-L2-09 (146.79 Mpc) and fy8-16-L3-06 (416.39 Mpc), computed first.
- exercises/exercises.json (fi, en, fi-easy): L2-09 (level 2, core; Hγ 434.0 -> 449.3 nm: z, v, H0 read from the figure's grid point, distance d) and L3-06 (level 3; H0 from the figure, the distance where the line reaches 0.10 c, why the estimate is uncertain, why v = cz fails at large z). `unit` is "Mpc" in every language.
- exercises/solutions.md (fi, en, fi-easy): complete solutions with **Kuvaajan lukeminen**, one equation per row in Sijoitus, a Järkevyys check with its limits (z < 0.1, bracketing points, multiplication check, the 21 000 km/s axis top at z = 0.070 against 0.10 c).

Checks: lint_lesson 0 errors (word-count warnings on the two new solutions, like existing multipart ones); check_solutions ok; check_i18n 0 errors.
Not run: check_layout at 360 px (playwright is missing here), so the 360 px layout is unchecked. Note: fy8-16/hubble-t has "fi-easy: missing 1" in the figure catalog, which is the lesson's figures.json (not fixable here). Its H0 = 72 is also read in the inquiry check.
