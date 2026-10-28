VERDICT: PASS
CONTENT-HASH: c4c4cfd59fc96576

## Blocking

## Polish
- lesson.md:64 — "Suhteen ratkaiseminen massan ja tilavuuden suhteen" (still) reads awkwardly — "Kun yhtälö ratkaistaan massan tai tilavuuden suhteen, saadaan kaksi muuta muotoa".
- lesson.md:7 — "Kaksi samankokoista kappaletta ovat eri painoisia, jos ne ovat eri ainetta" is not always true (jää and ruokaöljy share 920 kg/m³ in the lesson's own table) — "voivat olla eri painoisia".
- lesson.md:283 — "tai se näkyy suoran vakiotermi $m_0$" — "vakioterminä $m_0$".
- glossary.json "tiheys" still writes ρ = m/V — outside this lesson's files; align with the colon rule if the glossary is shown on the page.

## Checked
- Round-1 polish fixed: ennuste-1 feedback now `54 g : 20 cm³ = 2,7 g/cm³`; that is the only change since the PASS at d8159883.
- Notation: division as an operation written with `:` throughout (m : V, Δm : ΔV, V : ρ, (105,1 − 42,1) g : 80 cm³); `\cdot` only, no `×`/`\times`; remaining `/` are unit fractions (incl. m³ · m³/kg in Etsi virhe).
- Display formulas ρ = m/V, m = ρV, V = m/ρ correct; y = kx mapping and m_yht = ρV + m₀ correct; 1 g/cm³ = 1000 kg/m³ derivation correct.
- Worked example: m = ρa²L symbolic first, 7870 · 0,040² · 1,20 = 15,11 → 15 kg (2 s.f. from 4,0 cm), check 7,9 · 1,9 kg ≈ 15 kg.
- Inquiry recomputed: Al ratios 2,68/2,72/2,69/2,71/2,69 (mean 2,70), differences; metal 8,96 (mistakes 0,112, 7,17; one-row 8,97); liquid increments 15,8/15,6/16,1/15,5, ratios 2,9/1,8/1,5/1,3, slope 0,79, m₀ 42 g.
- siirto 2671 → 2,7·10³ kg/m³ (mistakes 2,67, 984, 2,67·10⁶); tarkistus-1 5,0 and 5,4·10⁻⁴ m³; tarkistus-2 4,00 kg (mistakes 4·10⁶, 100); Etsi virhe 675 000 vs 0,675 kg; exit ticket 2,7 g/cm³ and 1,5 kg.
- Figures to scale: cube bars 9,5 : 51,5 : 150 = 5,0 : 27 : 79 g; graph lines at 50 cm³ give 50/135/394 g; displacement 40 → 70 ml.
- Density table values correct (ice 920, ethanol 790, lead 11 300, gold 19 300).
- Hash identical at start and end.
