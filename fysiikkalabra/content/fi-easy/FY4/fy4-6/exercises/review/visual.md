VERDICT: PASS
CONTENT-HASH: 3dd1d151602926c5

## Blocking
None.

## Polish
- [Minor] Solution L1-07, Vastaus (open-exercises-1280-8) — "vähintään 2,3 · 10² N eli 230 N" gives the same value twice and begins with a lowercase word. Fix: "Voima on vähintään $230\,\text{N}$ (kaksi merkitsevää numeroa: $2{,}3 \cdot 10^2\,\text{N}$)."
- [Minor] L1-07 Voimakuvio — the rest friction at the limit case is labelled F_μ, while L1-06 uses F_μ0. Use F_μ0 for rest friction in the figure and its text. The figure is outside this diff, so I did not judge it as a blocker.
- [Minor] L2-04 Järkevyys/Vastaus — the range "0,41-0,43" in L2-05 (graph task, solution) uses a hyphen. Use an en dash, "0,41–0,43".
- [Minor] L2-05 (graph task, 8-14) data table — the caption is squeezed into the narrow first column and wraps over four lines. It would be better if the table box took the caption's full width.

## Checked (delta 2026-11-15, work queue 8m)
- Hash matches the packet (3dd1d151602926c5) at the start and the end. The captures were stale, so I regenerated them with `screenshot.py fy4-6 --lang fi-easy`.
- Opened at 1280 px with every solution open: Level 1 parts 1, 2, 3, 6, 7 and 8 (tasks 8-1, 8-2, 8-3, 8-6, 8-7 and its solution) and Level 2 parts 6 and 7 (L2-04, and the L2 graph task with its data table).
- Confirmed in the captures: liukukitka and liukukitkakerroin are used consistently. The lähtökitka wording in the concept task 8-6 (choices and feedback) is fluent and consistent with the glossary. L1-07 shows 2,3·10² N as the checked answer. Formulas, units and decimal commas render correctly, and nothing is clipped or overflowing.
- Not opened: Level 2 parts 1–5 and 8–14, Level 3, the contact sheets, and the 390 px captures. The remaining diff lines are the same word-for-word term swaps, judged from the diff text only.
- `figures.json` was changed, but no figure appears in the exercises' diff beyond the voimakuvio figures seen in the captures. Those were drawn correctly (force red, velocity blue, acceleration orange).

(Report text of the visual-editorial-reviewer run, saved by the orchestrator because the agent's report did not reach the file.)

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
