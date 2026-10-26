VERDICT: PASS
CONTENT-HASH: 227a1ba145001404

## Blocking
(none)

## Polish
- lesson.md Ydinajatus, figure 1 (hiukkasrivi) — the key step, that a particle swings further away than closer, is only in prose, and the cold and warm rows both show symmetric arrows. Pred-3 (Cem) and the model answer hinge on exactly this. Add the simple theory figure the teacher asked for: a potential-energy curve (steeper on the close side, gentler on the far side) with the mean position shifting right when the energy rises.
- sim canvas and readout (screenshot fy3-8-sim-390, fy3-8-lab-1280-1) — canvas labels "ΔL (mm)", "T (°C)", "välit 0 %" and the readout "ΔL = αL₀ΔT", "L₀" are plain text with Unicode or HTML subscripts, not maths. Under the 2026-10-26 rules (labels in LaTeX, symbols as maths) render them in maths type. The experiment intros, names and table heads ("L₀", "ΔT (K)", monospace) have the same issue. At 390 px the canvas text is about 9 px: enlarge.
- sim details — two folds with near-identical names, "Mallin oletukset ja selitys" and "Mallin oletukset": merge them.
- exercises L1-03/L2-03 — the model ties on numbers are fine. L2-03 solution "Järkevyys" says the rail "pitenee kumpaankin suuntaan" and then "yksi kisko ... raon leveyden verran": reword, since the student can read it as ΔL/2 or ΔL.
- inquiry.json olomuodot feedback — "0,36 cm³, 2,1 cm³ ja 11 cm³, 34 cm³" is a punctuation slip; write "0,36 cm³, 2,1 cm³, 11 cm³ ja 34 cm³". The correct option is also the longest in that item and in pred-3; shorten it.

## Checked
- Figures 1 to 3 at 390 px (fy3-8-fig-1/2/3-390): labels in maths type, symbols consistent (d₀, d, V₀, ΔV, L₀, ΔL), non-colour cues, "liioiteltu" stated, nothing clipped, close to the paragraphs they explain.
- Opening question is answered by the mikromalli, the formula and the bridge example; the slot's goals are covered, nothing beyond them.
- Prerequisite item (ΔT in kelvins) fits fy3-3; each wrong option's feedback repairs its misconception.
- Predictions 1 and 2 can be refuted by exp-1 and exp-2 (parameters locked, 2 or more records); pred-3 is only partly refutable by the sim, which shows the spacing growing but not the asymmetry. Acceptable.
- Worked example in four stages, units checked, 86 mm and 0.07 % are right; the error-spotting item and the thermometer transfer (44 mm) have correct numbers and three hints.
- Exercises: levels 1 to 3 are graded, none repeats the example, the answers and tolerances recomputed (2.9, -52, 0.85, 0.84, 0.34, 52, 3.0, 36, 23, 120, 20, 460), solutions in maths type with Annettu to Järkevyys.
- Exit ticket tests the formula, holes and the particle size misconception.
- 1280 px layout (top, lab) is two-column and readable; 390 px stages and experiments show no clipping.
- Chapter names are used instead of lesson ids.
- Workload is one lesson; the sim only computes the formula, so exp-1 and exp-2 confirm arithmetic, not emergent physics. Acceptable because the model is labelled as model values.
