VERDICT: FAIL
CONTENT-HASH: 704ca126f528bedf

## Blocking
- lesson.md:155 — "'kilowattitunti sekunnissa' ei ole teho" is physically wrong: energy per time is a power (1 kWh/s = 3,6 MW). — Use a real mix-up instead: "teho on 2 kWh" is wrong; it is 2 kW.
- lesson.md:10 (bar figure aria-label) — it says "televisio 100 W … 100 J", but the figure, table and graph use 80 W. — Write 80 W and 80 J.
- lesson.md:142–148 (Esimerkki) — 192 snt becomes 1,9 € with no conversion shown (teacher rule: conversion by substitution). — Add $192\,\text{snt} = 192 \cdot 0{,}01\,\text{€} = 1{,}92\,\text{€}$.
- exit-ticket.json:12 — "$1095\,\text{min} = 18{,}25\,\text{h}$" is not a conversion by substitution. — Substitute $1\,\text{min} = \tfrac{1}{60}\,\text{h}$.
- Numbers with units are plain prose (teacher's all-LaTeX rule) at lesson.md:108 and 112 ("30 vuorokautta"), and at inquiry.json:61, 66, 85, 88, 126, 195, 205, 221, 224 and 259 ("15 tuntia", "60 sekunnissa", "900 euroa", "365 vuorokautta", "90 minuutin" …). The table cells at inquiry.json:78 and 106 are plain numbers too. — Put each in $…$.

## Polish
- exit-ticket.json:12 — "kuten tehot 5,0 W ja 3,0 min": 3,0 min is not a power. — Write "kuten lähtötiedot".
- lesson-answers.py, `inq-check2-ilman-muunnosta` — it computes 1,2 : 90 = 0,0133, but the mistake value in inquiry.json:274 is 13,3. — Compute 1200 / 90.
- glossary.json "teho" (shown with this lesson) contains P = W/t and P = Fv, which are FY3/FY4 content. This is not a lesson file; flag it to the glossary's owner.

## Checked
- I recomputed every lesson, inquiry and exit-ticket number in one script. All are correct, and so are the correct options and the feedback numbers.
- Both figures are to scale: the graph slopes are 2000, 1000 and 80 W, and the bars are 400 : 200 : 16 px.
- Olkiluoto 3 is about 1600 MW electrical, verified in TVO's 2022 release.
- The Tilastokeskus 2025 figure "noin 18 snt/kWh" agrees with table 13rb (17,6 snt/kWh, found in round 1; the API was unreachable this round). 20 snt/kWh is labelled as an example price.
- All round-1 blockers are fixed.
- Scope is FY2. There is no ×, and written divisions use a colon.
