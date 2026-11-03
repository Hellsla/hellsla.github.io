VERDICT: PASS
CONTENT-HASH: d331af7cdb24643e

## Blocking

## Polish
- inquiry.json:385 — the siirto check says the listener hears the sound "huojuvan" between 1930 and 2080 Hz; this chapter defines huojunta as the loudness beat of two tones, so write "vaihtelevan" (the numbers and the twice-per-second rate are right).
- assets/sims/fy5/fy5-14/sim.js:36 — `heard()` uses wavefronts 0 and 1, so the constant f_A is fixed by the code rather than counted from the latest arrivals; physically correct for collinear motion (later fronts give the same value).

## Checked
- Round-1 blocker fixed: ennuste-1 now puts the listener on the road's line like A; the right-choice feedback adds the roadside glide with the right cause (radial component falls); the reflection contrasts it with the hook.
- Doppler signs and conditions (still air, collinear, one moves, v_s < v) are stated in lesson.md, the sim model box and the feedback.
- simState at f0 400 Hz and the required rows u = 0, 34, 102 m/s: source moving f_A 400/444.4/571.4 Hz, λ_A 0.850/0.765/0.595 m; listeners moving f_A 400/440/520 Hz, λ 0.850 m. These match the predictions, feedback and conclusion; slider step 2 reaches every row.
- Sim change (label backing) touches no physics; the arrival, glow and spacing geometry are unchanged.
- Doppler figure after clipping: shift 0.4·r, λ_A = 0.6λ, λ_B = 1.4λ; the brackets are unchanged.
- Worked example now says about 9 % on each side (30/311, 25/311); radar removed.
- Spectrum task: the sung vowel with a strong second harmonic is plausible and labelled invented; peaks 200–1000 Hz, answer 200 Hz.
- FFT fallback data 440 Hz fork vs 440/880/1320/1760 Hz sung tone, labelled invented; 10 Hz resolution claim right.
- Beats task 4.0 Hz (new definition sentence right); siirto 2077 Hz, mistakes 1929/2012/2000 Hz outside the 1 % tolerance; tarkistus-2 342.9 m/s.
- Exit ticket, retrieval and Etsi virhe items unchanged and correct.
