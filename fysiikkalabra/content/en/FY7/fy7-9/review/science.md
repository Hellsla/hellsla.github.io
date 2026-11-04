VERDICT: PASS
CONTENT-HASH: b7d2af821abef4eb

## Blocking

## Polish
- inquiry.json:90 (ennuste-huone, "does not radiate" feedback) — "the stone just radiates infrared" can be read as "only infrared"; "the stone radiates mainly infrared" matches the correct option and the lesson ("almost only infrared"). Carried from round 1, C if left.

## Checked
- Round-1 blocking fixed: sim.js:150 draws the region label through `__('alue_ir')`; lang/en.json gives "$\text{infrared}$", fi/fi-easy "infrapuna". review/shots/fy7-9-sim-1280.png (5800 K, short range) shows "infrared" on the canvas. No other hard-coded canvas words (only units, UV, max).
- Shortened en legend ("The colour band is visible light; the dashed line marks the peak wavelength.") still describes the drawing correctly.
- One script (scratchpad sci/recompute_r2.py), own Planck peak from x = 5(1 − e^−x): 966/644/483 nm at 3000/4500/6000 K, 9659 nm at 300 K, curve peaks 724/580/483 nm at 13.2/40.2/100 MW/(m²·µm); visible share 10.9 % at 3000 K (koe-1 capture), < 0.01 % at 300 K (koe-2 capture).
- Text: 3.0 m, 12 cm, 4.0·10¹⁴ / 7.9·10¹⁴ Hz; 9.66, 9.44, 3.62 µm; 502 nm; worked example 5773 K → 5.77·10³ K.
- virhe 2.47 vs 3.22 µm, bT = 2.61 m·K²; siirto 1072.08 nm (mistakes 1192.59, 1.07208); tarkistus-2 1380 K → 1106.85 °C (mistakes 1380, 1653.15); 5800/307 ≈ 19; exit ticket factor 1/3.
- Conditions kept: black-body assumption stated in example, siirto and tarkistus-2; absolute temperature; Wien approximate for real bodies; accelerated charge as source; sim readings called model values.
- Each choice item has exactly one correct option; distractor feedback names the real error.
- koe-1/koe-2 initial states, locked range and measured key lmax match simState.
- check_layout.py fy7-9 --width 340: en OK, no formula overflow.
