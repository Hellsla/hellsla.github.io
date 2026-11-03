VERDICT: FAIL
CONTENT-HASH: b4cca44759d1deba

## Blocking
- inquiry.json:62, :237, :240 (also lesson.md:1127) — A: the ball model is said to make the second slit "lisätä osumia (kaikkialla)". In koe-1 the total is fixed (N = 1000) and the measured quantity is the fraction n : N; with the same total a ball through one slit or the other gives the average of the two single-slit patterns, i.e. the fraction stays 4,3 % (exactly the "reitti mitataan" result, 43/1000). So the ennuste-1 "Osuus kasvaa" feedback, the johtopäätös model answer and its criterion state the wrong ball-model prediction (the "Osuus pysyy samana" option is the true ball-model prediction, and its feedback is right). lesson.md:1127 is B: "lisäisi osumia kaikkialla" holds only at a fixed source rate and time, which the text does not say (the patterns figure says "sama osumien kokonaismäärä"). — Fix: say that in the ball model the fraction would stay the same as with one slit (the sum of two single-slit patterns), but it fell to about 0,3 %; in lesson.md add "kun lähde lähettää yhtä paljon sekunnissa" or use the same-total wording.
- inquiry.json:352 (siirto, Järkevyys) — A: 290 µN ≈ the weight of a 30 mg mass; a mosquito is about 2–3 mg (≈ 25 µN), so "suunnilleen hyttysen paino" is off by about 10×. — Fix: compare with a ~30 mg object (e.g. a small fly or a grain of rice) or drop the comparison.

## Polish
- lesson.md:1035 (compton figure) — the electron's path (≈31° below the axis), its velocity arrow (≈15°) and the momentum-triangle p_e (≈25°) point in three directions; v and p_e must be parallel. Draw them in one direction (the photon's p' already matches its path, ≈20°).
- lesson.md:977 — "Kun vain toinen rako on auki, raidat katoavat": a single slit still has weak diffraction minima; "kahden raon raidat katoavat" would be exact (C, optional).

## Checked
- Scope: no de Broglie wavelength anywhere (lesson, inquiry, sim-spec "aallonpituutta ei näytetä"); Compton Δλ formula only in lesson-answers.py for the table.
- p = E/c = h/λ, units, 500 nm and 0,0711 nm values, ratio ≈ 7000.
- Worked example: 3,138e-19 J, 3,19e5 1/s, 941 m, 0,0013 photons in 1,2 m, 1 mW pointer 3e15 1/s, 10^10 dimming.
- Compton table (λ_C = 2,426 pm) all five values; distractor feedbacks correct.
- tarkistus-2: 795 eV, Δλ = 2,4 pm ≤ 2λ_C (θ ≈ 89°); mistakes 1,27e-16 J and 517 keV.
- siirto 290,5 µN, mistakes 145 µN, 9,08 µN, 2,9e-4 N.
- Sim model cos²(πx/2 mm)·sinc²(πx/10 mm); replay gives 43 and 3 of 1000 at x0 = 1,0 mm, as quoted; koe-1/koe-2 lock the right parameters; simState carries N, n, osuus.
- kertaus, virhe, tarkistus-1, ennuste-2: exactly one correct option, feedbacks right.
- Four photon models and Compton energy/momentum conservation statements.
- Exit ticket 700/450 ≈ 1,6.
