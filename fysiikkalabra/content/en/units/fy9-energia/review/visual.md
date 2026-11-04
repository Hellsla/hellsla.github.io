VERDICT: FAIL
CONTENT-HASH: 44d6a17aa7d17ef6

Visual & editorial review of the English translation of fy9-energia. Preview preview/en/fy9-energia.html (python3 scripts/build.py fy9-energia), Playwright at 390 and 1280 px, all details opened and model answers shown.

## Blocking
1. unit.md, figure `kartta` (concept map): the three branch headings are still Finnish: **teho**, **hyötysuhde**, **energian lähde** (seen at both 390 and 1280 px). figures.py draws them as `\textbf{...}` (lessons/units/fy9-energia/figures.py line 116), and figlib.translate() only translates `\text{}`, `\mathrm{}` and `\textsf{}`, so figures.json cannot supply them and they are not reported as MISSING (check_i18n passes). Fix (shared, see below): add `textbf` to the regex in scripts/figlib.translate, add "teho": "power", "hyötysuhde": "efficiency", "energian lähde": "source of energy" to content/en/units/fy9-energia/figures.json and redraw (translate_kit.py apply / units.py figures).

## Shared issues
- scripts/figlib.py translate(): `\textbf{}` labels are neither translated nor listed as missing. The same pattern is in other FY9 units' concept maps (grep `textbf{` in content/en/units/*/unit.md shows Finnish heads such as "Newtonin lait", "aallot", "kondensaattori"), so every en and fi-easy unit with a concept map is affected.

## Checks done
- No horizontal scroll (scrollWidth = viewport at 390 and 1280); no KaTeX errors, no unrendered $...$; no table, svg or display formula wider than the viewport.
- Figures at 390 px: hero, Investigate bar chart, energy flow `ketju` (English labels, decimal points 0.90/0.45/0.98), the borrowed fy2-4 grid (English), and the task 3 model graph (English axes, 230 kWh, 12 kWh, k ≈ −4.9 kWh/°C) are legible. Aria-labels translated.
- LaTeX everywhere with \, before units; decimal point throughout, no {,} or comma decimals left; true minus in the graph.
- Tables (cottage devices, January data with "7 Jan" dates, island options) fit at 390 px.
- Solutions' `### Yleisiä virheitä` / `### Hyväksytään myös` headings are rendered as English headings by practice.py (lang key), as intended.

## Polish
2. figures.json, hero description: "steam rising from its chimney and cooling" -> "from its chimney and its cooling tower".
3. figures.json, task 3 graph description: coordinates "(−20 °C; 191 kWh)" use a Finnish-style semicolon; in English "(−20 °C, 191 kWh)" reads better in the description (keep the LaTeX unchanged).
4. figures.json, `ketju` description: "Energy flow diagram to scale of a condensing power plant" -> "A to-scale energy flow diagram of a condensing power plant".
