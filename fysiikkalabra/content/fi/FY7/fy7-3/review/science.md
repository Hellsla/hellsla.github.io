VERDICT: FAIL
CONTENT-HASH: 96c7da8962aef32f

## Blocking
- inquiry.json:295 (epavarmuus, solution "Järkevyys") — A: the systematic-error explanation uses "käämin halkaisija on 3,0 cm" and the derived 98 % / 1,254·10⁻⁶ Vs/(Am). No diameter appears in the task text (inquiry.json:246), the coil-fit figure or the mittaus solution. The student is given data the task never stated (recomputed: R = 1,5 cm, l = 16 cm gives a centre factor of 0,983, so the arithmetic is right). — Fix: state the diameter in the mittaus text, e.g. "Käämin halkaisija on 3,0 cm.", after the length.

## Polish
- inquiry.json:268 (mittaus solution) — "2 % pienempi … samaa suuruusluokkaa kuin mittausepävarmuus" reads as "within uncertainty". The next task (line 295) correctly shows that 1,257 lies outside 1,23 ± 0,02 and points to a systematic error. Align the wording, e.g. "hieman suurempi kuin epävarmuus; syy selviää seuraavassa tehtävässä".
- inquiry.json:268 "Kuvaajan lukeminen" — slope estimated as 6,2 mT : 2,5 A, which ignores the intercept 0,04 mT that the same sentence cites. Use (6,2 − 0,04) mT : 2,5 A ≈ 2,46 mT/A.
- inquiry.json:276 (epavarmuus) — the task does not name the method. A student who adds the uncertainties in quadrature (1,3 %) is marked wrong by the 5 % tolerance. Say "laske suhteelliset epävarmuudet yhteen", or add 1,34 as a mistake with feedback.
- lessons/FY7/fy7-3/lesson-answers.py:25 — the comment says 4,87 mT for l = 10 cm; the model gives 4,67 mT. The comment only, not shown to students.
- sim.js picture — the tube is drawn with a radius of about 4 cm at the 8,4 px/cm scale, while the model uses R = 2,0 cm. It is not claimed to be to scale, so this is harmless.

## Checked
- Recomputed in one script, with my own formulas, every lesson number: worked example 12,57 mT / 251; Etsi virhe 5,0·10⁻⁵ T vs 5,03 mT; siirto 0,2653 A with mistakes 26,5 and 3,33; check 2 1,5 mT with mistakes 0,015 and 9,42; exit ticket (×1).
- Least-squares fit of the example data: A = 2,4651 mT/A, B₀ = 0,0352 mT, ΔA = 0,0121; μ₀ = 1,2326·10⁻⁶; relative uncertainty 1,74 %.
- Finite-coil axis model (sim.js, calc, lesson-answers.py): the koe-1/koe-2 values 2,46 / 1,25 / 2,41 / 0,36 mT, and 1,23 vs 1,26 mT on load.
- Predictions: exactly one correct option in each, and every distractor's feedback has the right physics and model values. The experiments lock I, N, x, dir (or l) and vary one parameter; simState gives B and n.
- Directions: wire-field side and top views (arrowheads, compass N-ends counter-clockwise for current up), coil-field (• top, × bottom → B to the right, N right), the sim's dir → N end, exit ticket 2.
- wire-graph polyline is to scale (200/100/50/40 µT at 1/2/4/5 cm).
- Conditions stated: long wire (r ≪ length, other wires far), long coil (centre, air core, end ≈ half), iron core.
- Electromagnet mechanism (domains align; soft iron loses its magnetisation) and the kertaus item agree with fy7-1 as quoted.
- Scope: within the FY7 contents; no self-induction and no para- or diamagnetism.
