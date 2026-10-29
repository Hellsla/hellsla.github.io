VERDICT: PASS
CONTENT-HASH: 1bb16197ef174c7b

## Blocking
- none

## Polish
- scripts/check_i18n.py does not list `detail` (a rubric criterion's specifics) in TEXT_KEYS, so it reports the translated check-3 criteria details as errors; the translation is right and the checker needs `detail` added (outside this review's scope; the content hash does not change when it is fixed).
- lang/en.json (not a lesson file): the sim's canvas title reads "Situation" where the lesson says "situation diagram".

## Checked
- Checked (full translation review against the reviewed Finnish): lesson.md (core idea, eight steps, the two representations, the YTL scoring paragraph, formula section, staged worked example 2.96 m/s² / 71.8 N rounded to 3.0 m/s² and 72 N, reasonableness 118 N = 72 N + 46 N, misconception, summary), inquiry.json (hook, review, both predictions with the model values 196/146 N and 5.0/2.5 m/s², sim texts, exp-1 numeric solution 50 N, exp-2 choice, conclusion model, spring-balance data 4.9 N, error-finding, elevator, fish 23 N, checks incl. sign 51 N, draw-it-yourself 52 N / 148 N), exit ticket, meta. Decimal points throughout, units and LaTeX preserved; no wrong option became right; the elevator options keep empty texts and the four figure descriptions only list arrow lengths. Force symbols G, N, T, F_mu, F consistent with the figure labels; buoyancy is F_b in the helium figure via figures.json. Fixed: the experiments' column name `tilanne` translated (situation), the six check-3 rubric details translated from Finnish, the sim howto now names the options as the sim shows them. figures.py --lang en --check up to date; preview at 360 px: no overflow, no page errors, sim labels in English, figures render.
