VERDICT: PASS
CONTENT-HASH: 8c105b85746eef7d
Mode: full (round 1)

## Blocking
- none

## Polish
- exercises.json fy8-6-L1-06 (feedback of the "kuori absorboi" distractor and of the correct option) — "fotoneja ei synny lainkaan" is stricter than the lesson, which says the LED "ei juuri" radiate and that the measured U_k is about 0,1 V below hf/e — write "ei juuri synny".
- solutions.md fy8-6-L2-06 Vastaus — 3,65 % comes from a difference (6,868 − 6,626), so the voltages' three figures do not carry its third figure — say "noin 3,6 %"; answer and tolerance accept both.
- solutions.md fy8-6-L2-04 Järkevyys — "kuten fluoresenssissa aina" — "yleensä".
- solutions.md fy8-6-L1-07 Periaate — "likimain" where the task assumes "täsmälleen" — one word.

## Checked
- All 19 numeric answers recomputed from the task texts in one script: agree with answers.py and exercises.json (largest relative difference 0,14 %, inside every tolerance).
- Least-squares fits redone: L2-05 slope 61,5 mA/V, U_k = 1,857 V; L3-01 k = 4,212·10^-15 V s, b = −0,164 V; L3-04 k = 4,208·10^-15 V s, b = −0,062 V → −0,112 V after the zero correction, slope unchanged.
- L2-08: the table's own fit gives k = 3,976·10^-15 V s, b = −0,074 V, standard error 0,21·10^-15 V s, as stated; h = 6,376·10^-34, Δh = 0,336·10^-34 J s; exactly one correct option, distractors wrong with correct reasons.
- L1-06: one correct option; the three distractors are really wrong.
- L2-06: h deviations −11,6 %, −4,5 %, +3,65 %; the reasoning about the reading methods is right.
- L2-07: half-maximum points 620 and 640 nm, ΔE = 0,0625 eV, realistic width; thermal-spread reason correct.
- L3-05: f = 6,169·10^14 Hz, λ = 486,0 nm, direct formula 504,1 nm, Δλ = 9,5 nm.
- Assumptions stated in the tasks (eU_k = hc/λ "oletetaan", one photon per electron, example data marked); internal-energy wording follows the guardrails.
- Scope inside FY8 and the brief; notation as in the brief.
- All 21 solutions: symbolic form before substitution, conversions, rounding reasons, real reasonableness checks. Hash identical at start and end.
