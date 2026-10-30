VERDICT: DONE

Draft, round 1. `check_lesson.py fy4-11` all ok; lint 0/0, check_solutions ok, check_choices no fy4-11 warnings.

- `lesson.md`: Ydinajatus (reaktio → reaktio-, jarrutus- ja pysähtymismatka; tien kitka hidastaa, force diagram; v vs v²; törmäyksessä Δp sama, Δt ratkaisee; vyö ja tyyny; OTI 2017–2021 statistic), Kaava: Pysähtymismatka ja törmäyksen voima (s_r = v0 t_r, t_j, s_j = v0²/(2a) from the (t,v) triangle, s_p, a = μg, F_k = mΔv/Δt), staged example (80 km/h, phone, t_r 2,0 s → 72 m), misconceptions, summary.
- `figures.py`: hero (moose at dusk), braking FBD (fbd.py), stopping distances to scale, occupant (t,v), schematic (t,v) areas, (t,F_k) equal areas.
- `inquiry.json`: 3 predictions, sim + 3 experiments, crash table (`example`), OTI/Liikenneturva table (`statistics`, source_note), conclusion, error spotting, transfer, 3 checks.
- New sim `assets/sims/fy4/fy4-11/` (phone stacking), `tests/sims/fy4-11.json` (22 assertions), `lang/fi.json` sims.fy4-11, sim-spec.
- Exercises 5/4/3 with answers.py and solutions; exit ticket 3; glossary: reaktioaika, reaktiomatka, jarrutusmatka, pysähtymismatka, turvavyö, törmäysaika.

Sources: Liikenneturva collision-speed calculator (t_r 1 s, 9 m/s²); OTI-Turvavyöraportti 2023; Liikenneturva belt-use monitoring 2024. Wet, snowy and icy decelerations and the crash table are labelled example values.
