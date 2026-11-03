VERDICT: FAIL
CONTENT-HASH: 67ba387cc1473fac

## Blocking
- lesson.md:1120 (Esimerkki, Tulos) — A: "Laitteen pituus 1,2 m on alle tuhannesosa fotonien välistä" is false: 1,2 m : 940,8 m = 0,0013, more than one thousandth, and the Järkevyys line two steps later says 0,0013. — Fix: "on vain noin tuhannesosa (0,13 %) fotonien välistä" or "alle sadasosa".

## Polish
- inquiry.json ennuste-1 prompt — it already says the path difference is half a wavelength, "joten aaltomallin mukaan kohta on tumma raita"; this hands over the wave-model answer before the prediction (pedagogy's call, not a physics error).

## Checked
- Round-1 findings fixed: ennuste-1 "Osuus kasvaa" feedback, johtopäätös model answer and criterion now give the right ball-model prediction (same fraction, sum of single-slit patterns); lesson.md:1127 states the fixed source rate; siirto Järkevyys now 29,6 mg ≈ a grain of rice; lesson.md:977 says "kahden raon raidat katoavat".
- Compton figure: electron path, v arrow and p_e all at 24,8°, photon path and p' at ≈20°; the momentum triangle closes (p = p' + p_e).
- Patterns figure (figures.py): curves normalised to equal area, as the "sama osumien kokonaismäärä" label says.
- Scope: no de Broglie wavelength anywhere (lesson, inquiry, sim-spec, exercises).
- Recomputed with CODATA constants in one script: worked example 3,138e-19 J, 3,19e5 1/s, 941 m, 0,0013, 1 mW pointer 3,2e15 1/s, 10^10 dimming; p(500 nm) 1,3e-27, ratio 7030; exit ticket 1,56.
- Compton table (λ_C = 2,426 pm) 0,0711 … 0,0760 nm; distractor feedbacks correct.
- tarkistus-2 794,8 eV, Δλ = 2,4 pm ≤ 2λ_C (θ ≈ 89°); mistakes 1,27e-16 J and 5,17e5 eV right.
- siirto 290,5 µN, mistakes 145, 9,08 µN, 2,9e-4 N.
- Sim model cos²(πx/2 mm)·sinc²(πx/10 mm), particle choice does not change the distribution, path measurement uses the single-slit weight; replay gives 43 and 3 of 1000 at x0 = 1,0 mm, as quoted in ennuste-1, ennuste-2 and johtopäätös; koe-1/koe-2 lock the right parameters, simState carries N, n, osuus.
- kertaus, ennuste-1, ennuste-2, compton-data, virhe, tarkistus-1: exactly one correct option, feedback physics right; four photon models and Compton energy/momentum statements consistent across theory, summary, glossary and tarkistus-3.
