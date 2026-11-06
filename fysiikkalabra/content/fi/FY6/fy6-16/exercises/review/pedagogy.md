VERDICT: FAIL
CONTENT-HASH: d7cc99d546a9be81
Round: 1

## Blocking
- exercises.json:230 (fy6-16-L2-08) — the options catch only unit and percent slips (factors 10, 100, 1000), not the chapter's own warned mistake, multiplying by η instead of dividing (t = 24 · 0,85 : 1,84 ≈ 11 h) or leaving η out (13 h). Both land beside 15 h, and "Valitse lähin arvo" makes a student who made that error choose 15 h and read "Oikein", so the mistake the lesson names is confirmed, not caught. A magnitude form cannot test a 25 % error — fix: change the form, e.g. type 4 (find the faulty line of a worked solution, one line multiplying by η) or type 6 (what happens to the time when η falls from 85 % to 60 %), keeping the unit slips as feedback.
- exercises.json:230 — 0,015 h (54 s), 0,15 h (9 min) and 15 000 h (21 months) are absurd for charging a car from a socket, so 15 h is found by common sense without calculating; if the magnitude form is kept, use values that a unit slip could really give for a plausible charge with the reasoning in the feedback.

## Polish
- exercises.json:243,256 — "samassa kerrannaisessa" is not Finnish usage; write "samassa kerrannaisyksikössä (kWh ja kW)".
- exercises.json:230 — the same calculation as L2-06 b) (t = W_akku : (ηP)) and an outlet as in L1-02; the new part is only the choice of magnitude, so there is little to gain as a separate task unless the form is changed as above.

## Checked
- Text only (no render); chains measured with KaTeX at 16 px: t = 24 kWh : (0,85 · 1,84 kW) 113 px, P = UI 195 px, under 300 px.
- Recomputed: P = 1,84 kW, t = 24 : (0,85 · 1,84) = 15,3 h; the three wrong values 0,0153 h, 0,153 h and 15 345 h come from exactly the slips the feedback names.
- Correct option not identifiable by form: equal wording ("noin ... h"), no hedge, only its value is plausible (see Blocking).
- Within the chapter (P = UI, t = W : (ηP), kWh and kW); the question is the last sentence; Finnish otherwise correct.
- Hash unchanged at the start and end.
