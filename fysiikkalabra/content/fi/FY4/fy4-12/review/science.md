VERDICT: FAIL
CONTENT-HASH: 47a97eb92976ebc3

## Blocking
- inquiry.json:267 (exp-2 solution, Järkevyys) — **A, causality.** The solution explains that 16 m/s is "yli kaksi kertaa" the cyclist's speed because the car must first make up the lead the cyclist gained while the car was slower. The lesson's own Kaava section (lines 273, 322) shows that making up that gain gives exactly $2v$. The amount over $2v$ comes from the initial 16 m head start. — Fix: "Se on yli kaksi kertaa pyöräilijän nopeus, koska pyöräilijä oli lisäksi alussa $16\,\text{m}$ edellä; samasta paikasta lähdettäessä ohitusnopeus olisi täsmälleen $2v$."

## Polish
- inquiry.json:143 (sim `model`) — "Kitkaa ja ilmanvastusta ei huomioida" sits oddly in a kinematic model of an accelerating car, because road friction is what drives the car. — Suggest: "Voimia ei mallinneta: kiihtyvyys on annettu vakio."
- lesson.md:383 (summary) — the maximum lead at equal speeds holds only if the follower becomes faster. — Add "ja kiihtyy".
- sim.js `track` — the velocity arrow is |v|·2,8 + 6 px long, so it is not strictly proportional to the speed, while howto says its length shows the magnitude. — Drop the +6 offset, or leave it as is (C).

## Checked
- I recomputed all 29 lesson-answers.py numbers in one script with my own meeting solver. All agree, including 8,0 s/64 m/16 m/s, the 25 m lead, case 5 at 1,55/6,45 s, the transfer task's 24 m/s and check-2's 6,0 s with its mistakes.
- Every choice item has exactly one correct option, and every distractor's feedback has the right physics and numbers.
- The worked example is complete: it is solved symbolically first, rounded to 2 sf, checked with the other position function, and the negative root is discarded.
- All six figures are to scale by their pixel coordinates (the arrows 3:2, the vt areas ±9 m, the intersections).
- Sim: CASES 1, 3, 4 and 5 match the texts. simState gives xA, xB, vA, gap and meetings. The 0,5 s slider step reaches 3, 8 and 10 s. The locked `tapaus` isolates t.
- The higher-line guardrail is followed with its direction condition (lesson.md:196).
- The root-count claims state their conditions, and the model box states point bodies and constant acceleration.
- The scope is FY4 linear motion only. The exit ticket and check-3 agree with the theory.
