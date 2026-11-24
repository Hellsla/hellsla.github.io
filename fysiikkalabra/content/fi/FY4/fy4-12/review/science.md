VERDICT: PASS
CONTENT-HASH: 624bb27d73e83b97

## Blocking

## Polish
- inquiry.json:143 (sim `model`) — "Kitkaa ja ilmanvastusta ei huomioida" reads oddly in a purely kinematic model of an accelerating car, because road friction is what drives the car. — Suggest: "Voimia ei mallinneta: kiihtyvyys on annettu vakio."
- lesson.md:383 (summary), lesson.md:214 — the claim that the lead is greatest at equal speeds holds only when the follower speeds up and overtakes. The context makes this clear (C). — If you want it explicit, add "ja kiihtyy".
- sim.js `track` — the velocity arrow is |v|·2,8 + 6 px long, so its length is not strictly proportional to the speed, while `howto` says the length shows the magnitude. — Drop the +6 offset, or leave it (C).

## Checked
- The round-1 blocking item is fixed. The exp-2 Järkevyys now says the speed is more than $2v$ because of the 16 m head start, and that starting from the same place would give exactly $2v$. That is right: $v_\text{A} = v + \sqrt{v^2 + 2ad} > 2v$.
- I recomputed all 29 lesson-answers.py numbers in one script with my own quadratic meeting solver, and every one agrees. They include 8,0 s, 64 m, 16 m/s and −2,0 s; the 25 m and 9 m greatest leads at 3,0 s; case 1 at 10 s and 50 m; case 4 at −10 s; case 5 at 1,55 s and 6,45 s; the transfer task's 24 m/s, 96 m and 8 s; and check-2's 6,0 s with its mistakes 15, 30 and 10. Extras also agree: case 2 meets at 5 s, pr-paikka is 25 m, and in ei-kohtaa at t = 10 s the bodies are at 30 m and 70 m.
- Every choice item has exactly one correct option, and each distractor's feedback has the right physics and numbers. This covers pred-1 to pred-3, exp-3, ei-kohtaa, virhe and check-1.
- The worked example has all seven stages, is solved symbolically first (with the quadratic coefficients), keeps 2 sf, checks with the other position function and with the speeds, and discards the negative root.
- Figures are to scale by their pixel coordinates. tilanne: arrows 3:2, meeting at 36 m. kohtaus: crossing at (12 s, 36 m). kaava: x = t² against 6t, crossing at (6 s, 36 m). vt: two triangles of 9 m each. esimerkki: crossing at (8 s, 64 m). fig ei-kohtaa: 36 m and 80 m at 12 s.
- Sim: the CASES match the texts and sim-spec. meetings() solves x_A − x_B = 0 correctly. simState gives xA, xB, vA, gap and meetings, where meetings counts only the meetings reached so far. The 0,5 s slider step reaches 3, 8 and 10 s. The locked `tapaus` isolates t. In exp-3 the suggested times (gap −5, +1, +1, −1,5 m) show both sign changes.
- The guardrail sentence on the higher line is used with its direction condition (lesson.md:196).
- The model's limits are stated: point bodies, constant acceleration, acceleration from the start. The root-count claims state their conditions.
- Scope: FY4 uniform and uniformly accelerated linear motion only. The exit ticket, check-3 and the conclusion's model answer agree with the theory, and their numbers are called model values.
