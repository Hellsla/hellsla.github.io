VERDICT: PASS
CONTENT-HASH: ff2f1b681aa38dda

## Blocking

## Polish
- glossary.json:2477 (*törmäysaika*) — the definition still writes the mean force as `F_k = mΔv/Δt`. Round 1 asked for this to change with the rest. The file is outside the hash and not rendered, so this is not blocking. — Write `F_ka`, as in the lesson and fy4-9.
- lessons/FY4/fy4-11/lesson-answers.py, comments `imp25-…` and `sp-…` (carried over from round 1) — the comments say 41,8 km/h and 70,7 m, but the code gives 40,7 km/h and 70,64 m. The text correctly says "noin 41" and 70,6 m. — Fix both comments.
- inquiry.json `tilasto` (carried over) — the 97–98 % belt use is for front seats only, but the deaths also include rear-seat passengers. — Add "etupenkillä" to "vyöttömiä on liikenteessä muutama prosentti". The conclusion still holds.

## Checked
- Rename: $F_\text{ka}$ is now used in lesson.md (the impulse equation, the formula, the variable list and the summary), in figure 6 (axis label and both bar labels, screenshot checked at 390 px) and in inquiry.json (`tormaystesti` feedback, and the check-3 criteria and model answer). No $F_\text{k}$ is left in the lesson, sim or answers files. This matches fy4-9.
- I recomputed every number in one script with my own formulas, and all are correct: 24,6 and 70,6 m (ratio 2,87); a 40,7 km/h hit at 25 m; 27,4 and 164,6 m; the example ≈ 72 m; μ = 0,917; 10,4 and 104 kN (14 G); 42 %; siirto 53,46 km/h; virhe 138,9 vs 10,7 m; 1,96; 62,96 m; 40 m.
- The model's conditions (level road, constant deceleration, no air resistance, full grip) are stated at the formula, in the worked example, in check 2 and in the sim box. $a=\mu g$ is derived from $N=mg$ on a level road.
- The force diagram (figure 2) shows G and N equal and friction as the only horizontal force, pointing backwards. v and a are drawn beside the car, not as forces. Figures 3 and 6 are to scale.
- sim.js implements the model, including a hit during the reaction time. Each experiment locks every parameter except the one it varies, and simState gives sR, sJ, sP, vImpact and a.
- Every choice item has exactly one correct option, and each distractor's feedback is correct. The mechanisms are right: Newton I, a longer Δt, and the airbag working with the belt.
