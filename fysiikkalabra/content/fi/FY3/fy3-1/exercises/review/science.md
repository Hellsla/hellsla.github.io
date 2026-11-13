VERDICT: PASS
CONTENT-HASH: 0fe3461097d29d49
SCOPE: delta added-exercise from 599e9ef3449e91a0 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-1-L1-10) — the lesson's own table gives $g_\text{Mars} = 3{,}71\,\text{m/s}^2$ and the task asks for the MAFY value $3{,}72\,\text{m/s}^2$; the solution already says the tables differ slightly and the $\pm 4\,\%$ tolerance accepts both (315 N vs 316 N). Optional: one clause "luvun taulukossa $3{,}71\,\text{m/s}^2$" so a student who uses the chapter's table knows it is fine.

## Checked
- MAFY value verified on mafytaulukot.fi (*Aurinkokunta*): Mars putoamiskiihtyvyys pinnalla $3{,}72\,\text{m/s}^2$, as the solution uses.
- L1-10 recomputed: $G = 85{,}0 \cdot 3{,}72 = 316{,}2\,\text{N}$ (answers.py same); with 3,71: 315,4 N, 0,3 % off, inside tolerance 0,04.
- Model $G = mg$ is the chapter's law; mass the same on Mars; in FY3 scope (no Newton's laws).
- Unit N; three significant figures justified by 85,0 kg and 3,72 m/s²; reasonableness check ($0{,}38 \cdot 834\,\text{N} \approx 317\,\text{N}$) is a real check.
- Solution complete: given, principle, formula (already solved), conversions, substitution with units, rounding reason, check.
- Data realistic (astronaut with suit 85 kg is plausible; light suit, but not a physics error).
- Rest of the set unchanged since PASS (added_exercises verified by script).
- Hash same at start and end.
