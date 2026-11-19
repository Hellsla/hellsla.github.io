VERDICT: PASS
CONTENT-HASH: eb8a72b4ee6e40f2

## Blocking

## Polish
- assets/sims/fy5/fy5-13/sim.js:68 (unchanged from round 1): with the open pipe, A rises toward the bottom of the slider because cot kL diverges as f → 0. This is the uniform n = 0 motion, and a student may read it as a resonance below f1. Add one clause to the `model` box, or clamp f to above about 0,3 f1.
- inquiry.json `model` box (unchanged from round 1): off resonance the driven end moves the most and is marked K. One sentence saying so would stop students reading it as a broken end condition.

## Checked
- inquiry.json:118 `calc`: "avoimessa päässä se on suurin ominaistaajuuksilla" is right. I recomputed the closed pipe with α = 0,06/L. At 100, 300 and 500 Hz, |U| at the open end equals the maximum, 16,69 mm. At 200 and 400 Hz the open end gives 0,06 mm against a maximum of 1,0 mm. Off resonance the open end of the open pipe is still at the maximum, and "ominaistaajuuksilla" does not deny this.
- inquiry.json:175 koe-2 intro: restricting the end question to the peaks matches what the sim shows at 200 and 400 Hz (a node at the open end).
- inquiry.json:273 conclusion model: "Huipuissa suljetussa päässä oli aina solmu ja avoimessa kupu" now matches the koe-2 table and fixes my earlier polish item. The numbers are unchanged: 16,7 mm, 1,0 mm, 100/300/500 Hz and 2/3/4 nodes.
- The diff changes no number, symbol or option, so the round 1 recomputations still hold.
- Hash eb8a72b4ee6e40f2 at the start and at the end.
