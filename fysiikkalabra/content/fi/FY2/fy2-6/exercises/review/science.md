VERDICT: PASS
CONTENT-HASH: 6f5fb811a8523689
## Blocking
## Polish
- exercises/exercises.json:64 — L2-03 "noin $31\,\text{TWh}$" (2024) names no source; add (Tilastokeskus) as L1-04 and L2-02 do.
- exercises/solutions.md:59 and :109 — the checks jump "$219\,000\,\text{MWh} \approx 220\,\text{GWh}$" and "$\ldots\,\text{MW} \cdot 8760\,\text{h} \approx 4{,}7\,\text{TWh}$" without the substitution ($219 \cdot 1000\,\text{MWh}$; $4{,}7 \cdot 10^{6}\,\text{MWh}$).
- exercises/solutions.md:18 — L1-02 claims two significant figures but writes $960\,\text{MWh}$; $9{,}6 \cdot 10^{2}\,\text{MWh}$ is unambiguous (the answer key is fine).
## Checked
- Hash unchanged start to end; round-1 items fixed (L1-04 $25{,}3\,\%$ three figures; LaTeX quantities; L2-02 $8{,}8 \cdot 10^{3}\,\text{h}$; households 2,86 million, Tilastokeskus 2024).
- Recomputed all 12 answers independently against answers.py: 420; 960; 38,4; 25,28; 14; 70,08; 8750; 2583; 2,803; 7,14; 2,727; 13,09 — all match, each rounded key within tolerance 0,02.
- Every solution has the seven parts, symbolic first, colon division in substitutions, \cdot only, real reasonableness checks; L3-03 answers the January-evening question correctly (no solar after sunset).
- Data: Tilastokeskus 2024 total 79,9, wind 20,2, hydro ≈ 14 TWh; OL3 1,6 GW; capacity factors wind 32–33 %, solar 11 %, nuclear 90 % realistic; invented situations marked "Esimerkkinä oleva".
- Scope: only E = P·t and shares; no FY3/FY4 content. Level counts 5/4/3.
