VERDICT: PASS
CONTENT-HASH: 3b1b29439e94b105

Round 2, physics-expert. Hash checked at start and at end: 3b1b29439e94b105 (unchanged). No real physics, number, unit or scope errors found. Findings below are optional polish only.

Scope: lesson stays within the MAOL FY3 text (system, state variables, "jos yhtä muutetaan, vähintään toinen muista muuttuu", micro model, absolute zero by extrapolation). No ideal gas law, Boyle's law or E_k formula. p proportional to T at constant V and n is used only as a stated fact and in the extrapolation experiment, which MAOL names explicitly.

Checked and correct (lesson.md):
- Lines 6-10: system/surroundings/closed system, state variables, p = F/A in Pa, micro model (smaller V: more frequent collisions, each equally hard; higher T at constant V: more frequent and harder), Celsius/Kelvin definitions, same size of degree, p and mean kinetic energy proportional to T. All correct at this level.
- Lines 24-26 and 50-62: k = 37/100 = 0,37 kPa/°C, theta = -100/0,37 = -270,3 °C, rounds to -270 °C. Table values 100/107/115/122/129/137 match 100·T/273,15 to the stated precision.
- SVG (line 30-46): scale 1,25 px/°C (0 at x=445, 100 at x=570), -270 at x=107, y scale 1,5 px/kPa (100 at y=100, 137 at y=44). Axis at x=70 is about -300 °C, as line 48 says. Consistent.
- Line 67: 293/283 = 1,035 (293,15/283,15 = 1,0353). Correct.
- Line 64: real gases liquefy before the extrapolated point; stated as a model limit. Correct.

Findings (all optional):
1. exercises.json:~46 (fy3-3-L2-03) and solutions.md:61-62 — exact result is -270,9 °C, answer given is -270 (2 sf data, 80 and 91 kPa). Within tolerance, and consistent with 2 sf, but the solution shows -270,9 and then states -270. Fix (optional): add "(2 merkitsevää numeroa)" to the answer line, or use answer -271. Not required.
2. sim.js:49-52 — when the volume slider is dragged smaller, particles beyond the new wall are clamped and counted as a collision (momentum added) in one frame, so the measured pressure spikes briefly. Transient only, 1,5 s window; the note already says the measured value fluctuates. No fix needed.
3. sim.js — all particles share one speed (no Maxwell distribution) and do not collide with each other. Acceptable simplification; the sim-spec says particles bounce off walls and the readout says "keskinopeus". No fix needed.

(2) Exercise recomputation in python3 -I from problem text alone (answer vs. results; OK = within 2 % for 273,15, for 273, and for student rounding):
 L1-01 294    -> 294,15 / 294        OK
 L1-02 77     -> 76,85 / 77          OK
 L1-03 -196   -> -195,75 / -195,6 (273)  OK
 L1-04 25     -> 25 K                OK
 L1-05 -270   -> -270,45 / -270,3    OK
 L2-01 60     -> 59,85 / 60          OK
 L2-02 102    -> 101,55 (101,6 or 102 by student) OK
 L2-03 -270   -> -270,909 (k = 0,275, p0 = 74,5)  OK (|diff| 0,3 %, graph readings -265..-280 pass)
 L2-04 4.0    -> 3,9955 (273,15) / 4,0 (273)  OK
 L3-01 321    -> 320,82 / 320,83 (273) / 320,8 rounded  OK
 L3-02 127    -> 127,05 / 127,0 (273)  OK
 L3-03 -127   -> -126,575 / -126,5 (273) / -126,4 rounded  OK
Worst-case relative deviation of any plausible student result from the answer: 0,3 %. All well inside tolerance 0,02.

(3) solutions.md: all substitutions, intermediates and sanity checks verified (e.g. L3-01 about 7 % rise, L3-02 "36 °C" wrong Celsius ratio = 27·200/150, L3-03 Celsius halving gives 10 °C, L2-04 Celsius ratio negative). No wrong reasoning. exit-ticket.json: all three answers correct (3,5 % rise; -273 °C = -273,15 rounded; more frequent and harder collisions).

(4) sim.js verified analytically: speed v = V_REF·sqrt(T/300), so mean E_k is proportional to T. Impulse per wall hit is 2|v_x| (unit mass), total x-wall momentum rate = N v²/W_c, per wall length (2H_c) gives N v²/(2 W_c H_c); this equals pRef = N V_REF²/(2·PX·H_c) at 300 K and 1 dm³ (W_c = PX). The y-walls give the same value. The effective box (W - 2R, H - 2R) is used consistently, so p is proportional to T/V and pTheory = 100·(T/300)/V is the correct reference. Note and readout texts are physically correct.
