VERDICT: PASS
CONTENT-HASH: f1c2e6bb3424337d

## Blocking
None.

## Polish
None.

## Checked
Delta re-review after the fixes. sim.js canvas arrows now read v_L and v_H, matching the slider labels (lang sims.fy5-14) and the text. The beats figure alt text (figures.py, figures.json, svg aria-label) ends "T H". The summary Doppler bullet lists MAFY's four formulas with correct signs and conditions in fi, fi-easy and en. The heading is now about choosing the formula. A grep of assets/sims/fy5/fy5-14 and the lesson files finds no v_s, v_h, f_h, T_h or f_b a student can see. The ones left are only in code comments in answers.py, lesson-answers.py and sim.js. answers.py and lesson-answers.py output is identical to origin/main. Earlier checks stand: the four formulas equal MAFY's, the symbols are defined where they first appear, and the example gives 341.10 Hz, 285.78 Hz and Δf 55 Hz.
