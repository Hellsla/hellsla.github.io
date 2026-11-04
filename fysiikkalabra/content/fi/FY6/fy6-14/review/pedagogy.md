VERDICT: PASS
CONTENT-HASH: 33436c68cf95a6c5

## Blocking
(none)

## Polish
- lesson.md "Diodi päästää virran..." — the new clause "kunhan jännite pysyy alle diodin läpilyöntijännitteen" uses a term the lesson never defines (the glossary has läpilyöntilujuus, a field strength) — "kunhan jännite ei ole suuri; liian suuri estosuuntainen jännite voi rikkoa diodin".
- Round 1 points still open: inquiry.json koe-2 intro wording ("Missä lähteen jännite on estosuunnassa?"); tarkista-2 uses the lesson's own panel (answerable by recall); figure label "maksimiteho" vs "maksimitehopiste"; the ennuste-2 prompt already names both extremes.
- Workload stays near the upper limit; keep koe-4 and koe-5 optional.

## Checked (round 2, diff cab03926)
- siirto: the 1,65 distractor was a wrong value (5,2 V x 0,30 A = 1,56); fixed to 1,56, so the feedback "kerroit erotukset" now matches the number a student would get.
- siirto solution now answers 24,8 W with a correct sig-fig justification, matching the accepted answer 24,76 W.
- The reverse-bias statement now has its caveat, consistent with the model note (breakdown not modelled, real LED about 5 V); the added bulb sentence ties back to the opening question.
- Efficiency paragraph now says P is the power at the maximum power point, so the 15 % figure is not read as any operating point.
- Lesson path, predictions, experiments, figures and exit ticket are otherwise unchanged and still fine.
