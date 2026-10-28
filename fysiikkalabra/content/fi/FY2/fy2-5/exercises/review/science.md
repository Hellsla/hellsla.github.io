VERDICT: FAIL
CONTENT-HASH: fdfbc1a91389a62a

## Blocking
- solutions.md:99 (fy2-5-L3-01, Järkevyys) — Problem: the check claims the difference "$8{,}0\,\text{kg} - 2{,}79\,\text{kg}$ on yli kaksi kertaa öljyn massa". That is false: 5,21 : 2,79 ≈ 1,87. A reasonableness check that states a wrong fact misleads. — Fix: say the difference is just under twice the oil mass. Or check with the ratio: the wood mass is 43 : 15 ≈ 2,9 times the oil mass, so the difference is about 1,9 times it: $1{,}87 \cdot 2{,}79\,\text{kg} \approx 5{,}2\,\text{kg}$.

## Polish
- solutions.md:29 (L1-03) — Problem: "polttoainetta kuluu kymmeniä tonneja", but the task burns 12 t per hour. — Fix: "noin kymmenen tonnia".
- exercises.json:82 (L3-01) — Problem: "Mökin lämmitykseen tarvitaan energiaa 120 MJ" could be read as useful heat. The lesson stresses that released energy is not useful energy. — Fix: "polttoaineesta pitää vapautua energiaa $120\,\text{MJ}$".
- L1-03, L1-04, L2-01 — Problem: the significant figures of 12 000 kg, 400 kg and 40 g are ambiguous. The solutions do justify their 2 s.f. by the other datum. — Fix (optional): 12,0 t and so on, or leave as is.

## Checked
- All 12 answers were recomputed independently in one script. They match answers.py and exercises.json, and every one is within tolerance (largest gap 0,78 %, L2-04). Rounding to the data's figures stays inside tolerance.
- answers.py uses the right physics on every line: E = Hm, m = E : H, E_hyöty = η E_sisään, E_sisään = E_hyöty : η, and P = E_hyöty : t with MJ/s = MW.
- Every solution has the seven parts. Each is symbolic first, and its conversions are by substitution (GJ → MJ, t → kg, kJ → MJ). The round-1 L3-03 and L1-05 issues are fixed.
- The H values match the lesson table, whose IPCC 2006 and Tilastokeskus values are verified. Kevyt polttoöljy at 43 MJ/kg is realistic.
- Magnitudes are realistic: about 6 l per 100 km at 0,74 kg/l, a 35 MW peat plant from 100 MW of fuel, nuts at 24 MJ/kg, 12 MJ per day for a hiker, and bread at 1200 kJ per 100 g.
- Everything is in LaTeX, written division uses a colon, and no × appears. Scope is FY2 only. The levels hold 5, 4 and 3 tasks, and none repeats the worked example.
