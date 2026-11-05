VERDICT: PASS
CONTENT-HASH: 8f45e577d831e5c3
Round: 2

## Blocking

## Polish
- exercises.json:296 fy8-11-L3-04 b): "Kuinka monta vuotta kuluu" no longer names its start, and t = 0 is now about 10 a after discharge. A student who counts from discharge gets about 260 a, which is 4 % off and outside the 2 % tolerance. Fix: "Millä ajanhetkellä t aktiivisuus on laskenut arvoon 100 TBq/t …", or "Kuinka monta vuotta ajanhetkestä t = 0 kuluu …".
- solutions.md:184 fy8-11-L3-05 Vastaus a): "1000 MW (samat kaksi merkitsevää numeroa)". Written as 1000, it shows neither its two figures nor the 1536 − 507 = 1029 MW behind it. Write 1,0·10³ MW, or "1030 MW ≈ 1,0·10³ MW".
- exercises.json:296 fy8-11-L3-04: "määräävät pääasiassa cesium-137 ja strontium-90" (with their daughters Ba-137m and Y-90). Pu-241 (14 a) also contributes at 10 a. Since this is example data the wording is acceptable; optionally add "ja niiden tytärnuklidit".

## Checked
- Hash 8f45e577d831e5c3 at the start and at the end.
- Round 1 Blocking (L3-04 c), "koko aktiivisuus 240 000 a"): resolved. The text now says "Plutonium-239:n oma aktiivisuus … (tehtävä L3-03)", and 24 100 a · log₂1000 = 240 200 a.
- Round 1 Blocking (L3-04 model B): resolved. t now starts about 10 a after discharge, the interim-storage condition is gone, and b) asks for the fission-product activity 100 TBq/t.
- Round 1 Blocking (L3-05 significant figures): resolved. The answer is 540 kg with two figures from η = 0,33 and 92 %, and a) gives 1500 MW. answers.py gives 543,0, inside the 2 % tolerance.
- L3-04 new data (×10): my own least-squares fit gives λ = 0,02285 1/a, T½ = 30,3 a and A₀ = 30 060 TBq/t. The two-point estimate gives 30,6 a. b) is 249,7 a, and the check 30 000 : 2⁸ ≈ 117 is right.
- The magnitude of 30 000 TBq/t at 10 a is now realistic (about 10⁴ TBq/t).
- L1-08: Q = 200·10⁶ · 1 eV = 3,204·10⁻¹¹ J, and the e/eV mix-up is fixed. The L2-06 source is made specific. L3-04 now uses the guardrail sentence on measurement uncertainty.
- L1-06, L1-07 reordered: exactly one correct option each, and `answer` matches.
- Recomputed: L2-06 4394 MW, 34,64 TWh; L3-05 1536 / 1029 MW, 543 kg, 1,86·10⁶ t coal, ratio 3,4·10⁶. All match.
