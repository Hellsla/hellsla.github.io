VERDICT: FAIL
CONTENT-HASH: b04a13ce486ff667

## Blocking
- [Major] L2-08 (7-16) task text (live render at 390 and 1280 px; open-exercises-L2-1280-*) — the four bullets "- Kappale A: …" are not rendered as a list: they run together in one paragraph ("… 50 cm³ - Kappale B: massa …"), so the data are hard to read and the dashes look like minus signs between values — it is the data the whole task rests on — fix: the exercise text renderer does not turn `\n- ` into a list; either support lists in exercise `text` or write the data as a small table / four short lines (separate paragraphs, e.g. "Kappale A: massa …" each after `\n\n`).
- [Major] solutions.md L2-08, Mallivastaus — the four `\dfrac{m}{V}` lines (ρ_A … ρ_D) are stacked with no line spacing: numerators touch the denominator above ("50 cm³" struck through by the next fraction, 360 g over 400 cm³ cramped) at 390 and 1280 px — clearly poor readability — fix: put each ρ in its own paragraph/row (blank line between) or use inline `\tfrac`, keeping the unit with the number.

## Polish
- [Minor] solutions.md L2-08 — the closing sentences (order, mass vs density, significant figures) are one dense block after the fractions; split after "B, D, A, C."
- [Minor] L2-08 Annettu — "0,36 kg, 0,40 dm³" without "B:" mixes the symbols with plain labels; "B: m = …, V = …" like A.

## Checked
- Hash at start and end b04a13ce486ff667. Delta: opened open-exercises-L3 captures for layout survival and my own live renders of L2-08 at 390 and 1280 px (ordering task, answer card, solution card); paragraph splits of L2-07 and L3-04 are clean. Ordering select rows are usable at 390 px.

## Scores
illustrations 4 · typography 2 · Finnish 4 · accessibility 4
