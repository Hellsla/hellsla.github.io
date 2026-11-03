VERDICT: FAIL
CONTENT-HASH: d5b2bdee471e987e

## Blocking
- exercises.json:73 (fy6-6-L2-04) — **B**: $Pt = cm\Delta T$ holds only while the water does not boil or evaporate. The task gives no starting temperature and does not state this, but solutions.md (L2-04 Periaate) assumes "eikä olomuoto muutu". Guardrails require that the model's assumptions are stated in the task and that the solution uses the same ones. — Fix: give the starting temperature (for example "vettä, jonka lämpötila on 20 °C") or add "ja ettei vettä höyrysty", as the lesson's transfer task does.

## Polish
- exercises.json:38 (fy6-6-L1-05) and figure ex-pi — the four points are called measured, yet they lie exactly on $P = 5I^2$. Either call them model values or say in the solution that real measured points do not usually lie exactly on the curve (guardrail "Fits").
- solutions.md:80 (L2-03 Järkevyys) — "Tavallisessa 5 V:n tai 9 V:n piirissä vastus on turvallisella alueella": add "vaikka koko jännite olisi vastuksen yli", which is the case that makes the claim true.
- solutions.md L1-03 — "kolme merkitsevää numeroa kuten jännitteessä" depends on reading 230 V as three significant figures. The figure is acceptable, but "verkkojännite 230 V" could be named as the convention.

## Checked
- All twelve answers recomputed in one script with independent formulas, and all agree with answers.py and exercises.json: 12 W, 1,88 W, 1,996 kW, 64,8 kJ, 5,0 Ω, 7,83 A, 3,2 W, 15,8 V, 17,9 K, 20,4 W, 287,5 Ω, 12 Ω.
- ex-pi: the points (0,5; 1,25), (1; 5), (1,5; 11,25), (2; 20) sit on 5 W and 0,5 A gridlines. The description gives the same data and does not give away R.
- L3-01 states the constant-resistance assumption. In L3-02 the hot resistance is asked "kun sarja palaa". L2-02 and L3-03 state an ideal source and wires.
- Every solution solves symbolically before substituting, and its conversions (kW, kΩ, h, min) are right.
- Rounding is justified by the limiting datum, and the reasonableness checks are real cross-checks: another formula, the energy balance, or a typical device rating.
- The notation (P, U, I, R, E = Pt, c, m, ΔT) and the energy wording ("muuttuu sisäenergiaksi", "valoksi ja sisäenergiaksi") follow the lesson and the FY6 rules.
- The tolerances (0,02, and 0,03 for L3-01) fit the data's significant figures.
