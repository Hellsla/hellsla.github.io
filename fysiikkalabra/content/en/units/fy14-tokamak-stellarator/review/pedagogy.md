VERDICT: FAIL
CONTENT-HASH: 398b2cfa18a413c4

Pedagogy review of fy14-tokamak-stellarator (2026-11-01). Built with `scripts/build.py`. I read unit.md, inquiry.json and teacher.md, and looked at the 390 px captures (intro and the reactors explorer; the 1280 captures were missing when I looked).

## Blocking
1. `pred-toroidal` is answered on the page before it is asked. The intro (capture `intro-390`) shows:
   - the *Prior knowledge* line "Charged particles drift across a curved magnetic field that is stronger on one side; a ring has no open ends";
   - the first goal, "explain why a magnetic fusion machine needs twisted field lines".

   Together they state that a purely toroidal field fails and that the plasma drifts. The previous unit also taught exactly this (Torus section, `order-ring`, check-explain). The "prediction" is therefore retrieval with the answer on screen. Fix either way:
   - (a) Keep the item as a `review`-style retrieval choice. Write a new prediction the student can argue about, for example: "Wendelstein 7-X has no central solenoid and no large plasma current. Where can its twist (poloidal field) come from?" Or: "What happens to a tokamak plasma if its current suddenly stops?" Reveal it with `theory-designs`.
   - (b) Remove the drift statement from `prior`. Reword goal 1 as "explain how a tokamak and a stellarator confine a plasma in a ring". Change the review feedback so that it does not hint "whether that is enough".

## Polish
2. `pred-pulse`: "Must a tokamak therefore *always* run in pulses …?" The word *always* signals the answer "No". Ask neutrally: "How long can a tokamak hold its plasma current?" with options such as only a few minutes / as long as the solenoid current keeps changing / as long as something else drives the current / for ever once started.
3. `compare-talk` asks for "one advantage and one drawback of each design that you found in the drawing". The explorer's side-by-side table lists these word for word (capture fx-1-390-2), so the task is copying. Ask for a reason instead, for example "Explain *why* the tokamak risks disruptions and the stellarator does not, and *why* that makes steady operation easier for one of them."
4. teacher.md, Investigate: "the short checks inside the component" do not exist on this page, because the component is set to `"checks": false`. Remove the phrase, or say that the unit's own checks replace them.
5. French corner:
   - the respelling style (*luh koo-RAHN*, *ahn kon-tee-NY*) differs from the passed units' shared style (italic, Finnish letters, õ/ã/ẽ), and *RAHN* and *ahn* suggest a sounded *n*;
   - *gn* is compared with English *canyon* here but with Finnish *nj* in fy14-magnetic-confinement. Use Finnish in both;
   - the last tip has no full stop.
6. Workload: the core theory is about 650 words, above the guide's 500 but in three short parts. The explorer is read in pairs, and the pulse table can be skipped. 75 minutes is realistic.

## Checked
- The hook, Why line and hero (no words) do not give away `pred-pulse`. The reveals are tied to theory sections that come after the explorer and the table, which act as evidence.
- The explorer is usable at 390 px. Layers and step cards let students act on the model.
- Non-inductive drive is taught, as the brief demands.
- Word bank and starters before both argue tasks. The chapter's question is answered in check-explain, with a measured result separated from a plan.
- The worked example and the field task have full solutions and mistake feedback (including the turns of a single coil).
- teacher.md has plans for fast pairs and for running out of time.
