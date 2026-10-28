VERDICT: PASS
CONTENT-HASH: 3d0ab462b0888669

Delta review over the audit's PASS (ba0823c1b322100e): L1-03 (water rocket) replaced by a figure task fy3-9/boyle-points; its solution, answers.py line and figure.

## Blocking
- none
## Polish
- many quantities in other exercises are still plain text (30,0 ml, 101 kPa, 160,0 kPa, 300,0 bar, 2800 m³ …); the conversion to LaTeX is incomplete.
- the solution could name the second route, p = 50 kPa · 40 ml / 25 ml = 80 kPa, as a check on the chosen point.
## Checked
- Figure needed: text gives only 25 ml; the values come from five points, none at 25 ml, so a student must use pV = vakio, not read or interpolate. The description lists points, not the constant.
- 20 ml · 100 kPa / 25 ml = 80 kPa; (40; 50) gives 80 as well; the interpolation trap gives 83,3 kPa, outside the ±3 % band (77,6-82,4). Solution says so.
- 360 px capture: five dots, axes and labels readable, grid on 5 ml and 25 kPa; answer and unit in answers.py match.
- Level L1 fits (one law, one chosen point). Solution has Kuvaajan lukeminen. Finnish clear; LaTeX in the new text.
