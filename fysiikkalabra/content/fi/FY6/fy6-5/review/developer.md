VERDICT: DONE

Round 1 fixes (check_lesson.py fy6-5 all ok; check_layout --width 345 ok).
- lessons/FY6/fy6-5/figures.py: current arrows violet #7048e8 (was orange); new figure `circuit-q` (circuit with points A–F, voltmeter with black lead and red probe, 9,0 V, 10/30/60 Ω, no potentials); alt text "Violettien"; REUSE note. Potential stays blue (no electrons in this chapter). Regenerated lesson.md figures and the catalog.
- inquiry.json: ennuste-2 gets `figure` fy6-5/circuit-q and a prompt that names the points; ennuste feedback openings varied; hook "kymmeniä tai satoja kilovoltteja" (also in siirto); siirto Periaate: Ohm's law keeps the bird's current tiny, current law then says the rest continues; tarkistus-2 says A is in the plus pole's wire; sim howto "Violetit nuolet"; point letters as maths.
- lesson.md: "pisteillä A–F merkityn piirin silmukka"; bird paragraph corrected; "lähde on tässä luvussa ideaalinen"; point letters as maths.
- assets/sims/fy6/fy6-5/sim.js: violet current arrows; at phone width I_1 label moved off R_1, meter smaller and further right (clear of R_3), earth symbol shifted away from F. Tests unchanged. lang/fi.json sims.fy6-5.selite "Violetti: virta".
