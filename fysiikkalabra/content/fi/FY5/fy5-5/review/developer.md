VERDICT: DONE

Round 1 fixes. check_lesson.py fy5-5: every line ok. Screenshots regenerated.

Exercises
- solutions.md: L1-02 Periaate (ships treated as point masses by the task; order-of-magnitude estimate) and Järkevyys (about a 250 g object's weight); L1-01 Järkevyys (0,04 mg:n massaisen hiukkasen paino); L1-05 "alle kolmasosaan"; L2-04 "lentokorkeudellakaan".
- exercises.json: L2-01 "samanmassaisen"; L1-03/L1-04 answers 3.70 / 3.80.

Lesson
- lessons/FY5/fy5-5/figures.py (regenerated into lesson.md): kuvaaja shows $m_1 = m_2 = 10\,\text{t}$ in the plot; the curve starts at r = 2 m, so the stub is gone.
- lesson.md: sentence before the graph names the 10 t case; apple 1,96 N (gives 9,8 m/s²); the g table paragraph says the Maa value 9,80 ignores rotation and the book uses 9,81; Finnish quotes in the misconception paragraph.
- inquiry.json: ennuste-1 option "koska suurempi massa vetää enemmän".
- lesson-answers.py: comment 2,702e-3.

Sim at 390 px: not a bug. IntersectionObserver calls loop() on entering the view; the new stage-tutki-390-1 and exp-koe-2-390-1 captures draw the canvas.
