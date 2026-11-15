VERDICT: PASS
CONTENT-HASH: 7d5645fe39460f43

## Blocking

## Polish
- inquiry.json `kertaus` 4th option — "$3{,}3 \cdot 10^{8}$ N" leaves the unit N outside LaTeX; and volumes in pred-1, pred-2, exp-1 intro, check-3 ("50 ml", "25 ml", "30,0 ml") are plain number+unit text, against the house rule that every number with its unit is LaTeX (`$50\,\text{ml}$`). Lint passed, so convert by hand.
- inquiry.json workload — two required predictions, two experiments, the syringe table, a conclusion, and theory that also covers isobaric, isochoric and absolute zero is close to an hour and a half; mark `exp-2` and `pred-2` optional (Core path) or move the absolute-zero part to the exp-2 question only, unless the slot's goals need it.
- inquiry.json `pred-3` — shares exp-1 with pred-1 and needs `min` 3; a student who records only two rows never sees either verdict. Lower `min` to 2 or state in exp-1's intro that three rows are needed.
- inquiry.json `johtopaatos` — `after` lists only exp-1 but the prompt needs the `ruisku` table; fine in order, but add "ruiskuaineisto" to the criteria so the poikkeava rivi is assessed (criterion 5 does this; criterion 4 repeats model-vs-measurement, merge them).
- lesson.md Ydinajatus — three figures and five paragraphs before the Kaava; keep, but the isobaric/isochoric paragraph could be its own `###` so the Boyle thread (hook → micro-model → experiment) reads in one run.

## Checked
- Path: prerequisites (p = F/A, kelvin proportionality, γ of air) are retrieved or reused; the hook (crisp bag) is answered by Boyle's law and the example with the same numbers' situation.
- Slot goals met: Boyle verified by the $1/V$ column and straight line (exp-1, ruisku, check-2/3), inverse proportionality shown graphically (pred-3 plus theory figure).
- Predictions are committed before evidence and can be refuted: exp-1 and exp-2 lock the other quantities; wrong-option feedback repairs "equal %", "celsius ratio", "linear 1 ml/°C".
- Ruiskukoe table (5040 kPa·ml on four rows, 5430 at 30 ml) is consistent; distractors test real misconceptions (vuoto vs heating); source note present.
- Exp-2 question links the earlier γ of air to the gas law (1/293), a meaningful connection, not restating.
- Worked example: seven stages, symbolic first, unit stage, check by $pV$; mistakes in the transfer task match the hints.
- Checks: concept (mikromalli), kelvin (celsius trap), graph slope calculation, explain with observable criteria; exit ticket present.
- Finnish and glossary terms (isoterminen, isobaarinen, isokoorinen) correct. Captures not opened; mechanics covered by passed tests.
