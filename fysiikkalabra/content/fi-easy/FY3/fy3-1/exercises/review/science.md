VERDICT: PASS
CONTENT-HASH: 2a0490285f2ef3cd

## Blocking

## Polish
- solutions.md:179 (fy3-1-L3-04): the solution calls $c = x/(mg)$ "jousen vakio". That is the stretch per newton, the inverse of the spring constant. After the L1-02 fix a student may read it as jousivakio. Consider "venymä newtonia kohti" or "jousen verrannollisuuskerroin". The same wording is in the Finnish version. B-type at most, and the algebra does not depend on the name.
- exercises.json:307 (fy3-1-L1-10): the stored answer 316,2 N has one more figure than the solution's 316 N. The tolerance covers both values.

## Checked
- I recomputed all 20 numeric answers with my own formulas, independently of answers.py. Every one lies within its tolerance. L2-05 used a least-squares fit through the origin (9,80 m/s²). L3-04 used a least-squares $x/m$ (3,61 against the stored 3,6).
- I compared the set with the Finnish version by script: same ids, answers, units, tolerances, figures, data tables, correct options and numbers in every task text.
- solutions.md:19 (L1-02): the round-1 blocking item is fixed. It now says "venymä newtonia kohti", $0{,}50\,\text{cm/N}$, which is correct.
- G = mg is used with the lesson's g table everywhere. Mass and weight are kept apart. The spring's stretch is proportional to force, with "ei venytetä liikaa" stated. No Newton's laws are used, so the set stays inside FY3 scope.
- L1-09: B is the only right option. A (pull missing), C (F twice G) and D (F_k acts on the meter) each carry exactly their intended error, and the feedback is right. The figures give every value, and their descriptions do not reveal the answer.
- L1-06 and L1-07: exactly one option is correct, and every distractor's feedback is physically right.
- L3-03 (a scale calibrated on Earth and read on Mars) and L3-05 (the leg limit is a force: 682 kg; on Earth 612 kg) use the right models, symbolic first.
- Significant figures follow the limiting datum, and every reasonableness check is real.
- The hash was the same at the start and the end.
