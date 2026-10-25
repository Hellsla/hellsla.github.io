VERDICT: PASS
CONTENT-HASH: 36ffef8025cd3db6
## Blocking
(none)
## Polish
- lesson.md:31 — label "Q < 0 tai W < 0" centred at x=478, 22px: measured left edge x≈404 (Arial metrics) or x≈391 (DejaVu Sans), so it touches or crosses the box stroke at x≈401 — use `x="414" text-anchor="start"` (right edge ≤ 588) or shorten it.
- lesson.md:43 — "olisi Q = −150 J ja ΔU = 0" assumes the slow compression still takes W = 150 J — write "olisi Q = −W ja ΔU = 0".
- exercises.json:82 — "Mäntää painetaan … 120 N:n voimalla" is the hand's force, not the piston's force on the air (atmosphere also pushes the piston) — reword as in L2-01: "mäntä työntää ilmaa … 120 N:n voimalla", so W = F s = 18 J is exact.
- exit-ticket.json:11–12 — system is "sen sisällön", yet energy goes from the coffee to "pullon kylmempiin seiniin", which would lower the contents' U — make the system "pullo ja sen sisältö".
- exercises.json:98 — L3-03 is the same computation as L2-03 (line 64), Q = ΔU − W with an expanding gas — add a second idea to make it level 3.
## Checked
- Hash 36ffef8025cd3db6 before and after; lint 0/0, not repeated
- ΔU = Q + W sign convention identical in lesson.md, 12 solutions, answers.py, exit ticket
- Worked example −40 J + 150 J = 110 J
- L1: 570 J, −8,4 kJ, 250 J, −500 J, −70 J; signs read correctly, negatives asked "etumerkkeineen"
- L2-01 W = 60 J, Q = −15 J; L2-03 Q = −1200 − (−2000) = +800 J
- L2-02 P t = 180 kJ, ΔU = 160 kJ; L2-04 W = 10 kJ, ΔU = 12 kJ (P from fy3-2)
- L3-01 ΔU = 0 ⇒ Q = −18 J; L3-02 h = 1000/(12·5,0·9,81) = 1,699 → 1,7 m, rounded only at the end
- L3-03 Q = +160 J; exit ticket 1: 180 J
- SVG: arrow tips at x=200 meet the box (200–400 × 70–230), line ends inside arrowheads, other labels clear; formula matches lesson.md:15
- Units of solutions and answers.py output match exercises.json
