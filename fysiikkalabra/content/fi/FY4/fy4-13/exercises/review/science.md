VERDICT: PASS
CONTENT-HASH: 703dc8fddc98e45f
## Blocking

## Polish
- solutions.md:68 (hanging body at rest, $29{,}43\,\text{N}$) — "Newtonin toinen laki levossa olevalle kappaleelle: $\Sigma F = 0$" is right only through $a = 0$. Fix: "Kappale on levossa, joten $a = 0$ ja Newtonin toisen lain mukaan $\Sigma F = 0$" (or name Newton I, as the chapters on Newton's laws do).
- solutions.md Kaava rows (about 15 tasks) — the same lead "Newtonin toinen laki kullekin kappaleelle erikseen, $\Sigma F = ma$, positiivinen suunta liikkeen suuntaan." is repeated verbatim, also in tasks that write one body's equation only (L2-09: $T = m_1 a$). Fix: in one-body tasks write "Kärrylle $\Sigma F = ma$, ja vaakasuunnassa ainoa voima on $T$".
- solutions.md L3 (train) Voimakuvio — "Veturin voima on merkitty $\overline{F}$." now stands alone as a paragraph before the description it belongs to. Fix: keep it with the next sentence.

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Every Kaava now names Newton's second law $\Sigma F = ma$ (or $\Sigma F = 0$ at rest) with a positive direction per body before the per-body equations, as the brief's lesson does; the per-body equations, their sum and the solved forms are unchanged and right.
- Atwood forms: $a = (m_2 - m_1)g/(m_1 + m_2)$, $T = 2 m_1 m_2 g/(m_1 + m_2)$, pulley $F_\text{akseli} = 2T$ ($18\,835\,\text{N}$) recomputed.
- $T_\text{max}$ task: $m_2 = m_1 T_\text{max}/(g m_1 - T_\text{max}) = 0{,}4405\,\text{kg}$ recomputed.
- Lift with two bodies: $T_1 = (m_1 + m_2)(g + a) = 880{,}8\,\text{N}$ right.
- L3 cart experiment: added $s = \tfrac12 a t^2 \Rightarrow a = 2s/t^2$ is correct for a start from rest.
- Train: $K_{12} = (m_2 + m_3)a = 15\,\text{kN}$ right.
- exercises.json: only the "esimerkkiaineisto" marker removed from captions (teacher 2026-11-15/16); paragraph splits change no wording or number; no answer, tolerance or id changed.
- Hash 703dc8fddc98e45f at the start and at the end.
