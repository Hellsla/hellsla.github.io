VERDICT: PASS
CONTENT-HASH: 1beb241a2eae9769

## Blocking

## Polish
- exercises/solutions.md (fy3-9-L3-03, Kaava) — the row $p_\text{raja} = p_0 + \rho g h$ repeats the first row $p = p_0 + \rho g h$ with a new subscript; correct, but one row "$p_\text{raja} = p_0 + \rho g h$ → $h = \dots$" would be enough. Optional.
- exercises/solutions.md (fy3-9-L2-10, Mallivastaus b) — earlier polish still stands: "mittausepävarmuuden rajoissa" next to the first point 51 kPa above the line (beyond ±30 kPa); the outlier sentence handles it.

## Checked
- Every changed Kaava starts from the basic law of the stated process (Boyle $p_1V_1 = p_2V_2$; isobaric $V_1/T_1 = V_2/T_2$; isochoric $p_1/T_1 = p_2/T_2$) and solves the asked quantity symbolically before Sijoitus; each final row is the form substituted into.
- L2-06 (hose volume): the expansion $p_1V_1 + p_1V_\text{h} = p_4V_4 + p_4V_\text{h}$ → $V_\text{h} = (p_4V_4 - p_1V_1)/(p_1 - p_4)$ re-derived; signs right; with the data 284/142,9 = 1,99 ml.
- Absolute-zero task: $0 = p_1 + k(\theta_0 - \theta_1)$ → $\theta_0 = \theta_1 - p_1/k$ correct.
- Tyre (L3-02): total pressure $p_1 = \Delta p_1 + p_0$ first, proportionality on total pressure, gauge reading $p_2 - p_0$ last: right model (351 → 303,1 → 202 kPa).
- Bicycle pump: $p_1AL_1 = p_2AL_2$ → $L_2 = p_1L_1/p_2$, $s = L_1 - L_2$; 10,07 cm and 29,9 cm recomputed.
- Bubble: $p_1 = p_0 + \rho g h$ then Boyle; 297,2 kPa and 5,89 cm³ recomputed; the safety sentence keeps the guardrail wording after the paragraph split.
- Fast compression two-stage Kaava (isothermal then isochoric, $\theta_2 = T_2 - 273{,}15\,\text{K}$) correct.
- L2-10: $p_2/p_1 = kT_2/(kT_1) = T_2/T_1 = 1{,}50$; k cancels.
- Other diff hunks only split paragraphs; numbers, Sijoitus and answers unchanged against the previous PASS.
- Hash the same at start and end.
