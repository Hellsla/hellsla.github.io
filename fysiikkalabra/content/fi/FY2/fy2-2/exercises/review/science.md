VERDICT: PASS
CONTENT-HASH: 7a1f623a266eb77d

## Blocking

## Polish
- content/fi/FY2/fy2-2/exercises/solutions.md:99 — 140 TJ : 790 TJ ≈ 18 % is nearer a fifth than "noin kuudesosan" (the six comes from rounding up); say "vajaan viidesosan" or "noin 18 %".
- content/fi/FY2/fy2-2/exercises/exercises.json (L3-01) — the comparison uses daily averages; "keskimäärin" for the production too (or "vuorokauden keskiarvona") would make clear that peak demand and outages are ignored (C).

## Checked
- All 12 answers recomputed independently in one script; all agree with answers.py and exercises.json (2,27 → 2,3; 33,3 → 33; 1,28 → 1,3 GJ; 954,5 → 950; ceil(5,64) = 6; 3194 → 3200; 1,16·10⁷ l).
- Units and tolerances fit the data's significant figures; L1-04 and the wind-farm-type subtractions justify rounding by the least precise datum.
- Data realistic: chocolate 22 MJ/kg, petrol 32 MJ/l, TNT 4,184 GJ/t, Finland 790 TJ/day (2023), OL3 1600 MW → 140 TJ/day and ≈4300 MW thermal → 370 TJ/day, 4,5 kg U-235 at 8,2·10¹³ J/kg.
- L2-03 states the assumption (light absorbed in the room) that makes the 6,0 kJ answer right.
- L3-02: the combined-heat-and-power remark is qualitative and correct (higher condensing temperature, slightly less electricity), within FY2 scope.
- Every solution has the seven parts, solves symbolically before substituting, and its reasonableness check is a real estimate.
- Notation (E_alussa, prefixes substituted by their values) matches the lesson.
