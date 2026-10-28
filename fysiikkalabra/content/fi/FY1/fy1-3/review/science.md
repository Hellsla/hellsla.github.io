VERDICT: PASS
CONTENT-HASH: 76b9b8b3e6ff81b1

## Blocking

## Polish
- exit-ticket.json:4 and inquiry.json:300, 312, 320 — the half-ranges $\Delta m = 0{,}1\,\text{g}$ and $0{,}1\,{}^\circ\text{C}$ start with 1. Under the lesson's own convention (lesson.md:134, 262) they would be $0{,}10$. The values are exact at the data's resolution, so this is not an error. Fix: write $0{,}10$, or qualify lesson.md:134.
- inquiry.json:394 (karkea, wrong-option feedback) — "$0{,}62\,\text{s}$" as an inflated error estimate would be $0{,}6\,\text{s}$ by the convention.
- inquiry.json:283, 291 (exp-3) — "$0{,}0850\,\text{s}$", but the readout shows $0{,}085\,\text{s}$ (open since round 2).
- lessons/FY1/fy1-3/lesson-answers.py — inq-ice-corrected (62,3 °C) is unused (open since round 2).
- Spelling — lesson.md:104, inquiry.json:519 and exit-ticket.json:12 write "virhearvio", elsewhere "virhe-arvio".

## Checked
- Round-3 FAIL retracted. It rested on a one-figure rule that the teacher never gave. The lesson's convention is one significant figure, two if the first digit is 1, with the result rounded to the same decimal. The worked example applies it: $\Delta t = 0{,}12\,\text{s}$, $t = 3{,}18\,\text{s} \pm 0{,}12\,\text{s}$, and $\varepsilon = 3{,}8\,\%$ with two figures as in $\Delta t$. Fig. 4, check-2 ($0{,}05\,\text{s}$, $2\,\%$) and exit-ticket item 3 ($4{,}52 \pm 0{,}09\,\text{s}$, $\approx 2\,\%$) also apply it.
- One script recomputed the worked example (3,1817 s; 0,120 s; 3,77 %), karkea (mean shift 0,19 s; 0,09 → 0,62 s), check-2 (2,08 %; entering 2 is 4,8 % off, so it is accepted), siirto and its four mistakes (5,44/5,6/27,2/4,8 g), the ice data (1,5 and 0,1 °C) and exit ticket item 1 (19,9 g, 1,99 %). Each matches lesson-answers.py.
- The sim series was recomputed. exp-1: n = 1 gives −0,22 s; n = 5 and n = 40 give half-ranges 0,25 and 0,26 s; at n = 40 the mean is 0,0005 s off. exp-2: n = 40 gives +0,2995 s. exp-3: 0,085/0,26/0,525 s, ratio 6,18. The feedback numbers match.
- SVG numbers to scale. Fig. 1: means 2,406 and 2,592 s, Δt_sys about 0,19 s. Fig. 4: dots, mean and ±0,12 band. Fig. 3: 48,7 − 1,2 = 47,5 g.
- Formulas (mean, half-range, d/2, ε, Δx_sys, correction) are correct and within FY1. The experiments lock the parameters they do not vary, and simState gives mean, puoli and vir.
- No ×, \times or ÷; divisions written as operations use ":"; the error symbols are Δx, Δt and Δt_sys; karkea virhe is taught and practised.
- Content hash is identical at the start and the end.
