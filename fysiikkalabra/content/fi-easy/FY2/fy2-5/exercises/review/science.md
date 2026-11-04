VERDICT: PASS
CONTENT-HASH: 2df2aed1e54f8f5e
Round: 2

## Blocking
(none)

## Polish
(none)

## Checked
- Round 1 -> 2 change (only solutions.md, L3-05 "Vastaus:" line, now "vastauslaatikkoon kohdan b) tulos $940\,\text{kg}$."): 940 kg is part b)'s result and the box value 940; short selkosuomi sentence, matches the Finnish. Mode: full.
- Translation review against the reviewed Finnish (2026-11-04), 16 tasks. New tasks L1-06..08, L2-05..07, L3-04..05: ids, answers (15 kg, 40 kWh, 5.6 kg, 18 kW, 3300 kg, 940 kg), units, tolerances (0.02, 0.03, 0.01), kind, correct flags, choices and feedback, data cells equal the Finnish (scripted comparison of all non-text JSON values: identical).
- All numbers in solutions.md equal the Finnish (scripted; only the position of one 0.65 in the L2-07 sentence differs, word order).
- Recomputed: 255/17=15; 144/3.6=40; 200/14.7-200/10.4=5.62; 0.065 kg/min -> 18.4 kW; 13300 kWh -> 3313 kg pellets, 940 kg difference; no formula changes.
- Distractor logic and feedback correct in L1-06 and L2-06 (21.7 kWh, 26:3.0=8.7, 129 MJ).
- Language: selkosuomi: short sentences, terms explained (tehollinen lämpöarvo, hyötyenergia), decimal comma in text and decimal point in data cells as in fi. check_i18n.py fi-easy: 0 errors. No edits needed.
