VERDICT: PASS
CONTENT-HASH: fcb065ab0c26d6d6

## Blocking
(none)

## Polish
- [Minor] inquiry.json ennuste-2 standby feedback — "$365 \cdot 21\,\text{h} = 7665\,\text{h}$" sits mid-sentence in parentheses; fine, but 120 vs 122 kWh in keitin feedback differs from the solution; use one value.
- [Minor] saastot table (carried over) — cell "$365 \cdot 10\,\text{min}$" tight to the right edge at 390 px; shorten header.

## Checked
- Hash at start and end: fcb065ab0c26d6d6.
- contact-1 (top, hero, both figures, example part 1/2, ennusta).
- stage-ennusta-390-2 and open-ennusta-1280-1/-2: prediction 2 options render, units in KaTeX, no clipping.
- The changed feedback (hidden until reveal, so not in any capture) was rendered in the preview at 390 px with Playwright: 0 katex-error elements, "365 · 21 h = 7665 h" parsed and rendered; the other changed feedback and lesson-answers.py diff are plain text/unit-LaTeX, no bare quantities.
- Diff covers only inquiry.json feedback text and lesson-answers.py (no figure change).

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
