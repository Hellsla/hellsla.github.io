VERDICT: FAIL
CONTENT-HASH: e9115553fe1fb6c4
SCOPE: delta, s4 b after the rewording of the question (task text, rubric, worked solution)

## Blocking
- s4 b, solutions.md, A (error; internal consistency, item 6). The task now asks "Arvioi, kuinka lyhyen ilmavälin yli läpilyönti tapahtuu varmasti". The worked solution still has the old reading in two places:
  - `**Kysytty:** ... ja pienin ilmaväli, joka voi lyödä läpi`
  - "Tasaisen kentän mallilla pienin läpilyövä väli on $d = \tfrac{U}{E_\text{max}} \approx 4\,\text{mm}$"

  In the uniform-field model the gap breaks down when $U/d \ge E_\text{max}$, that is when $d \le U/E_\text{max}$. So 4 mm is the longest gap that certainly breaks down, not the smallest. Every shorter gap breaks down too. Fix: "kysytty ... ilmavälin pituus, jonka yli läpilyönti tapahtuu varmasti" and "Tasaisen kentän mallilla läpilyönti tapahtuu varmasti, kun väli on enintään $d = \tfrac{U}{E_\text{max}} \approx 4\,\text{mm}$". Also check the same lines in en and fi-easy.

## Polish
- The task wording "kuinka lyhyen ... varmasti" is physically correct: breakdown is certain for gaps of 4 mm or less, and the answer is that limit. "Enintään kuinka pitkän" would read more plainly. That is wording, not physics.
- The rubric's math criterion and its assumptions criterion ("Arvio on alaraja ... valokaari voi syttyä selvästi pidemmästäkin välistä") agree with the new question. They also agree with the solution's "alaraja turvaetäisyydelle". Once the Kysytty line and the model-answer sentence are fixed, all three texts agree.
- The rubric asks for 4 mm from 12 kV. With $20/\sqrt3 = 11{,}55\,\text{kV}$ the result is 3,85 mm, so an answer of "about 4 mm" from either value is right.

## Checked
- `units.py hash fy9-sahkokentta` at the start and the end: e9115553fe1fb6c4. `practice.py check: OK`.
- Recomputed:
  - $20/\sqrt3 = 11{,}55\,\text{kV}$
  - $12\,\text{kV}/(3\,\text{MV/m}) = 4{,}0\,\text{mm}$
  - $U$ across the feet $= 1{,}5\,\text{mV}$
  - $12\,\text{kV}/10\,\text{k}\Omega = 1{,}2\,\text{A}$

  All four agree with the solution and answers.py.
- Physics of the new question: the field near the thin conductor and the rod tip is stronger than $U/d$. So when the mean field is at or above $E_\text{max}$, breakdown is certain, and longer gaps can also break down. The 4 mm is therefore the right "certain" threshold, and calling it a lower bound for the safety distance is correct.
- The rubric points still add up to 5 (1+2+1+1). Every criterion asks only for what the task gives and asks.
- The rest of s4, and s1–s3 and s5–s8, are unchanged since my earlier PASS and were not judged again.
