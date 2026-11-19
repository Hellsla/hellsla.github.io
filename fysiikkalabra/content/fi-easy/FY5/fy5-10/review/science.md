VERDICT: PASS
CONTENT-HASH: ff3d3e83e6353700

## Blocking

## Polish
- lesson.md:355 (figure `birth`, aria-label): "Rintaman takana naru on levossa." The rope is at rest *ahead of* the front; "takana" reads as the part already reached. Fix: "Rintaman edellä naru on levossa." This is sim-spec's wording.
- inquiry.json:467 (tarkistus-3, the "pysyy täysin paikallaan" feedback): "Ne eivät vain kulje aallon mukana" can be read as "they do not *only* travel with the wave". Fix: "Ne eivät kuitenkaan kulje aallon mukana."
- inquiry.json:215 (koe-2): λ and v are read from `simState`, where λ = v/f is coded. So the table's fλ = v check only repeats the program's arithmetic. The intro's ruler check is the real evidence. Consider asking for a ruler-read λ as well (pedagogy's call).

## Checked
- I recomputed every number in one script (scratchpad rc.py) against lesson-answers.py, and all agree: the worked example (v = 2,4 m/s, λ = 0,80 m, check v·T = 0,80 m), siirto 4,0 s and its mistakes 25 and 9, tarkistus-2 2,7 m/s and its mistakes 1,35, 0,833 and 5,4, the tarkistus-1 feedback (1,5 m → 0,75 m), kertaus 2,0 Hz, and the koe 1–3 and ennuste numbers. P's largest displacement sampled at 60 frames per second is 5,0 cm.
- The worked example and the siirto and tarkistus-2 solutions are solved symbolically first. The significant figures are justified and the units are right.
- Figures. Snapshot `valokuva`: crests at 0,5, 2,0 and 3,5 m, A = 4 cm, matching the task. `graphs`: λ = 1,0 m and T = 0,50 s at the axis scales, A = 4 cm. `birth`: the front is at λ/4, λ/2, 3λ/4 and λ, and the source phase and the marked point's direction agree with y = A sin(2πf(t − x/v)). `types`: compressions and rarefactions sit where the coil spacing is smallest and largest, with λ the same in both rows.
- sim.js implements the stated model: each point repeats the source's motion after a delay x/v, the medium is at rest ahead of the front, and the pulse is half a period long. Crests are at vt − λ/4 and compressions at vt − kλ, which follows from −ds/dx. The rope's displacement is drawn enlarged and the spring's to scale, both stated in the model box. No reflection and no damping, also stated.
- The experiments isolate their variable: koe-1 varies the wave type (a restart resets dyMax and dxMax), koe-2 the frequency and koe-3 the tension. Every measured key exists in `simState`.
- Exactly one prediction option is correct in ennuste-1 and -2, kertaus, virhe and tarkistus-1 and -3. Each distractor's feedback names the actual error.
- The physics is right. The ideal model is said to carry energy but not matter, with Stokes drift and gas thermal motion mentioned. Speed depends on the medium and frequency on the source, with conditions given: an ideal rope, dispersion and tsunami as counter-examples, small amplitude. The frequency stays the same across a boundary. Sound is 343 m/s at 20 °C and about 1500 m/s in water.
- Scope fits the slot (transverse and longitudinal waves, v = fλ). Light is not mentioned.
- The johtopäätös model answer, the summary and the exit ticket agree with the theory.
