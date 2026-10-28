VERDICT: FAIL
CONTENT-HASH: 833eb77a27e1f28f
## Blocking
- exercises/solutions.md:38 — L1-04: "kaksi merkitsevää numeroa kuten tuulivoiman energiassa" is false. $20{,}2$ and $79{,}9\,\text{TWh}$ have three figures, so the answer is $25{,}3\,\%$ (the tolerance accepts it); fix the answer and its justification.
- Teacher rule, all numbers in LaTeX: solutions.md:29 ("38 GWh", "10 TWh") and :89 ("2,8 miljoonaa") are plain text — put them in `$…$`.
- Teacher rule, conversions by substitution: solutions.md:56 "$100\,\text{MW} = 100\,000\,\text{kW}$" — write $100\cdot1000\,\text{kW} = 100\,000\,\text{kW}$.
## Polish
- solutions.md:89 — Tilastokeskus counts 2 861 000 households at the end of 2024 (Asunnot ja asuinolot 2024). Write "noin 2,9 miljoonaa (Tilastokeskus 2024)", which names the source as the scope note requires.
- solutions.md:68 — L2-02 claims two significant figures but shows $8750\,\text{h}$. Write $8{,}8\cdot10^{3}\,\text{h}$ (the answer key is fine).
- L2-01 has the same structure as the worked example (annual energy and rated power → % of rated); L3-03 is one formula ($t = E : P$), which fits level 1–2 more than level 3 (pedagogy decides).
## Checked
- Recomputed all 12 answers in one script against answers.py: 21,9; 960; 38,4; 25,28; 3,539; 10,84; 8750; 2583; 2,803; 7,14; 2,727; 562,5. They all match, and each rounded answer is within tolerance.
- Data verified at stat.fi: 2024 total 79,9, wind 20,2, hydro 14,1, solar 0,9 TWh; nuclear about 31 TWh (39 %). Households in Finland: 2,86 million (2024).
- Every solution has all seven parts, is solved symbolically first, uses `\cdot` and colon division with no × or "/", and has real reasonableness checks.
- Magnitudes are realistic: solar capacity factor 11 %, wind 27–33 %, nuclear 90 %, winter demand 11 GW, viisi reaktoria.
- Scope: only E = P·t; no FY3/FY4 content (work, Q = cmΔT, chain efficiency, CHP).
- Level counts are 5/4/3.
