VERDICT: PASS
CONTENT-HASH: dc13071f6130e116
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at b657e7155ea191a7.

## Blocking
(none)

## Polish
- tasks.json (s5 viimeinen kohta) sanoo 'koko aineisto antaa noin 151–153 s'; nykyinen ratkaisu on 153 s sovituksella ja 151 s kahdella pisteellä, joten sana 'koko aineisto' on epätarkka.

## Checked
s5 a: ratkaisu vaihtui kahden pisteen laskusta $\ln N$-suoran sovitukseen ($T_{1/2}$ = 153 s); answer 153, tolerance 0,04 = 147–159 vastaa Hyväksytään-riviä; 151 s säilyy kahden pisteen hyväksyttynä. Menetelmä on vaativampi mutta Kuvaajan lukeminen -vaihe opettaa sen eikä tehtävän teksti nimeä mallia. $E_0$, $m_\text{a}$, $b$, $m_\text{U}$ määritelty. Compared the diff hunks against the #522 notation and the unit text; no formula name or symbol of #522 is contradicted by a #523 solution, no derivation duplicated, LaTeX in the hunks balanced. Sample solutions now solve the asked quantity in symbols before the numbers (CLAUDE.md Lesson form 7), which supports the learning path.
