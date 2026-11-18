VERDICT: PASS
CONTENT-HASH: 75c95b152de5d86b
## Blocking

## Polish
- solutions.md fy4-k4 a) Kaava — "$W = Fs$" without a sign, then $\tfrac12 mv^2 - \mu mg\,s = 0$; the same task's Yleisiä virheitä calls positive friction work an error. Fix: "kitkan työ $W = -F_\mu s = -\mu mg\,s$" and the chapter's form $E_{\text{k}0} + W = E_\text{k}$ (carried over; fy4-16 now writes it this way).
- solutions.md fy4-k7 d) Kaava — "$W = Fs$ ja $F = ma$" uses $F$, which in c) is the helmet's force $F = m(a + g)$; here it is the total force. Fix: "$\Sigma F = ma$" or $v^2 = 2as$ as the Periaate says; numbers unchanged (carried over).
- solutions.md fy4-k6 e) Sijoitus — "$0{,}52\,\text{s}$ … $0{,}34\,\text{m}$": $9{,}81 \cdot 0{,}52^2 / 8 = 0{,}33\,\text{m}$; $0{,}34$ comes from $0{,}523\,\text{s}$. Fix: write $0{,}523\,\text{s}$ and $0{,}457\,\text{s}$, or $0{,}33\,\text{m}$ (carried over).
- solutions.md fy4-k7 c) Annettu gives $a = 600\,\text{m/s}^2$, Sijoitus uses $603\,\text{m/s}^2$. Fix: give $603$ in Annettu (carried over).
- solutions.md fy4-k5 a), c) — "$\dots \quad\Rightarrow\quad \dots$" after "joten" repeats the inference; one of the two is enough.

## Checked
- Diff since the version passed in round 1 (git diff fcc9aacbfc..HEAD on tasks.json, solutions.md, answers.py, figures.py): only the Kaava rows of k5 a) and c); no task, number, point, rubric or answer changed.
- k5 a) now starts from $p_\text{ennen} = p_\text{jälkeen}$ with $p = mv$ and $v_\text{B} = 0$, then $m_\text{A}v_\text{A} = (m_\text{A} + m_\text{B})u$, $u = m_\text{A}v_\text{A}/(m_\text{A} + m_\text{B})$; the round-1 Polish is done. Periaate (no horizontal external force on the two-car system) justifies it.
- k5 c) now starts from $I = \Delta p$, $I = F\,\Delta t$, $p = mv$ for car B alone, then $F = m_\text{B}u/\Delta t$; the coupling force is the only horizontal force on B (friction neglected in the task), so it is right.
- Recomputed: $u = 0{,}60\,\text{m/s}$; $E_{\text{k},1} = 27\,000\,\text{J}$, $E_{\text{k},2} = 10\,800\,\text{J}$, $\Delta E = 16\,200\,\text{J}$ ($60\,\%$); $\Delta p_\text{B} = 21\,600\,\text{N·s}$, $F = 27\,000\,\text{N}$; d) $-0{,}90$ and $+0{,}60\,\text{m/s}$, ratio $1{,}5$. Agree with answers.py.
- k5 b) "$\Delta E = E_{\text{k},1} - E_{\text{k},2}$" is defined as the energy turned into other forms (Kysytty), not as a change: no sign problem.
- The rest as checked in round 1 (all numbers recomputed, Osa 1 keys, physics wording, "sisäenergiaksi").
- Captures: none opened (text-only change, judged from the packet).
- Hash 75c95b152de5d86b at start and end.
