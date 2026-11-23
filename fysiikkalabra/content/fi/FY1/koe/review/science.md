VERDICT: PASS
CONTENT-HASH: 26b1711cf5753b06
Mode: delta (round 2; change under review: fy1-k7 c Kaava step, the aligned block split into rows and the remark on $\Delta d$ moved to its own line; previous PASS 823f6d310477ff2b)

## Blocking
- none

## Polish
- fy1-k7 c: the line "Tässä $\Delta d$ on lukeman epävarmuus." is followed by `**Muunnokset:**` without a blank line, so the two may render as one paragraph (presentation, the visual reviewer's call).
- Carried over from round 1, unchanged: k5 c has a number in the symbolic row ($2 \cdot 0{,}5\,\text{ml}$); k7 d calls the nominal $80\,\text{g/m}^2$ "tarkka arvo" (better: "oletetaan tarkaksi"); k6 b says "noin $1\,\%$" for $1{,}4\,\%$ (C).

## Checked
- Diff (`git diff HEAD~1`, commit 2a2efbe46f): only the k7 c Kaava step changed. The rows $d_1 = \frac{d-0}{N-0}$, $= \frac{d}{N}$ and $\Delta d_1 = \frac{\Delta d}{N}$ are the same equations as before, still symbolic before substitution and algebraically right. The slope through the origin is the thickness per sheet, as the Periaate step says.
- The definition of $\Delta d$ as the reading's uncertainty now sits in a sentence after the block. It still agrees with the Sijoitus ($1\,\text{mm}/500$) and with the Vastaus.
- Recomputed: $51\,\text{mm}/500 = 0{,}102\,\text{mm} = 102\,\mu\text{m}$; $1\,\text{mm}/500 = 2\,\mu\text{m}$; $0{,}080/(1{,}02\cdot10^{-4}) = 784\,\text{kg/m}^3$. These match answers.py (`fy1-k7-c-d` 102, `fy1-k7-c-dx` 2, `fy1-k7-d` 784).
- Nothing else changed: no other task, rubric, figure or answers.py output differs from round 1, so the round 1 checks still hold.
- practice.py check: OK. The hash was 26b1711cf5753b06 both at the start and at the end.
