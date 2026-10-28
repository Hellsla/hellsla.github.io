VERDICT: FAIL
CONTENT-HASH: fd714c1abef54a93

## Blocking
- lesson.md:125–128 (figure *energian-muuttuminen*, figures.py:107) — The figure still has the round-1 error. The flashlight figure draws a filament and labels the narrow arrow *säteilyenergia* and the wide one *lämpöenergia*. So the picture says radiation is the small part, but most of a filament lamp's output leaves as infrared radiation. It also contradicts the corrected text and the figure's own aria-label ("valoksi ja lämpöenergiaksi"). — Label the narrow arrow $\text{valo}$ (or $\text{näkyvä valo}$) in figures.py and regenerate.
- templates/inquiry.js:133, 163 (exp-1, exp-2 status line; shots exp-exp-2-390-2) — The status line is set with `textContent`, so the student sees the literal "Vakiona: kitka, alkukorkeus $h_0$. Säädä t …", raw dollar signs included. The recorded table cells (`fi(r.vary)` + unit, e.g. 1,0 s, 63) are plain text too. That breaks the teacher's rule that everything is in LaTeX. — Typeset the status and the rows (KaTeX render after `say`/`render`, values as `$1{,}0\,\text{s}$`). Fix it in the shared template.
- inquiry.json:244 (data) — The table header "Mekaaninen energia (J)" and the values 0,60 … 0,31 are plain text (shot stage-tutki-390-3). — Write `$E_\text{mek}\ (\text{J})$` and `$0{,}60$` etc.

## Polish
- inquiry.json:465–474, 538–547 — The measure labels are `"E_p"`, `"E_k"`, `"E"` without `$…$`. They render, but only because the template wraps them, while Eth carries its own `$`. — Make the four labels consistent.

## Checked
- One script recomputed every number (inquiry, example, exit ticket, exercises) and compared it with lesson-answers.py, answers.py and the JSON. All match: example 120 J, data 0,29 J, transfer 335 kJ, check-2 2380 J → $2{,}4\cdot10^3$ J (a rounded 2400 J is inside the relative tolerance), $mgh_0 = 981$ J, exit ticket 3,8 kJ.
- The sim's integration (bead on a parabola, tangential friction μmg, RK4) matches lesson-answers.py line for line. Every model-answer value matches the run after the sim's largest-remainder rounding: exp-1 63/918, 862/119, 424/557 J; exp-2 mechanical 981 → 469 → 143 J, thermal 0 → 512 → 838 J. The constant per-metre friction is stated in *Mallin oletukset*.
- Each experiment varies only t, with friction and h0 locked, and simState has Ep, Ek, Eth and Ekok.
- Round-1 fixes are in: check-2 uses *näkyvä valo* (about 5 %, with the IR said in the solution), lesson.md:103 is fixed, kitka shows its name, "korkeudelta $h_0$" is used, and the force wording is gone.
- The correct options and all feedback physics in pred-1/2, exp-1/2, virhe, check-1 and check-3 are right.
- Figure 3 is to scale (0,16 px/J, every bar 800 J).
- No E_k/E_p expressions, work, Q = cmΔT or chain products. \cdot, colon division and substitution conversions are used, with no ×. No named-source data.
- The canvas and readout are all LaTeX (sim-1280, sim-390).
