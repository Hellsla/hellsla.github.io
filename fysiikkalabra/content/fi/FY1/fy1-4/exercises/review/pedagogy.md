VERDICT: PASS
CONTENT-HASH: 40177a99521db833

## Blocking
(none)

## Polish
1. exercises.json fy1-4-L3-05 — the loivin suora (through 2 s and 5 s, slope 0,40 m/s) leaves the 6 s point 0,50 m above it and the 1 s point 0,25 m below, while the other residuals are 0,1 m or less. The text says the point set "mahtuu" this line, which a student who draws it will doubt. Fix: nudge the data so both lines stay within about 0,2 m of every point (e.g. 6 s: 3,20 m), or say "jyrkin ja loivin suora, jotka vielä kulkevat pisteiden joukon läpi".
2. exercises.json fy1-4-L3-05 — "Piirrä mittauspisteistä kuvaaja" is not needed for the answer: the task gives both lines' coordinates and the pupil's slopes, so the graph skill is only checked by the drawing. Fix: let the student find the two slopes themselves (drop the pupil's "0,55 ja 0,40") or keep the drawing and ask them to check the lines against it.
3. solutions.md fy1-4-L2-07 Periaate — "Kummassakin metallissa aine on tasalaatuista ja kappaleet ovat samaa ainetta" repeats itself. Fix: "Kummassakin metallissa kappaleet ovat samaa tasalaatuista ainetta, joten …".
4. solutions.md fy1-4-L3-04 Vastaus — "Lineaarinen malli pätee mitatuista pisteistä välillä 100–500 g, ja ekstrapoloiden …" is heavy for a 17-year-old. Fix: two sentences: "Malli pätee välillä 0–500 g. Pienemmillekin kuormille se pätee, koska suora kulkee likimain origon kautta."
5. Model graphs for the "Piirrä kuvaaja" tasks are still absent (known, deliberate this round); still the main remaining gap for self-checking.

## Checked
- L1-07 now says "saman metallin kappaleet", so the slope-as-density reading is valid; the solution adds why it holds only for one material, which repairs the mix-up with b.
- L2-05 "ripustettiin" and L2-07 wording ("Mitä kulmakerroin tässä kuvaajassa tarkoittaa, ja kumpi aine on tiheämpi?") are correct Finnish; question stays last.
- L2-07 solution's significant-figure reason now matches the data (three figures given, fit limits to two).
- L3-04 "kuormien väli" fixes the earlier ambiguity; "asettuvat" corrected; the overload reason (spring stretched beyond its elastic range, no longer proportional) is added.
- L3-05 is now a genuine error-analysis task: the table gives the data, the pupil's flawed solution (whole difference, 32 %) is quoted, and the solution names the error, gives 16 % and checks it against the 0,33–0,63 m/s interval.
- L3-05 numbers verified: slopes 0,55 and 0,40 m/s, mean 0,475, 0,075/0,475 = 15,8 %, pupil's 0,15/0,475 = 32 %; answers.py matches the key.
- Mix now includes error analysis; the spring context repeats (L1-08, L2-05, L3-04) but each asks something different.
- Counts 8/7/5 over the minimums; slot goals still all practised; no task repeats the kettle example.
