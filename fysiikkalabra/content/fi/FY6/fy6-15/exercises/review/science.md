VERDICT: PASS
CONTENT-HASH: 88b30325b9aedc30
SCOPE: delta added-exercise from c650c557cc001a60 base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-15/exercises/solutions.md (fy6-15-L2-08, Vastaus) — "kaksi merkitsevää numeroa kuten sulakkeen nimellisvirrassa" names a value that does not enter the calculation; the limiting data are the graph reading 4000 W (on a 1000 W gridline) and U = 230 V.

## Checked
- Hash 88b30325b9aedc30 at start and end; delta round 2: only fy6-15-L2-08 judged.
- Round-1 blocking item resolved: the task and the figure's alt text now say "esimerkkiaineisto", not "mitattu aineisto".
- Figure generator: steps 1000 / 3000 / 4000 / 2000 / 3500 W at 0–4 / 4–10 / 10–16 / 16–24 / 24–30 min, as the alt text and the solution's reading; maximum 4000 W on a gridline; no current or fuse limit drawn.
- Physics: the group's loads are in parallel at 230 V, so I = P : U (power factor about 1 as in the brief, C).
- Recomputed: I = 4000 W : 230 V = 17,39 A; answers.py agrees; tolerance 3 % covers the rounded 17 A (2,2 % off).
- Fuse statement right: P_max = 230 V · 16 A = 3680 W; only the 4000 W step exceeds it; "ei välttämättä laukea heti" agrees with the lesson's slow-overload remark.
- Solution complete: principle and reason, graph reading, formula before numbers, units, real check against 3680 W. Scope: FY6 sähköturvallisuus (sulake).
