VERDICT: FAIL
CONTENT-HASH: eb1f18684a64aec9

## Blocking
- lesson.md:192 (figure electromagnet; lessons/FY7/fy7-3/figures.py electromagnet()) — A: the right panel, "virta katkaistu", wires the battery straight to both coil leads (M476,96 H524 V128 and M476,210 H524 V182), so the circuit it draws is closed. The "switch" is a loose line on the battery's side (540,155 → 564,140) and is not part of the circuit. The left panel has no switch at all, although the aria-label says "johtimet menevät paristoon ja kytkimeen". A student sees a closed circuit labelled "current cut". — Fix: put a switch in one lead in both panels, closed on the left and open with a visible gap on the right.

## Polish
- inquiry.json:15 (hook) — "3 A … neula kääntyy lähes poikittain" holds only when the wire is very close to the needle. With B_h = 14 µT the needle turns 77° at 1 cm, 65° at 2 cm and 41° at 5 cm. Say "aivan neulan yläpuolella" or give about 1 cm.
- inquiry.json:264 (mittaus mistake 0.00123) — forgetting the mT → T conversion gives 1233, not 0.00123. The value 0.00123 has an extra factor of 10⁻³, so the feedback "Tarkista millitesla" does not describe it. Use 1233, or make the feedback fit the error.
- inquiry.json:436 (tarkistus-2, Järkevyys) — "hitsauskaapeli kääntää lähellä olevan kompassin selvästi" holds for DC welding current. With a 50 Hz AC welder the needle does not follow the field. Add "tasavirralla".

## Checked
- One script, my own formulas: example 12,57 mT/251; Etsi virhe 5,03 mT; siirto 0,2653 A (mistakes 26,5, 3,33); check 2 1,5 mT (0,015, 9,42); exit ×1; wire graph 200/100/50 µT.
- Sim axis model = calc = lesson-answers: load 1,232 vs 1,257 mT; koe-1 4,67/2,46/1,66/1,25; koe-2 2,46/2,41/1,25/0,363 mT.
- Fit A = 2,4651, B₀ = 0,0352, ΔA = 0,0121; μ₀ 1,2326·10⁻⁶; 1,74 %; finite factor 0,983 → 1,254. coil-fit figure matches.
- Round-1 items all fixed.
- Directions (wire views, compasses, coil •/×, sim N end, exit ticket 2); one correct option per choice item, distractor feedback right; experiments isolate l and x.
- Conditions stated; scope FY7 only.
