VERDICT: PASS
CONTENT-HASH: 83dc08db7ea57a37
ROUND: 2

## Blocking

## Polish
- [Minor] `fy3-16-L2-06` answer chip — the chip and Vastaus show "$1{,}4 \cdot 10^{2}\,\text{W/K}$" while the key is 139 (tolerance 5 %); consistent, but the chip would read simpler as "$140\,\text{W/K}$" (L2-1280-8, -9).
- [Minor] solutions `fy3-16-L3-04` Vastaus — "noin $480\,\text{€}$ ($480{,}6\,\text{€}$)" fine; the Mallivastaus c) block ends with the unsupported "Esimerkkiaineiston hinnat ja lämpötilat ovat keksittyjä" sentence, which would sit better in the task text beside "esimerkkiaineisto" (L3-1280-8).
- [Minor] solutions `fy3-16-L2-05`, `L2-07` — check that the b)/d) answers are in a "Mallivastaus" block like L2-06 and L3-04/05 now are (L2-05 b) is; confirm for the rest).
- [Minor] `fy3-16-L3-04` table — header "Kuukausi" is left-aligned over right-aligned numbers; align the columns.

## Round 1 items
- Round 1 had no Blocking items. Polish resolved: L3-04 c) wording is now "Kumpi ratkaisu on edullisempi, ja kuinka monta euroa se säästää?" with the Vastaus "noin 480 € (480,6 €)"; L2-07 and L3-04 $U$ now with `\cdot` (L2-1280-9); L3-05 chains carry units (L3-1280-9); Mallivastaus blocks added for L2-06 c, L3-04 c, L3-05 d.
- New L3-05 (water layer freezes): task now gives the layer thickness 0,030 m, $c_\text{vesi} = 4190$ and the density, so 54 000 kg, $Q_1 = 2{,}715$, $Q_2 = 18{,}04$, $Q_3 = 0{,}567\,\text{GJ}$, total 21,32 GJ over 36 000 s = 592 kW, answer 590 kW; matches the box. L2-07 now states $s = 334\,\text{kJ/kg}$ in the task.

## Checked
- 1280 px with solutions open: L2-1280-8, -9 (L2-06 line fit, L2-07 error task), L3-1280-8 (L3-04 solution end, L3-05 text), L3-1280-9, -10 (L3-05 solution, chains with units, answer, Mallivastaus d). Diff 315175221 read for exercises.json and solutions.md. No 360 px exercise captures exist; check_layout 360 px clean per packet.
- Answer keys: L2-05 76 %, L2-06 139 W/K, L2-07 2,9 h, L3-04 480 €, L3-05 590 kW agree with the solutions. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
