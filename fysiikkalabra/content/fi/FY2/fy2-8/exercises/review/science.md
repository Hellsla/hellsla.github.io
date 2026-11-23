VERDICT: PASS
CONTENT-HASH: 3abf4d8724bef942
SCOPE: delta md-paragraphs,numbers,typography from cef163f17e81a48e base 5b3ca4f

## Blocking

## Polish
- solutions.md L1-09, L3-01 Sijoitus — the Kaava now ends in one combined form ($m_\text{CO2} = e H m$; $e = e_\text{b} V h / E$), but the Sijoitus still goes through the intermediate $E$ and $m_\text{bensa}$ first; substituting into the combined form would follow the "substitute into the last symbolic form" rule (C, numbers right).
- solutions.md L1-09 — the fuel mass $m$ and the emission $m_\text{CO2}$ share the letter $m$; the subscript keeps them apart, but $m_\text{kaasu}$ for the fuel would be clearer (C).
- Still open from before: L3-06 d) "12 g/kWh" vs the table's 11–12; L2-10 a) "kaksi tuotantomuotoa" for Poland; L1-09 CH₄ check; L2-09 significant-figure reason.

## Checked
- Hash 3abf4d8724bef942 at the start and the end; only solutions.md changed since base 5b3ca4f (exercises.json and answers.py untouched).
- Every rewritten Kaava starts from $m = e\,E$ (and $E = V h$, $E = Hm$, $E = qA$, $1\,\text{kWh} = 3{,}6\,\text{MJ}$) and combines symbolically before substitution; the cancellations in L1-04 ($m_2/m_1 = e_2/e_1$, same $E$), L2-02 and L2-09 ($(e_1 - e_2)E$), L3-02 ($A_\text{b}/A_\text{a} = q_\text{a}/q_\text{b}$, same $E$) and L3-03 (per-passenger ratio with $N$ in the numerator) are right.
- L2-04: the derivation $e_\text{kWh} = e_\text{MJ} \cdot 3{,}6\,\text{MJ/kWh}$ via $m = e_\text{MJ} E_\text{MJ}$ is dimensionally and physically right.
- L3-01: equal emissions $e E = e_\text{b} V h$ is the task's condition, stated as such (not called conservation).
- Recomputed every numeric answer in one script with my own formulas: 11,95; 248,4 g/kWh; 736 g/kWh; 50; 4,14; 5,17 kg; 6,6 t; 150 g; 52 220 t total for L3-05, plus the rest of the set: all agree with answers.py and exercises.json within tolerance, units unchanged.
- The md-paragraph splits (L3-04, L3-05, L2-08, L2-10, L2-11, L3-06) move no number and change no claim; L2-08 keeps "todennäköisesti todellista" and "ei voi osoittaa" as the guardrails require.
