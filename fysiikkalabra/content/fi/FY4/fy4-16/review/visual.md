VERDICT: PASS
CONTENT-HASH: e5a952f85b37a28e

## Blocking

## Polish
- [Minor] lesson.md fig `kolme` (fig-6-390, theory-1280-1), kelkkamäki voimakuvio — $\overline{F}_\mu$ is a bare arrowhead: its line is 0,5 px long (`x1="534" … x2="533.5"`), so at 390 px it reads as a red triangle stuck to the box corner, not as a force. Give $\overline{F}_\mu$ a visible line along the slope from the lower surface. It may stay short to keep the scale, with a smaller head if needed.
- [Minor] lesson.md Esimerkki, "Kaava ratkaistuna" and "Sijoitus" (example-390-2) — one `aligned` block holds both the energy equation and the new equation $v_2 = …$. On a phone the $v_2$ row reads as the next step of the same chain, and the units switch from $\tfrac{\text{m}}{\text{s}}$ to $\text{m/s}$ inside one block. Put the $v_2$ rows in their own block (or start the row with "joten"), and use one unit form.
- [Minor] lesson.md Ydinajatus and Miksi pulkat… (theory-1280-1, theory-1280-3) — at 1280 px, short inline chains break across lines: "$N -$ / $mg = ma$", "$mgh -$ / $\mu mg(x_1+x_2) = 0$", and also in Järkevyys. NOTES §1 says inline maths stays on one line. Rephrase so that each chain fits one line, or keep it unbreakable.
- [Minor] inquiry.json `johtopaatos` — the prompt says "pysähtyy silti **lähes** yhtä kauas", but the hook, the lesson and the table say exactly "yhtä kauas" ($60{,}0\,\text{m}$ on every row). Drop "lähes".
- [Minor] inquiry.json check-2 solution (open-tarkista-1280-2), generated `voimakuvio` — $\overline{G}$ runs through the floor, the head of $\overline{N}$ sits on the hatching, and the $\overline{N}$ label is about 80 px below the tail of its arrow. The diagram is also about 540 px tall for two arrows. Renderer detail: put the label next to its arrow.

## Checked
- contact-1…6 for triage; top-390, top-1280, intro (hero in top-1280); fig-1-390 hero, fig-3-390 `hissi-kuvaaja`, fig-6-390 `kolme` (plus a 3× crop from theory-1280-1), fig-7-390 `kitkatyo`
- theory-1280-1…4 (all four)
- example-390-1, -2 (the `esimerkki` figure cropped at 3×) and #8 in the contact sheet
- stage-tutki-390-1, -2 (graph and table on a phone); stage-ennusta, -sovella, -tarkista through the contact sheets
- open-tarkista-1280-1, -2, -3; open-exit-1280
- SVG source of `kolme` and `esimerkki`, only to diagnose the arrows
- PLAIN_QTY scan of lesson, inquiry and exit ticket: no number with a unit in plain text

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
