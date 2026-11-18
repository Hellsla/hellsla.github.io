VERDICT: PASS
CONTENT-HASH: 7b61c71e80ac95f1

## Blocking

## Polish
- content/fi-easy/FY4/fy4-14/exercises/solutions.md (falling-body Kaava steps, e.g. @@ -41, -110, -203, -247) — "$\Sigma F = G - F_\text{v}$" presumes the positive direction down without saying so in the Kaava step; the road tasks and the up/down task name it ("Positiivinen suunta on alas"), and the same three words would make every chain self-contained.
- solutions.md (@@ -306, b) — the sentence that justifies $a = g$ ("Ilman ilmanvastusta $\Sigma F = G = mg$ …") comes after the result it justifies; put it before $v^2 = v_0^2 + 2as$.
- solutions.md (L2-08 Järkevyys) — the new breaks leave "Luvun kuvaajan malli antaisi … noin $53\,\text{m/s}$." as a one-sentence paragraph cut from the comparison it starts; keep it with the next sentence.
- Earlier polish (L2-04 limiting data 450 N and 180 N) still open; not part of this change.

## Checked
- Hash 7b61c71e80ac95f1 at the start and the end; since 062f457c28^ only `**Kaava:**` lines of solutions.md changed (numbers, answers, tolerances, tasks, ids, exercises.json, answers.py unchanged); the packet's other hunk only splits a paragraph.
- Every rewritten Kaava starts from $\Sigma F = ma$ (or $a = 0 \Rightarrow \Sigma F = 0$ at terminal speed), then $\Sigma F$ from the forces, then the asked quantity symbolically: the brief's $\overline{G} + \overline{F}_\text{v} = m\overline{a}$ in signed form.
- Signs: rising ball $-mg - F_\text{v} = ma$ (positive up); up/down task with positive down $mg + F_\text{v} = ma_1$, $mg - F_\text{v} = ma_2$, $\Delta a = 2F_\text{v}/m$; road tasks $F - F_\text{v} - F_\text{r} = 0$ and $-F_\text{v} - F_\text{r} = ma$ (positive forward). All consistent with the force directions in the brief.
- Halved drag after terminal speed: $a = g/2$ correct.
- $v = \sqrt{2gh}$ now from $v^2 = v_0^2 + 2as$ with $v_0 = 0$, $a = g$; condition (no air resistance) stated.
- Data tasks: $a$ from the slope, then $F_\text{v} = m(g - a)$; $F_\text{v} = mg$ at the end where $a = 0$.
- Notation as in the brief's lesson ($F_\text{v}$, $G$).
- Captures: none opened (fi-easy judged from text and the packet).
