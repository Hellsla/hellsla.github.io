VERDICT: PASS
CONTENT-HASH: 769fc33a98f38f23

## Blocking
(none left; see Fixed)

## Fixed
- content/en/FY3/fy3-11/lesson.md (Refrigerator and heat pump) — "three times the power of the electric power it uses" was clumsy and could be read as comparing the wrong powers → "three times as much heating power as the electric power it uses"
- content/en/FY3/fy3-11/meta.json glossary — "yhteistuotanto" and "lauhdevoimalaitos" were left in Finnish → "combined heat and power", "condensing power plant"

## Polish
- The experiment tables show the select value "sama paine" / "jäähdytys ensin" in Finnish in the setup line and rows, because the Finnish inquiry.json has no `values` map ({paluu: {...}}). A `values` map in en is refused by check_i18n (keys differ from Finnish). Add it to the Finnish source first, then en can show "at the same pressure" / "cool first".

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json (all activities, hints, feedback, solutions, experiment names/intros), exit-ticket.json, meta.json, figures.json and the sim labels (lang/en.json sims.fy3-11). Science: meaning, signs (W_g, Delta U = Q - W_g), numbers, units, terms, chapter titles and decimal sign compared with the Finnish.
