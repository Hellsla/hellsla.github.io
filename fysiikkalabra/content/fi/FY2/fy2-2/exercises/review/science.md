VERDICT: FAIL
CONTENT-HASH: 29181ffcb4929ba7

## Blocking
- exercises/solutions.md:39 (L1-04) — "$9{,}0\,\text{MJ}$ kolmestatoista" is wrong: the gas gave 12 MJ — "kahdestatoista".
- exercises/solutions.md:118 (L3-03) — the task asks how much petrol would give the same energy (370 TJ), but the solution compares only one kilogram (2,6 million litres) — add $V = \dfrac{E}{E_\text{litra}} = \dfrac{370 \cdot 10^{6}\,\text{MJ}}{32\,\text{MJ/l}} \approx 1{,}2 \cdot 10^{7}\,\text{l}$ (about 12 million litres) against 4,5 kg of uranium, with its rounding and check (CLAUDE.md Lesson form 7).

## Polish
- exercises/solutions.md:56, 67 (L2-01, L2-02) — "$800 : 1000\,\text{MJ}$" reads as 800 divided by 1000 MJ. Substitute the prefix instead: $800\,\text{kJ} = 800 \cdot 10^{3}\,\text{J} = 0{,}80 \cdot 10^{6}\,\text{J} = 0{,}80\,\text{MJ}$, or $(800 : 1000)\,\text{MJ}$.
- exercises/solutions.md:65 (L2-02) — in $E = V \cdot E_\text{litra}$ the units do not close unless $E_\text{litra} = 32\,\text{MJ/l}$ and $V = 40\,\text{l}$; write them so.
- exercises.json L1-02 and L2-01 — one chocolate bar has 4,4 MJ and the other 2,2 MJ; name the bars' masses (200 g and 100 g), which match 2200 kJ per 100 g.
- exercises/solutions.md:38 (L1-04) — "tasalukujen" is unclear; say that the difference is given to tenths of a megajoule as in 9,0 MJ.

## Checked
- Recomputed all 12 answers in one script against answers.py and exercises.json: 54 000 J, 4400 kJ, 140 GJ, 3,0 MJ, 22, 3,0 MJ, 1,3 GJ, 6,0 kJ, 2200, 5,6, 230 TJ, 4,5 kg all agree.
- Data verified: Tilastokeskus 2023 electricity 79,8 TWh → 787 TJ a day (790 TJ); OL3 1600 MW → 138 TJ a day, 4300 MW thermal → 372 TJ; U-235 $8{,}2 \cdot 10^{13}\,\text{J/kg}$; petrol 32 MJ/l; banana 450 kJ.
- L2-03 physics right: the absorbed light also becomes heat, so all 6,0 kJ ends up as heat.
- Every solution has the seven parts, solved symbolically first; rounding and the checks are real.
- Scope: no work, $Q = cm\Delta T$, $E_k$/$E_p$ or chain-efficiency products; no ×; division with a colon or a fraction.
