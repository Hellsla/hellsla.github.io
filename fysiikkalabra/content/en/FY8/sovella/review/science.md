VERDICT: PASS
CONTENT-HASH: 69790412287674ba

## Blocking
None.

## Polish
- **s1 "the lower one" has no antecedent, carried over.** Since the rename to first/second excited state, "from the second excited state to the lower one" appears in the s1 a criterion (tasks.json), the Substitution and the Answer. The physics is right (4.19 → 1.97 eV), but the phrase leans on the old upper/lower pairing, next to the listed common error (green taken as second excited → ground). Suggestion: "to the first excited state" in all three.
- Carried over: s2 c "The half-life 4.47·10⁹ a : 87.7 a ≈ 5·10⁷ times longer" is missing "is". Grammar only.
- Carried over: the "Hyväksytään myös" and "Yleisiä virheitä" headings stay in Finnish. That is the editorial reviewer's call.

## Checked
Hash 69790412287674ba at start and end.
- **Diff HEAD~1 (fd2e54e95).** In this set it touches only solutions.md, two lines: s1 a Substitution (E_v, λ₃) and s1 d Substitution (λ_max, E of the 1500 nm photon). Four expressions change from `\dfrac{h·c}{X}` to `h · \dfrac{c}{X}`. No number, unit, answer, tolerance or point value changed. practice.py check reports OK.
- **Values identical.** a·b/c = a·(b/c). Recomputed both forms: 3.562·10⁻¹⁹ J, 2.959·10⁻⁷ m, 1.107·10⁻⁶ m, 1.324·10⁻¹⁹ J, matching the stated results (2.22 eV, 296 nm, 1110 nm, 0.83 eV).
- **Typesetting.** Each new expression has balanced braces, `\cdot` between h and the fraction, units `\,\text{J}\,\text{s}`, `\text{m/s}` and the denominator's unit kept with their numbers, and decimal points as elsewhere in en. The denominator is unchanged, so units still reduce to J or m.
- Everything else is unchanged since the last PASS (level names, 1st/2nd excited ¹D/¹S, s5 a factor 1.36) and still agrees.
