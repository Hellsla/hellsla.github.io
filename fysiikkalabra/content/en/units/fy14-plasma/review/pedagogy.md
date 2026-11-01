VERDICT: FAIL
CONTENT-HASH: 8408172d1fd67ef6

Pedagogy review of fy14-plasma (2026-11-01). Built with `scripts/build.py`. I read unit.md, inquiry.json and teacher.md, and looked at the captures (intro, ennusta, tutki, fx).

## Blocking
1. `inquiry.json`, all seven choices: the correct option is the longest every time (`review`, `pred-aurora`, `pred-pressure`, `find-error`, `check-1`, `check-2`, `check-3`). The gaps are large:
   - `pred-aurora`: 89 characters against 61–65;
   - `check-1`: 57 against 35–43;
   - `check-3`: 69 against 39.

   A student who always picks the longest option gets both predictions and all three checks right. This is the systematic pattern that writing-guide §2.7 forbids, and the pilot lessons set a limit of ±30 %. Fix: bring each choice within ±30 % and leave the correct option shorter than a distractor in at least half of the choices. For example:
   - `pred-aurora`: "Fast electrons from space hit the upper air." Lengthen "The air above the poles is so hot that it glows like a flame." a little.
   - `check-1`: "Its free charges feel magnetic forces."
   - `check-3`: "Utsjoki lies under the auroral oval." Lengthen "There are fewer city lights in Lapland." to about 55 characters.

## Polish
2. `check-explain` (and its starters `lang-explain`) asks almost exactly what the *Common misconception* section answered a few minutes earlier: 280 W/m³, no gravity, a thin plasma and the walls. The model answer can be copied from the page. Make it a transfer task. For example: "A headline says *Fusion reactor will be hotter than the Sun, so it needs walls that survive 150 million degrees.* Answer in four or five sentences, using p = nkT." Alternatively, place the misconception section after the check.
3. `pred-aurora` is answered only by reading text (theory-states). Neither investigation touches the aurora. Add one aurora item to `plasma-sort`, for example "the air at 110 km during a bright aurora" (a plasma). The prediction then has some evidence that the student handles.
4. French corner tips (`fx-pl-french`) use English-style respellings (*luh plahs-MAH*, *tray SHOH*). The units that passed (fy14-photoelectric, fy14-fr-bonjour) use another style: italic, Finnish letters, õ/ã/ẽ for nasals, explained in the corner. Use that shared style.
5. Workload: the core theory is about 650 words, which is above the 500 in the guide but below the passed fy14-photoelectric. The 75-minute plan in teacher.md is realistic, and it has a running-out plan. No change is needed.

## Checked
- Order: hook → review → two committed predictions → sort and data → pair comparison → theory. The reveals are tied to `theory-states` and `theory-pressure`.
- The hook, Why line, hero and pressure figure do not give away either prediction.
- CLIL: word bank and starters for both writing tasks; vocabulary match; the French corner with `say`.
- Numeric tasks have complete seven-step solutions and feedback on mistakes.
- `find-error` is optional. teacher.md has plans for fast pairs and for running out of time.
