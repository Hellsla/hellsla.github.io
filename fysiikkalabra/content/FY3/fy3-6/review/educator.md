VERDICT: PASS
CONTENT-HASH: 2210dad2ca7dd030

## Blocking

## Polish
- lesson.md:34-35 — The step between the two aligned lines does two moves at once (moves −c₁m₁T right and −c₂m₂T₂ left), then factors. A first-timer practising the goal skill loses the thread here. — Insert a middle line `c_1 m_1 T_1 + c_2 m_2 T_2 &= c_1 m_1 T + c_2 m_2 T` before the factored line.
- lesson.md:42 — The weighted-mean formula and the 35 °C misconception (lines 90–99) are never connected, so students do not see that they are the same calculation. — After line 99 add one sentence: "Sama tulos saadaan painotetulla keskiarvolla: T = (3,0 · 20 °C + 1,0 · 80 °C)/4,0 = 35 °C."
- lesson.md:87 — One paragraph carries four ideas (significant figures, identifying copper, the lossless 24,6 °C vs measured 24,5 °C, the heat-capacity comparison). It also says losses explain the gap right after line 77 told students to ignore losses, which reads as a contradiction. — Split into two paragraphs (result and identification; then C comparison) and phrase the loss sentence as "Todellisuudessa osa lämmöstä siirtyy myös astiaan ja ilmaan, mikä selittää 0,1 K:n eron."
- lesson.md:81, :85 — The subscript in `c_\text{m}` looks like mass m in a formula full of m. — Use `c_\text{metalli}`.

## Checked
- Lint 0/0; hash identical at start and end; answers.py output matches every `answer` within tolerance.
- Round-1 blocking fixed: lines 31–42 solve for T step by step; lines 90–99 show the 35 °C working with c cancelling; L2-01 and L2-04 now practise solving for T.
- Round-1 polish applied: ΔT defined (17), magnitudes explained (29), C = cm displayed (21), "Tärkeä syy on" (8), C values computed (87).
- Prerequisites: Q and sign convention (fy3-5), ΔT same in K and °C (fy3-3), P = W/t (fy3-2) for L2-02; nothing untaught assumed.
- Hook is a real student question and line 8 answers it, now with the surface-layer factor.
- Level 1: five single uses of Q = cmΔT, including a negative Q (L1-04) and ice (L1-05).
- Level 2: each is one rearrangement, one conversion or two steps; L2-01 and L2-04 differ in substance count and units.
- Level 3: reasoning in each (final T of stones, area cancels, density vs c); none repeats the worked example.
- Exit ticket tests the formula, the meaning of c and "not a plain average" (65 °C checked).
- meta.json goals and prerequisites match curriculum.json.
