VERDICT: PASS
CONTENT-HASH: 31efd4d4ba7335fd

## Blocking
(none)

## Polish
- None.

## Checked
- The diff (solutions.md:238) reverses the inference to "The power is constant, so the graph is a straight line". This is now the right direction. The task gives constant power and says all of it goes to the block, so $\Delta T = Pt/(cm)$ grows linearly in $t$. Taking $c$ as constant over $40\,\text{K}$ is a fair simplification (C).
- The old wording inferred constant power from the straight line, which also needed the no-loss assumption. The new order uses only what the task states.
- The numbers are unchanged: $c = Pt/(m\Delta T) = 400 \cdot 180 / (2.0 \cdot 40) = 900\,\text{J/(kg·K)}$, the same as answers.py.
- The figure `fy3-6/heating-line` has its end points on grid crossings, (0 s; 20 °C) and (180 s; 60 °C), as the solution reads them.
- The hash was the same at the start and at the end.
