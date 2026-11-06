VERDICT: PASS
CONTENT-HASH: 37891267a0068020

## Blocking

## Polish
- fy5-12/exercises/solutions.md:200 — The check "matkaerot olisivat … 1,5 cm, 4,5 cm ja 7,5 cm" reads as a complete list. Write "1,5 cm, 4,5 cm, 7,5 cm ja niin edelleen", or "6,0 cm on 4,5 cm:n ja 7,5 cm:n puolivälissä".

## Checked
- New task L2-08 (type 4, find the error; exercises.json:284). λ = 0,36 / 12 = 0,030 m = 3,0 cm, Δs = 6,0 cm, and Δs/λ = 2,0, so the interference is constructive. Only line 4 is wrong, and "Laskussa ei ole virhettä" is last.
- The wrong line is exactly the lesson's warned mistake: Δs = nλ taken as destructive because the wave "travelled further". Each correct line's feedback names its own check.
- The correct choice's feedback gives a counter-example (2,5λ) and does not just repeat the solution. The option texts have similar lengths.
- The sources are in phase at the same frequency, as stated in the task. The ripple-tank values (12 Hz, 0,36 m/s) are realistic.
- Notation follows the lesson: Δs = |s₁ − s₂|, nλ and (n + ½)λ.
- The inline fractions in the task lines and the solution are single short fractions. From the text they fit 300 px. I did not render them.
- answers.py ran once. All numeric answers agree with exercises.json within tolerance.
- The hash was the same at the start and at the end.
