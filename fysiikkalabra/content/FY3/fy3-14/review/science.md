VERDICT: PASS
CONTENT-HASH: 8f0b3f29f2c22cd5

## Blocking

## Polish
- lesson.md (aria-labels of the energy-bar and graph figures) — they write "26.6 °C", "25.1 kJ" and "35.5 kJ" with a decimal point, while the rest of the lesson uses a decimal comma. — Use 26,6, 25,1 and 35,5.

## Checked
- The diff since round 1 is notation only: johtopaatos model and criteria now use \text{v}$ instead of $\theta_\text{v}$, in line with the Kaava section. The physics is unchanged.
- All 12 exercise answers were recomputed independently and match answers.py and exercises.json within tolerance. L3-03 checked: the water gives at most 37,59 kJ, which is less than the 42,0 kJ the ice needs, so all the water freezes and T = −3,5 °C.
- Worked example: Q_v = 25 140 J and Q_j = 17 540 J give T = 6,05 °C. The "noin 19 °C without fusion" (18,7–19,3) and the two-thirds share (16,7/25,1) both hold.
- Inquiry numbers: ennuste-1 (75,3 g melted, 24,7 g left, limit 26,6 °C), ennuste-2 and koe-2 (5,9 g vs 18,5 g, difference 12,6 g, heating about 1/8 of melting), johtopaatos (62,4 g at 10 °C, 10,1 °C at 40 °C), virhe (−25,6 °C, 0,225 kg ice left), siirto 39,9 g (mistakes 43,9 and 438), tarkistus-2 40 °C (mistake 56), exit (66,8 kJ, 12,5 g).
- Experiments isolate their varied parameter. koe-1 varies TW0 with mW, mI and TI0 locked; koe-2 varies TI0 with mW, TW0 and mI locked. simState provides Tf and iceLeftG.
- sim.js: all four cases of solve() follow from energy conservation, including the all-frozen T formula and Qend. stateAt() orders cooling, freezing, warming and melting correctly. The illustrative time constant is stated in the model box.
- SVGs: graph break at 26,6 °C (152,8 px) and 40,1 °C at 80 °C, and energy bars at 6 px/kJ (25,1; 2,1 + 33,4) are to scale as claimed. The before/after figure gives 0,375 kg water and 0,025 kg ice.
- Solutions' sanity checks hold: L2-01 (25,6 °C without fusion, 46 %), L2-03 (6 %), L2-04 (T read to 0,1 K means about ±1 kJ/kg) and L3-01 (42 kJ/kg).
- Formulas state their conditions (Q_v ≥ Q_j, the partial-melt range, freezing) and stay within FY3 contents.
