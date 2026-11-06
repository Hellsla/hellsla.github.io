VERDICT: PASS
CONTENT-HASH: 2c4015ccb6d6d59f

## Blocking
(none)

## Polish
- [Minor] fy5-17-L2-08 reasons — the correct reason is the longest (108 characters against 83–90) and has the shortest feedback among the wrong-vs-right lines; shorten it a little ("Kumpikin aalto kulkee saman matkan tasaisella nopeudella, joten aikaero on suoraan verrannollinen matkaan.").
- [Minor] fy5-17-L2-08 solution — the row $d_\text{B} = 8{,}4\,\text{km/s} \cdot 24{,}0\,\text{s} \approx 2{,}0 \cdot 10^{2}\,\text{km}$ measures 317 px in a 304 px scrolling line (flFitMath, by design); it fits on screen, only a few pixels scroll.

## Checked
- Method: rebuilt with `python scripts/build.py fy5-17`; own script (vr5_newtask_probe.py, scratchpad) opened the new task at 390 px after the page scripts ran, answered, opened feedback, hints and solution, measured overflow. Document scrollWidth 390, no clipped element outside a scroll box; image read at card width (332 px, downscaled to read the whole card).
- From text only: the packet's diff, form-of-answer check (length by character count), distractor-to-warned-mistake fit, scope against the chapter.
- Render: stem in three paragraphs, choice stage, reason stage with feedback and the correct-choice feedback pointing on to the reason stage without giving the reason; solution with five display rows; no overflow.
- Delta only: new task and its solution; the rest of the set was PASS and untouched. No figure.

## Scores
illustrations n/a (no figure) · typography 5 · Finnish 5 · accessibility 5
