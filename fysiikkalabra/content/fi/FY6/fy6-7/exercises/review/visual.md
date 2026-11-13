VERDICT: FAIL
CONTENT-HASH: cf2465df9ace3a5d

## Blocking
- [Major] fy6-7/dryer (task 7-18, lessons/FY6/fy6-7/figures.py `dryer`) — the label $\text{jäähdytys}$ is centred at 1,75 h, so its first letter sits on the vertical drop at 1,5 h and the word lies on the 0,4 kW gridline; NOTES §3 says a line never runs over a label — a new, unapproved graph must be clean in print and on a phone — move the label clear of the line (for example `ax.X(1.75) + 20`, `ax.Y(0.2) - 40`, or left-aligned at `ax.X(1.5) + 12`) and check it at 390 px.

## Polish
- [Minor] fy6-7/dryer — y tick labels read "2,4 · 2 · 1,6 …": the "2" should be "2,0" so the decimals match; `yfmt` drops the zero.
- [Minor] fy6-7-L2-08 Vastaus — "luetaan $0{,}4\,\text{kW}$:n … ruudukkoviivoilta" but the last step, $0{,}2\,\text{kW}$, lies midway between gridlines; say "viivojen välistä puolen ruudun tarkkuudella" or draw it on a line.
- [Minor] fy6-7-L1-10 Vastaus — "Vastaus kelpaa, kun se on noin $\pm 4\,\%$ sisällä" talks about the checker, not the physics; drop it. Sijoitus also leaves a lone $E$ on its first row.

## Checked
- open-exercises-1280-10 (task 7-10 solution), open-exercises-L2-1280-10 and -11 (task 7-18: dryer graph with its solution): the figure was zoomed at 2x to confirm the overlap; maths, units, case endings ("$0{,}4\,\text{kW}$:n") and Finnish are otherwise clean. Description of the figure matches it and does not give the answer away.

## Scores
illustrations 3 · typography 4 · Finnish 5 · accessibility 5
