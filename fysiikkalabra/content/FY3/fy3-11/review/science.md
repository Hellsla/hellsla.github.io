VERDICT: FAIL
CONTENT-HASH: 6810b9a2ace291b4

## Blocking
- lesson.md:216 (Esimerkki, Tulos) — the efficiencies are rounded to 38 % and 88 % "kahdella numerolla, mikä on vähemmän kuin tehojen ... tarkkuus sallisi". The text admits the data allows more and names no limiting datum. This breaks the three-figure rule and contradicts L1-03 and L1-05, which give 37,2 % and 21,7 % from the same kind of data. The worked example is the model students copy. — Give $\eta_1 = 0{,}380 = 38{,}0\,\%$ and $\eta_2 = 0{,}880 = 88{,}0\,\%$, and justify three figures from the whole-megawatt powers 190, 150, 290 and 500 MW. The same reading already justifies 310 MW and 60 MW.
- solutions.md:108 (L3-02, Vastaus) — the answer 9,6 MWh is justified by the decimal-place rule on $16{,}0 - 6{,}40$. But 6,40 MWh is derived from 16,0 MWh and is not an independent reading, so the two errors are correlated. The saving is $\Delta E = Q(1 - 1/\varepsilon) = 16{,}0\,\text{MWh} \cdot 0{,}600$, a product of three-figure data, which gives 9,60 MWh with three figures (±0,03). The stated limiting datum does not really limit the result. — Answer 9,60 MWh, justify it with $Q(1-1/\varepsilon)$ (data 16,0 and 2,50, three figures each), and set exercises.json `answer` to 9.60 (the tolerance is unaffected).

## Polish
- solutions.md:88 (L2-04) — "480 kW, jonka kaksi ensimmäistä numeroa ovat varmoja" is an assertion. The trailing zero is ambiguous, and the result 720 kW is the same either way. Say that the answer has as many figures as 480 kW, or give the power as 480 kW with three figures, as in L1-03.
- answers.py:11, 15, 34–36 — stale comments: "-> 37 %", "-> 22 %", "0,28", "6,0 l", "0,75" disagree with the task data and answers (37,2 %, 21,7 %, 0,280, 6,00 l, 0,750). The arithmetic is right.
- solutions.md:99 (L3-01) — "sen häviöt ovat vain savukaasuissa" is too strong (a boiler also loses heat through its walls and through incomplete combustion). Write "pääosin savukaasuissa".

## Checked
- All 12 exercise answers recomputed in one script from the task data with my own formulas: answers.py, exercises.json and my values agree. L1-02's 1,70 l agrees with ideal-gas steam (1,704 l). L2-03's W/Q = 2/7 is consistent with diatomic air.
- Worked example: 0,38, 310 MW, 0,88, 60 MW. Its energy balances and its reason for the lower CHP electricity are correct.
- Each solution's principle applies for the reason it gives (constant p → $p\Delta V$; cycle ΔU = 0 → $W = Q_1 - Q_2$; power ratio = energy ratio). Unknowns are solved symbolically and the conversions (MWh→J, l→m³, km/h→s) are right.
- The reasonableness checks are real: energy balances, order-of-magnitude estimates, typical efficiencies, and the 900 J sign test in L2-03.
- Sim: monatomic ideal gas, ΔV = 2Q/(5p₁). Return A gives Q₂ = Q and W = 0. Return B gives Q₁ = 650 J, Q₂ = 550 J, W = 100 J, η = 15 %, and W equals the lifted weight's (p₁−p₂)ΔV. The model limits are stated.
- inquiry.json: pred-1 300 J (Q = 750 J), exp-1 400 J/600 J, pred-2/exp-2 numbers, kertaus 250 J, virhe 360 J, suunnittele 2000/1250/800 MW (pump 60 MW), siirto 22,5 MW, check-2 450 J (difference of readings → 2 figures), exit-ticket. All correct options and feedback are right.
- exp-1 varies only Q at fixed p₁. exp-2 locks Q and p₂ and varies only the return path. simState gives dV, dU, Q1, Q2, W and eta (eta only once the cycle is done).
- Figures 3 and 4: the arrow widths are to scale (60 = 24 + 36; 60 = 20 + 40, 3× the electricity arrow).
- Scope: $W = Fs$, $p\Delta V$, the first law, η, heat pumps and the second law are qualitative only, with no cycle calculations. This fits FY3 and the slot note.
