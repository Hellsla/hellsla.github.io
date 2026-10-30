VERDICT: FAIL
CONTENT-HASH: 112ed45a9ee7889a

## Blocking
- lesson.md:346, 348, 350, 395, 400, 401, 461; inquiry.json:385, 389, 607, 611 (and the glossary term *törmäysaika*): the mean force is written $F_\text{k}$, but the momentum chapter fy4-9 (lesson.md:489–543, its solutions) writes it $F_\text{ka}$. The same quantity carries two symbols in consecutive chapters (A, internal consistency across chapters). Fix: use $F_\text{ka}$ everywhere in fy4-11, including the axis label and the two bar labels of figure 6 (the "Kuvaaja mittakaavassa … keskimääräinen voima" figure) and the glossary entry, or change both chapters to one agreed symbol.

## Polish
- lesson-answers.py, comment `imp25-…`: it says 41,8 km/h for 60 km/h. The code gives 40,7 km/h, which matches the "noin 41" in the text. Also `sp-100` says 70,7 m, but the code gives 70,64 m, which the text correctly shows as 70,6 m. Fix both comments.
- inquiry.json `tilasto`: the 97–98 % belt use is for front seats only, while the deaths include rear-seat passengers. Adding "etupenkillä" to the feedback "vyöttömiä on liikenteessä muutama prosentti" would keep the comparison exact. The conclusion ("moninkertainen") still holds.
- lesson.md:288: OTI says the 114 "olisi voinut eri todennäköisyyksillä selvitä". "Lautakuntien arvion mukaan" already carries this hedge, so the wording is acceptable.

## Checked
- I recomputed every number in one script with my own formulas (pysähtymismatka, törmäysnopeus, $a=\mu g$, impulse): 50/100 km/h 13,9/10,7/24,6 and 27,8/42,9/70,6 m, ratio 2,87; 60 km/h → 40,7 km/h at 25 m; 80 km/h on ice 165 m; siirto 53,5 km/h; check-2 62,96 m; worked example 71,9 m; Δp 1042 kg·m/s, 10,4 kN / 104 kN, 14 × G; μ = 0,917. All are correct.
- Sources verified. The OTI-Turvavyöraportti 2023 gives 278 belted and 198 unbelted car and van occupants killed and 114 who could have survived. Liikenneturva's calculator assumes 1 s and 9 m/s². Taloustaito 2025 gives 98 % and 97 % for 2024. The provenance labels are right: "statistics" with source_note, "example" with "pyöristetyt esimerkkiarvot", and sim numbers called mallin arvoja.
- The model's conditions (level road, constant deceleration, no air resistance, full grip) are stated at the formulas, in the worked example and in the sim box.
- Force diagram (figure 2): G, N of equal length, friction backwards at the tyres and about 0,92 G, no force of motion; v and a are drawn beside the car, not as forces.
- Figures 3 and 6 are to scale. In figure 4 the unbelted passenger's gap is consistent (relative travel 0,56 m before impact).
- sim.js implements the model exactly, including a hit during the reaction time. simState gives sR, sJ, sP, vImpact and a at each experiment's initial state, and every experiment locks all but one parameter.
- Every prediction, experiment question, error-spotting item and check has exactly one correct option, and each distractor's feedback is correct.
- The exit ticket and the explain model answers agree with the theory. The airbag is described as working with the belt.
