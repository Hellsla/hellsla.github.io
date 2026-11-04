VERDICT: PASS
CONTENT-HASH: 676595eaffa2a2cb

## Blocking
None.

## Polish
- **s2 e (C), carried over.** The result is one year's effective dose from a 10 Bq lung burden, not ICRP's 50-year committed dose, and the text does not claim otherwise. PuO₂ (Type S) clears over years and partly moves to bone and liver. Suggest one sentence in Järkevyys saying that dose also accrues in later years (the committed dose). The magnitude (0,57 mSv) is realistic.
- **s2 source_note, carried over.** It still gives no source for w_R and w_T (ICRP 103) or for the 5,9 mSv (STUK, year), which the scope note requires.
- **s4 c "Hyväksytään myös", carried over.** "noin 2 min" (120 s) lies outside 136 s ± 5 %. Fine as a verbal rounding, but a numeric checker would reject it.

## Checked
Hash 676595eaffa2a2cb at start and end.
- **Diff HEAD~1 (fd2e54e95).** In this set it touches only solutions.md, two lines: s1 a Sijoitus (E_v, λ₃) and s1 d Sijoitus (λ_max, E of the 1500 nm photon). Four expressions change from `\dfrac{h·c}{X}` to `h · \dfrac{c}{X}`. No number, unit, answer, tolerance or point value changed. practice.py check reports OK.
- **Values identical.** a·b/c = a·(b/c). Recomputed both forms: 3,562·10⁻¹⁹ J, 2,959·10⁻⁷ m, 1,107·10⁻⁶ m, 1,324·10⁻¹⁹ J, matching the stated results.
- **Typesetting.** Each new expression has balanced braces, `\cdot` between h and the fraction, units `\,\text{J}\,\text{s}`, `\text{m/s}`, `\text{m}`/`\text{J}` kept with their numbers, and Finnish decimal commas `{,}`. The numerator now holds c only and the denominator is unchanged, so units still reduce to J or m.
- Everything else is unchanged since the last PASS and still agrees.
