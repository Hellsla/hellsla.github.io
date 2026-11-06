VERDICT: PASS
CONTENT-HASH: c716085d5bc703dc

## Blocking
(none)

## Polish
- [Minor] fy5-13-L2-08 — no defect; the correct option is the shortest (26 characters against 29–30) and its feedback is the shortest, so form does not give it away; the distractors catch the chapter's own mistake (closed pipe computed as open, plug effect read the wrong way).

## Checked
- Method: rebuilt with `python scripts/build.py fy5-13`; own script (vr5_newtask_probe.py, scratchpad) opened the new task at 390 px after the page scripts ran, answered, opened feedback, hints and solution, measured overflow. Document scrollWidth 390, no clipped element outside a scroll box; image read at card width (332 px, downscaled to read the whole card).
- From text only: the packet's diff, form-of-answer check (length by character count), distractor-to-warned-mistake fit, scope against the chapter.
- Render: stem, four options with feedback, Vastaus button, answer, Kysytty/Periaate/Mallivastaus; the three display lines of the model solution and the inline fractions in feedback fit 300 px; no gap in the opened card.
- Delta only: new task and its solution; the rest of the set was PASS and untouched. No figure.

## Scores
illustrations n/a (no figure) · typography 5 · Finnish 5 · accessibility 5
