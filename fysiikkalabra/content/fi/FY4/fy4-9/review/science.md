VERDICT: FAIL
CONTENT-HASH: 1c5dd3ab4e00b829

## Blocking
- lesson.md:338 (figure `pysaytys`, figures.py:65) — **B, sign.** The figure draws the bumper's force on the cart as positive, with area "2,0 N·s". The sim draws the same force below the axis, and pred-1, exp-1 and johtopäätös give I = −2,00 N·s. — Draw F_x below the axis (0…−100), or label the axis and caption as the magnitude |F|.
- lesson.md:386, :557; inquiry.json:493, :497 (check-3 criterion 2 and model) — **B, net force.** "alustan on annettava sama impulssi" holds only for the net force. The mat's impulse is Δp + mgΔt. Example: 70 kg, 4,4 m/s, 0,3 s gives Δp ≈ 310 N·s but a mat impulse of ≈ 516 N·s. — Write "kokonaisvoiman impulssi" or "paino jätetään huomiotta". The conclusion still holds: F_alusta = mg + |Δp|/Δt.
- lesson.md:559, :566 — **B, sign.** "Muutos on 2mv" contradicts :514 (Δp = −2mv). — Write "muutoksen suuruus on 2mv".

## Polish
- lesson.md:489 vs :550 — F_ka is defined as |Δp|/Δt, yet the example's F_ka is signed ("Voima on positiivinen"). — Say that the direction comes from the sign of Δp.
- lesson.md:338 caption — the crushable bumper's abrupt drop to zero is explained only in the sim's model box. — Add "muovautuvan puskurin voima loppuu, kun kärry pysähtyy".
- model.js:5 — "perfectly plastic" is the wrong term for F = kc loading with no unloading force (a comment only).
- inquiry.json:497 — "samalta korkeudelta, joten samalla nopeudella": the mat's top is about 0,5 m high. — Write "oletetaan".
- sim-spec.md — "F = kc" vs "F = −kc": say which one is the magnitude.

## Checked
- model.js, all 72 combinations: I, Δt, F_max, v2 and I = Δp agree with analytic SHM (π/2·√(m/k), v√(mk), −mv0/−2mv0) to 3·10⁻⁶. Crush energy = ½mv0². Test passes (616).
- Graph scale ≥ 1,04·peak including the grey runs. The curve is never positive, and 0,444 s fits in 0,5 s, so nothing is cut at either width.
- Arrows: blue v, purple p and red F, drawn from the signed components. F is hidden after the crush ends.
- Crushable discontinuity explained in the model box; the spring bumper is lossless and stated so.
- All inquiry and lesson numbers recomputed (experiments, predictions, siirto and its mistakes, check-1 and check-2, example 870 N and 145 N).
- Exactly one correct option per item. The experiments isolate the varied key, and simState gives every measured key.
- Exit ticket correct.
