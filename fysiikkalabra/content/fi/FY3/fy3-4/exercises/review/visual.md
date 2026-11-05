VERDICT: FAIL
CONTENT-HASH: 7aab3f782db93840
ROUND: 1

## Blocking
- [Major] fy3-4-L1-09 solution, Mallivastaus, the line "$\Delta p = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 1000\,\text{m} = 9{,}81 \cdot 10^{6}\,\text{Pa}$" — it has only one `=`, so mathlayout does not break it; at 390 px it is 406 px wide in a 304 px box, the result $9{,}81 \cdot 10^{6}\,\text{Pa}$ is cut off at the card edge and the page gets a horizontal overflow (document scrollWidth 449 at both 390 and 360, measured in Playwright; the packet's layout check did not catch it) — the answer is unreadable on a phone — give the substitution and the result as two chain steps so that the row layout applies, e.g. a line "$\Delta p = \rho g h$", then "$\Delta p = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 1000\,\text{m}$", then "$\Delta p = 9{,}81 \cdot 10^{6}\,\text{Pa}$", or write the units with the numbers shorter (`\text{kg/m}^3`).

## Polish
- [Minor] fy3-4-L1-09 Mallivastaus — the order principle, symbolic equation, substitution, result is not followed: the symbolic $\Delta p = \rho g h$ stands only in Periaate; show it as the first row.
- [Minor] The last sentence of the solution packs three distractor remarks and an estimate into one paragraph; split it into two.

## Checked
- Rendered fy3-4-L1-09 at 390 px with feedback and solution open (two tiles) and measured overflow at 390 and 360: the finding above. Options $10^{5}$–$10^{8}\,\text{Pa}$ and their feedback read well, the quantities are in KaTeX, correct option not identifiable by form (magnitudes in order, similar length), distractors catch the km and metre conversion mistakes.
- fy3-4-L3-02 (text split into three paragraphs) rendered at 390 px: reads clearly, no overflow, input row intact.
- Text only: the rest of the set (unchanged).

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 3
