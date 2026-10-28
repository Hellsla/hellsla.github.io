VERDICT: PASS
CONTENT-HASH: 897018d85cf70a95

## Blocking

## Polish
- sim.js canvas at 390 px — the energy-axis ticks (+50, +25, 0, −25, −50) and the "hidas ▬ nopea" legend render at roughly 8 px, and the bar values (+7, 0) are small beside the 16 px readout below; they read but strain. Raise the tick and legend KaTeX size one step on narrow widths (the bar value labels and Q, W, ΔU are fine).
- sim.js canvas, 1280 px — "hidas", "nopea", "eristetty seinä" are set in the KaTeX serif (`\text`) while the page and buttons are sans; consistent with the LaTeX-everything decision, but the small serif text is the thinnest thing on the canvas. Optional: `\mathrm` at the same size as T.
- inquiry.json `pred-2` — the correct option is the only one that names the law (ΔU = W) and is the longest; shuffling does not hide that. Shorten it or give a wrong option an equally formal wording.
- inquiry.json `koe-2` intro — on a phone the student must wait until T ≈ 293 K before recording; say what to watch (the T readout in the line under the canvas) so a student does not record too early.
- Workload — two predictions, two experiments, four sovella items, three checks, exit ticket and 12 exercises is the upper end of one lesson; acceptable because the experiments are short, but do not add more.

## Checked
- Sim captures 390 and 1280 px, initial and after a slow push (the preview run at both widths): no overlap between the T readout, legend, energy axis, the W arrow at the piston, bars and their values; the "V = 94 %" and "eristetty seinä" labels do not collide at 390 px.
- Canvas and readout LaTeX (T, ΔT, V, p/p₀, W, Q, ΔU) render and update live; the readout under the canvas is legible at both widths; no raw `$` strings.
- Legacy notes now in Käyttöohje, Mallin oletukset and Laskennan selitys; the visible lead is under 30 words; one legend line; all three boxes start closed and no needed control is hidden.
- Pohdinta question (pump air gets energy without heating) is answered by the reflect item and check-1 (valve cools); retrieval item uses only fy3-3.
- Predictions are refutable: koe-2 can contradict Aino and Cem, koe-1 the speed misconceptions; feedback gives numbers only after the commitment and repairs the misconception.
- Scope: first law only, no entropy or the other laws, no E_k/E_p theorems; W = Fs matches fy3-2.
- Figures 1–3 (fig-1 seen at 390 px): labels legible, Q and W directions shown by arrows with text, not colour alone.
- Worked example has four stages with one step each; exercises 5/4/3, none repeats the example; mistake values (6,6; 599,4; 230; 10) match the arithmetic.
- Finnish: glossary terms correct, case after number+unit correct (75 N:n, 300 N:n); no sentence needs correcting.
