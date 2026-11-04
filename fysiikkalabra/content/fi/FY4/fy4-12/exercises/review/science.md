VERDICT: PASS
CONTENT-HASH: 140890ba59fc47db

## Blocking

## Polish
- solutions.md:189 (L3-04) — carried from round 1: "kolme merkitsevää numeroa, koska tulos on kahden kolminumeroisen summa" is weak; the limiting data (20 m/s, 1,5 m/s², 5,0 m) have two figures. — Write "≈ 270 m (kaksi merkitsevää numeroa); välitulos 267 m". The tolerance accepts both.
- solutions.md:170 (L2-07) — carried: "A on koko ajan edellä" holds only until t = 12 s, outside the table. — Write "A on edellä koko taulukon ajan (B saavuttaa A:n vasta hetkellä 12 s)". At :175, "kuten nopeuksissa" fits poorly (the table speeds have three figures); name 6,0 s instead.
- lessons/FY4/fy4-12/answers.py:33 — carried: the comment says "52,5 m", but the line computes 52,46 m and solutions.md says 52,4 m. — Change the comment to 52,4 m.
- exercises.json L2-05 — carried: `kind` includes "graph", but the task uses only the table. — Drop "graph" or ask for a sketch; update docs/exercise-bank/FY4.md where the plan's (t,v) figure item became the table task L2-07.
- exercises.json L1-06, last distractor feedback — carried: "Viivat voivat leikata, vaikka niiden kulmakertoimet ovat erisuuret" reads as if equal slopes were possible for crossing lines. — Write "Leikkaavilla suorilla kulmakertoimet ovat aina erisuuret".

## Checked
- Round 2. Round-1 Blocking item solutions.md:189 (L3-04, Vastaus) is resolved: the margin is now "ohituksen lopussa … noin 0,7 s … (33 m : 49 m/s)". Recomputed: closing speed at the end 29 m/s + 20 m/s = 49 m/s, 33 m : 49 m/s = 0,67 s ≈ 0,7 s.
- The rest of L3-04 is unchanged and still right: t = 6,0 s, s_h = 147 m, s_v = 120 m, d_min = 267 m, v = 29 m/s = 104 km/h > 80 km/h; Mallivastaus "+24 km/h" agrees.
- No other file in the set changed, so the round-1 recomputation of all 18 answers still holds.
- MC items L1-06, L1-08: exactly one correct option each, as in round 1.
- Scope, levels and plan unchanged since round 1.
- The hash was the same at the start and at the end.
