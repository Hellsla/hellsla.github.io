VERDICT: PASS
CONTENT-HASH: 5ebec19a370623c0

## Blocking
None.

## Polish
None open. The three earlier points are applied.

## Checked
- **Revision to 5ebec19a370623c0:** the only text change is in Johtopäätökset, "viittaa siitä" → "kertoo siitä" (I diffed it against c7ebaadb1a475059 with the SVGs stripped). It makes no physics claim. Using the late part of the main graph as partial evidence for prediction 3 is reasonable.
- **Steady-state hint:** now just "voi kestää kauan". My fin estimate, $\tau = \rho c/(2h/r + k\pi^2/4L^2)$, gives about 1–2 min for Cu and Al, 4–8 min for wood and plastic, and about 11 min for steel, so this neutral wording is right.
- **Rise uncertainty:** an offset that is the same in both readings cancels in $T - T_0$ (same spot, same camera), so reading variation matters more. Correct. The worst-case sum and the "differ clearly" rule are consistent.
- **Untaped-stretch test:** the bare and taped parts sit next to each other on one metal rod, so they are at almost the same temperature, and the difference in readings shows emissivity and reflection. The test is placed away from the measuring points, and "Älä koske sauvaan" fits the safety list.
- **Mode O (Cu, steel, wood at $x = 3\ \text{cm}$, about 10 min):** the diffusivities differ by about three orders of magnitude, so the ranking is clear. Wood will show almost no rise at 3 cm ($\sqrt{\alpha t} \approx 1\ \text{cm}$), which is a genuine result and is not predicted on the page. The table and teacher.md agree.
- **Model graph:** $1 + 8\,\text{erfc}(c/\sqrt{t})$ is the semi-infinite-rod shape. The delay on the fast curve is correct for $x > 0$. The graph has no data points or numbers and says it is a model.
- **Setup figure:** the tape is above the water only, which matches the text. The rendered SVG matches figures.py.
- **Unchanged and correct:**
  - Early heating compares diffusivity, not $k$ alone.
  - Steady state is independent of $\rho c$ (fin equation $kA\,T'' = hP(T - T_\infty)$), under the stated equal shape, surface and temperatures.
  - The emissivity explanation, the same-tape fix, and glass being opaque to the camera's infrared.
  - Camera accuracy treated as mainly systematic.
  - No camera specs or safety values are invented.
  - The hero does not reveal the ranking.
  - The page matches the card (p. 15, inventory item 25).
