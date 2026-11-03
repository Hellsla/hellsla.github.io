VERDICT: DONE

Drafted fy7-9 from scratch; `check_lesson.py fy7-9` all ok, `check_solutions.py` ok.

- `lesson.md`: Ydinajatus (EM wave from mutually inducing fields, E ⊥ B ⊥ travel, $c = f\lambda$, accelerating charge and antenna, spectrum figure + table of sources and effects, ionising part, thermal radiation, black body), `## Kaava: Wienin siirtymälaki` (absolute T, 300 K / skin / 800 K / Sun examples, Stefan–Boltzmann only qualitatively, one pointer to the FY8 course), staged example (Sun 502 nm → 5,77 · 10³ K, checked against IAU 2015 5772 K), misconceptions, summary. No photon or Planck quantisation.
- `lessons/FY7/fy7-9/figures.py`: hero (forge, rod glowing white→red), wave, antenna, spectrum, curves (Planck, 4000/5000/6000 K with a legend because the curves crowd at their ends), task figure spectrum-task. The spectral colours are outside the palette (two lint warnings, on purpose).
- `inquiry.json`, `exit-ticket.json`: two predictions tested by two experiments, a conclusion, an error-spotting task (°C in Wien), a transfer task (bulb filament), three checks.
- New sim `assets/sims/fy7/fy7-9/`: Planck curve, λ_max from the curve's highest point, visible share, glow colour (CIE), with 27 assertions in `tests/sims/fy7-9.json`; texts in `lang/fi.json` `sims.fy7-9`.
- Exercise set 5/4/3, `answers.py`, `lesson-answers.py`, `solutions.md`; 4 glossary terms.
