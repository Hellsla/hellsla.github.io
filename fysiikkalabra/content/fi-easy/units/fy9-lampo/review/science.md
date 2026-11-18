VERDICT: PASS
CONTENT-HASH: 689e602ef05c8a50
SCOPE: delta: fi-easy diff since 49ba8f9 (new tasks fy9-lampo-s7 heating line and s8 melting curve in sovella/tasks.json and solutions.md, intro "kuusi" -> "kahdeksan"); fidelity of s7/s8 to fi; s1-s6 not re-judged.

## Blocking
(none)

## Polish
- s8 Yleisiä virheitä (a): "lämpötilan muutokseksi otetaan 0 °C tai 16 °C". 16 °C is the right size of the change (16 K). The error meant is probably taking -16 °C or 0 °C as ΔT. The same line is in fi.

## Checked
- Recomputed in one script from the task text and the figure data (lessons/FY3/fy3-6 heating_line, fy3-7 melting_curve): s7 a 40 K/180 s = 0,222 K/s; b c = 100·180/(0,50·40) = 900 J/(kg·K), 0,45 % from Al 896; c t = 900·0,50·80/100 = 360 s (358 s with Al); s8 a 20 000/(0,60·16) = 2083 (2,1·10^3; the table value 2100 is inside the 2 % tolerance); b 200/0,60 = 333 kJ/kg; c 220 + 4,18·0,60·20 = 270,2 kJ; d (120-20)/333 = 0,300 kg (the wrong path gives 0,36). All keys are within tolerance. The figure's water slope 80/251 K/kJ matches 1/(4,18·0,60).
- Physics: Pt = cmΔT under the stated assumption that all of the power goes into the block; the plateau is melting at constant temperature, Q = sm. s7 d: the loss grows with the temperature difference, the net power falls, the temperature levels off where the loss equals the heater power, and 360 s is too short. Wording: energy is transferred as heat to the surroundings and increases internal energy; nothing says "turns into heat".
- Significant figures follow the data. Rounding is explained.
- Rubrics: s7 3+4+4+3 and s8 4+5+4+3. Each criterion asks only what its part asks and the solution shows. "Hyväksytään myös" covers the rate method, the table c and 2100.
- Fidelity to fi: ids, figures, skills, links, points, criterion keys and points, answers, tolerances, and the numbers in the text, criteria and solutions are identical (compared with a script).
- Intro: eight tasks, matching the eight in the set.
- The hash was the same at start and end.
