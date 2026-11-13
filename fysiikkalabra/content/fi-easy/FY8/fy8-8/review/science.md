VERDICT: PASS
CONTENT-HASH: c347cb60476725a3

## Blocking

## Polish
- inquiry.json `gammaspektri` text — "Kuvassa on gammailmaisimella mitatun spektrin muoto" while `source_note` says the peaks are drawn schematically (and the figure shows no sum peak or backscatter) — write "kaavamaisesti piirretty mitatun spektrin muoto" so the two agree.
- inquiry.json `siirto` solution, Järkevyys — "Sarjassa on siis oltava 4 beeta miinus -hajoamista, ja kumpikin kasvattaa" — "kumpikin" refers to two; use "jokainen".
- inquiry.json `siirto` solution, last sentence — "Uraani-238:n sarjassa on samoin 8 alfahajoamista ja 6 beetahajoamista" — "samoin" suggests the same counts; write "vastaavasti" or "Vertaa: …".
- inquiry.json `simulaatio` model — "pitkäikäiseen viritystilaansa" (Pa-234m, $T_{1/2} \approx 1{,}2\,\text{min}$) could add "(puoliintumisaika noin minuutti)" so "pitkäikäinen" is read relative to nuclear excited states (C as it stands).

## Checked
- Recomputed in one script: example λ = 1,8740 pm (E = 1,0600·10⁻¹³ J, hc = 1,9865·10⁻²⁵ J m), 500 nm ratio 2,67·10⁵; tarkistus-2 8,8256 pm, keV-as-eV mistake 8826 pm, ratio 4,71 both ways; kertaus 1,89 eV; Co-60 sum 2505,7 keV, mistake 159,3; siirto 7 α and 4 β⁻; exit ticket Pb-206, N = 8. lesson-answers.py agrees.
- Co-60 data vs ENSDF (levels 2505,753 / 1332,514 keV, γ 1173,228 / 1332,492 keV); gap 0,033 keV matches my recoil estimate ≈ 0,03 keV; "rounding mostly" is right.
- Levels figure is to scale as stated (0,1081 px/keV for both levels; Co-60 line at Q ≈ 2822 keV).
- Shifts figure: α (−2,−2), β⁻ (N−1, Z+1), β⁺ (N+1, Z−1) land on the right cells; nuclide-chart belt reaches Pb-208/Bi-209, β⁻ below and β⁺ above the belt correct.
- Sim CHAIN = NNDC main branch of the U-238 series (8 α, 6 β⁻, Pa-234m, Bi-214 β⁻), stable cells Tl-203/205, Pb-204/206/207/208, Bi-209 correct; simState gives Z, N, A, mode for koe-1; only k varies; limits (schematic nucleus, no timing, minor branches) stated.
- Decay equations, charge/mass-number conservation, electron capture (Be-7 → Li-7, possible below the positron threshold), β continuous spectrum vs discrete α and γ: correct mechanisms (neutron → proton, weak interaction; electron not pre-existing).
- Predictions 1–2, kertaus, virhe, tarkistus-1: exactly one correct option each, every distractor's feedback right.
- Explain model answers (johtopaatos, tarkistus-3) and criteria agree with the theory and summary.
- Worked example solved symbolically first, 4 s.f. justified, check is real; hook physics (Am-241 activity, ion current drop with smoke) sound.
- Scope: nuclear structure and decays within FY8 "atomiytimen rakenne ja muutokset"; no decay law or binding energy pulled in.
