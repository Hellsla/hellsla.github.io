VERDICT: PASS
CONTENT-HASH: 1500ef8744b0673d
## Blocking

## Polish
- content/fi-easy/FY4/fy4-1/exercises/solutions.md:178-180 (L1, laskeva suora) — the new paragraph break separates "kuvaa vakionopeutta." from its contrast "Se ei kuvaa hidastuvaa liikettä.", so "Se" opens a paragraph with an unclear referent — keep the two sentences together and break before "Aika kasvaa aina".
- content/fi-easy/FY4/fy4-1/exercises/solutions.md:202-206 (L3-04 Järkevyys) — the new paragraph opens with "Siksi mittausten toistaminen ...", whose reason (systematic error) is in the previous paragraph — break before "Mittakaavavirhe on systemaattinen" instead.
- content/fi-easy/FY4/fy4-1/exercises/solutions.md:195 (L3-04 Kaava) — "Kaikki pituudet kasvavat samalla luvulla" reads as an addition; "kerrotaan samalla luvulla $k$" says what the Periaate says; the last result $t = (x - x_0)/v$ could be a display formula like the other sets' Kaava steps.
- content/fi-easy/FY4/fy4-1/exercises/solutions.md:212 (L3-05 Annettu) — gives $(0\,\text{s};\, 205\,\text{m})$ while the fit reads $203\,\text{m}$ (unchanged; fine as a fitted line, but a reader may see a mismatch) — say "taulukon piste" vs "suoran piste".

## Checked
- Delta only: the four Kaava rewrites and the paragraph splits; no number, answer, tolerance, task or id changed.
- L2-06: from $x_\text{A} = x_\text{B}$ to $(v_\text{A} - v_\text{B})\,t = x_{0\text{B}} - x_{0\text{A}}$ and $t = (x_{0\text{B}} - x_{0\text{A}})/(v_\text{A} - v_\text{B})$: algebra right, signs right; $19{,}0/3{,}3 = 5{,}8\,\text{s}$ recomputed.
- L3-04: $x = k\,x_\text{ohj}$, $v = k\,v_\text{ohj}$, $x_0 = k\,x_{0,\text{ohj}}$, $t = (x - x_0)/v$: consistent with the scale-error model; $k = 1{,}25$, $v = 0{,}80\,\text{m/s}$, $t = 7{,}0\,\text{s}$ recomputed.
- L3-05: $x_{0\text{R}} + v_\text{R}t = v_\text{P}t - v_\text{P}t_0$ rearranged correctly; $331/6{,}1 = 54\,\text{s}$, $x \approx 7{,}4 \cdot 10^2\,\text{m}$, the 3 % sensitivity claim recomputed (56 s vs 54 s).
- Each Kaava step now starts from the basic equations ($x = x_0 + vt$ for each body), derives the formula symbolically to the end, and Sijoitus substitutes into the last symbolic form.
- Paragraph splits change no claim; the physics of the split passages (systematic vs random error, extrapolation caveats) unchanged and right.
- Notation as in the brief ($x_0$, $v$, $\Delta x$, subscripts A/B, R/P).
- Captures opened: none (judged from the text and the packet).
