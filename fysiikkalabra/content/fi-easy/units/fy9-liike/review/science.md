VERDICT: PASS
CONTENT-HASH: f7b2fe75776f33d3
SCOPE: delta review of the Sovella set: new tasks s7 (Kärry radalla) and s8 (Kaksi kulkijaa samalla tiellä) and the changed intro; s1-s6 not re-judged (previously passed).

## Blocking
- (none)

## Polish
- s8 d: the meeting place is given as $14{,}7\,\text{m}$ from data with two significant figures ($2{,}0$ and $1{,}0\,\text{m/s}$, positions read to whole metres); $15\,\text{m}$ (or "noin $15\,\text{m}$") would match the rounding reason used in a-c. Word task, no answer check.
- s8 figure: the lines cross on a grid crossing, so $4\,\text{s}$ and $12\,\text{m}$ can be read off; nothing is marked and the rubric scores the calculation, so no answer is given away. A Hyväksytään myös line on how a reading-only answer to c scores would help.

## Checked
- One script recomputed every number from the figures' own points (fy4-1 figures.py) with my own formulas, beside answers.py: s7 $3{,}0$ and $-2{,}0\,\text{m/s}$; $t_1 = 2{,}667\,\text{s}$, $t_2 = 8{,}0\,\text{s}$; $v_\text{ka} = 0{,}40\,\text{m/s}$, path $20\,\text{m}$, mean speed $2{,}0\,\text{m/s}$; s8 $\pm 2{,}0\,\text{m/s}$, $4{,}0\,\text{s}$, $12\,\text{m}$, d $5{,}33\,\text{s}$, $14{,}67\,\text{m}$. All agree; the relative tolerances accept the two-figure roundings.
- Every number token in the s7 and s8 tasks and solutions is identical to the Finnish text (script comparison); answers, tolerances and points identical. The simpler sentences keep every physical step (siirtymä, kuljettu matka, the reason for the negative sign).
- Physics: slope = velocity, sign = direction, displacement vs distance and why mean speed ≥ |mean velocity| are right; meeting condition and closing speed right; the s7 corners are an idealisation the text states. Scope FY1/FY4 kinematics.
- Rubrics: criterion points equal part points (s7 3+3+4+4, s8 4+5+2+4); each criterion asks only what its part asks; common mistakes and Hyväksytään myös right.
- Figures: neither marks a slope, crossing, path or mean value.
- Intro: "kahdeksan" matches the set (8 tasks, 124 points).
- `practice.py check` OK; hash the same at start and end.
