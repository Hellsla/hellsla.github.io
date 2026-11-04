VERDICT: PASS
CONTENT-HASH: 68bd08668901c4a2

## Blocking

## Polish
- content/fi/FY7/fy7-14/exercises/solutions.md:109 — "lisäävät kennolle pääsevää valoa noin viidenneksellä" is ambiguous: the gain is 19,5 percentage points of the incoming light but +28 % relative (90,06 : 70,6 = 1,28) — write "noin 19 prosenttiyksikköä eli runsaan neljänneksen".

## Checked
- One recompute script against exercises.json: all 12 answers agree (1117,2; 458,70; 90,58; 112,78; 1,2649; 638,4; 607,2; 282,61; 59,78; 442,86; 90,06 %; 592,1 nm, the last also by brute-force search over d).
- Shift counting right in every task: soap film one shift; MgF2 on glass two; TiO2 (2,30) on glass (1,52) one shift, so λ : (4n) is constructive.
- Visible-range selection: the other orders (319, 202, 1330/266-type values, 1050 and 350 nm) correctly excluded.
- L1-05: equal Fresnel amplitudes give n_p = √n_s (√1,60 = 1,265).
- L3-01: black top k = 0, second dark band k = 2, d = λ : n — matches the task's counting rule.
- L3-02: (1 − 0,013)^8 with the stated no-absorption, no-return assumptions; bare check (1 − 0,04258)^8 = 70,6 %.
- L3-03: consecutive orders (k + ½)630 = (k + 3/2)450 → k = 2, unique; "no other maxima between" stated in the task.
- Every solution has the 7 steps, symbolic before substitution; significant figures follow the limiting datum (two for 1,3 %).
- Units, tolerances (2 %) and magnitudes realistic; notation (2nd, λ_n, Δs, colon division) as in the lesson; scope within FY7 interferenssi.
