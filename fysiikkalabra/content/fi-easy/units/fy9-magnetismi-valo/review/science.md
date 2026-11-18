VERDICT: PASS
CONTENT-HASH: 43b392b3a623282a
SCOPE: delta: round 2, the fixes of round 1 in fy9-magnetismi-valo-s8 and -s9; s1-s7 and the intro untouched, not re-judged.
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
None.

## Polish
- s9 b: the chain now rounds its intermediate values ($0{,}405 \to 0{,}41\,\text{W}$, $0{,}288 \to 0{,}29\,\text{J}$). The result is unchanged ($0{,}372$ or $0{,}369$, both $\approx 0{,}37\,\text{J}$). This is the same chain as in the standard Finnish text, and no error.
- s9 Yleisiä virheitä line 1 lists only the mistake "$5{,}0 - 3{,}0\,\text{mWb}$". The standard text also names using only the final value $3{,}0\,\text{mWb}$. The physics is right, and this was unchanged in round 1.

## Checked
- `units.py hash --lang fi-easy` gave 43b392b3a623282a at the start and at the end. Packet check: `practice.py check: OK`.
- Round-1 Blocking item, s9 Yleisiä virheitä line 2: it now reads "jännite on tuhatkertainen ($2400\,\text{V}$ oikean $2{,}4\,\text{V}$:n sijaan)". This is right: $120 \cdot 8{,}0 / 0{,}40 = 2400$. Fixed in solutions.md line 658 and in the packet.
- Round-1 Polish, s8 line 1: it now reads $0{,}30 : 0{,}45$, which gives $0{,}67$. This is right.
- I diffed against the round-1 commit (ad5dcedf). The changes are:
  - s9 b: aligned chain rows with the power row added (solutions.md and the tasks.json detail).
  - s9 text: the sign convention is reworded.
  - s9 c: the question is reworded and still does not reveal the answer.
- In the solution of s9 b, the short sentences keep every causal step:
  - constant flux gives zero voltage and zero current;
  - $P = e^2/R$;
  - $W = P\,\Delta t$;
  - "muuttuu sisäenergiaksi" (P1).
- My recomputation script:
  - s9: $2{,}4$ and $1{,}8\,\text{V}$; $0{,}72$ and $0{,}405\,\text{W}$; $W = 0{,}369 \approx 0{,}37\,\text{J}$; $0{,}25\,\text{s}$.
  - s8: $n = 1{,}5$; $2{,}0 \cdot 10^8\,\text{m/s}$; $42^\circ$.
- The numbers match the standard Finnish text.
- Nothing newly broken:
  - two significant figures, matching the data;
  - the unit fields are unchanged and language-neutral;
  - no formula or method is named in the task text.
