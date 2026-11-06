VERDICT: PASS
CONTENT-HASH: 3310fe0c64a2e03d

## Blocking
(none)

## Polish
- [Minor] fy5-15-L2-08 solutions.md — "noin $10\,000$-kertainen" wraps before "-kertainen" on a phone (the hyphen part lands on the next line); `$10\,000$\u2011kertainen` or a rewording would keep it together.

## Checked
- Method: rebuilt with `python scripts/build.py fy5-15`; own script (vr5_newtask_probe.py, scratchpad) opened the new task at 390 px after the page scripts ran, answered, opened feedback, hints and solution, measured overflow. Document scrollWidth 390, no clipped element outside a scroll box; image read at card width (332 px, downscaled to read the whole card).
- From text only: the packet's diff, form-of-answer check (length by character count), distractor-to-warned-mistake fit, scope against the chapter.
- Render: stem, four options with feedback (inline fractions fit), model solution: five short display rows, no overflow. The correct option (23 characters) is not the longest; distractors are the warned mistakes (dB compared as plain numbers, difference read as a ratio, dB-to-power step skipped).
- Delta only: new task and its solution; the rest of the set was PASS and untouched. No figure.

## Scores
illustrations n/a (no figure) · typography 5 · Finnish 5 · accessibility 5
