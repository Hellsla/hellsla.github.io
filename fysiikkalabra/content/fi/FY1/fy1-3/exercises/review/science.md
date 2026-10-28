VERDICT: PASS
CONTENT-HASH: de0a10e74e106226

## Blocking

## Polish
- exercises/solutions.md:68 (L2-02) — "kolmen lukeman keskiarvo kantaa yhden numeron lisää" is not a sound rule. Justify 10,7 mm by the millimetre readings, or give 11 mm (both are inside the tolerance).
- exercises/solutions.md:49 (L1-05) — "Virhe-arvio ei voi olla asteikkoväliä suurempi" is too absolute (a scale that is hard to read can need more). Write "on tavallisesti enintään puoli asteikkoväliä".
- exercises/solutions.md:99 (L3-01) — "Viiveet kumoavat toisensa lähes kokonaan" overstates it: two thirds cancel. Write "suurimmaksi osaksi".
- exercises/solutions.md:18 (L1-02) — the task asks for the sign, but Vastaus gives $0{,}3\,\text{cm}$. Write $+0{,}3\,\text{cm}$.

## Checked
- Round-1 blocker fixed: L2-01 tolerance 0.04 accepts 5 % (3,5 % off 4,83), and the solution states 5 % with the one-figure rule and 4,8 % as the calculator value.
- All 12 answers recomputed independently in one script and compared with answers.py: identical (0,51; 0,3; 0,35; 47,5; 0,5; 4,83; 10,67; 12,4; 10; −0,06; 2,0; 0,26).
- Tolerances: a student rounding to the data's figures stays inside in every task (L1-03 asks for the half-range itself, not the rounded estimate, as its solution says).
- Signs: L1-02 +0,3 cm. L3-01: a late start shortens the reading and a late stop lengthens it, so −0,06 s, and the 3,44 s → 3,50 s check is right. L3-03 +0,26 cm.
- Magnitudes: paper 100 µm, so 2 % and a 250-fold gain; tape about 1 %; the 45,2 "nonsense mean" in L2-03 is right.
- All seven parts in every solution, symbolic before numbers; conversions in L2-02 (m→mm), L2-03 (m, mm→cm) and L3-02 (mm→µm) are right.
- Notation as in the brief: no × or ÷, \cdot in products, divisions as \frac, Δx, Δt_sys, ΔL_sys, Δh.
- Scope: mean, half-range, reading error, relative error and zero correction are all in FY1 "luotettavuuden arviointi".
