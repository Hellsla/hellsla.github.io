VERDICT: PASS
CONTENT-HASH: 7ff4568c0902edd0
SCOPE: delta added-exercise from e73b4e5e83dd72e3 base 5b3ca4f81c77

## Blocking

## Polish
- exercises/exercises.json (fy8-7-L2-08 text) — "the number of photons per second emitted by one laser as a function of wavelength" reads as if one laser's wavelength varied; the figure is a grid with one point — e.g. "The figure shows a laser as a point: its wavelength on the horizontal axis and the number of photons it emits per second on the vertical axis." The same applies to L3-06 for two lasers.

## Checked
- L1-10: N/t = Pλ/(hc) with MAFY h = 6.62607015e-34 J s: 6.7455e15 1/s; answer 6.7e15 is 0.7 % off, inside ±2 %; with h = 6.626e-34 the same to 4 figures. Two figures from 2.0 mW justified; check 3.0e-19 J per photon and comparison with L1-07 (1.3e16 1/s) right.
- L2-08: figure point at (520 nm, 3.927e15 1/s), generated from 1.5 mW; read 3.9e15 gives 1.490 mW, readings 3.85–3.95e15 give 1.47–1.51 mW, inside ±3 %. Photon 3.8201e-19 J = 2.38 eV (green); 1.0 mW would give 2.62e15 1/s; reasonableness check is a real one.
- L3-06: points X (450 nm, 6.796e15) and Y (800 nm, 4.027e15), generated from 3.0 and 1.0 mW; exact ratio 3.000, read values give 3.022; reading ±0.1 on both axes gives 2.91–3.15, so ±4 % is tight but fair for two well-placed points. hc cancels; photon energies 4.41e-19 and 2.48e-19 J right.
- Figure grids and descriptions give every value needed; neither prints a power or the answer.
- answers.py lines for the three exercises compute the right physics (P = (N/t)hc/λ) and match exercises.json; units 1/s, mW, dimensionless correct.
- Solutions: symbolic form before substitution, conversions, rounding reason and reasonableness in each; within FY8 scope (E = hf, photon flux).
- Hash 7ff4568c0902edd0 at start and end.
