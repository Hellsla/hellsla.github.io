VERDICT: FAIL
CONTENT-HASH: aeaaf3875259f90a

## Blocking
- [Major] lesson.md, "Kaava: Energiatase", "Tehtävä etenee näin:" (about line 196) — the five-step procedure renders as one run-on paragraph ("…minne se menee. 2. Kirjoita… 3. Käy…"), seen at 1280 and 390 px (theory-1280-3, stage-selita-390-4). It is the known lint warning, but on the page the numbered steps cannot be told apart, and step 4 is long — a student cannot use it as a checklist — put a blank line between "Tehtävä etenee näin:" and "1." so it builds as an ordered list.

## Polish
- [Minor] lesson.md Esimerkki task — "0,80 m²" is plain text beside maths values (teacher's rule: number with unit is maths) — write $0{,}80\,\text{m}^2$.
- [Minor] Esimerkki "Tunnetut" — $UA$ written with `\text{m}^2\text{K}` (no dot), while the task and everywhere else says W/(m²·K); the task also has a stray `\text{}\cdot` — use `\cdot\text{K}` consistently.
- [Minor] Tutki stage — "Seinien $U$ / -arvon" breaks at the line end and the full stop after "$= 25\,\text{W}$" sits alone on its own line — put "-arvon" in the maths or reword ("U-arvon"), and move the stop inside.
- [Minor] fig 3 and fig 5 at 390 px — bar values and axis words are about 8–9 px; legible but small — consider larger label size.
- [Minor] Exit ticket heading is English ("Exit ticket") in the Finnish page — a template label, name it "Loppukysymykset" if that is allowed.

## Checked
- fig-1…5-390 (hero, Tutki graph, cooler, model graph, cooling circuit), intro-1280, top-390, fig-row.
- theory-1280-1…4; the worked example, all 7 stages at 390 px (my own capture, because example-390 shows only stage 1).
- stage-herata, ennusta (390 and open-1280), tutki 1–3, selita 1–4, sovella, tarkista 1–2 (390) and open-tarkista-1280-1…4.
- No simulation in this chapter. aria-labels of all 5 figures read from the built page; they match the pictures (3,7 h in the Tutki graph, 2,4 h in the theory graph).
- Figures: no clipping or overlap; arrows, colours (heat orange, temperature red, cold blue) and the filled bars fit the palette.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
