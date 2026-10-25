VERDICT: DONE

Lesson-form retrofit (lint: 2 errors -> 0 errors, 0 warnings).

lesson.md
- Ydinajatus: new inline SVG after the paragraph deriving rho*g*h: a water column of base area A and height h in a pool, its weight G pressing on the base, with LaTeX labels (foreignObject .fig-tex) G = rho*A*h*g and p = G/A = rho*g*h; viewBox 0 0 600 300, currentColor, 24 px text, aria-label says it is a schematic.
- Esimerkki: same problem and numbers, now in 5 stages separated by `<!-- vaihe -->`: Tunnetut ja kysytty, Kaavat ratkaistuina (p = p0 + rho*g*h, F = rho*g*h*A; why only the overpressure loads the window), Sijoitus (117 720 Pa = 117,72 kPa; p ~ 219 kPa, symbolic first row), Voima ikkunaan (~1,8 kN), Jarkevyys (2,2 x air pressure, ~180 kg, diver not crushed).

No change to solutions.md (Kaava lines already symbolic), inquiry.json (section titles unchanged), sim.js, exercises, answers, exit ticket or tests.

check_lesson.py: all ok; test_inquiry.py: 28 passed; 390 px screenshot: new figure renders without clipped or overlapping labels.
