VERDICT: PASS
CONTENT-HASH: cacceb2e628b9b6e

## Blocking

## Polish
- lesson.md:653 (Yleinen virhekäsitys): "Kiihtyvyys on koko lennon ajan $g$ alaspäin" holds for the whole flight only when air resistance is small. The third sentence of the paragraph states that condition, and check-1 states it too, but this sentence does not. Fix: add "kun ilmanvastus on pieni" to it, as in check-1.
- inquiry.json:280 (exp-3 prompt): the right end of the tangent is given as $16\,\text{m}$, while hint 3 and the solution use $16{,}2\,\text{m}$. The sim's tangent really ends at $(4{,}2;\,16{,}2)$. With 16 m the student gets 5,92 m/s, which the tolerance accepts. Fix: give $16{,}2\,\text{m}$ in the prompt as well.
- inquiry.json:185 (exp-2 intro): "$v_0 = 6\,\text{m/s}$". Everywhere else this value is $6{,}0\,\text{m/s}$.
- review/shots/fy4-2-sim-390.png and the exp-*-390 shots show the canvas cropped, with tick labels drawn over each other ("20(40"). When I rendered preview/fy4-2.html at 390 px in Playwright, the narrow layout was correct: the road and both graphs showed and nothing overlapped. The captures were probably taken mid-resize, so the developer should regenerate them.

## Checked
- Definitions and signs: $a = \Delta v/\Delta t$. Speed grows when $\overline{v}$ and $\overline{a}$ point the same way and shrinks when they are opposed, and $a \ne 0$ at the instant $v = 0$. The theory, summary, misconception, pred-2, exp-2 and exit ticket 1 all say the same.
- Signed area: lesson :664 and the summary now count the part where $v < 0$ as negative. This agrees with the sim's calc box and its darker tint. check-2 and exp-1 state that the motion does not reverse.
- Recomputed everything independently in one script: hook (1,23 m, 4,91 m), retrieval 3,0 m/s, exp-1 (1, 4, 9 m and 5,0 m), exp-2 (v = 2, 0, −2 m/s; x = 9,0 m at 3 s; back at the origin at 6 s), exp-3 tangent (1,8 m and 16,2 m, slope 6,0 m/s), numpy fit A = 4,884, B = 0,126, C = 0,0013, g = 9,77 m/s², single-point mistake 10,4 m/s². Worked example: √76 = 8,72 m/s, t = 9,44 s, rejected root −25,4 s, v = 8,72 m/s, check 60 m. Etsi virhe 24 m, transfer 1,875 m/s² (40 s, 0,19 g), check-2 32 m, check-3 4,9 m and 14,7 m.
- Each choice item has exactly one correct option, and every distractor's feedback gives the right reason.
- figures.py: strobe gaps are 1:3:5 and 5:3:1, the v arrows step evenly and the a arrows are constant. The tangent figure's tangent at t = 6 passes through (3; 0). In the hero the stone's gaps are k·n² (1:3:5:7) and its arrow lengths are 19·n. ex-tv, ex-tangent, check-tv and fall-points match their data.
- Sim: v = v0 + at and x = v0t + ½at². The tangent spans ±1,2 s with slope v, and the shaded signed area equals x − x0. simState provides x and v. The experiment values lie within the slider ranges, v0 and a are locked, and the velocity arrow is scaled to the run's largest |v|.
- Conditions are stated: small air resistance, constant a, x0 = 0 in the model box, "yleensä" in the fit sentence, and B and C read as the initial velocity and initial position.
- Scope: everything stays within FY4 "tasaisesti kiihtyvä suoraviivainen liike" and the experimental determination of g. No forces appear.
