VERDICT: PASS
CONTENT-HASH: b84b000bd30022fa

## Blocking

## Polish
- exercises.json:157 (fy3-5-L1-10) — the stored answer is 11,3736 kJ (five figures), but the solution's Vastaus is $11\,\text{kJ}$ (2 s.f.). Consider storing 11.4 or 11. The ±4 % tolerance still holds around either.
- exercises.json:262 (fy3-5-L2-07) — the stored answer is 50,4 J, but the Vastaus says $50\,\text{J}$ with two significant figures. Make them agree. The mean 4,20 N arguably carries three figures, so 50,4 J with that reason is also defensible.

## Checked
- I recomputed all 20 numeric answers in one script, and every one matches. ΔU = Q + W with the lesson's signs (W > 0 for work done on the system) is applied consistently in every task, answers.py and every solution.
- Guardrails:
  - "Same temperature, same internal energy" is used only where the task states an ideal gas (L3-01, L3-03, L3-04 c).
  - Heat is never "in" a body: L1-06 option 4 and L1-09 statement 5 are wrong on purpose, and their feedback is right.
  - L2-07 adds the reason that heat flows to the air, so Q < 0.
- L3-04 data is plausible. An adiabatic fit gives F(0,20 m) = 160 N with a gas column of about 0,35 m, and the isothermal work over the same stroke is about 14,7 J, consistent with the given 14,0 J.
- L3-04 trapezoid rule: 0,04 m · 468 N = 18,72 J. L3-05 losses: 8,1 / 16,3 / 26,1 / 34,8 kJ, so 14,5 % and 2,00 kW.
- L2-05 cycle: ΣQ = 130 J and ΣW = −40 J, so W₄ = −90 J. The reasoning that "the state returns, so ΔU = 0" is right.
- The figure piston-force has both end points on grid crossings, and its description gives them without the work. L2-01 and L2-08 both get W = 60 J from it.
- L1-06, L1-07 (one correct option each) and the true/false statements of L1-09 are right, and so is their feedback.
- L2-03 explains why the answer has one significant figure. L2-02 and L2-04 justify their rounding from the subtraction.
- Every solution is symbolic first, then substituted with units, with real balance checks.
