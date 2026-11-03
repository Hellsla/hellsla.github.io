VERDICT: FAIL
CONTENT-HASH: 0ee7289539a81dc8

## Blocking
- lesson.md:216 (figure electromagnet; lessons/FY7/fy7-3/figures.py:146 `f.arrow(cx + 62, 210, cx + 40, 210, ...)`) — A: the current arrow points the wrong way. The battery's terminal nub, which marks the positive terminal, is on top (rect y = 122). The arrow on the bottom lead points left, away from the battery, so the drawing shows current leaving the − terminal. In the outer circuit it flows from + through the switch and the coil back to −. — Fix: make the arrow point right, `f.arrow(cx + 40, 210, cx + 62, 210, …)`, or draw the battery with its nub at the bottom.

## Polish
- (none)

## Checked
- One script with my own formulas and the coil field as a numerical sum of loops (not the closed form), printed beside lesson-answers.py; every value matches. Sim on load: 1,232 vs long-coil 1,257 mT. Koe 1: 4,67/2,46/1,66/1,25 mT. Koe 2: 2,46/2,41/1,25 mT, and 0,363 mT at 2 cm outside the end.
- Least-squares fit A = 2,4651, B₀ = 0,0352, ΔA = 0,0121 mT/A. μ₀ = 1,2326·10⁻⁶ Vs/(Am), relative uncertainty 1,74 %, 1,9 % below the true value. Finite-coil factor 0,983, corrected 1,254. Mistake values 123 and 1233 are the right slips, and the coil-fit figure matches the table.
- Worked example: 12,57 mT and 251×. Etsi virhe: 5,0·10⁻⁵ T and 5,03 mT. Siirto: 0,2653 A, mistakes 26,5 and 3,33. Check 2: 1,5 mT, mistakes 0,015 and 9,42, about 30× Earth's field. Exit ticket ×1. Wire graph: 200/100/50 µT.
- Round-2 items fixed. The electromagnet now has a switch in one lead in both panels, closed on the left and open on the right. Hook: "aivan neulan yläpuolella" (77° at 1 cm). Mittaus mistake is 1233. Check 2 says "tasavirralla".
- Directions: wire-field side view (front arcs to the right) and top view (CCW, compass N ends tangent), coil-field •/× giving N on the right, coil-dims (front strands down, B to the right), sim dir = 1 → N on the right, field lines outside running N → S, exit ticket 2.
- Choice items: exactly one correct option each, and every distractor's feedback is physically right.
- Conditions stated where used: long wire and other conductors far away, long coil with air inside and far from the ends, about half the centre value at the ends. Scope is FY7 only (no self-induction, no para- or diamagnetism).
