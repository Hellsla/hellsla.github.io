VERDICT: PASS
CONTENT-HASH: e297d1ba1b8c1dd6
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 90beeadb37d7835e.

## Blocking
(none)

## Polish
- d-kohdan Periaate kirjoittaa suoran muodossa $E = E_0 + kT$ ilman $T_0$:aa, vaikka c-kohdan kaava on $E_0 + k(T - T_0)$. Yksi sana ('kun $T_0 = 0\,{}^\circ\text{C}$') tekisi siirtymän avoimeksi.

## Checked
c ja d: symbolit $E_0$, $T_0$, $k$ esitellään Annettu-kohdassa ennen sijoitusta, sama $E_0$ molemmissa; d:n $T = (E_\text{muu}-E_0)/k$ antaa 16,5 C. Tuulivoima-a: $P_\text{ka}$, $k$, $N$, $P_\text{nim}$ määritelty. Compared the diff hunks against the #522 notation and the unit text; no formula name or symbol of #522 is contradicted by a #523 solution, no derivation duplicated, LaTeX in the hunks balanced. Sample solutions now solve the asked quantity in symbols before the numbers (CLAUDE.md Lesson form 7), which supports the learning path.
