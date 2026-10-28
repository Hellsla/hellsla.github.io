VERDICT: PASS
CONTENT-HASH: 897018d85cf70a95

## Blocking

## Polish
- inquiry.json:348 (kokeile.calc) — the formula $v_x' = 2w - v_x$ uses $w$, which the text never defines — define $w = -u$ or write $|v_x'| = |v_x| + 2u$.
- sim.js:1127-1128 — `fi` and `fs` are now unused after the TeX readout — remove them.
- exercises.json L3-03 / solutions.md — the solution relies on "ideaalikaasun sisäenergia riippuu vain lämpötilasta ja määrästä", but the task never says the gas is ideal — add "ideaalikaasu" to the task (carried over).
- exercises.json L2-04 — 2,0 kJ of heat in 40 s (50 W) into a cold jug is about 3× realistic — e.g. Q = 1,0 kJ and ΔU = 11 kJ (t stays 40 s) (carried over).

## Checked
- Commit 31bb150 for fy3-5: the sim.js physics (step, bounce, wall, update, adapter) is untouched; only the canvas labels and the readout are now TeX strings. The 1280 px and koe-2 captures show KaTeX rendering correctly.
- Test diff: no physics check lost. Readout and label assertions check the same numbers in TeX form (+40,8 J, 0,0 J, 407 K, +114 K, 75 %, 1,85 p₀). The removed assertion checked the wording of the Lisätietoja box. That text now sits in inquiry.json howto/model/calc, and I reviewed it here. The 2u rule is still covered by the simBounce assertions (and by a new one), the 0,359 J/K scale by ΔT/W = 2,786 K/J. The bookkeeping, conducting-wall, determinism and pressure assertions are unchanged.
- I re-derived model/calc: real air in an adiabatic compression to 75 % gives 35,8 K and 12,8 J, isothermal 12,1 J. The model gives 407,2 K, W ≈ 40,9 J, p/p₀ = 1,85, piston pressure 2,37 p₀ ≈ 2,4, and 1,33 p₀ conducting. All match the text and the tests.
- One script recomputed all 12 exercises (all agree), plus siirto 5,4 J (mistakes 6,6 and 599,4), check-2 30 J (230 and 10), virhe 160, exit 180 and example 110 J.
- The feedback numbers in pred-1, pred-2 and koe-2 match the asserted sim values. koe-1 and koe-2 each lock the other parameter, and simState gives every measured key.
- ΔU = Q + W (W done on the system) is consistent across the formula, figures 1–3, the example, solutions, hints and feedback. It stays within FY3 scope (first law only, W = Fs).
- Mallin oletukset states the model's limits.
- Hash identical at start and end.
