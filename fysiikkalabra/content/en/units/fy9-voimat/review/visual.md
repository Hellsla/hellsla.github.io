VERDICT: FAIL
CONTENT-HASH: 46a45e2ca835c026
SCOPE: delta: sovella s7 (Laskuvarjohyppääjä) and s8 (Hissi ja voima-anturilevy) with solutions, the changed intro; s1-s6 not re-judged. Captures taken for this hash (en), 390 px with every box open; 360 px not separately captured, the solution rows seen wrap cleanly at 390.

## Blocking
- [Major] `sovella/solutions.md` s7, "Yleisiä virheitä", last bullet ("proportional to the mass (...)") — a one-row `$$\begin{aligned}...$$` block sits inside a sentence in a list item; the page breaks the bullet into text ending in "(", a boxed formula, then "), ..." on a new line, so the sentence reads as broken — clearly poor readability on a phone and on desktop — write the single comparison inline: `$100 : 75 \cdot 48\,\text{m/s} \approx 64\,\text{m/s}$` (same numbers and units). Same in the other languages (the fix is language-neutral).

## Polish
- [Minor] s7 Given rows use `m = 75,0 kg` while the task says `75 kg`; the Given row should repeat the task's data (answers are rounded to two figures either way).
- [Minor] s7 d) rubric calculation row: `k ≈ 0,31` and `0,315 kg/m` in the same row; use one value (the solution uses 0,3147).
- [Minor] s7 b) force diagram: F_v (up) and G (down) are drawn close side by side, so the two labels nearly touch; readable, arrows and lengths correct.
- [Minor] `tasks.json` s7 text (en): "her position stays the same" / part d "in the same position" is ambiguous (place vs posture); "body position" or "posture" (fi: "asento").

## Checked
- s7 and s8 task text, graphs (`fy4-14/hyppy-vt-points`, `fy4-16/ex-hissi`: axes, units, LaTeX labels, N and v names equal the task's), all parts a)-e) with solutions, rubrics and common mistakes at 390 px.
- Force diagrams s7 b)/c), s8 a)/c): arrow lengths to scale (F_v shorter than G, N shorter/longer than G as stated), a and v marked apart, vectors with overline.
- Calculation chains: aligned rows, equals signs aligned, no clipped formula at 390 px with solutions open; results rounded to the data (1,5; 6,2·10²; 48; 56; -1,1; -2,3; 0,86; 12 m).
- Task texts do not reveal solution structure (no "phases", "twice"); s8 c) "osoita ... pysähtyy" is a show-that task, acceptable. Intro sentence (eight tasks) reads correctly.
- Unit is language-neutral: figures, numbers and symbols identical in fi, en and fi-easy; fi-easy sentences are short and clear.
