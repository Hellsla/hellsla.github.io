VERDICT: PASS
CONTENT-HASH: 66175cc0749d903c

## Blocking

## Polish
- assets/sims/fy6/fy6-13/sim.js:81 — the code comment still says "the ideal model's values before it"; for the next sim edit, align it with the new label ("at this voltage, as if no breakdown occurred"). It is a code comment, so students never see it.
- inquiry.json simulation `model` (Mallin oletukset) — still does not say that, while the source is connected, the readout keeps the ideal $Q = CU_0$ and $W$ at breakdown. The readout itself now says this correctly, so this is optional.

## Checked
- Previous Blocking fixed: lang/fi-easy.json `sims.fy6-13.lukemat_lap` now reads "Ideaalimallilla lasketut arvot tällä jännitteellä, jos läpilyöntiä ei tapahtuisi", which is what sim.js computes ($Q = CU_0$, $W = \tfrac{1}{2}QU_0$ at the set voltage). fi and en carry the same meaning.
- Browser (fi-easy preview, air, $A = 200\,\text{cm}^2$, $d = 1{,}0\,\text{mm}$): at 3,0 kV there is no breakdown and the normal readout shows C 177 pF, Q 531 nC, W 797 µJ; at 4,0 kV lapilyonti = 1, and the new label shows Q 708 nC and W 1417 µJ with the breakdown and model-limit notes.
- Recomputed in one script: C 88,5 pF; koe-1 Q 44,3/88,5/133/177 nC and W 11,1/44,3/99,6/177 µJ; koe-2 C ∝ 1/d; koe-3 glass U 0,179 kV, W 7,9 µJ; koe-4 495,8 nC, 248 µJ; paper 160 V; example 6,75 J, 6,75 kW, Q 0,045 C, 3,4 s; kertaus 150 kV/m; virhe 0,034 J; siirto 190,35 µJ; TV 12,0 J; exit 1,2 mC. All match the texts and the feedback.
- Predictions 1–2, kertaus, virhe, tarkistus 1–2: each has exactly one correct option, and each distractor's feedback is right.
- Experiments isolate the varied parameter, and simState gives every measured key (Q, W, C, E, U, lapilyonti); koe-5 starts below breakdown (2 MV/m).
- Models and conditions: the plate formula (small gap, gap filled), $U_\text{max} = E_\text{max} d$, the half-energy loss stated as a result of this charging model, the connected/disconnected table and its mechanism; charging is treated qualitatively only, with no capacitor connections (scope kept).
