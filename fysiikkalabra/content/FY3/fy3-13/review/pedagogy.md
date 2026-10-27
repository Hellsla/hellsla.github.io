VERDICT: PASS
CONTENT-HASH: 82b128401cc8a8cf
## Blocking

## Polish
- Worked example, stage 7 (Järkevyys) gives the interval as -294...-258 °C, but stage 5-6 give the contour zeros as -258,66 and -294,81 (-259 and -295 when rounded). A student comparing the stages sees two different pairs; use one rounding.
- Worked example, stage 1: the best-fit line's own equation is never given, so the readings (0 °C; 101,3 kPa) and (100 °C; 138,0 kPa) can only be taken from the figure. Add "(luettu kuvan suoralta)" with the line's p0 and k, or say they are given, so a student can reproduce 0,367 and 276,02.
- Worked example, stage 3: the formula block breaks "Δθ0 / = ..." over two lines; put Δθ0 and its fraction on one line.
- Stage 6 rounding argument is dense ("tunnetaan kolmella numerolla ja niiden erotus vain kahdella"); one sentence on why a difference loses figures would help a weak student. The same sentence style recurs in L2-02, L3-01.
- Sovella solution (A, B points): "lopuksi vähennys 20,0 - 296 antaa tuloksen kokonaisina asteina" is cryptic; say the result is rounded to whole degrees because the subtraction 20,0 - 296 is limited by the 296 (whole degrees).
- L3-01: Vastaus says "20 (tarkasti 20,3)" while the checked answer is 20,3; state which the check expects.

## Checked
- Hash at start and end 1fd418b2cad4dd9b. Read the lesson text, all 12 exercises and solutions, the example captures (390 px, 3 parts), the Tehtävät capture and, in Playwright at 390 px, a rendered Näytä ratkaisu (Sovella A/B task): closed until pressed, seven labelled parts, readable, LaTeX fits the width, no horizontal overflow.
- Every solution has Annettu, Kysytty, Periaate (with a why), Kaava solved in symbols first, Muunnokset (or why none), Sijoitus with intermediate steps, Vastaus with the figures justified, Järkevyys with a real check. A student who cannot start can follow: L1 are short and explicit; L2-03 (ylipaine) and L3-02 (kelvin, condensation) justify the one non-obvious step; L3-03 explains the n criterion and causes.
- Worked example has seven staged steps with bold lead-ins, one step each; numbers are consistent apart from the Polish items.
- Exercise levels 5/4/3, none repeats the example.

## Round 2 (delta)
- Only inquiry.json feedback line changed: theta0 = 40 C - 116 kPa/(0,367 kPa/C) now uses \dfrac. Content unchanged and still correct (40 - 316,1 = -276 C); the stacked fraction wraps instead of overflowing at 360 px. No new findings. VERDICT stays PASS, 0 Blocking.
