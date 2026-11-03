VERDICT: PASS
CONTENT-HASH: 2114363472e26314

## Blocking

## Polish
- exercises/solutions.md:80 (L2-03 Järkevyys) — "joten lauta alkaa kiertyä vastapäivään" ignores the board's own weight, which the task does not exclude; the asked quantity (moment of the two forces) is unaffected — add "laudan paino jätetään huomiotta" to the task, or say "voimat kiertävät lautaa vastapäivään".
- exercises/solutions.md (L3-01 Vastaus) — "suurin, kun kampi on vaakasuorassa eteenpäin": with the crank horizontal backwards the magnitude is equally large (opposite sense); fine as "suurin ajosuuntaan", worth saying so.

## Checked
- One script recomputed all 12 answers with my own vector torque τ = r_x F_y − r_y F_x: L1 37,5 / 9,6 / 150 / 12 / 0,30; L2 17,2 / 29,75 / 7,0 / 231; L3 61,9 / 1,0 / 48 — all within tolerance of exercises.json and answers.py.
- Figure fy5-1/ruutu rendered: P is 4 squares right and 3 up from O, force horizontal, arm 3 squares = 0,30 m; solution reads it correctly and cross-checks with d sin α = 0,50·3/5.
- L2-01: angle to the door plane equals angle to the hinge–handle line, so r = d sin 35° is right.
- L2-03 and L3-03 signs: CCW positive; L3-03 couple, ΣF = 0, ΣM = 48 Nm CCW (loosening direction).
- L3-01: weight-direction force, arm = horizontal distance d cos 45°; zero with crank vertical; correct.
- Every solution complete (Annettu → Järkevyys), unknown solved symbolically first, cm→m conversion in L2-02, significant figures justified by the limiting datum.
- No later-course physics; no angular quantities.
