VERDICT: PASS
CONTENT-HASH: ce39622129de7cc0

## Blocking

## Polish
- solutions.md:34 (L1-04, Periaate) — "Säiliö ei rajoita laajenemista, koska kyse on vain veden tilavuuden kasvusta" is circular, and the real reason the plain γ applies is missing: 12–32 °C is above 4 °C, so the water expands normally. — Say that, and that 0,21·10⁻³ 1/K is the 20 °C value (the true growth over 12–32 °C is about 0,45 %, near the 0,42 % computed).
- inquiry.json:397 (check-2, Periaate) — "joten verrannollisuus pätee eikä sauva muuta olomuotoaan" does not follow from the doubling (carried from round 1). — Drop the clause after "pätee".
- solutions.md:99 (L3-01, Järkevyys) — "alle teräksen sulamisen" is too loose to count as a check (carried). The forward check before it is enough. — Drop the clause.
- inquiry.json:226 (johtopaatos model) — "6,0 mm" where the predictions' feedback says 6,00 mm (carried). — Write 6,00 mm.
- solutions.md:59 (L2-01, Järkevyys) — "Suuri sallittu muutos tai pieni lämpötilaero sallisi pidemmän putken" states a trend, not a check of this result. The forward check carries the stage. — Optional: drop it, or compare with a typical straight run of a district-heating pipe.

## Checked
- One script: all 12 answers agree with answers.py and exercises.json (largest deviation 0,8 %, within tolerance). Every intermediate and Järkevyys number is right: 0,048 %, 0,10 %, 0,0225 % and 0,45 mm, 49,9 mm, 0,15 %, 1,08 and 1,53 mm, 2,4 % and 0,09 %, ratio 26.
- Round-1 Blocking fixed: L2-03 now says that each rail end moves ΔL/2, so the gap closes by ΔL, which is the task's assumption. Correct.
- Every solution has the seven stages. Each principle fits and gives its reason (rigid solid that stays solid, free expansion, γ≈3α from three directions, a hole scales like the body, a fixed end puts all of ΔL at the gauge). Every unknown is solved in symbols before substitution.
- Rounding follows NOTES §2: differences of whole-degree readings (40, −45, 80, 42, 30, 25 K) have two figures, and 100 K has three. Δd = 0,090 mm and Δα = 5,0 have two figures each. 475 − 18 is rounded to tens (460). Each Vastaus names the datum that really limits the figures.
- Worked example: seven stages, ΔT = 60 K, 86,4 → 86 mm with two figures from α and ΔT, 0,072 %, and the estimate 60 mm is a real order-of-magnitude check.
- Inquiry: siirto 44 mm (43 mm with glass, ratio 41), its mistakes 0,044 and 110, its Vastaus and Järkevyys; check-2 23·10⁻⁶ 1/K from both columns, mistakes 46 and 15,3; Etsi virhe 28 vs 1,8 mm (×15, 0,7 %); predictions 6,00 and 12,0 mm and 0,0600 %; the olomuodot table (0,36, 2,1, 11, 34 cm³); air/steel ≈ 94 ("noin sata"); exit ticket 21 mm.
- Physics: the asymmetric-potential micro-model, the bimetal bending toward the steel (a 1 mm strip's tip moves about 0,75 mm, far more than 20 µm), the 4 °C anomaly, and the table coefficients (air 1/293 K).
- sim.js implements ΔL = αL₀ΔT from 20 °C, states the ×100 exaggeration and the symmetric drawn vibration, and exp-1 and exp-2 each lock the other two parameters. It is unchanged since round 1, and the content stays within FY3 scope.
