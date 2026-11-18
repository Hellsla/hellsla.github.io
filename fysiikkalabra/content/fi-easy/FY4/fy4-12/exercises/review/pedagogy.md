VERDICT: PASS
CONTENT-HASH: 4e1a211f752c40d9
SCOPE: delta numbers,wording from 7f15135115338371 base cabadc3e6179

## Blocking
None.

## Polish
1. exercises/solutions.md (overtaking-cyclist task, Kaava) — the clause has no verb: "Toisen asteen yhtälön ratkaisukaavasta $t = \dfrac{...}{a}$" — "Toisen asteen yhtälön ratkaisukaavasta saadaan $t = ...$".
2. exercises/solutions.md (bus and runner, Kaava) — $s_\text{min} = -x_{0\text{R}} - \dfrac{v^2}{2a}$ is correct only because $x_{0\text{R}} < 0$ here; add "(tässä $x_{0\text{R}} = -20\,\text{m}$, joten $-x_{0\text{R}}$ on positiivinen)".
3. exercises/solutions.md (first task, Sijoitus) — "$2{,}0 - (-3{,}0)$" uses $v_\text{B} = -3{,}0\,\text{m/s}$ without saying so — add "kärry B liikkuu vasemmalle, joten $v_\text{B} = -3{,}0\,\text{m/s}$" before the substitution.

## Checked
- Rewrite only: every meeting and overtaking Kaava now starts from x = x0 + vt (or x = ½at² from rest), writes each position, sets them equal, solves symbolically, and only then Sijoitus; no number, answer or id changed.
- Symbolic ending verified: t = (x0B - x0A)/(vA - vB) gives 4,0 s; s_min = -x0R - v²/(2a) gives 20 - 16 = 4,0 m; s_max = ½·t·vA gives 36 m with t = vA/aB = 6,0 s.
- Sign handling: "-(-2,0 m/s)" in Sijoitus matches negative velocities and removes the earlier hidden sign flip.
- Quadratic tasks: positive/first root chosen with a stated reason; "no real root means no meeting" is explained.
- Passing-lorry task: relative displacement ½at² is derived from the two positions, not just stated.
- Paragraph splits in Kuvaajan lukeminen, Periaate and Mallivastaus are line breaks only.
- Caption marker esimerkkiaineisto removal is an approved wording change; no effect on tasks.
- Captures not opened: only solution wording and formula order changed; judged from the packet's diff.
- Hash the same at start and end.
