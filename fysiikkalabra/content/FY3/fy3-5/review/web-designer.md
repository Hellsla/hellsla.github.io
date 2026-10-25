VERDICT: PASS
CONTENT-HASH: cf54311aa7720cb5
## Blocking
(none)
## Polish
- lesson.md:19 — SVG text renders at 13,1 px (390) and 12,0 px (360), above the 10 px floor but on the small side; if the figure is touched again, raise font-size from 22 to 26 so the phone size stays >= 14 px.
- site.css (template-wide, needs human OK) — measured lines at 1280 px are 63–81 characters, mean 74 (target 60–75); a slightly narrower max-width would keep the longest lines inside.
## Checked
- Lint 0 errors/0 warnings; build ok (`build.py --all`); preview/fy3-5.html measured at 1280, 390, 360 px (on a private copy, since concurrent builds remove preview files).
- No horizontal overflow at any width, closed or with every `<details>` open (scrollWidth = clientWidth); 0 KaTeX display blocks wider than their box.
- Re-checked after the template change: no "X = value" in the opened solutions breaks between "=" and the value at 1280, 390 or 360 px (0 splits; round-1 polish fixed).
- Nav has no Simulaatio tab (Teoria / Tehtävät / Lähtölippu); no link, summary, input or button under 40 px in height or width.
- Negative answers print with the true minus U+2212 (−8,4 kJ, −500 J, −70 J, −15 J, −18 J); no hyphen-minus answers remain.
- Answer field at 360 px: "-8,4" and "−8,4" accepted, "8,4" rejected with message; input, unit and button fit in one row.
- SVG: 608/358/328 px wide, all text inside the viewBox; the moved label "Q < 0 tai W < 0" (x 414–572, y 117–144) is clear of the arrow, "ulos" and the box; uses currentColor.
- Opened solutions (3): 15,2 px (1280), 14,7 px (390/360), no horizontal scroll.
- Body text 17 px; about 41 (390 px) and 37 (360 px) characters per line on average.
- Screenshots: review/fy3-5-wd2-*.png (git-ignored).
