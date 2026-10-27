VERDICT: PASS
CONTENT-HASH: fdcab429ebd8dd6e

## Blocking

## Polish
- inquiry.json:480 (check-2, Periaate): "pV = NkT" uses a k that the lesson never defines. Write "p = nRT/V ja n ∝ N, joten p ∝ NT/V".
- solutions.md:118 (L3-03, Vastaus): says M = 29 g/mol "ei rajoita". M has two figures, as Δp = 3,0 bar does, so it limits the answer just as much. Name both data.
- solutions.md:119 (L3-03, Järkevyys): the "30 % ylipaineesta … koska ilmanpaine ei vuoda" sentence is muddled. The 11,0 bar total also assumes an atmospheric pressure of 1,0 bar, and the solution never says so.
- solutions.md:79 (L2-03, Järkevyys): "lämpötila nousee, kun kaasua puristetaan" holds for this data (a fast compression), not for every compression.

## Checked
- Round-1 blocking items are fixed. laske-r gives its Vastaus as 8,3 J/(mol·K) with two figures, limited by m = 0,83 g, with 0,2075 kept as an intermediate value. siirto now shows m = 2644,8 kg, which rounds to 2,64·10³ kg.
- One script recomputed all 12 exercise answers independently, side by side with answers.py. All agree, and every stated answer is within 0,5 % of the exact value, inside its 2 % tolerance.
- Inquiry and other numbers recompute correctly:
  - laske-r 8,302 and its mistakes 121,7, 8302 and 0,008302.
  - siirto n = 91 200 mol, m = 2645 kg, mistakes 9870 and 2,64.
  - check-2 3,0, virhe 1,2 and 0,083 mol, exp-2 N = 50, exit ticket 0,601 mol.
  - The pV/(NT) column of the table (0,98, 0,98, 0,99), and the m/M values 0,2064–0,2076.
- Worked example: 0,2073 mol and 0,83 g. Two figures is justified by 5,0 l and 4,0 g/mol. The 24 l/mol check and the 6,0 g air comparison are independent checks.
- Every solution's stated principle applies, and its reason is right: closed vessel, so nR is constant (L2-03); equal n at the same p, V and T (L3-02); gauge pressure cancels in a difference (L3-03); n has no M in it (L1-03, L3-01).
- Conversions are correct: l→m³, kPa/MPa/bar→Pa, g↔kg, θ+273,15. Each unknown is solved in symbols before substitution.
- Differences of data keep the right figures: 10,0 − 7,0 bar = 3,0 bar and 40 − 29 g/mol = 11 g/mol, two figures each.
- Reasonableness checks are real and correct, for example:
  - L1-04 gives 16 °C at 101 kPa.
  - L2-02 gives the gas masses 0,16, 1,32, 1,65 and 1,81 g.
  - L3-02 back-computes 21,8 − 15,8 = 6,0 g.
  - L3-03 gives 2,64 kg in total and a 27 % share.
  - siirto gives 3360 · 293/373 ≈ 2640 kg.
- sim.js, the figures and lesson.md's theory are unchanged since my round-1 full review, which checked them: impulse per perimeter per time gives NkT/A, speeds scale as √T, and the figure ratios (√(29/4) = 2,69, √2) are right.
- Every correct option and every feedback in inquiry.json is physically right, including pred-1's statement that helium makes more hits, each weaker. The experiments lock T and V and vary only N.
