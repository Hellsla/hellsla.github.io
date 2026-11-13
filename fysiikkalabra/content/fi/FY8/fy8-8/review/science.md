VERDICT: PASS
CONTENT-HASH: 4c90a57d51c6dba6

## Blocking

## Polish
- lesson.md:259 — "kymmeniä kiloelektronivoltteja tai enemmän, satojatuhansia kertoja enemmän": tens of keV is about $10^4$ times a few eV, so the low end of the range contradicts the factor — write "kymmenistä tuhansista miljooniin kertoja" or start the range at hundreds of keV.
- lesson.md:401 — "Alkuaine vaihtuu vain alfa- ja beetahajoamisessa" leaves out electron capture, which was taught a few paragraphs earlier ($Z - 1$) — add "ja elektronisieppauksessa" (or "alfa- ja beetahajoamisessa ja niiden kaltaisissa").
- lesson.md:261, inquiry.json:206 — the rounded data show 2505,8 − 2505,7 = 0,1 keV, and almost all of that is rounding. The true recoil deficit is 0,033 keV from ENSDF (my estimate is 28 eV from $E^2/2Mc^2$). "alle 0,1 keV" is correct, but a student may put the visible 0,1 keV down to recoil. A half-sentence on rounding would help.
- inquiry.json:315 (tarkistus-1) — "Fotoni ei ole hiukkanen, joka sisältäisi protonin" can be read as "a photon is not a particle". Use "Fotoni ei sisällä protonia".
- inquiry.json:116 (sim model) — "pitkäikäiseen viritystilaansa": Pa-234m has a half-life of about 1,2 min, so "metastabiiliin" or "suhteellisen pitkäikäiseen" fits better.

## Checked
- I recomputed everything in one script with my own formulas, and every value matches: worked example $E = 1{,}0600 \cdot 10^{-13}$ J, λ = 1,874 pm, ratio to 500 nm ≈ 2,7·10⁵; Tc-99m λ = 8,826 pm (the keV-as-eV mistake gives 8826 pm); ratio 4,71; kertaus 1,89 eV; Co-60 sum 2505,7 keV; U-235 series 7 α and 4 β⁻; exit ticket Pb-206 and N = 8; Am-241 → Np-237.
- U-238 main branch in the sim and lesson-answers.py: all 14 steps match NNDC (8 α, 6 β⁻; Pa-234m, Bi-214 and Po-218 by their dominant branch, which the model box states). simState gives k, Z, N, A and mode for koe-1, and koe-1 varies only k.
- STABLE cells (Tl-203, Pb-204, Tl-205, Pb-206/207/208, Bi-209) are right and none is missing in the window Z 81–93, N 122–147.
- Levels figure is to scale (0,1081 vs 0,1079 px/keV), and the Co-60 ground state sits at its Q value. Shifts figure: α (−2, −2), β⁻ (−1 N, +1 Z), β⁺ (+1 N, −1 Z). Isotope figure counts 6p+6n and 6p+8n. The nuclide-chart arrows and the β∓ sides are right; the band is schematic (C).
- Decay equations and the electron-capture equation (Be-7 → Li-7) conserve A and Z; the EC energy condition compared with β⁺ is correct.
- Gamma energies (Cs-137 661,7, Tc-99m 140,5, Ni-60 levels and lines) agree with ENSDF; the recoil explanation is physically right.
- Mechanisms are right: n → p + e⁻ + ν̄ by the weak interaction, no electrons in the nucleus, the strong force's short range, the neutron excess in heavy nuclei, beta's continuous spectrum explained by the antineutrino.
- Every prediction, Etsi virhe and tarkistus-1 item has exactly one correct option, and each distractor's feedback is right. The numeric mistakes (28, 10, 5, 1332,5, 159,3) are diagnosed correctly.
- Hook: Am-241 activity of tens of thousands of α/s, the ionisation-chamber mechanism and the "decades" lifetime are plausible.
- Spectrum capture: peaks at the stated energies; the Compton continuum is drawn schematically, as the source note says.
- Scope is within FY8's "atomiytimen rakenne ja muutokset" plus the slot's täsmennys.
