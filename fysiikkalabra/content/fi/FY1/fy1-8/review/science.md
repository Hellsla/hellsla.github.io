VERDICT: PASS
CONTENT-HASH: 259fae214dbc0e89
Mode: delta (three new `pysahdy` blocks in lesson.md, the worked-example knowns split into two paragraphs, inquiry.json presentation only)

## Blocking
- none

## Polish
- content/fi/FY1/fy1-8/lesson.md:398 — the theory defines a hypothesis as *perusteltu ja testattava*, but the model answer says "Kelpaa" on testability alone, and the statement gives no reason. Not wrong at this level (C), but it only half-matches the definition two lines above it — add a reason to the prediction ("Auto liikkuu vakionopeudella, joten …"), or have the answer note that a reason would make it a full hypothesis.

## Checked
- The `pysahdy` at line 615: $t \ge \Delta t/\varepsilon_\text{max} = 0{,}2\,\text{s}/0{,}020 = 10\,\text{s}$. Recomputed: 10,0 s, exact, so rounding to the safe side changes nothing. It uses the symbols and the direction ("vähintään") of the Kaava section.
- The new item agrees with the Kaava text: $5\,\%$ gives 4 s, $2{,}0\,\%$ gives 10 s. Both are recomputed and consistent with the same $\Delta t = 0{,}2\,\text{s}$.
- The `pysahdy` at line 412 (distance and batteries changed together): "Ei voi" is correct. It is the same example and the same reasoning as the paragraph before it, and it matches the glossary term *muuttuja*.
- The `pysahdy` at line 398: the falsifiability reasoning is correct and agrees with the glossary term *hypoteesi* (a measurable result that can turn out false).
- Worked example: splitting the knowns and the question into separate paragraphs leaves the numbers unchanged. $s_\text{min} = v\Delta t/\varepsilon_\text{max} = 1{,}68 \to 1{,}7\,\text{m}$ (rounded up), recomputed.
- Content hash checked at the start and the end: unchanged.
