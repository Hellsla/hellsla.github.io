VERDICT: PASS
CONTENT-HASH: e3a9ded2e50a2046

## Blocking

## Polish
- inquiry.json:206 (gammaspektri, Järkevyys) — "Fotonien summa jää siitä alle 0,1 keV, koska fotonin lähtiessä ydin saa rekyylin" puts the whole visible 0,1 keV gap (2505,8 − 2505,7) down to recoil. lesson.md now says correctly that most of the gap is rounding and the recoil is only about 0,03 keV. Use the lesson's wording here too: "suurin osa erosta on pyöristystä; rekyyli on vain noin $0{,}03\,\text{keV}$".
- inquiry.json:116 (sim model) — "pitkäikäiseen viritystilaansa": Pa-234m has a half-life of about 1,2 min. "metastabiiliin viritystilaansa" or "suhteellisen pitkäikäiseen" would be more accurate. Carried over from round 1.

## Checked
- I recomputed all the numbers in one script with my own formulas, and they match: worked example $E_\gamma = 1{,}0600\cdot10^{-13}$ J, $hc = 1{,}9865\cdot10^{-25}$ J m, λ = 1,874 pm, 500 nm / λ ≈ 2,7·10⁵; Tc-99m λ = 8,8256 → 8,826 pm (keV taken as eV gives 8826 pm); energy ratio 4,71; kertaus 1,89 eV; Co-60 sum 2505,7 keV; U-235 series 7 α and 4 β⁻; Am-241 → Np-237; exit ticket Pb-206 and N = 8. lesson-answers.py agrees.
- Round-1 fixes: the energy ratio is now "kymmeniätuhansia tai satojatuhansia" (tens of keV / eV ≈ 10⁴, consistent). Element change now includes electron capture. The Co-60 rounding versus recoil sentence is right: ENSDF deficit 0,033 keV, my $E^2/2Mc^2$ estimate 0,028 keV. The tarkistus-1 photon sentence is fixed.
- U-238 main branch: applying the modes by the α/β⁻ rules from (92, 238) ends at (82, 206) with 8 α and 6 β⁻. This is the same CHAIN in sim.js and lesson-answers.py. simState gives Z, N, A and mode for koe-1, and koe-1 varies only k.
- The sim's STABLE cells (Tl-203/205, Pb-204/206/207/208, Bi-209) are right for its window. The model box states the dominant-branch choice and the schematic nucleus. The 1280 px capture shows the right labels and readout.
- Levels figure is linear at 0,108 px/keV, so it is to scale as stated. The Co-60 level sits at Q = 2823 keV, and the β⁻ decay goes to 2505,8 keV. Shifts figure: α (−2, −2), β⁻ (N−1, Z+1), β⁺ (N+1, Z−1). The chart has β⁻ below the band, β⁺ above it and α down-left.
- Decay, EC (Be-7 → Li-7) and Cs-137 → Ba-137 equations conserve A and Z. The EC energy condition relative to β⁺ is correct.
- Mechanisms: n → p + e⁻ + ν̄ by the weak interaction, no electrons in the nucleus, the strong force's short range, the neutron excess in heavy nuclei, beta's continuous energies because of the antineutrino, discrete α energies.
- Every choice item (kertaus, both predictions, Etsi virhe, tarkistus-1) has exactly one correct option, and every distractor's feedback is right. The numeric mistakes (1332,5; 159,3; 28; 10; 5; 8826) are diagnosed correctly.
- Hook: tens of thousands of α/s fits a ~37 kBq source, and the ionisation-chamber mechanism is right. Nucleus/atom size ratio 10⁴–10⁵.
- Scope: FY8 "atomiytimen rakenne ja muutokset, radioaktiivinen hajoaminen" and the slot's täsmennys (nuclear levels by analogy with the gamma spectrum).
