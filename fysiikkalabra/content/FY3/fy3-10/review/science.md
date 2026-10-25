VERDICT: PASS
CONTENT-HASH: 32171daf1820acd1

## Blocking

## Polish
- inquiry.json:124 (pred-3, Bea) — "Kokeen 1 perusteella … sama paine vaatii saman hiukkasmäärän": Koe 1 uses equal-mass particles only, so it cannot show that the particle mass drops out; that comes from the model — say "Kokeen 1 ja hiukkasmallin perusteella".
- inquiry.json:340/345 (check-1) — "sama hiukkanen ehtii seinästä seinään lyhyemmässä ajassa" is true for the walls the piston moves towards; on the other walls the hit rate per unit length rises because the gas is denser — add "ja hiukkasia on tiheämmässä".
- solutions.md:47 (L2-01) — "noin 6 % liian suuren paineen" is plausible for O₂ (Z ≈ 0,94) but has no source; "muutaman prosentin" is safer.

## Checked
- answers.py, exercises.json and my own formulas agree for all 12 exercises (largest rounding offset 0,4 %, inside the 2 % tolerance).
- Worked example: n = 0,2073 mol, m = 0,829 g, air 6,01 g, molar volume 24,1 l. The SVG labels (0,21 mol, 0,83 g, 6,0 g) match.
- siirto: 91 200 mol and 2645 kg. The listed mistakes (9869 kg if T stays in °C, 2,64 kg if p stays in kPa) are right. 20 °C air weighs 3,37 t, so the difference is about 700 kg.
- virhe (1,2 → 0,083 mol), check-2 (3,0; mistakes 2,25 and 1,69) and the exit ticket (0,601 mol) recompute correctly.
- Feedback physics for pred-1 to pred-3 is right: at the same T, the larger hit rate (∝ v) times the momentum per hit (∝ mv) gives p ∝ m⟨v²⟩ ∝ T, whatever the particle mass.
- The interpret table's pV/(NT) column follows from its own rows (1,05 / 1,00 / 0,98 / 0,98 / 0,99).
- sim.js: impulse per unit perimeter per unit time and P_REF = NkT/A follow 2D kinetic theory. I ran the sim in Chromium (10 × 2 s runs per state). Measured p matches pV = NkT within 0,1 % in 9 states. In 300 → 600 K the hit rate grows 1,41× (93,6 → 132,2 1/s) and p grows 2,00×. At N = 20 the scatter is about ±10 %, as the note says.
- exp-1 and exp-2: the start states, locked parameters and slider ranges isolate the varied quantity. simState exposes pMeasured, pPredicted and hitRate.
- Scope and conditions: Kelvin temperatures, total pressure in the formula, gauge pressure cancels in the difference (L3-03), and the model fails at high p and low T.
