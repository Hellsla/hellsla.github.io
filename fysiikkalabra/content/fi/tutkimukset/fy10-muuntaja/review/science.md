VERDICT: FAIL
CONTENT-HASH: b2a47a0e93d5bdb5

## Blocking
- **A (figure, `data-fig="setup"`).** Since the last PASS (commit 57de8ab9a6) the vector circuit diagram was replaced by `<image href="pics/fy10/fy10-muuntaja-setup.webp">` (commit 36f68f6e8b). This is more than the typographic change in teacher.md. The raster `assets/pics/fy10/fy10-muuntaja-setup.webp` does not show a transformer. It shows a spring-mass setup: a support bar, an unloaded and a loaded spring, a block with two red force arrows and length bars. It looks the same as `fy10-jousivakio-setup.webp`. The figure's own KaTeX labels (rautasydän, ∼, A, V, $I_1$, $U_1$, $I_2$, $U_2$, $R$, $N_1$, $N_2$) and its aria-label (ammeters in series, voltmeters across the coils) now sit on the wrong picture. The text's rule for connecting the meters ("Virtamittari kytketään sarjaan … jännitemittari rinnan") has no correct diagram behind it. The teacher's figure approval (teacher-figures.tsv 2026-11-22, fy10-muuntaja/setup) does not change this. Fix: put the transformer circuit raster in its place (or restore the vector diagram) and check that the labels line up with it.

## Polish
- Hero raster (`fy10-muuntaja-hero.webp`): a closed iron core with two coils, a supply, four meters and a load resistor. It matches the aria-label; the wiring is illustrative and acceptable.

## Checked
- teacher.md diff vs HEAD: only "lämpönä" → ”lämpönä”; meaning unchanged.
- Diff since the reviewed commit: investigation.md changes only the two SVG bodies (vector → `<image>`). All text, formulas ($U_2/U_1=N_2/N_1$, $P=UI$, efficiency, $U_1I_1$ as an upper bound on the true input power, so the efficiency is a lower bound) and investigation.json are unchanged. The earlier passes stand for them.
- Both rasters viewed after converting them to PNG.
