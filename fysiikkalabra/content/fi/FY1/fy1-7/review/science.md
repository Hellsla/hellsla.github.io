VERDICT: PASS
CONTENT-HASH: d8159883d7386560

## Blocking

## Polish
- inquiry.json:59 — ennuste-1, wrong option's feedback: `54 g : 20 cm³ = 2,7 g` equates g/cm³ with g (pre-existing, carried through the colon sweep) — write `= 2,7 g/cm³` (or `54 g : 20 = 2,7 g`).
- lesson.md:64 — "Suhteen ratkaiseminen massan ja tilavuuden suhteen" reads awkwardly — e.g. "Kun yhtälö ratkaistaan massan tai tilavuuden suhteen, saadaan kaksi muuta muotoa".
- glossary.json "tiheys" still writes ρ = m/V — outside this lesson's files; align with the colon rule if the glossary is shown on the page.

## Checked
- Notation sweep (a196d94): every `/` operation in lesson.md, inquiry.json and exit-ticket.json became `:` with operands intact (m : V, Δm : ΔV, (105,1 − 42,1) g : 80 cm³, 0,50 kg : 920 kg/m³, V : ρ); no expression became ambiguous; no `×` or `\times` left; remaining `/` are unit fractions only.
- Display formulas ρ = m/V as \frac, ρV, V = m/ρ correct; y = kx mapping and m_yht = ρV + m₀ correct.
- Worked example: 7870 · 0,040² · 1,20 = 15,1 kg → 15 kg (2 s.f.), check 7,9 · 1,9 kg ≈ 15 kg.
- Inquiry numbers recomputed: Al ratios 2,68–2,72 (mean 2,70), differences, metal 8,96 (mistakes 0,112, 7,17), liquid increments and ratios 2,9/1,8/1,5/1,3, slope 0,79, siirto 2671 → 2,7·10³ (mistakes 2,67, 984, 2,67·10⁶), tarkistus-1/-2 and their mistakes, Etsi virhe 0,675 kg.
- Figures to scale: cube mass bars (15,8:1), graph lines/points and slope triangle (Δm ≈ 157 g), displacement 40 → 70 ml on the 28 px/10 ml scale.
- Density table values correct; exit ticket correct.
- Hash identical at start and end.
