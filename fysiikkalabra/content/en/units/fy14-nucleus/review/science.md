VERDICT: PASS
CONTENT-HASH: 32e35f45c81f307f

Science review of fy14-nucleus, 2026-11-01 (full review). I recomputed every number in one Python script using CODATA 2018 and AME2020 constants.

## Blocking
None.

## Polish
1. `unit.md`, *Inside the atom*: the text says "Rutherford identified the proton around 1919–1920", but the source in unit.json says 1917–1920. Make the two agree. (C: either is defensible.)
2. `unit.md`, *Key idea*: "Isotopes have the same chemistry" is a fair simplification. If you want to keep it exact, write "practically the same chemistry". Heavy water differs slightly, and the course uses it later.

## Checked
- **Numbers.** Coulomb force at 2.0 fm is 57.7 N, and both mistake values (1.15·10⁻¹³ N, 5.77·10⁻²⁹ N) are correct for the errors they name. The acceleration is 3.4·10²⁸ m/s². Gravity is about 1.24·10³⁶ times weaker than the Coulomb force. For Fe-56: nuclear mass 9.286·10⁻²⁶ kg, R = 4.59 fm, ρ = 2.29·10¹⁷ kg/m³, ρ/ρ(iron) ≈ 3·10¹³, and a teaspoon of nuclear matter has a mass of 1.15·10¹² kg. N/Z values: 1.15, 1.40, 1.49 and 1.537 for Pb-208. The alpha/electron mass ratio is 7294. The stadium analogy is right: the nucleus would be 1.7–3.7 mm across.
- **Facts.** Chadwick: Po–Be radiation on paraffin, letter of February 1932, Nobel Prize 1935. Todd and Soddy named isotopes in 1913. Deuterium is about 1 in 6420 hydrogen atoms. Tritium half-life 12.3 a, C-14 5700 a. The nuclear force is attractive from about 0.7 fm to about 2.5 fm, with a repulsive core inside. Nothing is stable above lead (Bi-209 is listed with 2.01·10¹⁹ a). The diproton is unbound.
- **Stable-nuclei table.** Every row is stable in NUBASE2020 (Ca-40 is observationally stable).
- **Choices.** Every prediction, choice and check has exactly one correct option, and each distractor's feedback gives the right reason. The model answers match the criteria.
- **Figures.** The figures agree with the text: hydrogen isotopes, notation (N = 8 for C-14), and the range bars at 0.7 and 2.5 fm with a Fe-56 diameter of 9.2 fm.
- **Isotope Builder.** Six tasks. The data matches the text for d, t, He-3, C-14 and Fe-56. For the diproton the builder says "Not in our table … probably very unstable", which is consistent with the "done" text.

## Shared issues
See the binding-energy report for the nuclides.json notes; none of them affects this unit.
