VERDICT: PASS
CONTENT-HASH: 362a88b85a61f5f1

## Blocking

## Polish
- lessons/FY1/fy1-3/lesson-answers.py:31,35 — the code comments still say "relative error" for Δt/t̄·100 % — rename them to "relative uncertainty" to match the lesson's term (comment only).

## Checked
- Round 2: `git diff HEAD~2` changes only the first Tiivistelmä bullet (lesson.md:536). It now says "Jokaiseen mittaustulokseen liittyy epävarmuutta. Virhettä ei yleensä tunneta." This is right by the guardrails (error unknown and signed, uncertainty its estimate) and worded as in the Ydinajatus (lesson.md:282) and content/fi.
- Round 1 full review still holds for the unchanged rest. It was checked against content/fi/FY1/fy1-3 and found the same in physics. "Suhteellinen epävarmuus" ε = Δx/x̄·100 % is used everywhere, and no "suhteellinen virhe" is left in student text. The terms follow the measurement guardrails: virhe, epävarmuus, resoluutio, half the range as a scatter estimate, and the outlier procedure.
- I recomputed every number in one script and all agree. Worked example: 3,1817 s, 0,12 s, 3,8 %. Figures: 2,407 s, 2,594 s, 47,5 g. Karkea: 0,19 s, 0,09→0,62 s. Ice: 1,5 °C, 0,1 °C. Coins: 5,44 g and the mistakes. Check-2: 2,08 %. Exit ticket: 19,9 g, 1,99 %. Sim experiments 1–3: −0,22/+0,076/−0,0005 s, 0,30 s, ratio 6,18.
- Every choice has exactly one correct option, every distractor's feedback says why it is wrong, and the locked parameters isolate the varied one.
