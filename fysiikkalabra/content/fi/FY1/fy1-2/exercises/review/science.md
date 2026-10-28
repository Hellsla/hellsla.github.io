VERDICT: PASS
CONTENT-HASH: 4157a622aabadf49

## Blocking

## Polish
- solutions.md L2-03 Kaava — "$10^{6} : 10^{4}\,\text{ha}$" reads as $10^{6} : (10^{4}\,\text{ha})$. Write "$1\,\text{km}^2 = 10^{6}\,\text{m}^2$ ja hehtaareja on $10^{6}\,\text{m}^2 : 10^{4}\,\text{m}^2 = 100$, joten $1\,\text{km}^2 = 100\,\text{ha}$".
- answers.py comments — they still say "km/AU", "m/km" and "s/a". Students never see them, but they could be aligned with the house rule.

## Checked
- Round-2 blocker fixed: L3-03 now counts the hours, $1{,}447\cdot10^{5}\,\text{s} : 3600\,\text{s} = 40{,}2$, with no s/h factor.
- Round-2 polish fixed: L3-02 names the scale ("jokainen $3474\,\text{km}$ on yksi kuvapiste") and counts pixels with ":", consistent with L1-05.
- One script recomputed all 12 answers independently. Each one equals answers.py: 0,082; 384,4; 1,702; 15 341; 400,7; 1,6·10⁷; 500; 240; 1,3255; 63 247; 674,4; 40,2. Tolerance 0.02 accepts correct rounding.
- Regression scan of exercises.json and solutions.md: no ×, \times or ÷; \cdot in products; conversions by substituting the unit's value or by counting with ":"; no conversion-factor units.
- Every solution has all seven parts, solves symbolically first, justifies its significant figures and makes a real reasonableness estimate.
- Scope is FY1 ($s = vt$, $t = s : c$, $N = ft$, area as a product).
- Content hash is identical at the start and the end.
