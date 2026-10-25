VERDICT: FAIL
CONTENT-HASH: b3c4e9982c3bef92

## Blocking
- lesson.md:23, lesson.md:71, exercises.json (all 12) — The curriculum skill goal "useita termejä sisältävän suureyhtälön ratkaiseminen" is never shown or practised in its real form: solving the balance equation for the equilibrium temperature T, which appears on both sides. The worked example solves for c (a single division), L3-01 solves for m with T known, and line 71 just states "35 °C" with no working. A first-time student cannot reproduce the 35 °C, which is also the main reasoning behind exit ticket 3. — Fix: (1) at lesson.md:71 (or right after line 23), show the 35 °C case in display math: $3{,}0\,\text{kg}\cdot(T-20\,^\circ\text{C}) = 1{,}0\,\text{kg}\cdot(80\,^\circ\text{C}-T)$, so $4T = 140\,^\circ\text{C}$ and $T = 35\,^\circ\text{C}$ (c cancels because both are water). (2) Replace L2-04, which only rearranges $Q = cm\Delta T$ for c, as L2-03 already does for ΔT, with a mixing task between two different substances that asks for T. Example: a 0,25 kg aluminium block at 95 °C is placed in 0,40 kg of water at 18 °C. Update answers.py and solutions.md to match.

## Polish
- lesson.md:17 and lesson.md:21 — Line 17 says Q is negative when a body cools, but line 21 writes the hot body's term as (T₁ − T), so it is positive, and nothing explains why. — Define $\Delta T = T_\text{loppu} - T_\text{alku}$ at line 17. After line 21, add: "Yhtälössä molemmat puolet ovat luovutetun ja vastaanotetun lämpömäärän suuruuksia, siksi kuumalle kappaleelle lasketaan alku − loppu."
- lesson.md:8 — C = cm is introduced only inline, yet the example (line 68), the exit ticket and the sim rely on it. The house rule says every formula appears in display form once. — Give `C = c m` its own display line in `## Kaava` and name the symbol and unit there.
- lesson.md:3 and lesson.md:8 — The hook's answer is credited entirely to c, but water also mixes to depth and evaporates. A student who has felt warm surface water may object. — Write "Tärkeä syy on, että veden ominaislämpökapasiteetti on…" instead of the flat "Siksi".
- lesson.md:68 — The values 1257 J/K and 75 J/K appear without working. — Show the working inline: "0,300 kg · 4190 J/(kg·K) ≈ 1260 J/K" and "0,200 kg · 375 J/(kg·K) ≈ 75 J/K".

## Checked
- lint_lesson.py: 0 errors, 0 warnings. The proofreader's diff is already in lesson.md (lines 6, 71, 76).
- Prerequisites are covered: Q, internal energy, sign convention and isolated systems (fy3-5); ΔT is the same in K and °C (fy3-3); P = W/t, needed for L2-02 (fy3-2, through fy3-5).
- The hook (sand vs water) is a question students really ask, and line 8 answers it.
- Each Ydinajatus paragraph adds one idea: Q ∝ mΔT with c, then the role of large c, then equilibrium and the calorimeter.
- Level 1: L1-01 to L1-05 each use Q = cmΔT once, with c taken from the table.
- Level 2: L2-01 (g to kg), L2-02 (Q, then t), L2-03 (rearrange, then add) and L2-04 (rearrange) each have two steps or one rearrangement.
- Level 3: L3-01 (balance plus reasoning about the stones' final temperature), L3-02 (the area cancels) and L3-03 (density vs c) each need reasoning.
- No exercise repeats the worked example with new numbers.
- The exit ticket tests the formula, the meaning of c and the "not an average" idea, so it targets core ideas, not details.
- meta.json goals, prerequisites and glossary match curriculum.json.
