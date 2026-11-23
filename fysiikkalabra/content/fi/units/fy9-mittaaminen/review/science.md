VERDICT: PASS
CONTENT-HASH: c66703f1d31a22ae
SCOPE: full. The change is three new `pysahdy` boxes in unit.md, judged first. After that the unit text, inquiry.json, teacher.md and the Sovella task set (s1–s8) were judged with it.

## Blocking
None.

## Polish
- Box 2 (kulmakerroin) gives two reasons: the fitted line represents all the data, and far-apart points shrink the share of the reading error. Both are correct and agree with lahto-3 and the "Yleisiä virheitä" list. It could also say that two measurement points carry their own random errors and leave out the other points, as the lahto-3 feedback does. This is optional (C).
- Carried from round 3: s8 a criterion 5 range versus the model answer; s7 c rubric $1{,}2/30{,}0$ versus $1{,}22$; s8 c interval wording. None is an error.

## Checked
- Box 1 (clock that always runs fast): this is a systematic error with the same sign in every reading, so averaging does not remove it. Correct (A/B: none). It agrees with the theory paragraph above it, with lahto-2, with virhelaji and with the "Yleisiä virheitä" item.
- Box 3: $s = \tfrac{a}{2}t^2$, so $k = \tfrac{a}{2}$ and $a = 2k$. Correct. The conditions (start from rest, constant acceleration, time from the start) are stated in the paragraph just before the box. A straight $(t^2, s)$ line through the origin implies them anyway, so there is no unstated condition (B: none). It agrees with lahto-5 and kuula-kouru.
- Inquiry numbers, recomputed in scratchpad `r/sov.py` and `inq.py`:
  - lahto-1: $2{,}705 \to 2{,}7\,\text{g/cm}^3$.
  - tutki-kaasu: $\theta_0 = -271{,}7 \approx -270\,{}^\circ\text{C}$.
  - kolikot: $2{,}70\,\%$.
  - jousi-suora: $79{,}0\,\text{N/m}$; mistakes $48{,}6$ and $8$.
  - kuula-kouru: $1{,}24\,\text{m/s}^2$; mistakes $0{,}62$ and $0{,}31$.
  - kattila: $10{,}0\,\text{min}$; mistakes $13{,}0$ and $16{,}1$.
  - tarkista-1: A $(1{,}8033 \pm 0{,}0005)\,\text{m}$, B $(1{,}803 \pm 0{,}015)\,\text{m}$.
  - tarkista-2: $28\,\text{kg/m}^3$.
  - The rounded final answers ($1{,}2$, $30$) stay inside their tolerances.
  - Each multiple-choice question has exactly one correct option, and every distractor's feedback is right.
- Sovella numbers, recomputed with my own fits (numpy, not answers.py):
  - s1: $13{,}71 \pm 0{,}19\,\text{s}$, $7{,}29\,\text{m/s}$, bounds $7{,}17$/$7{,}42$, Mira $13{,}96 \pm 0{,}16\,\text{s}$.
  - s2: $102\,\mu\text{m}$, $79{,}8\,\text{g/m}^2$, $783\,\text{kg/m}^3$.
  - s3 (row $60\,\text{ml}$ excluded): $k = 0{,}9183$, $b = 118{,}65\,\text{g}$, $V \approx 70{,}5\,\text{ml}$, $1{,}378\,\text{kg}$.
  - s4: $k = 1{,}0205$, $b \approx 0$, $749{,}7\,\text{g}$.
  - s5: $0{,}477\,\text{m/s}$, and the report's through-the-origin slope $0{,}6341$ is reproduced.
  - s6: $pV$ $2269 \to 2454$, $V_0 = 1{,}77\,\text{ml}$, $n = 1{,}06\,\text{mmol}$.
  - s7 and s8 as in round 3 (answers.py agrees).
- The other changes to solutions.md since 6b32d6f31 only split paragraphs (carry `md-paragraphs`, carry.tsv 2026-11-18). No number or claim changed.
- No later-course physics appears: the scope is FY1 measurement, plus Boyle's law and $pV = nRT$ in s6 as the unit states.
- `practice.py check`: OK. The hash is c66703f1d31a22ae at the start and at the end.
