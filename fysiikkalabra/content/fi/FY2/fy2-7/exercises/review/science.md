VERDICT: PASS
CONTENT-HASH: 0cc60ee64a913711

## Blocking

## Polish
- solutions.md fy2-7-L2-09 Vastaus — with 9 % and 4 % rounded to whole percents, the difference 5 % is uncertain by about ±1 percentage point, so even two significant figures (13 MWh) are generous; the tolerance 0,05 now accepts both 12,5 and 13 (C).
- solutions.md fy2-7-L2-10 c) — "summassa tuotannon, tuonnin ja viennin on pysyttävä tasapainossa kulutuksen kanssa": add "ja sähkövarastojen" for completeness (C).

## Checked
- Delta review: hash 0cc60ee64a913711 at the start and the end; I judged the added L2-10, the L2-09 rounding and tolerance, and the four captions without "(esimerkkiaineisto)".
- Every L2-10 value checked against docs/audits/2026-11-16-fy2-aineistot.md (16.11.2026 klo 10.48): consumption 11 603, production 11 341, net −210, nuclear 2594, wind 5571, hydro 1823, CHP 853 + 329, solar 56, other 73, storage 71 MW; 1.00: wind 7639, production 12 791, consumption 10 647, net +2142; 10.00 wind 5885. All agree.
- Recomputed: E = 11 603 MW · 1 h = 11,603 GWh → 11,6 (answers.py 11,603, tolerance 0,02); gap 262 MW, unexplained 52 MW = 0,45 % of consumption, 262/11 341 = 2,3 %; wind 49,1 %, nuclear 22,9 %; 11 603 : 1600 = 7,25.
- The source items sum to 11 370 MW against 11 341, and the task says the parts do not match exactly; true.
- E = PΔt with a stated constant-power assumption and the hour exact; three significant figures justified by the 0,45 % mismatch.
- c), d): interconnection, import/export, and a moment not giving the yearly structure are correct.
- The four captions lost "(esimerkkiaineisto)", but each task text still says "Taulukossa on esimerkkiaineisto", so no invented data reads as measured.
- L2-09: 12,5 MWh recomputed, 13 MWh is 4 % away, inside 0,05.
