VERDICT: FAIL
CONTENT-HASH: fed6c0617f0111b5

## Blocking
- solutions.md:100 (fy6-13-L3-01, Vastaus) — A: the rounding reason breaks the teacher's binding rule P7b (trailing zeros are significant unless the task says otherwise). The data $120\,\text{pF}$ and $500\,\text{V}$ both have three significant figures, so "kaksi merkitsevää numeroa kuten kapasitanssissa $120\,\text{pF}$" is wrong. — Fix: write the answer as $15{,}0\,\mu\text{J}$, "kolme merkitsevää numeroa kuten kapasitanssissa $120\,\text{pF}$ ja jännitteessä $500\,\text{V}$". The answer 15 and the tolerance 0.02 can stay.

## Polish
- solutions.md:50 (L1-05) and :241 (L2-08) — the answer is written $360\,\mu\text{J}$ / $370\,\mu\text{J}$ and called two significant figures. Under P7b the written number reads as three. Write $3{,}6 \cdot 10^{2}\,\mu\text{J}$ and $3{,}7 \cdot 10^{2}\,\mu\text{J}$, the form this round already used for L1-08.
- solutions.md:196 (L2-07) — "kuten kapasitanssissa ja jännitteessä": $220\,\mu\text{F}$ has three figures under P7b. The limiting datum is $24\,\text{V}$ alone.
- solutions.md:60 (L2-01) — "$320\,\text{V}$ eli $3{,}2 \cdot 10^{2}\,\text{V}$": only the second form shows two figures. Give it first, or give it alone.

## Checked
- Hash fed6c0617f0111b5 at start and end. The only change since the last PASS is the L1-08 answer step (git c40cc4fbb); I still reviewed the whole set.
- Recomputed all 19 numeric answers in one script with my own formulas, including the two least-squares fits (L2-05: C = 47,2 µF; L3-04: k = 100,0 V/s, C = 150 µF). Every one agrees with answers.py and exercises.json.
- L1-08: ΔW = ½C(U₂² − U₁²) = 144 mJ. Two figures (from 6,0 V and 18 V; 1000 µF has four under P7b) is right. The shown answer 1,4·10² mJ gives a step of 10, so the check accepts 139–149 and a student's 140 passes.
- Every other tolerance lets an answer rounded to its data's figures pass (L2-05's 3,3–3,5 mJ fits inside 4 %).
- Physics: C = Q/U, the plate-capacitor conditions (thin gap, dielectric fills it), U_max = E_max·d, W = ½QU = ½CU². Source connected vs disconnected (L1-07, L3-01, L3-02) and the energy halving in L1-09 and L2-07 are stated with their model.
- L2-06: the voltage rises per second are 3,5 / 2,0 / 1,4 / 0,8 / 0,5 / 0,3 V. Exactly one option is correct, and each distractor's numbers are right.
- L3-05: ratio 6,89, and the scaling ε_r·E_max² is right.
- Figures ex-qu and ex-qu2: the points (60 µC; 12 V) and (120 µC; 8 V) lie on grid lines, and neither figure gives C or W.
- Scope: no capacitor connections and no exponential function. Every task stays inside "kondensaattori ja kondensaattorin energia" and "läpilyöntilujuus".
