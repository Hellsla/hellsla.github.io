VERDICT: PASS
CONTENT-HASH: d311cb11b332d994

Round 2. Full review of the 20-task set (8/7/5) after the round-1 fixes (`git diff HEAD~1`); focus on new L1-06..08, L2-05..07, L3-04..05.

## Blocking

## Polish
- solutions.md L2-06 Vastaus a) — "tulos kertoo vain, kumpaa lähimpänä taulukon kerroin on" is garbled; e.g. "kolmas numero ei muuta johtopäätöstä: tulos riittää kertomaan, minkä taulukon metallin kerrointa se on lähimpänä".
- solutions.md L2-07 c), L3-05 a) — the new "käytännössä noin 10 m / 76 mm" sentences are right; the answer box still holds 10.4 and 75.9 with tolerance 0.03, which is fine, but the Vastaus could lead with the rounded value.
- L1-07 — "heikot vuorovaikutukset" is a fair level-1 simplification (C); the added "vakiopaineessa kaasu saa laajentua vapaasti" covers the round-1 note.

## Checked
- Round-1 Blocking (L2-07 b, mittausvirhe vs mittausepävarmuus) resolved: solutions.md now says "mittausepävarmuus voisi olla yli puolet tuloksesta (52 %)" and "suhteellista epävarmuutta".
- Round-1 Polish resolved: L2-06 b uses the guardrail sentence and a fitted line (free least-squares slope 22,90 · 10⁻⁶ 1/K, same as end points); L3-04 a Vastaus "13,2 mm, käytännössä 13 mm" matches the answer 13.2; "Taulukon lukeminen" headings; L2-07 c and L3-05 a justify the digits.
- All numeric answers recomputed in one script: agree with answers.py and exercises.json (L1-08 2,3 mm; L2-05 45,0 · 10⁻⁶; L2-06 22,9; L2-07 0,96 mm, ratio 52 %, 10,4 m; L3-04 13,2 / 18,0 / 25,2 mm; L3-05 A 0,283 mm², 75,9 mm, 77,8 mm, +2,5 %, water 12,9 mm).
- L1-06 reordered and reworded options (teräs/lasi): exactly one correct, feedback right (12 > 9 · 10⁻⁶ 1/K); L1-07 ratios 16 and 94 ("noin 90") right.
- L1-08 "(yksiköt jätetty pois)" makes clear that the student's error is 65 instead of ΔT = 50 K.
- L2-05 restructure (Mallivastaus c moved into Vastaus) keeps the 4 °C, negative-γ and lake reasoning correct.
- Scope inside FY3 lämpölaajeneminen; levels and kinds fit the plan; every new task has a complete solution, symbolic before substitution.
- Hash unchanged at start and end.
