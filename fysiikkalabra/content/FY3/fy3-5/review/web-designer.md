VERDICT: PASS
CONTENT-HASH: 87f4767f5cf84869
## Blocking
(none)
## Polish
- templates (answer `<details class="answer">`) — negative answers print with a hyphen-minus ("-8,4 kJ", "-500 J", "-70 J", "-15 J", "-18 J") while solutions.md and the prose use the true minus "−" — render the answer with U+2212 in the template (not a lesson edit; needs human OK).
- solutions.md:74 — "s = 0,15 m" breaks across lines at 360/390 px ("s =" / "0,15 m") — use a no-break space inside "s = 0,15 m" (the same may happen with other "X = value" in solutions).
- lesson.md:19 — SVG labels render at 13,1 px (390) and 12,0 px (360), fine but near the floor; if the diagram is touched again, raise font-size to 24–26 so the phone size stays >= 14 px.
- site.css (template-wide, not this lesson) — desktop text column is 70–79 characters per line at 1280 px (mean ~73), just over the 60–75 target; narrowing max-width a little would bring the first lines inside.
## Checked
- Build ok (`build.py --all`), lint 0 errors/0 warnings; preview/fy3-5.html measured at 1280, 390 and 360 px.
- No horizontal overflow at any width, closed or with every `<details>` opened (scrollWidth = clientWidth); no KaTeX block wider than its box.
- Nav has no Simulaatio tab or #sim section (Teoria / Tehtävät / Lähtölippu only); all nav links and buttons >= 40 px tall.
- Inline SVG energy diagram: scales to the column (608/358/328 px wide), no text clipped or overlapping, arrowheads and the "Q < 0 tai W < 0" label inside the viewBox, uses currentColor so it follows the text colour.
- Body text 18,4 px; text column 32 (390 px) and 29 (360 px) characters per line, 70-79 at 1280 px.
- Opened solutions (3 shown: L1-01, first of L2, first of L3): 14,7 px, no horizontal scroll at 360/390; the negative result "Q = −18 J" and "ΔU = 0" read clearly with the true minus.
- Answer field with negatives: "-8,4" and "−8,4" both accepted, "8,4" rejected with the message and the answer opened below; input, unit and button fit at 360 px.
- Screenshots in review/ (fy3-5-wd-*.png, git-ignored).
