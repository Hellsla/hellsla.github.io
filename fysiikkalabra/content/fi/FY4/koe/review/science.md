VERDICT: PASS
CONTENT-HASH: 9cc11d9de8effe6c

## Blocking

## Polish
- solutions.md (fy4-k7 b Järkevyys) — The figure draws a half sine (figures.py: `950 * sin(pi t / 9.0)`), so the exact area factor is $2/\pi = 0{,}637$. The area is then $5{,}44\,\text{m/s}$, which agrees with part a's $5{,}42\,\text{m/s}$. The rounded 0,64 gives 5,47, so "≈ 5,5, lähes sama" is honest as written. Optional fix: "noin $0{,}64$ (puolisinikaarelle $2/\pi$)".

## Checked
- Delta review (teacher 2026-11-16, economical): only the fy4-k7 b Järkevyys row was judged; the rest rests on my previous report (hash 570b93738d02c5c4, reflow carried in carry.tsv).
- I recomputed it: $0{,}64 \cdot 950\,\text{m/s}^2 \cdot 0{,}0090\,\text{s} = 5{,}47\,\text{m/s} \approx 5{,}5\,\text{m/s}$. Part a: $\sqrt{2 \cdot 9{,}81 \cdot 1{,}50} = 5{,}42\,\text{m/s}$. "lähes sama" is now correct, where the old "≈ 5,4, sama" misreported the product.
- The physics of the check is right: the area under the $(t, a)$ curve is the change in speed, and the head form stops without bouncing.
- No answer, rubric criterion or point changed.
- Content hash was the same at the start and at the end.
