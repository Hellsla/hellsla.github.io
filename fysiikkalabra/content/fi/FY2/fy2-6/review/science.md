VERDICT: PASS
CONTENT-HASH: 251c772de007ee67

## Blocking

## Polish
- inquiry.json tarkistus-3 model — "Kumpaakaan ei voi säätää nopeasti" is true only for raising wind output; a turbine can be curtailed in seconds, and nuclear can reduce output (lesson text says so) — say "tuulta ei voi lisätä tarpeen mukaan, ydinvoimaa ajetaan yleensä tasaisesti" (B, minor).
- inquiry.json data-viikko solution — "Sähköä ei voi varastoida verkkoon" is absolute; the lesson text hedges ("suuria määriä suoraan"). Use the same wording.
- lesson.md Suomen sähköntuotanto — text says "fossiilisten osuus muutama prosentti" but the bar (3,4 TWh) is fossil fuels and peat; write "fossiiliset polttoaineet ja turve".
- inquiry.json data-viikko — wind nominal "noin 8 GW" (Tuulivoimayhdistys 2024): not checkable offline; confirm the year-end figure (it may be nearer 9 GW) or word it as "noin".
- The 8760 h year ignores that 2024 was a leap year (8784 h); immaterial at this precision.

## Checked
- Recomputed all numbers (lesson-answers.py, example, check tasks, siirto): 1598 kW, 32 %, 2,31 GW, 14,0 TWh, 8,76 GWh, 8,4 GW, 320 turbines all correct; shares sum to 79,9.
- Bar and log-scale figures: bar lengths at 10,5 px/TWh and dot positions at 70 px/decade match values; 320x = 2,5 decades.
- Teacher brief 2026-10-29: classifications are properties, not categories (text, table intro, summary, check-ominaisuudet); hydro controllable yet rain-dependent; nuclear steady but can reduce (Olkiluoto example); peat clarified. Consistent across theory, options, feedback, exit ticket.
- All predictions/choices have exactly one correct option; distractor feedback is right (nuclear largest, hydro quick response).
- Scope: no FY3 content; no chain efficiencies.
