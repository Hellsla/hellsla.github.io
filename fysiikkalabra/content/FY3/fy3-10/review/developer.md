VERDICT: DONE

Correction pass, four items. check_lesson.py fy3-10: lint, latex, build, sims (34 assertions, sweep at 360/390/1280 px), layout 360 px all ok.

- lesson.md (line 148): the p/p_ref sentence now names the reference state (N = 100 hiukkasta, T = 300 K, V = 100 %; p/p_ref = 1, value 2 = twice the reference pressure).
- sim.js: note under the canvas gains the clause that changing the volume leaves particle speeds, and so the temperature, unchanged. "mikä on normaalia tilastoa" became "(tilastollista vaihtelua)". The note also gains the sentence "Pylväiden asteikko mukautuu arvoihin: vertaa pylväitä toisiinsa ja lue arvot numeroina, älä vertaa pylväiden korkeutta eri tiloissa." The note is about 77 words, slightly over the 75-word target because both required additions were kept.
- sim.js drawing: added the label "asteikko mukautuu" (ts(10), via lab()) on the axis-name row, left of "p/p ref". A first placement below the axis name collided with the bar value labels in the sweep, so it moved.
- solutions.md, fy3-10-L2-01 Järkevyys: Z removed. The new text says the molecules are close together at 180 bar, size and attraction matter, the ideal-gas equation gives about 6 % too high a pressure, the result is an estimate, and the answer 180 bar stands.

No exercise, answer, answers.py, figure, formula or exit ticket changed.
