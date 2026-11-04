VERDICT: FAIL
CONTENT-HASH: 91ada7bf896f45b8

## Blocking
- exercises.json:261 (L3-04) — **B**, missing condition. The task gives a wind park's *keskimääräinen* power and computes the yearly loss as R(P/U)²·8760 h. That holds only if the power is constant. Since P_h ∝ P², a varying wind power gives a larger mean loss than the mean power does, so the text teaches a wrong picture. — Fix: drop "keskimääräinen" and add "Oletetaan, että siirrettävä teho on vakio 200 MW koko vuoden". The numbers stay.

## Polish
- exercises.json:261 (L3-04) — "Johtimien resistanssi on 0,040 Ω kilometriä kohti" lets a student double the length for the return conductor (answer 3,03 M€). Write "johtimien yhteinen resistanssi on 0,040 Ω johdon kilometriä kohti", as the other tasks do.
- solutions.md:165 (L2-06) — the rounding reason is wrong: I₁ = 0,114 A has three significant figures, and so do 11,5 V and 2,00 A. Either give 87,7 % or base the two figures on 0,020 A. Also, U₁I₁ is the input power only if current and voltage are in phase (B; the primary has a magnetising current). Consider adding "ensiöteho P₁ = U₁I₁" as a stated assumption in the task.
- solutions.md:195 (L3-05) — "kaksi merkitsevää numeroa kuten vakiohäviössä 0,6 kW": 0,6 kW has one significant figure. Also, the 20 kW row gives 49 kW, not "54–57 kW". A least-squares fit P_h vs P² gives 54,1 kW. Write "49–57 kW".
- exercises.json:44 (L1-06) — "toisiokäämin jännitteeksi mitataan nolla" holds after switch-on; a brief pulse is induced when the current starts. Add "kun virta on asettunut vakioksi" (B, minor).

## Checked
- Every answer recomputed in one script (L1-07 210 kW, L1-08 90 %, L2-05 k 0,012354 V → 485,7, free fit 486,6, L2-06 87,72 %, L2-07 0,20 A, L3-04 4,959 / 1,500 MW, 1,5149 M€, L3-05 54,35 kW): all equal answers.py and exercises.json.
- L2-05: the unloaded secondary justifies U₂ : U₁ = N₂ : N₁, and the fit through the origin is physically motivated.
- L2-06 table: losses of 2,1–3,2 W grow slowly while P₂ grows tenfold, so the efficiency rises with load; the explanation is right.
- L3-05: P_h = P₀ + aP² with I = P/U at constant U is right; η is maximal where P₀ = aP², and the table's best row (60 kW, 97,9 %) agrees.
- L1-06 exactly one correct option, feedback right; L2-07 power conservation right.
- Notation matches the lesson; levels fit; no duplicate.
