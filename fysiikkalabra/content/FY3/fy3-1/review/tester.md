VERDICT: PASS
CONTENT-HASH: 307c0dfc144588a5

Re-review after the human-ordered change (g in m/s², never N/kg). Hash before and after: 307c0dfc144588a5 (unchanged).

1. test_sims.py: `PASS preview/fy3-1  [] []` (no console errors, no failed assertions; 19 assertions).
2. Test file history (`git log -p -3 -- tests/sims/fy3-1.json`, commit cf407aa): only two strings changed, the note of the g assertion ("9,81 N/kg" to "9,81 m/s²") and the readout assertion (`x.includes('g = 9,81 N/kg')` to `'g = 9,81 m/s²'`, with its note). No expected value, tolerance or expression was loosened. The assertions cover the sim-spec (G = m g, four bodies, stretch/arrow/bars proportional to G, canvas size, options, slider unit, readout).
3. preview/fy3-1-sim.js is identical to content/FY3/fy3-1/sim.js (diff empty). `grep -c "N/kg"` is 0 in preview/fy3-1.html, preview/fy3-1-sim.js and every file of content/FY3/fy3-1 (including review/).
4. Own Playwright run (viewports 1280, 390, 320 px), console/page errors: `[]` at all three widths. No horizontal overflow.
5. For all four bodies (g 1,62 / 3,71 / 9,81 / 24,8) at m = 1, 7, 10, 33, 100 kg: simState.G = m g (exact to 1e-9), simState.g and body correct, stretch/G = 190/2480, arrow/G = 110/2480, every bar/(m g) = 220/2480 (all constants), and readout contains "m/s²". Result at every width: `proportionality/G all ok: True`.
6. Text: DOM body text and full page HTML contain no "N/kg". Canvas fillText strings (hooked) are only "n kg" and "x N" values; none contains "N/kg". Readout: `Massa m = 10 kg (sama kaikkialla) | g = 9,81 m/s² (Maa) | G = m · g = 98,1 N`.
7. Canvas 600x400 at all widths; select options `['Kuu','Mars','Maa','Jupiter']`; slider label `Massa m = 10 kg` (unit kg).

Missing assertions: none. No failures.
