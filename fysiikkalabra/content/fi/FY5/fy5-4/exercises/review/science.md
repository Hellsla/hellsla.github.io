VERDICT: PASS
CONTENT-HASH: 7284fbb36ad10d40

## Blocking

## Polish
- exercises.json:247 (L2-08) — "ja rata painaa vaunua", together with "radan alapuolella", nearly states that $\overline{N}$ points down, which makes option A easy to rule out. "Vaunun pyörät ovat radan alapinnalla" (or nothing at all) would leave the direction for the student to reason out.

## Checked
- Diff against HEAD~1: only L2-08 (type 3, Voimakuvion valinta) and its four figures in figures.py are new. The rest of exercises.json is reformatting only.
- answers.py run once; all numeric answers inside tolerance.
- Physics: at the top of the loop, $G + N = m\cdot 1{,}5\,g$ gives $N = 0{,}5\,G$, pointing down. The figures draw it to one scale: G = 80 units and N = 40 units. Figure C is correct.
- Figure A: $N$ up at $0{,}5\,G$ gives a net force of $0{,}5\,G$, as its feedback says. Figure B: $F_\text{kp} = 120$ units cancels $G + N$, so "voimat kumoavat toisensa" is literally true. Figure D: velocity drawn as a force, otherwise correct. Each wrong figure has exactly one error.
- The acceleration direction (`a_dir`) is passed to the FBD check only and not drawn (scripts/fbd.py), so the correct figure carries no extra arrow that gives it away. All four figure descriptions are full and parallel.
- Distractor B catches the chapter's warned mistake (keskipakoisvoima). The correct option's feedback ($N = 0{,}5\,G$) only confirms the answer.
- Scope: an extension of nyppylä/notko ($G \pm N = m\tfrac{v^2}{r}$). It is fine at level 2 because the stem gives $a_\text{n}$.
- Checked from the text and figures.py only; no render.
