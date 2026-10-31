VERDICT: PASS
CONTENT-HASH: e60c792ab4128301

## Blocking

## Round (delta)
- Only change since the previous pass: sim.js mass options now use the page language's decimal sign (git diff 0c6ca8ec). Built fy4-10 and opened the en page: mass selects show 0.20/0.40/0.60 kg (decimal point), no page errors. Earlier Polish note about the sim's decimal comma is resolved. Verdict unchanged.

## Polish
- The Finnish symbol $E_\text{sis}$ is $E_\text{int}$ in en (inquiry.json and the sim key "sis": "int"); other en chapters write E_thermal for the Finnish E_lämpö, but the sim's quantity is internal energy as a whole, so E_int is consistent within the chapter.

## Checked
- Re-reviewed the passages changed since the earlier review (git diff a6af45ae): inquiry.json stage "simulaatio" (text, howto, model, calc) and the fy4-10 sim strings in lang (kok, sis, lukemat; selite unchanged) against the Finnish. lesson.md, exit-ticket.json, meta.json and figures.json are unchanged in all three languages.
- Every changed fact agrees with the Finnish: energy bars E_k, E_p (bumper or spring), E_int and the dashed original total; kinetic energy dips for a moment even in an elastic collision (E_p of the compressed bumper); with the tape the bumper stays compressed and its energy becomes internal energy; E_p = 1/2 k d^2 with k = 300 N/m; E_int from the work of the bumper damping; E_k + E_p + E_int constant; 4.0 cm, 0.24 J, 0.2 ms unchanged; decimal point in all numbers and LaTeX.
- Readout string: same placeholders (p0, E0, Ep0, u1, u2, pJ, EJ, t, w1, w2, p, E, Ep, Es, Et) and same order as the Finnish.
- check_i18n 0 errors; figures.py fy4-10 --lang en --check clean; build.py fy4-10 run; check_layout fy4-10 OK at 360 and 1280 px.
- Sim opened in the built en page at 390 and 1280 px, all four cases (elastic, inelastic, tape, explosion) run: energy-bar legend (E_k, E_p, E_int), before/now labels, p_tot labels and readout fit the canvas, no horizontal scroll.
