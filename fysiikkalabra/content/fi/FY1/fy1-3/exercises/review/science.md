VERDICT: PASS
CONTENT-HASH: f6ea8ce2311e052c

## Blocking

## Polish
- solutions.md L1-02 Vastaus — the task asks for the sign, so give $+0{,}3\,\text{cm}$ (the Sijoitus line already does). The closing guess "todennäköisesti systemaattinen" rests on one reading; "voi olla systemaattinen" is safer.
- exercises.json L1-03 — a student who applies the lesson's rounding enters $0{,}4\,\text{s}$, which is 14 % off with tolerance 0.02. The answer is not wrong, but a tolerance of 0.15 would accept both.
- solutions.md L3-02 — the chain ends at "$= 2{,}0\,\mu\text{m}$" while Vastaus gives "$2\,\mu\text{m}$". L3-01 says "lähes kokonaan" where two thirds of the delay cancels.

## Checked
- Round 2: re-check of round-1 Blocking items against the fix diff. (Round 3 follow-up: the leftover Δx notation.)
- L1-02 now writes mittausvirhe as $x - x_\text{oikea}$ in Kysytty, Kaava and Sijoitus, with no Δx. This matches the lesson. Δx is left only for uncertainties (L1-05, L3-02), and $\Delta x_\text{sys}$ (L3-03) keeps the lesson's own subscripted notation. The answer +0,3 cm, the unit and the tolerance are unchanged, and the solution still has its seven parts.
- From the round-1 full review, unchanged:
  - one script recomputed all 12 answers (0,51 s; +0,3 cm; 0,35 s; 47,5 g; 0,5 mm; 4,83 %; 10,67 mm; 12,4 cm; 10; −0,06 s; 2,0 µm; 0,26 cm), and all match answers.py;
  - the rounded answers stay inside the tolerances;
  - the guardrail terms are kept apart, and the scale-reading wording is the agreed one;
  - the physics of the zero-point error, tape wear, start/stop delays and stacking is right.
- Hash identical at start and end.
