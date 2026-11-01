VERDICT: PASS
CONTENT-HASH: 9b8e68e634f060d3

Science review of fy14-binding-energy, 2026-11-01 (full review). I recomputed every number using AME2020 and CODATA 2018.

## Blocking
None.

## Polish
1. `unit.md`, *Binding energy per nucleon*: "A large $B/A$ means a stable, tightly bound nucleus" is not right as it stands. B/A does not decide stability: Kr-92 (8.51 MeV, radioactive) beats He-3 (2.57 MeV, stable), and the explorer shows this. Fix: write "a tightly bound nucleus". Also drop "with little mass per nucleon", or keep it only as "roughly", because Fe-56, not Ni-62, has the least mass per nucleon.
2. `unit.md`, *Fission and fusion*: "Meitner and Frisch explained it early in 1939" contradicts the biography, which says they worked it out over Christmas 1938. Fix: "explained it at Christmas 1938 (published February 1939)".
3. `binding.js` (shared) calls the reaction's Δm "Mass defect". It is a mass difference, and "mass defect" in the unit means the nucleus's missing mass. Suggest "Mass difference".

## Checked
- **Numbers.** Tea: 63 kJ and 7·10⁻¹³ kg. He-4: Δm = 0.030377 u, B = 28.30 MeV, B/A = 7.074 MeV, and the mass loss is 0.75 %. D–T: Q = 17.59 MeV, 2.82·10⁻¹² J, and the binding-energy check of 17.60 MeV is right within rounding. The find-error value (bare proton) is 0.029279 u → 27.3 MeV. Deuteron: 2.22 MeV, and 3.56·10⁻¹³ J. U-235: total B is 1784 MeV. The U-235 → Ba-141 + Kr-92 + 3n split gives Q = 173.3 MeV. With the fragments' decay chains (≈ 26 MeV) the total is ≈ 200 MeV, so the 173/200 explanation is right. Fission gives 0.85 MeV per nucleon of fuel and D–T 3.52, about 4 times more. Nuclei with A ≈ 112 have B/A ≈ 8.5 MeV.
- **Uncertainties.** The table uncertainties are below 10⁻⁹ u, as the text says.
- **Facts.** Hahn and Strassmann, December 1938. Meitner: 1878–1968, fled in July 1938, Nobel Prize 1944 to Hahn alone, meitnerium (109). Becquerel discovered radioactivity in 1896.
- **Choices.** Every choice has exactly one correct option, with right feedback. The criteria match the models.
- **Explorer.** Q is computed from atomic masses (the electrons cancel) and checked against ΣB. The arrows leave out the neutron. The caption and aria text are correct.
