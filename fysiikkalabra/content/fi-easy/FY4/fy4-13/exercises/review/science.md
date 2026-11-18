VERDICT: PASS
CONTENT-HASH: ae9268d2c79b7c5f

## Blocking

## Polish
- content/fi-easy/FY4/fy4-13/exercises/solutions.md (16 Kaava steps) — the added lead "Kirjoita Newtonin toinen laki …" is an instruction in a model solution; the brief's lesson and the other steps use the passive ("Kirjoitetaan …").
- solutions.md:429 (Kaava) — "jokaiselle kappaleelle erikseen" with only one equation, $T = m_1 a$, written; the generic lead does not fit a one-body step — "Kärryn liikeyhtälö $\Sigma F = ma$: vaakasuunnassa vaikuttaa vain $T$".
- solutions.md:12 and 28 (L1 Kaava) — "$\Sigma F = ma$. $T = ma$" (and "$mg - T = ma$") jump from the law to the body's equation; a few words ("Vaakasuunnassa kokonaisvoima on $T$", "Kokonaisvoima on $mg - T$") make the step visible.
- solutions.md (many Kaava steps) — a sentence beginning with a formula ("… suunta. $T = m_1 a$ …"); "Silloin $T = m_1 a$ …" reads better.

## Checked
- Hash ae9268d2c79b7c5f at the start and the end; since 062f457c28^ only `**Kaava:**` lines of solutions.md changed (numbers, answers, tolerances, tasks, ids, exercises.json, answers.py unchanged); every change only prepends the basic law to the existing derivation, which is kept verbatim.
- Each body's equation matches its stated positive direction: cart $T = m_1 a$, hanging mass $m_2 g - T = m_2 a$, Atwood $T - m_1 g = m_1 a$, stacked lift $T_1 - T_2 - m_1 g = m_1 a$, train couplings $K_{12} - K_{23} = m_2 a$.
- Static cases rightly from $\Sigma F = 0$ (hanging body at rest; pulley axle $F_\text{akseli} = 2T$ for a light pulley at rest).
- Symbolic results unchanged and correct: $a = m_2 g/(m_1 + m_2)$, $T = 2m_1 m_2 g/(m_1 + m_2)$, $m_2 = m_1 T_\text{max}/(g m_1 - T_\text{max})$, $m_1 = m_2(g/a - 1)$, $g = kM$.
- Data task: $a = 2s/t^2$ now from $s = \tfrac12 a t^2$ (start from rest), as in the brief's lesson.
- Notation the same as the brief's lesson ($T$, $m_1$, $m_2$, positive direction per body).
- Captures: none opened (fi-easy judged from text and the packet).
