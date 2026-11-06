VERDICT: FAIL
CONTENT-HASH: 4e883ea054d82bf0
## Blocking
- content/fi/FY4/fy4-2/exercises/solutions.md:210 — in fy4-2-L2-08 the check line `s_2 = 8,0 m/s * 4,0 s + 1/2 * (-2,0 m/s^2) * (4,0 s)^2` is 397 px wide in a 304 px box at 390 px (measured in the render), so it scrolls sideways; limit is about 300 px — split into two lines, e.g. `s_2 = 8,0 m/s * 4,0 s + (-16 m)` after first evaluating each term in its own line (`v_0 t = 32 m`, `1/2 a t^2 = -16 m`, `s_2 = 16 m`).
## Polish
- Polish: the three wrong options catch dependence misreadings (time squared, inverted, independent), not one of the chapter's three warned mistakes (a = 0 when v = 0, negative a = slowing, heavy falls faster); acceptable for type 6, no change required.
## Checked
- New L2-08 (prediction, type 6) at L2 is right: needs t = v0/a and area under (t,v); within FY4.2 (area as displacement, v = v0 + at).
- Form: correct option (2-fold) is neither longest nor the only hedged one; wrong-option feedbacks are longer than the correct one, no pattern; options span 4x, 2x, 1/2, 1x.
- Numbers verified: t = 2,0 s and 4,0 s, s = 8,0 m and 16 m, check by x formula = 16 m; wrong-option feedbacks consistent with that.
- Task order: situation, data, question last as its own sentence; direction (wet road) stated.
- Solution is complete and explains why each wrong answer arises.
- Rendered at 390 px: only the line above overflows; other formulas fit (widest 304 px = box width). Text only: Finnish and logic.
