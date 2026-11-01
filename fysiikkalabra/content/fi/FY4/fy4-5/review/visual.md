VERDICT: FAIL
CONTENT-HASH: 5ba546ce0da699f5

## Blocking
- [Major] lesson.md "Voimakuvion piirtäminen" (theory-1280-1, stage-selita-390-2/3) — the five sub-bullets under step 3 (Paino, Tukivoima, Kitkavoima, Jännitysvoima, Ilmanvastus) render as numbered steps 4–8, so the list runs to 13 although the text says "kahdeksalla vaiheella" — the eight-step method, the chapter's core structure, reads wrong — indent the sub-bullets four spaces (or fix the build's nested-list handling) so they render as a bullet sublist of step 3.
- [Major] simulation (sim-390, sim-1280, lab-1280) — the canvas voimakuvio is drawn tiny in a mostly empty panel: box about 40 px, arrows 12–30 px, labels $\overline{N}$, $\overline{F}$, $\overline{G}$ and the panel titles about 7 px at 390 and 9 px at 1280 — the force diagram is the simulation's central object and is unreadable on a phone — scale the diagram to fill its panel and draw labels at 13 px or more.
- [Major] check-2 solution diagram (open-tarkista-1280-2) — component labels are $\overline{T}_{1_y}$ with a nested subscript; $\overline{T}_{1_y}$ floats above the label $\overline{T}_1$ and $\overline{T}_{2_y}$ sits between the two dashed arrows — which component is which is ambiguous — put each label at its own dashed arrow's tip and write $T_{1y}$, $T_{1x}$.

## Polish
- [Minor] example figure (example-390-1) — the $35^\circ$ label touches the $\overline{T}_x$ dashed arrowhead — move it into the arc's opening, clear of the line.
- [Minor] "Kaava ratkaistuna" block (example-390-2) — x:/y: rows are left-aligned while the a=/N= rows align at "=", in one block — split into two aligned blocks.
- [Minor] Kaava section — units in plain text, "(N)", "(kg)", "(m/s²)" — write $(\text{N})$, $(\text{m/s}^2)$ as the standing rule asks.
- [Minor] check-2 Sijoitus (open-tarkista-1280-2) — the auto-split chain puts "$T$" half a line above its "=" — for the build (mathlayout.py): keep a short left side on the fraction's row.
- [Minor] simulation — the "Nopeus" select (playback speed) shares its name with the velocity $v$ in the same readout, and the components checkbox sits apart above its label — rename it "Toistonopeus" and put the box inline with its label.

## Checked
- contact-1…6 to triage; top-390, intro-1280 (hero), fig-1/4/5/6/8/11-390 at full size
- example-390-1 (figure zoomed 3×: arrows to scale, $N : G$ matches $72 : 118$), example-390-2
- sim-390 (canvas zoomed), sim-1280, lab-1280
- theory-1280-1, stage-selita (list numbering), open-tarkista-1280-2 (Sijoitus zoomed), open-ennusta, exit via contact sheets

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 3
