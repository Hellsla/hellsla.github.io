VERDICT: PASS
CONTENT-HASH: cac0fd5db47fb84c
Round: 1

## Blocking

## Polish
- figures.py pick_kiihtyy — the curve starts with zero slope at t = 0 (A = A₀(1 − t²/8 h²)), i.e. no decay at first; harmless as a distractor, but a curve with the right initial slope that steepens later would isolate the "ageing nuclei" idea alone.

## Checked
- Recomputed all four curves in one script against figures.py: C 400/200/100/50 kBq at 2/4/6/8 h; D = 800 e^(−t/2 h) 294/108/40/15 kBq; A straight line to 0 at 4 h; B through (2 h; 400 kBq), zero at √8 = 2,83 h. Figure descriptions and feedback numbers (≈290, ≈110, ≈15 kBq; 2,8 h) agree.
- Exactly one correct option (C); C and D both decay smoothly, so the answer is not identifiable by form and needs the 2 h reading (400 vs 294 kBq, distinguishable on the 50 kBq grid).
- Distractors A and B are the lesson's two warned mistakes (all gone after two half-lives; nuclei with a memory); D is λ = 1/T½ without ln 2, inside the taught N = N₀e^(−λt), λ = ln 2/T½.
- Task states large N and no in-growth, so the continuous law applies (guardrail: conditions stated).
- Notation A, A₀, T½, λ as in the brief.
- From render: I rendered the four option SVGs (Playwright, LaTeX left raw) and checked the curves' shapes and axis ranges 0–8 h, 0–900 kBq; feedback/solution layout not rendered.
- Hash identical at start and end.
