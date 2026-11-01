VERDICT: FAIL
CONTENT-HASH: ed31b144d397cb3e

Science review, 2026-11-01. Every number was recomputed with NIST masses (script output: Q_DT 17.589 MeV, E_α 3.541 MeV, ⁶Li+n 4.783 MeV, N = 7.097·10²², m_T = 0.3554 g, P_α = 99.4 MW, 16/24 = 0.667, n_air/n_plasma ≈ 2.5·10⁵). All agree with the unit.

## Blocking
1. **(A, causality and source) The plant electricity.** Places: `unit.md` "Gain is not electricity" ("To deliver 50 MW of heating, the plant draws over 300 MW of electricity from the grid, and its magnets, cryogenics and pumps need power too"). The same claim is in `check-explain` (model and criterion 3), `pair-gain` (model and criterion 2), the feedback of all four `pred-gain` options, the bar "> 300" in the `power` figure, and `unit.json` (source 9). The sentence makes the heating systems alone need more than 300 MW. ITER's own page (https://www.iter.org/node/2751) says: "Electricity requirements for the ITER plant and facilities will range from 110 MW up to 620 MW for peak periods of 30 seconds during plasma operation"; "the cooling water and cryogenic systems will absorb about 80% of this supply." "Over 300 MW" comes only from Wikipedia, which gives no source, and students are graded on it. The comparison "170 MW … less than ITER draws" rests on the same number: it is not true against the 110 MW minimum. Fix:
   - **Text:** "During a pulse the whole plant (heating systems, cooling water, cryogenics, magnets) draws far more electricity than the 50 MW that reaches the plasma: ITER gives 110 MW at the least and up to 620 MW in 30-second peaks."
   - **Comparison:** write "…about 170 MW of electricity: far less than ITER's peak demand of 620 MW."
   - **Figure:** draw the third bar as the range 110–620 MW.
   - **Feedbacks, models, criteria:** write "draws more electricity than it would make (110–620 MW, iter.org)" or "far more than 50 MW".
   - **Sources:** cite iter.org Power supply.

## Polish
2. `unit.md` worked example, Reasonableness: "The other 401 MW" has three significant figures, but the answer has two. Write "about 400 MW".
3. `teacher.md` line 25 attributes "110 MW to 620 MW peak" to Wikipedia. It is iter.org node/2751.

## Checked (correct)
- Q definition, Q = 1 breakeven, JET 1997 16/24 MW ≈ 0.67 (iter.org), Q = 10, 500/50 MW, 400–600 s, 830 m³ (facts page), and "no electricity" (iter.org: "ITER will not convert … as electricity").
- The alpha share, the burning-plasma claim (α ≈ 2× external) and the momentum argument.
- Engineering breakeven vs scientific gain, and ignition in `check-1`.
- The tritium numeric with its three mistakes, CANDU, half-life 12.3 a, the 2012 licence.
- Every component number against the iter.org machine pages (see Shared issues for the data file).
- The divertor as the highest heat flux is correct.

## Shared issues
- `assets/units/fy14/data/iter.json` `q.points[3]`: "over 300 MW, according to Wikipedia". Replace it with the iter.org range above. It is not shown in this unit (`about: false`), so it does not block here.
- `iter.json` `schedule.items[1]`: "the first plasma experiments with the full machine". The PDF says "a more complete machine": SRO starts with a temporary first wall and the initial heating. Write "with a more complete machine".
- Developer's open questions:
  - **Plasma volume:** the facts page gives 830 m³ and the machine pages give 840 m³ (both checked today). Keeping 830 with the existing `number_note` is fine.
  - **"Over 300 MW":** see Blocking 1.
  - **Cryopumps:** the hint is right. iter.org says the six torus cryopumps go "in the divertor ports of the vacuum vessel and cryostat", which are the lower ports. Optionally write "in a lower (divertor) port".
- All other numbers in `iter.json` match the iter.org pages read today: magnets, vessel, thermal shield, cryostat, divertor, blanket, heating (16.5 MW ×2 at 1 MeV, 170 GHz 40→67 MW, 40–55 MHz 10→20 MW), diagnostics (60/101), cryopumps (6/2/4), members and the site.
