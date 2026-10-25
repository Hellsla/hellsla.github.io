VERDICT: FAIL
CONTENT-HASH: c2beae7057b81e7e

## Blocking
1. lesson.md:55 — "kaasun paine johtuu kaasun painosta" is called a misconception without limits, but fy3-4:12 and the glossary entry `ilmanpaine` define air pressure as the weight of the air column per unit area. — Write "…että suljetun astian kaasun paine johtuu kaasun painosta. Pienessä astiassa kaasun paino on mitätön…"
2. exercises.json:72 (L2-04), solutions.md:67–71 — The question is what "on työntynyt ulos aukosta". 890 m³ is right only when that air is measured at 100 °C. Measured at 10 °C it is 675 m³ and is marked wrong. — Ask: "Kuinka monta kuutiometriä lämmenneestä alkuperäisestä ilmasta ei mahdu kuoreen, kun sen lämpötila on 100 °C?" and match the solution.

## Polish
1. exercises.json:64 (L2-03) — "puristettiin" does not fit 81 kPa and 66 kPa, which are below atmospheric pressure. — "mäntää liikutettiin hitaasti". Tolerance 0,05 is fine.
2. lesson.md:10, :19 — Boyle's law needs the total pressure and a constant amount of gas, and L2-04, L3-02 and L3-03 rely on both. — State both conditions.
3. lesson.md:37 — The right-hand SVG has 6 points and the left one 8, although the aria-label says both show the same measurements. — Add circles at (417.2, 170) and (504.4, 90).
4. solutions.md:23, :47 — The rocket expansion is really fast (adiabatic, about 244 kPa), and at 300 bar air is about 10 % stiffer than Boyle's law assumes (about 1,8 m³). — Note this in Järkevyys.
5. solutions.md:71 — "ympäröivä ilma nostaa" is buoyancy, which is FY4. — Keep only "pallo kevenee".

## Checked
- Lint: 0 errors, 0 warnings. Hash is the same at start and end.
- answers.py: each line uses the right law, kelvins, the bar and kPa·ml→J conversions and ylipaine + p₀. All 12 values match exercises.json.
- Recomputed by hand: L2-03, L2-04, L3-02 and L3-03.
- The °C pitfalls in the lesson, exit ticket and solutions are correct.
- In the SVG, pV is constant on the left and the slope is constant on the right.
- sim.js:50–53 uses the exact laws, with correct SI factors (:122), axes covering the full slider range and speed ∝ √T.
- Scope: no pV = nRT. The goals are covered: Boyle's law tested experimentally and a 1/V column computed.

```
pV [2030.0, 1987.5, 2010.0, 1980.0, 2025.0, 1980.0]
slope0 2.0089 J; free 2.0336 J (b -1.74 kPa); tol 1.908-2.109
balloon 100C 890.0 / 10C 675.3 / exit 772.8
rocket adiab 243.7; pump adiab 25.06; tyre gauge-only 215.9
```
