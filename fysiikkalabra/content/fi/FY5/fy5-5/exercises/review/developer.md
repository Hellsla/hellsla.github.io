VERDICT: DONE

Work queue 18, teacher's decision P3 (field strength = extension). Same changes in fi, en, fi-easy.

**exercises.json**
- Prefix `Syventävä tehtävä.` / `Extension task.` on L1-03, L1-09, L2-02, L2-04, L2-05, L2-07, L2-09, L3-02, L3-04, L3-05. All ten verified: field strength is asked (L1-03, L2-04, L2-05, L3-02) or given and needed (L1-09, L2-02, L2-07, L2-09, L3-04, L3-05; in L3-05 only as the given $g$ in $G = mg$).
- No unlisted exercise asks, gives or needs it. Note: L2-08 names the field only in one wrong reason and its feedback; not prefixed.
- Core before: L1-03, L1-06, L2-01, L2-07. After: L1-02, L1-06, L2-01, L2-06 (`"core": true` removed from L1-03 and L2-07, set on L1-02 and L2-06; both use the law of gravitation directly, L2-06 is a data task as L2-07 was).

**solutions.md**
- L2-03 Järkevyys: $3{,}4 \cdot 6378\,\text{km} \approx 21\,700\,\text{km}$ (was 21 900); the number is not used afterwards.
- L2-06 Vastaus: the justification "mean is more accurate" replaced: the data have two significant figures, so the result is reliable to two ($6{,}7 \cdot 10^{-11}$); the third is kept for the comparison. Value 6,72 and `answer` unchanged.

answers.py: unchanged. Checks: lint 0 errors (5 old length warnings), check_solutions ok, answers.py runs, check_i18n: no line about fy5-5.
