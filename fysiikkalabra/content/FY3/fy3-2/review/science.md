VERDICT: PASS
CONTENT-HASH: d31013346dd6f94d

## Blocking

## Polish
- sim.js:85 — at 390 px the clamped "W = pinta-ala" caption now sits on top of the "F (N)" axis label (exp-2 shot) — move the caption right (e.g. G.x + G.w/2 + ts(20)) or put "F (N)" lower when k > 1.
- inquiry.json:92 — pred-2 feedback still calls simulation output "mittausten" — "mallin arvojen mukaan".
- inquiry.json:234 — "mittauksiisi": the student recorded model values — "kirjaamiisi mallin arvoihin".
- inquiry.json exp-1/exp-2 — the sim computes W = Fs directly, so the experiments confirm arithmetic; the Joule table is the evidence — say so at the point of use.

## Checked
- Conversion since 4132080^: word diff of lesson.md prose, inquiry.json, exercises.json, exit-ticket.json; only plain symbols became inline maths, "(s,F)" became "$(s, F)$" and "Selitä-vaihe" became "Teoriatiivistelmä"; no number, formula or meaning changed.
- solutions.md: the multiset of numbers is unchanged apart from LaTeX subscripts, exponents and \tfrac{1}{2}; symbolic formula first in each solution.
- All 12 answers recomputed in one script: they agree with answers.py and exercises.json within 2 %.
- Inquiry numbers: 98 N; 600/1200 J; 120 → 30 W; 240 W (mistakes 9,6 and 0,24); 180 J (mistakes 240 and 120); check-1 ratio 3; virhe 4,0 J; exit ticket 98 J and 20 J; Joule table Q/W ≈ 0,99.
- Teoriatiivistelmä references in pred-3 point to the theory stage (Ydinajatus + Kaava), which holds the carry figure and W = Fs with its condition.
- Speed control: u advances by min(Δt, 100 ms)·speed/t, so W, P and Wdone(u) do not depend on speed; the readout's elapsed time u·t is simulated time; the `howto` text says so correctly.
- Model limits (constant speed, friction = pull, work → heat) moved from the canvas note to the "Mallin oletukset" panel, which the page shows.
- simState still holds F, s, t, W, P for the experiments; exp-1 locks F and t and varies s, exp-2 locks F and s and varies t.
- Figures: the spring graph is to scale (0,20 m ↔ 302,5 px, 40 N ↔ 171 px); the F and G arrows are equal (58 px); h is marked between the correct edges.
- Formulas W = Fs, area under (s,F), W = Gh = mgh, P = W/t = Fv: conditions stated and within FY3 scope.
