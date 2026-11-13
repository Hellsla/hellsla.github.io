VERDICT: PASS
CONTENT-HASH: 5b120f8cff7105c8

## Blocking

## Polish
- inquiry.json:116 (sim model) — "pitkäikäiseen viritystilaansa": Pa-234m has a half-life of about 1,2 min, so "long-lived" is relative at best. Fix: write "metastabiiliin viritystilaansa". This was raised in rounds 1 and 2 and is still open.
- inquiry.json:184 (gammaspektri) — "Kuvassa on gammailmaisimella mitatun spektrin muoto" says the drawing is a measured spectrum. The source_note and the figure's aria-label say the peaks are drawn schematically, and a real Co-60 spectrum also shows a Compton continuum and a sum peak. Fix: "kaavamainen kuva gammailmaisimella mitatusta spektristä".
- lesson.md:278 (decays figure) — The β⁻ panel shows the same 9 p + 11 n as the other panels, and nothing marks which neutron became a proton. The figure is labelled schematic and its Z + 1 label is right, so this is a C-level simplification. A highlighted nucleon would make the mechanism visible.

## Checked
- I recomputed all the numbers in one script with my own formulas, and they all agree with lesson-answers.py:
  - kertaus 1,89 eV
  - Cs-137 example: $E_\gamma = 1{,}0600\cdot10^{-13}$ J, hc = 1,9865·10⁻²⁵ J m, λ = 1,8740 pm, and 500 nm / λ ≈ 2,67·10⁵, which matches "noin 270 000"
  - Tc-99m: 8,8256 → 8,826 pm, the keV-as-eV mistake gives 8826 pm, and the ratio is 4,71
  - Co-60: the sum is 2505,7 keV, the ENSDF deficit 0,033 keV and my recoil estimate $\sum E^2/2Mc^2$ = 0,028 keV
  - U-235 series: 7 α and 4 β⁻; Am-241 → Np-237; Po-210 → Pb-206; C-14 has N = 8
- U-238 main branch: I applied the α/β⁻ rules from (92, 238). The chain ends at (82, 206) after 8 α and 6 β⁻, and every N matches the sim's CHAIN. koe-1 varies only k, and simState gives Z, N, A and mode. Rows 0–5 contain both kinds of decay.
- The sim's window and STABLE cells are correct: Tl-203/205, Pb-204/206/207/208 and Bi-209. The model box states the dominant-branch choice, the schematic nucleus and that decay is random. The readout equations in lang/fi.json (yhtalo_alfa, yhtalo_beeta) conserve A and Z.
- Figures:
  - The levels figure is to scale (0,108 px/keV), and Co-60 sits at Q ≈ 2822 keV.
  - The shifts grid steps are α (−2, −2), β⁻ (Z+1, N−1) and β⁺ (Z−1, N+1).
  - On the chart, β⁻ is below the band and β⁺ above it, and the Sn band (N ≈ 61–73) is plausible.
  - The isotope figure has 6p6n and 6p8n.
  - The spectrum figure's peaks are at 1173,2 and 1332,5 keV.
- The Co-60 explanation (most of the deficit is rounding, the recoil is about 0,03 keV) now reads the same in lesson.md and the gammaspektri solution, which closes the round-2 Polish item.
- Mechanisms are correct: n → p + e⁻ + ν̄ by the weak interaction, no electrons are in the nucleus, the strong force acts at short range, heavy nuclei have a neutron excess, β energies are continuous and α energies discrete. Electron capture works below the β⁺ threshold, and Be-7 → Li-7 is correct.
- Each choice item (kertaus, the two predictions, Etsi virhe, tarkistus-1) has exactly one correct option, and every distractor's feedback is right. The numeric mistakes (1332,5; 159,3; 28; 10; 5; 8826) are diagnosed correctly.
- The explain model answers, the criteria and the exit ticket agree with the theory and the summary.
- Magnitudes are right: tens of thousands of α/s fits a ~37 kBq Am-241 source, the ionisation-chamber mechanism is right, and the nucleus/atom size ratio is 10⁴–10⁵.
- Scope: FY8 "atomiytimen rakenne ja muutokset, radioaktiivinen hajoaminen" and the slot's täsmennys (nuclear levels by analogy through the gamma spectrum).
