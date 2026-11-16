VERDICT: FAIL
CONTENT-HASH: 6ef02eec981df84d
Mode: full (round 1)

## Blocking
- solutions.md:101 (L2-01) and solutions.md:286 (L2-06) — **B**: "Mitattu kynnysjännite on yleensä noin 0,1 V tätä arviota pienempi" / "kynnysjännite on yleensä noin 0,1 V pienempi kuin hf/e" state the 0,1 V gap as a general property of LEDs. The lesson says the opposite in so many words: the gap is about 0,1 V in this chapter's data sets, "ei yleispätevä arvo", and it varies from LED to LED. — Say what the lesson says: "yleensä hieman pienempi; tämän luvun aineistoissa ero on noin 0,1 V". (Line 287, L3-04 and L3-05 are fine.)

## Polish
- exercises.json:71 and solutions.md:216 (L1-06) — "fotoneja ei synny lainkaan" below the threshold, while L2-05's table has 0,1–0,6 mA below U_k = 1,86 V and L2-06 says a current flows before the threshold — "ei juuri lainkaan", as the lesson's "ei juuri johda virtaa eikä säteile".
- solutions.md:148, 297 (L2-04, L2-07) and 286 (L2-06) — three significant figures justified "kuten aallonpituuksissa/jännitteissä", but the result is a difference of nearly equal numbers (Δλ = 20 nm, 2,756 − 2,214 eV, 6,868 − 6,626), so the limiting precision is that of the difference — give that reason; the tolerances already accept the two-figure result.

## Checked
- All 19 numeric answers recomputed with my own formulas in one script: equal to answers.py and to exercises.json within half the tolerance; units fit.
- Least-squares fits redone: L2-05 k = 61,5 mA/V, U_k = 1,857 V; L3-01 4,212e-15 V s, b = −0,164 V; L3-04 4,208e-15 V s, b = −0,062 → −0,112 V, slope unchanged by the zero error; L2-08's stated k, Δk and intercept agree with its table (3,98e-15, 0,21e-15, −0,07 V).
- L2-08 and L1-06: exactly one correct option; each distractor is wrong and its feedback gives the right reason (Δh = eΔk = 0,34e-34 J s, difference 0,25e-34 J s); "sopusoinnussa", not "equal".
- L2-04 (the changed line): the photon-energy difference stays in the phosphor as internal energy: correct term, 0,541 eV, about a fifth.
- Data realistic (GaAs 873 nm, UV LED 22 %, thresholds 1,86–2,64 V); assumptions stated in L1-07, L2-02, L2-03, L2-06; scope inside FY8 (E = hf, eV, fitting).
- L2-06 and L3-05 side results (−11,6 %, −4,5 %, 504,1 nm, Δλ = 9,5 nm) recomputed; solutions symbolic first, conversions right.
- Hash identical at the start and the end.
