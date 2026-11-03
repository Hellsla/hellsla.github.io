VERDICT: FAIL
CONTENT-HASH: 73a8167482140fc3

## Blocking
- lesson.md:79, 110, 179, 183, 185 (kulma aria), 252, 256; inquiry.json:10, 344, 350, 361 — **A (definition, consistency).** The round-1 polish replaced the physics term *vaikutuskohta* with *otekohta* (a hand's grip point) everywhere and redefined it at lesson.md:110 as "kohta, jossa voima vaikuttaa kappaleeseen". This (1) applies "otekohta" to a weight, which nothing grips: siirto hint 2, mistake feedback and solution say "painon otekohdan vaakasuora etäisyys" (inquiry.json:344, 350, 361); (2) attributes the term to FY4 in the prior-knowledge line "Voimalla on suuruus, suunta ja otekohta (luku *Vuorovaikutus ja voima…*)" (inquiry.json:10), whereas FY4 uses *vaikutuskohta* (9 FY1/FY4 lesson files, *otekohta* in none); (3) contradicts the glossary's *vääntövaikutus* ("…suunnasta ja vaikutuskohdasta"), which FY5 later chapters will build on. — Fix: keep *vaikutuskohta* as the physics term in the theory, summary, misconception, kulma caption, prior line and siirto (weight: "painon vaikutuskohdan" or "puomin keskikohdan"); keep *otekohta* only where a hand grips (sim, experiments, wrench tasks), introduced once, e.g. lesson.md:110 "…vaikutuskohdan (avaimessa käden otekohdan) kautta…". This also settles the pedagogy note (one physics term, the grip word tied to it).

## Polish
- inquiry.json:254 (exp-2 distractor "voiman otekohta on kauempana") — fine for a hand pull; leave, or write "vaikutuskohta" with the rest.

## Checked
- Diff 6d0c7fa..HEAD read in full; no number, formula, option correctness or sim code changed.
- Round-1 polish taken: fixed-axis condition in Kaava text and Tiivistelmä; cosine feedback now "$Fd\cos\alpha$ … varren suuntaista komponenttia" (correct); conclusion "saman mutterin yritykset"; check-2 "käsien voimat kiertävät pyörää yhdessä vastapäivään".
- Example Järkevyys rewording keeps 84 Nm ≥ 80 Nm logic.
- figures.py changes are label positions only (ovi: "sarana", $\overline{F}_1$); geometry unchanged.
- Round-1 recomputation of every lesson number stands (no data changed).
