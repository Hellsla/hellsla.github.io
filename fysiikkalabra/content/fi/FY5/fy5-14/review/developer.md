VERDICT: DONE

Fix round 1.
- inquiry.json ennuste-1 (:59): geometry stated (listener on the road's line like A, not roadside); correct-choice feedback (:64) says a roadside listener hears a gliding frequency; reflection prompt (:315) contrasts it with the hook. Hook left as is (the contrast is explicit).
- inquiry.json: koe-1/koe-2 intros name 0, 34, 102 m/s as required rows and min 3, so prediction feedback quotes only tabulated values; spectrum task now a sung vowel (labelled invented example data); "huojuntataajuus" defined in huojunta-kuvaaja; fft task has an example-data fallback without a microphone.
- lesson.md: "kummallakin puolella noin 9 %" (Järkevyys); police radar dropped; aria-label "äänirautalla".
- figures.py: Doppler figure arcs clipped inside the margins and above the brackets; huojunta-tehtava shows the origin 0. Regenerated with figures.py.
- sim.js lab(): paper backing behind every canvas label.
- "Dopplerin ilmiö" is used throughout the text (only the glossary key differs). "Exit ticket" heading is the shared template: left.
Not changed: sim.js heard() polish (not in the list). Checks: figures.py, check_lesson.py (all ok), lint_lesson.py (0 errors), check_solutions.py ok.
