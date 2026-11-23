VERDICT: PASS
CONTENT-HASH: 61fda8c0ee607a52
Mode: full, en (round 1; change under review: Kaava steps of fy1-s1 b and fy1-s2 b as aligned rows from the basic equations, work queue 8g)

## Blocking
- none

## Polish
- fy1-s1 b: **Given** names the floor points as $t = 0{,}4$–$2{,}0\,\text{s}$, answers.py fits $t \geq 0{,}6\,\text{s}$. Both give $0{,}80\,\text{m/s}$ (0,7998 vs 0,7993) and the rubric accepts either, so there is no error, only two different choices.

## Checked
- Recomputed in my own script from the task data: a least-squares fit for $t \geq 0{,}4$ and $t \geq 0{,}6\,\text{s}$ gives $k = 0{,}800 / 0{,}799\,\text{m/s}$ and $s_0 = -0{,}161 / -0{,}160\,\text{m}$. The largest residual is $1{,}9\,\text{mm}$ (under one pixel of $2{,}5\,\text{mm}$, as the text says). Extrapolated to 10 s the line gives $7{,}83\,\text{m}$. The ramp points lie above the line ($+161$ and $+39\,\text{mm}$). The floor steps are $156$–$163\,\text{mm}$ per $0{,}20\,\text{s}$, so the reasonableness check of $0{,}80\,\text{m/s}$ holds. The values read off the line, $(0{,}6;\,0{,}319)$ and $(2{,}0;\,1{,}439)$, agree with $0{,}32$ and $1{,}44\,\text{m}$.
- New Kaava fy1-s1 b: $v = \Delta s/\Delta t = (s_2 - s_1)/(t_2 - t_1)$ is the slope of uniform motion $s = s_0 + vt$, stated as the principle. It is symbolic before any substitution and correct.
- New Kaava fy1-s2 b: the mean and the half range are symbolic. Sums $11{,}85$ and $12{,}00\,\text{s}$, means $2{,}37$ and $2{,}40\,\text{s}$, half ranges $0{,}08$ and $0{,}07\,\text{s}$, difference $0{,}03\,\text{s}$. The standard errors of the means are $0{,}031$ and $0{,}025\,\text{s}$ ("noin $0{,}03\,\text{s}$", correct). The original report's difference is $0{,}328\,\text{s}$.
- Physics and scope: uniform motion only, no forces. The negative intercept is explained correctly (slower on the ramp). The ramp-mass investigation draws no claim about mass independence beyond the tested conditions. The rubric criteria ask only what the parts ask. Points add up: 3+3+3+3, 8+4+3, 14.
- Units and significant figures: $0{,}80\,\text{m/s}$ is justified by an uncertainty under 1 % over $1{,}12\,\text{m}$. Times are given to hundredths, as measured.
- No invented data is presented as measured: both tasks carry `source: example` with a note.
- en: every number of tasks.json and solutions.md equals the Finnish version (decimal separators normalised; the only differences are figure label coordinates).
