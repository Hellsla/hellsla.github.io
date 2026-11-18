VERDICT: PASS
CONTENT-HASH: f5355edae2761e52
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8 and -s9; older tasks untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- s8 Common mistakes, part a: the example "$\mu = 16 / 20\,\text{cm} = 0.80$" is left over from the old read-off values. With the current points $(0;\,80)$ and $(10;\,20)$ the quotient is $80/20 = 4$ and the wrong result $4/10\,\text{cm} = 0.40\,\text{1/cm}$. Fix the numbers so the student does not see a 16 that is not in the data.
- s9 a: the grid point now appears only in the solution and criterion, not in the task text; the second point is still the origin. Acceptable.
- s8 gives the model ready-made (a conscious choice).

## Checked
- Opened the en packet: s8 and s9 in tasks.json (own English text), solutions.md and the checks (practice.py check OK); hash same at start and end (f5355edae2761e52).
- Round-1 items: s9 a text no longer gives $(250;\,18\,000)$, so $H_0$ is read off the graph and `graph_read` measures something. s8 a: second point $(10\,\text{cm};\,20\,\mu\text{Sv/h})$ matches the solution ($\ln 4/10 = 0.14$).
- s8 d: the assumption is asked in the text ("Also name one assumption ... and its effect"); the criterion matches and what the assumption is stays with the student.
- s9 c: the reworded task (distances "were zero", constant rate) does not reveal $t = 1/H_0$ or the unit conversion.
- Translation: same numbers, points, tolerances and criteria as Finnish; decimal points; terms (attenuation coefficient, dose rate, Hubble constant) correct. Results rounded to two figures like the data; aligned calculation rows; unit fields language-neutral.
- Points 3+3+3+4 and 3+3+4+3 equal the criterion sums; 360 px: check_layout and shots.md, not opened.
