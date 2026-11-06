VERDICT: PASS
CONTENT-HASH: e2a4b4fa15ee78b7

## Blocking
(none)

## Polish
- exercises.json:265 — the second model-solution line "ΔI = 0,010 · 140,0 mA + 2 · 0,1 mA" measures 312 px at 17 px, over the 300 px budget (display block scrolls) — write "ΔI = 0,010 · 140 mA + 2 · 0,1 mA" or split the sum onto two lines (solutions.md:191 block).
- exercises.json:272,276,285 — "Jos rivin luulee virheelliseksi, ajattelee, että ..." is stiff — "Jos pidät riviä virheellisenä, ajattelet ehkä, että ...".
- exercises.json:265 — the no-error option's feedback ("suurempi alue ei anna pienempää virherajaa") hands over the key; shorten to "Laske virheraja kummallakin alueella."

## Checked
- Correct (wrong) row is not the longest and not the only one with a reason; every row has a "koska".
- Rows 1, 2, 4 are correct and carry the chapter's other warned mistake (ammeter in parallel) and the legitimate start-at-largest rule; row 3 is exactly the warned mistake "largest range always best".
- Numbers: 0,02*0,14+0,03 = 33 mA; 0,01*140+0,2 = 1,6 mA; 4,38 V needs the 20 V range - all correct; ranges and limits are in the task and lesson table.
- Within lesson scope; does not repeat L2-02 (limit calculation) or L2-06 (OL).
- Question last, with the "viimeinen vaihtoehto" rule stated; no figures, no data captions.
- Text only (no renders: packet screenshots were empty; I measured widths of the model-solution formulas with KaTeX in Chromium at 17 px, 390 px viewport).
