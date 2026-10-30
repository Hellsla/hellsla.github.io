VERDICT: PASS
CONTENT-HASH: e34507e30a372cc0

## Blocking
(none left)

## Fixed
- solutions.md fy4-s2: "Yleisiä virheitä" and "Hyväksytään myös" were in the opposite order to the Finnish; reordered to match (content unchanged).

## Polish
- none

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): compared tasks.json (intro, all 3 tasks, source notes, every part text, rubric criterion and detail, links), solutions.md (every part of fy4-s1, fy4-s2, fy4-s3, Yleisiä virheitä, Hyväksytään myös) and figures.json line by line with content/fi/FY4/sovella.
- Physics matches line by line: slopes 0.39 / 0.245 m/s², μ = (g sin α − a)/(g cos α) = 0.030 / 0.045, ±0.002 vs difference 0.015 and the direction of the air-resistance bias; 17.2 m/s ≈ 62 km/h, E_p 9123 J, E_k 3889 J, F_res 29 N, 5234 J, 13 979 J → 13.6 ≈ 14 m/s with the two-figure reason and the 29 N / 5220 J alternative; v' 7.86 m/s, v_B 13.6 m/s ≈ 49 km/h, F_avg 4455 N ≈ 6.7 × weight, friction impulse ≤ 2600 N·s (11 %).
- Terms right: weight, normal force, kinetic friction, air resistance, work–energy principle, impulse, free-body diagram; F_\text{res} for F_vast and F_\text{avg} for F_ka (\text{} only, formulas identical to the Finnish); decimal points everywhere, also in LaTeX; \overline{G}, \overline{N}, \overline{F}_\mu kept.
- Figures: labels situation / forces / before / after / "wax A: ", alt texts complete; practice.py figures --check up to date; check_layout at 345 and 360 px OK; practice.py check OK; check_i18n en 0 errors; check_latex OK.
