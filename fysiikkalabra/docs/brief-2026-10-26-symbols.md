# Brief 2026-10-26 (2): symbols as maths in the activity texts

The teacher's rule (CLAUDE.md "Lesson form", NOTES.md §1): a quantity symbol, a formula or a symbol pair named in the
student's text is inline maths, so the page never shows one symbol in two typefaces. `lesson.md` already follows it;
this pass does the same for the activity texts of one lesson `<id>` (work in `fysiikkalabra/`).

**Files:** `inquiry.json`, `exercises.json`, `exit-ticket.json` of the lesson. Every student-visible string: `title`,
`text`, `intro`, `prompt`, `options`/`choices` text, `feedback`, `hints`, `solution`, `model`, `criteria`, `answer`
texts, `howto`/`calc` boxes, table cells in markdown tables.

**Rule:**
- A symbol or formula in prose goes in `$...$`: "T:hen" → "$T$:hen", "(V, p)-kuvaaja" → "$(V, p)$-kuvaaja",
  "1/V:n funktiona" → "$1/V$:n funktiona", "p₁V₁ = p₂V₂" → "$p_1V_1 = p_2V_2$", "ΔT" → "$\\Delta T$", "θ" →
  "$\\theta$", "P = UAΔT" → "$P = UA\\Delta T$", "n = pV/(RT)" → "$n = \\dfrac{pV}{RT}$", "R = 8,31 J/(mol·K)" →
  "$R = 8{,}31\\,\\tfrac{\\text{J}}{\\text{mol}\\cdot\\text{K}}$", "10¹² J" → "$10^{12}\\,\\text{J}$".
- A symbol given a value inside a formula takes its unit inside the maths (`$m = 10\\,\\text{kg}$`). A number with a
  unit alone in plain prose stays as it is ("98 N painoista reppua", "20 m").
- Markdown table headers: "| t (s) | x (m) |" → "| $t$ (s) | $x$ (m) |".
- Finnish case endings after maths: "$T$:hen", "$V$:n".
- Decimal comma `{,}`, `\\cdot`, `\\Delta`, Greek as commands, subscripts `T_\\text{alku}` for word subscripts.
- In JSON a backslash is written twice (`"$\\Delta T$"`). Keep the file valid JSON (`python3 -m json.tool` must pass).
- Change nothing else: no wording, no numbers, no ids, no answer values, no SVG inside texts (already done), not the
  `names`/`measure` labels of experiments (the build renders those). Do not wrap words in maths.

**Do not touch**: `lesson.md`, `figures.py`, `solutions.md`, `sim.js`, `answers.py`, `review/`, `scripts/`,
`templates/`, `NOTES.md`, `CLAUDE.md`, other lessons.

**Finish**: `python3 scripts/check_lesson.py <id>` (or at least `python3 scripts/lint_lesson.py <id>`,
`python3 scripts/check_latex.py content/<course>/<id>` and `python3 scripts/test_inquiry.py <id>` if it exists) all
pass; then `python3 scripts/build.py <id>` and check one changed passage renders (no red KaTeX error) with
`python3 scripts/check_latex.py`. Do not commit. Report in at most 80 words: how many strings changed, anything left.
