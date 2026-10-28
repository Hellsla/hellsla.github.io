VERDICT: FAIL
CONTENT-HASH: a9811cc31ee4fe1e

## Blocking
- inquiry.json:137 and inquiry.json:173 — A: the activities `ketju` and `kaukolampo` carry `"source": "simulated"` (badge "Simuloitu esimerkkiaineisto: produced by a simulation"), but the lesson has no simulation (sim-spec: "Ei simulaatiota") and the numbers are invented example values (source_note says so); the badge states a false provenance (guardrail: say whether each number is measured, simulated or calculated) — set `"source": "example"` on both.

## Polish
- lesson.md:73, inquiry.json:222, exit-ticket.json:12 — a hydro plant's energy is described as "virtaavan veden liike-energia" taken "suoraan"; the energy comes mainly from the head (the water's drop height), which the turbine takes as pressure and motion. Since E_p is FY4, write "veden mekaaninen energia" (or "putoavan veden energia"); the explanation's key point (not a heat engine) is right.
- inquiry.json:353 (check-1, correct feedback) — "poltettavaa hiiltä tarvitaan 2,5-kertainen määrä sähkön energiaan verrattuna" compares a quantity of coal with an energy; write "hiilen energiaa tarvitaan 2,5-kertaisesti".

## Checked
- Recomputed in one script: worked example (0,38038; 228 MW; 38,0 %; 372 MW; condenser 306 MW; boiler 54 MW, generator 12 MW), ketju 248,4 MW with mistakes 270 / 211,6 / 288,4 / 300, kaukolämpö 48 MW (mistakes 280 / 168 / 240), välitila 130 MW and 0,76, virhe 342 MW and 540 MW, siirto 8,64 MW (mistakes 20 / 164), check-2 216 MW, kertaus 520 MJ and 0,35, exit ticket 0,432 / 85 % / 15 MW, misconception mean 0,78 vs product 0,40.
- Figures to scale: Sankey 0,4 px/MW (500 = 200 + 40 + 248 + 12, scale bar 40 px = 100 MW), stacked-area chart (160→120 MW electricity, 240→48 MW waste, 232 MW heat), stage bar chart 500/460/211,6/200 MW.
- Exactly one correct option in kertaus, pred-1, pred-2, tyypit, virhe, check-1; distractor feedback physically right (back-pressure lowers turbine work; grid losses a few per cent).
- Efficiency guardrail wording respected: losses of the heat engine "ei voi kokonaan välttää", η ≤ 1 reasoning, CHP total efficiency kept apart from electrical efficiency and value of heat vs electricity.
- P_L = c q_m ΔT with Q = cmΔT condition (water only warms); condenser heat called the largest part of the waste, not all of it.
- Rounding reasons consistent with the data; tolerances admit correctly rounded answers.
- Scope inside FY3 (energy conservation, efficiency, heat).
