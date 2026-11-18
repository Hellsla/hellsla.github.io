VERDICT: PASS
CONTENT-HASH: a7fd1f4cabdc517a
SCOPE: delta: new tasks s7 (Calibrating a spring) and s8 (A steel ball dropped, filmed on video, with graph s8-kuvaaja) and the changed intro; older tasks untouched

## Blocking
- (none)

## Polish
- [Minor] s8 c, Comparison: the second row of the chain is a bare "≈ 5.5 %" with no quantity; write `\dfrac{0.54}{9.81} \approx 5.5\,\%`.
- [Minor] s8 c, error in the time scale: two separate calculations (`√(9.81/10.35) = 0.974`, `0.974 · 0.05 s = 0.0487 s`) share one block with no named left side; two blocks, or name them.
- [Minor] s8 b, "Reading the graph" does not say the read points are the circled ones in the figure (only the alt text does); add "(circled in the graph)".
- [Minor] s7/s8 Substitution: chain boxes end in ";" or "," (`= 30.0 N/m;`); same as the older tasks, so optional.

## Checked
- Playwright is missing, so I rendered the English page (`preview/en/fy9-mittaaminen.html`) in headless Chrome at 360 px, s7 and s8 cards isolated with solutions open (own captures; graph at 2.5x). Opened: both task cards, s8 graph, s8 solution b-c; s7 solution read from the Finnish render, the English structure being the same.
- English text: natural and consistent with the Finnish; same numbers and units (30.0 ± 1.2 N/m, 10.35 ± 0.15 m/s², 15.0 ± 0.6 cm, 9.81 m/s²); decimal point used in prose and graph labels; "She measures" matches the student; "Skills from the chapters" links read correctly; chapter names match the interface ("Measuring and the reliability of a measurement").
- Graph labels and alt text in English match the task text ("distance s the ball has fallen", t², 5.18 m/s², 0.01 m, circled points). Axes carry quantity and unit, points distinct from the line, nothing clipped.
- 360 px: aligned rows wrap, no clipped formula, tables stack readably.
- Intro: "Eight problems … Two problems start from a ready graph, and one combines measuring with the ideal gas law" read from tasks.json; true (s7 and s8 give a graph). Intro not opened as a render.

## Scores
illustrations 4 · typography 4 · Finnish (English text) 5 · accessibility 4
