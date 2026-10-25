VERDICT: PASS
CONTENT-HASH: eb6e34926d620a2b

## Blocking

## Polish
- inquiry.json simulaatio text — "todelliset muutokset ovat alle prosentin kymmenesosia" is ambiguous; aluminium at 120 °C reaches 0,23 % — say "alle 0,3 %".
- lesson.md Ydinajatus SVG — the warm particles' vibration arrows are drawn symmetric while the text stresses the asymmetric swing (farther out than in) — consider a longer outward arrowhead or a note that d is the mean spacing.
- sim.js — no speed control (hidas · normaali · nopea) for the animated vibration, as the lesson form asks; only a pause button.
- exercises.json fy3-8-L3-01 — Δd = 0,09 mm carries one significant figure, answer 120 °C is fine but "0,090 mm" (75,090) would justify the precision.
- lesson.md Yleinen virhekäsitys — "jää kelluu ja järvet jäätyvät pinnalta" leans on ice floating; the 4 °C density maximum (stated in Ydinajatus) is the main reason the surface freezes first.

## Checked
- All 12 answers recomputed independently = answers.py, all within tolerance (L3-03 457 → 460, L2-01 52,08 → 52).
- Worked example 0,0864 m, 0,072 %; exit ticket 21 mm; tables α, γ realistic (air 1/T = 3,41·10⁻³ 1/K).
- pred-1/2 model values 6,00 / 12,0 mm and 0,0600 % match the sim's ΔL = αL₀(T − 20 °C).
- pred-3 feedback: asymmetric potential explanation correct; Cem's and Daniel's misconceptions repaired correctly.
- Interpret table 0,36 / 2,1 / 11 / 34 cm³ per litre per 10 K correct.
- siirto 44 mm, mistakes 0,044 and 110, glass-corrected ≈ 43 mm, ratio ≈ 40 correct.
- check-2 α = 23·10⁻⁶ 1/K, mistakes 46 and 15,3 correct; virhe item 28 mm vs 1,8 mm, "15×" correct.
- check-1 (4 °C density maximum) and check-3 model answer (air ≈ 94× steel's 3α) correct.
- Experiments: exp-1 locks material, L0, varies T; exp-2 locks material, T, varies L0; simState carries dT, dL, rel.
- sim.js: ΔL = αL₀ΔT, amplitude ∝ √T(K), lattice and rod scaled by the same 1 + EαΔT, chart range fits all L₀; solutions symbolic before substitution, L1-04 note about water's growing γ verified (real ≈ 0,90 l).
