VERDICT: FAIL
CONTENT-HASH: 1079c8766e1b2551

## Blocking
- content/en/FY2/fy2-1/exercises/solutions.md:5, 15, 30, 59, 117, 127, 137, 147, 192, 207 (L1-01, L1-02, L1-03, L1-05, L2-01, L2-02, L2-03, L2-04, L2-07, L2-08) — the rewritten Kaava step opens with the Finnish symbols $E_\text{alussa} = E_\text{lopussa}$. The Principle line just above it in the same solution writes the same law as $E_\text{initial} = E_\text{final}$, and the English text never defines the Finnish symbols. One law now has two symbol pairs within a few lines, and the reader cannot tell whether they mean the same quantities. This is an internal-consistency and notation error (guardrail item 6). The other seven English FY2 sets use only English symbols. — Write $E_\text{initial} = E_\text{final}$ in these ten Formula lines. Also correct the docstring in lessons/FY2/fy2-1/answers.py:2 if it is shared with the English version (it is not shown to students).

## Polish
- solutions.md:192 (L2-07): the Formula goes from $E_\text{initial} = E_\text{final}$ straight to $E_\text{thermal} = E_\text{elec} - E_\text{light}$. The middle step $E_\text{elec} = E_\text{light} + E_\text{thermal}$ appears only in the Principle line. Repeating it here would match the other solutions.

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was 1079c8766e1b2551, the same as the packet.
- I recomputed all 17 numeric answers in one script, from the task data with my own balances. All of them agree with exercises.json and answers.py. L2-08 is 14.29 vs 14.3 and L3-04 is 39.17 vs 39.2, both within tolerance.
- No number, unit or answer changed in the diff. All the changes are Formula wording, paragraph splits and the L1-10 hint moved into `hints`.
- Every rewritten Formula line is physically right. It starts from energy conservation of the stated isolated system (or from $H = E/m$ in L1-10, or from share = part : whole in L2-05) and then solves symbolically before substituting.
- L2-02: the added conditions are right. The child is at rest at the top and $E_\text{p} = 0$ at the bottom, so $E_\text{p} = E_\text{k} + E_\text{thermal}$.
- L2-06: the added sentence "a device cannot produce energy from nothing" is the correct principle for the perpetual-motion analysis.
- L3-01 and L3-05: the new starting equations $E_\text{A} = E_\text{p} + E_\text{k} + E_\text{thermal}$ and $E_\text{in} = E_\text{out} + E_\text{thermal}$ are correct.
- L1-10: the previous Polish item is fixed (dry wood, MAFY $16.2\,\text{MJ/kg}$). The hint names the right MAFY table.
- The split paragraphs (L1-04, L1-06 to L1-09, L3-03, L3-04, L3-05) keep the physics and the numbers unchanged.
