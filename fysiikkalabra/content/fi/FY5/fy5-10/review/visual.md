VERDICT: FAIL
CONTENT-HASH: 4abdffd582dd2934

## Blocking
- [Major] content/fi/FY5/fy5-10/inquiry.json:333 (Esimerkki 2: Etsi virhe, prompt; fy5-10-inq-virhe-0-390.png and -1280.png) — after the display block the student's quotation ends on a new line that begins with `.”`: the page shows `.” Missä on virhe?`. — A line starting with a full stop and a closing quotation mark is a visible typesetting error in a task text, at both widths; before the change the sentence ended inline (`… = 1,0 m/s.” Missä on virhe?`). — Take the full stop and the closing quotation mark into the last row, as the build does with a comma elsewhere: `… \\\\ &= 1{,}0\\,\\text{m/s}\\text{.”} \\end{aligned}$$ Missä on virhe?` (tested in the page's KaTeX: renders `= 1,0 m/s.”`, capture kt-quote.png). Numbers, signs and units stay as they are.

## Polish
- [Minor] same prompt (as on main, untouched) — the page starts the emphasised question part at "Koska taajuus on…", in the middle of the student's quotation, so the real question "Missä on virhe?" is not what stands out.

## Checked
- Delta, round 2: the prompt of Esimerkki 2 (inquiry.json:333). Opened fy5-10-inq-virhe-0-390.png and fy5-10-inq-virhe-0-1280.png: the block `v = fλ = 2,0 Hz · 0,50 m = 1,0 m/s` itself is clean (three rows, equals signs in a column, no clipping), the choices below are intact.
- Compared with the markup built on main for the same prompt.
- Not re-judged: the formula names in lesson.md (teacher-approved, not in this branch's diff).
- Own Playwright captures from preview/ (?ratkaisut=1, every details box open) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-7/; measured there: page scrollWidth equals the viewport, no formula past its box.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 5
