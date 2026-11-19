VERDICT: PASS
CONTENT-HASH: dc09b0ce9519b96f

## Blocking

## Polish
- lessons/FY7/fy7-10/answers.py:51–52 — the comment still says "slope k = 0,596 / 0,40 = 1,49 = n" and computes an unused `k`, while line 53 and the solution use n = 1,50 (carried) — drop the dead line or reword the comment.

## Checked
- Delta: four Kaava steps rewritten as aligned chains (solutions.md:65, 75, 116, 133; the packet's diff shows them with the aligned markup stripped, the file on disk has proper `aligned` rows), three paragraphs split, caption marker removed; no number, answer, Muunnokset or Sijoitus changed; hash identical at start and end.
- solutions.md:65: $n_1\sin\alpha_1 = n_2\sin\alpha_2 \Rightarrow n_2 = n_1\sin\alpha_1/\sin\alpha_2$; $n_2 = c/v \Rightarrow v = c/n_2$: correct.
- solutions.md:75: $t_\text{lasi} = d/v$, $t_\text{ilma} = d/c$, $v = c/n$, $\Delta t = nd/c - d/c = (n-1)d/c$: correct (normal incidence, path $d$, air $n = 1{,}00$ as the Periaate says).
- solutions.md:116: Snell with $n = c/v$ gives $(c/v_1)\sin\alpha_1 = (c/v_2)\sin\alpha_2 \Rightarrow \sin\alpha_2 = v_2\sin\alpha_1/v_1$: correct.
- solutions.md:133: same $f$, $\lambda = v/f$, $\lambda/\lambda_0 = v/v_0 = (c/n)/c = 1/n$ with air $v_0 \approx c$: correct.
- Paragraph splits (refraction model answer, apparent-depth Periaate and Vastaus): text identical, physics unchanged.
- Every chain's last symbolic form is the one the unchanged Sijoitus substitutes into.
