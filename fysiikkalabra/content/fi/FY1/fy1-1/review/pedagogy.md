VERDICT: FAIL
CONTENT-HASH: eed3551ade27dd66

## Blocking
- fy1-1/lesson.md:94 (Suuruusluokka kertoo karkean koon) — the removed sentence was the only place in the lesson text that taught where a number rounds up. The new text gives only "lähinnä lukua" plus two examples (1,7 -> 10^0, 8,8·10^3 -> 10^4); neither tests the boundary. Yet inquiry.json check-1 (Proxima Centauri, 4,0·10^16 m) and its feedback, the Etsi virhe item and exercise solutions (solutions.md:105, "alle noin 3") rest on "kerroin yli noin 3 -> seuraava kymmenpotenssi". A student without the rule must guess (on a plain scale 4 is nearer 0 than 10, so many will answer 10^16), and the check marks that wrong before the rule is ever taught. Only the glossary tooltip holds it. Fix: keep one sentence with no square root, e.g. "Jos kerroin a on alle noin 3, suuruusluokka on $10^{n}$, ja jos yli noin 3, se on $10^{n+1}$, koska kymmenpotenssien akselilla raja on lähempänä kohtaa $10^{n}$ kuin $10^{n+1}$ vain näin." (or simpler: "Kerroin 3 on likimain puolivälissä akselilla").

## Polish
- Simplifying was a good call for reading level; the rule just needs to return in one plain sentence.

## Checked
- Diff read in context: the definition, the Everest example (8,8·10^3 -> 10^4) and the rounding remark still read well in Finnish.
- Other uses of suuruusluokka (atomi-ydin ero, Linnunrata, worked example steps) need only exponents and are unaffected.
- Optional exp-3 (puoliväli of n values) uses the exponent midpoint, not the rule; unaffected.
- Glossary entry still states the "noin 3" rule, consistent with inquiry feedback.
