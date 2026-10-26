VERDICT: FAIL
CONTENT-HASH: f9bbdacd430c964b

## Blocking
- exercises.json:90, solutions.md:87 (L3-02) — The task claims "Typpi nesteytyy 77 K:ssä", and the solution says the pressure collapses at 77 K. 77 K is the boiling point at about 101 kPa. At the task's own 28,2 kPa the gas is still unsaturated at 77 K and condenses only at about 67 K, so the reasoning asked for is false. — State that nitrogen boils at 77 K at normal pressure and condenses lower (about 67 K) at this lower pressure, so the line cannot reach 0 K; fix the solution to match.
- lesson.md:185 — "tulos pyöristetään samaan kymmenen asteen tarkkuuteen" is wrong: −276 ± 16 is rounded to one degree. — "…samaan tarkkuuteen eli yhden asteen tarkkuuteen."

## Polish
- lesson.md:142, inquiry.json "epavarmuus" — The quoted lines are not quite the extremes: the true extremes are 100,14 + 0,386θ (−259,4 °C) and 102,3 + 0,347θ (−294,8 °C). Optionally call them "piirretyt ääriviivat".
- lesson.md:81 — θ₀ = θ₁ − p₁/k is used throughout the solutions but appears only inline. Give it a display block.
- lesson.md:63 — "hiukkasten liike on loppunut" contradicts the glossary's "pienimmillään".
- solutions.md:71 — The sentence compares a °C uncertainty with a kPa uncertainty. Compare 0,18 kPa with 1,0 kPa instead.

## Checked
- answers.py: all 12 answers recomputed independently and they match. Tolerances admit correct rounding, and every mistake value lies outside its tolerance.
- Data: a least-squares fit gives θ₀ = −276,2 °C. The best, steep and shallow lines stay within ±1 kPa of every point.
- Worked example (−276,0 °C; Δθ₀ = 15,7 °C) is symbolic before substitution.
- Inquiry numerics are correct (A/B −275,8, siirto −276,9, tarkistus-2 −282,9, virhe −276,1, kertaus 1,068, exit 0,36), and every prediction key and its feedback numbers are right.
- SVG coordinates of all five figures were checked against the data. Figure 5 is to scale, as stated, and all labels are LaTeX.
- Apparatus figure: the bulb is submerged and V is constant. Scope matches the FY3 experiment, and no lesson ids appear in student text.
