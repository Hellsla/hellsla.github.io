VERDICT: PASS
CONTENT-HASH: 22c488369ee7ef37
Round: 2

## Blocking

## Polish
- [Minor] L1-08 — a two-formula ratio is the upper end of level 1 (carried over). The assumption "Käämi on pitkä paksuuteensa verrattuna." now sits before the question in L1-07 and L1-08 (resolved).
- [Minor] L2-05, L3-04, L3-05 — "Vastauslaatikkoon tulee kohdan b) tulos" still differs from "Anna vastauskenttään…" used elsewhere (carried over); keep one phrase.
- [Minor] L2-06 Perustelu kohtaan d) — the display-sized `\dfrac` inside a running sentence stretches the line; use `\tfrac` or a one-line `161\,\mu\text{T}\,\text{cm} : 0{,}50\,\text{cm}`.

## Checked
- Round 1 Blocking (L2-06 "poikkeavat toisistaan alle 2 %") is resolved: it now reads "poikkeavat keskiarvostaan 161 µT cm alle 2 %" (164 and 158 are 1,9 % from the mean), and a Perustelu for part d) was added (322 µT ≈ 320 µT).
- Captures L2-1280-7 and 8 (L2-05 end, L2-06 task and full solution) and L3-1280-5 (L3-04 Linearisointi, tan α table, B_h = 16 µT): rows aligned, no red KaTeX, no clipping.
- Recomputed L2-05 (μ0 = 1,26 µVs/(Am), l = 0,300 m now in task and solution), L2-06 (8,05 A; 54 µT; 322 µT), L3-04 (k = 0,313 1/A; B_h = 16 µT): all agree with answers and answers.py.
- L2-07 mallivastaus now covers the constant Earth-field term; L1-06 option rewording leaves the correct option unchanged. check_layout 360/768/1280 clean.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
