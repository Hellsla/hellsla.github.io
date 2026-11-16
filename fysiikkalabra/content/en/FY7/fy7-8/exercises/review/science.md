VERDICT: PASS
CONTENT-HASH: 3c82ce2ff300ff5d

## Blocking

## Polish
- lessons/FY7/fy7-8/answers.py:687 — the line computes with `8.0` and its comment says "8,0 V", but the task now gives $8.00\,\text{V}$; the value (1150) is the same — write `8.00` so the script matches the task data.
- content/en/FY7/fy7-8/exercises/exercises.json (fy7-8-L1-05) — the three-phase formula $P = \sqrt{3}\,UI\cos\varphi$ is taught only in the solution. The packet's exercise brief is empty, so I could not check whether the lesson teaches it — confirm it does, or else move the task to level 2 and give the formula in the task text.
- solutions.md fy7-8-L3-04 Answer — "two significant figures like the power $200\,\text{MW}$": the datum that clearly limits the precision is $0.040\,\Omega/\text{km}$ — name that one instead.
- solutions.md fy7-8-L1-05 Principle — "carries power at the phase voltage $U:\sqrt{3}$, because the voltages of the phases are out of phase" is a correct but compressed reason (120° phase shift, star connection). Fair at this level (C), so optional.

## Checked
- One script recomputed all 20 numeric answers from the task text with my own formulas. Every one agrees with exercises.json and with answers.py (to within 0.5 %).
- L1-02 after the edit: $N_1 = 40 \cdot 230\,\text{V} / 8.00\,\text{V} = 1150$. The three significant figures are justified. The check (factor ≈ 29, so ≈ 1160) is a real check.
- L2-05: fit through the origin gives k = 0.012354 V/turn and N₁ = 485.7. A free linear fit gives 486.6, inside the 3 % tolerance. The listed ratios are right.
- L2-06: efficiencies 0.539/0.758/0.828/0.865/0.877 and losses 2.1–3.2 W are right. The reason the efficiency is lowest at small load (an almost constant loss) is right. The assumption $P_1 = U_1 I_1$ is stated in the task.
- L3-05: losses, efficiencies, a = 2.03·10⁻⁴ kW⁻¹ and P = 54.35 kW are right. A least-squares fit gives 54.1 kW, inside the 5 % tolerance. The 49–57 kW spread is right.
- L3-04: R = 6.0 Ω, 909.1 A and 500 A, 4.959 MW and 1.500 MW, 30 300 MWh, 1.515 M€; shares 2.5 % and 0.75 %.
- L2-08: exactly one correct option. Each distractor's number is right (75 V; 9.45 MW at 690 V; U²/R = 800 MW). Factors 29 and 840 are right.
- L1-06: exactly one correct option, and each feedback names the right mechanism (a constant flux induces no voltage).
- Figures: loss-current points scatter around 0.8 I², and (5.0 A; 20 W) is a grid point. In loss-graph-curve, 6.0·200 MW/U² gives 3.0 % at 200 kV (a grid point), 12 % at 100 kV and 24.5 % at 70 kV (inside the axis). Neither figure gives R away.
- Two-wire model stated in every line-loss task; $U^2:R$ correctly rejected; ideal-transformer relations match the glossary; the content is inside the FY7 central contents (transformer, energy transmission).
