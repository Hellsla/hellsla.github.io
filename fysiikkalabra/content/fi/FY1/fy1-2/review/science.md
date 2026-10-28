VERDICT: FAIL
CONTENT-HASH: a5d16bc42cc16ad8

## Blocking
- content/fi/FY1/fy1-2/inquiry.json:116 (sim `model`, Mallin oletukset) — still says "heliopaussin eli Auringon vaikutusalueen rajan ylityksestä". "Vaikutusalue" (sphere of influence) is a gravitational idea. The new hook (line 18) correctly says Voyager 2 is "yhä Auringon painovoiman piirissä", and the teacher's brief (fy1-1) contrasts the heliosphere with the reach of the Sun's gravity. So the box contradicts the hook and teaches the misconception the change was meant to remove. Fix: "heliopaussin eli aurinkotuulen kuplan rajan ylityksestä" (or "rajan, jonka ulkopuolella aurinkotuuli ei enää hallitse avaruutta", as in `voyager-malli`).

## Polish
- content/fi/FY1/fy1-2/solutions.md:97 (fy1-2-L3-01 Sijoitus) — $2{,}998\cdot10^{5}\cdot3{,}156\cdot10^{7} = 9{,}4617\cdot10^{12}$ rounds to $9{,}462\cdot10^{12}\,\text{km}$, not $9{,}461$. This was also flagged in earlier rounds; the final AU answer is unaffected. Fix: write 9,462.

## Checked
- Hash a5d16bc42cc16ad8 at start and end; diff since the last PASS (077ae69): prior line, hook, the new section at lesson.md:250, and the s = ct sentence.
- New table: nucleus 10⁻¹⁵–10⁻¹⁴ m (proton about 1,7 fm up to heavy nuclei about 15 fm), atom 10⁻¹⁰ m, red cell 7,5 µm, Earth 1,27·10⁷ m (12 756 km), planet region 10¹²–10¹³ m (Neptune's orbit diameter is about 9·10¹² m), stars and galaxies 10¹⁶–10²¹ m; the prefix definitions (fm, nm, µm, km), AU ≈ 1,5·10¹¹ m and ly ≈ 9,46·10¹⁵ m are right.
- H atom 0,11 nm (2a₀ = 0,106 nm) and proton 1,7 fm (2 × 0,84 fm) are correct; the AU and the light-year are correctly called non-SI units defined in metres.
- Prior line: log₁₀(8,8·10²⁶ / 1,6·10⁻³⁵) = 61,7, so "yli kuudellakymmenellä" holds.
- Hook: the heliopause as the edge of the solar-wind bubble, and Voyager 2 still bound by the Sun's gravity, are both correct.
- s = ct for light at constant c, then t = s/c, stays within FY1's s = vt scope; 1 AU takes 499 s = 8,32 min.
- One Python run reproduced all 12 exercise answers, the worked example (4,503·10⁹ km, 4,17 h), siirto 3,236 AU/a, tarkistus-2 3,22 min and every mistake value (3236, 4,84·10⁸, 193, 0,0536); they agree with answers.py.
- Voyager model: 142,86 AU and 19,8 h on 1.1.2026 (ratio 142,9); 143,26 AU in mid-February 2026 (JPL gives 143,05 AU); the table rows 119,7 / 132,6 / 145,6 / 158,5 AU with 16,6 / 18,4 / 20,2 / 22,0 h are right.
- Experiment 1 gives 33,4 / 334 / 3340 s; the prediction feedback (7,2 AU per hour, about 1212 AU per week, 63 250 AU per light-year) is right.
- sim.js is unchanged since the last PASS; the earlier checks of its scale (1 px = 3474 km, 86,3 px/s, Sun 401 px) still hold.
