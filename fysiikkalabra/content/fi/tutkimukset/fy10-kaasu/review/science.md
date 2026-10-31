VERDICT: PASS
CONTENT-HASH: 0ec9c5c89c784dc6

## Blocking
None.

## Polish
None open. Both polish points from the previous review (hash f3ac9962b7bb5d92) are fixed correctly.

## Checked (revision to 42873aed6a17b4f6)
- Sensor-type check: open to room air, a total-pressure sensor reads about 100 kPa and a gauge sensor reads about 0. Total pressure = gauge reading + air pressure. Weather services report sea-level-reduced pressure, so local pressure is somewhat lower at altitude. All correct.
- Two causes told apart by the intercept sign. Gauge readings: straight line, intercept about $-p_\text{ilma}$. Dead volume: positive intercept, and the points bend down at large $1/V$ (concave). My fits for $V_0 = 5$ ml, $V = 20$–$60$ ml: about +23 kPa, and about −101 kPa for a gauge reading. $V = \text{vakio} \cdot \frac{1}{p} - V_0$ is exactly linear, and its intercept $-V_0$ has the right sign and meaning.
- Error direction in the isochoric series: tube air at room temperature makes $p$ change less than the model predicts, the fitted slope too small and the extrapolated zero below 0 K. My fit with 5 % of the volume outside the bath: about −17 K. Correct, and the effect grows with the tube's share, as stated.
- teacher.md, why V–T at constant p is left out: it needs a volume that moves freely at constant pressure, and syringe friction makes that inaccurate. The extension's $pV/T$ still links all three quantities. Sound.
- Unchanged and still correct: Boyle $p = \text{vakio} \cdot \frac{1}{V}$ with slope $pV$ (1 kPa·ml = 1 mJ); total pressure required in the theory outside the tuki blocks; $p \propto T$ in K, extrapolated (dashed), with its conditions stated; extension $pV/T = nR$ and the warning that refilling changes $n$; "sopusoinnussa", not proven equal; uncertainty propagation; predictions 1–2.
- No pressure limit invented. Figures show model lines only, with no data points; the SVGs match figures.py.
- Stray control characters: none. No tab or other control character in investigation.md, teacher.md, investigation.json (also after JSON decoding) or figures.py. Every `\text`, `\theta`, `\frac` and `\dfrac` is intact. `build.py fy10-kaasu` builds.
- `investigations.py hash fy10-kaasu` gives 42873aed6a17b4f6 at the start and at the end.
