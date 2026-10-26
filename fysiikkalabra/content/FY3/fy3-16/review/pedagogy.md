VERDICT: PASS
CONTENT-HASH: 7b642f39b87c6795

## Blocking
(none)

## Polish
- lesson.md Ydinajatus (sauna paragraph) and Yleinen virhekäsitys (ice-water mixing) — the teacher's "simple figure wherever visualisable" rule is met only for the cooler and the coolant loop; a two-bar picture (67 kJ vs 452 kJ) beside the sauna paragraph and one (126 kJ available vs 334 kJ needed) for the mixing case would finish it.
- inquiry.json `loyly` — the student only divides two values already given in the theory (67 and 452 kJ appear there); consider a choice about where the energy goes, or cut it, since sauna numbers recur many times.
- inquiry.json `pred-2` — one proportion with no tempting wrong model besides the percentage one; the table checks consistency (Pt = sm) rather than refuting. Acceptable; `reflect` already names this.
- exercises.json L3-03 — now varied (ice at -10 °C, warm drinks, target time), no longer table lookup; fine. L1-05, L2-03 now LaTeX for c.
- The inquiry graph (t0 about 3,7 h, UA 0,90 W/K) and the Kaava graph (2,4 h) show different cooler set-ups; the text says which, so it is not blocking, but one line "toinen laukku" in `kayra` would avoid a moment's confusion.

## Checked
- Round-1 blocking fixed: all figure labels (jää, sulaa, +10 K, bar values, axis ticks, t0, moottori, jäähdytin, T1, T2, P, m/t) are LaTeX foreignObject; no SVG `<text>` left in lesson.md or inquiry.json.
- Captures at 390 px: three figures recognisable, uncluttered, colour paired with labels, legible; 1280 px puts the figure beside its paragraph.
- Hook now says "viileitä"/"sama teho alussa"; Finnish slips from round 1 ("kuluessa", decimal commas) corrected.
- Path: hook, retrieval, predictions, graph and table, theory, reflect, staged example (five stages, symbolic first), error-spotting, transfer, three checks, exit ticket, Tehtävät last; slot goals (cooler, sauna, coolant) covered, no more.
- Opening question answered only after commitment; Ennuste closed, options shuffled, speakers varied.
- Exercise levels 5/4/3, none repeats the example; solutions in LaTeX; no lesson ids in student text.
- Numbers spot-checked: 2,4 h, 333 vs 334 kJ, 86 %, 65 s, 1,5 kg.
- No simulation, justified by topic; workload one lesson.
- 360/768/1280 px: 390 px and 1280 px captures read; the 360 px fit is tested.
- Hash unchanged at end.
