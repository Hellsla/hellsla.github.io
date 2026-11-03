VERDICT: PASS
CONTENT-HASH: 304ecd496a987db8

## Blocking

## Polish
- lesson.md:209 (Kahden virtajohtimen välinen voima): the paragraph uses $B_1 = \mu_0 I_1 : (2\pi r)$ without saying the wires are long and straight ($l \gg r$). The retrieval item says it, and every task meets the condition (2 m vs 1,5 cm), so this is not blocking. Suggest writing "Kahden pitkän suoran rinnakkaisen virtajohtimen …".
- inquiry.json:319 check-1, the correct option's feedback: "kääntäisivät silmukkaa puolen kierroksen jälkeen takaisin" is loose. The torque reverses as soon as the loop passes the position perpendicular to the field. Suggest "kun silmukka on ohittanut kenttää vastaan kohtisuoran asennon, voimat kääntäisivät sitä takaisin".
- lessons/FY7/fy7-4/lesson-answers.py:39 says "wire east–west" in its comment, but the tarkistus-2 prompt gives no direction. Fix the comment only.

## Checked
- I recomputed every number in one script with my own formulas, and all agree. Worked example: 4,90 m and 6,98 N → 7,0 N. Sim values: Δm 2,45, 1,22, 1,22 and 2,12 g, readings 247,75 and 242,85 g, B 0,080 T. siirto: 0,60 N, with mistakes 0,006, 3,77 and 0,30 N. virhe: 0,15 vs 0,26 N. tarkistus-2: 0,20 N (cos gives 0,346). Exit ticket: 0,30 N, and east × north = up.
- The changed speaker figure is right. The field points radially out from N to S, the current goes in (×) at the top and out (•) at the bottom, and F points toward the cone on both sides. Its aria-label agrees.
- The directions in swing, motor, angle and wires agree with I × B. The motor turns counter-clockwise, and its forces point away from the axle at the perpendicular position.
- The new radial-field sentence is correct: in a uniform field the net force on a closed coil is zero. tarkistus-3 says the same.
- The new check-1 distractor is clearly wrong, and its feedback says why. Each item has exactly one correct option.
- sim.js: F = I l B sin α. The top-view and side-view signs agree, and the reading is m = m0 + F/g. The locks isolate I and α.
- The ampere definition, the tesla unit and μ0 are right. The scope is within FY7, and "kupari ei ole ferromagneettinen" is a fair simplification (C).
