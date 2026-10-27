VERDICT: DONE
Round 1, simulation redone before review (coordinator's finding: one object at a time). check_lesson.py all ok; test_sims.py 205 assertions.
- assets/sims/fy1/fy1-1/sim.js: "Scale of the Universe" layout. Every object from about 1/2000 to 3 times the view width is drawn at once, to scale, side by side on the ground in size order; a larger one is cropped (limb arc), under 4 px a dot with a leader line; smooth fades; staggered/shrunk labels never overlap or leave the canvas (scanned L = -34 … 27,5 in steps of 0,1 at 360/390/1280 px). The ±10 buttons and arrow keys glide one power of ten. 40 objects now (21 new, so 2–5 are in view at every L except the physical gaps below). Sun granules no longer flicker.
- lang/fi.json sims.fy1-1: 21 new object names. tests/sims/fy1-1.json: visibility and glide tests updated, new tests per object and 2–5 objects at 14 scales.
- inquiry.json (sim activity text, howto, model, calc) and sim-spec.md: wording follows the new behaviour.
Known gaps: L = -31,5 … -15,3 shows 0–1 objects (no known sizes between the Planck length and the proton; readout says so).
