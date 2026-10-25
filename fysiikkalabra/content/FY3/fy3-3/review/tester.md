VERDICT: PASS
CONTENT-HASH: 536cade809f2b051

Hash checked at start and end of review: 536cade809f2b051 (unchanged).

## 1. test_sims.py (3 runs)
```
PASS preview/fy3-3  [] []
PASS preview/fy3-3  [] []
PASS preview/fy3-3  [] []
```
tests/sims/fy3-3.json has 16 assertions covering theta, speed scaling, theory pressure, measured pressure trends, readout, canvas size, slider units, N. Coverage of sim-spec is adequate; no missing assertions.

## 2. Own Playwright checks (preview/fy3-3.html)
- Console/page errors: none at 1280, 390, 360, 320 px. Horizontal overflow 0 px at all widths.
- Canvas attributes 600x400 at all widths (CSS-scaled to 574/324/294/254 px).
- Slider labels: "Lämpötila T = 300 K", "Tilavuus V = 1,0 dm³" (units present).
- Readout (DOM text): "T = 300 K = 27 °C / Hiukkasten keskinopeus: 1,00 × 300 K:n keskinopeus / Paine p ≈ ... (suhteellinen, 100 = 300 K ja 1,0 dm³), teoria 100".
- theta - (T-273.15) = 0.0 at all tested T (100..600).
- Speed = V_REF*sqrt(T/300): 100K 69.282, 200K 97.9796, 450K 146.9694, 600K 169.7056 (all equal expected to 4 dp).
- Deterministic start: seed fixed (p.randomSeed(7)); default state T=300, V=1, vRel=1, N=80, speedCheck=120 on every load.
- Particles stay in box after V reduced 2.0 -> 0.5 dm³: green particle pixels right of the piston = 0 of 2112 (canvas pixel count, 300 ms after change). Code clamps positions every frame.
- Thermometer labels "600 K"/"100 K" placed left of tube; screenshots at 1280 and 320 px show them fully visible, not clipped; "300 K" under the bulb visible.

## 3. Measured pressure vs pTheory
Fresh page, set (T,V), 3 s then 8 s (deviation of pRel from pTheory):
```
100 0.5  3s -21.2%  8s -13.6%
100 2    3s -34.4%  8s -18.8%
100 1    3s -30.2%  8s -15.9%
200 1    3s  +6.7%  8s  +6.9%
300 1.5  3s  -4.9%  8s -17.6%
450 1.5  3s  -8.0%  8s +10.7%
600 2    3s  +1.5%  8s  -3.9%
150 0.7  3s  +0.1%  8s  +1.4%
```
Continuous sliding (several combos, 3 s each): +9 to +16 % typical, -1.4 % and +22.7 % extremes; transients after V increase at low T (particles need seconds to reach a far piston) gave -47.6 % once.

Statistics at 100 K (40 samples at 0.5 s spacing after 2 s settle):
```
100 K, 1,0 dm3: mean ratio 0.996, sd 0.158, min 0.70, max 1.28, 75 % of samples within 20 %
100 K, 2,0 dm3: mean ratio 1.009, sd 0.192, min 0.69, max 1.46, 67.5 % within 20 %
```
Measurement is unbiased (mean ratio ~1.00). At high T it is within ~10-15 %; at low T (100 K, few collisions in the 1,5 s window) shot noise is ~16-19 %, so single readings can exceed 20 % off. This is statistical fluctuation (the on-page note says the value "vaihtelee hieman"), not a defect. Not a FAIL; optional improvement: a longer window or a note that low T fluctuates more.

## 4. Other
No sim.js, lesson file or test file was edited. build.py not run.
