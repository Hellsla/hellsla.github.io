VERDICT: PASS
CONTENT-HASH: 33e452fa72f8750d

## Blocking

## Polish
- exercises.json fy7-4-L1-04 — a Finnish power line carries alternating current, so in the Earth's static field the force on it reverses 100 times a second and its time average is zero. 1,0 N is the force at the instant the current is 200 A. The text leaves a steady force implied (C at level 1, no wrong number) — add "hetkellä, jolloin virta on $200\,\text{A}$" or make it a tasavirtayhteys; the fi version has the same text.
- solutions.md fy7-4-L3-01 Järkevyys — "langan jännitys olisi kaksinkertainen painoon verrattuna": with two threads each one carries $mg$, and only the two together carry $2mg$ — write "lankojen yhteinen jännitysvoima".
- figures.py force_angle description "tasaisesti nouseva käyrä" — the curve is $0{,}45\,\text{N}\cdot\sin\alpha$, which rises less and less steeply. "Nouseva ja loiveneva käyrä" would not suggest a straight line to a reader who cannot see the figure (also noted in the fi review).
- solutions.md fy7-4-L1-04 Järkevyys — "about $1\,\text{kg}$ per metre" for a $200\,\text{A}$ conductor is on the high side (typically about $0{,}5\,\text{kg/m}$). The conclusion still holds.

## Checked
- Hash 33e452fa72f8750d (--lang fi-easy) at the start and the end.
- One script recomputed all 21 numeric answers with my own formulas, and compared them with exercises.json and with the output of answers.py. Every answer is inside its tolerance, and every 2-figure rounding is inside the 2–3 % band.
- Directions: L1-06 I east × B north = up. L2-08 I down × B right = towards the viewer. The palm descriptions of both hand rules are right, and every distractor's feedback names the actual misconception.
- L1-04 and L3-03: the angle 74° between the wire and the field (N–S wire), and the horizontal component $B\cos 74^\circ$ that lifts the E–W wire (current east). The vertical component gives only a horizontal force: correct.
- Fits: balance-points least-squares slope 0,2995 g/A, so the line passes (5,0 A; 1,50 g) and B = 0,0734 T. Coil slope 5,795 N/A gives l = 5,27 m (≈ 65 turns at 1,3 cm). For force-angle the sine fit gives F_max = 0,451 N. Rod: slope 0,935 (m/s²)/A and intercept −1,96 m/s², so B = 0,351 T and μ = 0,200. Slopes are read from the fitted line, as the guardrails ask.
- L2-05 half range 0,0018 T is called a simple scatter estimate, "ei keskiarvon epävarmuus", as the guardrails ask. L2-06 the student's 0,0169 T comes from using l = 6,0 cm.
- L3-05: opposite currents repel, I = 54,25 A. The vertical stability argument from F ∝ 1/r is right, the lateral caveat is stated, and the task limits the motion to vertical.
- L3-02: AC short circuit "hetkellisesti". The force on opposite currents stays repulsive. −270 N with the stated sign rule.
- Every solution states the principle, solves symbolically first, converts units and justifies the significant figures. The notation ($I l B\sin\alpha$, $B_1$, $\mu_0$) matches the brief, and the scope stays inside FY7 fy7-4.
