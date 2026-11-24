VERDICT: PASS
CONTENT-HASH: afa411dcc776f0f4

## Blocking

## Polish
- lesson.md:147 — the paragraph first says an integer's trailing zeros are ambiguous ($384\,400\,\text{km}$: you cannot tell whether it is to 100, 10 or 1 km), then gives the book's rule that a measured or rated value's trailing zeros are significant. The Moon distance is a measured value, so a student may read the two as clashing. The scope "Tämän kirjan tehtävissä" settles it, but only just. Fix (optional): "… tehtävissä annetun mitatun tai nimellisarvon loppunollat …", or a short "ellei tehtävä toisin sano".
- lesson.md:124,155 — conversion results such as $4{,}2\,\text{km} = 4200\,\text{m}$ now look like four significant figures under the new rule, though the datum has two. Line 124 already shows $4{,}2\cdot10^{3}\,\text{m}$, so this is a C-level simplification. Fix (optional): one clause saying a converted value keeps the original value's precision, or stop the chain at $4{,}2\cdot10^{3}\,\text{m}$.
- Carried over from round 1 and not part of this diff: the slider label at d = 0 (sim.js:997,1000), d0 = 119,0 AU against the brief's 119,7 AU (tell the teacher), and the aria-label "40 yksikköä" (lesson.md:116).

## Checked
- Diff: the new sentence agrees with docs/physics-guardrails.md "Values and significant figures" and CLAUDE.md (teacher P7, 2026-11-16). A time span or count the task sets, such as $10\,\text{min}$, is exact. A measured or rated value's trailing zeros are significant, and $230\,\text{V}$ has three.
- The new sentence agrees with the glossary entry "merkitsevä numero" (loppunollat mukaan lukien) and with the rules on the next line (an exact conversion factor $1000$ does not limit the result; $1{,}85\cdot0{,}92 = 1{,}702 \to 1{,}7\,\text{m}^2$).
- The change touches nothing else: the worked example (three figures from $30{,}1\,\text{AU}$), the "merkitsevat" choice and the $0{,}0250\,\text{m}$ check do not use the changed rule, and their correct options stay right. The reasonableness check "$30\,\text{AU}\cdot8{,}3\,\text{min} \approx 250\,\text{min}$" is an estimate, so its figures do not matter.
- Content hash afa411dcc776f0f4 was the same at the start and at the end.
