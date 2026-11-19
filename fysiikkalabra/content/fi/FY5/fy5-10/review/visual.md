VERDICT: FAIL
CONTENT-HASH: 3efbc288e36bc5e2

## Blocking
- [Major] fig "birth" (Aaltoliikkeen perusyhtälö, fig-3-390, theory-1280-2) — the bottom row's label $t = T$ is missing in both captures: its foreignObject (lesson.md line 370) was wrapped in an animation group (`fa-k`, `fa-fy510-birth-0`) and that keyframe (`fa-fy510-birth-0`) holds opacity 0 throughout, so the label is invisible while the animation runs — the row for the whole period is then the only one unlabelled and the text says "neljä hetkeä", so the reader cannot tell which moment it shows — fix: keep the `t = T` label outside every `fa-k`/clip group (static, like the other three labels, x≈53–98, y≈231.5 centred on the row at y≈246; the current y 289.5 is also below the row).
- [Major] same figure — the λ gauge (about x 132–445 of 600) is shorter than the distance from the source to the dashed front (about 124–495), so in the last row the measure does not equal the distance the wave has advanced in one period, which is exactly the point of the paragraph — fix: draw the gauge from the source x to the front x (and check it in the animated frames and in the reduced-motion still).

## Polish
- [Minor] fig "types", lower half — the label "kierroksen liike" sits on top of the coils at 1280 px (theory-1280-1) — raise it a few px or move it above the arrow.
- [Minor] fig "types" — "kohdan liike" label sits low, close to the dashed line of the pitkittäinen section; add a little space.

## Checked
- fig-1, fig-2, fig-3, fig-4 at 390 px; theory-1280-1 and theory-1280-2 (the animated figures beside text, the pause button). Wording diff is not visible in captures beyond the theory paragraph, read in the diff. Other figures and stages unchanged by the diff and not reopened.

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 4
