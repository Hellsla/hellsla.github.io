VERDICT: PASS
CONTENT-HASH: dd6218aea5581d8e

## Blocking

## Polish
- lesson.md:1127 (Yleinen virhekäsitys) — the parenthesis "(jos lähde lähettää yhtä monta kvanttia sekunnissa yhtä kauan)" is attached to a claim about the fraction at equal total hits, where it is not needed; the physics is right (ball model: fraction unchanged, since the two single-slit patterns coincide in the lesson's model) — consider dropping the parenthesis or moving it next to "lisäisi osumia".

## Checked
- Round-2 finding fixed: Esimerkki Tulos now says "vain noin tuhannesosa (0,13 %)", agreeing with Järkevyys 0,0013.
- ennuste-1 prompt (changed): no longer states the wave-model answer; asks for n : N at equal total hits; exactly one correct option, both distractor feedbacks right and consistent with Virhekäsitys, johtopäätös and the patterns figure.
- Recomputed in one script with CODATA constants: worked example 3,138e-19 J, 3,19e5 1/s, 941 m, 0,0013; 1 mW pointer 3,2e15 1/s, dimming 10^10; p(500 nm) 1,33e-27, X-ray 9,32e-24, ratio 7030; exit ticket 1,56; all agree with lesson-answers.py.
- Compton table (λ_C = 2,426 pm): 0,0711 / 0,0718 / 0,0735 / 0,0752 / 0,0760 nm; interpret option and distractor feedbacks correct.
- tarkistus-2: 794,8 eV (Δλ 2,4 pm, θ ≈ 89°, physically possible); 4 % check fair (1 − 1/1,04 = 3,8 %); mistakes 1,27e-16 J and 5,17e5 eV right; two sig figs from Δλ justified.
- siirto: F = 2IA/c = 290,5 µN; mistakes 145, 9,08, 2,9e-4 right; 29,6 mg weight check right.
- Simulation: cos²(πx/2 mm)·sinc²(πx/10 mm) vs sinc² for one slit or measured path; dark fringe at ±1 mm; seed replay gives 43/1000 and 3/1000 as quoted; koe-1/koe-2 lock the right parameters and every change resets the screen; simState gives N, n, osuus; model box states its simplifications.
- Physics text: four photon models, zero rest mass, p = E/c = h/λ, Compton energy and vector momentum conservation, N/t = P/hf, dualism wording consistent across theory, glossary, summary, checks and exit ticket.
- Scope: no de Broglie wavelength anywhere (λ = h/p used for photons only); nothing beyond FY8 content.
- Hash unchanged start to end.
