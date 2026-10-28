VERDICT: PASS
CONTENT-HASH: 0944393120c8dd63

Delta review over the audit's PASS (b41a8c9ef224a497): L1-04 (800 − 320 MW) replaced by a figure task (fy3-15/chain-bars: P0 = 400, P1 = 350, P2 = 150, P3 = 140 MW; largest drop and its heat).

## Blocking
- none
## Polish
- exercises/solutions.md:35 — "Pylväiden päät ovat ruudukon viivoilla": P3 = 140 MW is not on a gridline (grid 50 MW); the screenshot shows it just under 150. The answer does not need it, but write "P0, P1 ja P2 ovat ruudukon viivoilla; P3 on hieman alle 150 MW, noin 140 MW".
## Checked
- Figure code and screenshot: bars at 400, 350, 150, 140 MW; y ticks every 50 MW, labels every 100.
- Drops: 50 MW (boiler), 200 MW (steam cycle), 10 MW (generator and transformer); largest P1 − P2 = 200 MW; answers.py = 200.
- Tolerance 0,02 -> 196–204 MW; rejects P0 − P3 = 260 MW and P0 − P1 = 50 MW.
- Balance 50 + 200 + 10 = 260 = 400 − 140; steam cycle 150/350 = 0,43, plant 0,35, generator stage 0,93: plausible.
- Steady operation and energy conservation stated; heat to surroundings = drop in a stage, consistent with the lesson.
