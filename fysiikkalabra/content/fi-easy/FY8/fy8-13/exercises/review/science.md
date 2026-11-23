VERDICT: PASS
CONTENT-HASH: 7c16a8e1ffdd91f3
SCOPE: delta md-paragraphs,numbers,reflow,typography from eeccff04aba30fbe base 64d4935

## Blocking

## Polish
- exercises/solutions.md:93, 115, 177, 218, 406 — each display block opens on the same line as "**Kaava:**" ("**Kaava:** $$\begin{aligned} …"). The physics is right. Whether it renders as a display block is for the visual reviewer to look at.

## Checked
- Hash 7c16a8e1ffdd91f3 (`reviews.py hash fy8-13 --exercises --lang fi-easy`) at the start and the end.
- `git diff origin/main`: only solutions.md changed, and every removed line is a `**Kaava:**` line. Answers, answers.py, tolerances and the Sijoitus steps are unchanged.
- Dose chain $D_\text{T} = E/m$, $H_\text{T} = w_\text{R}D_\text{T}$, $H_\text{E} = w_\text{T}H_\text{T}$ gives $w_\text{T}w_\text{R}E/m$: correct.
- Inverse-square time $t = H/\dot H_2 = (H/\dot H_1)(r_2/r_1)^2$: correct.
- Distance-versus-shield comparison: $H_\text{A}-H_\text{B} = (\dot H_\text{A}-\dot H_\text{B})t$ gives the earlier bracket form.
- Radon plus gamma: $H_\text{E} = w_\text{T}w_{\text{R},\alpha}D_\text{keuhkot} + w_{\text{R},\gamma}D_\gamma$ is the same as before, now built from $H_\text{T}$ and the two parts.
- Combined shield and distance: $t = (H/\dot H_1)(r_2/r_1)^2\,2^{d/d_{1/2}}$ is the same as $H/\dot H$. I checked this numerically. The factors commute, so applying the shield before the distance is valid.
