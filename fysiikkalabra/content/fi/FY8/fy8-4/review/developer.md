VERDICT: DONE

Drafted from scratch; every line of check_lesson.py fy8-4 says ok.

- `lesson.md`: Ydinajatus covers the single-quantum double slit, the probability reading of the wave, which-path measurement, wave–particle duality and four photon models. `## Kaava: Fotonin liikemäärä` has p = E/c = h/λ, the Compton effect (hf = hf' + E_k, momentum vectors) and photon flow N/t = P/(hf). The worked example uses weak 633 nm light and has 7 stages. No de Broglie wavelength.
- `figures.py`: a hero picture (weak-light double-slit lab) and three figures: hits building up, one slit vs two slits vs measured path, and the Compton collision with its momentum triangle.
- `inquiry.json`: retrieval on chapter 1, two predictions, the simulation, koe-1 (one or two slits) and koe-2 (electrons, path measured), a conclusion, a Compton data table with competing models, an error-spotting task, a transfer task (solar sail), checks and the exit ticket.
- New simulation `assets/sims/fy8/fy8-4/` (seeded hits, 600×600 layout on narrow screens), texts in `lang/fi.json` `sims.fy8-4`, 22 assertions in `tests/sims/fy8-4.json`.
- Exercises 5/4/3 with complete solutions. `answers.py` computes the exercise answers; `lesson-answers.py` computes the lesson's numbers and replays the simulation's model.
- `glossary.json`: aalto-hiukkasdualismi, Comptonin ilmiö, kaksoisrakokoe.
