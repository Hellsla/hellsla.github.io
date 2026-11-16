VERDICT: FAIL
CONTENT-HASH: c9c128908c01d05e

## Blocking
- [Major] content/fi/FY7/fy7-13/exercises/exercises.json:202 (fy7-13-L2-06 task text; own captures fy7-13-390-s2, fy7-13-1280-s1) — the quoted solution now ends `…\end{aligned}$$.”`, and the full stop with the closing quotation mark stands alone on its own line under the formula at both widths — a stray `.”` line in the task every student reads; the build sets a mark inside the last row only when a space follows it — put it inside the formula's last row (`&= 562\,\text{nm}\text{.”}`) or let `mathlayout.with_punct` take a closing quote too.
- [Major] content/fi/FY7/fy7-13/exercises/solutions.md:163 (fy7-13-L2-06 Sijoitus; fy7-13-390-s2) — "ja virhe" block: on a phone the fraction row is centred with its `=` and the continuation `·100 % = 5,53 %` is flush left, outside the column, with the result on the continuation row — misaligned rows, the result does not read as the chain's end — break as `&= \dfrac{…}{…} \\ &\quad \cdot 100\,\% \\ &= 5{,}53\,\%`.

## Polish
- [Minor] same block starts with a bare `=` after the word "virhe" (as before the change).

## Checked
- own captures of every aligned block of the opened solutions at 390 and 1280 px (preview page at this hash, /tmp/claude-0/-home-user-hellsla-github-io/97f9a470-9f3f-5d71-b718-20679448b3a1/scratchpad/vis_b916/shots/fy7-13-390-s1…s3, fy7-13-1280-s1…s2): all 17 aligned blocks (L1-02, L1-04, L1-09, L2-01, L2-03, L2-04, L2-06, L2-08, L2-09, L2-10). The others are clean: d = 1 · 10⁻³ m : 600 chains, x₂ : x₁, x₁ = L tan θ₁ with the · continuation.
- No formula of the exercises overflows its box at 360 or 390 px (measured in the browser, every solution open).

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
