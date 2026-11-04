VERDICT: PASS
CONTENT-HASH: 00b576af999c02d9
Round: 2

## Blocking
(none)

## Polish
- L3-04 b and L2-05 b teach the same point: a pressure change alone does not show how much gas left when the temperature changed. L3-03 is also a Δn tank task. For a distinct level 3, make c) (the balloon count, or the end limit at 101 kPa) the boxed result, or say in the plan line that L3-04 builds on L2-05.
- solutions.md:184 (L3-04 Vastaus a) — $n_3 = 5{,}32$ mol has three digits, but $p_3 = 6{,}5$ bar has two. Write 5,3 mol, or say that it is an intermediate value.
- solutions.md (L3-04 Järkevyys) — "Yksi litra ilmaa … 0,041 mol": say "kaasua", since the gas is helium.
- L3-04 — a real cylinder gauge shows overpressure. The task says "kokonaispaine", so the data are consistent, but adding "(mittari on kalibroitu kokonaispaineelle)" or using 15,2 / 12,0 / 7,5 bar as gauge readings would make the setup realistic.

## Checked
- Round-1 Blocking (L3-04 CO₂ Z table) resolved: the task has been replaced by a helium cylinder task. The plan line in docs/exercise-bank/FY3.md is updated to match.
- New L3-04 recomputed: n₁ = 12,29, n₂ = 9,000, n₃ = 5,318 mol; m = 27,87 g → 28 g (answers.py agrees); one balloon is 0,2066 mol; 33,7 balloons used (15,9 + 17,8); 21,7 more down to 101 kPa, so "21 täyttä" is right; the pressure-difference shortcut gives 25,2 g, too small for the reason stated. The model assumptions are stated, and the task is level 3 YO style.
- Round-1 Polish resolved: L1-07 is 2,3 l (2,314 l intermediate, answer 2.3); L3-05 now gives the ICAO-rounding reason; L2-05 uses a realistic 300 kPa total pressure.
- L2-05 (new numbers): 322,6 kPa without a leak and a leaked share of 5,47 % → 5,5 %.
- L2-06: least-squares fit 0,408 cm³/K + 1,1 cm³; the line values 115,4 and 148,0 cm³ match; n = 4,95 mmol → 5,0 mmol.
- L2-07 (new B volumes): pV is 244 (A) and 304,5–306 (B); exactly one correct option, and its feedback says 305.
- L3-05 c: the linear estimate gives 12,8 km. "Todellinen raja hieman korkeammalla" is right: V(h) is convex, and the ICAO profile gives about 13,3 km.
- All 20 answers recomputed in one script; they agree.
- Hash unchanged at the start and the end.
