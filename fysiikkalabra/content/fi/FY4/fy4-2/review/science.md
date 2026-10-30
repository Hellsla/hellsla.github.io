VERDICT: PASS
CONTENT-HASH: 80abae277caa0b18

## Blocking

## Polish
- lesson.md:653 (Yleinen virhekäsitys): "Kiihtyvyys on koko lennon ajan $g$ alaspäin" holds only when air resistance is small. That condition is in the same paragraph's last sentence and in check-1, but not in this sentence (carried from round 2). Fix: add "kun ilmanvastus on pieni".
- inquiry.json:280 (exp-3 prompt): the prompt gives the tangent's right end as $16\,\text{m}$, but hint 3, the solution and the sim's tangent all use $16{,}2\,\text{m}$ (carried from round 2). Fix: write $16{,}2\,\text{m}$.
- inquiry.json:185 (exp-2 intro): "$v_0 = 6\,\text{m/s}$", while every other mention uses $6{,}0\,\text{m/s}$ (carried).
- sim.js:12: the comment says the phone canvas is 600 × 700, but `setLayout` sets `H = 785`. This is a code comment only and changes nothing on the page.

## Checked
- Phone layout (sim.js `setLayout`, narrow < 500 px): the physics is the same in both layouts: $v = v_0 + at$, $x = v_0t + \tfrac12at^2$, a tangent of ±1,2 s with slope $v$, and a signed area shaded in two tints. Only the geometry, the arrow scales (v up to 200 px at the run's largest |v|, a at 28 px per m/s²) and the tick thinning change. In the 390 px shots (sim, exp-1–3) the road, both graphs and the arrows show without overlap. In exp-3 (t = 3,0 s) the tangent, $v = 6{,}0$ m/s and $x = 9{,}0$ m match the model.
- simState still exposes x and v, and the experiments' v0/a/t lie within the slider ranges with v0 and a locked.
- I recomputed everything in one script. Hook: 1,23 m and 4,91 m. Retrieval: 3,0 m/s. exp-1: 1, 4, 9 m, so 5,0 m in the third second. exp-2: v = 2, 0, −2 m/s; x = 9 m at 3 s and 0 at 6 s. exp-3: the tangent runs from (1,8; 1,8) to (4,2; 16,2), giving 6,0 m/s. Free-fall fit (numpy): A = 4,884, B = 0,126, C = 0,0013, so g = 9,77; the single-point estimate gives 10,4. Worked example: 76, 8,72 m/s, 9,44 s, rejected root −25,4 s, and v = 8,72 m/s checks back to 60 m. Etsi virhe: 24 m. Transfer: 1,875 m/s², 40 s, 0,19 g. check-2: 32 m. check-3: 4,9 m and 14,7 m.
- Each choice item has exactly one correct option, and every distractor's feedback gives the right reason (pr, pred-1, pred-2, exp-2, virhe, check-1).
- Signs: speed grows when $\overline{v}$ and $\overline{a}$ point the same way, and $a \ne 0$ when $v = 0$. The theory, summary, misconception, predictions, exp-2 and exit ticket 1 agree on both.
- Signed area: the part below the time axis counts as negative in the theory, the summary and the sim's calc box. check-2 and exp-1 state that the motion does not reverse.
- Figures: in the hero, the stone's gaps are 25:75:125:175 (1:3:5:7). The strobe figure has 1:3:5 gaps and a constant a arrow. fall-points and check-tv match their data.
- Scope: the lesson stays within FY4's uniformly accelerated straight-line motion and the experimental determination of g. Conditions are stated: small air resistance, constant a, x0 = 0, and "yleensä" in the fit sentence.
