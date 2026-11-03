VERDICT: PASS
CONTENT-HASH: bf91c53f5e3e3250

## Blocking

## Polish
- L3-01 — the task could say "Maan ja Kuun välillä", because a second equal-force point exists beyond the Moon. The trip "Maasta kohti Kuuta" and the solution's "Maan ja Kuun välissä" already rule it out. Optional.

## Checked
- The round-1 blocking item is fixed: L1-02 Periaate now says the point-mass model is the task's assumption and the result is only an order-of-magnitude estimate.
- Round-1 polish is fixed: L1-02 says 250 g, L2-04 says "lentokorkeudellakaan", and L1-03 and L1-04 store 3.70 and 3.80. L1-05 Järkevyys ("alle kolmasosaan") and L2-01 ("samanmassaisen") still read correctly.
- I recomputed all 12 answers in one script with my own formulas: 0,401 µN, 2,50 N, 3,70 m/s², 3,80 kN, 4,0 µN, 37,9 kg, 0,8154, 15 488 km, 0,3440 %, 3,456·10⁵ km, 19,6 m/s², 177,4. They match exercises.json, and answers.py gives the same output.
- The models fit the situations:
  - point masses are stated where they are used;
  - spherical symmetry with r measured from the centre;
  - γ and M cancel correctly in the ratio tasks.
- Every unknown is solved symbolically before substitution.
- The reasonableness checks are real checks (lead sphere 9 cm, 2h/R, √81 = 9, 390²).
- Data are realistic, and the significant figures follow the limiting datum.
- Notation matches the lesson (γ, R, G = mg). Scope is inside FY5; L3-02 uses sphere volume, which Level 3 allows.
- The 2 % tolerances fit the data.
