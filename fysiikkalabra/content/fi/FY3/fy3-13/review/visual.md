VERDICT: FAIL
CONTENT-HASH: 37a5fe9968b14bfe

## Blocking
- [Major] lesson.md:214 (Esimerkki table) and inquiry.json:100 (Tutki table) — table headers `θ (°C)` and `p (kPa)` are plain text; built HTML has `<th>θ (°C)</th><th>p (kPa)</th>` in a sans face beside KaTeX italic θ and p in the prose. Same in Tutki prose: "alkaa arvosta 95 kPa" (number with unit not in maths) — house rule §1: a plain-text symbol anywhere the student looks is blocking — fix: `| $\theta$ (°C) | $p$ (kPa) |` as fy3-3 does, and `$95\,\text{kPa}$`.

## Polish
- [Minor] Esimerkki Järkevyys, exercise solutions — "101/0,37", "98/0,36" use a slash for a written division; the house rule is a colon (or a fraction) — write `101 : 0{,}37`.
- [Minor] Esimerkki, "Ääriviivoille" — inline `\tfrac{100{,}1}{0{,}387}` renders tiny at 390 px; set as a short aligned block like the Sijoitus rows.
- [Minor] Ennusta/Tarkista — ranges such as "10–$100\,^\circ\text{C}$" mix sans "10–" with serif maths; put the whole range in maths (`10\ldots 100\,{}^\circ\text{C}`).
- [Minor] Lesson Kaava text — units "(kPa)" and "(kPa/°C)" in plain text after symbols; put in maths for one typeface.
- [Minor] fig-3 and fig-6 — y axis starts at 95 kPa without a break mark; fig-3 is named in text, fig-6 is not; add the same note to fig-6's description.

## Checked
- contact-1,2,3; top/intro-1280; fig-1,2,3,4,6,7,8 at 390; fig-row/theory-1280-1,2
- example-390-1,2,3; stage-tutki-390-1; open-ennusta-1280-1; open-tarkista-1280-1; open-exit-1280
- Hero, gas thermometer, extrapolation graph: clear, LaTeX labels, dashed beyond data, error bars, uncertainty bracket; no clipping.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
