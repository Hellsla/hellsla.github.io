VERDICT: PASS
CONTENT-HASH: 59f8c6d98072df03

## Blocking
(none)

## Fixed
- none needed

## Polish
- The lesson figures and the simulation draw their own symbols from shared code (lessons/FY3/fy3-11/figures.py, sim.js): they show $W_\text{k}$ (and $E_\text{s}$ in the heat-pump figure label) while the English text uses $W_\text{g}$ / $E_\text{el}$. Not a translation file and meaning is unambiguous from the figure captions and the text; suggest letting the shared code take the symbols from the language.

## Checked
Full translation review (English) of lesson.md, inquiry.json, exit-ticket.json, figures.json and meta.json against the reviewed Finnish. Script comparison of all numbers and inline LaTeX: every value, unit and answer equals the Finnish (worked example 38.0 % / 310 MW and 88.0 % / 60 MW; $W = p\Delta V$; $\Delta U = Q - W_\text{g}$ sign convention and $W = -W_\text{g}$ kept). Symbol subscripts translated consistently in text, inquiry and solutions. Physics statements (second law, cogeneration, heat pump COP can exceed 1, no work without volume change) agree with the Finnish. No Finnish words left. check_i18n 0 errors.
