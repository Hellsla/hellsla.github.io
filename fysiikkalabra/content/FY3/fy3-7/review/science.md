VERDICT: PASS
CONTENT-HASH: e352c445313a4f16

## Blocking

## Polish
- sim.js:1048,1058 (thermometer reading `tx(T, 0)`) — for −0,5 °C < T < 0 °C the reading shows "−0 °C" while the ice warms (unchanged from the old `fi`) — round to 0 when |T| < 0,5.
- sim.js:1073 — at 390 px the faint preview curve (stroke 205) lies on the 100 °C grid line (stroke 225) and the boiling plateau is hard to tell from the grid before *Lämmitä*; the bold red run curve is clear — draw the preview curve a little darker.
- exercises.json L1-03 — 45 kg/m² (about 5 cm) is a lot for "syksyn ensimmäinen pakkasyö" (carried over).
- solutions.md L3-02 — "Muutama kauhallinen" understates: one ladle already gives 27 K (carried over).
- lesson.md phase-diagram SVG — the liquid/gas fill boundary runs on horizontally past the end of the vaporisation curve, hinting at a boundary above the critical point (taste, carried over).

## Checked
- Since the last PASS (46aa00b) only sim.js and tests/sims/fy3-7.json changed. The sim.js diff is labels only: text → `$…$`, `fi` → `tx` (decimal `{,}`, TeX minus), thousands separator `\,`. Physics, constants, `stateAt`, `stages`, simState keys and the adapter are unchanged.
- Test diff: the 5 changed assertions read `simText` and still check every number they checked before (phase name, T = 0,0 °C, Q = 100,0 kJ, t = 100 s, 167 s, 1130 s, axis 0–2000 s; −10,5 °C and Q = 10,0 kJ; boiling phase text; pace 60 and 30 s; m = 0,80 kg, P = 2500 W). The new readout assertion is stricter (it also checks 167 000 J / 1000 W and 1 130 000 J / 1000 W). The −10,5 test lost only its "T =" prefix: no physics check is lost.
- `test_sims.py fy3-7` run now: PASS, 65 assertions, KaTeX labels checked. The `FAIL sims` line in checks.txt is from an earlier run.
- Independent recompute of all 12 answers (one script): all match answers.py within tolerance. Sim values: tEnd 1557,5 s; T(10 kJ) = −10,48 °C.
- Inquiry numbers: pr-lampo 209,5 kJ; pred-1 1130/565 s; pred-2 83,5/565 and 167/1130 s (ratio 6,77); worked example 2,34 MJ/kg; virhe 66,8 kJ; siirto 188 W (mistakes 27,8; 11 300); check-2 0,597 kg (0,677; 4,04); check-3 264 J, ×9,6.
- Screenshots at 390 and 1280 px: the KaTeX labels sit in the right places (axis labels, tick values, plateau labels "sulaa 167 s" and "kiehuu 1130 s", heater 1000 W, −20 °C reading). The readout's values match the model.
- The sim activity's `model` still states the idealisations (all heater energy goes into the water; the steam stays in the container). Experiments exp-1 (m locked, P varied) and exp-2 (P locked, m varied) isolate their parameter, and simState gives tMelt and tBoil.
- The hash was the same at the start and at the end.
