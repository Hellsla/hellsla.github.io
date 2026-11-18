VERDICT: PASS
CONTENT-HASH: e2d1a4f13b4f84c1
SCOPE: delta: en tasks fy9-lampo-s7 (fy3-6/heating-line) and s8 (fy3-7/melting-curve) in sovella/tasks.json and solutions.md, and the changed intro (git diff 49ba8f9 HEAD); fidelity to fi; s1-s6 not re-judged. Language: en.

## Blocking
(none)

## Polish
- s8 b, d call 333 kJ/kg "the table value", while s1 data and s5 use 334 kJ/kg (both acceptable).
- s8 text: after 220 kJ the graph shows meltwater, not ice; "temperature of the ice/water" would be exact.
- s7 b reasonableness uses water 4190 J/(kg·K), s8 uses 4.18 kJ/(kg·K); harmless.

## Checked
- Recomputed in one script from the task text and the figure source (lessons/FY3/fy3-6, fy3-7 figures.py): s7 a 40 K/180 s = 0.222 K/s; b c = 100*180/(0.50*40) = 900 J/(kg·K), 0.4 % from Al 896; c t = 900*0.50*80/100 = 360 s (358 s with 896); s8 a 20000/(0.60*16) = 2083 J/(kg·K); b 200/0.60 = 333 kJ/kg; c 220 + 4.18*0.60*20 = 270.2 kJ; d 100/333 = 0.30 kg (wrong path 120/333 = 0.36). All answers inside their tolerances. Figure: line (0 s; 20 °C)-(180 s; 60 °C); melting curve (0; -16), (20; 0), (220; 0), (300; 31.9), whose last slope 0.398 K/kJ equals 1/(4.18*0.60).
- Physics: s7 Pt = cm dT with the stated all-power assumption; d mechanism (loss grows with temperature difference, net power falls, levels off at balance, 360 s too short) correct, no "energy lost". s8 plateau = melting at constant temperature, Q = sm; 120 kJ is mid-plateau so half melted, temperature 0 °C. Scope FY3. Significant figures follow the read values.
- Assessment: criteria sum to part points (s7 3+4+4+3, s8 4+5+4+3); each criterion asks only what the part asks; Hyväksytään myös covers the rate route and table values.
- Fidelity to fi: ids, figures, skills, links, kinds, points, criteria keys/tags, answer values and tolerances identical; every number in task text, criteria and solution sections s7/s8 matches fi (script comparison).
- Intro: "Eight problems", matches the eight tasks.
- Hash e2d1a4f13b4f84c1 (units.py hash --lang en) at start and end.
