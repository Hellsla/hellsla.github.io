VERDICT: PASS
CONTENT-HASH: bff7149aaf35caf4
## Blocking

## Polish
- lesson.md Ydinajatus, paragraph "Boylen laki voidaan todentaa kokeellisesti …" — about 150 words with five steps (setup, slowness, table column 1/V, line, sim). Split after "…huoneenlämpöön." so the graph argument ("Kun tulokset piirretään …") is its own paragraph, or add a ### heading "Boylen lain todentaminen".
- inquiry.json sim `text` and siirto prompt, "ideaalikaasua" / "pullon ilma on ideaalikaasua" — the term is used before the lesson (or the course so far) defines it; add half a sentence at first use ("ideaalikaasu on harva kaasu, jonka hiukkaset vaikuttavat toisiinsa vain törmätessään").
- inquiry.json kertaus, pred-1/2/3, siirto, exit ticket — plain "3,0 cm²", "100 kPa", "50 ml", "72,0 kPa", "1,50 litran" sit next to LaTeX values (e.g. `$3{,}3 \cdot 10^{8}$ N`); convert the plain numbers with units to one style.
- inquiry.json pred-1/pred-2 — prompts say "50 ml ilmaa" and "25 ml" while feedback quotes "200 000 Pa"; keeping Pa and kPa in one thread is correct but the switch is abrupt. Say "200 000 Pa eli 200 kPa" at first mention.
## Checked
- Path: airplane crisp-bag hook -> optional retrieval (p = F/A) -> three predictions (p halves V, isobaric heating by kelvin ratio, graph shape) -> sim with locked mode/T -> isobaric experiment with the gamma = 1/293 link to the previous chapter -> interpret table of syringe data with one outlier -> conclusion -> theory -> staged example -> checks. Hook question answered in the reflect (101/78) and Johtopäätös. Slot goals (Boylen todentaminen, kääntäen verrannollisuus graafisesti, uusi sarake 1/V) met.
- The sim computes pV/T = vakio, and the page says so (calc, pred-3 feedback, Johtopäätös); the invented syringe data with a real, explainable outlier (fast compression heats) supplies the genuinely testable evidence. Good design.
- Numbers re-derived: pV = 5,00 J; 60,2 ml and 0,171 ml/K; 3,4·10⁻³ = 1/293; syringe rows 5040/5050/5040/5430/5040 (outlier +8 %); virhe 250 vs 40 kPa; siirto 1,07 l (2,1 and 0,00107 distractors); check-2 120 kPa (108, 0,12); exit tickets 160 kPa and 308/280 = 1,1.
- Each choice item still has exactly one correct option; distractor feedback repairs the misconception (celsius ratio, "50 % less volume -> 50 % more pressure", p ∝ V, gas weight).
- Guardrail edits (kireä pussi: pressure slightly above cabin pressure; vapaasti laajeneva pussi) are consistent in Ydinajatus, Esimerkki and reflect.
- Example: seven one-step stages, units cancel stated, sig-figure rationale and pV check.
