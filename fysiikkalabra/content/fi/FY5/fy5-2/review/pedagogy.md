VERDICT: PASS
CONTENT-HASH: a2c4fdc9e0e64166

## Blocking
(none)

## Polish
1. figures.py `board_fbd` (solution of `siirto`) — the seesaw diagram shows the arms (1,50 m, 1,20 m) with dashed lines, the board diagram shows none. The solution then computes arms 0,50 m, 1,50 m and 2,50 m that the diagram does not show. Add the three arms from the support, as in `keinu-voimat`.
2. figures.py `seesaw_fbd` — G is drawn at an invented 15 kg (the task gives no mass; the alt text says so). Add half a sentence to the Voimakuvio paragraph of `tarkistus-2`: "$\overline{G}$:n pituus on valittu; se ei vaikuta tulokseen, koska sen varsi on nolla."
3. The `siirto` diagram repeats the model figure `lauta-voimat` of `piirra` exactly. This is harmless, because `siirto` is optional and its solution points back to the figure, but a student who drew the diagram has nothing new to compare there. The solution may say "vertaa piirrokseesi".

## Checked
- Premature disclosure: `lauta-voimat` appears only as `model_figure` (shown after the draw task) and inside the `siirto` solution; `keinu-voimat` only inside the `tarkistus-2` solution. Prompts, hints and mistake feedback have no diagram.
- Both diagrams come directly after the Voimakuvio paragraph and before the equation, as docs/force-diagrams.md requires. They help: the student sees the directions (the bolt pulls down, N is the longest arrow) before the moment equation.
- Arrow lengths are consistent with the numbers (board: N = Fp + G + Fh; seesaw: F = 1,25 Fl, N = sum of the others). The positive turning arrow matches the text (board counterclockwise, seesaw the adult's direction).
- Alt texts give a reader who cannot see the figure the same data without giving away anything the task asks.
- Labels in my own render appeared as raw LaTeX because I rendered without KaTeX. Geometry, spacing and overlaps are only partly checkable that way: the F label sits close to the title "keinulauta" at 390 px. The packet had no capture of these solutions, so the visual reviewer should confirm.
- The rest of the lesson is unchanged since the last PASS: path, predictions that can be refuted, inquiry sequence, example stages, exit ticket and Finnish are in order. The hash is the same at the start and the end.
