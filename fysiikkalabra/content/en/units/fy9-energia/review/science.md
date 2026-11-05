VERDICT: PASS
CONTENT-HASH: b346ed8b9e1ca0c5

Science review, round 3, of the English translation of fy9-energia (source content/fi/units/fy9-energia/, already passed).

## Blocking
None (rounds 1 and 2 had none).

## Changes since round 2
- The only content change is the redrawn concept map in unit.md: its branch headings are now `\textbf{power}`, `\textbf{efficiency}`, `\textbf{source of energy}`, which are correct physics English. No formula, number, answer or correct flag changed (commit 433d9adba diff for this unit: only foreignObject widths and the three heading texts in unit.md).

## Checks done
- python3 scripts/check_i18n.py: no errors for fy9-energia (the one en error reported is in fy9-lampo, another unit).
- python3 scripts/units.py check and python3 scripts/practice.py check: en/units/fy9-energia OK, 6 tasks, 90 points.
- Round-1 recomputations (chain 198 MW, pumped storage 75 %, kettle 83.4 %, pellets 3.7 t, January extrapolation 230 kWh, k ≈ −4.9 kWh/°C) still stand; the concept map formulas (P = ΔE/Δt, E = Pt, 1 kWh = 3.6 MJ, η = E_a/E_o, E_o = E_a + E_h, η = η1 η2 η3, E = Hm, W = Fs, W = mgh) match the Finnish.

## Polish
None.
