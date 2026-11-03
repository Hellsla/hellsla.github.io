VERDICT: PASS
CONTENT-HASH: 101c5ea6adac8b3f

## Blocking
(none)

## Polish
- [Minor] fig-4-390 — "ear protector" is shorter than the text's "hearing protector" (column width); reads naturally and matches the drawing.

## Checked
- Re-ran figures.py fy5-16 --lang en after editing figures.json and re-shot; contact-1, -2, -4 opened for triage.
- fig-2-390: "hearing damage / danger" read as one odd phrase → now "risk of / hearing damage", right-aligned, unclipped.
- fig-4-390: "barrier, space" mistranslated "este, etäisyys" → now "barrier, distance"; "protector" → "ear protector"; both fit their columns.
- fig-8-390: "electric → motion → sound" (adjective as noun) → "signal → motion → sound" / "sound → motion → signal", fits both halves; alt text updated to match.
- fig-1, 3 (bar chart, decimal points 0.5/0.25), 5 (room), 6 (decay graph 0.2–1.4 s), 7 (anti-noise): English labels, LaTeX, nothing clipped.
- theory-1280, intro-1280, top-390, example-390-1/2 (staged, decimal points, thin spaces), stage-tutki-390-1 (table after fix).
- No Finnish in text, labels or alt text (script grep); headings show without anchors.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
