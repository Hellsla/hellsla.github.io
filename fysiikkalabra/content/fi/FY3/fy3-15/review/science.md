VERDICT: PASS
CONTENT-HASH: 1c22f1cf8a9689bc

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking

## Polish
- lesson.md:73, inquiry.json:222, exit-ticket.json:12 — a hydro plant's energy is described as "virtaavan veden liike-energia" taken "suoraan"; the energy comes mainly from the head (the water's drop height), which the turbine takes as pressure and motion. Since E_p is FY4, write "veden mekaaninen energia" (or "putoavan veden energia"); the explanation's key point (not a heat engine) is right.
- inquiry.json:353 (check-1, correct feedback) — "poltettavaa hiiltä tarvitaan 2,5-kertainen määrä sähkön energiaan verrattuna" compares a quantity of coal with an energy; write "hiilen energiaa tarvitaan 2,5-kertaisesti".

## Checked
- Round-1 Blocking resolved: `ketju` and `kaukolampo` now carry `"source": "example"` (invented example data, badge "Keksitty esimerkkiaineisto"), matching their source_note and the lesson having no simulation; no `simulated` badge remains.
- The diff changes only those two lines; no numbers, options, feedback or solutions changed.
- From the full round-1 review (unchanged content): worked example 228 MW / 38,0 % / 372 MW, ketju 248,4 MW, kaukolämpö 48 MW, välitila 130 MW, virhe 342 MW, siirto 8,64 MW, check-2 216 MW, exit ticket 0,432 / 85 % / 15 MW all recomputed right.
- Figures to scale (Sankey 0,4 px/MW, stacked-area chart, stage bars); exactly one correct option in every choice item; efficiency and CHP guardrails respected; scope inside FY3.
