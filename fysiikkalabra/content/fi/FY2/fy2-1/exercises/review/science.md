VERDICT: PASS
CONTENT-HASH: 575f3df5f4e893ad

## Blocking

## Polish
- solutions.md L1-10 Järkevyys — "kuiva puu 16,2 MJ/kg" is the MAFY value (docs/mafy-arvot.tsv, VERIFIED) and fixes my earlier point; the chapter *Polttoaineet ja lämpöarvo* uses air-dry firewood 15 MJ/kg, so "kuivaan" (not "ilmakuivaan") is the right word here (C, no change needed).
- Earlier items outside this delta (L1-09 "likimain eristetyn", L3-04 c), L1-07 option 3, L1-10 table name in hint vs solution) are still open.

## Checked
- Delta review: hash 575f3df5f4e893ad at the start and the end; I judged only the one changed line in solutions.md L1-10 Järkevyys.
- The comparison value 16,2 MJ/kg for dry wood matches MAFY *Polttoaineiden LHV-lämpöarvoja*; petrol 43,4 MJ/kg is still about 2,7 times it, so "energiatiheys on suuri" holds.
- Recomputed: E = 43,4 MJ/kg · 2,0 kg = 86,8 MJ ≈ 24 kWh, same as answers.py and exercises.json (86,8 MJ, 0,04). No answer, unit or tolerance changed.
