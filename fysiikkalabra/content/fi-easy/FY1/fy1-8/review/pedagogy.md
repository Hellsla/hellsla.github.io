VERDICT: PASS
CONTENT-HASH: 01607ed274d08372

## Blocking
(none)

## Polish
1. lesson.md "Tulos" stage (6/7 of the example) and the solution of `siirto` — the reasoning contradicts itself: "the uncertainty 0,2 s has one figure, therefore round to two figures". A student cannot follow why. Fix: "Vähimmäismatka on suunnitteluarvio, joten kaksi numeroa riittää. Pyöristä ylöspäin, jotta raja täyttyy: $1{,}68\,\text{m} \to 1{,}7\,\text{m}$."
2. exit-ticket.json q1 — word for word the same numbers as the first ```pysahdy``` in the formula section ($0{,}2\,\text{s}$, $2{,}0\,\%$, $10\,\text{s}$). The student recalls the answer instead of using the idea. Fix: change the numbers (e.g. $\Delta t = 0{,}3\,\text{s}$, $\varepsilon_\text{max} = 1{,}5\,\%$ gives $20\,\text{s}$).
3. inquiry.json `tarkistus-2` (Laskutehtävä) — computes a mean and a half-range, which is fy1-3 and repeats the `kertaus` item. The lesson's new calculation (the shortest time or distance from $\varepsilon_\text{max}$) is only in the optional `siirto`. Fix: make the core Laskutehtävä the design calculation, or make it a change of $\Delta t$ from a data set followed by the design step. Also the correct option is the longest in `kertaus`, `ennuste-1` and `tarkistus-1`.
4. inquiry.json `graafi` — the point $(5{,}0\,\text{s};\ 2{,}1\,\text{m})$ is given in the prompt, so the task is a division, not graph reading. The reason for "matka pystyakselilla, vaikka sitä muutettiin" sounds like a rule about axes. Fix: say that this is the usual $s$–$t$ graph, whose slope is $v$. Ask the student to read the value at $t = 5{,}0\,\text{s}$ from the graph.
5. Lesson goal "toteuttaa" — carried only by the text step `tee-itse` after the core explain item. The report's "tulos epävarmuuksineen" ($v = 0{,}42\,\text{m/s} \pm 0{,}02\,\text{m/s}$ in the `tarkistus-3` model answer) is never derived. Fix: one short line on where $\pm 0{,}02$ comes from (e.g. the spread of the five speeds in the table).

## Checked
- Opening question is answered by the theory and `pohdi`; hook gives the data and nothing more; prediction precedes the evidence and the feedback repairs each misconception.
- Table values in `poytakirja` (means, $\Delta t$, $\varepsilon$, $v$) and the line of `graafi` recomputed: consistent with the figure.
- Example: seven stages, symbols first, conversion stage, sanity check; numbers verified ($1{,}68\,\text{m}$, $4{,}9\,\%$, $17\,\%$).
- `siirto`, `virhe`, `tarkistus-2` answers recomputed: $14\,\text{m}$, $2{,}4\,\text{m}$, $2{,}0\,\%$.
- Core path: optional items are retrieval, reflection, error spotting, transfer and the explanation check. Workload is one lesson.
- Selkeä suomi: terms explained at first use, short sentences, glossary terms match; contact sheets 1–2 show no clipped content at 390 px.
- Scope stays FY1 ($s = vt$, uncertainty, fitting a line); nothing from FY2.
