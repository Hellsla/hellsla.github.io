VERDICT: PASS
CONTENT-HASH: fb4a6839555b1dd9
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the FY7 editorial-correction diff since origin/main only; round 2 after the fixes to the round-1 findings)

## Blocking
- none

## Polish
- [Minor] solutions.md L1-05 Periaate — "koska vaiheiden jännitteet ovat eri vaiheissa" is close to a tautology and the causal link is loose; e.g. "Vaihejännite on $U : \sqrt{3}$, koska vaihejännitteiden välillä on $120^\circ$:n vaihe-ero. Kukin vaihejohdin siirtää tehon $(U : \sqrt{3}) \cdot I$, joten kokonaisteho on …"

## Checked
- Source diff since origin/main plus the round-2 diff (scratchpad round2.diff); no screenshots in light mode (parent runs the layout checks).
- Round-1 blocker fixed: L1-05 Sijoitus "$P = \sqrt{3} \cdot 400\,000\,\text{V} \cdot 800\,\text{A} \approx 554\,260\,000\,\text{W} = 554{,}26\,\text{MW}$" (en 554.26) is now correct: √3 · 3,2·10⁸ W = 554 256 258 W ≈ 554 260 000 W; Vastaus 554 MW (3 s.f.) and the stored answer 554.2563 agree.
- L1-05 Periaate: phase voltage $U : \sqrt{3}$ and total power $3 \cdot (U : \sqrt{3}) \cdot I = \sqrt{3}\,U I$; LaTeX, division colon and \cdot per house rules.
- Two-wire sentences in the other tasks and solutions unchanged since round 1.
- Hash identical at start and end of this round.
