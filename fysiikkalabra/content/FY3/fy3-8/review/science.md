VERDICT: FAIL
CONTENT-HASH: 9abea8307a52e0cc

## Blocking
- solutions.md:79 (fy3-8-L2-03, Järkevyys) — "Todellisuudessa myös naapurikisko pitenee, joten rako sulkeutuisi jo alemmassa lämpötilassa" is wrong. On a track of identical rails each rail end moves ΔL/2, so a gap closes by ΔL/2 + ΔL/2 = ΔL, which is exactly the task's assumption. The check teaches a false correction. — Delete it, or replace it with: "Todellisuudessa kummankin kiskon pää liikkuu raon suuntaan ΔL/2, joten rako sulkeutuu juuri, kun kisko on pidentynyt raon verran, kuten tehtävässä oletettiin."

## Polish
- solutions.md:34 (L1-04) — "Säiliö ei rajoita laajenemista, koska kyse on vain veden tilavuuden kasvusta" is circular. Water's γ also varies strongly over 12–32 °C (from about 0,12 to 0,32·10⁻³ 1/K). — Note that 0,21·10⁻³ 1/K is the 20 °C value and roughly the mean over the range.
- inquiry.json:397 (check-2, Periaate) — "joten verrannollisuus pätee eikä sauva muuta olomuotoaan" does not follow from the doubling. — Drop the clause after "pätee".
- solutions.md:99 (L3-01) — "alle teräksen sulamisen" is too loose to count as a check. The forward check before it is enough, so drop this clause or state a real bound.
- inquiry.json johtopaatos model — gives "6,0 mm" where the predictions' feedback says 6,00 mm. Make them match.

## Checked
- One script: all 12 answers match answers.py and exercises.json within tolerance (max 0,8 %).
- Inquiry numbers: siirto 44 mm (43 with glass), mistakes 0,044 and 110; check-2 23·10⁻⁶ 1/K from both columns, mistakes 46 and 15,3; Etsi virhe 28 vs 1,8 mm; pred 6,00 and 12,0 mm; interpret table; exit ticket 21 mm.
- Worked example: 86 mm and 0,072 %, with correct two-figure reasoning.
- Rounding follows NOTES §2 in every solution: differences of whole-degree readings, Δα = 5,0, 475−18 to tens, Δd = 0,090 mm.
- Physics: asymmetric-potential micro-model, γ≈3α, the hole grows, the bimetal bends toward steel, the 4 °C anomaly, the table values.
- sim.js implements ΔL=αL₀ΔT from 20 °C, states the ×100 exaggeration and discloses the symmetric vibration. Its chart matches α in the capture.
- exp-1 and exp-2 each lock the two other parameters, and the simState keys exist. Everything is within FY3 scope.
