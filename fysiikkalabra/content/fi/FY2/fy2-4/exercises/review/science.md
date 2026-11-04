VERDICT: PASS
CONTENT-HASH: f04f800bbdb5c377

Round 2: there were no blocking items in round 1. The changed tasks are correct. L2-05 now uses a 40 W halogen lamp with 2,8 W of light (7,0 %), as suggested, so the ratio is 4,3. L3-04 now says "samankokoisten autojen". L3-05 has been extended into a multi-step level-3 task (power from the table, annual energy, cost). L2-06 now asks for each row's ratio.

## Blocking
(none)

## Polish
- solutions.md L3-05 Vastaus and exercises.json L3-05 — "lämmöksi muuttuu vuodessa 6,9 kWh" counts only the heat the lamp gives off directly. The light (2,96 kWh) also ends up as thermal energy in the room, as fy2-1 teaches. Write "muuttuu suoraan lämmöksi" in the task and the answer.
- solutions.md L3-05 — the heading "Kuvaajan lukeminen" is used for a table. Write "Taulukon lukeminen".
- docs/exercise-bank/FY2.md:29–30 (carried over) — the plan still lists a kettle task (c·m·ΔT) and chain-efficiency tasks, which are outside FY2 scope (they belong to FY3 fy3-15). The set rightly avoids them, so update the plan to match.

## Checked
- Recomputed in one script (scratchpad recompute_r2.py): L2-05 efficiencies 5,0 / 7,0 / 20 / 30 %, ratio 4,29, so 4,3, and the halogen equivalent is 2,7 W / 0,070 = 39 W; L2-06 row ratios 0,80 / 0,787 / 0,798 / 0,792, so 79 %; L3-04 3,14, useful energies 15,3 and 13,3 kWh, loss 40 kWh; L3-05 P = 9,0 W, 9,855 kWh a year, heat share 0,694–0,704 on every row, 6,89 kWh, 1,38 €, η = 30,1 %, total cost 1,97 €. All match the answer key and solutions.md.
- L2-05: the realism point from round 1 is resolved (halogen about 1,4 × incandescent). "Eniten valoa antaa loistelamppu (3,6 W)" is correct for the new table.
- L3-05: the error identified (loss share taken as efficiency) is right. Using 70 % for the heat calculation is physically justified (30 % + 70 % = 100 %). The assumption of steady power is now stated, and the energy check 2,96 + 6,89 = 9,85 kWh holds.
- The scope holds: one device's η and P = E : t only, with no product of efficiencies and no c·m·ΔT. Invented data are labelled "Esimerkkimittaus".
- The hash was the same at the start and the end.
