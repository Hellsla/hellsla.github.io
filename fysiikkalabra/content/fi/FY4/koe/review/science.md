VERDICT: FAIL
CONTENT-HASH: c30111e28700e7df
Mode: full (round 1, work queue 8m: liikekitka → liukukitka, lähtökitka)

## Blocking
1. **A, fy4-k3 c Vastaus** (solutions.md): "Auton hidastuvuus on $5{,}0\,\text{m/s}^2$, enemmän kuin lepokitkan enimmäisarvo $3{,}9\,\text{m/s}^2$." This gives a friction force in m/s². The $3{,}9\,\text{m/s}^2$ is the greatest deceleration that the friction can give the crate, $\mu_0 g$, not the friction itself. The new term rule asks for "lähtökitka" after the term is introduced, so one rewording fixes both problems. Example: "…enemmän kuin suurin hidastuvuus $3{,}9\,\text{m/s}^2$, jonka lähtökitka voi laatikolle antaa." The Periaate line already says it right.

## Polish
- fy4-k6 b Mallivastaus says the curve is under the weight line "noin hetkestä $0{,}33\,\text{s}$". Linear interpolation of the table gives $0{,}34\,\text{s}$. Both fit "noin". Optional.
- fy4-k3 d Järkevyys could say "lähtökitka" instead of "lepokitkan enimmäisarvo", to match k1 f (C, not wrong).

## Checked
- The term change: no "liikekitka" is left in tasks.json, solutions.md, answers.py or figures.py. k1 f names $\mu_0 N \approx 196\,\text{N}$ "täysin kehittynyt lepokitka eli lähtökitka", and the static friction $120\,\text{N}$ is the right answer. "Lepokitka on enintään $\mu_0 N$" stays in k3 b. Sliding friction $F_\mu = \mu N$ is used in k3 d and k4.
- I recomputed every number in my own script and it matches answers.py:
  - k1: h $I = 6{,}0\,\text{N·s}$, $14\,\text{m/s}$, with distractors $28$, $13\,953$ and $2{,}6$. i: $67\,\%$, $44\,\%$, $33\,\%$. g: $2v$.
  - k2: $0{,}95\,\text{m/s}^2$ (origin fit $0{,}952$), $76\,\text{m}$, $30{,}4\,\text{kN}$.
  - k3: $3{,}92\,\text{m/s}^2$ (an "enintään" value rounded down to $3{,}9$), $5{,}0\,\text{m/s}^2$, $2{,}94\,\text{m/s}^2$.
  - k4: $0{,}249$, extremes $0{,}234$ and $0{,}265$, giving $\pm 0{,}02$.
  - k5: $0{,}60\,\text{m/s}$; $27{,}0$ and $10{,}8\,\text{kJ}$, so $16{,}2\,\text{kJ}$ ($60\,\%$); $27\,\text{kN}$; $-0{,}90$ and $+0{,}60\,\text{m/s}$.
  - k6: $70{,}0\,\text{kg}$; area $447{,}2\,\text{N·s}$; net $172\,\text{N·s}$; $2{,}46\,\text{m/s}$; $0{,}309\,\text{m}$. From the flight time $0{,}294\,\text{m}$, range $0{,}26$–$0{,}33\,\text{m}$. A $1\,\%$ error in the area gives $2{,}6\,\%$ in $v$ and $5\,\%$ in $h$.
  - k7: $5{,}42\,\text{m/s}$; $603\,\text{m/s}^2$ ($61\,g$); $3{,}06\,\text{kN}$; half-sine area $5{,}44\,\text{m/s}$. The half-sine stopping distance is $2{,}43\,\text{cm}$, consistent with $2{,}4\,\text{cm}$. Then $613\,\text{m/s}^2$, factor $1{,}55$, $1472$ and $2280\,\text{m/s}^2$, margin $6{,}9\,\%$, energy ratio $1{,}64$.
- Every Osa 1 item has exactly one correct option, and its distractor feedback is right. The k1 e figures match their text: A is correct, and B, C and D each have one error. The k3 force diagram: static friction forward, $N = G$, no "liikevoima".
- Rubric sums 15/15/15/15/20/20; criteria ask only what the task gives. Scope, units, figures and Hyväksytään myös sound.
- Hash identical at the start and the end.
