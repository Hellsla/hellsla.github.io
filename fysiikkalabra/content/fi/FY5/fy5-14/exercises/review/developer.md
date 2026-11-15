VERDICT: DONE

Round 1, exercises (work queue 18 + 19), same changes in fi, en and fi-easy.

**Fixes (queue 18)**
- fy5-14-L1-04, Järkevyys: (415 − 397)/415 ≈ 4,2 % → 4,3 % (18/415 = 4,34 %). The number is used nowhere else; answer unchanged.
- fy5-14-L1-10, Vastaus: justification rewritten: "1400 Hz eli 1,40 · 10³ Hz, kolme merkitsevää numeroa kuten kuvaajasta luetussa perustaajuudessa 200 Hz" (P7b: plain 1400 Hz would read as four figures). Value, `answer` and answers.py unchanged.

**New task (queue 19)**
- fy5-14-L2-09 = teacher's FY5-A3 (Yle, 440 vs 432 Hz), kind data + reasoning, level 2, last. Box: part a) wavelength at 432 Hz, 0.794 m, tolerance 0.02 (answers.py: 343/432; 440 Hz gives 0,780 m in the solution).
- Solution: full rows for a), then Kohta b), c), d) and "Mallin ja aineiston rajat". b) uses beats (8 Hz) and the article's 415 Hz semitone (8 Hz ≈ a third); no 2^(1/12).

**Tarkennukset**
- Teacher's title is the opening question; "432 hertsin" written as LaTeX quantity; a closing sentence names the box value. Parts and order unchanged.
- fi-easy: one sentence explains "viritystaso".
- en: "(in Finnish)" and a two-sentence summary of the claims (no verdict).

**Open**
- Lint warning: L2-09 solution is 626 words (four parts; guideline 100–220). Not shortened.
- Dates in the solution are written out (lint reads 25.1.2020 as a decimal point).
- check_layout at 360 px not run (brief forbids builds); only lint, check_solutions, answers.py, check_i18n (all without errors).
