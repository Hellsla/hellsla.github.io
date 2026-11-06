VERDICT: FAIL
CONTENT-HASH: bbc9cb838c12abd5

## Blocking
- fy6-8/exercises/exercises.json:321-335 — the correct option is identifiable by form: "1,55 V" appears in three of four options and "0,40 Ω" in two, so the only option combining both is the key; a student can pick it without reading the table — rebuild so each value appears equally often, e.g. A 1,51 V/0,40 Ω, B 1,55 V/0,40 Ω (correct), C 1,51 V/1,3 Ω, D 1,55 V with a changing-resistance claim whose figure is also decoy-balanced (or give D E = 1,51 V).

## Polish
- solutions.md:206 and exercises.json:335 — "mahtuu kahden lukeman epävarmuuteen 2 · 0,01 V" miscounts: comparing two drops involves four readings (± 0,04 V) - say so; the conclusion only gets stronger.
- exercises.json:280 — the lesson says E and Rs of a real battery do change slightly with current, so option D is rejected only by the data; add "mittauksista ei voi päätellä" to the feedback.
- exercises.json:280 — same procedure as L2-05 (fit line, read E and Rs, slope uncertainty); differentiate by asking only for the supported conclusion.

## Checked
- Numbers recomputed: drops 0,08 / 0,07 / 0,09 / 0,08 V; end-point slope 0,40 Ω; E = 1,51 + 0,04 = 1,55 V; least-squares line 1,552 V and 0,40 Ω; U : I = 1,3 Ω for the last row - correct.
- Distractors catch the lesson's warned mistakes (E read at smallest I, R = U : I of a load) and the data-versus-uncertainty trap.
- Data caption short; uncertainty given; unit of each column in the header; level 2 data task fits the lesson (slope from far points).
- Longest solution formula 249 px (fits).
- Text only (no renders: packet screenshots were empty; I measured widths of the model-solution formulas with KaTeX in Chromium at 17 px, 390 px viewport).
