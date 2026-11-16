VERDICT: FAIL
CONTENT-HASH: 0a3636b79a231054
SCOPE: delta added-exercise fy1-7-L2-09, fy1-7-L2-10 (work queue 19), round 1

## Blocking
- content/fi/FY1/fy1-7/exercises/solutions.md:282 — This is an A error (causality) in model answer c). The solution says the Earth's 0,4 % difference is "samaa suuruusluokkaa kuin lähtöarvojen pyöristys". That is wrong.
  - Rounding the mass to 5,97 (true value 5,9722) accounts for only about 0,04 %.
  - The difference is almost entirely the Earth's own flattening. The equatorial radius is 6378 km and the polar radius 6357 km, so a/c = 1,0034. Correcting for the flattening gives 5493 · 1,0034 · 1,0004 ≈ 5514 kg/m³, which is NASA's value.
  - "jäykkä kivipallo" is also not why the Earth is less flattened. The reason is its slower rotation.
  - Fix: write "Maakin on hieman litistynyt, koska se pyörii, mutta paljon vähemmän kuin nopeasti pyörivä Saturnus; siksi Maan ero on vain noin 0,4 %."

## Polish
- content/fi/FY1/fy1-7/exercises/solutions.md:284 — The solution says Saturn's density is "noin puolet" of Neptune's. The ratio is 687/1638 = 0,42, so "alle puolet" would be more accurate.

## Checked
- This review covers fy1-7-L2-09 and L2-10 only (new exercises, judged in full). The hash was 0a3636b79a231054 at the start and at the end.
- I recomputed L2-09. With ρ = 6m/(πd³):
  - Earth: 5493 kg/m³, NASA 5514 (−0,38 %).
  - Saturn: 619 kg/m³, NASA 687 (−9,8 %).
  - Saturn corrected with a/c = 60 268/54 364 gives 687 kg/m³, so the flattening explanation for Saturn is exactly right.
  - answers.py gives 5493.29, which matches the key 5493. The tolerance of 0,02 also accepts NASA's own value. Three significant figures (from the mass) is right.
- I fetched the NASA Planetary Fact Sheet on 2026-11-16. All eight planets' mass, diameter and density in the solution's table match it, and so does the Rotation Period of 10,7 h (the hint's "noin 11 h"). The Notes page confirms that the diameter is equatorial and that density is mass divided by volume.
- The other L2-09 parts are correct:
  - b) and d): the two groups, Neptune the densest giant, Mercury denser than Mars, Jupiter about 4,2 times less dense than the Earth.
  - Composition is given as the cause, and no line is drawn through points that are different objects.
- I recomputed L2-10:
  - The origin fit of the example readings gives 2699,7 kg/m³, which matches the key 2700 (tolerance 0,02).
  - Each reading is m/2,70 rounded to 0,01 l, and 25,00 kg ↔ 9,26 l is consistent. The prediction is 2,70 · 9,26 = 25,0 kg.
  - The conversion 1 l = 10⁻³ m³ is right.
- I checked the PhET Density build (density_all.html):
  - Aluminium is 2700 kg/m³ and is a material choice in Intro.
  - The volume range is 1–10 l and the mass range is up to 27 kg, so the readings and the 9 l check point are possible.
  - The density meter marks Human, Glass, Titanium, Steel and Copper, with Glass at 2700. So the answer to d), that glass and aluminium coincide, is true of the sim.
- a) correctly says not to use the water level for a floating block. The extrapolation in c) is justified by the constant ratio.
