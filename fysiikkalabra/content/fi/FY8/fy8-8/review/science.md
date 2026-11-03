VERDICT: FAIL
CONTENT-HASH: c43174dd158bac10

## Blocking
- lesson.md:363 and :371 — A: worked example converts 61{,}7\,\text{keV} = 1{,}0600\cdot10^{-14}\,\text{J}$; correct is {,}0600\cdot10^{-13}\,\text{J}$ (61\,700\cdot1{,}602\cdot10^{-19}$). With the printed denominator the division gives {,}874\cdot10^{-11}\,\text{m}$, not the stated {,}8740\cdot10^{-12}\,\text{m}$ (the final {,}874\,\text{pm}$ is right). lessons/FY8/fy8-8/lesson-answers.py:27 hides it — fix the exponent in both lines and the script.
- lesson.md:250, :252/:261 (levels figure), inquiry.json:206 — A: Ni-60 upper level attributed to NNDC as 505{,}7\,\text{keV}$; ENSDF level energy is 2505,753 keV (→ 2505,8), level 1332,514 (→ 1332,5). Gammas 1173,228 and 1332,492 keV are right; their sum 2505,72 falls ~0,03 keV short of the level because of nuclear recoil. The solution's "NNDC:n tietokannan mukaan tasot ovat juuri 1332,5 ja 2505,7 keV" is false. Fix: give the level as $\approx 2506\,\text{keV}$ / "noin 2,51 MeV" in text and figure, and in the solution say the sum agrees with the tabulated level within 0,1 keV (or cite 2505,8 and name the recoil share in one clause).
- glossary.json:1925 "beetahajoaminen" — B: defines only β⁻ (n→p, electron + antineutrino) while the lesson (lesson.md:258, Kaava, chart and shifts figures) and exercise L1-05 teach β⁺ as beetahajoaminen too. Fix: "…neutroni muuttuu protoniksi (β⁻: elektroni ja antineutriino) tai protoni neutroniksi (β⁺: positroni ja neutriino)."
- assets/sims/fy8/fy8-8/sim.js:13–14 — A: model text (inquiry.json:116) says the green cells are the region's stable nuclides, but the chart starts at N = 122 and omits stable Tl-203 (Z 81, N 122) and Pb-204 (Z 82, N 122). Fix: add [81,122], [82,122] to STABLE (and sim-spec), or start the chart at N = 123.

## Polish
- lesson.md:248 — "kymmeniä kiloelektronivoltteja … satojatuhansia kertoja enemmän": tens of keV / a few eV is ~10⁴; say "tuhansista satojentuhansien kertoihin" or "sadoista kiloelektronivolteista megaelektronivoltteihin".
- inquiry.json:116 — "pitkäikäiseen viritystilaansa": Pa-234m has T½ ≈ 1,2 min; "metastabiiliin" is more exact.

## Checked
- U-238 chain: all 14 steps, modes (8 α, 6 β⁻), branches (Po-218, Bi-214, Pb-210, Bi-210 minor branches correctly called rare), Bi-209 quasi-stable.
- Cs-137 661,7 keV, Am-241 59,54 keV, Tc-99m 140,5 keV, Co-60 γ 1173,2/1332,5 keV agree with ENSDF (NuDat unreachable: 403).
- Recomputed: kertaus 1,89 eV, tarkistus-2 8,826 pm (mistake 8826), siirto 7 α/4 β⁻, interpret 2505,7, worked-example λ and 270 000 ratio.
- Predictions: exactly one correct each, distractor feedback correct; Etsi virhe C-14 → N-14.
- Figures: levels to scale (Co-60 Q ≈ 2,82 MeV), shifts arrows α (−2,−2), β⁻ (+1,−1), β⁺ (−1,+1); chart β⁻ below / β⁺ above band.
- Decay equations, positron notation, β spectrum continuous vs α/γ discrete, nucleus size ratio 10⁴–10⁵.
