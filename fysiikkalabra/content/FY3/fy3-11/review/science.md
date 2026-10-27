VERDICT: PASS
CONTENT-HASH: 2f2d68eed3fb6d87

## Blocking

## Polish
- solutions.md:88 (L2-04, Vastaus) — "480 kW, jonka kaksi ensimmäistä numeroa ovat varmoja" is still only an assertion: the trailing zero of 480 is ambiguous. — Say that the answer takes as many figures as 480 kW, or write the power as 480 kW with three figures and answer 720 kW with three, as in L1-03.
- solutions.md:99 (L3-01, Järkevyys) — "sen häviöt ovat vain savukaasuissa" is too strong, since a boiler also loses heat through its walls and through incomplete combustion. — Write "pääosin savukaasuissa".
- solutions.md:98 (L3-01, Vastaus) — typo "polttoatehon". — Write "polttoainetehon".
- answers.py:11, 15, 34–36 — the comments are stale ("-> 37 %", "-> 22 %", "0,40", "6,0 l", "0,75", "-> 12 kW") and disagree with the task data and answers (37,2 %, 21,7 %, 0,400, 6,00 l, 0,750, 12,0 kW). The arithmetic is right. — Update the comments.

## Checked
- Hash 2f2d68eed3fb6d87 at the start and at the end. One script recomputed all 12 exercises with my own formulas: answers.py, exercises.json and my values agree (L3-02 is now 9,60 MWh, the product Q(1 − 1/ε)).
- Both round-1 Blocking findings are fixed. In the worked example, η₁ = 0,380 = 38,0 % and η₂ = 0,880 = 88,0 %, justified by the three-figure whole-megawatt powers; 310 MW and 60 MW are known to the megawatt. In L3-02, three figures are justified from 16,0 and 2,50, and the text says why the difference rule does not apply.
- Every principle applies for the reason it gives: constant p gives pΔV; a cyclic engine has ΔU = 0, so W = Q₁ − Q₂; an efficiency can be computed from powers (energy in the same time); a heat pump's heat inside is Q_ulko + E_s. Every solution solves the unknown symbolically first.
- The conversions are right (kPa→Pa, l→m³, MWh→J, TJ, km/h→s, % → decimal).
- Each Vastaus names the datum that really limits the figures. L1-04 and check-2 use the difference-of-readings rule. In L2-03 the 200 J work, known to the joule, sets the precision. In the design task, 0,40 and 0,45 set two figures.
- The reasonableness checks are real and correct: energy balances recomputed, order-of-magnitude estimates (L2-01: 160 MW electric, 390 MW fuel), typical efficiencies, the latent-heat share in L1-02 (≈ 7,5 %), the 900 J sign test in L2-03, and in L3-03 54 kWh → 15 kWh → 17 kWh.
- Inquiry recomputed: pred-1 300 J; exp-1 400 J and 600 J; return path A gives W = 0 and Q₂ = 500 J; path B gives Q₁ = 650 J, Q₂ = 550 J, W = 100 J and η ≈ 15 %. Also kertaus 250 J, virhe 360 J, the design task 2000, 1250 and 800 MW (pump 60 MW, mistakes 941 and 667), siirto 22,5 MW, check-2 450 J, and the exit ticket 100 J and 18 kW / 42 kW. Every correct option and every feedback is right.
- The new inquiry solutions (exp-1, design task, siirto, check-2 with its graph reading) are complete and their reasoning is right.
- The simulation and the figures are unchanged since round 1. The SVG arrow widths are to scale (60 = 24 + 36, 60 = 20 + 40), and the sim's monatomic model, ΔV = 2Q/(5p₁), matches its stated limits.
- Scope: W = Fs, pΔV, the first law, η and heat pumps are taught; the second law is qualitative only, with no cycle calculations. This fits FY3 and the slot note.
