VERDICT: FAIL
CONTENT-HASH: f6b7111742cce851

The lesson delivers its three goals: it covers the three state changes, describes the syringe-and-manometer experiment, and builds the 1/V column and the straight-line test. The lesson text, the SVG, L2-03, exit-ticket Q2 and the sim (table with a 1/V column, "Piirrä p 1/V:n funktiona") all tell the same story, and the sipsipussi hook comes back in the worked example. At 795 words it is the same length as the reviewed FY3 lessons (700–1200; `_gold` is still a stub), and nothing is redundant. One gap blocks publication: the main skill exercise asks for a unit that the lesson never teaches. The issues already sent to the fixer (gas weight, L2-04 volume, SVG 1/V points) are not repeated here.

## Blocking
- exercises.json:64 (L2-03) — the task asks for the slope pV "jouleina", but the lesson never says that Pa·m³ = N/m²·m³ = N·m = J. The solution has to use 1 kPa·ml = 0,001 J, and that fact is first taught in fy3-10 (its lesson.md:19). A student cannot answer this level-2 task, which is the experimental goal of this lesson, from what this lesson teaches. — Either add one sentence after lesson.md:19 ("pV:n yksikkö on Pa·m³ = N·m = J") or ask for the slope in kPa·l (answer 2,0) or kPa·ml, the unit the sim's table already uses.

## Polish
- lesson.md:12 — the hook is answered at the end of the temperature paragraph, but the bag swells because of Boyle's law (isothermal). — Move the sentence to the end of :8 or into the example at :52.
- lesson.md:10 / :19 — the goal's form p = vakio·1/V never appears explicitly, so the reason the slope equals pV is left implicit. — Add inline $p = pV\cdot\tfrac{1}{V}$ and compare it with y = kx.
- lesson.md:12, :21–25 — the V/T and p/T laws carry 5 of 12 exercises (L1-04, L1-05, L2-02, L2-04, L3-02) and exit-ticket Q3, but they get no worked calculation. — In the °C misconception at :55, show the step V₂ = V₁·T₂/T₁ with its numbers.
- lesson.md:10 — the text never sends the student to the sim, which reproduces exactly this experiment. — Add "Kokeile simulaatiossa: tallenna mittauksia ja valitse Piirrä p 1/V:n funktiona."

## Checked
- The lint reports 0 errors and 0 warnings; the hash was the same at the start and at the end of the review.
- The curriculum goals (state changes, Boyle experiment, the 1/V column) are each covered in the theory, the exercises and the exit ticket.
- The goals and glossary in meta.json match curriculum.json, and all five terms are in glossary.json.
- The section structure matches the gold template; the length is in line with fy3-1…fy3-6.
- No exercise repeats the worked example (the bag expanding at lower pressure).
- The level counts are 5/4/3, and the level-3 tasks combine ideas (hydrostatic pressure, gauge pressure, the pump stroke).
- Exit-ticket Q3 reinforces the °C misconception at lesson.md:55.
- The sim spec's processes, ranges, table columns and 1/V toggle match the lesson's story.
- The scope stays within FY3: no pV = nRT (fy3-10) and no vectors.
