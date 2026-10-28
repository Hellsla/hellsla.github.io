VERDICT: FAIL
CONTENT-HASH: da2cc58228b58e6a
## Blocking
- inquiry.json:301-307 (transfer task hints 2-3 and the mistake feedback for 1092) — the touched lines teach the km/h conversion as a formula: "jaa luku 3,6:lla", `(21,6 : 3,6)\,\text{m/s}`. The teacher's rule is conversion by substitution for understanding: write 1 km/h = 1000 m / 3600 s, so `21{,}6\,\text{km/h} = 21{,}6\cdot\dfrac{1000\,\text{m}}{3600\,\text{s}} = 6{,}0\,\text{m/s}`. Hint 2 should say "kirjoita km:n ja h:n paikalle niiden arvot m:ssä ja s:ssa", not "jaa 3,6:lla". The same factor-first style is in lesson.md:129 ("1 m/s = 3,6 km/h") and in the `solution` Muunnokset (line 314, `\dfrac{21{,}6}{3{,}6}`); fix them together.
## Polish
- The new parentheses `(21{,}6 : 3{,}6)` are correct and read well; keep them if the conversion is rewritten.
## Checked
batch delta review: diff judged in context; arithmetic correct (21,6 : 3,6 = 6,0), but the conversion method conflicts with the substitution rule above.
