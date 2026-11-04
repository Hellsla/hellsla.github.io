VERDICT: PASS
CONTENT-HASH: b57c3875fe94cbd2
Mode: delta (en lesson wording change in inquiry.json)
Round 2

## Blocking
(none)

## Polish
- (Minor) Fixed: slider label 'Resistance of charger and wires R = ...' fits 360 px on one line (sim-390); same wording in the experiment names.
- (Minor) Figure 13 label 'stored in the battery' is clearly within its box.

## Checked
- Recaptured en shots; contact sheets, sim at 390 px, experiments 1 to 3, figures 5, 7, 9, 11, 13, hero: no overflow, maths renders, no Finnish left.
- Re-review: fy6-9-sim-390.png and fy6-9-sim-1280.png show the charger voltage on the circuit canvas as U_ch (earlier blocking U_lat finding resolved by the lang keys sims.fy6-9.ulat_lab / ulat_eq); sliders, readouts and canvas all read U_ch, nothing overflows or clips at either width.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
- Re-review after the concept-review commit: howto wording (electrical energy transformed into internal energy), efficiency paragraph (often below 100 %, charging always, R and R_s), L3-03 sisäenergiaksi, matching the Finnish; no numbers changed; $ counts equal.
- Delta re-review: slider label for R is shorter ('charger and wire resistance'), the intended 360 px overflow fix; wording only, no numbers or symbols changed; layout of the sim panel is not harmed by the shorter text (it is shorter than the earlier label that already fit at 390 px).
