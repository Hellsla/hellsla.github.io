VERDICT: FAIL
CONTENT-HASH: 60603fd33fb68666

## Blocking
- [Major] fy7-5-L2-08 (5-17) text and solution — the new English text uses the Finnish decimal comma ($0{,}40\,\text{s}$, $5{,}0\,\text{mWb}$, $4{,}0\,\text{V}$, $0{,}020\,\text{V}$, "0–0,40 s") while the rest of the English set and the figure's own ticks (0.2, 0.4) use the decimal point — inconsistent in the same task and wrong for the language — change every `{,}` in this exercise's text and solution to `.`.
- [Major] fy7-5/flux-task-2 — the tick labels 0.2, 0.4, 0.6, 0.8 sit on the zero axis inside the plot, and the green line crosses straight through the label "0.2" (struck through at 1280 px) — a line running over a label breaks the graph rule and makes the first reading harder — put the time axis and its labels at the bottom of the plot (or draw the labels below the axis at the zero line), keeping the line clear of every label.

## Polish
- [Minor] fy7-5-L2-08 solution — the subscript "ka" in $|e_\text{ka}|$ is the Finnish abbreviation, unexplained in English — use $|e_\text{avg}|$ (or just $|e|$ with "average" in the text).
- [Minor] fy7-5/flux-task-2 — the y-axis labels 5 4 3 2 1 and −1 −2 −3 are crowded and have no 0 beside the axis; label every second gridline, or set the zero at the axis crossing.

## Checked
- fy7-5-open-exercises-L2-1280-10, -11 (en): task 5-17 with the flux graph (axis titles with units, green piecewise-linear line), answer field "4,0 V", opened solution and reasonableness block.
- Typography otherwise fine: units upright with thin space, aligned chains, no red KaTeX, no overflow. The other exercises are unchanged and were not re-reviewed.

## Scores
illustrations 3 · typography 4 · Finnish 3 · accessibility 4
