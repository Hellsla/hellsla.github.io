VERDICT: PASS
CONTENT-HASH: 8abc86d61268b96c

## Blocking
(none)

## Polish
- inquiry.json ennuste-1 / koe-1 — the sim's 25 % is a typed-in constant (the intro says so), so the experiment is a lookup and cannot refute the prediction; the one prediction the sim can test (ennuste-2, time independence) is optional, so on the core path the student meets time independence without predicting it — make ennuste-2 core, or state in ennuste-1 that the value is read from the table, not tested.
- inquiry.json koe-1 question — the prediction asks for the useful share, the task asks for the loss share (75 %) and leaves the last step to a sentence; ask for the efficiency directly or add "Mikä on hyötysuhde?" as the closing step.
- lesson.md "Hyötysuhde kertoo hyödyn osuuden" — one dense paragraph, and "Kun laitteen hyöty on muuta kuin lämpöä, hyötysuhde vaihtelee paljon: sähkömoottori ... mutta lamppu ja polttomoottori jäävät selvästi alle" is muddled; "Laitteiden hyötysuhteet vaihtelevat paljon:" repeats it. Split before the heater sentence and drop one of the two.
- inquiry.json tarkistus-3 criterion 4 — asks for a numeric example the question does not ask for; ask "Anna esimerkki luvuilla." in the prompt or drop the criterion.
- inquiry.json ennuste-1 hint — "Kuumenevatko auton moottori ja pakoputki ajossa?" nearly gives the 25 % option away together with the option "koska moottori kuumenee yhtä paljon kuin hehkulamppu"; fine, but the hint belongs behind a button.

## Checked
- Hook answered: lesson text and conclusion explain where the lamp's energy goes and how goodness is measured; goals (E and P definitions, energy conservation, Sankey) covered, nothing beyond FY2 scope (no chain, no Carnot).
- Figures (captures fig-1, fig-2 at 390 px): legible, same scale, colour paired with labels; descriptions carry the data.
- Worked example: seven stages, one step each, units, sig figs and sanity check.
- Option feedback repairs misconceptions (kertaus, ennuste, Etsi virhe, check-patteri); no letter references.
- Sim at 390 px: controls and readout clear; model assumptions stated in "Mallin oletukset".
- Finnish read through: no errors found.
- Workload fits one lesson.
- Delta 01da3ae6 (ennuste-2 option texts): lengths now similar, each still a plausible misconception, nothing gives the answer away. Hash 8abc86d61268b96c. check_layout 1280 px now OK for fy2-4 (packet showed FAIL).
