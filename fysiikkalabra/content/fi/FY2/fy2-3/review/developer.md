VERDICT: DONE

Round 2 fixes (all Blocking plus the listed Polish items).
- lesson.md: bar-figure aria-label now 80 W / 80 J; "30 vuorokautta" as $30\,\text{vrk}$; Esimerkki gains the snt to € conversion by substitution ($1\,\text{snt} = 0{,}01\,\text{€}$, rows 192 snt = 192 · 0,01 € = 1,92 €); "ovat annetut"; "Jouleina laskettaessa tunti on"; misconception now says "teho on 2 kWh" is wrong, 2 kW is right (replaces "kilowattitunti sekunnissa").
- inquiry.json: every number with a unit in prose or table cells is maths (ennuste-1 options, 60 s, 20 s, 24 h, 900 €, 365 vrk, 90 min; the mittari and aika table cells).
- exit-ticket.json: conversion by substitution $1\,\text{min} = 1\,\text{h} : 60$; "kuten lähtötiedot".
- lesson-answers.py: mistake value computed as 1200 / 90 (13,3).
Checked: check_lesson.py fy2-3 all ok. Not fixable here: glossary.json "teho" still holds P = W/t and P = Fv (FY3/FY4 content); flag to the glossary's owner.
