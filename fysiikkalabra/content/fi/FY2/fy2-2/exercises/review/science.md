VERDICT: FAIL
CONTENT-HASH: 7103b82e24297b4b
Mode: full
Round: 1

## Blocking
- content/fi/FY2/fy2-2/exercises/exercises.json:99 — (scope) L1-09 needs power, the watt and the kilowatt-hour, and the brief's lesson teaches none of them: it covers only the joule and the prefixes k, M, G, T and says that power comes "seuraavassa luvussa *Teho*". No other fy2-2 task uses W or kWh. A level-1 student cannot tell kW from kWh, or J/s from J, with what this chapter teaches, and every feedback (including 1 kWh = 1000 W · 3600 s) explains with concepts from the next chapter. The physics is right (exactly one correct option, every distractor really wrong, 3,6 MJ correct); the chapter is wrong. — Fix: move the task to the Teho chapter (fy2-3), where P = E : t and 1 kWh = 3,6 MJ belong, and give fy2-2 a YO-skill task on joule prefixes or energy conversion; or else the fy2-2 lesson must first introduce the watt and kWh.

## Polish
- content/fi/FY2/fy2-2/exercises/exercises.json:119 — "Sähköenergian yksikkö kirjoitetaan kertomalla" suggests kWh is only for electrical energy; write "Energian yksikkö kilowattitunti kirjoitetaan ...".
- solutions.md:149 (Periaate) — "Energia kertoo, kuinka paljon energiaa muuttuu" defines energy by itself. Write "Energian yksikkö kertoo energian määrän; se on joule tai sen kerrannainen".
- exercises.json:111 — "jouleina tai niiden kerrannaisina": kWh is not a prefix multiple of the joule. Write "jouleina tai muissa energian yksiköissä, kuten kWh".

## Checked
- Hash 7103b82e24297b4b at start and end; the only change since the PASS set is L1-09 (exercises.json, solutions.md), commit 18b454cd1.
- Recomputed 1 kWh = 1000 W · 3600 s = 3 600 000 J = 3,6 MJ; matches the feedback and solutions.md.
- Options: kW (power), J/s = W (power), kW/h (power per time, not energy), kWh (energy). Exactly one correct; each feedback gives the right reason.
- `answer` matches the option marked correct.
- No number in L1-09, so answers.py needs no line; the other tasks are unchanged from the PASS set.
