VERDICT: PASS
CONTENT-HASH: e622704b652606af
Mode: delta (added aineisto task fy8-3-L2-09, caption badges removed)

## Blocking
(none)

## Polish
- exercises/solutions.md:309 — "If you choose other lines of the table, for example $434.0\,\text{nm}$, they match the transitions $5 \to 2$ and $6 \to 2$" can be read as one line matching two transitions — write "$434.0\,\text{nm}$ matches $5 \to 2$ and $410.2\,\text{nm}$ matches $6 \to 2$" (model: 434.17 nm and 410.29 nm).

## Checked
- Recomputed independently: hc/656.3 nm = 3.027e-19 J = 1.889 eV; hc/486.1 nm = 2.551 eV; ΔE(3→2) = 13.6·5/36 = 1.889 eV; ΔE(4→2) = 2.550 eV; answers.py 1.888889 → box 1.89 eV, tolerance 0.02 fits.
- Model wavelengths 656.47 nm and 486.27 nm (solution 656.5 / 486.3 nm); deviation from the table 0.03 %, so "under 0.1 %" is right; air vs vacuum wavelength named as a cause, correct.
- Source facts used (Å units, air wavelengths for visible lines, 6562.8518 Å and 4861.3615 Å, several close values per line) are within the verified list; 1 Å = 0.1 nm stated in the task as required.
- Line-spectrum explanation (quantised levels, photon energy = level difference) is the right mechanism; E_n given as data, inside FY8 scope.
- Significant figures: three, from 13.6 eV, justified; reasonableness check (1240 eV nm/656 nm) is a real check.
- Caption changes "(example data)" removed: no number changed; follows the teacher's 2026-11-13 rule on provenance badges.
- Hash e622704b652606af at start and end.
