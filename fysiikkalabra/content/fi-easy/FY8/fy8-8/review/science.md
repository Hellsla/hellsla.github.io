VERDICT: PASS
CONTENT-HASH: b260c2a61609fe23

## Blocking

## Polish
- lesson.md:249 — "kymmeniä kiloelektronivoltteja ... Ne ovat satojatuhansia kertoja suurempia": tens of keV against eV is ~10^4, the hundred-thousand factor holds for the 0,1–1 MeV lines of the examples (wording kept from the Finnish source, C) — optionally "satoja kiloelektronivoltteja" or "kymmeniä- tai satojatuhansia".

## Checked
- All numbers in lesson.md, inquiry.json, exit-ticket.json and meta.json match the passed Finnish source token for token; the translation changes no formula, sign or condition.
- Recomputed in one script: Cs-137 example (1,0600·10⁻¹³ J, 1,874 pm, 500 nm/λ ≈ 2,67·10⁵), Tc-99m 8,826 pm, ratio 4,71, Co-60 sum 2505,7 keV, ENSDF residual 0,033 keV vs recoil ≈ 28 eV, kertaus 1,89 eV, siirto 7 α and 4 β⁻.
- Decay rules (α Z−2/A−4, β⁻ Z+1, β⁺ Z−1, γ unchanged) consistent in theory, grid-figure alt text (β⁻ up-left, β⁺ down-right), decays figure, summary, feedback and model answers.
- Easy-language rewrites keep the mechanisms: electron created in β⁻ (not pre-existing), weak interaction, β continuous spectrum via antineutrino share, recoil explanation, randomness of a single decay.
- Predictions: exactly one correct option each; every distractor's feedback names the right reason.
- Hook: ~37 kBq Am-241 gives "kymmeniätuhansia" α per second; ionisation explanation correct.
- meta.json key_concepts: nukleoni, isotooppi, alfahajoaminen, beetahajoaminen, gammasäteily all correct and consistent with glossary (neutrino omitted in beetahajoaminen: acceptable simplification, C).
- Glossary entries correct.
- Exit ticket: Po-210 → Pb-206 + α balanced; C-14 6 p, 8 n.
- Simulation is the shared course sim (passed with the source); sim-spec and model box match the U-238 chain data (8 α, 6 β⁻, ends at Pb-206).
