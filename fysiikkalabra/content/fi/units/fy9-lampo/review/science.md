VERDICT: PASS
CONTENT-HASH: fbd646831d6db0e2
SCOPE: delta re-review after the FAIL at 7c3de62e349e40a5; diff since 3cfd723ecc judged.

## Blocking
None.

## Polish
- Carried over: s3 d rubric says "noin $12\,\%$" but the solution says $13\,\%$. The recomputed value is $2{,}54/2{,}256 = 1{,}127$, so $13\,\%$. It costs no points.
- Carried over: box 1 could say "Lämpö on siirtyvää energiaa, ei kappaleen ominaisuus" instead of "sitä on vain siirtymisen aikana".
- Carried over: s8 b, d call $333\,\text{kJ/kg}$ "the table value", while the rest of the set uses $334\,\text{kJ/kg}$.

## Checked
- **Third pysahdy box (Lämpötasapaino), fixed.** The answer now reads "Kun astiassa on sekä jäätä että vettä, lämpötila on tasan $0\,{}^\circ\text{C}$." It states its condition (both phases present at normal pressure), so it no longer conflicts with the paragraph above it ("Hyvin kylmä jää voi myös jäädyttää … kaiken veden"). This is category B, resolved.
- **Diff since the reviewed version.** `git diff 3cfd723ecc HEAD` over `content/fi/units/fy9-lampo` and `lessons/units/fy9-lampo`, review folders excluded, shows one changed line in unit.md: this answer. inquiry.json, teacher.md, tasks.json, solutions.md and answers.py are unchanged, so the previous recomputation of every number still holds. The only uncommitted change in the unit is review/pedagogy.md.
- The same commit made the matching fix in en and fi-easy unit.md ("When the container holds both ice and water …"), so the language versions agree.
- practice.py check: OK.
- The unit hash was fbd646831d6db0e2 at the start and at the end.
