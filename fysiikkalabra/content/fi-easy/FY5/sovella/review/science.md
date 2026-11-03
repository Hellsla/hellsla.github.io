VERDICT: PASS
CONTENT-HASH: 10312941cf0bba5e

## Blocking
(none left)

## Fixed
- fy5-s4 e criterion (tasks.json): "Harjoituksessa ei myöskään soiteta koko ajan täysillä" said "never", where the Finnish says "harvoin" (seldom). It is now "soitetaan myös harvoin koko ajan täysillä".
- fy5-s3 Yleisiä virheitä (solutions.md): "kulmakerroin käännetään väärin päin" was vague. It now says what the error is: "jousivakioksi otetaan kulmakertoimen käänteisarvo".

## Polish
- fy5-s4 c: same as fi. The solution claims one significant figure but stores 5,2.

## Checked
- Compared every string of tasks.json and every section of solutions.md and figures.json with content/fi/FY5/sovella.
- Answers, units, tolerances, criteria, points (64) and links are identical (practice.py check OK). Formulas are identical (check_i18n fi-easy: 0 errors), with decimal commas.
- Every physical claim survives the sentence splitting:
  - momentin merkit
  - tyhjä/kuormattu nosturi
  - no centrifugal force (ground frame)
  - massa supistuu
  - m ≪ M ja pallosymmetria
  - jousen massa siirtää suoraa mutta ei kulmakerrointa
  - kupu/solmu
  - pistelähde, heijastukset, A-painotus
- No condition is dropped. The fi-easy addition "Normaalikiihtyvyys tarkoittaa kiihtyvyyttä, joka osoittaa kohti ympyrän keskipistettä" is correct.
- Numbers as in fi and answers.py: 21 m, 2,6 t, 412/608 kNm, 0,60°, 1,9·10²⁷ kg, 1,6·10⁸ m, 19,9 N/m, 0,45 m/s, 250 Hz, 0,686 m, 5,2 Hz, 94 dB, 1 h.
- Hash: ca5820268430c5f8 at the start, 10312941cf0bba5e at the end, after my fixes.
