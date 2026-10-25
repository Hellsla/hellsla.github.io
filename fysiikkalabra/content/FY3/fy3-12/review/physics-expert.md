VERDICT: FAIL
CONTENT-HASH: d23d088adff6a242

## Blocking
1. exercises.json:72, solutions.md:70–71 — L2-04 blames Arctic sea-ice melt for a 1-point albedo drop (+3,4 W/m²) and concludes it is over three times today's imbalance. That is unrealistic: sea-ice loss since 1979 adds about 0,2 W/m² globally, and an ice-free Arctic would add under 1 W/m². The arithmetic is right. — Keep the numbers and the answer 3,4, but make the cause hypothetical: "Oletetaan, että maapallon heijastama osuus pienenisi 30 %:sta 29 %:iin (esimerkiksi lumi- ja jääpeitteen ja pilvisyyden muuttuessa)". In the solution add: "Arktisen merijään väheneminen on tähän mennessä lisännyt imeytymistä vain noin 0,2 W/m²."

## Polish
1. lesson.md:31 — "Ilman ilmakehää … −18 °C" clashes with the 30 % reflected by clouds. — Write "Jos ilmakehä ei imisi lämpösäteilyä".
2. lesson.md:3 — "säteilee … yhtä paljon kuin saa Auringosta": Earth emits 240 W/m², not 340. — Write "kuin imee".
3. lesson.md:41 (figure 2) — The reflected arrow starts 75 px from the incoming ray. — Start it where the ray meets the atmosphere (about x 118, y 110).
4. lesson.md:15–17 (figure 1) — The convection loop is open at the bottom. — Close it, or put the heater under the rising side only.
5. lesson.md:105, 111 — The example rounds intermediates (730 W, 1,45 kW). — Carry 734,4 W and 1454 W (NOTES §2). The result, 35 kWh, is unchanged.

## Checked
- The climate numbers are realistic: −18/+15 °C, 30 %, 340 W/m², 280 → >420 ppm, about 1 W/m², and most of the heat goes into the oceans.
- Figures 1–2: every flow points the right way (hot → cold, incoming down, reflected up, thermal radiation up, back-radiation down).
- Figure 3: the hot side is on the left and P points outward. About 90 % of the drop is in the insulation (142/158 px), where the slope is steepest.
- Worked example: symbolic rows come first, every value has its unit, and it has 5 stages.
- answers.py: every line uses the right formula, conversion and sign.
- L3-01: "keskimäärin 1,4 W" makes E = Pt valid. That rate is realistic (90 → 70 °C), and the vacuum and mirror reasoning is correct.
- L3-02: 2,6·10²⁰ kg = 3,6·10¹⁴ m² · 700 m · 1025 kg/m³, and 4,0·10³ J/(kg·K) and 90 % are right. Really about ⅓ of the heat goes below 700 m, but the task states the assumption.
- L3-03: the heat-pump reasoning is correct.
- Exit ticket: 300 W is correct.

Python (hand checks):
```
esim 734.4 720.0 1454.4 34.906
L2-04 3.400  L1-05 238.0
L3-01 20.048
L3-02 Ev 1.608e+22 dT10 0.1392 mass700 2.583e+20
wall share 0.899
```
