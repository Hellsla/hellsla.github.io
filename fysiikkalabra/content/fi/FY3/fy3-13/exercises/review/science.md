VERDICT: FAIL
CONTENT-HASH: 5c05f2a4a93f43a5

Round 2 (exercise bank): round-1 Blocking item and the fix diff (HEAD~2..HEAD~1) re-checked; new tasks re-read in full.

## Blocking
- lessons/FY3/fy3-13/answers.py:31 (fy3-13-L1-07) — A: `round(-195.8 + 273.15, 1)` prints 77.3, not 77.4 (the float sum is 77.34999…), so answers.py now disagrees with exercises.json:77 (77.4) and solutions.md (77,4 K). The answer check passes only through the 2 % tolerance. — Fix: `round(-195.8 + 273.15 + 1e-9, 1)` (or `float(Decimal("-195.8") + Decimal("273.15")).quantize…`), and check that it prints 77.4.

## Polish
- exercises.json:69 (L1-06, distractor "hiukkaset pysähtyvät kokonaan") — the new feedback "ei siitä, että liike pysähtyisi sinulle tutun mallin mukaan" is hard to parse and no longer says plainly what the guardrail says. Suggest: "Väärin: absoluuttisessa nollapisteessä hiukkasten energia on pienimmillään, mutta liike ei lopu kokonaan."
- solutions.md:237 (L3-05) — "desimaali annetaan, jotta tulos vastaa vastauskentän arvoa" is not a physics reason. Either give −17 ± 3 °C as the result, or justify −17,5 ± 2,7 °C as unrounded intermediate values.
- exercises.json:74 (L1-07) — "kind" was removed rather than corrected; if the field is expected for every new task, use ["data"] or the bank's substitution kind.

## Checked
- Round-1 Blocking resolved in the task: L1-07 answer 77,4 K, Vastaus "kymmenesosan tarkkuudella kuten −195,8 °C; tarkka 273,15 ei rajoita", Sijoitus 77,35 ≈ 77,4 K; back-check −195,75 ≈ −195,8 °C right. (answers.py still off, see above.)
- Round-1 Polish resolved: L2-06 now −302 °C "vain noin kahden numeron tarkkuudella (−3,0·10² °C)"; L3-05 names the limiting difference −6,4 kPa; formula T = θ + 273,15; L2-05 "graph" kind removed; "keskiarvon satunnaista virhettä", "75 °C:n levyiseltä väliltä" and midpoint wording fixed.
- One script recomputed: L2-05 θ0 −274,46 °C; L2-06 −302,2 °C; L2-07 −370 °C, steps 6,6/5,4/4,0 kPa; L3-04 −242,5/−302,0 → 29,75 and −258,44/−279,90 → 10,73 °C; L3-05 k 0,3660, −17,49 °C, Δθ 2,73 °C. All match answers.py (except L1-07) and the solutions.
- L1-06: exactly one correct option ("alin mahdollinen lämpötila…"); the other three distractors wrong and their feedback right; Mallivastaus keeps "ei pidä ymmärtää niin, että hiukkaset pysähtyisivät" (guardrail met).
- L1-08: options reordered and reworded; one correct option, interpolation / repetition / every-point distractors wrong, feedback right.
- L2-07: "Ryhmä epäilee vuotoa… Tukeeko taulukko epäilyä?" — the falling slopes (0,33 → 0,27 → 0,20 kPa/°C, steps ≫ ±0,5 kPa) do support it; solution answers that question.
- Aligned Sijoitus blocks: every line recomputed, values unchanged.
- No Newton's laws or other FY4 content; levels and plan coverage unchanged and fit.
