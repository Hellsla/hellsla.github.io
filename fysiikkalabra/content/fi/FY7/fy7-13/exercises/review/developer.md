VERDICT: DONE

Added (fi, en, fi-easy; only additions, nothing existing changed):
- exercises.json: fy7-13-L1-09 (MAFY lookup: helium 587,56 nm, table *Spektriviivoja*, 600 lines/mm, first-order angle 20,6°), fy7-13-L2-09 (figure fy7-13/setup-q: λ from the k = 2 spot, 630 nm), fy7-13-L2-10 (figure fy7-13/spectrum-q: lines/mm from the red edge of the first-order spectrum, 250).
- solutions.md: complete solutions for all three; the figure tasks have **Kuvaajan lukeminen:**.
- lessons/FY7/fy7-13/answers.py: three lines added.
- lessons/FY7/fy7-13/figures.py: question-safe variants setup-q and spectrum-q inside FIGURES and REUSE (no x, λ or N written in them).
- content/en and content/fi-easy figures.json: translations of the two new figures.
Checks: check_lesson.py all ok; check_solutions ok; figures --check ok. Not run: figcat.py build, check_i18n.py (coordinator).
