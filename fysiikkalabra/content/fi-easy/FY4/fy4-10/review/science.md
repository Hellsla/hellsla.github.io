VERDICT: PASS
CONTENT-HASH: 37da2defef2c46f3

## Blocking

## Round (delta)
- Only change since the previous pass: sim.js mass options now use the page language's decimal sign (git diff 0c6ca8ec). Built fy4-10 and opened the fi-easy page: mass selects show 0,20/0,40/0,60 kg (decimal comma), no page errors. Earlier Polish note about the sim's decimal comma is resolved. Verdict unchanged.

## Polish

## Checked
- Re-reviewed the passages changed since the earlier review (git diff a6af45ae): inquiry.json stage "simulaatio" (text, howto, model, calc) and the fy4-10 sim strings in lang/fi-easy.json (kok, sis, lukemat; selite unchanged) against the Finnish. lesson.md, exit-ticket.json, meta.json and figures.json are unchanged.
- Every changed fact agrees with the Finnish: energy bars E_k, E_p (bumper or spring), E_sis and the dashed original total; kinetic energy dips for a moment even in an elastic collision; with the tape the bumper stays compressed and its energy becomes internal energy; E_p = 1/2 k d^2, k = 300 N/m; E_sis from the work of the bumper damping; E_k + E_p + E_sis constant; 4,0 cm, 0,24 J, 0,2 ms unchanged; decimal comma in all numbers and LaTeX; symbols E_k, E_p, E_sis, p_kok identical to the Finnish.
- Readout string: same placeholders and order as the Finnish.
- check_i18n 0 errors; figures.py fy4-10 --lang fi-easy --check clean; build.py fy4-10 run; check_layout fy4-10 OK at 360 and 1280 px.
- Sim opened in the built fi-easy page at 390 and 1280 px, all four cases run: legend (E_k, E_p, E_sis), "ennen"/"nyt", p_kok and readout fit the canvas, no horizontal scroll.
