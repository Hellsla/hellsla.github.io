VERDICT: DONE

Round 1 fix, lesson.
- inquiry.json: mittaus text states "Käämin halkaisija on 3,0 cm" (science Blocking); mittaus solution: slope read as (6,2 − 0,04) mT : 2,5 A ≈ 2,46 mT/A, and Järkevyys says the difference is slightly larger than the uncertainty, cause in the next task; epavarmuus prompt says to add the relative uncertainties; koe-1 name "käämin pituus (cm)" so the table header has its unit.
- lesson.md: one sentence in "Magneettivuon tiheyden määrittäminen käämin sisällä" on adding relative uncertainties (slope rule A = μ0 N : l was already there); Järkevyys no longer claims the school sensor's range, compares with Earth's field instead; figures regenerated from figures.py.
- lessons/FY7/fy7-3/figures.py: hero car now clamped to the magnet's face (no gap); coil-dims B label moved left of the coil, off the windings; wire-field I arrow and label moved below the table onto clear paper; "virta katkaistu".
- lesson-answers.py: comment 4,67 mT.
- assets/sims/fy7/fy7-3/sim.js: coil radius rp 17 px (2,0 cm at 8,4 px/cm) in both layouts. No test loosened.
check_lesson.py fy7-3: all ok.
