VERDICT: PASS
CONTENT-HASH: 5b1dbbf676a79d5e

## Blocking
- none

## Polish
- lesson.md:542 — the worked example's reasonableness check (v·T = 0.80 m = λ) only restates λ = v/f, so it checks nothing new — compare instead with a real taut-rope speed (a few m/s), or note that 6.0 m holds 7.5 wavelengths (the lesson-answers row esim-n-lambda is already there).

## Checked
- Definitions: wave as a travelling disturbance, with the mechanism (each point pulls the next one); energy but not matter in the ideal model, with Stokes drift and gas thermal motion named; transverse and longitudinal waves; wavelength (crest to crest, or the shortest distance between points in phase); glossary-consistent.
- Conditions: v depends on the medium, not on f or a small amplitude, "in an ideal rope"; dispersion of water waves and tsunami v rising with depth stated; f is kept across a boundary (tarkistus-1, theory).
- One script recomputed every inquiry and lesson number from the task data (kertaus 2.0 Hz/0.50 s; koe-1 6.0 m and 5.0 cm; koe-2 λ 4.0/2.0/1.0 m, fλ = 2.0 m/s; koe-3 λ 1.0 m; esim 2.4 m/s → 0.80 m; siirto 4.0 s, mistakes 25 and 9; tarkistus-2 2.7 m/s, mistakes 1.35, 0.833, 5.4; tark-1 1.5 → 0.75 m). All agree with lesson-answers.py.
- Figures: in graphs, λ = 1.0 m and T = 0.50 s agree with each other (v = 2.0 m/s). The snapshot's crests fall at 0.5, 2.0 and 3.5 m. In birth, the four rope shapes match y = A sin 2π(t/T − x/λ) (the t = T path is sampled at x = 200, 280, 360), the handle moves up first, and the wave travels one λ per period. In types, the dots and coils follow the travelling shape (figlib oscillate phase checked), and the compression labels sit where −ds/dx is largest.
- Sim: y = A sin 2πf(t − x/v) behind the front, zero ahead of it. The pulse is a half-period crest (length λ/2). The λ marker is placed at crests (offset λ/4) or compressions (offset λ). The spring is drawn with the strain shading, the enlarged rope displacement is stated, and there is no reflection or damping, as the Assumptions box says.
- Experiments: each one locks everything except the varied key. simState carries xFront, dyMax, dxMax, lambda, v and f, and restart() zeroes the maxima when the wave type changes. The 60 fps sampling gives 5.0 cm.
- Predictions: exactly one correct option in each. Every distractor's feedback quotes the right model values (6.0 m in 3.0 s; 2.0 m/s; 2.0 → 1.0 m).
- virhe, tarkistus-1 and tarkistus-3 (sound is longitudinal; molecules oscillate and are not carried along): exactly one right option each, feedback correct.
- The explain model answer, criteria, summary, exit ticket (λ/3) and misconception section all agree with the theory and the sim values, and call the numbers model values.
- Scope: within FY5 "aaltojen synty ja eteneminen"; reflection is only pointed forward to its chapter.
