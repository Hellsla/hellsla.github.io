VERDICT: FAIL
CONTENT-HASH: d032fc6ba7d117ce
## Blocking
- lesson.md:225 and :229 — teacher rule, conversions by substitution: the worked example's result jumps from $1598\,\text{kW}$ (stage Sijoitus) to $1{,}6\,\text{MW}$, and the check from $5000\,\text{kW} \cdot 8760\,\text{h}$ straight to $43{,}8\,\text{GWh}$. This is the model solution students copy — add $1598\,\text{kW} = 1{,}598 \cdot 1000\,\text{kW} \approx 1{,}6\,\text{MW}$ (in Sijoitus or Tulos) and $= 43\,800\,000\,\text{kWh} = 43{,}8 \cdot 10^{6}\,\text{kWh} = 43{,}8\,\text{GWh}$.
## Polish
- inquiry.json:137 (data-viikko) — daily mean consumption $14{,}1$–$14{,}6\,\text{GW}$ is above Fingrid's hourly peak of winter 2023–24 (just over $14{,}5\,\text{GW}$, 2–3 Jan 2024); a daily mean is always below the peak hour. Scale consumption down by about $1{,}5\,\text{GW}$ (with the answer $9{,}9$, mistakes and model answer), or present the rows as hourly values of an exceptionally cold week. Example-labelled, so not blocking.
- inquiry.json:314 (tarkistus-2 Järkevyys) — "$9000\,\text{MWh} = 9\,\text{GWh}$" without the substitution; write $9 \cdot 1000\,\text{MWh}$.
- inquiry.json:79 and :137 — table cells (31, 20,2 …; 12,8 …) and the headers' units are plain text; the teacher's "everything in LaTeX" may want $31$ and $(\text{TWh})$.
## Checked
- Hash unchanged start to end; round-1 blocking items all fixed (world-ratio feedback now "kymmeniä kertoja", 36×; 2306 "megawatteina"; data-fi answer $2{,}31\,\text{GW}$ to three figures; aria "kaksi viidesosaa"; plain-text quantities; substitution conversions).
- Recomputed lesson-answers.py in one script: 1598 kW, 0,320, 43,8 GWh, 2,306 GW, 320, 14,016 TWh, 17,5 %, 8,76 GWh, 9,9 / 2,1 GW, world ratio 35,8; the table sums to 79,9 TWh. Every numeric answer and mistake value matches its stated wrong path.
- Data: Tilastokeskus 2024 (79,9; wind 20,2; hydro 14,1; fossil+peat 3,4; solar 0,9; nuclear ≈ 31 from 39 %). Wind capacity end-2024 8 358 MW (Suomen Tuulivoimayhdistys, vuositilastot 2024), so "noin 8 GW" is right. Nuclear 4,3 GW fits 4,4 GW installed.
- Figures: fi-bars to scale at 10,5 px/TWh; log chart 70 px per decade, points at log10 P, "kaksi ja puoli askelta" = 2,50 decades.
- E = P·t with the constant-P condition stated; mean power defined. Scope: no FY3/FY4 content; no ×; colon division (only the formula keeps \frac).
- Every correct option and the feedback physics (nuclear largest; hydro fastest to adjust; nuclear base load). Provenance: data-fi `statistics` with source_note, data-viikko `example`.
