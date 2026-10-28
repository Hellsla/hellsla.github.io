VERDICT: DONE

Fix, round 1. `lint_lesson.py fy2-2`: 0 errors (one old warning on L1-01's Kaava); `check_solutions.py fy2-2`: ok.

- `answers.py`: new or changed answers computed first (L1-02, L1-05, L2-04, L3-01, L3-02, L3-03).
- `exercises.json`: every number with a unit in LaTeX. L1-02 is now a context task (200 g chocolate bar against a day's food, 2,3). L1-03 is a wind farm (tuulipuisto), so it no longer contradicts OL3's 140 TJ. L1-05 uses an apple (example value 300 kJ), not the banana. L2-01 names its 100 g bar. L2-04 compares a TNT tonne with chocolate bars (950), so it no longer repeats tarkistus-2. Level 3 now asks for reasoning: L3-01 asks for the smallest whole number of units (6, rounded up and justified). L3-02 combines conservation with a comparison against house heating (3200). L3-03 asks for the petrol volume (1,2 · 10⁷ l, tolerance 0,05 because the answer has two significant figures) and compares it with 4,5 kg of uranium, without a per-kilogram energy.
- `solutions.md`: L1-04 says "kahdestatoista" and gives its rounding to tenths of a megajoule. L2-01 and L2-02 convert by substitution ($0{,}80 \cdot 1000\,\text{kJ}$, $1{,}28 \cdot 1000\,\text{MJ}$), and L2-02 writes $V = 40\,\textsf{l}$ and $32\,\text{MJ}/\textsf{l}$. The changed tasks have new complete solutions.

Not fixable here: hints and common-mistake feedback for exercises, because the exercise schema (README) has no fields for them.
