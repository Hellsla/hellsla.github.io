VERDICT: PASS
CONTENT-HASH: 73146e3356a7793b

## Blocking

## Polish
- sim.js:974 — the animated vibration has only a pause button, no speed control (hidas · normaali · nopea) as the lesson form asks — add a three-step speed select that scales tAnim.
- lesson.md:158-173 — the warm particles' vibration arrows are symmetric while the text stresses the asymmetric swing (farther out than in) — lengthen the outward arrowheads or label d as the mean spacing.
- lesson.md:253 — "Siksi jää kelluu ja järvet jäätyvät pinnalta" credits floating ice; the 4 °C density maximum (Ydinajatus, check-1) is the main reason the surface freezes first — name it here too.
- exercises.json fy3-8-L3-01 — Δd = 0,09 mm carries one significant figure; the answer 120 °C is fine, but 75,090 mm would justify it.

## Checked
- All 12 answers recomputed independently = answers.py and within tolerance (L3-03 457 → 460, L2-01 52,08 → 52, L1-02 −51,75 → −52).
- Worked example 0,0864 m, 0,072 %; staged and symbolic first; exit ticket 21 mm; tables α, γ realistic (air ≈ 1/293 K).
- kertaus 60 K and its distractors (333, 0, −60 K); hook's comb-joint direction (less overlap when cold) correct.
- pred-1/2 model values 6,00 / 12,0 mm, 0,0600 % match the sim's ΔL = αL₀(T − 20 °C); pred-3 feedback on asymmetric interaction, particle size and caloric correct.
- exp-1 locks material, L0, varies T; exp-2 locks material, T, varies L0; simState carries dT, dL, rel.
- Interpret table 0,36 / 2,1 / 11 / 34 cm³ per litre per 10 K correct; the correct choice's bonding argument is sound.
- virhe 28 mm vs 1,8 mm, ≈15×, 0,7 %; siirto 44 mm, mistakes 0,044 and 110, glass-corrected ≈ 43 mm, ratio ≈ 40.
- check-2 α = 23·10⁻⁶ 1/K from both columns, mistakes 46 and 15,3; check-3 model air ≈ 94× steel's 3α ("noin sata").
- sim.js: ΔL = αL₀ΔT, amplitude ∝ √T(K), lattice and rod scaled by the same 1 + EαΔT; simulaatio text "alle 0,3 %" now right (Al at 120 °C 0,23 %).
- Solutions: symbolic before substitution; L2-03 rail-gap reasoning, L3-02 bend toward steel, L3-03 can expansion 18 cm³ correct.
