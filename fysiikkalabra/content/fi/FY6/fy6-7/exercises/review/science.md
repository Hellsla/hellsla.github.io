VERDICT: PASS
CONTENT-HASH: 9c608f6808629688

## Blocking

## Polish
- solutions.md:260 (fy6-7-L2-09) — "tilavuusluokka 15–17,9 ft³" is a filter value that the task does not give and nobody re-checked. It is harmless, but it can be dropped, since the task only says "suodattimet Type ja Capacity".
- solutions.md (fy6-7-L2-09, Kohta d) — "Jääkaapin kompressori ei käy koko ajan" fits these models. An inverter compressor runs most of the time at reduced speed, so "yleensä" or "tavallinen kompressori" would keep the claim exact without changing the point (C, not blocking).

## Checked
- One independent script recomputed all 22 numeric answers and compared them with exercises.json: all are inside tolerance. L2-07 as a least-squares fit gives 299,1 kWh, inside 5 % of 299,3.
- L2-09 data matches the pair read on 15 Nov 2026: LG LT18S1100* 344 kWh/a and LT18S1200* 440 kWh/a, both Top Freezer, 17,5 ft³. The task says it is a standardised test result, not a home measurement.
- L2-09 a) 96 kWh, 440/344 = 1,279 → 28 %. b) P_ka = E/t: 39,27 W and 50,23 W with t = 8760 h, solved symbolically first. c) K = naE: 688 € and 880 €, difference 192 €. The rounding to 690/880/190 € is justified by 0,20 €/kWh.
- L2-09 d): the duty-cycle mechanism (thermostat, compressor power above the mean, P_ka ≈ kP_käy) is correct. The 100 W figure is marked as a general order of magnitude, not as source data. k ≈ 0,39 is consistent.
- 1 ft³ ≈ 28,3 l is correct (28,32 l), so 17,5 ft³ ≈ 495 l. The answer 39,269 W with tolerance 0,02 suits three significant figures.
- Nothing in the solution is attributed to the source beyond the table values and the field names (Type, Capacity, Annual Energy Use).
- Reflowed chains (L2-08 and the rest): same numbers, signs and units in the same order.
- The notation matches the brief (E = Pt, K = aE, kWh, snt → €). Everything is within FY6 scope (household energy).
- Hash read at start and end: unchanged.
