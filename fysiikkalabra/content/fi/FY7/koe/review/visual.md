VERDICT: FAIL
CONTENT-HASH: f09b1fd9dac7accf

## Blocking
- [Major] content/fi/FY7/koe/solutions.md:306 (task 6 c Sijoitus; own captures FY7-koe-390-s1, FY7-koe-1280-s1) — "säästö" is broken inside its parentheses (`= (6912 MWh` / `− 228,5 MWh)`) and the last row `·50 €/MWh = 334 200 €` is flush left, outside the column of the `=`, with the result on a continuation row — misaligned, hard to read on a phone — break as `&= (6912\,\text{MWh} - 228{,}5\,\text{MWh}) \\ &\quad \cdot 50\,\text{€/MWh} \\ &= 334\,200\,\text{€}`.
- [Major] content/fi/FY7/koe/solutions.md:122 (task 2 b Sijoitus) — the block ends at `· 1,81 · 10⁻⁵ m²/V` and the result `= 1,16 · 10⁻¹¹ T²m²/V` follows outside it as inline text in a larger size, at both widths — the chain's result is detached from the chain — make it the block's third row.

## Polish
- [Minor] task 6 c — "säästö" and "takaisinmaksuaika" chains begin with a bare `=` after a word; the latter inline fraction is larger than the chains around it.
- [Minor] carried: fig-3 / fig-12 small markers, fig-6 tick numbers, task 2 b unit fraction.

## Checked
- own captures of every aligned block of the opened solutions at 390 and 1280 px (preview page at this hash, /tmp/claude-0/-home-user-hellsla-github-io/97f9a470-9f3f-5d71-b718-20679448b3a1/scratchpad/vis_b916/shots/FY7-koe-390-s1, FY7-koe-1280-s1, koe-k7-390.png): all five re-broken blocks (B²k, the two MWh products, säästö, the square root). The MWh products and the root are clean at both widths.
- Overflow of every formula measured at 360 and 390 px with all boxes open: none (the task 7 table reads in full).
- Figures and the rest of the page: not re-opened; unchanged since my full review of the previous version.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
