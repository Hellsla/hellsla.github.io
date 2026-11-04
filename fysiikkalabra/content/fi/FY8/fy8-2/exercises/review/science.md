VERDICT: PASS
CONTENT-HASH: d01b35fa24c40ba7
Round: 2

## Blocking

## Polish
- solutions.md:181 (L3-05 Kaava) — the new part d) uses $E_\text{fl} = E_\text{abs} - Q$ and $\lambda_\text{fl} = \tfrac{hc}{E_\text{fl}}$, but Kaava lists only $Q$ and $p$. — Add "ja kohdassa d) $\lambda_\text{fl} = \dfrac{hc}{E_\text{abs} - Q}$" to Kaava, so the unknown is solved symbolically before Sijoitus.
- answers.py (L3-05) — part d) (477 nm) is not checked anywhere, because the answer box is b). — Optionally add a comment line `# d) hc/(hc/400 nm - 0,50 eV) = 476,9 nm -> 477 nm`.

## Checked
- Round-1 blocker fixed: exercises.json L3-04 now says "Kuudes viiva syntyy alimmalta viritystilalta perustilaan". A brute-force search of all level triples (±0,02 eV) now gives only $E_1 ≈ 1{,}10$, $E_2 ≈ 2{,}40$, $E_3 ≈ 3{,}90\,\text{eV}$. In the mirror scheme (1,50/2,80/3,90) the line $E_1 \to 0$ = 1,50 eV would have been measured, as the new Järkevyys says. Unique, and the answer 1127 nm → 1130 nm is right.
- L3-04 Sijoitus now covers a), b) and c), and assigns every line A–E to its transition correctly.
- Round-1 polish applied: L1-06 says "viileämmän kaasun" in the answer, option, Periaate and Mallivastaus; L2-06 says "kalsium (kalsiumioni)".
- L1-06 and L1-08 reordered: exactly one correct option in each, the answer string matches it, and every distractor is wrong with correct feedback.
- L3-05 d) recomputed: hc/400 nm = 3,100 eV, minus 0,50 eV = 2,600 eV, giving 476,9 nm → 477 nm ✓.
- L2-07 slope 12,01 nm/mm and max residual 0,76 nm (stated as 0,8 nm) ✓. L2-05 2,2698 eV ✓, L2-06 −0,8486 eV ✓, L3-05 B 22,1 % (A 18,9 %, C 15,1 %) ✓.
- The Vastaus lines of L2-05, L2-06, L2-07 and L3-04 now answer every part; L1-07 now asks for the cause it requires.
- Levels 8/7/5, no duplicates, the plan in docs/exercise-bank/FY8.md is followed, and the data are labelled esimerkkiaineisto.
- The L3 captures at 1280 px were taken after the fix commit.
- Hash d01b35fa24c40ba7 is the same at the start and the end.
