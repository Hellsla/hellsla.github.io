VERDICT: PASS
CONTENT-HASH: f7903aada0819615
SCOPE: delta round 2 (L2-09 tolerance and solution wording, L2-10 reasonableness check, answers.py comment)

## Blocking

(none)

## Polish

1. fy8-9-L2-09 — the two readings (380, 58) are still given in the task text, so the figure is not needed to answer (earlier polish 1, unchanged; optional): give only the background and let the student read the values.
2. solutions.md L2-09 "Kuvaajan lukeminen" — "Se erottaa tuloksen" has no clear referent; say what the 2 % margin separates: "Tämä tarkkuus erottaa tuloksen vielä taustaa vähentämättä saatavasta 73,7 s:sta."

## Checked

- L2-09 tolerance 0,02: answer 70,9 s accepts 69,5-72,3 s; the no-background result 73,7 s (3,9 % off) now falls outside "oikein", so the task's point counts. Corrects my earlier 73,9 s; 73,7 s verified.
- The solution's reading paragraph now honestly says the readings are approximate and why the margin is 2 %; the "wider tolerance" wording is gone.
- "\dfrac{375}{53}" replaces the colon (earlier polish 4 done), also in the no-background check.
- L2-10 check: 0,5^(1/5,0) = 0,871 each hour, 0,871^5 = 0,50 is exact and cleaner than 0,86^5 = 0,47; the 13 % decay figure matches.
- answers.py comment 70,85 -> 70,9 matches the solution and the json.
- Seven solution steps, level, figure and phone captures unchanged by the diff.
- Method: delta; hash unchanged at start and end.
