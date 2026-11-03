VERDICT: PASS
CONTENT-HASH: a0b2e7a7c4453baf

## Blocking

## Polish
- exercises/solutions.md (fy5-6-L3-02, Järkevyys) — the new check only says that 0,015 % "sopii" for a 0,03 % change in the radius. Adding "eli puolet suhteellisesta säteen muutoksesta, koska $v \propto 1/\sqrt{r}$" would make it a quantitative check without derivatives.

## Checked
- One script recomputed all 12 answers again from the task text with my own formulas, and all agree with exercises.json and answers.py: 7,44; 12,0 h; 0,224 m/s²; 1,02; 1,63 km/s; 9570 km; 3,36; 1,68 km/s; 650 N; 17 040 km; 1,13 m/s; 84,4 min.
- Round 1 polish done: L3-02 now tells the student not to round before subtracting, and the solution says why. L2-04 writes 6,5·10² N, which makes the two significant figures unambiguous.
- L3-01's wording change and its reasonableness check now say "kiertoradan säde r = 20 400 km", which matches r = 2,0427·10⁷ m. The physics is unchanged.
- The new L3-02 reasonableness numbers are right: 2/6771 is 0,030 % and 1,133/7671 is 0,015 %, and the sign explanation (drag lowers the orbit, so v grows) is right.
- answers.py computes the right physics for each line.
- The solutions are complete, solve symbolically first and convert units correctly. The rounding is justified by the limiting datum and the 2 % tolerances fit the data.
- Data are realistic, and the notation matches the brief (γ, r = R + h, $a_\text{n}$, no ω), within the FY5 scope.
