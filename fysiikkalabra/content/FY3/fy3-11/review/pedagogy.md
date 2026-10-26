VERDICT: PASS
CONTENT-HASH: 87ecc45640f9156a

## Blocking

(none)

## Polish

1. inquiry.json exp-1 `question` — the experiment asks about Q = ΔU + W_k, which the sim readout already prints ("ΔU + Wk = 500 J"), so it is read, not inferred. What Ennuste 1 is about (W_k = pΔV, the area) gets no evidence question. Fix: ask which quantity W_k is proportional to (ΔV, at constant p), or give the rows 500/750/1000 J and ask for W_k/ΔV. The intro also states "Lämpö 750 J vie tilavuuden 1,0 → 2,5 l", which does the setup for them.
2. inquiry.json exp-2 `intro` — one dense paragraph (shelf, locked piston, extra weight) is hard to follow on a phone. Fix: split into two short lines, "A: …" and "B: …", and say that p₂ < p₁ because cooling at constant volume lowers the pressure (fy3-9 covers only isobaric).
3. inquiry.json `suunnittele` table — at 390 px the assumption column is cut off ("sähköä 40 % polttoai…"), scrollable sideways with no cue. Fix: wrap the cells or use a list.
4. inquiry.json `siirto` solution — "≈ 23 MW" while the answer is 22,5 (22,5 MW). `suunnittele` solution "Polttoaineteho on yhtä suuri kuin hyödyksi saatu 800 MW" is confusing; drop it. The symbol P_s means plant output in the Esimerkki but heat-pump electricity in the tasks; use P_pumppu in the tasks.
5. Workload: about 25 activities (two experiments of at least 2 rows, a design task with a 2-unknown system, 12 exercises, 3 checks). It is an hour only if the exercises are chosen from; the lesson should say so ("valitse 4–5 tehtävää").

## Checked

- Cycle idea at 390 px: the sim shows A (W = 0, Q₂ = Q₁ = 500 J) and B (Q₁ 650, Q₂ 550, W 100 J, η 15 %) without cycle theory. The hatched blue area (work done on the gas) has no label in the picture; the exp-2 question explains it.
- Symbols: W_k for gas work, W for net engine work, E_s for pump electricity. The fy3-5 bridge W = −W_k is stated in the Kertaus and in Kaava. Clear.
- Refutability: pred-1's 200 J, 500 J and 300 000 J options fail on the table rows. In pred-2, Aino fails on A, Cem on the frictionless sim, Daniel on Q₁ = W + Q₂.
- Gating: feedback appears only after a committed answer ("Palaute näkyy, kun olet tehnyt mittaukset"), and reveal needs 2 rows. No answer to the opening question is shown before commitment. The sim, with its readout, is visible while predicting, which is the same site-wide as every lesson.
- Variable control: exp-1 varies Q only (paluu locked); exp-2 varies paluu only (Q and p₂ locked). "Aseta alkutila" sets the sim state; checked.
- Sim at 390 px: no horizontal scroll (390 = 390), buttons 40 px high, readout legible, locked controls greyed with "(vakio)". The speed control is present.
- Design task numbers check out: option 3 gives 800 MW; the mistake values 2000, 1250, 941 and 667 match their derivations.
- Exercises 5/4/3, none repeats the Esimerkki; the exit ticket tests W_k, η and the heat pump. Finnish reads fine.
- Hash unchanged at the end.
