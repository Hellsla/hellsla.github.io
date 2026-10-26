VERDICT: FAIL
CONTENT-HASH: 47e17fa000fec6df

## Blocking
- solutions.md:47 (fy3-15-L2-01, Järkevyys) — "kattilan ja höyrykierron häviöt vievät siis yli kaksi kolmasosaa polttoaineen energiasta" is false. Boiler and steam-cycle losses are $1 - 0{,}880 \cdot 0{,}420 = 0{,}630$, and all losses together are $1 - 0{,}362 = 0{,}638$. Both are below $2/3 \approx 0{,}667$. — Write "lähes kaksi kolmasosaa (noin 63 %)" or "noin 64 % polttoaineen energiasta".

## Polish
- exercises.json:30 and solutions.md:27 (L1-04) — "siirtyy *lopulta* lämpönä ympäristöön": in the end the 320 MW of electricity also becomes heat in the environment, so a careful student could answer 800 MW. — Drop "lopulta" and write "siirtyy voimalaitoksesta lämpönä ympäristöön".
- solutions.md:38 (L1-05) — the Vastaus is $90\,\%$, but the data and exercises.json have three significant figures. — Write $90{,}0\,\%$.
- solutions.md:87 (L3-02) — "Tuulipuiston 0,42" is not given in the task. — Write "Tuulipuiston hyötysuhde kertoo vain…".
- solutions.md:22 (L1-03) — "Loput 15,8 kW lämmittää paneelia": part of that power is reflected. — Write "lämmittää paneelia tai heijastuu".
- lesson.md:111,113,115 — the three invisible `<path … stroke="none"/>` leftovers in figure 3 are still there. — Remove them.

## Checked
- Round-1 blockers are fixed. The condenser heat now has its own symbol $P_\text{L} = c\,q_m\,\Delta T$, and the lesson says it is the largest part of $P_\text{h}$, not all of it (figure 4, summary). All 12 solutions are in LaTeX, symbolic first, and L2-03 substitutes directly.
- All 12 final answers were recomputed independently. They match answers.py and exercises.json, and every Vastaus in solutions.md agrees with exercises.json to the stated figures. Tolerances cover rounding.
- Worked example: $P_1 = 546$, $P_2 \approx 240$, $P_3 \approx 228\,\text{MW}$, $\eta = 0{,}380$, $P_\text{h} = 372\,\text{MW}$. The condenser takes 306 MW (51 %), and the loss chain 54 + 306 + 12 = 372 MW is consistent.
- Figure 1 Sankey is to scale (0,4 px/MW): 40 / 248 / 12 / 200 MW. Figure 3 bars (0,5 px/MW) are 500/460/212/200 MW with loss boxes of 40/248/12 MW. Figure 2 is to scale: 160→120 MW electricity, 352 MW useful at 232 MW, waste 240→48 MW.
- All figure labels are LaTeX `foreignObject`s. Figure 4 reads cleanly at 390 px.
- Inquiry numbers: 520 MJ, 248 MW, 48 MW, 130 MW, 8,64 MW (about 6 % of 155,5 MW), 342/360/540 MW and 216 MW. Every mistake value reproduces its stated wrong method, and every correct option is right.
- Pred-2 physics: a hotter condenser means less turbine work. The figure of 0,17 MW of electricity per MW of heat is realistic. Typical efficiencies are realistic, and the lesson states that their denominators differ.
- Exit ticket: 0,432; 85 % and 15 MW; the hydro vs. heat-engine explanation is correct.
- Scope: power, efficiency, energy conservation and $Q = cm\Delta T$ are FY3 content, with no FY4 formulas.
- No lesson ids appear in visible student text, and the prerequisite chapter is now named by title only.
