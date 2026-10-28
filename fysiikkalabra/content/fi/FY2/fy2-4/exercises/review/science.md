VERDICT: PASS
CONTENT-HASH: e13ddfe39bad5ca6

## Blocking

## Polish
- content/fi/FY2/fy2-4/exercises/solutions.md:101 — L3-02 "Vastaus: 2083 s eli noin 2,1·10³ s, kaksi merkitsevää numeroa": lead with the rounded value (2,1·10³ s, about 35 min) so the four-figure number is not read as the answer's precision.

## Checked
- All 12 answers recomputed independently in one script and compared with answers.py and exercises.json: 85 %, 30 %, 3,0 W, 2000 J, 4,0 kJ, 96 kJ, 54 W, 0,228 → 0,23 kWh, 45 kW, 1,5, 2083 s, 180 J; all agree, and each rounded answer lies inside its 2 % tolerance.
- Every task uses one device's efficiency η = E_a/E_o = P_a/P_o with E_o = E_a + E_h, inside FY2 scope (no chain products, no heat-engine cycle).
- Steady power is stated or implied wherever P_a/P_o or E = P t is used (L1-02, L2-01, L2-03, L3-02).
- L2-02 reasoning (equal light power → equal P_a) is right, and its check (10 W LED ≈ 60 W filament lamp) is realistic.
- L3-01 handles mixed J and kJ correctly (each device's ratio in its own unit); L3-03 reads η from arrow thicknesses as the lesson teaches.
- Data realistic (motor 85–90 %, LED 30 %, filament 5 %, petrol 25 %, panel 20 %); solutions complete in seven parts, symbolic first, conversions explicit, rounding justified, checks real.
- Notation (E_a, E_o, E_h, P_a, P_o, P_h, η) the same as in the lesson.
