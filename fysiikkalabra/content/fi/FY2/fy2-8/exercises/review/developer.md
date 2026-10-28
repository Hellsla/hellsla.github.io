VERDICT: DONE

Round 2, fix mode. lint_lesson.py and check_solutions.py: no errors.

solutions.md
- Järkevyys conversions by substitution in L1-01, L1-02, L1-05, L2-01, L2-02, L2-03 (grams to kg or t via `\cdot 0{,}001` or `\cdot 10^{-6}`; L1-01 coal check now via grams).
- L3-01 and L3-03 Kaava symbolic first ($m = e_\text{b} \cdot V \cdot h$; $m_\text{bussi} = e_\text{b} V_\text{b} h_\text{b} : N$), with symbols explained.
- L3-03 Sijoitus keeps units l and MJ; "$25$ matkustajalle" in LaTeX.
- L3-02 solved for the area ratio: Kysytty, Kaava, Sijoitus (100 km² : 2,0 km² = 50) and Vastaus (50 kertaa).

exercises.json
- L3-02 asks how many times the field area exceeds the solar park area; answer 50, unit "kertaa", tolerance 0,02.

answers.py
- L3-02 computed as A_bio / A_sol = 50.
