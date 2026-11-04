VERDICT: FAIL
CONTENT-HASH: 061654f593114adf

## Blocking
- content/fi/FY7/fy7-13/exercises/solutions.md:190 (L3-05 b) — A: "pahvilla näkyy kolme valopistettä: reikä ja maksimit k = ±1". The beam hits the disc perpendicularly, so the k = 0 reflection goes straight back through the hole towards the laser and makes no spot on the card. Only the two k = ±1 spots show there — fix: answer "kaksi valopistettä (k = ±1); nollannen kertaluvun heijastus palaa reiän kautta laseria kohti, joten maksimeja on kolme (k = 0, ±1)", or change the question in exercises.json:312 to "Kuinka monta maksimia syntyy?" (3).
- content/fi/FY7/fy7-13/exercises/exercises.json:254 (L3-04 b) and solutions.md:179 — A (the task asks for something its data does not give): "Tarkista, sopiiko tulos taulukon lukemiin" asks for a check against the table, but the table (exercises.json:271–303) runs only from 3,0 to 7,0 mm and x₂ = 10,0 mm lies outside it. The solution does not do the check in b either. The table also leaves out the central maximum, so the reader cannot see that the 5,0 mm peak is the first order — fix: extend the data with rows from the same cos² model (fringe spacing 5,0 mm), e.g. 0,0 → 1,00, 1,0 → 0,65, 2,5 → 0,00, 7,5 → 0,00, 9,0 → 0,65, 9,5 → 0,91, 10,0 → 1,00, 10,5 → 0,89 (an envelope may lower them), and have b) read the 10,0 mm peak from the table.

## Polish
- solutions.md:190 (L3-05) — close to the existing L3-02 (CD), as planned; 3 significant figures is weak with 2x = 8,3 cm.
- exercises.json L3-04 — kind "graph" but nothing is plotted: ask for a sketch of I(x) or drop "graph".
- L2-07 — answered word for word by the lesson's measurement paragraph, so it is closer to level 1.
- The plan's level-2 picture questions (`pattern`, `setup`, `white`) are missing (pedagogy).

## Checked
- All 18 answers recomputed in one script: exercises.json, answers.py and mine agree (L1-07 32,14°, L1-08 4, L2-05 633,7 nm, L2-06 5,53 %, L3-04 625,0 nm, L3-05 0,7374 µm).
- L2-05: tan then sin, LSQ through the origin, per-point λ 625–638 nm.
- L2-06: 562 against 532,3 nm, tan/sin = 1,055.
- L3-04: the data fit cos²(πx/5,0 mm) to ±0,01; x₂ = 10,0 mm; part c is right.
- L3-05: sin θ₂ = 1,44 > 1; −0,36 %.
- L1-06 and L2-07: exactly one correct option, all feedback right; conditions stated; lesson symbols used.
