VERDICT: DONE

Round 1 fix. check_lesson.py all ok; layout ok at 360, 768 and 1280 px. One lint warning remains (solutions.md uses LaTeX, as the teacher's rule asks).

- answers.py: now also computes the lesson and inquiry numbers. True extreme lines go through bar ends (10;104)–(85;133) and (25;111)–(100;137), checked against every bar, giving Δθ₀ ≈ 18 °C. Also covers suora, siirto, tarkistus-2, the misses of candidate line s₂, and the 5,5 °C gauge zero.
- lesson.md: "liike loppunut" changed to glossary wording; θ₀ = θ₁ − p₁/k is a display block; extremes 100,1 + 0,387θ and 102,3 + 0,347θ (−258,7 / −294,8) with their touch points; result −276 ± 18 °C, interval −294…−258, "yhden asteen tarkkuuteen"; the example says the 0 °C point is read from the line's extension; Kaava figure lines, bracket and aria updated.
- inquiry.json: both predictions have conceptual feedback with no data numbers, and their options are balanced in length (ennuste-2 has a 4th distractor); ennuste-1 no longer mentions a graph; `suora` adds a full-range figure with the dashed extension to θ₀ = ?; new `aariviiva` choice: is s₁ or s₂ a valid steepest line?; `epavarmuus` figure, text, hints and solution use the exact extremes (answer 18,1, full-width mistake 36,1); tarkistus-1 uses ±18.
- exercises.json: L2-04 reworded; L3-02 now says 77 K is the boiling point at normal pressure and that the gas condenses at about 67 K.
- solutions.md: L2-03 says 5,5 °C; L2-04 compares 0,18 kPa with 1,0 kPa; L3-02 Järkevyys fixed.
