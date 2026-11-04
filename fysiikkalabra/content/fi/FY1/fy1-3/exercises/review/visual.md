VERDICT: PASS
CONTENT-HASH: 2d365219ba2e0aa3

## Blocking

## Polish
- [Minor] L3-04 Vastaus (open-exercises-L3-1280-4) — a stacked inline fraction sits in the sentence and the "=" is left stranded at a line end ("… on [fraction] =" / "0,03 s") — write the half-range as one inline chain `\tfrac{…}{2}` or move it to its own row.
- [Minor] L2-07 Vastaus (open-exercises-L2-1280-9) — the check `\dfrac{0{,}2}{13 \cdot 1{,}5} = 1{,}03\,\%` is a tall fraction inside a bracket in prose and spreads the line — use `\tfrac` or a colon division, as the Järkevyys line already does.
- [Minor] L3-05 task (open-exercises-L3-1280-5) — the pupil's quotation is run into the task paragraph and opens with a straight `"` — set it as its own quoted paragraph with ” ”; the question already stands last and bold.
- [Minor] L1-05 Vastaus (open-exercises-1280-6, top; not in this diff) — after the answer chip the sentence starts with a stranded "; virhe-arvio …" — drop the semicolon or begin with a word.
- [Minor] L2-05, L2-06, L3-04 tables — left-aligned and narrow, numbers not aligned by the decimal comma (known shared-component item).

## Checked
- Delta, captures current for this hash: open-exercises-1280-6 to -9 (L1-06 multiple choice on error types with misconception feedback, L1-07, L1-08); open-exercises-L2-1280-6 to -9 (L2-05 and L2-06 measurement tables, L2-07 estimate of N); open-exercises-L3-1280-4 to -6 (L3-04 outlier table, L3-05 interval comparison).
- Multiple choice: options are whole rows, feedback opens inside the card, change-once text clear. Tables have captions and LaTeX headers with units, decimal comma, equal decimals; `\bar{x}`, `\Delta`, `\pm`, `{}^\circ\text{C}` and `\text{g/cm}^3` render correctly; every number has its unit as maths; solutions follow principle, formula, substitution, result, Järkevyys; chains aligned in rows; no overflow or clipping.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
