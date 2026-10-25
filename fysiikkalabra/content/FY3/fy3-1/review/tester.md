VERDICT: PASS
CONTENT-HASH: 941320a85db9b4cb

Final tester check, fy3-1 (wording-only edits since last PASS).

1. gate.py --hash fy3-1 -> 941320a85db9b4cb (start and end, unchanged).
2. test_sims.py fy3-1 -> `PASS preview/fy3-1  [] []`
3. `git diff 975714b~1 975714b --stat -- content/FY3/fy3-1/sim.js tests/sims/fy3-1.json` -> empty output: neither file changed in the last commit.
4. Own Playwright run (preview/fy3-1.html, headless Chromium):
   - 1280 px: console errors/warnings [], page errors [], no horizontal scroll.
   - 320 px: console errors/warnings [], page errors [], no horizontal scroll.
   - G = m g checked for Kuu 1,62 / Mars 3,71 / Maa 9,81 / Jupiter 24,8 at m = 1, 7, 25, 50, 100 kg (20 combinations): 0 mismatches; simState.m and simState.g also correct (e.g. Mars 25 kg 92.75, Jupiter 100 kg 2480, Kuu 1 kg 1.62).
   - Proportionality over all 20 combinations: stretch/G = 0.0766129 (min = max), arrow/G = 0.0443548 (min = max), each bar/G constant per body.
   - Readout (DOM text): 'Massa m = 100 kg (sama kaikkialla)\ng = 24,80 m/s² (Jupiter)\nG = m · g = 2480,0 N' -> g in m/s².
   - "N/kg" in page HTML: False; in visible body text: False.

No failures. No missing assertions noted.
