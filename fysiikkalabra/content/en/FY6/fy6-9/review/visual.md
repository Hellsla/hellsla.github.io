VERDICT: FAIL
CONTENT-HASH: c932c0f64f57fc50

## Blocking
- [Major] The sim circuit canvas shows the charger voltage as U_lat (Finnish subscript), see review/shots/fy6-9-sim-390.png and fy6-9-exp-koe-3-390-1.png; the slider and readout say U_ch. The label is hard-coded in assets/sims/fy6/fy6-9/sim.js line 116: lab('$U_\text{lat}$', ...). Fix (outside translation scope; assets/ is off limits to the reviewer): take the label from lang (a new key such as sims.fy6-9.ulatkuva, $U_\text{ch}$ in en, $U_\text{lat}$ elsewhere) with __(). Until then the en page has Finnish in the sim.

## Polish
- (Minor) Fixed: slider label 'Resistance of charger and wires R = ...' fits 360 px on one line (sim-390); same wording in the experiment names.
- (Minor) Figure 13 label 'stored in the battery' is clearly within its box.

## Checked
- Recaptured en shots; contact sheets, sim at 390 px, experiments 1 to 3, figures 5, 7, 9, 11, 13, hero: no overflow, maths renders, no Finnish except the U_lat canvas label.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
