VERDICT: PASS
CONTENT-HASH: e964c37910114b98

## Blocking

## Polish
- inquiry.json `johtopaatos` model — "noin $1\,\text{mA}$:sta" for the rubber-sole case; the table gives $1{,}15\,\text{mA}$, so "noin $1{,}2\,\text{mA}$" would match the `iho` solution exactly (C-level, not a finding).

## Checked
- Previous Blocking fixed: lesson.md (Suurjännitejohdot, bird paragraph) and Yleinen virhekäsitys now say the potential difference between the feet is very small and only a very small current flows, the same wording as `ennuste-2`'s correct option and all four feedbacks; the askel figure's $U \approx 0$ and its aria-label agree.
- ennuste-2: exactly one correct option; distractors (dry feet insulate, current "chooses" least resistance, insulating sheath) really wrong, and their feedback repairs each one correctly.
- ennuste-1: the RCD is the one correct option ($100\,\text{mA} > 30\,\text{mA}$, the fuse sees 1 % of its $10\,\text{A}$); the distractor feedback is right.
- Recomputed in one script with my own formulas: kertaus 8,70 A; keittio 13,9 A (all five 22,6 A); iho 230 / 11,5 / 1,15 mA; example 19,6 A (9,57 + 4,35 + 5,65; estimate 22,5 A); virhe 12,6 A; siirto 14,8 A, 131 W, the cord drop 8,9 V, mistakes 8,87 / 45,4 / 88 167; P_max 2300 / 3680 W; exit $(16:10)^2 = 2{,}56$. All match lesson-answers.py and the texts.
- Models and conditions: parallel loads at $230\,\text{V}$ effective value with power factor ≈ 1 stated; $P = RI^2$ heating; TN system named for the fault-current path; RCD limit (L–N contact) stated; shoes protect only under the stated conditions.
- Safety statements exact: never replace a fuse with a larger one, cut the power before touching a victim, 112, Tukes' list of permitted lay work; IEC 60479-1 effect thresholds are labelled indicative and depend on duration and path.
- Scope: fuse, protection classes and breakdown strength are LOPS FY6 contents; no later-course physics.
- Assessment: virhe, tarkistus-1, tarkistus-2 each have exactly one correct option; the tarkistus-3 rubric asks only what the prompt gives.
