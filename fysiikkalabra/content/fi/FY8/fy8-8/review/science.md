VERDICT: PASS
CONTENT-HASH: 37344eea11544f32

## Blocking

## Polish
- lesson.md:248 — "kymmeniä kiloelektronivoltteja … satojatuhansia kertoja enemmän": tens of keV over a few eV is ~10⁴, not 10⁵; say "tuhansista satojentuhansien kertoihin" — or drop "kymmeniä".
- inquiry.json (sim model text) — "pitkäikäiseen viritystilaansa": Pa-234m has T½ ≈ 1,2 min; "metastabiiliin viritystilaansa" is more exact.

## Checked
- Round 1 fixed: worked example $E_\gamma = 1{,}0600\cdot10^{-13}\,\text{J}$ (recomputed 1,06004·10⁻¹³); 1,9865·10⁻²⁵ / 1,0600·10⁻¹³ = 1,8741·10⁻¹² m, printed 1,8740 (full-precision value 1,87396) — consistent; lesson-answers.py now e13.
- Round 1 fixed: Ni-60 level 2505,8 keV in text, levels figure and its alt text; recoil sentence true (sum 2505,72 vs ENSDF 2505,753, recoil 0,012 + 0,016 keV = 0,028 keV < 0,1 keV); inquiry interpret solution says the same; answer 2505,7 is the photon sum, as asked.
- Levels figure still to scale: 1332,5 at y 200 (computed 200,2), Co-60 at ≈ 2825 keV (Q ≈ 2,82 MeV).
- Round 1 fixed: glossary "beetahajoaminen" now covers β⁻ and β⁺, matches lesson text and Kaava.
- Round 1 fixed: sim STABLE adds Tl-203 [81,122] and Pb-204 [82,122]; sim-spec agrees; 1280 px capture shows both green in the N = 122 column. In the chart window (Z 81–93, N 122–147) the stable set Tl-203/205, Pb-204/206/207/208, Bi-209 is now complete.
- Spectrum figure labels 1173,2 and 1332,5, so the new hint "Lue kummankin piikin energia kuvasta" is answerable; the removed numbers from the item text do not leave it underdetermined.
- Th-234 prediction prompt: the removed "yhtä raskaaksi" clause no longer hints the answer; options and feedback unchanged and correct.
- Decay equations, U-238 chain (8 α, 6 β⁻), shifts figure, β spectrum continuous vs α/γ discrete: unchanged since round 1, still correct.
