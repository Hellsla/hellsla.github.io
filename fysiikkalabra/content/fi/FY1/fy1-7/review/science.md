VERDICT: FAIL
CONTENT-HASH: bdc9369e9ae219f6
## Blocking
- lessons/FY1/fy1-7/answers.py:29 — the key `fy1-7-inq-tarkistus` computes the Etsi virhe item (675 g), and the numeric check `tarkistus-2` (pine cube, answer 4.0 kg) is not computed anywhere, so answers.py does not cover every numeric task — add `a["fy1-7-inq-tarkistus-2"] = 500 * 0.200**3` (4.00 kg) and rename the 675 g line to `fy1-7-inq-virhe` (or drop it, since it is not a numeric task).
- content/fi/FY1/fy1-7/inquiry.json:121 (and :129) — "poikkeavat toisistaan alle prosentin" / "Vaihtelu on alle prosentin" is false: 2,68 and 2,72 differ by 1,5 %; each ratio is within 1 % of the mean 2,70 — write "poikkeavat keskiarvostaan 2,70 g/cm³ alle prosentin" (and the same in :129).
## Polish
- content/fi/FY1/fy1-7/solutions.md:99 — L3-01 justifies two figures by "taulukon tarkkuus", but the table gives three (8960, 2,70); either answer 3,32 or justify the rounding otherwise; the check 9000/2700 repeats the same division rather than checking it.
- content/fi/FY1/fy1-7/lesson.md:50 — 7870/500 = 15,7: "noin kuusitoista kertaa" is closer than "viisitoista".
- content/fi/FY1/fy1-7/lesson.md:216 — the difference of two readings does not always have fewer significant figures than either; say "voi olla vähemmän" or tie it to the absolute uncertainty (two readings' errors add).
- content/fi/FY1/fy1-7/lesson.md table — ruokaöljy (920) is listed after vesi (1000); sort by density.
## Checked
- All 12 exercises, metalli 8,96, siirto 2671→2,7·10³, tarkistus-2 4,00 kg, virhe 0,675 kg and the worked example 15,1 kg recomputed independently: all match answers.py/stated answers; tolerances admit correctly rounded answers.
- Every mistake value (0,112; 7,17; 2,67; 984; 2,67·10⁶; 4·10⁶; 100) reproduces the named error.
- Alumiini ratios, neste increments (15,8/15,6/16,1/15,5), m/V ratios and slope 0,79 g/cm³ correct; intercept = bottle mass correctly explained.
- Correct options of kertaus, both predictions, three interpret items, virhe and tarkistus-1 are right; wrong-option feedback physics sound.
- Graph figure to scale (6,88 px/cm³, 0,58 px/g): water, Al, Fe lines and ΔV = 20 cm³, Δm ≈ 157 g triangle correct.
- Cubes figure: masses 5,0/27/79 g for 10 cm³ and bar lengths proportional; displacement figure 40 → 70 ml on a 2,8 px/ml scale.
- Density table values within rounding of handbook values; unit conversions 1 g/cm³ = 1000 kg/m³, dm³, ml correct.
- Solutions complete in seven parts, symbolic before substitution; rounding justified (except L3-01).
- Scope: m = ρV as proportional/linear model fits FY1 slot and central contents; no simulation.
- Exit ticket answers correct.
