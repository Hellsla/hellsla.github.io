VERDICT: FAIL
CONTENT-HASH: ad2b40581b17ae1a

## Blocking
- lesson.md:5 (figures.py `hero()`, line 212 ff.) — **A**. The prism has its apex up, but the fan leaves the prism bending *up* toward the apex, with violet at the top and red at the bottom of the fan and the screen. A prism bends light toward its base, and violet is bent most, so with the apex up violet must be lowest. As drawn it shows the opposite dispersion. — Fix: turn the prism apex-down (then the current upward fan with violet on top is right), or keep the apex up, aim the fan downward from the incoming beam and reverse the gradient (red on top, violet at the bottom) on both the fan and the screen.
- inquiry.json:105 (ennuste-2, option "Kaikkialla spektrissä…", feedback) — **A**. "Absorptio ei riipu siitä, kuinka kylmä kaasu on" contradicts the lesson (lesson.md:126, the sibling feedback at :97, the spectra caption): which lines are absorbed depends on temperature, because it decides which levels hold atoms. That is why hot stellar gas shows 656 nm dark. — Fix: "Kylmyys ei lisää absorptiota: kaasu absorboi vain niiden tilojen erotuksia, joissa sen atomeja on, ja kylmässä vedyssä ne ovat perustilassa."
- assets/sims/fy8/fy8-2/sim.js:138, lang/fi.json:1601, the mode option "absorptio (kylmä kaasu)", inquiry.json:114 howto — **A** (the sim misleads). In absorption mode with n_a = 2–4 the sim labels the cell "kylmä vetykaasu" and draws it absorbing 656/486 nm. The reflection item then asks why cold hydrogen does *not* absorb visible light. The model box admits this, but the picture shows the wrong thing. — Fix: when n_a > 1, label the cell "kuuma vetykaasu" (or drop "kylmä" from the mode name and the label), and say in the howto that n_a = 1 is cold gas.
- lesson.md:279 — **A**. "Hiilidioksidin ja vesihöyryn värähtelytilojen erotukset ovat noin 0,1 eV tai pienempiä" is wrong: CO₂ at 4,3 µm is 0,29 eV and H₂O at 6,3 µm is 0,20 eV (and 0,46 eV at 2,7 µm). — Fix: "noin 0,1–0,5 eV".

## Polish
- inquiry.json:228 — "spektrissä ei ole muita viivoja" as an identification rule fails for a lamp that holds a mixture. Write "eikä spektrissä ole viivoja, joita lampun alkuaineella ei ole" or limit the rule to one element.
- inquiry.json koe-1 — n_y = 2 can be chosen with n_a = 2 locked, which records dE = 0, lam = 0 in the table. Consider offering only n_y > n_a.
- lesson.md:187 ("Näkyvän valon viivat … tasolta 3–6") — 7→2 (397 nm) lies inside the lesson's own visible range of 380–750 nm. "voimakkaimmat näkyvät viivat" would be exact.

## Checked
- Recomputed in one script: Balmer 656,5/486,3/434,2/410,3 nm, gaps 170/52/24 nm, Lyman 122–94 nm, retrieval 1,91/3,02 eV, example 1,9375 eV, Etsi virhe 1,05·10⁻²⁵ m and 656 nm, siirto 1,0126 eV (mistake 8,00 eV), check 2 2,105 eV (3,37 and 0,475 mistakes): all agree.
- Spectra figure to scale (1 px/nm, lines at 410/434/486/656). Levels figure to scale (22 px/eV). Fluorescence figure to scale (55,9 px/eV for both photons).
- Lamp figure and table: Hg 405/436/546/577/579, He, Na, H against NIST. The correct option is unique.
- Predictions 1–2: exactly one correct option each. Experiments lock tila and n_a, vary n_y, and simState gives dE and lam.
- sim.js: E_n, λ = hc/ΔE with the lesson's constants, region limits, IR arrow. Line colours intended.
- Fluorescence mechanism, the absorption re-emission explanation, the misconception box, helium 1868, exit ticket.
