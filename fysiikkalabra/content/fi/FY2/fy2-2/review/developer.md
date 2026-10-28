VERDICT: DONE

Round 2 (fix). check_lesson.py fy2-2: all ok.

- inquiry.json: ennuste-1 ratio as `$32\,\text{MJ} : 10\,\text{MJ} \approx 3{,}2$`; tarkistus-2 mistake 0.0001 -> 0.01 with feedback on the inverted ratio; its solution uses a colon (`N = E_salama : E_ruoka = 1000 MJ : 10 MJ = 100`); ketju Järkevyys keeps units in every step; koe-2 initial renamed to the new option name.
- lang/fi.json (sims.fy2-2): new TeX names t_suklaa, t_kaasu, t_tankki, t_aurinko_s, t_aurinko_h, t_aurinko; option n_aurinko_h now "Aurinko Maahan tunnissa" (plain option, no number+unit, so Alkutila line is clean).
- assets/sims/fy2/fy2-2/sim.js: readout and canvas labels use t_<id> when present (`texOf`).
- tests/sims/fy2-2.json: two selects renamed to "Aurinko Maahan tunnissa" (no assertion loosened).
Not changed: lesson.md, exit-ticket.json (clean).
