VERDICT: PASS
CONTENT-HASH: fddaf5eacf9edc15

## Blocking

## Polish
- check-1 (inquiry.json): the Finnish says "pallo ammutaan" (a ball shot from a bow); this translation says "arrow", which is physically right. The Finnish wording is the odd one and should be fixed there; the translation was left as is.

## Checked
- Compared lesson.md, figures.json (aria-labels, labels), inquiry.json (all activities, feedback, model answers, numbers), exit-ticket.json, meta.json and the sims.fy4-7 labels line by line with the Finnish: every step, number and justification kept, nothing added.
- Terms: kinetic, potential, mechanical, internal energy, conservative force, zero level, friction, air resistance; chapter names match courses.json; decimal point everywhere, LaTeX symbols, \overline{v}, \cdot.
- Opening illustration at 360, 768 and 1280 px: labels are only language-neutral LaTeX ($v$, $\tfrac{v}{2}$, $v=0$, $\tfrac14 h$, $\tfrac34 h$), no overflow, no Finnish; aria-label in English.
- check_i18n, check_latex (541 fragments) and figures.py --check --lang en are clean.
- Fixed: the experiment tables' column and lock labels (`names`) still said "ramppi" and "kitka" in English; now "ramp" and "friction". Reworded "Practise still" to "Practise some more".
