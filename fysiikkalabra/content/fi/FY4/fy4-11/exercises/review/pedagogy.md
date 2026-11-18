VERDICT: PASS
CONTENT-HASH: e7d898f05aacd758
SCOPE: delta md-paragraphs,numbers,reflow,typography from a1d86531e0f61248 base cabadc3
## Blocking
(none)
## Polish
- solutions.md, the two-cars distance task, Kaava — "Autot eivät törmää, jos $d$ ja edellä ajavan pysähtymiskohta yltävät takana ajavan pysähtymiskohtaan" is hard to read; write "Autot eivät törmää, jos edellä ajavan pysähtymiskohta on vähintään yhtä kaukana kuin takana ajavan: $d + s_1 \geq s_2$; rajatapauksessa $d + s_1 = s_2$."
- solutions.md, the stopping-distance graph task (the $s_\text{p}/v$ graph), Kaava — about 120 words and holds the derivation, the graph reading and the quadratic; split into two paragraphs at "$t_\text{r}$ = leikkauskohta".
- solutions.md fy4-11-L3 calculator task, Kuvaajan lukeminen a) — "nopeudella $40\,\text{km/h} 11\,\text{m}$, …" has no connector between speed and distances (unchanged line); write "nopeudella $40\,\text{km/h}$: $11\,\text{m}$, $7\,\text{m}$ ja $18\,\text{m}$".
- Earlier polish on L2-10 (hint for c, b/e overlap) still stands.
## Checked
- Round 1, delta: only the diff judged; numbers, answers, tasks and ids unchanged (the stopping-time task only reorders Sijoitus, same values).
- Every rewritten Kaava now starts from the basic relation ($v = s/t$, $I = F\Delta t$, $I = \Delta p$, $\Sigma F = ma$, $F_\mu = \mu N$, $s_\text{j} = \tfrac12 v_0 t_\text{j}$), then the derived formula, symbolic result before substituting.
- Braking-distance formula is now derived in each solution from the triangle area and $t_\text{j} = v_0/a$; a student who forgot it can rebuild it.
- Friction-limited braking tasks put $a = \mu g$ in the Kaava and substitute into the last symbolic form ($s = v_0^2/(2\mu g)$).
- Paragraph splits in the Mallivastaus and L3 answers give one idea per paragraph.
- Finnish in the changed lines correct; glossary terms kept.
- Captures opened: content/fi/FY4/fy4-11/review/shots/fy4-11-open-exercises-L3-1280-9.png (Kaava rows, Sijoitus blocks, nothing clipped); phone widths judged from the text.
