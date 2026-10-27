VERDICT: FAIL
CONTENT-HASH: 23ee674947cc5bdb

## Blocking
- solutions.md:18 (L1-02, Vastaus) — the line says that all three data, 24,0 l, 160,0 kPa and 280,0 kPa, are given to three figures. 160,0 kPa and 280,0 kPa have four significant figures, so the line teaches a wrong count and does not name the datum that really limits the answer. The answer 13,7 l itself is right. — Fix: "kolme merkitsevää numeroa; rajoittava tieto on tilavuus 24,0 l (kolme numeroa), paineet 160,0 kPa ja 280,0 kPa ovat neljän numeron arvoja." Make the same correction at solutions.md:58 (L2-01): 300,0 bar is a four-figure value, not three. Its limiting datum, 6,8 l, is already named correctly.

## Polish
- solutions.md:79 (L2-03) — every pressure is read to 1 kPa, so 66 kPa ±0,5 kPa is about 0,8 %. That would support 2,01 J. Two figures follows the stated rule and is defensible; consider saying in one clause that the counting rule is what is applied.
- lesson.md:118 — "noin 78 kPa" is a reasonable cabin pressure (about 2200 m equivalent). Optionally add "(enintään noin 2400 m:n korkeutta vastaava)" so students see where the number comes from.

## Checked
- One script recomputed all 12 exercise answers independently. They match answers.py and exercises.json; the largest difference is under 0,1 %. L2-03 uses a least-squares fit through the origin: 2009 kPa·ml, and the pV products are 1980–2030.
- Every solution states the right principle and why it applies: Boyle for the syringe, tank, rocket, bottle and pump; isobaric for the balloons; isochoric for the freezer, bottle and tyre. Gauge pressure is converted to absolute in L3-02 and L3-03, and ρgh is added in L3-01. Each unknown is solved in symbols first.
- The rounding in differences is correct: L2-04 ΔT = 90 K gives 2 figures, L3-02 303 − 101 gives 202 at unit precision, and L3-03 40,0 − 10,1 gives 29,9.
- Reasonableness checks are genuine. They use ratio estimates and the wrong result from Celsius degrees (negative volume, 25 °C). L2-01's real-gas remark is right: Z ≈ 1,1 at 300 bar gives about 1,8 m³.
- Worked example: 1,036 l rounds to 1,0 l. The figures are justified by 0,80 l and 78 kPa, the +30 % is right and the pV check is 80,8 kPa·l.
- Misconception (1,04 l, 3,5 %), exit ticket (160 kPa, 308/280 = 1,1) and 1 kPa·l = 1 J are correct.
- Figures are to scale. The boyle-graphs points lie on pV = 2000 kPa·ml, and the (1/V, p) line has slope 2000. In absolute-zero, V and p at 253 K and 373 K are in the ratio 1,474, and the extension passes through 0 K.
- inquiry.json: pred-1 gives 200 kPa and 5,00 J, pred-2 60,2 ml and 0,171 ml/K, and the γ = 1/293 item is right. In ruisku, pV = 5040 and the 30 ml row is 5430 (+7,7 %, heating). Etsi virhe gives 252 kPa, siirto 1,07 l with mistakes 2,10 and 0,00107, check-2 120 kPa with mistakes 108 and 0,12. The model answer gives 1/V values. All are correct.
- sim.js uses V₀ = 50 ml, p₀ = 100 kPa and T₀ = 293,15 K for all three processes. simState gives p and constant in SI, and the adapter gives Vgas and VperT. exp-1 locks mode and Tc and exp-2 locks mode, so each varies only its parameter. The calc box says that the values come from the law, not from measurement.
- Scope: everything is within FY3, including hydrostatic pressure from the prerequisite lesson and F = pA.
