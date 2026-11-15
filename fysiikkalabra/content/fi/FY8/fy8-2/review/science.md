VERDICT: PASS
CONTENT-HASH: 759101bad721fe20

## Blocking

## Polish
- inquiry.json `siirto` (hint 3, the 2,34 mistake, the solution) — the prompt asks for the energy left "sisäenergiaksi", but hint 3 ("Lämmöksi jää"), the 2,34 mistake feedback ("Kysytty lämpö") and the solution ("lämmön summa") call the same quantity heat; the Tiivistelmä and the exit ticket say sisäenergia — use sisäenergia throughout (guardrail: a body has internal energy, heat is energy in transfer).
- lesson.md Kaava (level table) with inquiry.json `ennuste-1` — the table's rounded level $-0{,}38\,\text{eV}$ gives $3{,}02\,\text{eV}$ and 411 nm for 6 → 2, while the text and the sim (unrounded $-13{,}6/n^2$) say 410 nm — say in the sim's `calc` that the model uses unrounded level energies, so the last digit can differ from a hand calculation with the table.
- lesson-answers.py `ex-J` — the comment says 3,1037e-19 J; the value is 3,1039e-19 J (as the worked example has it) — correct the comment.

## Checked
- One script recomputed every number of lesson.md, inquiry.json, the exit ticket and lesson-answers.py from h, c and 1 eV as given: Balmer 656/486/434/410 nm, gaps 170/52/24 nm, Lyman 122/103/97/95/94 nm and 10,2 eV, 7 → 2 at 397 nm, visible 1,65–3,26 eV, example 1,9375 eV, Etsi virhe 1,05e-25 and 656 nm, siirto 0,722 eV (mistakes 9,92; 3,06; 2,34), check 2 2,27 eV (3,64; 0,44), CO2 0,083 eV. All agree.
- Formula section: hf = E_y − E_a and λ = hc/(E_y − E_a), symbols and the eV → J conversion stated; hydrogen levels given as data (scope note); no later-course physics.
- Worked example: symbolic first, conversions shown, three figures justified by 640 nm, a real reasonableness check.
- Figures to scale as claimed: spectra (1 px/nm, lines at 410/434/486/656), levels (22 px/eV, six levels), fluorescence arrows (3,40 and 2,38 eV), lamp spectrum (405/436/546/577/579 nm).
- Predictions: exactly one correct option each; every distractor wrong and its feedback right.
- Experiments: tila and n_a locked, n_y varied; simState gives dE and lam there; sim.js uses the lesson's constants and E_n; its limits (one atom, no line brightness, n_a > 1 means hot gas) are stated.
- Interpret task: NIST lines of H, He, Na, Hg correct; mercury the only full match.
- Absorption by re-emission in random directions: fair simplification (C). Linewidth and weak-transition caveats, Sun's dark H line from n = 2, helium 1868, fluorescence, greenhouse box: correct.
