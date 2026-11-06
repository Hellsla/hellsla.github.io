VERDICT: PASS
CONTENT-HASH: 2da55825729970a3

## Blocking

## Polish
- content/fi/FY4/fy4-4/exercises/exercises.json:237 (L2-08) — "Esimerkkiarvot:" at the start of the text reads as if the values were placeholders — drop the prefix.
- lessons/FY4/fy4-4/answers.py:32 — add the correct value of the task as a check line, e.g. `# fy4-4-L2-08 is multiple choice (error in row 4); a = 36 N / 18 kg = 2,0 m/s²`, so the stated correct value 2,0 m/s² is computed somewhere.

## Checked
- New task fy4-4-L2-08 (Virheen löytäminen, type 4): recomputed ΣF = 45 − 9,0 = 36 N; G = 18 · 9,81 = 176,58 ≈ 177 N; a = 36 N / 18 kg = 2,0 m/s²; the shown 36/177 = 0,20 is the only wrong line. Rows 1–3 are really correct, so exactly one correct option.
- The error is this chapter's own warned mistake (massa vs. paino on a horizontal track), and the "Laskussa ei ole virhettä" feedback uses the lesson's words (tukivoima kumoaa painon, kiihtyvyyttä pienentää massa). Distractor feedback for rows 1–3 says why each line is right and which idea would make it look wrong.
- Form: the five options are parallel ("Rivi n: …"), so the right one cannot be picked by form; the unit check N : N ≠ m/s² is a real check.
- Physics: friction 9,0 N on an 18 kg cart (μ ≈ 0,05) and a = 2,0 m/s² are plausible; F_μ is the symbol already used in this set's solutions; air resistance left out is stated.
- Scope: ΣF = ma with signed forces, taught here; friction only as a given force.
- Solution complete (rows checked one by one, symbolic a = ΣF/m first, direction and significant figures stated).
- All 21 answers: answers.py run once and compared: 19 numeric within tolerance; L1-06 and L2-08 one correct choice each.
- Inline formulas (text only, not rendered): the longest, Rivi 4 "a = 36 N / 177 N ≈ 0,20 m/s²" with \dfrac, ≈ 170 px; all under 300 px. The 360 px layout check passed.
- Hash identical at start and end.
