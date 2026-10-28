VERDICT: FAIL
CONTENT-HASH: 6d8061bd4d988520

Round 2: exit ticket 2 → 1 (the 0 K question removed), stage text "Lopuksi yksi". The diff itself is correct; one guardrail break outside it, missed in round 1, is reported below.

## Blocking
- inquiry.json:354 — (A, guardrail "Absolute zero", same error fixed in fy3-9 and fy3-10) check-c2 distractor feedback: "Celsiusasteikon nollakohta on valittu veden jäätymispisteeksi, ei tilaksi, jossa liike loppuu" implies a temperature (0 K) at which particle motion stops; the lesson (lesson.md:219) rightly says only that the mean kinetic energy is at its lowest. Fix: "…valittu veden jäätymispisteeksi, ei absoluuttiseksi nollapisteeksi."
## Polish
- none
## Checked
- Remaining exit question: heating at fixed volume → larger mean kinetic energy, faster particles, more frequent and harder wall hits → higher pressure; mechanism right.
- Count 1 matches "Lopuksi yksi"; the 0 K value stays in lesson.md:231.
- check-c2 numbers: 293,15/283,15 = 1,035 → +3,5 %.
