VERDICT: PASS
CONTENT-HASH: e8571d0ddd50133c
SCOPE: delta added-exercise from 717b427c7d574c97 base 81db4a6fd727

## Blocking

## Polish
- exercises/solutions.md (fy3-16-L1-09, Periaate) — "Lämpö otetaan keittolevyltä, joten energia säilyy" draws the wrong conclusion from the right fact. Better: "Energia säilyy: höyrystymiseen sitoutuva lämpö tulee keittolevyltä."
- exercises/solutions.md (fy3-16-L2-09, Järkevyys) — "Oletus häviöttömyydestä tekee todellisesta arvosta hieman pienemmän" is still ambiguous (carried over). Meant: with losses, less than $Pt$ reaches the block, so the true $c$ is a little below the computed 900 J/(kg·K). Say that.

## Checked
- L1-09 (new situation, boiling pan): water already at 100 °C, so $Q = rm$ alone applies; $2260 \cdot 0{,}30 = 678\,\text{kJ} \approx 680\,\text{kJ}$; MAFY 2260 kJ/kg as in docs/mafy-arvot.tsv (VERIFIED); answers.py agrees. The check against heating the same water 0→100 °C (126 kJ, ratio 5,4) is right.
- L2-09: $c = Pt/(m\Delta T) = 400 \cdot 180/(2{,}0 \cdot 40) = 900\,\text{J/(kg·K)}$; the lossless assumption is stated in the task; both end points are on grid crossings of `fy3-6/heating-line`.
- The same figure in the chapter *Aineen lämpeneminen ja jäähtyminen* (0,50 kg, 100 W) also gives 900 J/(kg·K), so the two chapters do not contradict each other.
- L2-10: $t = Q/P = 220\,000/25 = 8800\,\text{s} = 2{,}44\,\text{h}$; answers.py gives 2,444. The figure's data agree with the task: $2100 \cdot 0{,}60 \cdot 16 + 334\,000 \cdot 0{,}60 = 20{,}2 + 200{,}4 = 220{,}6\,\text{kJ}$ (2,45 h, inside tolerance 0,03), and the solution's independent check says so.
- L2-10: constant 25 W through the walls is stated as a task condition; the read point (220 kJ; 0 °C) is a grid crossing; the J and h conversions are shown; two figures from 25 W.
- All three solutions are complete, solved in symbols first, with units carried; inside FY3 (lämpeneminen, olomuodon muutokset).
- Rest of the set unchanged since PASS; hash same at start and end.
