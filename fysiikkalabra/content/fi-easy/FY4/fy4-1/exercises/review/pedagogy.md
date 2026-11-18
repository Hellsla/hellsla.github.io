VERDICT: PASS
CONTENT-HASH: 1500ef8744b0673d

## Blocking
None.

## Polish
1. solutions.md:136 (fy4-1-L1-06) — the new paragraph break leaves "Se ei kuvaa hidastuvaa liikettä." opening a paragraph with "Se" whose referent ("Suora, jonka kulmakerroin ei muutu") is in the previous paragraph — keep the sentence in the previous paragraph, or write "Vakionopeutta kuvaava suora ei kuvaa hidastuvaa liikettä."
2. solutions.md:213 (fy4-1-L3-04) — "Siksi mittausten toistaminen ei poista sitä keskiarvossa." starts a paragraph and "sitä" points back across the break — write "Mittausten toistaminen ei siksi poista mittakaavavirhettä keskiarvossa."

## Checked
- Round 1, delta: the Kaava-step rewrites judged in their context; no number, answer, unit or exercise changed.
- L2-06: the meeting condition x_A = x_B is stated, then x_0A + v_A t = x_0B + v_B t is rearranged to (v_A - v_B) t = x_0B - x_0A, giving the displayed t; algebra correct, substitution unchanged.
- L3-05: x_R = x_P with x_P = v_P (t - t_0) gives x_0R + v_P t_0 = (v_P - v_R) t; correct and matches the substitution (203 + 16*8,0 = 331 m; 331/6,1 = 54 s).
- L3-04: scale factor k applied to x and v, x = k x_0,ohj + k v_ohj t = x_0 + v t, then t = (x - x_0)/v; correct and a student can follow why the correction factor works on position and velocity alike.
- The Kaava step now derives the combined formula from the basic condition or equation before the symbolic result, as CLAUDE.md asks; display lines unchanged.
- L1-09: paragraph split between graphs B and D is clean, no content change.
- Paragraph splits in L1-06, L3-04, L3-05 keep every sentence; none over 120 words.
- Language and case endings in the changed text are correct; numbers with units stay in LaTeX.
- No figure, task text or level changed; set mix and counts unchanged from the passed version.
