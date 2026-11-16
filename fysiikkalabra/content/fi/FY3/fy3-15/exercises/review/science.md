VERDICT: PASS
CONTENT-HASH: 3982956434865159

## Blocking

## Polish

## Checked
- The hash was 3982956434865159 at the start and the end.
- Delta (fy3-15-L3-05): in d) of the exercises.json text, "ei voi enää tuottaa sähköä" became "ei voi enää käytännössä tuottaa sähköä". The Järkevyys line of solutions.md now adds that at so small a temperature difference the largest possible efficiency is only a few percent.
- "käytännössä" is the correct qualifier. Low-grade heat is not unusable in principle; it is only uneconomic, and the round-1 wording claimed too much. The added limit names the real reason, which agrees with the guardrail that a heat engine cannot turn all of its heat into work.
- I recomputed the bound from the task's own data in one script. The monthly outlet temperatures 12,1 / 14,2 / 28,4 / 23,2 °C and rises of 10,9 / 10,7 / 10,6 / 10,9 K give 1 − T_c/T_h = 3,5–3,8 %. For a stream that cools as it gives off heat the bound is about half that. "muutama prosentti" is therefore right as an upper limit.
- The same script gives the unchanged numbers again: ΔT_ka = 10,775 K, P_L = 4190 · 38 000 · 10,775 W = 1716 MW (answer 1720 MW, answers.py 1716, tolerance 2 %), P_h = 1800 MW, share 95 %, remainder 84 MW.
- The sentence keeps energy conservation explicit: the energy "ei ole kadonnut vaan lämmittää merta". No number, symbol or answer changed.
- Scope: the limit is stated as a fact in the reasonableness check. The student is not asked to compute it, so the task stays within FY3 and its prerequisite chapter on the heat engine.
