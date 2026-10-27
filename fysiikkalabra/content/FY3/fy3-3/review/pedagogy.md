VERDICT: PASS
CONTENT-HASH: 6dfb464fbab8578b
## Blocking
(none)

## Polish
- solutions.md fy3-3-L2-03 Vastaus — "(lukemien erotuksella on erotuksen numerot)" is too terse for a student who could not do the task; say "(kahden lukeman erotuksessa on yhtä monta merkitsevää numeroa kuin erotuksessa 27 kPa)" or drop the parenthesis.
- solutions.md fy3-3-L2-02, L2-03 Vastaus — the answer line now uses k rounded (0,33; 0,39; kθ ≈ 12; 23) while Sijoitus shows 11,55 and 0,385714; add "pyöristettynä" before the rounded values so the student does not think the calculation changed.
- solutions.md fy3-3-L2-04 Vastaus — "100 K ja 400 K kelvinin tarkkuudella, kolme merkitsevää numeroa" is accurate only because the data are whole degrees; say "täysinä asteina annetut lämpötilat ovat 1 K:n tarkkuudella". exercises.json stores the answer as 4.0 while the solution says 4,00 (tolerance covers it).
- inquiry.json check-2 solution — heading "Kuvaajan lukeminen" still sits over a text that now reads a table; rename to "Pisteiden lukeminen".
- Carried from round 1, still open: Esimerkki "Kaava ratkaistuna" gives no reason for using the end points or meaning of k.

## Checked
- Diff reviewed: exit-ticket answer −273,15 °C (noin −273 °C) matches lesson.md and the glossary.
- L1-02 and L2-05 (glossary-adjacent) Vastaus lines now say the exact 273,15 does not limit and show the one-decimal alternative: reads clearly, correct (−195,75 -> −196; −270,45 -> −270).
- L2-02 and L2-03 sig-fig reasoning (Δp has two figures, sum/difference rounded to units) is followable and consistent with the arithmetic (101,55; 86,86).
- L2-04 now 4,00 with a stated reason; arithmetic 3,9955 consistent.
- L3 energy-halving Periaate now "pienimmillään (mallissa nolla)": consistent with the glossary and no longer overclaims.
- check-2 "Taulukosta luetaan" matches the table the task shows.
- Rest of the lesson unchanged since my round-1 PASS; example and phone captures not affected by the diff.
