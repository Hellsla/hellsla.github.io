VERDICT: FAIL
CONTENT-HASH: ed31b144d397cb3e

## Blocking
1. [Major] `power` figure (`figures.py`; capture `stage-selita-390-1`, my own 2× capture). At 390 the figure is 358 px wide (measured), so the 22-unit labels are 13.1 px. This affects the axis ticks 0–500, $P\ (\text{MW})$, $\alpha\text{: }100$ and the grey captions "into plasma", "made in plasma" and "electricity in". The subscripts "heating" and "fusion" come out at about 9 px. The house rule is at least 14 px at 390, and this chart is the evidence for the pair discussion and for prediction 2. Fix: raise every label to at least 24 units, 26 to match `schedule` in the sister unit, which gives 15.5 px. Give the grey captions more contrast than `#6b7480` at that size, or move them into one line under the chart. If it is still crowded, make the viewBox narrower (about 520 wide) so that the scale goes up.

## Polish
1. [Minor] `power` aria-label: it says "A note says that ITER produces no electricity", but the figure draws no such note. Fix: add the note (for example $\text{ITER: no electricity out}$ beside the grid bar), or remove the sentence from the aria-label.
2. [Minor] Worked example, step 1 at 390: the inline equalities break after "=" ("$P_\text{heating} =$" / "$50\ \text{MW}$", and the same for $E_\text{total}$). Fix: wrap each equality in braces, `${P_\text{heating} = 50\ \text{MW}}$`.
3. [Minor] Worked example, Reasonableness: "The other $401\ \text{MW}$" uses a precision the answer has just rejected ($P_\alpha \approx 99\ \text{MW}$, two significant figures), and the figure says 400. Fix: "about $400\ \text{MW}$".
4. [Minor] `tritium` solution, **Answer**. The page boxes $m \approx 0.36\ \text{g}$ and starts the next line with the fragment "Of tritium in one 400-second pulse, …". Fix: "**Answer:** $m \approx 0.36\ \text{g}$. This is the tritium burned in one $400$-second pulse; two significant figures, because …". In its Substitution block, align the `= 7.093…` line under the first "=" (`N &= …`) as the conversion block does.
5. [Minor] Text and criteria. "real D–T fuel" breaks at the en dash at 390: use U+2011 or `$\text{D–T}$`. The `pair-gain` criterion "needs more than $Q > 1$" should read "needs $Q$ far above 1". The criteria write "300 MW", "500 MW" and "4 K" as plain text, while the prompts use LaTeX.

## Checked
- Fresh build and captures for this hash: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets 1–5.
- The `power` figure at 390 (2× capture, label sizes measured in the browser) and at 1280 (22–24 px, fine).
- The `iter` explorer and the parts quiz over HTTP at 390 and 1280: Divertor selected, panel with LaTeX key number and sources.
- The worked example with every step revealed (my capture), and the tritium hints and solution.
- Match and say components. The hero has no text.
- No `.katex-error`, no raw `$` and no overflow.

## Shared issues
- `fx/iter.js`: the markers (r = 11 in a 640-wide drawing) are about 11 px across at 390, with numbers of about 7 px. They are hard to read and to tap. Scale r and the font to the drawing width, at least 22 units at 390.
- `fx/iter.js`: on a phone, the panel of a part tapped in the drawing appears below the 13-item list, about 800 px further down. Scroll it into view, or show it right under the drawing.
- Template: a solution step that starts with a formula is boxed, and the rest becomes a capitalised fragment (see Polish 4).

## Scores
illustrations 3 · typography 4 · English/French 4 · accessibility 3
