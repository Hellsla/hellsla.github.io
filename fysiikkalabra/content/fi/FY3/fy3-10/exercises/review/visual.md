VERDICT: FAIL
CONTENT-HASH: 0033aa9bfd64001a

## Blocking
- [Major] exercises.json fy3-10-L1-08 (tehtävä 12-8), text — oppilaan laskun tulos "$n = \dfrac{150 \cdot 0{,}0020}{8{,}31 \cdot 300} = 1{,}2 \cdot 10^{-4}$ mol": yksikkö "mol" on tavallista tekstiä kaavan ulkopuolella (kuvassa 12-8 "mol" tekstifontilla kaavan perässä) — uuden tekstin vakiosääntö (opettaja 2026-11-01): luku ja yksikkö kuuluvat samaan LaTeX-kaavaan, ja Major uudessa tekstissä — siirrä yksikkö kaavaan: `...= 1{,}2 \cdot 10^{-4}\,\text{mol}$`. Muissa uusissa tehtävissä ei löytynyt tekstinä kirjoitettuja suureita.

## Polish
- [Minor] for science: L3-04 (hiilidioksidipullo, $Z = pV/(nRT)$, kokoonpuristuvuustekijä) — lukua ei löytynyt oppitunnin tekstistä (reaalikaasu ei kuulu sisältöön), joten LOPS-rajaus kuuluu tieteen tarkastajalle.
- [Minor] solutions.md L3-04 Muunnokset/Vastaus — "Z" interpoloidaan ja c)-kohdan raja (noin 6 bar) on yhdessä pitkässä Vastaus-kappaleessa — jaa a), b), c) omiksi virkkeiksi tai riveiksi.
- [Minor] solutions.md L1-07 ja L3-05 Järkevyys — jakoviiva tekstissä ("264,15/294,15", "26,5/101", "0,77/0,26") — kaksoispiste kirjoitetussa jakolaskussa.
- [Minor] L2-06 solutions Kuvaajan lukeminen — suoralta valitut pisteet (280 K; 115,4 cm³) ja (360 K; 148,0 cm³) eroavat taulukon arvoista (115,0; 147,6) ilman selitystä — lisää "suoran arvot".
- [Minor] L1-07 vastauslaatikon yksikkö "l" ja tulos "2,31 l" tekstinä (\textsf{l} kuvassa lukeutuu pystyviivalta) — projektin litrakäytäntö, ei muutosta; harkitse "litraa" sanallisesti kysymyksessä.

## Checked
- open-exercises-1280-7, -8, -9 (L1-07, L1-08), L2-1280-6 to -11 (L2-05, L2-06, L2-07), L3-1280-5 to -9 (L3-04, L3-05 with data tables and solutions). No 360 px exercise captures exist; layout checks in the packet are clean.
- Tables, answer fields, MC feedback, solution cards inside their cards, no red KaTeX, no overflow. Regex scan of all new task texts and choices for plain-text quantities (only L1-08 found).

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
