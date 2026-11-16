VERDICT: PASS
CONTENT-HASH: dcbb4a54776d9f88
SCOPE: delta added-exercise from aa0f837dfa88aba8 base 415cbc7c6bc3

## Blocking

## Polish
- content/fi-easy/FY8/fy8-3/exercises/solutions.md:309 — "esimerkiksi 434,0 nm, ne vastaavat siirtymiä 5 → 2 ja 6 → 2" pairs one line with two transitions — write "434,0 nm vastaa siirtymää 5 → 2 ja 410,2 nm siirtymää 6 → 2".

## Checked
- Recomputed: 6562,8518 Å = 656,3 nm, hc/λ = 3,0268e-19 J = 1,8894 eV; 486,1 nm gives 4,0866e-19 J = 2,5509 eV ✓.
- ΔE(3→2) = 13,6 eV·5/36 = 1,8889 eV and ΔE(4→2) = 13,6 eV·3/16 = 2,550 eV; answers.py gives 1,888889 ✓. Box 1,89 eV with relative tolerance 0,02 ✓.
- Model wavelengths 656,47 nm and 486,27 nm differ from the table by under 0,1 % ✓, as the brief asks; the air-wavelength remark is right.
- Extra lines checked: 434,0 nm gives 2,857 eV against 5→2 at 2,856 eV, and 410,2 nm gives 3,023 eV against 6→2 at 3,022 eV ✓.
- Source facts: the table is in Å with air wavelengths for visible lines, the strongest values 6562,8518 and 4861,3615 Å, and close parallel values (fine structure) that may all be used, all on the verified list ✓. The task states 1 Å = 10⁻¹⁰ m = 0,1 nm.
- The line-spectrum explanation (quantised levels, a photon carries the difference) and the energy-conservation principle are right; constants given; three significant figures justified by 13,6 eV.
- Hash dcbb4a54776d9f88 at the start and the end.
