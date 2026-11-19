VERDICT: FAIL
CONTENT-HASH: e00d5048884bf778

## Blocking
- lesson.md:486 — A (internal consistency): "tämän luvun tehtävissä ajanotto alkaa aina niin" (C = 0) is contradicted by the chapter's own task inquiry.json:335 `vaihe`, where timing starts at release from the extreme and C ≈ π/2. A student who reads the theory and then meets that task is told two different things. — Narrow the claim, e.g. "tämän luvun laskutehtävissä ajanotto alkaa niin" or "… alkaa niin, ellei toisin kerrota", or drop the sentence's second half.

## Polish
- lesson.md Esimerkki "Kaava ratkaistuna" — The house rule asks for full simplification before substituting. Here T = t_n/n and x = A sin(2πt/T) stay as two rows. It could end in x = A sin(2πnt/t_n), with T still computed for the reasonableness check. This is a pedagogy choice, not a physics error.
- inquiry.json tarkistus-2 solution, Järkevyys — The "noin 0,8 m:n heiluri" check uses the pendulum formula from a later chapter (L = g(T/2π)² = 0,805 m, which is correct). It could be marked as a preview ("myöhemmin kurssilla") or replaced with a check that uses only this chapter's tools.

## Checked
- I recomputed every number in one script with my own formulas, sim data included (the Park–Miller noise reproduced). Koe 1: d = 1,85 / 0,13 / 3,70 cm for A = 3 / 6 / 12 cm. Koe 2: N = 6 and 3, f = 1,25 and 0,625 Hz. Koe 3: the best fit on the slider grid is A = 8,5 cm, T = 2,20 s, d = 0,127 cm, f = 0,455 Hz. All match the predictions, the conclusion and the numeric answer.
- Esimerkki: T = 0,60 s, argument 2,618 rad, x = 2,0 cm. In degree mode sin = 0,046, giving 0,18 cm. Siirto: 3,80 cm. The degree-mode value is 0,0877, and using f as T gives −3,80 cm. Tarkistus 2: 0,556 Hz (mistakes 1,11 and 0,185). Tarkistus 3: T = 0,800 s, f = 1,25 Hz, range 0,378–0,482 m. Etsi virhe: 1,1 Hz. Kertaus, exit ticket and swing check: 2,0 Hz, A = 0,80 m. All correct.
- Definitions (jaksollinen, värähtely, tasapainoasema, poikkeama, amplitudi, jaksonaika, taajuus, vaihe) agree with the glossary and with the circular-motion chapter.
- The sinusoidal model's conditions are stated: no damping, timing from the upward equilibrium crossing, small swings for the pendulum, radians.
- Figures: fig 3 (T = 0,8 s, A = 4 cm, to scale), fig 4 (the phasor point at 150° matches x = A/2 between T/4 and T/2), fig 5 (3T = 3,6 s, A ≈ 3 cm) and the check figure (crossings at 0, 1,8, 3,6 and 5,4 s) agree with their texts.
- The simulation implements the lesson's model. d is the mean |residual| and N = ⌊5/T⌋, as the calc box says. Its limits (simulated data, noise ±0,25 cm, d never zero) are stated in the model box.
- Experiments: each locks the right controls (koe-3 leaves A and T free on purpose), and simState carries d, N, f and A at the initial values.
- Every choice item has exactly one correct option, and every distractor's feedback states the right physics. The vaihe item's physics (C = π/2 means an extreme at t = 0) is correct.
- The phase and sign reasoning in the tarkistus-3 model answer (C ≈ 0 means the distance is increasing) is correct.
- Scope: all within FY5 "jaksollinen liike, jaksonaika, taajuus ja amplitudi". No ω or rad/s symbols are introduced.
