VERDICT: FAIL
CONTENT-HASH: 5976e5a1e11b688e

## Blocking
- inquiry.json:81 (pred-2 prompt) — B: "törmäys on kimmoisa: liike-energiaa ei muutu muihin muotoihin" is true only for the totals before and after; during the contact the spring bumper stores kinetic energy as elastic energy, and the sim's "nyt" E_k bar visibly dips. The prompt contradicts what the sim shows. — Write instead: "törmäys on kimmoisa: jousi palauttaa puristuessaan varastoimansa energian, joten liike-energia on törmäyksen jälkeen yhtä suuri kuin ennen."
- exit-ticket.json:8 — B: the model answer says the shot is an explosion "jossa vain sisäiset voimat vaikuttavat". Weight and the shooter's support also act on the rifle, and the lesson's law states the real condition, a negligible impulse from the external forces. — Write: "…koska laukauksen lyhyen ajan ulkoisten voimien impulssi on merkityksettömän pieni ja vain sisäiset voimat muuttavat liikemääriä."

## Polish
- lesson.md:333 — "käytetään vain itse törmäyksen … yli" reads as a universal rule. — Write "kun ulkoiset voimat vaikuttavat, säilymislakia käytetään vain…".
- inquiry.json:455 (siirto solution) — "Paino ja veden noste kumoavat toisensa pystysuunnassa" does not hold during the push-off. Only the horizontal momentum matters. — Write "vaakasuunnassa ei vaikuta muita voimia kuin veden vastus, joka jätetään huomiotta".

## Checked
- I recomputed every number in lesson.md, inquiry.json and lesson-answers.py with my own formulas, and all agree: the example 1,14 → 1,1 m/s (E_k 38,3 → 32,5 kJ, 15 %), the inline 0,30 m/s and 0,072 → 0,036 J, pred-1 0,42, the explosion 0,63/1,26 m/s, elastic 0,20/0,80 and −0,12/0,48, virhe 0,025, siirto 1,0, check-2 0,15 and the mistake values.
- sim.js matches the stated model and lesson-answers.py: simState gives u1, u2, pJ and EkJ for exp-1–3, and each experiment varies only m2.
- The derivation from Newton's third law is sound, including a force that varies in time. The condition (zero net external force, or negligible impulse) is stated in the theory, summary, glossary and example.
- In the billiards answer, v1'+v2' = v with v1'²+v2'² = v² leaves only the swap.
- Figures: "tarra" ½v and equal p arrows are to scale (132/66 px). "tyypit" has equal momentum arrows, and the explosion arrows are equal and opposite.
- Every prediction and check has exactly one correct option, each distractor's feedback is correct, and the explain model answers match the theory.
- The scope is FY4 and one-dimensional only.
