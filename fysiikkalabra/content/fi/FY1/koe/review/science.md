VERDICT: FAIL
CONTENT-HASH: 1268505f7ede9abf

## Blocking
1. **A, fy1-k3 c (rubric criterion 3, 2 p, and the last sentence of the model answer): wrong mechanism.** The criterion awards "nopeuksien erotus 2,8 m/s, jonka suhteellinen epävarmuus on *paljon suurempi* kuin Elinan nopeuden", but 0,2/2,8 ≈ 7 % against 0,2/3,2 ≈ 6 %: hardly larger. Since s = v_A v_E t_0/(v_A − v_E), a larger v_E both lengthens Elina's lead (≈ 6 %) and shrinks the closing speed (≈ 7 %); the two add to ≈ 13 % (±0,3 km of 2,1 km). The solution's middle sentences say this correctly, but "Kun lähes samoista nopeuksista lasketaan erotus" is false here (3,2 and 6,0 m/s are not nearly equal). Fix: reword the criterion to "suurempi v_E kasvattaa etumatkaa ja pienentää erotusnopeutta, vaikutukset summautuvat (≈ 6 % + 7 %)", and drop or correct the last sentence.

## Polish
- fy1-k4 a criterion 1: "tunnistaa *todennäköiseksi* karkeaksi virheeksi"; deviation alone is not the reason (guardrail, outliers). The cause (≈ 12 swings) is in criterion 2, good.
- fy1-k4 b: say that half the range is a simple scatter estimate chosen for this task, not the uncertainty of the mean (guardrail).
- fy1-k5 b: "alumiini on varmasti poissuljettu" → "selvästi poissuljettu".
- fy1-k5 c Periaate: "massan epävarmuus, noin 1 %" is not given in the task; say "jos massa tunnetaan grammaan, noin 1 %".
- fy1-k6 c criterion 2 compares air resistance with "paino" (a force, FY2/FY4); also accept "kevyt suureen pintaan nähden".
- fy1-k3 b Vastaus: "kaksi merkitsevää numeroa" but writes 10,7 min.

## Checked
Hash at start and end 1268505f7ede9abf. Own script recomputed every number: k1 d, f, g, h, j. k2 fit −0,1174 cm/min, 15,02 cm; read slope −0,118; t = 110 min. k3 642,9 s, 2057 m; extremes 1800 m and 2354 m. k4 mean 14,22 s, half range 0,3 s, T = 1,42 ± 0,03 s, 16,8 s ≈ 11,8 swings. k5 7,68; 7,11–8,35 g/cm³. k6 fit 9,70 m/s², read 9,675, −1,4 %; filter data = 1,5·tanh(gt/1,5); 11,6 m/s = 42 km/h (9,81: 42). k7 origin fit 0,1020 mm, 2 µm, 784 kg/m³. Every choice item: exactly one correct option, every distractor wrong. Scope: s = vt, s = s₀ + vt, v = gt and ρ = m/V only; no s = ½gt², forces or energy. Rubric sums: 20 + 4 × 15 + 2 × 20, maximum 70; each criterion matches its solution except Blocking 1.
