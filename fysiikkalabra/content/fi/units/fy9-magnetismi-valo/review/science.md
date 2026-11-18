VERDICT: FAIL
CONTENT-HASH: 1197865df5c60483
SCOPE: delta: new Sovella tasks s8 (Laserkoe akryylilevyllä) and s9 (Käämin vuo ja induktiovirta) and the changed intro; s1-s7 untouched, not re-judged.

## Blocking
- s9, Yleisiä virheitä, line 2 (A, quantitative): "$\text{mWb}$ jää muuntamatta yksiköksi $\text{Wb}$, jolloin jännite on tuhannesosa oikeasta" is the wrong way round. If $8{,}0$ is used as webers, $120 \cdot 8{,}0 / 0{,}40 = 2400\,\text{V}$, which is a thousand times the right value. Fix: "jännite on tuhatkertainen oikeaan verrattuna ($2400\,\text{V}$)".

## Polish
- s8, Yleisiä virheitä, line 1: the inverted slope from the quoted line points is $0{,}30 : 0{,}45 \approx 0{,}67$. The text has $0{,}30 : 0{,}44 = 0{,}68$, which is one point's own ratio, not the slope "väärin päin". The conclusion ($n < 1$) still holds.
- s9 figure fy7-5/flux-task-2: the alt text says "käämin läpi kulkeva magneettivuo", but the task text says "yhden kierroksen läpi kulkeva". Read alone, the alt text could mean $N\Phi$. This is the owner figure's text (fy7-5 figures.py). Flagged only because the teacher's rule asks the names to match.
- s9 b, c (C, no finding): the coil's self-inductance is ignored, so the current jumps at the corners. That suits the level.

## Checked
- `units.py hash` gave 1197865df5c60483 at the start and at the end. `practice.py check` OK.
- I wrote one script with my own formulas, beside answers.py output:
  - s8: the refit from fy7-10 figures.py (FIT_A1/A2) gives $A = 1{,}4895$, $B = -0{,}0041$, so the line is at $0{,}443$ at $0{,}30$ and $0{,}890$ at $0{,}60$. The readings $(0{,}30; 0{,}44)$ and $(0{,}60; 0{,}89)$ are right. $n = 1{,}5$, $v = 2{,}0 \cdot 10^8\,\text{m/s}$, $t = 0{,}75\,\text{ns}$ (in air $0{,}50\,\text{ns}$), $\alpha_\text{r} = 41{,}8^\circ \approx 42^\circ$, and $42{,}2^\circ$ with $n = 1{,}49$. The tolerances (3 %, 2 %) accept both a reading of $1{,}49$ and the rounding to $42^\circ$.
  - s9: $\pm 20$ and $15\,\text{mWb/s}$, $2{,}4$ and $1{,}8\,\text{V}$, $0{,}72$ and $0{,}405\,\text{W}$, $W = 0{,}288 + 0{,}081 = 0{,}369 \approx 0{,}37\,\text{J}$, $I = 0{,}30$ and $0{,}225\,\text{A}$, flux zero at $t = 0{,}25\,\text{s}$. All agree with answers.py.
- Physics:
  - Snell's law with $n_1 = 1{,}00$ and the slope as $n$: right.
  - The origin argument from zero incidence and $n = c/v$: right.
  - TIR only from the denser medium, with the refraction angle $90^\circ$ at the critical angle: right.
  - $\lvert e \rvert = N\lvert\Delta\Phi\rvert/\Delta t$: right.
  - Lenz directions: first interval induced field $+$ and $e > 0$, last interval $-$ and $e < 0$: right.
  - The sign of the flux does not change the current; the rate does: right.
  - "Muuttuu sisäenergiaksi" follows P1.
- Scope: FY7 (fy7-5, fy7-6, fy7-10, fy7-12) plus fy1-4 and fy6-6.
- Rubrics: criterion points equal part points (s8 4+4+4+3, s9 4+4+4). Each criterion asks only what its part asks. The Hyväksytään myös lines are right.
- Data: invented and labelled as such. The rounding reasons match the data (two significant figures).
- Task texts give the axes and data. They do not name the slope method or the formulas.
- Intro: "Yhdeksän" matches 9 tasks, and the seventh (s7) is the source-based task.
