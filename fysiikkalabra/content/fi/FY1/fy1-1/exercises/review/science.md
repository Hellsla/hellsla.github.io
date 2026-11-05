VERDICT: FAIL
CONTENT-HASH: b0168537939bf78a

## Blocking
- content/fi/FY1/fy1-1/exercises/solutions.md:202 (L1-09, A, assessment reasoning) — The Periaate says that the Sun's distance lies between the Moon's distance and Neptune's, "ja vaihtoehdoista vain yksi sopii väliin". That is false: both 1,5·10⁹ m and 1,5·10¹¹ m lie between 3,84·10⁸ m and 4,5·10¹² m. The inference "Aurinko kuuluu Aurinkokuntaan, joten …" is also not valid, because the Moon belongs to the Solar System too. — Rule out 1,5·10⁹ m with a reason of its own (as the Mallivastaus already does), and replace the sentence with "Maan rata on Kuun radan ja Neptunuksen radan välissä, mikä sulkee pois arvot 1,5·10⁸ m ja 1,5·10¹³ m".
- content/fi/FY1/fy1-1/exercises/exercises.json:101 (L1-09, B, assessment) — The task gives the Moon's distance and the Earth's diameter. Neither one separates the key from 1,5·10⁹ m or 1,5·10¹³ m. Those are ruled out only by facts the task does not give: the Sun's diameter, the claim of "about a hundred diameters", Neptune's distance and the "about 400 times" in the key's feedback. The Earth's diameter is not used anywhere. — Replace the Earth's diameter with data that decide the answer. For example: "Auringon halkaisija on 1,39·10⁹ m ja Kuun 3,47·10⁶ m; auringonpimennyksessä ne näyttävät yhtä suurilta". Then d ≈ 3,84·10⁸ m · 400 = 1,54·10¹¹ m, and the feedback and Mallivastaus can show that step.

## Polish
- content/fi/FY1/fy1-1/exercises/exercises.json:263 (L2-07) — "pisteet asettuvat suoralle" (carried over): measured points lie on the line only roughly. — Write "likimain suoralle".
- content/fi/FY1/fy1-1/exercises/exercises.json:67 (L1-06) — The distractor's feedback leaves "malli on teoria" unanswered (carried over). — Add that a theory also stays open to revision.

## Checked
- The hash was b0168537939bf78a at the start and at the end.
- All 19 numeric answers recomputed independently match exercises.json and answers.py, among them L2-07 (0,1019 mm), L3-04 (1,19·10⁹, −42 % at d +20 %) and L3-05 (143,16 AU).
- L1-09 numbers: 1 AU / Moon distance = 390 ("noin 400" is fine), 1 AU / Sun's diameter = 108, light time 8,3 min, 1,5·10⁸ m / 3,84·10⁸ m = 0,39 ("alle puolet"), 1,5·10¹³ m / 4,5·10¹² m = 3,3. Nearest stars are about 4·10¹⁶ m away. Every distractor is really wrong, and the key is correct. The factors of 100 between options fit type 5 in docs/exercise-types.md.
- The other tasks are unchanged and were PASS before. The L1-02 figure exponents (−10, −2) give 8.
