VERDICT: PASS
CONTENT-HASH: 08fbb7bd52ff00b7

## Blocking
(none)

## Polish
- [Minor] malli-laatikko model figure — the figure itself is shown only after the tick "Olen piirtänyt voimakuvion paperille" and "Näytä mallikuvio", so no capture of it exists; the diff changes only its description text (liikekitka → liukukitka), the drawing is unchanged, so this did not block. Add a capture of the unlocked model figure to the screenshot set.

## Checked
- Delta only: "liikekitka" → "liukukitka" in the task prompt, rubric, model answer, and the figure's description (figures.json, figure source), a wording change with no numbers or symbols changed.
- review/shots/fy5-8-open-tarkista-1280-3.png: Selitystehtävä 4 "Piirrä itse" shows "Lattian liukukitka laatikkoon on 18 N" with LaTeX numbers and units, upright, no clipping; the tick, notes box and "Näytä mallikuvio ja arviointi" button lay out as before.
- review/shots/fy5-8-open-tarkista-1280-4.png: the following card and the self-assessment rows are intact.
- Not opened: the model figure (locked, no capture); the model answer text (hidden behind the lock), read from the diff: "liukukitka $\overline{F}_\mu$" correct and consistent with the glossary and the project rule.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
