VERDICT: FAIL
CONTENT-HASH: c24ba5ae8d1c151a

## Blocking
- solutions.md:189 (L3-04, Vastaus) — A, wrong number. The text says the 33 m margin is "noin 0,8 s kahden auton yhteisellä lähestymisnopeudella (33 m : 40 m/s)". 40 m/s is the closing speed at the start. When the overtaking ends, the car is at 29 m/s, so the closing speed is 29 + 20 = 49 m/s and the margin is 33 m : 49 m/s ≈ 0,7 s. Fix: write "noin 0,7 s, koska ohituksen lopussa autot lähestyvät toisiaan nopeudella 29 m/s + 20 m/s = 49 m/s (33 m : 49 m/s)".

## Polish
- solutions.md:189 (L3-04) — The rounding reason "kolme merkitsevää numeroa, koska tulos on kahden kolminumeroisen summa" is weak. The limiting data (20 m/s, 1,5 m/s², 5,0 m) have two figures. Write "≈ 270 m (kaksi merkitsevää numeroa); välitulos 267 m". The tolerance already accepts both answers.
- solutions.md:170 (L2-07) — "A on koko ajan edellä" holds only until t = 12 s, when B catches up. That is outside the table. Write "A on edellä koko taulukon ajan (B saavuttaa A:n vasta hetkellä 12 s)". At :175, "kuten nopeuksissa" fits poorly, because the table speeds have three figures. Name 6,0 s instead.
- lessons/FY4/fy4-12/answers.py:33 — The comment says "52,5 m", but the line computes 52,46 m and solutions.md says 52,4 m. Change the comment to 52,4 m.
- exercises.json L2-05 — `kind` includes "graph", but the task uses only the table and asks for no graph. Either drop "graph" or ask for a sketch of the two lines. The plan's figure item "(t,v)-kuvaaja kahdesta autosta → etäisyys hetkellä t" is done as a table (L2-07). That is fine, but update docs/exercise-bank/FY4.md to match.
- exercises.json L1-06, last distractor — In the feedback, "Viivat voivat leikata, vaikka niiden kulmakertoimet ovat erisuuret" reads as if the slopes might also be equal. Straight lines that cross always have different slopes. Write "Leikkaavilla suorilla kulmakertoimet ovat aina erisuuret".

## Checked
- I recomputed all 18 numeric answers in one script with my own models: L2-06 with numpy roots, L2-07 by a numeric gap maximum, and L3-04 by a time-stepped overtaking. All agree with exercises.json and answers.py.
- L2-05: a least-squares fit gives t = 7,01 s, the same as the endpoint method (7,0 s). The solution names and justifies the extrapolation past 5 s.
- L2-06: the wrong t = 2,0 s is the maximum-lead moment (16 m), as the error explanation says.
- L3-04: t = 6,0 s, 147 m, d_min = 267 m, final speed 104 km/h > 80 km/h. Both start at 72 km/h, which is legal.
- L3-05: with v = 5,975 or 6,0 m/s, x = 52,1 or 52,5 m. Both are inside the 5 % tolerance. The car's speed is 52 km/h. With the 40 km/h limit, the car stops accelerating at τ = 5,6 s, before the pass, and the pass moves to about 56 m. That confirms "myöhemmin ja kauempana".
- The new MC items (L1-06, L1-08) each have exactly one correct option, and every distractor's feedback is right.
- Scope: everything is uniform or uniformly accelerated 1-D motion (FY4 central content), with no vectors and nothing beyond the lesson. No new task duplicates an existing one, and the levels fit.
- The L3-04 and L2-05 solution captures (1280 px) render without overflow.
- The hash was the same at the start and at the end.
