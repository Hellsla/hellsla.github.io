VERDICT: PASS
CONTENT-HASH: c56abff2c3e9e364

## Blocking

## Polish
- solutions.md fy3-15-L3-05 Reasonableness: "…only a few per cent, but the energy has not disappeared: it warms the sea" chains two colons in one sentence. Fix: start a new sentence at "The energy has not disappeared; it warms the sea." This is style only.
- solutions.md fy3-15-L3-05 (line 215): the heading "Reading the graph" introduces a table. Fix: "Reading the table". Carried over.
- solutions.md fy3-15-L1-05 (line 49): "all powers are given to the nearest megawatt" does not fit 75.0 MW. Fix: rest the three figures on 225 MW and 250 MW. Carried over.
- solutions.md fy3-15-L1-09 (line 229): the row ends at 13.4 MW but the answer is 13 MW. Fix: end the row at 13 382 kW ≈ 13 MW. Carried over.
- exercises.json fy3-15-L1-01: "kinetic energy of the water" is a C simplification (the water's head is what the turbine mainly uses). Optional fix: "energy of the flowing water". Carried over.

## Checked
- The hash was c56abff2c3e9e364 at the start and the end.
- Delta (fy3-15-L3-05): d) now says "in practice no longer be used to produce electricity". The Reasonableness line adds that with so small a temperature difference the largest possible efficiency would be only a few per cent. This matches the Finnish version.
- "in practice" is the correct qualifier: low-grade heat is uneconomic, not unusable in principle. The added limit gives the real reason and is consistent with the guardrail that a heat engine cannot turn all of its heat into work.
- I recomputed the bound from the task data in one script. Outlets at 12.1 to 28.4 °C with rises of 10.6 to 10.9 K give 1 − T_c/T_h = 3.5–3.8 %, and about half that for a stream that cools as it gives off heat. "a few per cent" is therefore right as an upper limit.
- The unchanged numbers recompute as before: ΔT_avg = 10.775 K, P_L = 1716 MW (answer 1720 MW, tolerance 2 %), P_h = 1800 MW, share 95 %, remainder 84 MW.
- No number, symbol or answer changed. Energy conservation is still stated explicitly ("it warms the sea").
- Scope: the limit is stated, not asked for, so the task stays within FY3 and its prerequisite chapter on the heat engine.
