VERDICT: PASS
CONTENT-HASH: 83e12053f0efcc73

Science review of the English translation of fy9-ympyraliike, round 3 (source content/fi/units/fy9-ympyraliike/ PASS at 678dc353273487b6). Reviewer 2026-11-04.

Since round 2 the only changes are figure texts in the concept map: the redrawn figure (after the shared figlib.translate() fix for \textbf{}) and the round-2 Polish 1 wording, which this reviewer applied. No number, formula, answer, tolerance or correct flag has changed; the round-1/2 checks still hold (geostationary r = 42 160 km, h = 35 790 km, polar satellite 7438 m/s and 101.4 min, loop 22.76 m/s and 3696 N, trailer 445 N / 45.3 kg, exit ticket 2.51 m/s). check_i18n.py: en 0 errors; units.py check: 77 units ok; practice.py check en/units/fy9-ympyraliike: OK, 6 tasks, 95 points.

## Blocking
None.

## Polish
1. Round-2 Polish 1 fixed: figures.json "ei etene" now "does not start to move" (concept map beside $\Sigma\overline{F} = \overline{0}$), and the alt text says "so the body does not start to move", consistent with the "Key idea". Figure redrawn with units.py figures --lang en; label fits at 390 px.
