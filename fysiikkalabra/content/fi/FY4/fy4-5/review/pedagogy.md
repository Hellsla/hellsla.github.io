VERDICT: PASS
CONTENT-HASH: df3ef99aaf2cf768

## Blocking

(none)

## Polish

- inquiry.json hook / exp-2 / reflect — the opening question asks about both pull and push ("kummassakin tapauksessa"), but the push case is only in the optional exp-2 and the optional reflect; on the core path pull is investigated and push is only mentioned in "Yleinen virhekäsitys" — make exp-2 (or the reflect) non-optional, or let exp-1's conclusion name the push case.
- inquiry.json pred-1, first option's feedback — "pystysuunnassa vaikuttavat kaksi voimaa ja narun voiman pystykomponentti" is garbled (that is three things, and the component is part of the rope's force) — "pystysuunnassa vaikuttavat paino ja tukivoima sekä narun voiman pystykomponentti: ne yhdessä ovat nolla."
- inquiry.json simulaatio "model" vs lesson.md Voimakuvion piirtäminen step 4 — the sim calls the rope's force $\overline{F}$ although the guide and example name it $\overline{T}$; the box explains it, but a student learning "each force its own symbol" meets two names for one force — use $\overline{T}$ in the pull case, or $\overline{F}$ also in the guide's example.
- inquiry.json exp-1 question — "how large is $F_y$" is the sim's own readout ($|F_y| = 50\,\text{N}$) and $F\sin 30^\circ$; the $G-N$ route adds a step but little reasoning. Ask a harder one: "what is $N$ at $45^\circ$ before you set it?" so the student uses the equation, then checks it.
- Sim at 390 px (captures #2, #33) — the force diagram occupies a narrow right half and its symbols are about 9 px; legible but small. The virhe figure (#7) is the same size. A taller or wider diagram on a phone would help.

## Checked

- Learning path: prerequisites suffice; slot goals and examples A, B, C, E, H, I covered, nothing extra.
- Predictions commit-first, wrong options' feedback repairs; exp-1 can refute both; the model box states "no friction".
- Theory that states N < G comes after Tutki: no premature disclosure.
- Force-diagram plan: identify, select, error, equations and draw (check-3, six criteria) all practised; distractors carry one named error.
- Figure descriptions (virhe, hissi-a to d) list arrows without saying which is right.
- Worked example: nine one-step stages, values correct; figures sit beside their paragraphs.
- Finnish: glossary terms and case after number+unit correct.
- Exit ticket tests the core ideas; core-path workload about one lesson.
- Packet's "sims" FAIL did not reproduce: `test_sims.py fy4-5` passes on all three pages.
