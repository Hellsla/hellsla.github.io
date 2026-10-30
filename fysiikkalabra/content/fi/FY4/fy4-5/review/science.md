VERDICT: FAIL
CONTENT-HASH: 0277f559f7d013b3

## Blocking
- inquiry.json:231 (exp-2 question) — B: "tukivoima on työnnössä suurempi kuin paino 196 N" holds only for α > 0°. The experiment starts at α = 0°, where the student's own table shows N = G. — Add the condition, e.g. "…työnnössä vinoon kulmaan (α > 0°)…".

## Polish
- lesson.md:3 and the hero — the Miksi box and the picture use snow ("painunut syvälle lumeen"), but the hook and every inquiry activity use ice. Inside inquiry.json the ice is consistent: hook, predictions, sim, exp-1/2 and reflect. Match the hero to the hook.
- inquiry.json:18 and :488 — "kahvasta, joka osoittaa vinosti alaspäin": the handle rises backwards, while the push points down and forward. Write "työntää … kahvasta vinosti alaspäin". Pull/push is otherwise consistent: rope = pull, handle = push, F_y up or down.
- sim.js:59 — v is capped silently at 12 m/s while the readout still shows a = 5,00 m/s². State the cap or stop the run there.
- inquiry.json:180 (aineisto diagram) — the labels N̄ and F̄_y overlap.
- sim.js:139 — the F_x label touches F's arrowhead in push mode near 40° (carried over).

## Checked
- The 50 N rounding is justified correctly. inquiry.js shows values ≥ 100 to whole newtons (146,2 → 146), and G = 196 comes from the intro and the readout. Each is within ±0,5 N, so the difference is good to about 1 N, and F sin 30° confirms it. The 3 % tolerance fits.
- Recomputed every number in one script: worked example 2,96 / 71,8 / 46 / 5,5; pred-1/2; exp-1; aineisto 4,886; siirto and its mistakes; check-2 and its mistakes; check-3 52 / 148. All agree.
- sim.js implements N = G ∓ F sin α and a = F cos α / m, and 150 sin 80° < 196 N. simState has N, Fx and a. exp-1 locks tapa, F and m and varies α.
- Exactly one option is correct in each prediction, in virhe, in hissi a–d and in check-1. The feedback is right, and each wrong figure has one error.
- The inquiry diagrams were rendered and agree with the text. The exit ticket and the check-3 model are correct.
- Hash unchanged start and end.
