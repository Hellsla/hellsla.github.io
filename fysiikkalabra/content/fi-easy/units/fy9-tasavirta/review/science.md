VERDICT: PASS
CONTENT-HASH: 683e4a80b5d04cff
SCOPE: delta: uncommitted rewording of the s8 b and s8 c Vastaus lines in sovella/solutions.md (lines 598, 618), measured against the previous PASS (3b9eee5b55139e4f), which judged s7/s8 from 49ba8f9; nothing else re-judged.

## Blocking
(none)

## Polish
- [Minor] fi solutions.md lines 598 and 618 still begin with the formula (`$60\,\Omega$:n vastuksessa ...`, `$20\,\Omega$:n vastuksen teho ...`). If the visual finding (the box shows only the first formula) applies to fi too, fi needs the same rewording. Not a physics issue, and fi is outside this scope.

## Checked
- s8 b: the answer still gives I_60 = 0,10 A and I_30 = 0,20 A, each assigned to the right resistor (60 Ω, 30 Ω). This agrees with Up = 6,0 V across 60 Ω || 30 Ω (Rp = 20 Ω, I = 0,30 A), recomputed earlier. The significant-figure sentence is unchanged.
- s8 c: the answer still gives P_20 = 1,8 W (20 Ω resistor) and P = 3,6 W (whole circuit), from 20 Ω·(0,30 A)² and 12 V·0,30 A. The two-significant-figure reason is unchanged.
- Fidelity to fi: the same quantities, values, units, subscripts and resistor assignments. Only the sentence structure differs (the quantity comes first and the resistor is in brackets). The physics is unchanged, and the Järkevyys lines and rubrics are untouched.
- No other content line changed (git diff HEAD). Besides this edit, the diff shows only review/visual.md.
- The hash was the same at start and end.
