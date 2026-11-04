VERDICT: FAIL
CONTENT-HASH: 29e577cbf20e55f6
Round: 2

Round 1 had no Blocking items. All four Polish items are addressed:
- The answers are rounded (2800 h, 23 pp, 17 €/MWh), and Vastaus gives the calculated value.
- The life-cycle wording is in L2-07 and L3-05 c).
- The solution writes (ΣP)·24 h.
- Wind is 12 g/kWh in both tasks.

The changed numbers are correct. The new L1-07 option order revealed one defect that round 1 missed.

## Blocking
- content/fi/FY2/fy2-6/exercises/solutions.md:60 (L1-07 Mallivastaus) — **A**, internal consistency. The text says "Oikea vastaus on ensimmäinen … Toinen vaihtoehto kuvaa perusvoimaa … Kolmas kuvaa sääriippuvaista", but the options are shown shuffled (inquiry.choice_order). preview/fy2-6.html shows the correct option first, sääriippuvainen second and perusvoima third, so "toinen" and "kolmas" are swapped. Fix: name the options by content, for example "Oikea vastaus: voimalaitos, jonka tehoa voi muuttaa nopeasti, kuten vesivoimala. Tasaisesti tuottava ydinvoimala on perusvoimaa, ja tuulivoimalan teho vaihtelee sään mukaan, eikä sitä voi säätää tarpeen mukaan."

## Polish
- exercises.json L2-07 and the L3-05 table — the IPCC life-cycle factors are CO₂ equivalents. Say "hiilidioksidiekvivalentti" or add a footnote (carried over, minor).
- solutions.md L3-05 Vastaus — "päästöjen perusteella kumpikin kelpaa" holds because the factors are now equal. Say so directly.

## Checked
- Recomputed in one script: L1-08 2750 → 2800 h (1,8 %, inside 0,02); L2-05 22,79 → 23 pp; L2-06 32 / 28,5 / 33,3 %; L2-07 1,616·10⁶ t; L3-04 others 1,2/3,2/6,1/6,7/4,7/1,0/−0,5 GW, wind 489,6 GWh, 32 %; L3-05 16,60 → 17 €/MWh (2,4 %, inside 0,03), nuclear 10,57, c) 3469 t and 113 530 t. answers.py prints the same values.
- L3-05 Järkevyys: 113 530 : 3469 = 32,7 ≈ 33, the production ratio, as it should be with equal factors.
- L3-04 c): 6,7 − 1,0 = 5,7 GW and 6,7 − (−0,5) = 7,2 GW. Järkevyys: 1615 GWh and 538 GWh.
- L1-06 ("uusiutuva"): only Tuuli is correct, and the feedback on uraani, kivihiili and maakaasu is right.
- L1-07: exactly one correct option, and every option's feedback is right.
- L2-07 Vastaus "12 g/kWh pienin (yhtä pieni kuin tuulivoimalla)" agrees with the table.
- FY2 scope: only E = Pt, shares and factor × energy.
