VERDICT: PASS
CONTENT-HASH: 78ca43a94673e3d9

Pedagogy review of fy14-magnetic-confinement (2026-11-01). Built with `scripts/build.py`. I ran it in Playwright at 390 px:
- committed both predictions;
- exp-field rows: 0.5 → 41.8 mm, 1 → 20.9 mm, 2 → 10.4 mm, 4 → 5.22 mm;
- exp-mirror rows: 10° and 20° false, 40°, 60° and 80° true.

There were no console errors.

## Blocking
None. Each prediction is tested by its own experiment, and both experiments can refute the prediction (a student who predicts "small θ turns back" sees 10° and 20° escape). The simulation is the investigation, not decoration.

## Polish
1. Option lengths in `inquiry.json`: the correct option is clearly the longest in four choices:
   - `review`: 82 against 56–59;
   - `find-error`: 78 against 46–56;
   - `check-1`: 77 against 48–63;
   - `check-2`: within the limit, but `exp-particles` is spread 28–51.

   Shorten the correct options, for example `check-1` "Its speed stays the same." and `review` "Its free charges feel magnetic forces.", or lengthen a distractor, so that each choice is within ±30 %.
2. `check-2` uses the same situation as the unit's orbit figure: a positive charge moving right, the field into the page, the force up. Its feedback even says "as in the figure". The check tests looking up, not the right-hand rule. Change the case, for example an electron moving up the page with the field out of the page (⊙). Adapt the options and feedback.
3. Simulation readout (shared file, see below): in the side view, the readout prints the mirror condition and the verdict ("inside the loss cone (θ < 30°), escapes through the end" / "trapped between the mirrors"). Students can fill the *trapped* column from the text without watching the orbit, and the rule they should infer from their table is printed for them. "How the calculation works" also states θ ≥ 30°. In experiments, hide the verdict line, or collapse it until the experiment has 3 rows. Then the evidence is the motion.
4. Workload: this is the heaviest unit of the four, with a simulation, two experiments, a pair conclusion, about 610 words of core theory, an ordering task and a three-step alpha task. The timing in teacher.md works only if exp-particles and find-error stay optional, as they are. Consider moving the *Electric field* checkbox mention out of `howto`, so that no one spends time on it in the core path.
5. French corner: the respelling style (*luh shahn mah-nyay-TEEK*) differs from the passed units (italic, Finnish letters, õ/ã/ẽ). *shahn* suggests a sounded *n* in a nasal vowel. Use the shared style.

## Checked
- The learning goals and prior knowledge do not answer the predictions.
- The reveals are gated on 3 rows. The conclusion is gated on both experiments, with a word bank and starters.
- The single-particle model is clearly separated from the collective behaviour of a plasma (theory, `model` box, check-3).
- The alpha task has a full solution and mistake feedback. teacher.md has plans for fast pairs and for running out of time.

## Shared issues
- `assets/sims/fy14/magnetic/`: the mirror verdict and the loss-cone rule are printed in the readout during experiments (Polish 3).
- Experiment tables show the raw `true`/`false` (already noted by the developer).
