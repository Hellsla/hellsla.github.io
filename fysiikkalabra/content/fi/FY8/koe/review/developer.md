VERDICT: DONE

Wrote FY8 Esimerkkikoe from scratch (7 tasks, 120 p offered, max 70 p, 120 min).
- tasks.json: Osa 1 fy8-k1 (10 choices, chapters 1,1,2,3,6,7,9,10-11,13,15); Osa 2 fy8-k2 LED/Planck constant with error bars (graph, uncertainty), k3 decay counts with exponential fit and sqrt(N) scatter, k4 D-T fusion (binding energy, Q, energy per kg, explanation), k5 hydrogen levels (photon, absorption, ionisation, orbital); Osa 3 fy8-k6 lead shielding (background, ln plot, mu, dose limit design, uncertainty/validity), fy8-k7 F-18 PET (decay, annihilation, effective dose, isotope choice). All data invented (source: example); real sources cited only for STUK-A263 (2020) 5,9 mSv and the 1 mSv public limit.
- solutions.md: complete solutions, Yleisiä virheitä, Hyväksytään myös; model graphs generated.
- lessons/FY8/koe/answers.py computes every number; figures.py has fy8-k1-stop (task figure) and three model graphs; docs/figures/catalog.json rebuilt.
Checks: practice.py figures/check OK, build OK, check_layout 360/768/1280 OK.
Open: no en/fi-easy translation exists or was written; fy8-k7 dose coefficient 0,019 mSv/MBq is an example value (FY8-14 uses another FDG dose).
