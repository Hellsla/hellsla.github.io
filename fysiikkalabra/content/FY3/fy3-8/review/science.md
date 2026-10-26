VERDICT: PASS
CONTENT-HASH: c12bfebed8c95baf

## Blocking

## Polish
- lesson.md:98 — the particles figure draws the vibration arrows symmetric (equal left and right), which is exactly Cem's rejected model in pred-3, while the paragraph above explains that the outward swing is longer — draw the outward arrowhead of each warm particle longer than the inward one.
- inquiry.json:245 and lesson.md:156 — the gas's large expansion is credited only to "weak bonds / nearly free particles"; for an ideal gas at constant pressure the reason is that V ∝ T (γ = 1/T ≈ 3,4·10⁻³ 1/K at 20 °C), which the lesson *Kaasujen tilanmuutokset* gives — add half a sentence that the gas value follows from V ∝ T, so the bond picture is not read as the whole story.
- inquiry.json:139 — "ohuet suorat ovat muiden aineiden suorat: jyrkin on alumiini" is false when aluminium itself is selected (it is then the thick line) — say "jyrkin suora on alumiinin, loivin borosilikaattilasin".

## Checked
- All 12 exercise answers recomputed independently (one script) and against answers.py: every one inside tolerance.
- Worked example 12·10⁻⁶·120·60 = 0,0864 m, 0,07 %; symbolic step before substitution; units check.
- Tables: α (steel 12, Al 23, Cu 17, glass 9, borosilicate 3,3) and γ (water 0,21, ethanol 1,1, petrol 0,95, air 3,4 ·10⁻³) are correct 20 °C values; γ ≈ 3α derivation and the "about 100 K" validity limit are right.
- pred-1/pred-2 numbers (6,00 / 12,0 mm, 0,0600 %), pred-3 physics and kertaus options correct.
- interpret table and "air ≈ 100 × steel γ" (94) correct.
- Etsi virhe: 28 mm, 1,8 mm, 0,7 %, ×15 correct; siirto 44 mm, mistakes 0,044 and 110, glass-corrected 43 mm, factor 40 correct.
- check-2: α = 23·10⁻⁶ 1/K, mistakes 46 and 15,3 match their stated errors. Exit ticket 21 mm correct.
- L1-04 remark that water's real growth is "slightly larger" holds (density data give ≈ 0,90 l); L2-03 two-neighbour gap argument and L3-02 bending direction correct.
- sim.js: ΔT from 20 °C, ΔL = αL₀ΔT, ×100 exaggeration stated on canvas, amplitude ∝ √T (K), max real change 0,23 % < 0,3 % as howto says; simState gives dT, dL, rel, model box says the spacing is set from the formula.
- Experiments: exp-1 locks material and L₀, varies T from 20 °C; exp-2 locks material and T = 70 °C, varies L₀ — each isolates its parameter. Hash identical at start and end.
