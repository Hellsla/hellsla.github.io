VERDICT: PASS
CONTENT-HASH: d7633bb66bf5dcc9

## Blocking

## Polish
- inquiry.json simulaatio `model` — "its long-lived excited state": Pa-234m lasts about 1.2 min, while the ground state lasts 6.7 h — write "its metastable (isomeric) excited state, half-life about 1.2 min".
- lesson.md Key idea, electron capture — "from the innermost electron shell" — add "usually".
- lesson.md worked example, Substitution — the printed values give $1.9865/1.0600 = 1.8741$, but the text shows $1.8740$ — write $1.874\cdot10^{-12}\,\text{m}$.
- inquiry.json gammaspektri solution — "There are no other peaks", but a real detector spectrum also has a sum peak and a backscatter peak — add "in this figure".

## Checked
- Recomputed in one script: H 3→2 = 1.89 eV; Cs-137 → Ba-137 with λ = 1.874 pm; Tc-99m λ = 8.826 pm (the eV mistake gives 8826 pm, ratio 4.71); U-235 → Pb-207 needs 7 α and 4 β⁻; the nucleus/atom size ratio is 10⁴–10⁵. All match lesson-answers.py.
- U-238 series: every step follows the α/β⁻ rule, 8 α + 6 β⁻ ending at Pb-206; matches the NNDC main branches. The sim's CHAIN and STABLE [Z, N] lists are correct.
- Co-60/Ni-60 energies match NNDC. Exact gap 0.033 keV; my recoil calculation gives 0.028 keV, so "most of it is rounding" holds. The numeric answer and both mistake values are right.
- The levels figure is to scale as it says (9.25 keV/px; Co-60 at Q ≈ 2823 keV).
- Shifts figure, chart-of-nuclides β⁻/β⁺ regions and the isotope nucleon counts are correct. Every decay equation, electron capture included, balances.
- Predictions, virhe and tarkistus-1: exactly one correct option each; every distractor's feedback is right.
- koe-1: varies only k, and simState gives Z, N, A and mode. The conclusion's model answer matches the data.
- Hook (Am-241, ionisation current) and the exit ticket are correct.
- The sim's readout equations include $\bar\nu$. The model's limits are stated (data, schematic nucleus, no timing).
