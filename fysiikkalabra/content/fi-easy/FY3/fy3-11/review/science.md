VERDICT: PASS
CONTENT-HASH: 48c9187745f733f6

## Blocking
(none left; see Fixed)

## Fixed
- content/fi-easy/FY3/fy3-11/figures.json — values were shifted: the label "leveys kuvaa tehoa" held the whole description of the (V, p) graph, and the description's own key held the dense Finnish original → label restored to "leveys kuvaa tehoa", the (V, p) description now simplified under its own key; figures redrawn (figures.py fy3-11 --lang fi-easy)

## Polish
- Same Finnish-source gap as in en: no `values` map for the select "paluu"; harmless in fi-easy since the words are Finnish.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json (all activities, hints, feedback, solutions, experiment names/intros), exit-ticket.json, meta.json, figures.json and the sim labels (lang/fi-easy.json sims.fy3-11). Science: meaning, signs (W_g, Delta U = Q - W_g), numbers, units, terms, chapter titles and decimal sign compared with the Finnish.
