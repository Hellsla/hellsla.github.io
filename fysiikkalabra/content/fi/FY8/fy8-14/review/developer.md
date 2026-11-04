VERDICT: DONE

Drafted the chapter Säteily lääketieteessä ja teknologiassa.

- `lesson.md`: Ydinajatus (the X-ray tube, X-ray images and CT, a table of typical doses, tracers with Tc-99m and SPECT, PET with 511 keV annihilation photons and coincidence detection, radiotherapy from several directions, technology uses, and justification, optimisation and dose limits). Kaava covers attenuation through layers and $E_\gamma = m_e c^2$. The worked example on X-ray contrast has seven stages. There are two misconceptions and a summary. The text has 6 figures, including the hero.
- `figures.py`: hero, rontgen, pet, sadehoito, mittari, kontrasti (graph to scale).
- `lesson-answers.py`, `answers.py`: every number. NIST XCOM μ/ρ, ICRP 128 and STUK values come from my own knowledge, because the network was closed. The PET model is repeated in Python and matches sim.js (checked with node).
- New sim `assets/sims/fy8/fy8-14/sim.js`: PET coincidence localisation with back-projection, a seeded generator and an adapter (N, kohde, ilmaisu). Its texts are in `lang/fi.json` under `sims.fy8-14`. `tests/sims/fy8-14.json` has 20 assertions. `meta.json` now has `"sim": true`.
- `inquiry.json`: 3 predictions; koe-1 (how many coincidences are needed); an interpret table on X-ray energy and contrast; the transfer task (FDG transport); 3 checks; the exit ticket.
- Exercises 5/4/3 with complete solutions.
- `glossary.json`: röntgensäteily, merkkiaine, sädehoito.
