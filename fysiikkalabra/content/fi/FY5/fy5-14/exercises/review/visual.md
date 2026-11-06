VERDICT: PASS
CONTENT-HASH: c512778582165624

## Blocking
(none)

## Polish
- [Minor] fy5-14-L1-09 — the stem joins two unrelated situations (violin spectrum and car horn) in one true/false set; it reads clearly and each statement is self-contained, so only a note: a later set could keep one situation.
- [Minor] fy5-14-L1-09 statement 4 — feedback ends with a bare "Lähestyessä kasvaa voimakkuus."; "äänen voimakkuus" would read as a full clause.

## Checked
- Method: rebuilt with `python scripts/build.py fy5-14`; own script (vr5_newtask_probe.py, scratchpad) opened the new task at 390 px after the page scripts ran, answered, opened feedback, hints and solution, measured overflow. Document scrollWidth 390, no clipped element outside a scroll box; image read at card width (332 px, downscaled to read the whole card).
- From text only: the packet's diff, form-of-answer check (length by character count), distractor-to-warned-mistake fit, scope against the chapter.
- Render: five statements with Tosi/Epätosi buttons and feedback, answer line, model solution with five paragraphs; no overflow, formulas inline and short. Statement answers are 2 true, 3 false: no pattern leak.
- Delta only: new task and its solution; the rest of the set was PASS and untouched. No figure.

## Scores
illustrations n/a (no figure) · typography 5 · Finnish 4 · accessibility 5
