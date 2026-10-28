VERDICT: PASS
CONTENT-HASH: 4336e3fb3c6c8370

## Blocking
- none.

## Polish
- exercises.json fy1-7-L2-01 — "mitat ovat $10{,}0\,\text{cm} \cdot 5{,}0\,\text{cm} \cdot 2{,}0\,\text{cm}$" is correct with \cdot, but it writes the product the student should form; "mitat ovat $10{,}0\,\text{cm}$, $5{,}0\,\text{cm}$ ja $2{,}0\,\text{cm}$" (as the solution's Annettu has it) leaves the volume to the student.
- solutions.md L2-01 Järkevyys — "Kulta on noin 19-kertaisen tiheää" is ungrammatical; write "Kulta on noin 19 kertaa vettä tiheämpää".
- solutions.md L3-01 Kysytty/Kaava — the ratio is written $V_\text{Al} : V_\text{Cu}$ but computed as $\rho_\text{Cu} / \rho_\text{Al}$ in a display fraction; with the size-comparison rule say "suurempi tilavuus jaetaan pienemmällä" in Periaate so the colon and the fraction read as the same thing.

## Checked
- Delta: × replaced by \cdot in L2-01 and the value is unchanged (100 cm³, 1,93 kg).
- Three "/" divisions (L1 ice estimate 37 kg : 0,04 m³, L2 steel 33 g : 4 cm³, L3-01 8960 : 2700) are now colons with correct values (925; about 8 g/cm³; 3,32).
- No other × or " / " operation left in exercises.json or solutions.md.
- Counts, contexts and solutions otherwise as previously passed; the L2-01 conversion cm to m is stated per dimension.
- Finnish and case after number+unit correct apart from the item above.
