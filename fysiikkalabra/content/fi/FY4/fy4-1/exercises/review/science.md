VERDICT: PASS
CONTENT-HASH: fd398a527c525186

## Blocking

## Polish
- content/fi/FY4/fy4-1/exercises/solutions.md:237 (L1-09) — "Kuvaaja A nousee paikasta $6\,\text{m}$ paikkaan $10\,\text{m}$" and "kohdassa $-1\,\text{m}$" drop the figures used everywhere else ($6{,}0$, $-1{,}0$) — write $6{,}0\,\text{m}$, $10\,\text{m}$, $-1{,}0\,\text{m}$ as in the feedback.
- lessons/FY4/fy4-1/answers.py:26 — the comment lists L1-06..08 as multiple choice; L1-09 is not mentioned — add it to the comment.

## Checked
- New task fy4-1-L1-09 (graph choice, type 2): recomputed x(4,0 s) = 6,0 m − 1,0 m/s · 4,0 s = 2,0 m; only figure C (6 → 2 m over 0–4 s) fits; exactly one correct option.
- Figures (from figcat source and descriptions, text only): all four share one grid (t 0–5 s, x −6…12 m, axis at x = 0); every value is on a 1 s / 2 m grid line or halfway (D at −1 m); each description is complete and gives the same information as the picture; none is identifiable by form (same label "Kuvaaja X", same axes, same line width).
- Distractors catch the chapter's warned mistakes: A = sign of v ignored ("negatiivinen nopeus hitaana"/direction), D = velocity read as a position ((t,x) vs (t,v)), B = start position forgotten. Each feedback says why it is wrong; the correct feedback gives only the check, no extra stage.
- Scope: only x = x₀ + vt and slope = v from this chapter; (t,v) graph is already used in L2-07 and FY1.
- Solution: Kysytty/Periaate/Mallivastaus complete, symbolic first, slope check right, notation x₀, v, (t, x) as in the lesson.
- All 21 answers: answers.py run once (python -I) and compared with exercises.json: 17 numeric answers within tolerance; L1-06..09 non-numeric, each with exactly one correct choice.
- Inline formulas (text only, not rendered): the longest inline chain is the slope fraction (≈ 120 px); all under 300 px at 390 px. The deterministic 360 px layout check passed.
- Hash identical at start and end.
