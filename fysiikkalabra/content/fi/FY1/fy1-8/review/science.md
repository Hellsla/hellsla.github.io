VERDICT: FAIL
CONTENT-HASH: 320dd4262c607fdd

## Blocking
- content/fi/FY1/fy1-8/inquiry.json:164 (`suunnittele` model) — the model plan says a ball released from rest down a slope ("päästetään irti ilman työntöä") has "likimain vakio" speed, so time is proportional to distance. A ball rolling down an incline from rest accelerates (s ∝ t², not s = vt), so the model answer presents a physically wrong hypothesis as the example. It also contradicts its own 4 s minimum: 0,50 m in 4 s down a slope is not realistic. — Fix: make the ball roll on a level floor after a short launch ramp, with timing started past the ramp, so constant speed is a fair assumption. Or keep the slope and frame the s = vt hypothesis as one the measurement is expected to refute.
- content/fi/FY1/fy1-8/lesson.md:155 — "sitä lyhyempi mittaus ei kerro mitään, koska epävarmuus on yhtä suuri kuin mittaus itse" is false. Below the minimum distance the relative uncertainty only exceeds the chosen limit ε_max: at 2 s it is 10 %, not 100 %. — Fix: "sitä lyhyemmällä matkalla suhteellinen epävarmuus ylittää valitun rajan ε_max".

## Polish
- inquiry.json:18 (hook) — group B runs 2,00 m "viisi kertaa" with a mean of 4,74 s, but B's table in Tutki has three repeats with a mean of 4,73 s. Make them match.
- inquiry.json:95 — "pidemmillä matkoilla suhteellinen epävarmuus on alle 6 %", but the 1,00 m row has 6,1 %. Say "noin 6 % tai alle".
- lesson.md:77 — "(ks. seuraava osa)" points to Mittauspöytäkirja; the relative-uncertainty rule is in the Kaava section.
- lesson.md:155 — "pitkän tutkimuksen perusta" is unclear wording.
- exercises L2-02 — "kolmen metrin matkan" is given in words, while the solution uses 3,0 m with two significant figures. Write "3,0 m" in the task.

## Checked
- One script recomputed all 12 answers (my formulas, answers.py and exercises.json): all agree.
- Table in Group B's measurement record (poytakirja): means, Δt, ε, v and v-uncertainties recomputed; all printed values are right. The 0,39 ± 0,05 m/s interval contains 0,42 m/s.
- Opening question (hook) and Ennusta feedback: A gives 0,50 ± 0,10 m/s at ε = 20 %; B gives 0,42 m/s ± about 0,01 m/s.
- Worked example: t_min = 4 s, s = 1,68 m → 1,7 m; the reasonableness check (4,05 s, 4,9 %; 0,50 m gives 17 %) is right.
- Graph questions (graafi, virhe, siirto, tarkistus-2, exit ticket, kertaus): answers, mistake values and solutions are right.
- Formula ε = Δt/t and t ≥ Δt/ε_max: correct, and inside FY1's "luotettavuuden arviointi".
- SVG figures: set-up drawn to scale (150 px/m, s = 2,00 m); ε(t) curve hits 20 %, 5 % and 2 % at 1, 4 and 10 s; s–t graph points, ±Δt error bars and the fitted line (slope 0,419; least squares through the origin gives 0,419) are to scale.
- Solutions: each one solves symbolically before substituting values; the L3-01 two-uncertainty argument and the L3-02 data (plausible for Newtonian cooling) are right.
- Correct choice options (reilu-koe, tarkistus-1) are physically right.
