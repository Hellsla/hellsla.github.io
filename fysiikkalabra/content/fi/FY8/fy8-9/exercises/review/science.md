VERDICT: PASS
CONTENT-HASH: 9d4ef2778f138504
Round: 2

## Blocking

## Polish
- solutions.md:125 fy8-9-L2-05 Vastaus: "tarkkuus noin ±8 %, koska nettomäärän 64 hajonta on noin √64 = 8" mixes two quantities. 8 counts is 12,5 % of 64, and its effect on T½ is 12,5 % : ln 4,42 ≈ 8 %. Fix: "nettomäärän 64 hajonta √64 = 8 (12,5 %) antaa puoliintumisajalle noin ±8 % epävarmuuden".
- fy8-9-L2-05 / plan: `kind` "graph" is dropped (round 1 Polish resolved that way). The plan's log-scale plot and the `fy8-9/pa-points` graph-reading task are still not in the set (carried over). Add a c) "piirrä nettopulssimäärät logaritmiasteikolla ja lue T½", or record the deviation in docs/exercise-bank/FY8.md.
- solutions.md:167 fy8-9-L3-02: "kolme merkitsevää numeroa kuten ajassa 10,0 min". The limiting datum is the net count rate 200, which has two figures (carried over from earlier rounds).

## Checked
- Hash 9d4ef2778f138504 at the start and at the end.
- Round 1 Polish: L2-05 hint now reads "hieman alle neljäsosaan … noin 23 %" (64/283 = 22,6 %), and the solution says "hieman yli kaksi puoliintumisaikaa". This is consistent: T½ = 149,2 s, inside the 6 % tolerance, and the log fit gives 150 s.
- L3-05 c) now asks "pienentää … aktiivisuutta nopeammin" and answers with λ_bio = 0,140 > λ_fys = 0,0864 1/d. This is correct, and it removes the misleading exposure claim.
- answers.py comments are now right: 16,29 %, 0,6953 → 0,695 mg and 6,97 %.
- L1-06: the reordered options still have exactly one correct, and `answer` matches it. L1-07 uses the colon form.
- L2-06: the solution split (a) check, then "Selitys kohtaan b)") is correct physics. Background does not decay, so the gross count reaches 100 at about 70 s.
- All new numeric answers match my own recomputation (L2-05 149,2 s; L3-05 T_eff 3,065 d, T_bio 4,96 d, 50,1 % / 16,4 %).
- Set 8/7/5 = 20 tasks, and the levels fit the plan. Apart from the L1-07/L1-02 similarity (acceptable), no new task duplicates an existing one.
