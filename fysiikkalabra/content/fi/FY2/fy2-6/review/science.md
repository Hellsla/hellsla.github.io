VERDICT: PASS
CONTENT-HASH: aee5688129bd889b

## Blocking

## Polish
- inquiry.json:330 — tarkistus-3 model answer "Kumpaakaan ei voi säätää nopeasti … tuulta ei voi lisätä": wind output can be cut quickly (curtailment), only not raised — say "Kumpaakaan ei voi nostaa nopeasti tarpeen mukaan" so the model answer does not contradict how wind is actually used in balancing.
- lesson.md:83 — "Ydinvoimala käy mieluiten tasaisesti, koska sen tehon muuttaminen on hidasta": the main reason is economic (small fuel cost, large capital cost; OL3 does follow load to some extent). Consider "koska sen polttoainekustannus on pieni ja tehon muuttaminen on hidasta" (C at this level, so optional).
- inquiry.json:101 — "vuoden tuntimäärä 8760 h on tarkka luku": 2024 was a leap year (8784 h). The prompt fixes 8760 h, so the answer stands; say "annettu" rather than "tarkka".
- lesson.md:72 — "turve ovat fossiilisia" while the statistics row and figure label it "fossiiliset polttoaineet ja turve" separately; Statistics Finland classes peat as its own (hitaasti uusiutuva) fuel. Defensible via IPCC treatment; a half-clause would make the two consistent.
- inquiry.json:228 — "energia kerrottiin ajalla tehon sijaan" is unclear; "energia kerrottiin ajalla, vaikka se olisi pitänyt jakaa".

## Checked
- Worked example recomputed: 14·10⁶ kWh : 8760 h = 1598 kW ≈ 1,6 MW, 0,32 of 5000 kW; check 43,8 GWh, 14 : 43,8 = 0,32; symbolic first, staged, two figures justified.
- All inquiry numerics recomputed: wind 2,306 GW → 2,31; 320 turbines; Thursday 8,4 GW (mistakes 8,8 / 12,7 / 0,6 correct); OL3 14,0 TWh (mistakes 14 016 GWh, 0,00018); check-2 8,76 → 8,8 GWh (mistake 8760 MWh); exit ticket 17,52·10⁶ kWh ≈ 18 GWh.
- "Kymmeniä kertoja maailman keskiteho": 122 640 : ≈3400 GW ≈ 36 — true.
- Statistics table sums to 79,9 TWh; text's "noin neljännes" (25 %), "kaksi viidesosaa" (39 %), "muutama prosentti" (4 %) agree.
- Bar chart to scale (10,5 px/TWh, every bar within 0,5 px); log chart points at the right decades, 2,5 decades = 320×.
- 1 GWh = 10⁶ kWh, 1 TWh = 10⁹ kWh; E = Pt stated for constant power, keskiteho defined via E/t.
- Week data realistic (nuclear 4,3 GW ≈ Finnish fleet, wind ≤ 0,8 of ~8 GW) and marked as invented.
- Every choice item has exactly one correct option; distractor feedback says why each is wrong.
- Grouping (sääriippuvainen / säädettävä / perusvoima) consistent across theory, summary, checks and exit ticket; misconception "noin kolmannes" matches 32 %.
- Within FY2 scope: no chain efficiencies, no FY3 formulas; hash identical at start and end.
