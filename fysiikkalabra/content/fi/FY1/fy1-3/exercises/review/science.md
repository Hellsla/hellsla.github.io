VERDICT: PASS
CONTENT-HASH: 9c0e2ae1f4be967f

## Blocking

## Polish
- solutions.md L1-02 vs L1-05 / L3-02 — $\Delta x$ stands for the signed mittausvirhe in L1-02 ($\Delta x = x - x_\text{oikea}$) and for a positive uncertainty in L1-05 and L3-02. This mirrors the lesson's double use of the symbol, which is a Blocking item in the lesson's science review. When the lesson renames the error, change L1-02 to match, for example "virhe $x - x_\text{oikea} = +0{,}3\,\text{cm}$".
- solutions.md L1-02 Vastaus — the task asks for the sign, so give $+0{,}3\,\text{cm}$. The closing guess "todennäköisesti systemaattinen" rests on a single reading; "voi olla systemaattinen" is safer.
- exercises.json L1-03 — a student who applies the lesson's rounding enters $0{,}4\,\text{s}$, which is 14 % off with tolerance 0.02. The task asks for the half-range itself, so the answer is not wrong, but a tolerance of 0.15 would accept both.
- solutions.md L3-02 — the chain ends at "$= 2{,}0\,\mu\text{m}$" while Vastaus gives "$2\,\mu\text{m}$". L3-01 says "lähes kokonaan" where two thirds of the delay cancels.

## Checked
- Changes since the last pass are correct and match the guardrails:
  - L1-05 and L3-02 now say "lukeman epävarmuudeksi arvioidaan puoli asteikkoväliä" and mention the total uncertainty;
  - the over-absolute "ei voi olla asteikkoväliä suurempi" is gone;
  - L2-02's unsound "one more digit" rule is replaced by 11 mm, with the spread of ±1,5 mm as the reason;
  - the numbers with units are now in LaTeX, and no value changed.
- One script recomputed every answer from the task text: 0,51 s; +0,3 cm; 0,35 s; 47,5 g; 0,5 mm; 4,83 %; 10,67 mm; 12,4 cm; 10; −0,06 s; 2,0 µm; 0,26 cm. All equal answers.py and exercises.json.
- Rounded answers stay inside the tolerances: L2-01 gives 5 % (3,5 % off, tolerance 4 %) and L2-02 gives 11 mm (3,1 % off, tolerance 4 %).
- Physics: zero-point and tape-wear errors are systematic and are corrected by subtraction; the opposite-sign start and stop delays (L3-01) are right; stacking divides the reading uncertainty by the exact count (L3-02, equal sheets stated); the units are converted before averaging (L2-03).
- The guardrail terms are kept apart: half-range = scatter (satunnaisvirheen arvio), mittausvirhe has a sign, repeatability is not correctness (L2-04 reasonableness).
- Every solution has all seven parts, symbolic first, with real reasonableness checks.
- Hash identical at start and end.
