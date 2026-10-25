VERDICT: PASS
CONTENT-HASH: 08a0371466573687

## Blocking
(none)

## Polish
- lesson.md:23 (also lesson.md:71, :76, sim.js readout, sim-spec.md) — "tasapainolämpötila" is used throughout but is not in glossary.json (meta lists only 5 terms); add it to the glossary (e.g. "lämpötasapainon lämpötila, tunnus T") rather than leaving an unlisted term. Not a language error, so not in the diff.

## Diff
```diff
```
(empty: the round-1 diff is applied and verified; nothing genuinely wrong remains)

## Checked
- Round-1 diff confirmed applied: lesson.md:6 "Kilogramman veden ... raudan lämmittäminen", :71 "Kilon veden ja kilon raudan", "erisuuruiset", :76 "Tasapainolämpötila ei yleensä ole alkulämpötilojen keskiarvo"; exercises.json L1-02 "jonka massa on 2,4 kg", L1-04 "veteen siirtyvä lämpömäärä Q"; exit-ticket.json:7 "Kilo vettä ja kilo rautaa saavat"; sim-spec.md "Painike ”Upota”" (sim.js button label also "Upota")
- lint_lesson.py fy3-6: 0 errors, 0 warnings (not repeated)
- Decimal comma in Finnish text, decimal point only in JSON values; minus sign U+2212 in text and solutions
- Space before units everywhere; case after number+unit correct (kg:n, kg:aan, kg:ssa, °C:sta, °C:seen, °C:een, °C:ta, K:ssa); no "80 N voimalla" pattern
- Terminology against glossary: ominaislämpökapasiteetti, lämpökapasiteetti, lämpömäärä, lämpötasapaino (state), kalorimetri, sisäenergia, kelvin; lämpö/lämpömäärä not treated as a body property; kelvin never called "aste" (only everyday "yhdellä asteella")
- solutions.md, exit-ticket.json, sim.js strings (labels, readout, flow text, note) read: grammar and punctuation fine, Finnish quotes ”Upota” correct
- Reading level suitable for 16–19-year-olds; no numbers, formulas, LaTeX or JSON values touched
- Proofreader hash unchanged during review (08a0371466573687 at start and end)
