VERDICT: PASS
CONTENT-HASH: fdddeeb5c9f1df61

## Blocking

## Polish
- content/fi/FY4/fy4-3/exercises/solutions.md:301 (L2-08) — carried from round 1: the "Tarkistus" only restates the third law (circular) — replace it with a real check, e.g. "Yhtä suuri voima muuttaa kevyemmän henkilöauton liikettä paljon enemmän kuin kuorma-auton: henkilöauto sinkoutuu, kuorma-auto tuskin hidastuu."
- content/fi/FY4/fy4-3/exercises/exercises.json:277 (L2-08) — carried: "Esimerkkiarvot:" at the start reads as if the masses were placeholders — drop the prefix.
- lessons/FY4/fy4-3/answers.py:23 — carried: the comment lists L1-06, L1-07, L2-07 as multiple choice; add L2-08.

## Checked
- Round 2, delta since commit 5a93acbfc (packet generated in full mode; reviewed the change against the round-1 PASS): only L2-08 subscripts changed, KH/HK now upright in every occurrence — magnitudes in text, answer, options, solution, and (edited in the working tree during this review, hash 07ea70e3 → fdddeeb5c9f1df61) the vectors \overline{F}_{\text{KH}}, \overline{F}_{\text{HK}} in the text, the "kumoavat" reason's feedback, Periaate and Mallivastaus. No italic _{KH}/_{HK} left (grep). The notation is now one symbol family.
- K, H are word abbreviations (kuorma-auto, henkilöauto), so upright follows the word-subscript rule; meaning F_KH = by K on H matches the lesson's F_{AB}.
- Physics, option order, correct flags and feedback wording otherwise unchanged; Newton III answer still right, exactly one correct choice and one correct reason.
- answers.py run once: all 17 numeric answers within tolerance; the 4 multiple-choice tasks each have exactly one correct option.
- Text only, no render this round; the inline formulas stay short (about 100 px).
- Hash fdddeeb5c9f1df61 at the start of the redo and at the end.
