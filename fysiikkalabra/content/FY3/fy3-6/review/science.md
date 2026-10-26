VERDICT: PASS
CONTENT-HASH: 35e87e039a774d36

## Blocking

## Polish
- inquiry.json `simulaatio.model` — "Kappaleen lämpötila pysyy välillä 0–100 °C, eikä kummankaan olomuoto muutu": with the body set to *vesi* the slider ends sit exactly at freezing and boiling; "pysyy välillä 0–100 °C, joten vesikappale pysyy nesteenä (päätepisteet ovat raja-arvoja)" or a 1–99 °C range would remove the edge case. Not misleading in any experiment, which use 80 °C and 90 °C.

## Checked
- All 12 exercise answers recomputed independently (Q = cmΔT, T as a heat-capacity-weighted mean, P t = cmΔT, ΔT = Q/(cm), equal-storage volume ratio): all match answers.py and exercises.json within tolerance; the data's significant figures give the stated answers.
- Worked example: c_m = c_v m_v (T − T_v)/(m_m (T_m − T)) solved symbolically first; 374,6 → 3,7·10² J/(kg·K) and the 24,6 °C → 383 J/(kg·K) sensitivity both correct; a lossless 0,200 kg copper body gives 24,6 °C as stated.
- Derivation of T = (c₁m₁T₁ + c₂m₂T₂)/(c₁m₁ + c₂m₂) correct; the misconception example (35 °C) and its weighted-mean check correct; ΔT in K = ΔT in °C stated.
- ennuste-1 numbers: sand 26,8 °C / 8,5 kJ, water 44,0 °C / 30,2 kJ, C = 160 and 838 J/K. ennuste-2: 40,0 / 55,0 / 63,1 °C, 50 K vs 20 K, ratio 2,5. All match.
- Etsi virhe (6,6 °C wrong, 30,0 °C right), siirto 29,1 kg with mistakes 220 and 21,3, tarkistus-2 891 J/(kg·K) with mistakes 768 and 501, tarkistus-1 (4500 vs 838 J/K, mass ratio 50), exit ticket (419 kJ, ratio ≈ 9, 65 °C): all correct.
- Figures: water-sand ΔT bars 20 px vs 105 px (ratio 5,25, c ratio 5,24) are to scale as claimed; c-bars at 93,5 px per 1000 J/(kg·K) match every table value within 0,5 px; calorimeter figure matches the example.
- Sim: Teq and Q follow the lesson formula; both temperatures relax with the same τ, so C_W(T_W − T_W0) = C_B(T_B0 − T_B) holds at every instant (energy conserved during the illustrative approach); the timescale is labelled illustration only.
- Experiments: koe-1 locks everything but c (measures Teq, CB), koe-2 everything but m_B; all initial values lie within the sliders and simState carries the measured keys.
