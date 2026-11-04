VERDICT: PASS
CONTENT-HASH: 321eee9838d818f2

Round 2 (delta review of round 1 fixes; round 1 hash c908c7c1c4a5b48e)

## Blocking (round 1) — verified
1. s5 b model answer and mistake line: fixed. The model answer now reasons with an estimate (needed ≈ 70 J/K vs a few J/K for the mug) and with the corrected value matching the table; the mistake line now penalises accepting the mug without estimating its heat capacity, which is the right misconception. Rubric `conclusion` (2 p) uses the same observable criterion. teacher.md's question on the mug remains consistent.

## Polish (round 1) — verified
2. aineisto: solution says the start point is read between gridlines (±1 °C); tolerance 0,07 accepts −15 and −17 °C readings (2222 and 1961 J/(kg·K), +6,7 % / −5,9 %).
3. Miksi quote is now a pure question ("Kumpi vie enemmän energiaa…") and no longer pre-empts Pohdinta.
4. s6 d: "pumppaustyö" removed from model answer, Periaate and rubric; only engine friction and the cooling system remain (FY1–FY8 content).
5. Units in the "missä" lists are LaTeX; preview shows no plain "(K)", "(kg)", "(°C)", "(1/K)".

## New problems
None. Task counts, points (15/15/20/15/15/15) and rubric sums are unchanged by the fixes.

## Checked
Sources diffed against round-1 findings; built fy9-lampo; opened all details at 390 and 1280 (no console or KaTeX errors).
