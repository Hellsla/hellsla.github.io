VERDICT: PASS
CONTENT-HASH: 848b37994704cca1

## Blocking

## Polish
- solutions.md fy2-8-L3-06 d) — "oppitunnin taulukossa tuulivoiman elinkaaren päästökerroin on 12 g/kWh": the lesson's table gives 11–12 g/kWh; write "11–12".
- solutions.md fy2-8-L2-10 a) — the task asks for "kaksi tuotantomuotoa" per country; for Poland gas 14,3 % and wind 14,2 % are named both, which is honest but the task could say "suurimmat osuudet" without "kaksi" (C).
- Earlier items (L1-09 CH₄ mass ratio check, L2-09 significant-figure reason) are still open.

## Checked
- Delta review: hash 848b37994704cca1 at the start and the end; I judged the added L2-10, L2-11, L3-06 and three captions without "(esimerkkiaineisto)".
- Every value checked against docs/audits/2026-11-16-fy2-aineistot.md: OWID e (FI 246,82/57,47, SE 35,26, PL 954,6/588,6, DK 627,89/114,41), all 2025 shares of FI, SE, PL and the 2000 shares used, Fingrid 10.48 readings and the 1.00/8.00/10.00 table. All agree.
- L2-10 recomputed: 588,6 · 5,0 = 2943 g → 2,9 kg (answers.py 2,943, 0,02); FI 287 g, SE 176 g; 588,6 : 35,26 = 16,7; import 210 : 11 603 = 1,8 %; zero-emission import would lower 16 g/kWh by 0,29; 57,47 : 16 = 3,6.
- L2-10 d): Fingrid estimate vs OWID lifecycle explained by moment vs annual mean and by lifecycle scope; the source note that Fingrid does not call it lifecycle is respected.
- L2-11 recomputed: shares 59,7/53,4/50,7 %; 98, 137, 150 g (answers.py 150); Δe per 1000 MW 4,2 and 1,6 (ratio 2,70); 52 g = 35 %; coal 8200 g ≈ 55 times.
- L2-11: correlation stated, causation not claimed; the other sources' changes are honestly given as a possible reason.
- L3-06 recomputed: Δe −189,35/−366,0/−513,48; −76,7 % → −77 % (answers.py −76,72), −38 %, −82 %; 588,6 : 57,47 = 10,2.
- m = eE and the relative change solved in symbols first; units g/kWh · kWh = g right.
- Captions: the task texts still say "esimerkkiaineisto, ei tilasto" / "esimerkkimaan", so nothing invented reads as measured.
