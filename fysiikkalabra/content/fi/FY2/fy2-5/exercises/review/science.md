VERDICT: PASS
CONTENT-HASH: ca27eff8e9804aac

## Blocking

## Polish
- exercises/solutions.md:79 (fy2-5-L2-03, Järkevyys) — Problem: rounding 0,85 up to 0,9 and getting 610 MJ only shows the order of magnitude. — Fix (optional): the loss is 15 % of 680 MJ ≈ 100 MJ, so the useful energy is about 580 MJ.
- solutions.md fy2-5-L3-03, Muunnokset — Problem: "$1\,\text{h} = 3600\,\text{s}$" is stated, not substituted. This is acceptable because the task text gives it. — Fix (optional): $1\,\text{h} = 60 \cdot 60\,\text{s} = 3600\,\text{s}$.

## Checked
- The hash was ca27eff8e9804aac at the start and the end.
- The round-3 blocking item is fixed. In L2-01, 100 g and 40 g are converted to kg by substitution.
- I recomputed all 12 answers independently and they match answers.py and exercises.json: 86, 96, 312 000 → 310 000, 4000, 0,96; 480, 41,86 → 42, 578 → 580, 4,465 → 4,5; 5,209 → 5,2, 3,6, 35. Each rounded answer deviates by at most 0,8 %, inside the 2 % tolerance.
- answers.py uses the right physics on every line: E = Hm, m = E : H, E_hyöty = η E_sisään, E_sisään = E_hyöty : η, and P = E_hyöty : t with 1 MJ/s = 1 MW.
- Every solution has all seven parts. Each solves symbolically before substituting, does its conversions (GJ → MJ, t → kg, kJ → MJ, g → kg) by substitution, and justifies its rounding.
- The magnitudes are realistic: about 6 l of petrol per 100 km, a 35 MW peat plant at 35 %, kevyt polttoöljy at 43 MJ/kg, nuts at 24 MJ/kg, 12 MJ a day for a hiker.
- The levels have 5, 4 and 3 exercises. None repeats the worked example (6,0 kg of wood). All are inside FY2 scope, with one efficiency per task and no chain.
