VERDICT: PASS
CONTENT-HASH: 63c6cf4b2739bc04

## Blocking
(none)

## Polish
1. lesson.md "### Aktiivisuus" — "pulsseja niistä säteilykvanteista, jotka osuvat sen anturiin" — alfa- ja beetahiukkaset eivät ole kvantteja, ja kuvateksti sanoo "hiukkasia". Fix: "niistä säteilyhiukkasista ja -kvanteista, jotka osuvat sen anturiin". (Minor)
2. lesson.md "Lähde:" paragraph after the half-life table — the I-131 value range (8,021–8,025 d) and rounding note is detail a 17-year-old does not need; cut to the source and "8,02 d". (Minor)
3. inquiry.json `johtopaatos` criterion 4 ("Kutsun simulaation lukuja mallin arvoiksi enkä mittauksiksi") — assesses vocabulary, not what the question asks (halving, size effect, law vs chance); replace with a criterion on the 20 vs 1600 comparison using numbers. (Minor)
4. inquiry.json `sovitus` solution "Järkevyys" — compares half of the background-subtracted start (188) with raw counts 211 and 165 that still include background; subtract about 5 from both (about 206 and 160, giving about 69 s). Also the exercise relies on one external program with no fallback if a student lacks it (Minor)
5. Activity is only seen through N: the hook speaks of activity, but no investigation or check takes A = λN to a count (the bridge is one prose sentence), and only `virhe` (optional) uses N = A/λ. A short line in the `sovitus` text or a check item linking pulse count to N would close it. (Minor)

## Checked
- Learning path: random single nucleus → regular large set → T½ → λ and A → fit; matches the three slot goals, nothing extra; the Miksi question is answered by the Ydinajatus and the reflect.
- Predictions (`ennuste-1`, `ennuste-2`): wrong options are real misconceptions (all gone in the second half, size-dependent rate, neighbour-triggered decay); feedback cites model values, repairs the idea. Experiments can refute them (koe-2/3 vary only the series, N0 locked).
- Simulation is a counted result, not a formula readout; model values are named as such; 5 fixed series is a stated limit.
- Worked example: 7 stages, one step each, arithmetic verified (0,17754, 97,6 MBq), reasonableness check bounds the result.
- Etsi virhe and `mistakes` lists name real errors (1/T instead of ln2/T, no B term, 1/C); numbers verified (31 %, 6,2·10^10).
- tarkistus-1 tests memorylessness with the "vuorossa" and 1/16 distractors; tarkistus-2 needs the graph; solutions follow the 7 steps.
- Exit ticket tests the halving and the constant B; the core idea of randomness is covered in the checks.
- Finnish: terms from the glossary, case after number+unit correct; reading level fits.
- Workload: core path fits an hour; the software fit plus optional items lean long. Captures in review/shots not opened; layout is covered by the deterministic checks.
- Exercises not judged (separate set).

## Scores
Dimensions of docs/EDITORIAL_QUALITY_STANDARD.md (all findings above Minor):
- 2 Conceptual clarity: 5 — memorylessness, per-nucleus probability and the law/chance split are stated and tested.
- 3 Pedagogical effectiveness: 4 — strong sequence; A = λN and N = A/λ get little practice in the core path.
- 4 Exercise quality (inquiry tasks and checks): 4 — good misconception feedback; the exit ticket leaves randomness to the checks.
- 5 YO readiness: 4 — graph reading, fit and a numeric chain all present; a fit task depends on one program.
- 6 Experimental reasoning and data analysis: 5 — locked variables, refutable predictions, background term explained, fit compared with the literature value.
