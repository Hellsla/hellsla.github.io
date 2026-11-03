VERDICT: PASS
CONTENT-HASH: 92a5b4a05f31aa7b

## Blocking
(none)

## Polish
- [Minor] sim-390 / sim-1280 — the readout's first line (force of the spring on the trolley … force of the hand on the trolley …) wraps mid-formula at 390 px; it stays legible. Keep as is or shorten in lang/en.json if it bothers.
- [Minor] fig-2 (hand pulls spring) and the sim keep the Finnish-origin subscripts v and k; explained in the text now.

## Checked
- contact-1…contact-6 at readable size; fy5-8-sim-390, fy5-8-sim-1280, fy5-8-exp-exp-1-390-1.
- Figures fig-1…fig-8: all English words drawn from figures.json (equilibrium position, stretched, rest length, compressed, situation, hand pulls spring, spring pulls hand); decimal points on axes (0.025, 0.050 …); no clipping.
- Worked example (example-390 in contact-1 #10–#12): staged, aligned chains, answer and check blocks.
- Exercises and opened solutions (contact-5, contact-6), free-body diagram in L3-03 rendered with English-neutral labels.
- check_layout.py fy5-8 --width 345: OK for preview/en/fy5-8.
- Alt texts translated (figures.json), British spelling, LaTeX units with thin spaces.

## Scores
illustrations 5 · typography 5 · English 5 · accessibility 4
