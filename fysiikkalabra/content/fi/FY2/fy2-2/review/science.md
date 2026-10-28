VERDICT: FAIL
CONTENT-HASH: 668eb210f7a5ef23

## Blocking
- inquiry.json:63 (ennuste-1, correct option) — "suhde on noin 3,2" is a number outside LaTeX (teacher's rule: everything in LaTeX) — write $32\,\text{MJ} : 10\,\text{MJ} \approx 3{,}2$.
- inquiry.json:329 (tarkistus-2, mistake 0.0001) — "Lukuarvot 1,0 ja 10" are plain-text numbers — write $1{,}0$ and $10$.
- lang/fi.json:193 `valittu` with `n_suklaa`, `n_kaasu`, `n_tankki`, `n_aurinko_s`, `n_aurinko_h`, `n_aurinko` — the readout (and the experiment's Alkutila line) shows "suklaalevy 200 g", "kaasupullo 11 kg", "bensiinitankki 50 l", "Aurinko Maahan, 1 h" as plain text, but the teacher requires LaTeX for numbers with units in sim readouts. The canvas sets them as \text words, not number and unit — give each object a TeX name (e.g. `\text{suklaalevy}\ 200\,\text{g}`) and use it in the readout and the canvas. The select can keep the plain name.

## Polish
- inquiry.json:328 — the value 0.0001 is not a likely mistake: the unconverted ratio is 0,1 (already listed), and the inverted, converted one is 0,01. Use 0.01, with feedback about the inverted ratio.
- inquiry.json:181 (ketju solution, Järkevyys) — "$100 - 40 = 60$, … megajoulea" drops the units inside the chain; write $100\,\text{MJ} - 40\,\text{MJ} = 60\,\text{MJ}$ etc.

## Checked
- Hash 668eb210f7a5ef23 at start and end. All round-1 blocking items fixed (thousand-years option, 0,1 and 51 000 feedbacks, LaTeX in the `s_*` source lines).
- Recomputed in one script, matching lesson-answers.py: 340 kJ, 3,2, $6{,}25 \cdot 10^{20}\,\text{J}$ (625 EJ, shown as 620), 41 days, 600 kJ, 66 MJ, 51 GJ, 100, 2500 J.
- All 28 sim values recomputed (photon $3{,}6 \cdot 10^{-19}\,\text{J}$, AA 13,5 kJ, banana 456 kJ, OL3 $1{,}38 \cdot 10^{14}\,\text{J}$, M 9 $2{,}0 \cdot 10^{18}\,\text{J}$, U-235 $8{,}2 \cdot 10^{13}\,\text{J}$ …).
- Web-verified (stat.fi): electricity 79,8 TWh in 2023; total energy 1,32 million TJ in 2023. Energy Institute 620 EJ (2023), and IAU $3{,}828 \cdot 10^{26}\,\text{W}$ agree.
- Figures to scale: the ladder positions (33,2 px per decade) and the Sankey widths (96 = 24 + 72 for 800 = 200 + 600).
- Experiments: initial names match the lang names; simState gives E_MJ and E_EJ (620 for both koe-2 objects).
- Worked example: symbolic first, conversion by substitution, rounding justified, a real check.
- Scope: no $E_k$, $E_p$, work, force or $Q = cm\Delta T$; N·m removed; no ×; written division uses a colon.
