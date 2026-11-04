VERDICT: PASS
CONTENT-HASH: c36b87a99d9ffab9

## Blocking

## Polish
- solutions.md:106 (L3-02) — the "Kaava" line still says "maksimitehopisteessä $U = RI$" (the Periaate now says correctly that it applies to the load). Write "kuormalle $U = RI$".

## Checked
- Round 2: diff cab03926 judged against the round-1 blocking items.
- L3-02: the data are now inline LaTeX pairs instead of a Markdown table, so the table no longer has to render. Recomputed: the maximum is 17,0 V · 2,90 A = 49,3 W, and R = 5,86 Ω matches answers.py.
- L2-01: the task now states the assumption that no current flows in reverse, and the solution's Annettu line repeats it. The 9,0 V answer is now conditioned consistently with the Järkevyys line's 5 V remark.
- L1-03: the Periaate now uses the given 0,70 V instead of "kynnysjännitteen suuruinen". The answer 8,3 mA is unchanged.
- No new errors. The other answers did not change, and the round-1 recomputation of all 12 still holds.
