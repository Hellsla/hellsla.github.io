VERDICT: FAIL
CONTENT-HASH: 87ea237c564217c5

## Blocking
- exercises/solutions.md:56 (fy2-5-L2-01, Muunnokset) — Problem: "$100\,\text{g} = 0{,}100\,\text{kg}$ ja $40\,\text{g} = 0{,}040\,\text{kg}$" are bare equalities, not conversions by substitution, against the teacher's rule. The kJ → MJ step on the same line does substitute. — Fix: write $100\,\text{g} = 100 \cdot (1 : 1000)\,\text{kg} = 0{,}100\,\text{kg}$, and the same for 40 g.

## Polish
- solutions.md L2-03 Järkevyys — Problem: the check rounds 0,85 up to 0,9 and gets 610 MJ, which only shows the order of magnitude. — Fix (optional): check that 578 MJ is a bit under 680 MJ, the loss being 15 % ≈ 100 MJ.
- solutions.md L3-03 — Problem: "$1\,\text{h} = 3600\,\text{s}$" is stated, not substituted. It is acceptable, since the task text gives it. — Fix (optional): $1\,\text{h} = 60 \cdot 60\,\text{s} = 3600\,\text{s}$.

## Checked
- Hash 87ea237c564217c5 at the start and the end.
- All 12 answers were recomputed independently and match answers.py and exercises.json: 86, 96, 312 000 → 310 000, 4000 and 0,96; 480, 41,86, 578 and 4,465; 5,209, 3,6 and 35. Each rounded answer is within tolerance.
- answers.py uses the right physics on every line: E = Hm, m = E : H, E_hyöty = η E_sisään, E_sisään = E_hyöty : η, and P = E_hyöty : t with MJ/s = MW.
- Every solution has all seven parts and is symbolic first. GJ → MJ, t → kg and kJ → MJ are done by substitution. Division is written with a colon, and the symbolic fractions are allowed.
- The round-2 issue is fixed: the L3-01 check now says 1,87 times the oil mass, which is correct. The L1-03 wording ("noin kymmenen tonnia") and the L3-01 wording ("pitää vapautua") are fixed too.
- Magnitudes are realistic: about 6 l per 100 km, a 35 MW peat plant, kevyt polttoöljy at 43 MJ/kg, and a hiker's 12 MJ per day.
- Scope is FY2 only, with one efficiency per task and no chain. No × appears, and everything is in LaTeX.
