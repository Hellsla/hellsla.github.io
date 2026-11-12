VERDICT: PASS
CONTENT-HASH: 33fcccd3aae0531c
Delta review (solution practice, 2026-11-12) of the version passed before.

## Blocking
(none)

## Polish
1. `sovella/tasks.json` s2 c: `answer.value` is still 9.81 while the model answer now gives $g \approx 9{,}8\,\text{m/s}^2$ with two figures (the rubric accepts both, tolerance covers both). Fix: set the value to 9.8 so the stored answer matches the solution.

## Checked
s2 c: $g = 4\pi^2/k$ = 9,808 m/s²; the two-figure reason (reading 0,46 s², ±0,05 s² ⇒ ±0,3 m/s²) is right. The `unit.md` precision sentence (exact quantities never limit precision) is correct. The fi, fi-easy and en diffs carry identical mathematics (every changed formula compared token by token); answers.py run; `units.py check` passes.
