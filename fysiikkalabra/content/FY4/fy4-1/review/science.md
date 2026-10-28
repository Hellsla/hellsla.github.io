VERDICT: PASS
CONTENT-HASH: d1e3f3544f8c599a

## Blocking

## Polish
- inquiry.json:332 — the endpoint-mistake feedback (1,9) builds Δx from the table value 4,2 m, while the question and solution use the fitted line's start 4,1 m — write $\Delta x = 19{,}1\,\text{m} - 4{,}1\,\text{m}$ (read from the line), consistent with "lue piste suoralta".
- solutions.md:43 — fy4-1-L2-01 asks for *matka* but "Kysytty" names *siirtymä Δx*, in a lesson whose point is that they differ — name it matka $s$ (equal to $\Delta x$ here because the motion is one-way and positive).
- assets/sims/fy4/fy4-1/sim.js:52 — a control labelled "Nopeus (toisto)" with hidas/normaali/nopea in a lesson about velocity can be read as the carts' velocity — consider "Toistotahti" (the test at tests/sims/fy4-1.json checks this label and would follow).
- inquiry.json:448 — "alkupaikka on noin −11 m": it is exactly −11 m from the given data; drop "noin".
- inquiry.json (data, mistake 1,3) — only the first neighbouring pair gives 1,3; the others give 1,7 / 1,55 / 1,25 / 1,65, so the neighbour-pair mistake is caught only for one pair (feedback still correct where it fires).

## Checked
- One script recomputed all 12 exercise answers and every inquiry number (exp-1 4,0; exp-3 −3,0; data slope LS 1,494, drawn line 4,1→19,1 = 1,50; siirto 39, x₀ −11; check-2 13; example 2,5 m/s and 170 m; E path 16 m, mean speed 1,6, mean velocity 0) — all match answers.py, exercises.json and the text; mistake values 50/74/5, 25/37, 2,0/40, 3,0/30, 1,9/0,67 are the errors their feedback names.
- sim.js physics unchanged by the LaTeX commit (diff read): pos/vel/path give A 0→20 m; B 0→40; C 20→40; D 30→0 meeting A at t = 6 s, x = 12 m; E 0→8→8→0 with s = 16 m — matching every prediction's feedback numbers.
- Experiments: tapaus locked, t varied on a 0,5 s slider (4,0, 6,0, 10 s reachable); simState exposes t, xA, x2 at those values.
- Test diff: the readout assertions keep the same physics values (A 20,0 m / s 20,0 m, E 0,0 m / s 16,0 m at 10 s; A 5,0, B 10,0 at 2,5 s; D 22,5 m) now read as TeX via simText; only the Lisätietoja-wording check was replaced, and that text (model values, constant velocity, case 4) is now in inquiry.json `model`. No physics check lost.
- Readout formatting `tx()`: no negative position occurs (D and E stop at exactly 0), so the dropped Unicode minus cannot show as "-0,0".
- Figures to scale where claimed: displacement (40 px/m; +6 m, −5 m), jogger (5,4 px/s, 1,17 px/m; 20/120/170 m), robot data (points and line on 11,1 px/m), E graph (0→8 m, 4–6 s plateau).
- Formulas $v_\text{ka}=\Delta x/\Delta t$, $x=x_0+vt$ with conditions (uniform motion, x₀ at t = 0) stated; inside FY4 "tasainen suoraviivainen liike"; worked example and every solution symbolic first.
- Sign conventions consistent (siirtymä/nopeus as signed components of vectors; matka/vauhti non-negative) across lesson, exit ticket and check-3 model answer.
- 1280 px and exp-3 captures: KaTeX labels and readouts render; numbers match the model.
