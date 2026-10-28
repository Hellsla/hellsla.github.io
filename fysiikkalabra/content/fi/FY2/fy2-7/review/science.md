VERDICT: FAIL
CONTENT-HASH: 5e17e209235f27bb

## Blocking
- inquiry.json:143 ("sahko" table) — The cells "noin 4 %" and "9,2 %" are percentages in plain text inside a task. That breaks the teacher's standing rule that everything is in LaTeX. The other cells ("noin 83", "noin 3", "36,0", "3,3") are bare numbers as well. — Write each cell in LaTeX: `$\approx 4\,\%$`, `$9{,}2\,\%$`, `$\approx 83$`, `$36{,}0$` and so on. Do the same for the bare numbers in the "kl" table (line 111: 36,0 and 32,7) and the "jannite" table (line 174: 20 / 0,80 …), which have their units only in the column headers.

## Polish
- inquiry.json:190 ("jannite" choice feedback) — "häviö pienenee $400$-kertaiseksi" literally says the loss grows 400-fold. — Write "pienenee $400$:sosaan" or "$400$ kertaa pienemmäksi", as the correct option already does.
- lesson.md:152 — "Sähköä ei varastoida sellaisenaan" is true at the scale of the grid, but capacitors do store electrical energy directly. — Add "suuria määriä" if wanted.

## Checked
- I recomputed every number of lesson.md, inquiry.json and exit-ticket.json in one script. All match lesson-answers.py: example 222,95 → 223 MWh and 22,05 → 22 MWh (the rounding is now justified per datum); kl 9,17 → 9,2 %; siirto 15 %; tarkistus-2 500 MWh; exit 768 MWh and 48 kWh.
- Every mistake value is now outside its tolerance: kl 10,1 and 3,3; siirto 85 and 17,6; tarkistus-2 281 and 469. The exact answers lie inside.
- The "jannite" model table follows the $1 : U^2$ scaling (0,80 → 0,0264 → 0,0020 MW). The 10 MW / 10 km example is plausible and labelled as a model. Its percentages, 8,0 %, 0,26 % and 0,020 %, are correct.
- The data is unchanged from round 1, where it was verified (Energiateollisuus, Sähkövuosi 2024: about 83 TWh with about 4 % losses; Kaukolämpötilasto 2024: 36,0 / 32,7 TWh). The 9 % is still marked as an estimate. The "sahko" comparison holds: about 3 TWh in each network, and 83 : 36 > 2.
- The grid voltages are correct (110–400 kV, 20 kV, 0,4 kV, 230 V). The high-voltage reasoning is qualitative and correct, with no $P = UI$.
- The Sankey is to scale (77 : 80 = 96 %, 3 : 80 ≈ 4 %; 73 : 80 ≈ 91 %, 7 : 80 ≈ 9 %). The figure labels are in LaTeX and read correctly.
- Every correct option and feedback in kertaus, ennuste-1/2, virhe, tarkistus-1/3 and johtopäätös is physically right. Losses are always heat to the surroundings, so energy is conserved.
- No FY3 content: no Q = cmΔT, no U-value, no chain product, no $P = I^2R$.
- Prose and task texts outside the tables are all in LaTeX. There is no ×, written division uses a colon, the % → decimal conversions are written by substitution, and the worked example is solved symbolically first.
