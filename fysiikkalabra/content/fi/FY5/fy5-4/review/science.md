VERDICT: FAIL
CONTENT-HASH: c64883a8ea9fcc46

## Blocking
- inquiry.json:141, 87, 91, 95, 279 (also lessons/FY5/fy5-4/sim-spec.md) — **A**. The sim does not show what the feedback and model answer say it shows. In sim.js `advance()`, a sliding car turns on a radius of v²/(μ0 g). At the test point exp-1 names (20 m/s, r = 50 m, dry asphalt), that radius is 51.0 m. I ported `advance()` to Python with the desktop geometry: the car never leaves the track. It circles at most 52.0 m from the centre, inside the 7.3 m half-width of the drawn asphalt, and its heading keeps turning. The readout says "auto liukuu radalta". Even at 25 or 30 m/s on dry asphalt the heading turns 56° or 31° before the car leaves the track. "Jatkaa lähes radan tangentin suuntaan" holds only far above the limit (on ice at 20 m/s, 7°). So the student who presses Käynnistä at 20 m/s, as told, sees the opposite of the pred-2 feedback and the johtopäätös model answer. — Fix: in exp-1:141, test the slide at 30 m/s (or on märkä asfaltti or jää). Replace "jatkaa lähes (radan) tangentin suuntaan" with "kaartaa loivemmin kuin rata ja ajautuu ulkoreunan yli; mitä suurempi nopeus, sitä suoremmin". Make the same change in sim-spec.md and in the sim.js header comment.

## Polish
- lesson.md:280 — "Jos v²/r kasvaa yhtä suureksi kuin g … auto irtoaa": when v²/r = g, N = 0 and the car is exactly at the limit. It leaves the road only when v²/r > g. Write "yhtä suureksi kuin g, tukivoima on nolla; jos suuremmaksi, auto irtoaa" (the guardrails' ≥/> boundary rule).
- lesson.md:139 — "Tasaisessa kaarteessa ajavaan autoon ainoa vaakasuora voima on tien kitka": this holds only on a level road with air resistance neglected. Add "vaakasuoralla tiellä, kun ilmanvastusta ei oteta huomioon" (the example states the condition, the theory does not).
- lesson.md:96 (figure muutos) — the caption says the arrows are to scale with each other. The v arrows are about 68 px long on the left and about 98 px on the right. Either drop the claim or give both panels one length.
- exercises/solutions.md:29 (L1-03) — see the exercise report.

## Checked
- I recomputed in one script: the worked example (6000 N, μ0 ≥ 0.510, a_n = 5.0 m/s²), the kuvaaja points (2, 8, 4, 18, 9 m/s²; the SVG coordinates are to scale), exp-1 (750, 3000, 6750, 12 000 N; F_max = 11 772 N; v_max = 19.81; mistakes 22.15 and 392.4), exp-2 (ratio 0.920 at every mass), siirto (15.34; mistakes 18.79 and 10.85), check-2 (148.0; mistakes 47.12 and 294.3) and check-3 (T = 0.765 N, G = 1.67 N). All match.
- muutos: v1 and v2 are tangent for counter-clockwise motion, and Δv and a_n point to the centre. kaarre: the road arc is centred on the drawn centre point, N = G, and friction points inward.
- nyppylä figure: N = 0.6 G on the bump and 1.4 G in the dip, the same a_n in both. virhe: N < G, N + F_kp = G. In valitse, only a has N > G with nothing extra. No figure gives the answer away with an acceleration arrow.
- Every prediction has exactly one correct option, and the distractor feedback is sound (apart from the tangent claim above).
- exp-1 and exp-2 lock r, m, surface and v correctly. simState gives an, Ftarve, Fmax and pito. The initial values are inside the slider ranges and steps.
- Sim: N = mg, F = min(mv²/r, μ0mg), and a = F/m is drawn toward the centre of the turn. The model box states its limits.
- Exit ticket and summary: no centrifugal force, a ninefold a_n at three times the speed, N = m(g − v²/r).
- Scope: no ω or rad/s, and v = 2πr/T is used.
